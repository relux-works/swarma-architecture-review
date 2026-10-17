"""D-009 source-derived issuer-local order controls, before 0.2.6 intake.

Expected orders come from kernel v0.3 section 5.3 and DECISIONS.md D-009.
The finite DAG control checks all 256 four-event cases described below, not
arbitrary graph size, deployment attribution, or foreign implementation code.
"""

import copy
import itertools
import json
from pathlib import Path
import unittest

from adapter import Adapter, refusal
from evaluator import Refusal
from transactions import Transactions, key, ref


BASE = Path(__file__).resolve().parent
CASES = BASE.parent / "cases"
H = "subj:h1"


def fixture(name):
    return json.loads((CASES / name).read_text())


def projected_order(value):
    return (value["currentness"], [item["ref"] for item in value["items"]], value["historical"])


class IssuerLocalOrderControls(unittest.TestCase):
    def assert_order(self, state, query, ordered):
        a = Adapter(state, "source-D009")
        writer = Transactions(a)
        shape = writer.shapes.vector["properties"]
        self.assertTrue(writer.shapes.valid(state, shape["initial_state"]))
        self.assertTrue(writer.shapes.valid(query, shape["query"]))
        before = copy.deepcopy(a.__dict__)
        result = a.query(query)
        one, three = ({"id": "rec:d", "version": n} for n in (1, 3))
        self.assertEqual(projected_order(result),
                         ("current", [three], [one]) if ordered else
                         ("ambiguous_current", [one, three], []))
        target = a.records[key(one)]
        self.assertEqual(writer.head(target, a.records), three if ordered else None)
        self.assertEqual(writer.strict_successor({"id": "rec:receipt3", "version": 1},
                                                {"id": "rec:receipt1", "version": 1}, H), ordered)
        self.assertEqual(a.__dict__, before)

    # The exact previously un-oracled native pair now has the owner's outcome:
    # H1 middle orders d3; protected H2 middle leaves both current candidates.
    def test_original_owner_pair(self):
        original = fixture("astra-24-authority-issuer.input.json")
        self.assertEqual(len(original["probes"]), 2)
        for probe in original["probes"]:
            with self.subTest(name=probe["name"]):
                self.assertEqual(probe["operations"], [])
                middle = next(e for e in probe["initial_state"]["policy"]["authority_events"]
                              if e["receipt"]["id"] == "rec:receipt2")
                self.assert_order(probe["initial_state"], probe["query"], middle["issuer"] == H)

    # Assertion-free own events count. A foreign bridge adds no order and is
    # never contracted; one direct own path still wins despite that branch.
    def test_path_matrix_and_event_permutations(self):
        for foreign, direct, reverse in itertools.product((False, True), repeat=3):
            with self.subTest(foreign=foreign, direct=direct, reverse=reverse):
                v = fixture("astra-24-receipt-only-order.vector.json")
                events = v["initial_state"]["policy"]["authority_events"]
                middle = next(e for e in events if e["receipt"]["id"] == "rec:receipt2")
                middle["issuer"] = "subj:h2" if foreign else H
                latest = next(e for e in events if e["receipt"]["id"] == "rec:receipt3")
                if direct:
                    latest["predecessors"].append({"id": "rec:receipt1", "version": 1})
                if reverse:
                    events.reverse()
                source = next(r for r in v["initial_state"]["records"]
                              if r["envelope"]["id"] == "rec:receipt2")
                self.assertEqual(source["envelope"]["issuer"], H)
                self.assert_order(v["initial_state"], v["query"], not foreign or direct)

    # With exactly the same induced H graph, changing only foreign issuer and
    # foreign predecessor edges preserves order; both absent/present H paths
    # are checked, so always accepting or rejecting cannot satisfy this pair.
    def test_foreign_part_invariance(self):
        for direct in (False, True):
            own_edges = None
            for foreign_issuer, linked in itertools.product(("subj:h2", "subj:h3"), (False, True)):
                with self.subTest(direct=direct, foreign_issuer=foreign_issuer, linked=linked):
                    v = fixture("astra-24-receipt-only-order.vector.json")
                    events = v["initial_state"]["policy"]["authority_events"]
                    middle = next(e for e in events if e["receipt"]["id"] == "rec:receipt2")
                    middle.update(issuer=foreign_issuer, predecessors=[{"id": "rec:receipt1", "version": 1}] if linked else [])
                    latest = next(e for e in events if e["receipt"]["id"] == "rec:receipt3")
                    if direct:
                        latest["predecessors"].append({"id": "rec:receipt1", "version": 1})
                    vertices = {key(e["receipt"]) for e in events if e["issuer"] == H and e["canonical"]}
                    edges = sorted((key(e["receipt"]), key(p)) for e in events
                                   if key(e["receipt"]) in vertices for p in e["predecessors"] if key(p) in vertices)
                    if own_edges is None:
                        own_edges = edges
                    self.assertEqual(edges, own_edges)
                    self.assert_order(v["initial_state"], v["query"], direct)

    # All 64 acyclic edge subsets on four chronologically indexed events and
    # all four H/foreign choices for two assertion-free middles (256 states)
    # agree with independent Boolean-matrix closure on the induced H graph.
    # Public currentness, CAS head and strict succession must agree throughout.
    def test_all_four_event_dags(self):
        v = fixture("astra-24-receipt-only-order.vector.json")
        state = v["initial_state"]
        extra = copy.deepcopy(next(r for r in state["records"] if r["envelope"]["id"] == "rec:receipt2"))
        extra["envelope"]["id"] = "rec:d009-middle"
        extra["envelope"]["recorded"]["sequence"] = max(r["envelope"]["recorded"]["sequence"] for r in state["records"]) + 1
        extra["body"]["object"] = "object:d009-middle"
        state["records"].append(extra)
        state["policy"]["lineage_facts"].append({"output": ref(extra), "profile": {"id": "integration:synthetic", "version": 1},
                                                    "kind": "direct", "inputs": [], "complete": True})
        refs = [{"id": name, "version": 1} for name in ("rec:receipt1", "rec:receipt2", "rec:d009-middle", "rec:receipt3")]
        edges = [(i, j) for i in range(4) for j in range(i)]
        for middles in itertools.product((H, "subj:h2"), repeat=2):
            issuers = [H, *middles, H]
            for mask in range(64):
                with self.subTest(middles=middles, mask=mask):
                    selected = [edge for bit, edge in enumerate(edges) if mask & (1 << bit)]
                    trial = copy.deepcopy(state)
                    trial["policy"]["authority_events"] = [
                        {"receipt": refs[i], "issuer": issuers[i], "canonical": True,
                         "predecessors": [refs[j] for left, j in selected if left == i]} for i in range(4)]
                    reach = [[False] * 4 for _ in range(4)]
                    for i, j in selected:
                        reach[i][j] = issuers[i] == H and issuers[j] == H
                    for via in range(4):
                        for i in range(4):
                            for j in range(4):
                                reach[i][j] = reach[i][j] or (reach[i][via] and reach[via][j])
                    self.assert_order(trial, v["query"], reach[3][0])

    # Replace/correct use that same relation through the real write boundary:
    # foreign-only succession refuses with the existing exact code and no
    # state mutation; an own chain or direct own bypass admits and reads d2.
    def test_strict_replacement_and_correction(self):
        for foreign, direct, relation in itertools.product((False, True), (False, True), ("replace", "correct")):
            with self.subTest(foreign=foreign, direct=direct, relation=relation):
                v = fixture("astra-24-authority-succession-transitive.vector.json")
                events = v["initial_state"]["policy"]["authority_events"]
                next(e for e in events if e["receipt"]["id"] == "rec:receipt-mid")["issuer"] = "subj:h2" if foreign else H
                if direct:
                    next(e for e in events if e["receipt"]["id"] == "rec:receipt2")["predecessors"].append({"id": "rec:receipt1", "version": 1})
                op = copy.deepcopy(v["operations"][-1])
                op["revision"]["body"]["relation"] = relation
                a = Adapter(v["initial_state"], "source-D009")
                writer = Transactions(a)
                shapes = writer.shapes
                self.assertTrue(shapes.valid(a.initial, shapes.vector["properties"]["initial_state"]))
                self.assertTrue(shapes.valid(op, shapes.vector["properties"]["operations"]["items"]))
                before = copy.deepcopy(a.__dict__)
                if foreign and not direct:
                    with self.assertRaises(Refusal) as error:
                        writer.apply(op)
                    self.assertEqual(refusal(error.exception.code), {"type": "refusal", "code": "authority_receipt_required", "retryable": False})
                    self.assertEqual(a.__dict__, before)
                else:
                    self.assertEqual(writer.apply(op)["outcome"], "revised")
                    self.assertEqual(len(a.records), len(before["records"]) + 2)
                    self.assertEqual(writer.head(a.records[key({"id": "rec:d", "version": 2})], a.records), {"id": "rec:d", "version": 2})
                    query = copy.deepcopy(v["query"])
                    query["cut"]["memory"] = a.runtime["memory_cut"]
                    result = a.query(query)
                    self.assertEqual(result["currentness"], "current")
                    self.assertEqual([item["ref"] for item in result["items"]], [{"id": "rec:d", "version": 2}])


if __name__ == "__main__":
    unittest.main(verbosity=2)
