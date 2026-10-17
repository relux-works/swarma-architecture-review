"""0.2.6 K-REV-3 controls derived only from the released package."""

import copy
import itertools
import pathlib
import unittest

from common import Grammar, ref, strict_loads
from engine import Engine
from run_vectors import compare, package_version, put

SPEC = pathlib.Path(__file__).resolve().parents[2] / "spec"


def vector(name):
    return strict_loads((SPEC / "kernel/vectors/semantic" / (name + ".json")).read_text())


def engine(v):
    grammar = Grammar(SPEC / "kernel/schemas")
    assert grammar.matches(v["initial_state"], grammar.schemas["fixture"]["properties"]["initial_state"])
    return Engine(v["initial_state"], grammar, package_version(SPEC))


def snapshot(e):
    return copy.deepcopy((e.state, e.captures, e.view_bindings, e.dirty_since))


def graph_cases():
    # All eight acyclic edge subsets on three ordered events; policy attribution,
    # carrier attribution and event-list order vary independently (64 admitted inputs).
    for mask, own_middle, own_carrier, reverse in itertools.product(range(8), (False, True), (False, True), (False, True)):
        v = vector("S34")
        events = v["initial_state"]["policy"]["authority_events"]
        first, middle, last = events
        middle["issuer"] = "subj:h1" if own_middle else "subj:h2"
        middle["predecessors"] = [copy.deepcopy(first["receipt"])] if mask & 4 else []
        last["predecessors"] = ([copy.deepcopy(first["receipt"])] if mask & 1 else []) + (
            [copy.deepcopy(middle["receipt"])] if mask & 2 else [])
        carrier = next(r["envelope"] for r in v["initial_state"]["records"] if ref(r) == middle["receipt"])
        carrier["issuer"] = carrier["submitter"] = "subj:h1" if own_carrier else "subj:h2"
        carrier["perspective"]["principal"] = carrier["issuer"]
        if reverse:
            events.reverse()
        # On this three-node DAG, exactly a direct edge or an all-H two-edge chain qualifies.
        ordered = bool(mask & 1 or (mask & 2 and mask & 4 and own_middle))
        yield (mask, own_middle, own_carrier, reverse), v, ordered


