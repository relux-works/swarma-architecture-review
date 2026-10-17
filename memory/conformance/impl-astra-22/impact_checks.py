"""Dirty-cause and authorized registered-impact controls."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter, key, ref
from transactions import Transactions
from impact import closure


BASE = Path(__file__).resolve().parent


def fixture(name):
    return json.loads((BASE.parents[1] / "spec/kernel/vectors/semantic" / (name + ".json")).read_text())


def visible_case():
    return json.loads((BASE.parent / "cases/astra-25-hidden-dirty-invalidation-visible-control.vector.json").read_text())


class ImpactControls(unittest.TestCase):
    # Revision and exact cause commit together. Before-cause reads stay complete;
    # resolved causes are not reconstructed from immutable revision history.
    def test_retained_cause_and_historical_cut(self):
        vector = fixture("S17")
        adapter = Adapter(vector["initial_state"], "control")
        result = Transactions(adapter).apply(vector["operations"][0])
        self.assertEqual(result["outcome"], "revised")
        self.assertEqual(adapter.runtime["dirty_causes"], [{"assertion": {"id": "rec:b", "version": 1},
                                                          "revision": {"id": "rec:r", "version": 1}}])
        current = adapter.query(vector["query"])
        self.assertEqual(current["cutoffs"], ["dirty"])
        self.assertTrue(current["items"][0]["needs_review"])
        for sign in ("support", "oppose"):
            self.assertEqual(current["items"][0][sign]["evaluation"], "incomplete")
            self.assertEqual(current["items"][0][sign]["witness"], "not_found")
        query = copy.deepcopy(vector["query"])
        query["cut"]["memory"] = 100
        past = adapter.query(query)
        self.assertEqual(past["cutoffs"], [])
        self.assertEqual(past["items"][0]["support"]["witness"], "present")
        adapter.runtime["dirty"] = []
        adapter.runtime["dirty_causes"] = []
        resolved = adapter.query(vector["query"])
        self.assertEqual(resolved["cutoffs"], [])
        self.assertFalse(resolved["items"][0]["needs_review"])
        self.assertEqual(resolved["review_required"], [])

    # Hiding any necessary path element removes its public dirty effect while
    # preserving the independent public witness and protected cause inventory.
    def test_hidden_path_elements_do_not_disclose_dirty(self):
        vector = visible_case()
        for hidden in ("rec:a", "rec:j", "cert:j", "rec:r"):
            with self.subTest(hidden=hidden):
                initial, ops = copy.deepcopy(vector["initial_state"]), copy.deepcopy(vector["operations"])
                candidates = initial["records"] + [ops[1]["revision"]]
                next(r for r in candidates if r["envelope"]["id"] == hidden)["envelope"]["disclosure"]["audiences"] = ["aud:private"]
                adapter = Adapter(initial, "control")
                Transactions(adapter).apply(ops[1])
                before = copy.deepcopy(adapter.runtime)
                result = adapter.query(vector["query"])
                self.assertFalse(result["items"][0]["needs_review"])
                self.assertEqual(result["items"][0]["support"]["evaluation"], "complete")
                self.assertEqual(result["items"][0]["support"]["witness"], "present")
                self.assertEqual(result["review_required"], [])
                self.assertEqual(result["cutoffs"], [])
                self.assertEqual(adapter.runtime, before)
                self.assertEqual(len(adapter.runtime["dirty_causes"]), 1)
        adapter = Adapter(vector["initial_state"], "control")
        Transactions(adapter).apply(vector["operations"][1])
        self.assertTrue(adapter.query(vector["query"])["items"][0]["needs_review"])

    # An AND impact edge needs every premise to be eligible; a hidden sibling
    # cannot be skipped just because the changed input itself is visible.
    def test_hidden_sibling_and_context_filter(self):
        vector = visible_case()
        initial = copy.deepcopy(vector["initial_state"])
        other = copy.deepcopy(initial["records"][0])
        other["envelope"]["id"] = "rec:sibling"
        other["envelope"]["disclosure"]["audiences"] = ["aud:private"]
        initial["records"].append(other)
        rule = next(r for r in initial["records"] if r["envelope"]["id"] == "rec:j")
        rule["body"]["premises"].append({"kind": "assertion", "literal": {"assertion": ref(other), "polarity": "support"}})
        adapter = Adapter(initial, "control")
        Transactions(adapter).apply(vector["operations"][1])
        self.assertFalse(adapter.query(vector["query"])["items"][0]["needs_review"])
        adapter.records[key(ref(other))]["envelope"]["disclosure"]["audiences"].append("aud:public")
        self.assertTrue(adapter.query(vector["query"])["items"][0]["needs_review"])
        adapter.records[key(ref(other))]["envelope"]["context"] = "dream"
        self.assertFalse(adapter.query(vector["query"])["items"][0]["needs_review"])

    # Later withdrawal of a path does not remove a retained earlier cause;
    # cause eligibility uses its pre-revision registration graph.
    def test_later_withdrawal_preserves_cause(self):
        vector = visible_case()
        adapter = Adapter(vector["initial_state"], "control")
        Transactions(adapter).apply(vector["operations"][1])
        revision = copy.deepcopy(adapter.records[key(ref(vector["operations"][1]["revision"]))])
        revision["envelope"].update(id="rec:withdraw-path", recorded={"sequence": 103, "at": "2026-10-17T00:00:01Z"})
        revision["body"].update(relation="withdraw", target={"id": "rec:j", "version": 1}, replacement=None)
        adapter.records[key(ref(revision))] = revision
        adapter.runtime["memory_cut"] = 103
        adapter.runtime["committed_cuts"].append(103)
        query = copy.deepcopy(vector["query"])
        query["cut"]["memory"] = 103
        result = adapter.query(query)
        self.assertEqual(result["cutoffs"], ["dirty"])
        self.assertTrue(result["items"][0]["needs_review"])
        self.assertEqual(result["items"][0]["support"]["witness"], "not_found")

    # A revised decision exposes authorized cross-schema review dependents, even
    # after recomputation clears dirty state; hidden review edges disclose none.
    def test_cross_schema_review_is_not_global_dirty(self):
        vector = fixture("B01")
        adapter = Adapter(vector["initial_state"], "control")
        Transactions(adapter).apply(vector["operations"][0])
        expected = [{"id": "rec:dependent", "version": 1}]
        self.assertEqual(adapter.query(vector["query"])["review_required"], expected)
        adapter.runtime["dirty"] = []
        adapter.runtime["dirty_causes"] = []
        self.assertEqual(adapter.query(vector["query"])["review_required"], expected)
        adapter.records[key({"id": "rec:review-dependent", "version": 1})]["envelope"]["disclosure"]["audiences"] = ["aud:private"]
        self.assertEqual(adapter.query(vector["query"])["review_required"], [])

    # Finite closure visits transitive branches and cycles without confusing a
    # support-only path with one containing a registered review edge.
    def test_transitive_closure_oracle(self):
        edges = [("B", ["A"], False), ("C", ["B", "X"], True),
                 ("D", ["C"], False), ("B", ["D"], True), ("Z", ["Y"], True)]
        self.assertEqual(closure(edges, {"A"}), {"B", "C", "D"})
        self.assertEqual(closure(edges, {"A"}, review_only=True), {"B", "C", "D"})
        self.assertEqual(closure(edges[:1], {"A"}, review_only=True), set())
        self.assertEqual(closure(edges, {"absent"}), set())


if __name__ == "__main__":
    unittest.main(verbosity=2)
