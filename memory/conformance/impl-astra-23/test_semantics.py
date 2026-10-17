"""Clause-derived positive/negative controls for corrected and newly released behavior."""

import copy
import pathlib
import unittest

from common import Grammar, ref, strict_loads
from engine import Engine
from run_vectors import compare, package_version

SPEC = pathlib.Path(__file__).resolve().parents[2] / "spec"


def vector(name):
    return strict_loads((SPEC / "kernel/vectors/semantic" / (name + ".json")).read_text())


def engine(v):
    return Engine(v["initial_state"], Grammar(SPEC / "kernel/schemas"), package_version(SPEC))


class Semantics(unittest.TestCase):
    # R7-020: authorized coverage uses the closed ref field; no declaration remains unknown.
    # A planted declaration spelling must fail both the exact comparison and closed view grammar.
    def test_coverage_mapping(self):
        v = vector("S30")
        report = engine(v).execute(v["operations"], v["query"])
        for sign in ("support", "oppose"):
            self.assertEqual(report["operation_results"][0]["items"][0][sign]["corpus_coverage"],
                             {"kind": "declared", "ref": {"id": "rec:coverage", "version": 1}})
            self.assertEqual(report["result"]["items"][0][sign]["corpus_coverage"], {"kind": "unknown"})
        self.assertEqual(compare(report, v, Grammar(SPEC / "kernel/schemas")), ([], []))
        planted = copy.deepcopy(report)
        coverage = planted["operation_results"][0]["items"][0]["support"]["corpus_coverage"]
        coverage["declaration"] = coverage.pop("ref")
        diffs, checks = compare(planted, v, Grammar(SPEC / "kernel/schemas"))
        self.assertTrue(any(p.endswith("/corpus_coverage/declaration") for p, _, _ in diffs))
        self.assertIn("response 0 violates closed view schema", checks)

    # K-DISC-2: missing second-owner evidence commits nothing; joint evidence permits release;
    # later owner revocation preserves the captured bytes but refuses new delivery.
    def test_joint_release_and_revocation(self):
        v = vector("P05")
        e = engine(v)
        before = copy.deepcopy(e.state)
        rejected = e.operation(v["operations"][0], 0)
        self.assertEqual(rejected, {"type": "refusal", "code": "declassification_invalid", "retryable": False})
        self.assertEqual(e.state, before)
        self.assertEqual(e.operation(v["operations"][1], 1)["outcome"], "declassified")
        saved = e.operation(v["operations"][2], 2)
        immutable = copy.deepcopy(saved)
        self.assertEqual(len(saved["items"]), 1)
        self.assertEqual(e.operation(v["operations"][3], 3)["outcome"], "delivered")
        self.assertEqual(e.operation(v["operations"][4], 4)["outcome"], "revoked")
        self.assertEqual(e.operation(v["operations"][5], 5)["code"], "disclosure_revoked")
        self.assertEqual(saved, immutable)
        self.assertEqual(e.read(v["query"])["items"], [])

    # K-DISC-1: the integration fact overrides model citations; missing facts refuse the whole batch.
    # Complete public lineage is a positive control beside tainted and unknown lineage.
    def test_lineage_bounds(self):
        v = vector("P13")
        e = engine(v)
        report = e.execute(v["operations"], v["query"])
        self.assertEqual(report["operation_results"][0]["outcome"], "admitted")
        self.assertEqual([i["content"][0]["value"] for i in report["result"]["items"]], ["candidate from only public context"])
        records = {r["envelope"]["id"]: r for r in e.state["records"]}
        self.assertEqual(records["rec:model-unknown"]["envelope"]["lineage"], "unknown")
        self.assertIn({"id": "rec:private-input", "version": 1}, records["rec:model-tainted"]["envelope"]["lineage"])
        e = engine(v)
        e.state["policy"]["lineage_facts"] = [f for f in e.state["policy"]["lineage_facts"] if f["output"]["id"] != "rec:model-clean"]
        before = copy.deepcopy(e.state)
        self.assertEqual(e.operation(v["operations"][0], 0)["code"], "invalid_reference")
        self.assertEqual(e.state, before)

    # K-PROJ-2: one version excludes an item; both old audience and issuer projections remain intact.
    def test_exclusion_is_projection_only(self):
        v = vector("P15")
        e = engine(v)
        before = copy.deepcopy(e.state)
        result = e.execute(v["operations"], v["query"])
        self.assertEqual([len(x["items"]) for x in result["operation_results"]], [2, 2])
        self.assertEqual(len(result["result"]["items"]), 1)
        self.assertEqual(e.state, before)

    # B01 in 0.2.0 omits a mandatory proposed revision lineage fact. Rejection has no partial state;
    # adding that exact direct integration fact in an isolated copy restores the expected revision.
    def test_b01_lineage_fact_control(self):
        v = vector("B01")
        e = engine(v)
        revision = v["operations"][0]["revision"]
        e.state["policy"]["lineage_facts"] = [f for f in e.state["policy"]["lineage_facts"] if f["output"] != ref(revision)]
        before = copy.deepcopy(e.state)
        self.assertEqual(e.operation(v["operations"][0], 0)["code"], "invalid_reference")
        self.assertEqual(e.state, before)
        template = copy.deepcopy(e.state["policy"]["lineage_facts"][0])
        template.update(output=ref(revision), kind="direct", inputs=[], complete=True)
        e.state["policy"]["lineage_facts"].append(template)
        actual = e.execute(v["operations"], v["query"])
        self.assertEqual(compare(actual, v, Grammar(SPEC / "kernel/schemas")), ([], []))


if __name__ == "__main__":
    unittest.main()