class Authority(unittest.TestCase):
    # K-REV-3: the bounded graph matrix proves no contraction, one-path sufficiency,
    # assertion-free traversal and protected-event attribution across projection and CAS.
    def test_projection_graph_matrix(self):
        for label, v, ordered in graph_cases():
            with self.subTest(graph=label):
                e = engine(v)
                first = {"id": "rec:receipt1", "version": 1}
                last = {"id": "rec:receipt3", "version": 1}
                self.assertEqual(e.authority_succeeds(last, first), ordered)
                self.assertFalse(e.authority_succeeds(first, last))
                self.assertFalse(e.authority_succeeds(last, last))
                target = next(r for r in e.state["records"] if ref(r) == {"id": "rec:d", "version": 1})
                self.assertEqual(e.revision_head(target), {"id": "rec:d", "version": 3} if ordered else None)
                before = copy.deepcopy((e.state, e.captures, e.dirty_since))
                result = e.read(v["query"])
                self.assertEqual(result["currentness"], "current" if ordered else "ambiguous_current")
                self.assertEqual([i["ref"]["version"] for i in result["items"]], [3] if ordered else [1, 3])
                self.assertEqual(result["historical"], [{"id": "rec:d", "version": 1}] if ordered else [])
                self.assertEqual((e.state, e.captures, e.dirty_since), before)
                self.assertEqual(len(e.view_bindings), 1)  # An authorized read creates only its ephemeral binding.
                self.assertTrue(e.grammar.matches(result, e.grammar.schemas["view"]))

    # K-REV-3: exact foreign-edge removal pairs preserve both established and absent order;
    # only declared fresh handles are normalized when comparing complete observations.
    def test_foreign_edit_invariance(self):
        for left, right in (("S34", "S37"), ("S36", "S38")):
            with self.subTest(pair=(left, right)):
                reports = []
                for name in (left, right):
                    v = vector(name)
                    e = engine(v)
                    actual = e.execute(v["operations"], v["query"])
                    self.assertEqual(compare(actual, v, e.grammar), ([], []))
                    for path in v["normalization"]["fresh_handles"]:
                        put(actual, path, "<fresh-handle>")
                    reports.append(actual)
                self.assertEqual(*reports)

    # K-REV-3/K-REV-1: both relations refuse a mixed-only path without any native mutation.
    # The same key succeeds after adding qualifying order; replay stays immutable and stale CAS refuses.
    def test_revision_relation_atomicity(self):
        refusal = {"type": "refusal", "code": "authority_receipt_required", "retryable": False}
        conflict = {"type": "refusal", "code": "version_conflict", "retryable": True}
        for relation, shape in itertools.product(("replace", "correct"), ("mixed", "own_chain", "mixed_direct")):
            with self.subTest(relation=relation, shape=shape):
                v = vector("S39")
                events = v["initial_state"]["policy"]["authority_events"]
                if shape == "own_chain":
                    events[1]["issuer"] = "subj:h1"
                elif shape == "mixed_direct":
                    events[2]["predecessors"].insert(0, copy.deepcopy(events[0]["receipt"]))
                e = engine(v)
                op = copy.deepcopy(v["operations"][0 if relation == "replace" else 1])
                self.assertTrue(e.grammar.matches(op, e.grammar.schemas["vector"]["properties"]["operations"]["items"]))
                if shape == "mixed":
                    before = snapshot(e)
                    self.assertEqual(e.operation(op, 0), refusal)
                    self.assertEqual(snapshot(e), before)
                    e.state["policy"]["authority_events"][1]["issuer"] = "subj:h1"
                before = snapshot(e)
                success = e.operation(op, 1)
                self.assertEqual(success.get("outcome"), "revised", success)
                self.assertEqual(len(e.state["records"]), len(before[0]["records"]) + 2)
                self.assertEqual(e.state["runtime"]["memory_cut"], before[0]["runtime"]["memory_cut"] + 2)
                self.assertEqual(e.state["runtime"]["dirty"], [{"id": "rec:dependent", "version": 1}])
                self.assertEqual(len(e.state["runtime"]["idempotency"]), 1)
                before = snapshot(e)
                self.assertEqual(e.operation(op, 2), success)
                self.assertEqual(snapshot(e), before)
                stale = copy.deepcopy(op)
                stale["idempotency_key"] = "key:issuer-stale"
                self.assertEqual(e.operation(stale, 3), conflict)
                self.assertEqual(snapshot(e), before)
                q = copy.deepcopy(v["query"])
                q["cut"]["memory"] = e.state["runtime"]["memory_cut"]
                result = e.read(q)
                self.assertEqual(result["currentness"], "current")
                self.assertEqual([i["ref"] for i in result["items"]], [{"id": "rec:d", "version": 2}])

    # K-REV-3/K-REV-1: failed succession reserves no key; ordinary mixed import is admissible,
    # creates ambiguity without a revision/dirty effect, and exact replay survives ambiguous CAS.
    def test_plain_import_and_ambiguous_cas(self):
        v = vector("S39")
        e = engine(v)
        for index in (0, 1):
            before = snapshot(e)
            self.assertEqual(e.operation(v["operations"][index], index),
                             {"type": "refusal", "code": "authority_receipt_required", "retryable": False})
            self.assertEqual(snapshot(e), before)
        admitted = e.operation(v["operations"][4], 4)
        self.assertEqual(admitted["outcome"], "admitted")
        self.assertFalse(any(r["envelope"]["kind"] == "revision" for r in e.state["records"]))
        self.assertEqual(e.state["runtime"]["dirty"], [])
        result = e.read(v["query"])
        self.assertEqual(result["currentness"], "ambiguous_current")
        self.assertEqual([i["ref"]["version"] for i in result["items"]], [1, 2])
        self.assertEqual(result["historical"], [])
        before = snapshot(e)
        self.assertEqual(e.operation(v["operations"][5], 5),
                         {"type": "refusal", "code": "version_conflict", "retryable": True})
        self.assertEqual(snapshot(e), before)
        self.assertEqual(e.operation(v["operations"][6], 6), admitted)
        self.assertEqual(snapshot(e), before)


if __name__ == "__main__":
    unittest.main()
