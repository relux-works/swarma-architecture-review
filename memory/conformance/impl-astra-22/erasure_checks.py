"""Synthetic erasure boundaries and recovery; no physical deletion claim."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter
from evaluator import Refusal
from transactions import Transactions, key, ref


BASE = Path(__file__).resolve().parent
NOW = "2026-10-17T00:00:00Z"


def fixture(name):
    return json.loads((BASE.parents[1] / "spec/kernel/vectors/semantic" / (name + ".json")).read_text())


def snapshot(adapter):
    return copy.deepcopy((adapter.records, adapter.runtime, adapter.policy, adapter.captures))


class ErasureControls(unittest.TestCase):
    def apply(self, adapter, op):
        from erasure import Erasure
        return Erasure(adapter).apply(copy.deepcopy(op))

    def denied(self, adapter, op, code):
        before = snapshot(adapter)
        with self.assertRaisesRegex(Refusal, "^" + code + "$"):
            self.apply(adapter, op)
        self.assertEqual(snapshot(adapter), before)

    # Exact receipt replay preserves its handle, cut, generation and inventory;
    # changed receipt scope conflicts and later read revocation blocks replay.
    def test_receipt_replay_and_current_authority(self):
        from boundary import Boundary
        v = fixture("P08")
        a = Adapter(v["initial_state"], "control")
        first = self.apply(a, v["operations"][0])
        self.assertEqual(first["refs"], [{"id": "rec:sensitive", "version": 1}])
        self.assertEqual(a.runtime["erasure_generation"], 1)
        state = snapshot(a)
        replay = copy.deepcopy(v["operations"][1])
        replay["at"] = "2026-10-18T00:00:00Z"
        self.assertEqual(self.apply(a, replay), first)
        self.assertEqual(snapshot(a), state)
        self.denied(a, v["operations"][2], "idempotency_conflict")
        full = self.apply(a, v["operations"][3])
        self.assertEqual(len(full["refs"]), 2)
        self.assertEqual(a.runtime["erasure_generation"], 2)
        Boundary(a).apply(v["operations"][4])
        self.denied(a, v["operations"][5], "not_authorized")
        self.assertEqual(a.runtime["idempotency"][-1]["receipt"], full)

    # A different audience/purpose is a key conflict even without metadata in
    # that new scope; current erase authority still precedes the conflict.
    def test_changed_context_before_replay_metadata(self):
        for dimension in ("audience", "purpose"):
            with self.subTest(dimension=dimension):
                v = fixture("S20")
                a = Adapter(v["initial_state"], "control")
                original = v["operations"][1]
                first = self.apply(a, original)
                self.assertEqual(len(first["refs"]), 2)
                self.assertEqual(self.apply(a, original), first)
                changed = copy.deepcopy(original)
                changed["receipt_context"][dimension] += ":ungranted"
                fresh = copy.deepcopy(changed)
                fresh["idempotency_key"] = "key:new-context"
                fresh_receipt = self.apply(a, fresh)
                self.assertEqual((fresh_receipt["outcome"], fresh_receipt["refs"]), ("purged", []))
                self.denied(a, changed, "idempotency_conflict")
                self.assertEqual(a.runtime["idempotency"][0]["receipt"], first)
                for grant in a.policy["grants"]:
                    grant["rights"].remove("erase")
                self.denied(a, changed, "not_authorized")
                self.denied(a, original, "not_authorized")

    # Current read/use/metadata loss blocks only the exact stored-ref replay;
    # fresh empty-ref erasure and changed-intent conflict remain distinct.
    def test_replay_metadata_loss_and_changed_intent(self):
        for missing in ("read", "use", "metadata"):
            with self.subTest(missing=missing):
                v = fixture("S20")
                a = Adapter(v["initial_state"], "control")
                original = v["operations"][1]
                first = self.apply(a, original)
                for grant in a.policy["grants"]:
                    if grant["audience"] == "aud:private" and grant["purpose"] == "purpose:read":
                        if missing == "metadata":
                            grant["metadata"] = False
                        else:
                            grant["rights"].remove(missing)
                self.denied(a, original, "not_authorized")
                fresh = copy.deepcopy(original)
                fresh["idempotency_key"] = "key:without-metadata"
                fresh_receipt = self.apply(a, fresh)
                self.assertEqual((fresh_receipt["outcome"], fresh_receipt["refs"]), ("purged", []))
                changed = copy.deepcopy(original)
                changed["receipt_context"]["purpose"] += ":ungranted"
                self.denied(a, changed, "idempotency_conflict")
                self.assertEqual(a.runtime["idempotency"][0]["receipt"], first)

    # Broader metadata rights cannot expand a stored empty receipt on replay;
    # its empty refs also cannot bypass later loss of erase operation authority.
    def test_empty_receipt_replay_stays_immutable(self):
        v = fixture("S20")
        a = Adapter(v["initial_state"], "control")
        grants = [g for g in a.policy["grants"] if g["audience"] == "aud:private" and g["purpose"] == "purpose:read"]
        for grant in grants:
            grant["metadata"] = False
        original = v["operations"][1]
        first = self.apply(a, original)
        self.assertEqual(first["refs"], [])
        for grant in grants:
            grant["metadata"] = True
        before = snapshot(a)
        self.assertEqual(self.apply(a, original), first)
        self.assertEqual(snapshot(a), before)
        fresh = copy.deepcopy(original)
        fresh["idempotency_key"] = "key:broader-metadata"
        self.assertEqual(len(self.apply(a, fresh)["refs"]), 2)
        for grant in a.policy["grants"]:
            grant["rights"].remove("erase")
        self.denied(a, original, "not_authorized")

    # Removing read/use or metadata for the exact receipt scope hides refs, but
    # does not spare any payload, generation or protected closure from erasure.
    def test_receipt_metadata_does_not_reduce_purge(self):
        for missing in ("read", "use", "metadata", "audience", "purpose"):
            with self.subTest(missing=missing):
                v = fixture("S20")
                for grant in v["initial_state"]["policy"]["grants"]:
                    if grant["audience"] == "aud:private" and grant["purpose"] == "purpose:read":
                        if missing in ("read", "use"):
                            grant["rights"].remove(missing)
                        elif missing == "metadata":
                            grant["metadata"] = False
                        else:
                            grant[missing] += ":other"
                a = Adapter(v["initial_state"], "control")
                result = self.apply(a, v["operations"][1])
                self.assertEqual(result["refs"], [])
                self.assertEqual(result["outcome"], "purged")
                self.assertEqual(len(a.runtime["erased"]), 2)
                self.assertTrue(all(not c["present"] for c in a.runtime["custody"]))
                self.assertEqual(a.runtime["memory_cut"], 100)

    # Owner/operation authority, required context, exact references and valid
    # time are required before any fence, receipt or partial custody mutation.
    def test_invalid_and_unauthorized_are_atomic(self):
        v = fixture("S20")
        for change, code in (("owner", "not_authorized"), ("right", "not_authorized"),
                             ("context", "invalid_shape"), ("target", "invalid_reference"),
                             ("time", "invalid_time")):
            with self.subTest(change=change):
                a = Adapter(v["initial_state"], "control")
                op = copy.deepcopy(v["operations"][1])
                if change == "owner":
                    op["actor"] = "other:actor"
                elif change == "right":
                    for grant in a.policy["grants"]:
                        grant["rights"].remove("erase")
                elif change == "context":
                    del op["receipt_context"]
                elif change == "target":
                    op["targets"][0]["id"] = "absent:record"
                else:
                    op["at"] = "2026-02-31T00:00:00Z"
                self.denied(a, op, code)
        a = Adapter(v["initial_state"], "control")
        self.assertEqual(self.apply(a, v["operations"][1])["outcome"], "purged")

    # Omitted/unreachable controlled sinks remain pending. A new key can finish;
    # an independent recipient remains present and is never reported as purged.
    def test_partial_unreachable_and_independent_custody(self):
        v = fixture("S20")
        v["initial_state"]["runtime"]["custody"].append({
            "id": "custody:independent", "inputs": [{"id": "rec:summary", "version": 1}],
            "kind": "export", "controlled": False, "reachable": True, "present": True})
        a = Adapter(v["initial_state"], "control")
        first = self.apply(a, v["operations"][0])
        self.assertEqual((first["outcome"], first["custody"]), ("incomplete", ["custody:payload"]))
        embedding = next(c for c in a.runtime["custody"] if c["id"] == "custody:embedding")
        embedding["reachable"] = False
        op = copy.deepcopy(v["operations"][1])
        op["boundary"].append("custody:independent")
        pending = self.apply(a, op)
        self.assertEqual(pending["outcome"], "incomplete")
        self.assertEqual(pending["custody"], ["custody:payload"])
        next(c for c in a.runtime["custody"] if c["id"] == "custody:embedding")["reachable"] = True
        op["idempotency_key"] = "key:reachable"
        done = self.apply(a, op)
        self.assertEqual(done["outcome"], "purged")
        self.assertEqual(done["custody"], ["custody:embedding", "custody:payload"])
        self.assertEqual([c["id"] for c in a.runtime["custody"] if c["present"]], ["custody:independent"])

    # Incomplete integration facts supply a real erasure lower bound; future
    # proposal facts and independent records do not become admitted tombstones.
    def test_unknown_lineage_and_future_fact_boundary(self):
        path = BASE.parents[1] / "conformance/cases/astra-25-unknown-lineage-erasure.vector.json"
        v = json.loads(path.read_text())
        a = Adapter(v["initial_state"], "control")
        result = self.apply(a, v["operations"][0])
        self.assertEqual(result["refs"], [{"id": "rec:a", "version": 1}, {"id": "rec:unknown", "version": 1}])
        self.assertEqual(a.runtime["erased"], result["refs"])
        self.assertNotIn(key({"id": "rec:derived", "version": 1}), a.records)
        before = snapshot(a)
        with self.assertRaisesRegex(Refusal, "^erasure_fenced$"):
            Transactions(a).apply(v["operations"][1])
        self.assertEqual(snapshot(a), before)

    # Stale generation and a current-generation erased dependency are different
    # atomic refusals; an independent current-generation output still admits.
    def test_late_writers_and_independent_positive(self):
        v = fixture("S26")
        a = Adapter(v["initial_state"], "control")
        self.apply(a, v["operations"][0])
        op = copy.deepcopy(v["operations"][1])
        for generation, code in ((0, "stale_generation"), (1, "erasure_fenced")):
            op["expected_generation"] = generation
            before = snapshot(a)
            with self.assertRaisesRegex(Refusal, "^" + code + "$"):
                Transactions(a).apply(op)
            self.assertEqual(snapshot(a), before)
        output = ref(op["proposals"][0])
        fact = next(f for f in a.policy["lineage_facts"] if f["output"] == output)
        fact.update(kind="direct", inputs=[], complete=True)
        op["proposals"][0]["envelope"]["lineage"] = []
        self.assertEqual(Transactions(a).apply(op)["outcome"], "admitted")

    # Restore revives only backup custody presence behind the global read fence;
    # stale witness and wrong cut preserve full state, current witness repurges.
    def test_restore_fence_and_current_reconciliation(self):
        v = fixture("S25")
        a = Adapter(v["initial_state"], "control")
        self.apply(a, v["operations"][0])
        op = copy.deepcopy(v["operations"][1])
        op["restore_cut"] -= 1
        self.denied(a, op, "invalid_time")
        result = self.apply(a, v["operations"][1])
        self.assertEqual((result["outcome"], result["erasure_status"]), ("fenced", "access_closed"))
        self.assertTrue(all(c["present"] for c in a.runtime["custody"]))
        self.assertEqual(a.runtime["erasure_generation"], 1)
        self.assertEqual(a.query(v["query"])["code"], "erasure_fenced")
        self.denied(a, v["operations"][2], "erasure_incomplete")
        reconcile = copy.deepcopy(v["operations"][2])
        reconcile["external_witness"] = True
        result = self.apply(a, reconcile)
        self.assertEqual(result["outcome"], "reconciled")
        self.assertTrue(all(not c["present"] for c in a.runtime["custody"]))
        self.assertEqual(a.runtime["restore"]["status"], "open")
        self.assertEqual(a.query(v["query"])["items"], [])
        self.assertEqual(a.runtime["erasure_generation"], 1)

    # A complete witness cannot make an unreachable controlled payload purged;
    # reconciliation stays atomic/fenced until all affected sinks are reachable.
    def test_restore_unreachable_custody_stays_fenced(self):
        v = fixture("S25")
        a = Adapter(v["initial_state"], "control")
        self.apply(a, v["operations"][0])
        self.apply(a, v["operations"][1])
        a.runtime["custody"][0]["reachable"] = False
        op = copy.deepcopy(v["operations"][2])
        op["external_witness"] = True
        self.denied(a, op, "erasure_incomplete")
        a.runtime["custody"][0]["reachable"] = True
        self.assertEqual(self.apply(a, op)["outcome"], "reconciled")


if __name__ == "__main__":
    unittest.main(verbosity=2)
