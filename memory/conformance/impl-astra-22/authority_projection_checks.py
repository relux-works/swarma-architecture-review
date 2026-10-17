"""Receipt ancestry remains authoritative without an intermediate assertion."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter
from transactions import Transactions, ref


CASES = Path(__file__).resolve().parent.parent / "cases"


def fixture(control=False):
    return json.loads((CASES / ("astra-24-receipt-only-order" + ("-control" if control else "") + ".vector.json")).read_text())


class AuthorityProjectionControls(unittest.TestCase):
    def read(self, adapter, query):
        shapes = Transactions(adapter).shapes
        self.assertTrue(shapes.valid(adapter.initial, shapes.vector["properties"]["initial_state"]))
        self.assertTrue(shapes.valid(query, shapes.vector["properties"]["query"]))
        before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy, adapter.captures))
        result = adapter.query(query)
        self.assertEqual((adapter.records, adapter.runtime, adapter.policy, adapter.captures), before)
        return result

    # With or without the middle assertion, the identical complete receipt DAG
    # makes d3 current and earlier eligible decisions historical, without writes.
    def test_missing_middle_assertion(self):
        for control in (False, True):
            v = fixture(control)
            result = self.read(Adapter(v["initial_state"], "control"), v["query"])
            self.assertEqual(result["currentness"], "current")
            self.assertEqual([i["ref"] for i in result["items"]], [{"id": "rec:d", "version": 3}])
            self.assertEqual(result["historical"], [{"id": "rec:d", "version": n} for n in ([1, 2] if control else [1])])

    # More than one receipt-only intermediate and event-array permutations do
    # not change transitive ordering; no assertion is fabricated for the gap.
    def test_long_receipt_chain(self):
        for reverse in (False, True):
            v = fixture()
            state = v["initial_state"]
            middle = copy.deepcopy(next(r for r in state["records"] if r["envelope"]["id"] == "rec:receipt2"))
            middle["envelope"]["id"] = "rec:middle-extra"
            middle["envelope"]["recorded"]["sequence"] = 7
            middle["body"]["object"] = "object:middle-extra"
            state["records"].append(middle)
            state["policy"]["lineage_facts"].append({"output": ref(middle), "profile": {"id": "integration:synthetic", "version": 1},
                                                       "kind": "direct", "inputs": [], "complete": True})
            events = state["policy"]["authority_events"]
            next(e for e in events if e["receipt"]["id"] == "rec:receipt3")["predecessors"] = [ref(middle)]
            events.append({"receipt": ref(middle), "issuer": "subj:h1", "canonical": True,
                           "predecessors": [{"id": "rec:receipt2", "version": 1}]})
            if reverse:
                events.reverse()
            result = self.read(Adapter(state, "control"), v["query"])
            self.assertEqual(result["currentness"], "current")
            self.assertEqual([i["ref"]["version"] for i in result["items"]], [3])
            self.assertEqual(result["historical"], [{"id": "rec:d", "version": 1}])

    # A genuinely incomparable branch remains ambiguous; mere receipt presence
    # or later arrival cannot manufacture a predecessor relationship.
    def test_incomparable_branch(self):
        v = fixture()
        next(e for e in v["initial_state"]["policy"]["authority_events"] if e["receipt"]["id"] == "rec:receipt3")["predecessors"] = []
        result = self.read(Adapter(v["initial_state"], "control"), v["query"])
        self.assertEqual(result["currentness"], "ambiguous_current")
        self.assertEqual([i["ref"]["version"] for i in result["items"]], [1, 3])
        self.assertEqual(result["historical"], [])

    # Hidden, historical-cut, different-subject and different-mode candidates
    # cannot suppress the eligible old decision. A private control sees d3.
    def test_candidate_eligibility(self):
        for variant in ("hidden", "cut", "subject", "mode"):
            v = fixture()
            latest = next(r for r in v["initial_state"]["records"] if r["envelope"]["id"] == "rec:d" and r["envelope"]["version"] == 3)
            if variant == "hidden":
                latest["envelope"]["disclosure"]["audiences"] = ["aud:private"]
            elif variant == "cut":
                v["initial_state"]["runtime"]["committed_cuts"] = [4, 100]
                v["query"]["cut"]["memory"] = 4
            elif variant == "subject":
                latest["envelope"]["subject"] = "subj:other"
            else:
                latest["envelope"]["context"] = "simulated"
            adapter = Adapter(v["initial_state"], "control")
            result = self.read(adapter, v["query"])
            self.assertEqual(result["currentness"], "current")
            self.assertEqual([i["ref"]["version"] for i in result["items"]], [1])
            self.assertEqual(result["historical"], [])
            if variant == "hidden":
                private = copy.deepcopy(v["query"])
                private["audience"] = "aud:private"
                result = self.read(adapter, private)
                self.assertEqual([i["ref"]["version"] for i in result["items"]], [3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
