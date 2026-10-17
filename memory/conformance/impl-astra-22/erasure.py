"""Semantic custody/fence transitions; no store or external actor is controlled."""

import copy

from evaluator import Refusal, canonical
from transactions import Transactions, json_values, key, receipt, ref, timestamp


def ordered(references):
    return sorted({key(r): copy.deepcopy(r) for r in references}.values(),
                  key=lambda r: (r["id"], r["version"]))


class Erasure:
    def __init__(self, adapter):
        self.adapter = adapter
        self.writer = adapter.writer or Transactions(adapter)

    def apply(self, operation):
        op = copy.deepcopy(operation)
        json_values(op)
        if not self.writer.shapes.valid(op, self.writer.shapes.vector["properties"]["operations"]["items"]):
            raise Refusal("invalid_shape")
        mode = op["op"]
        if mode == "erase":
            return self.erase(op)
        if mode in {"restore", "reconcile_restore", "set_availability", "control"}:
            if op["actor"] != self.adapter.policy["owner"]:
                raise Refusal("not_authorized")
            timestamp(op["at"])
        if mode in {"restore", "reconcile_restore"}:
            return self.restore(op)
        if mode == "load":
            self.adapter.runtime["hidden_work"] = op["hidden_work"]
            return receipt(mode, "proceeded")
        if mode == "set_availability":
            if self.adapter.policy["availability_disclosure"] != "coarse_unavailable":
                raise Refusal("not_authorized")
            self.adapter.runtime["memory_available"] = op["state"] == "available"
            return receipt(mode, "availability_changed")
        if mode == "control":
            self.adapter.runtime["control_observations"].append(op["action"])
            return receipt(mode, "proceeded")
        raise Refusal("unsupported_operation")

    def closure(self, targets):
        """Only admitted outputs participate, including known unknown-lineage inputs."""
        affected = {key(r) for r in targets}
        while True:
            previous = set(affected)
            for identity, record in self.adapter.records.items():
                if any(key(r) in affected for r in self.writer.known_inputs(record)):
                    affected.add(identity)
            if affected == previous:
                break
        return affected

    def metadata_allowed(self, reference, op):
        from releases import Releases
        record = self.adapter.records.get(key(reference))
        if record is None:
            return False
        scope = op["receipt_context"] | {"principal": op["actor"]}
        disclosure = Releases(self.adapter).effective(record, scope)
        return (all(self.adapter.granted(record, scope, right) for right in ("read", "use"))
                and scope["audience"] in disclosure["audiences"]
                and scope["purpose"] in disclosure["purposes"])

    def erase(self, op):
        policy = self.adapter.policy
        known = [self.adapter.records[key(r)] for r in op["targets"] if key(r) in self.adapter.records]
        spaces = {r["envelope"]["space"] for r in known}
        if op["actor"] != policy["owner"] or not any(
                g["principal"] == op["actor"] and "erase" in g["rights"] for g in policy["grants"]):
            raise Refusal("not_authorized")
        if any(not any(g["principal"] == op["actor"] and g["space"] == space and "erase" in g["rights"]
                       for g in policy["grants"]) for space in spaces):
            raise Refusal("not_authorized")
        if len(spaces) > 1:
            raise Refusal("cross_scope")
        if not op["targets"] or len(known) != len(op["targets"]):
            raise Refusal("invalid_reference")
        space = next(iter(spaces))
        identity = (op["actor"], space, op["idempotency_key"])
        intent = copy.deepcopy(op)
        del intent["idempotency_key"], intent["at"]
        digest = canonical(intent)
        if identity in self.writer.idempotency:
            old_digest, old_receipt = self.writer.idempotency[identity]
            if not all(self.metadata_allowed(r, op) for r in old_receipt["refs"]):
                raise Refusal("not_authorized")
            if old_digest != digest:
                raise Refusal("idempotency_conflict")
            return copy.deepcopy(old_receipt)
        timestamp(op["at"])
        affected = self.closure(op["targets"])
        references = ordered(ref(self.adapter.records[k]) for k in affected)
        disclosed = [r for r in references if self.metadata_allowed(r, op)]
        runtime = copy.deepcopy(self.adapter.runtime)
        runtime["erasure_generation"] += 1
        runtime["erased"] = ordered(runtime["erased"] + references)
        runtime["fences"] = ordered(runtime["fences"] + references)
        accounted, complete = [], True
        for entry in runtime["custody"]:
            if not entry["controlled"] or not any(key(r) in affected for r in entry["inputs"]):
                continue
            if entry["id"] not in op["boundary"] or not entry["reachable"]:
                complete = False
                continue
            entry["present"] = False
            accounted.append(entry["id"])
        result = receipt("erase", "purged" if complete else "incomplete", disclosed)
        result.update(custody=sorted(accounted),
                      erasure_status="purged_within_boundary" if complete else "purge_pending")
        runtime["idempotency"].append({"actor": op["actor"], "space": space,
                                       "key": op["idempotency_key"],
                                       "canonical_request": digest.decode("utf-8"),
                                       "receipt": copy.deepcopy(result)})
        self.adapter.runtime = runtime
        return result

    def restore(self, op):
        if any(key(r) not in self.adapter.records for r in op["obligations"]):
            raise Refusal("invalid_reference")
        runtime = copy.deepcopy(self.adapter.runtime)
        obligations = ordered(runtime["erased"] + runtime["fences"]
                              + runtime["restore"]["obligations"] + op["obligations"])
        if op["op"] == "restore":
            if op["restore_cut"] != self.adapter.backup["memory_cut"]:
                raise Refusal("invalid_time")
            # Restore storage presence, never old policy, generations, receipts
            # or the authority to read. Keep current reachability facts.
            present = {c["id"] for c in self.adapter.backup["custody"] if c["present"]}
            for entry in runtime["custody"]:
                if entry["id"] in present:
                    entry["present"] = True
            runtime["restore"] = {"status": "fenced", "external_witness": op["external_witness"],
                                  "obligations": obligations}
            result = receipt("restore", "fenced")
            result["erasure_status"] = "access_closed"
        else:
            if not op["external_witness"]:
                raise Refusal("erasure_incomplete")
            affected = self.closure(obligations)
            accounted = []
            for entry in runtime["custody"]:
                if not entry["controlled"] or not any(key(r) in affected for r in entry["inputs"]):
                    continue
                if not entry["reachable"]:
                    raise Refusal("erasure_incomplete")
                entry["present"] = False
                accounted.append(entry["id"])
            references = ordered(ref(self.adapter.records[k]) for k in affected)
            if affected - {key(r) for r in runtime["erased"]}:
                runtime["erasure_generation"] += 1
            runtime["erased"] = ordered(runtime["erased"] + references)
            runtime["fences"] = ordered(runtime["fences"] + references)
            runtime["restore"] = {"status": "open", "external_witness": True, "obligations": references}
            result = receipt("reconcile_restore", "reconciled")
            result.update(custody=sorted(accounted), erasure_status="purged_within_boundary")
        self.adapter.runtime = runtime
        return result
