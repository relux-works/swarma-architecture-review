"""Strict canonical successor authority is separate from CAS head selection."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter
from evaluator import Refusal
from transactions import Transactions, key, ref


CASES = Path(__file__).resolve().parent.parent / "cases"


def fixture(suffix):
    return json.loads((CASES / ("astra-24-authority-succession" + suffix + ".vector.json")).read_text())


class SuccessionControls(unittest.TestCase):
    def denied(self, adapter, op, code):
        before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy, adapter.captures))
        with self.assertRaisesRegex(Refusal, "^" + code + "$"):
            Transactions(adapter).apply(op)
        self.assertEqual((adapter.records, adapter.runtime, adapter.policy, adapter.captures), before)

    # Incomparable, identical and older canonical receipts cannot replace or
    # correct an authoritative record; every refused attempt is fully atomic.
    def test_forbidden_receipt_orders(self):
        for suffix in ("", "-same", "-prior"):
            for relation in ("replace", "correct"):
                with self.subTest(suffix=suffix, relation=relation):
                    v = fixture(suffix)
                    op = v["operations"][-1]
                    op["revision"]["body"]["relation"] = relation
                    self.denied(Adapter(v["initial_state"], "control"), op, "authority_receipt_required")

    # Direct and transitive receipt ancestry admits the ordered transaction.
    # Reversing event array order does not alter authority reachability.
    def test_valid_successors(self):
        for suffix in ("-control", "-transitive"):
            for reverse in (False, True):
                v = fixture(suffix)
                if reverse:
                    v["initial_state"]["policy"]["authority_events"].reverse()
                adapter = Adapter(v["initial_state"], "control")
                op = v["operations"][-1]
                result = Transactions(adapter).apply(op)
                self.assertEqual(result["outcome"], "revised")
                self.assertEqual(len(adapter.records), len(v["initial_state"]["records"]) + 2)
                self.assertEqual(adapter.runtime["memory_cut"], 102)
                self.assertEqual(adapter.runtime["dirty"], [{"id": "rec:dependent", "version": 1}])
                self.assertEqual(len(adapter.runtime["idempotency"]), 1)

    # Exact successful replay precedes the now-advanced head. A fresh key with
    # the same stale expected head conflicts without adding records or causes.
    def test_replay_before_cas(self):
        v = fixture("-control")
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        first = writer.apply(v["operations"][-1])
        retry = copy.deepcopy(v["operations"][-1])
        retry["context"]["at"] = "2026-10-17T00:00:01Z"
        before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy))
        self.assertEqual(writer.apply(retry), first)
        self.assertEqual((adapter.records, adapter.runtime, adapter.policy), before)
        retry["idempotency_key"] = "key:stale-new-attempt"
        self.denied(adapter, retry, "version_conflict")

    # Plain canonical receipt imports may remain incomparable; they create no
    # memory replacement or dirty effect and leave the slot head ambiguous.
    def test_plain_incomparable_import(self):
        v = fixture("")
        adapter = Adapter(v["initial_state"], "control")
        source = v["operations"][-1]
        op = {"op": "admit", "context": source["context"], "idempotency_key": "key:plain-import",
              "proposals": [source["replacement"]], "expected_generation": source["expected_generation"]}
        result = Transactions(adapter).apply(op)
        self.assertEqual(result["outcome"], "admitted")
        self.assertEqual(adapter.runtime["memory_cut"], 101)
        self.assertEqual(adapter.runtime["dirty"], [])
        self.assertIsNone(Transactions(adapter).head(adapter.records[key(ref(source["replacement"]))], adapter.records))
        self.assertEqual(len(adapter.records), len(v["initial_state"]["records"]) + 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
