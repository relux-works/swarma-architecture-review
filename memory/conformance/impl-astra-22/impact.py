"""Registered impact traversal, distinct from evidence witness evaluation."""

import copy

from evaluator import Memory, applicable
from transactions import key, ref


def dependencies(record):
    return [key(p["source"] if p["kind"] == "source" else p["literal"]["assertion"])
            for p in record["body"]["premises"]]


def retired(records, cut, eligible):
    result = set()
    for k, record in records.items():
        e, b = record["envelope"], record["body"]
        if e["kind"] != "revision" or e["recorded"]["sequence"] > cut or not eligible(k, cut):
            continue
        target = key(b["target"])
        if b["relation"] == "withdraw" or (b["relation"] in {"replace", "correct"}
                                           and records[target]["envelope"]["kind"] != "assertion"):
            result.add(target)
    return result


def closure(edges, seeds, review_only=False):
    reached = set(seeds)
    review = set()
    while True:
        before = (set(reached), set(review))
        for target, inputs, is_review in edges:
            if reached.intersection(inputs):
                reached.add(target)
                if is_review or review.intersection(inputs):
                    review.add(target)
        if before == (reached, review):
            return review if review_only else reached - set(seeds)


def global_dependents(records, revision):
    """Protected invalidation inventory uses registered edges before the write."""
    cut = revision["envelope"]["recorded"]["sequence"] - 1
    available = lambda k, c: records[k]["envelope"]["recorded"]["sequence"] <= c
    withdrawn = retired(records, cut, available)
    edges = []
    for k, record in records.items():
        if (record["envelope"]["kind"] == "justification" and available(k, cut) and k not in withdrawn
                and record["body"]["role"] in {"sufficient_support", "review_on_change"}):
            edges.append((key(record["body"]["target"]["assertion"]), dependencies(record),
                          record["body"]["role"] == "review_on_change"))
    return closure(edges, {key(revision["body"]["target"])})


class Impact:
    def __init__(self, records, normalized, runtime, query):
        self.records, self.runtime, self.query = records, runtime, query
        # Reconstruct registration time independently of later withdrawals. The
        # current normalized scope/rights/erasure decisions still constrain it.
        self.base = copy.deepcopy(normalized)
        for record in self.base.values():
            record.pop("withdrawn_at", None)

    def eligible(self, k, cut):
        return k in self.base and applicable(self.base[k], self.query | {"cut": cut})

    def edges(self, cut, allow_retired_inputs=False):
        withdrawn = retired(self.records, cut, self.eligible)
        result = []
        for k, record in self.records.items():
            b = record["body"]
            if (record["envelope"]["kind"] != "justification"
                    or b["role"] not in {"sufficient_support", "review_on_change"}
                    or k in withdrawn or not self.eligible(k, cut)):
                continue
            target, inputs = key(b["target"]["assertion"]), dependencies(record)
            needed = [target] + inputs + ([key(b["check"])] if b["check"] else [])
            if not all(self.eligible(x, cut) for x in needed):
                continue
            if target in withdrawn or (b["check"] and key(b["check"]) in withdrawn):
                continue
            if not allow_retired_inputs and withdrawn.intersection(inputs):
                continue
            result.append((target, inputs, b["role"] == "review_on_change"))
        return result

    def affected(self):
        dirty = {key(r) for r in self.runtime["dirty"]}
        result, cache = set(), {}
        for cause in self.runtime["dirty_causes"]:
            target, revision_key = key(cause["assertion"]), key(cause["revision"])
            if target not in dirty or not self.eligible(revision_key, self.query["cut"]):
                continue
            revision = self.records[revision_key]
            changed = key(revision["body"]["target"])
            cut = revision["envelope"]["recorded"]["sequence"] - 1
            if not self.eligible(changed, cut):
                continue
            if revision_key not in cache:
                cache[revision_key] = closure(self.edges(cut), {changed})
            if target in cache[revision_key] and self.eligible(target, self.query["cut"]):
                result.add(target)
        return result

    def review(self, affected, assertions):
        old = set(Memory(assertions).project(self.query)["historical"])
        old.update(retired(self.records, self.query["cut"], self.eligible))
        return set(affected) | closure(self.edges(self.query["cut"], allow_retired_inputs=True),
                                       old, review_only=True)
