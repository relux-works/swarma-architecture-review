"""Exact storage-scope and atomic replay controls for the released wire contract."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter
from boundary import Boundary
from evaluator import Refusal
from transactions import Transactions, key, ref


BASE = Path(__file__).resolve().parent


def fixture(name):
    return json.loads((BASE.parents[1] / "spec/kernel/vectors/semantic" / (name + ".json")).read_text())


class RetentionControls(unittest.TestCase):
    def denied(self, adapter, op, code="not_authorized"):
        before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy))
        with self.assertRaisesRegex(Refusal, "^" + code + "$"):
            Transactions(adapter).apply(op)
        self.assertEqual((adapter.records, adapter.runtime, adapter.policy), before)

    # Every grant dimension and every output/direct/transitive input needs the
    # one explicit storage scope. A narrow metadata=false retain grant suffices.
    def test_exact_scope_and_known_closure(self):
        v = fixture("P11")
        for op in v["operations"][:7]:
            with self.subTest(context=op["context"]):
                self.denied(Adapter(v["initial_state"], "control"), op)
        adapter = Adapter(v["initial_state"], "control")
        result = Transactions(adapter).apply(v["operations"][8])
        self.assertEqual(result["outcome"], "admitted")
        self.assertEqual(adapter.runtime["memory_cut"], 101)
        self.assertEqual(len(adapter.runtime["idempotency"]), 1)
        output = adapter.records[key(result["refs"][0])]["envelope"]
        self.assertEqual(output["disclosure"]["audiences"], ["aud:private"])
        self.assertEqual(output["lineage"], [{"id": "rec:private", "version": 1}])

    # Retention traverses known lower bounds through an already unknown input;
    # an unrelated publish grant on the ancestor cannot authorize storage/read.
    def test_transitive_unknown_lower_bound(self):
        for suffix, success in (("", False), ("-control", True)):
            path = BASE.parent / ("cases/astra-25-retention-authority-transitive-unknown" + suffix + ".vector.json")
            v = json.loads(path.read_text())
            adapter = Adapter(v["initial_state"], "control")
            op = next(op for op in v["operations"] if op["op"] == "admit")
            if success:
                self.assertEqual(Transactions(adapter).apply(op)["outcome"], "admitted")
            else:
                self.denied(adapter, op)

    # Missing inputs cannot be conjured from future facts. The same key succeeds
    # with the input in either batch order and inherits its private restriction.
    def test_same_batch_resolution_and_order(self):
        v = fixture("P13")
        for reverse in (False, True):
            adapter = Adapter(v["initial_state"], "control")
            self.denied(adapter, v["operations"][1], "invalid_reference")
            op = copy.deepcopy(v["operations"][2])
            if reverse:
                op["proposals"].reverse()
            self.assertEqual(Transactions(adapter).apply(op)["outcome"], "admitted")
            output = adapter.records[key({"id": "rec:model-tainted", "version": 1})]["envelope"]
            self.assertEqual(output["disclosure"]["audiences"], ["aud:private"])
            self.assertEqual(len(adapter.runtime["idempotency"]), 1)

    # Empty onward labels can be retained explicitly; retain confers no query
    # access or metadata visibility and unknown lineage does not waive authority.
    def test_empty_labels_and_unknown_direct_input(self):
        v = fixture("P13")
        self.denied(Adapter(v["initial_state"], "control"), v["operations"][0])
        adapter = Adapter(v["initial_state"], "control")
        op = copy.deepcopy(v["operations"][2])
        op["proposals"] = [p for p in op["proposals"] if p["envelope"]["id"] == "rec:model-empty"]
        result = Transactions(adapter).apply(op)
        self.assertEqual(result["outcome"], "admitted")
        output = adapter.records[key(result["refs"][0])]["envelope"]
        self.assertEqual(output["disclosure"]["audiences"], [])
        query = copy.deepcopy(v["query"])
        query["cut"]["memory"] = adapter.runtime["memory_cut"]
        self.assertEqual(adapter.query(query)["items"], [])

    # Every original output and ancestor remains authorized before receipt
    # replay; denial preserves the original stored receipt and all state.
    def test_replay_current_record_authority(self):
        v = fixture("P11")
        for denied_id in ("rec:paraphrase", "rec:private", "rec:retained-root"):
            adapter = Adapter(v["initial_state"], "control")
            writer = Transactions(adapter)
            first = writer.apply(v["operations"][8])
            self.assertEqual(writer.apply(v["operations"][9]), first)
            for grant in adapter.policy["grants"]:
                if ("retain" in grant["rights"] and grant["audience"] == "aud:private"
                        and grant["purpose"] == "purpose:read" and denied_id in grant["records"]):
                    grant["records"].remove(denied_id)
            self.denied(adapter, v["operations"][9])
            self.assertEqual(adapter.runtime["idempotency"][0]["receipt"], first)

    # Live retain revocation blocks a new key and old receipt without erasing
    # data or revoking read/use. A different authorized context still conflicts.
    def test_revocation_and_context_identity(self):
        v = fixture("P11")
        adapter = Adapter(v["initial_state"], "control")
        first = Transactions(adapter).apply(v["operations"][8])
        self.denied(adapter, v["operations"][10], "idempotency_conflict")
        Boundary(adapter).apply(v["operations"][12])
        for op in v["operations"][13:15]:
            self.denied(adapter, op)
        self.assertEqual(adapter.runtime["idempotency"][0]["receipt"], first)
        self.assertEqual(adapter.runtime["erased"], [])
        self.assertEqual(len(adapter.query(v["operations"][15]["query"])["items"]), 1)

    # The context is mandatory and has no principal override or inferred query
    # default; complete explicit context remains a valid positive neighbor.
    def test_context_closed_shape(self):
        v = fixture("P11")
        for variant in ("missing", "principal", "purpose"):
            op = copy.deepcopy(v["operations"][8])
            if variant == "missing":
                op["context"].pop("retention_context")
            elif variant == "principal":
                op["context"]["retention_context"]["principal"] = op["context"]["actor"]
            else:
                op["context"]["retention_context"].pop("purpose")
            self.denied(Adapter(v["initial_state"], "control"), op, "invalid_shape")
        self.assertEqual(Transactions(Adapter(v["initial_state"], "control")).apply(v["operations"][8])["outcome"], "admitted")

    # Inputs use their own exact space, not the output's. A matching input-only
    # storage grant repairs this failure without widening any disclosure labels.
    def test_input_space_is_independent(self):
        v = fixture("P11")
        adapter = Adapter(v["initial_state"], "control")
        root = adapter.records[key({"id": "rec:retained-root", "version": 1})]
        root["envelope"]["space"] = "space:input"
        self.denied(adapter, v["operations"][8])
        adapter.policy["grants"].append({"principal": "subj:h1", "space": "space:input",
                                         "audience": "aud:private", "purpose": "purpose:read",
                                         "rights": ["retain"], "records": ["rec:retained-root"], "metadata": False})
        self.assertEqual(Transactions(adapter).apply(v["operations"][8])["outcome"], "admitted")


if __name__ == "__main__":
    unittest.main(verbosity=2)
