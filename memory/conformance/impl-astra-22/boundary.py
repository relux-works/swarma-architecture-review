"""Synthetic delivery checks over immutable captured views; no external sending."""

import copy

from evaluator import Refusal
from transactions import key, receipt, json_values, timestamp


class Boundary:
    def __init__(self, adapter):
        self.adapter = adapter

    def apply(self, op):
        from transactions import Transactions
        if self.adapter.writer is None:
            self.adapter.writer = Transactions(self.adapter)
        shapes = self.adapter.writer.shapes
        json_values(op)
        if not shapes.valid(op, shapes.vector["properties"]["operations"]["items"]):
            raise Refusal("invalid_shape")
        timestamp(op["at"])
        if op["op"] == "revoke_declassification":
            decision = next((d for d in self.adapter.policy["declassification_decisions"] if d["ref"] == op["decision"]), None)
            if decision is None or decision["owner"] != op["actor"]:
                raise Refusal("not_authorized")
            revoked = self.adapter.runtime["revoked_declassifications"]
            if op["decision"] not in revoked:
                revoked.append(copy.deepcopy(op["decision"]))
                revoked.sort(key=lambda r: (r["id"], r["version"]))
            return receipt("revoke_declassification", "revoked")
        if op["op"] == "revoke":
            if op["actor"] != self.adapter.policy["owner"]:
                raise Refusal("not_authorized")
            event = {k: op[k] for k in ("principal", "audience", "purpose", "right", "at")}
            event["owner"] = op["actor"]
            if event not in self.adapter.runtime["revocations"]:
                self.adapter.runtime["revocations"].append(event)
            return receipt("revoke", "revoked")
        if op["op"] == "deliver":
            return self.deliver(op)
        raise Refusal("unsupported_operation")

    def deliver(self, op):
        saved = self.adapter.captures.get(op["view_operation"])
        if saved is None or saved["view"]["type"] != "view":
            raise Refusal("not_authorized")
        prepared = saved["query"]
        if (op["actor"] != prepared["principal"] or op["audience"] != prepared["audience"]
                or op["purpose"] != prepared["purpose"]
                or self.adapter.rules[key(prepared["projection_rule"])]["family"] != "audience_projection"):
            raise Refusal("not_authorized")
        if (prepared["policy"] != self.adapter.policy["revision"]
                or prepared["evidence_policy"] != self.adapter.policy["evidence"]["ref"]
                or self.adapter.runtime["restore"]["status"] != "open"):
            raise Refusal("disclosure_revoked")
        selected = saved["selected"]
        query = copy.deepcopy(prepared)
        query.update(now=op["at"], kind="recall", since=None)
        query["scope"]["targets"] = copy.deepcopy(selected)
        query["cut"] = {"memory": self.adapter.runtime["memory_cut"],
                        "sources": copy.deepcopy(self.adapter.runtime["source_cuts"])}
        fenced = {key(r) for r in self.adapter.runtime["erased"] + self.adapter.runtime["fences"]}
        for reference in selected:
            record = self.adapter.records.get(key(reference))
            if (record is None or key(reference) in fenced or record["envelope"]["lineage"] == "unknown"
                    or not all(self.adapter.granted(record, query, right) for right in ("read", "use", "forward"))):
                raise Refusal("disclosure_revoked")
        # An empty prepared projection never silently acquires later items.
        if not selected:
            return receipt("deliver", "delivered")
        current_binding = {}
        current = self.adapter.query(query, binding=current_binding)
        if current["type"] != "view" or current_binding["selected"] != selected:
            raise Refusal("disclosure_revoked")
        for item in current["items"]:
            if (item["currentness"] in {"historical", "last_received"}
                    or any(item[sign]["freshness"] == "stale" for sign in ("support", "oppose"))):
                raise Refusal("publication_stale")
        return receipt("deliver", "delivered")
