"""Exact structured releases; retained evidence is never live authorization."""

import copy
import hashlib

from evaluator import Refusal, canonical
from transactions import key, ref


class Releases:
    def __init__(self, adapter):
        self.adapter = adapter

    def inputs(self, record):
        facts = [f for f in self.adapter.policy["lineage_facts"] if f["output"] == ref(record)]
        if len(facts) != 1 or not facts[0]["complete"] or record["envelope"]["lineage"] == "unknown":
            raise Refusal("declassification_invalid")
        return facts[0]["inputs"]

    def closure(self, output, state):
        seen, result = set(), []

        def visit(reference):
            k = key(reference)
            if k in seen:
                return
            seen.add(k)
            if k not in state:
                raise Refusal("declassification_invalid")
            record = state[k]
            result.append(record)
            for parent in self.inputs(record):
                visit(parent)
        for reference in self.inputs(output):
            visit(reference)
        return result

    def validate(self, output, state):
        e = output["envelope"]
        citations = e["disclosure"]["declassification"]
        inputs = self.inputs(output)
        if not citations or e["lineage"] != inputs:
            raise Refusal("declassification_invalid")
        evidence = self.adapter.policy["evidence"]
        decisions = {key(d["ref"]): d for d in self.adapter.policy["declassification_decisions"]}
        revoked = {key(r) for r in self.adapter.runtime["revoked_declassifications"]}
        owners, common = set(), None
        for citation in citations:
            assessment = state.get(key(citation))
            if assessment is None or assessment["envelope"]["kind"] != "assessment":
                raise Refusal("declassification_invalid")
            b = assessment["body"]
            release = b["declassification"]
            if (b["check_kind"] != "declassification" or b["result"] != "pass"
                    or b["executor"] not in {"human", "deterministic"} or release is None
                    or b["pins"]["subject"] != ref(output)
                    or b["pins"]["policy"] != evidence["policy_pin"]
                    or b["pins"]["environment"] != evidence["environment_pin"]):
                raise Refusal("declassification_invalid")
            pins = {k: v for k, v in release.items() if k != "decision"}
            decision = decisions.get(key(release["decision"]))
            if (decision is None or not decision["active"] or key(release["decision"]) in revoked
                    or decision["owner"] != assessment["envelope"]["issuer"] or decision["pins"] != pins
                    or pins["inputs"] != inputs or pins["output_schema"] != e["schema"]
                    or pins["output_digest"] != hashlib.sha256(canonical(output["body"])).hexdigest()
                    or common is not None and pins != common):
                raise Refusal("declassification_invalid")
            common = pins
            owners.add(decision["owner"])
        assignments = {key(c["input"]): c["owners"] for c in self.adapter.policy["constraint_owners"]}
        for record in self.closure(output, state):
            disclosure = record["envelope"]["disclosure"]
            lifted = (common["audience"] not in disclosure["audiences"]
                      or common["purpose"] not in disclosure["purposes"]
                      or not set(disclosure["field_classes"]) <= set(e["disclosure"]["field_classes"]))
            required = assignments.get(key(ref(record)), [self.adapter.policy["owner"]])
            if lifted and not set(required) <= owners:
                raise Refusal("declassification_invalid")
        return common

    def effective(self, record, query):
        """Recompute fallback constraints without changing immutable records."""
        if not record["envelope"]["disclosure"]["declassification"]:
            return record["envelope"]["disclosure"]
        from transactions import Transactions
        writer = self.adapter.writer or Transactions(self.adapter)
        ordinary = copy.deepcopy(record)
        writer.inherit(ordinary, writer.known_inputs(record), self.adapter.records)
        if ordinary["envelope"]["kind"] == "assertion":
            writer.assertion(ordinary)
        fallback = ordinary["envelope"]["disclosure"]
        try:
            pins = self.validate(record, self.adapter.records)
        except Refusal:
            return fallback
        if query["audience"] != pins["audience"] or query["purpose"] != pins["purpose"]:
            return fallback
        result = copy.deepcopy(record["envelope"]["disclosure"])
        result["retain_until"] = fallback["retain_until"]
        return result
