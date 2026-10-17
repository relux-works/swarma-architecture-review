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
    # R7-043: rule and certificate identities are dependencies of their target.
    # Both withdrawals retain the exact cause and replay cannot duplicate it.
    def test_changed_rule_and_certificate(self):
        for name in ("rule", "certificate"):
            with self.subTest(name=name):
                vector = json.loads((BASE / "fixtures/dirty-rule-certificate-v0.2.3" / (name + ".vector.json")).read_text())
                adapter = Adapter(vector["initial_state"], "control")
                writer = Transactions(adapter)
                result = writer.apply(vector["operations"][0])
                self.assertEqual(adapter.runtime["dirty"], [{"id": "rec:b", "version": 1}])
                self.assertEqual(adapter.runtime["dirty_causes"], [{"assertion": {"id": "rec:b", "version": 1},
                                                                  "revision": {"id": "rec:r", "version": 1}}])
                before = copy.deepcopy(adapter.runtime)
                self.assertEqual(writer.apply(vector["operations"][0]), result)
                self.assertEqual(adapter.runtime, before)
                current = adapter.query(vector["query"])
                self.assertEqual(current["cutoffs"], ["dirty"])
                self.assertTrue(current["items"][0]["needs_review"])

    # Hidden changed rules/checks keep protected dirtiness without a public
    # effect; the private control remains dirty. Challenges invalidate nothing.
    def test_rule_check_visibility_and_challenge(self):
        for name in ("rule", "certificate"):
            vector = json.loads((BASE / "fixtures/dirty-rule-certificate-v0.2.3" / (name + ".vector.json")).read_text())
            initial = copy.deepcopy(vector["initial_state"])
            target = vector["operations"][0]["revision"]["body"]["target"]
            changed = next(r for r in initial["records"] if ref(r) == target)
            changed["envelope"]["disclosure"]["audiences"] = ["aud:private"]
            adapter = Adapter(initial, "control")
            Transactions(adapter).apply(vector["operations"][0])
            self.assertEqual(adapter.runtime["dirty"], [{"id": "rec:b", "version": 1}])
            public = adapter.query(vector["query"])
            self.assertFalse(public["items"][0]["needs_review"])
            self.assertEqual(public["cutoffs"], [])
            private = copy.deepcopy(vector["query"])
            private["audience"] = "aud:private"
            self.assertTrue(adapter.query(private)["items"][0]["needs_review"])
            adapter = Adapter(vector["initial_state"], "control")
            op = copy.deepcopy(vector["operations"][0])
            op["revision"]["body"]["relation"] = "challenge"
            self.assertEqual(Transactions(adapter).apply(op)["outcome"], "challenged")
            self.assertEqual(adapter.runtime["dirty"], [])
            self.assertEqual(adapter.runtime["dirty_causes"], [])
            self.assertEqual(adapter.query(vector["query"])["items"][0]["support"]["witness"], "present")

    # A changed rule reaches downstream registered consumers transitively;
    # pre-cause and recomputed snapshots must not invent an unresolved cause.
    def test_transitive_rule_cause_history_and_recompute(self):
        vector = json.loads((BASE / "fixtures/dirty-rule-certificate-v0.2.3/rule.vector.json").read_text())
        initial = copy.deepcopy(vector["initial_state"])
        c = copy.deepcopy(next(r for r in initial["records"] if r["envelope"]["id"] == "rec:b"))
        j = copy.deepcopy(next(r for r in initial["records"] if r["envelope"]["id"] == "rec:j"))
        cert = copy.deepcopy(next(r for r in initial["records"] if r["envelope"]["id"] == "cert:j"))
        for record, name, sequence in ((c, "rec:c", 97), (j, "rec:jc", 98), (cert, "cert:jc", 99)):
            record["envelope"]["id"] = name
            record["envelope"]["recorded"]["sequence"] = sequence
            initial["records"].append(record)
            initial["policy"]["lineage_facts"].append({"output": ref(record), "profile": {"id": "integration:synthetic", "version": 1},
                                                       "kind": "direct", "inputs": [], "complete": True})
        j["body"]["target"]["assertion"] = ref(c)
        j["body"]["premises"][0]["literal"]["assertion"] = {"id": "rec:b", "version": 1}
        j["body"]["check"] = ref(cert)
        j["body"]["rule"]["id"] = "rule:jc"
        cert["body"]["pins"].update(subject=ref(j), rule=copy.deepcopy(j["body"]["rule"]))
        adapter = Adapter(initial, "control")
        Transactions(adapter).apply(vector["operations"][0])
        expected = [{"id": "rec:b", "version": 1}, {"id": "rec:c", "version": 1}]
        self.assertEqual(adapter.runtime["dirty"], expected)
        self.assertEqual([c["assertion"] for c in adapter.runtime["dirty_causes"]], expected)
        query = copy.deepcopy(vector["query"])
        query["scope"]["targets"] = [ref(c)]
        self.assertTrue(adapter.query(query)["items"][0]["needs_review"])
        query["cut"]["memory"] = 100
        self.assertEqual(adapter.query(query)["items"][0]["support"]["witness"], "present")
        query["cut"]["memory"] = 101
        query["bounds"].update(roots=0, rules=0, source_resolutions=0)
        self.assertEqual(adapter.query(query)["cutoffs"], ["dirty"])
        adapter.runtime["dirty"] = []
        adapter.runtime["dirty_causes"] = []
        query["bounds"] = vector["query"]["bounds"]
        result = adapter.query(query)
        self.assertEqual(result["items"][0]["support"]["evaluation"], "complete")
        self.assertFalse(result["items"][0]["needs_review"])

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
        Transactions(adapter).apply(vector["operations"][6])
        query = copy.deepcopy(vector["query"])
        query["cut"]["memory"] = adapter.runtime["memory_cut"]
        expected = [{"id": "rec:dependent", "version": 1}]
        self.assertEqual(adapter.query(query)["review_required"], expected)
        adapter.runtime["dirty"] = []
        adapter.runtime["dirty_causes"] = []
        self.assertEqual(adapter.query(query)["review_required"], expected)
        adapter.records[key({"id": "rec:review-dependent", "version": 1})]["envelope"]["disclosure"]["audiences"] = ["aud:private"]
        self.assertEqual(adapter.query(query)["review_required"], [])

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
