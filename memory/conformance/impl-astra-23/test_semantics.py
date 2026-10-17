"""Clause-derived positive/negative controls for corrected and newly released behavior."""

import copy
import pathlib
import unittest

from common import Grammar, Refused, ref, strict_loads
from engine import Engine
from run_vectors import compare, package_version

SPEC = pathlib.Path(__file__).resolve().parents[2] / "spec"


def vector(name):
    return strict_loads((SPEC / "kernel/vectors/semantic" / (name + ".json")).read_text())


def engine(v):
    return Engine(v["initial_state"], Grammar(SPEC / "kernel/schemas"), package_version(SPEC))


class Semantics(unittest.TestCase):
    # K-EVAL-8: hidden causes preserve global dirtiness while public evidence remains complete;
    # the exact same cause is dirty/incomplete for the separately authorized private query.
    def test_dirty_cause_authorization(self):
        v = vector("S24")
        e = engine(v)
        report = e.execute(v["operations"], v["query"])
        self.assertIn({"id": "rec:a", "version": 1}, e.state["runtime"]["dirty"])
        self.assertTrue(e.state["runtime"]["dirty_causes"])
        public = report["result"]
        self.assertEqual(public["cutoffs"], [])
        self.assertEqual(public["review_required"], [])
        self.assertEqual(public["items"][0]["support"]["witness"], "present")
        self.assertEqual(public["items"][0]["support"]["evaluation"], "complete")
        private = report["operation_results"][3]
        self.assertEqual(private["cutoffs"], ["dirty"])
        self.assertTrue(private["items"][0]["needs_review"])
        self.assertEqual(private["items"][0]["support"]["evaluation"], "incomplete")

    # K-ENV-1: identity is explicit, not string equality. Wrong-subject proposals are atomic
    # refusals; a trusted binding permits distinct subject/principal strings. Invalid snapshots reject.
    def test_self_declaration_identity(self):
        v = vector("P02")
        e = engine(v)
        before = copy.deepcopy(e.state)
        self.assertEqual(e.operation(v["operations"][1], 1)["code"], "invalid_domain_value")
        self.assertEqual(e.state, before)
        self.assertEqual(e.operation(v["operations"][2], 2)["outcome"], "admitted")
        initial = copy.deepcopy(v)
        initial["initial_state"]["policy"]["subject_principals"] = []
        with self.assertRaises(Refused) as caught:
            engine(initial)
        self.assertEqual(caught.exception.code, "invalid_domain_value")

    # K-EVAL-9: an explicit multi-sequence target must not collect another sequence's history;
    # the same authorized unfiltered projection may include that other sequence's old version.
    def test_history_stays_in_selected_sequence(self):
        v = vector("S24")
        e = engine(v)
        for index, operation in enumerate(v["operations"][:3]):
            e.operation(operation, index)
        q = copy.deepcopy(v["operations"][3]["query"])
        self.assertEqual(e.read(q)["historical"], [])
        q["scope"]["targets"] = []
        self.assertEqual(e.read(q)["historical"], [{"id": "rec:hidden", "version": 1}])
        q["scope"]["targets"] = [{"id": "rec:hidden", "version": 1}]
        historical = e.read(q)
        self.assertEqual(historical["items"][0]["currentness"], "historical")
        self.assertEqual(historical["items"][0]["ref"], {"id": "rec:hidden", "version": 1})
        self.assertEqual(historical["historical"], [])
        q["scope"]["targets"] = []
        q["audience"] = "aud:public"
        public = e.read(q)
        self.assertEqual(public["historical"], [])
        self.assertEqual([i["ref"] for i in public["items"]], [{"id": "rec:a", "version": 1}])

    # K-EVAL-5/K-AUTH-1: a found derived witness retains its authorized exact source;
    # hiding that source removes both the witness and source metadata before accounting.
    def test_derived_source_references(self):
        path = SPEC.parent / "conformance/cases/astra-24-derived-source-refs.vector.json"
        v = strict_loads(path.read_text())
        result = engine(v).execute(v["operations"], v["query"])["result"]
        self.assertEqual(result["items"][0]["source_refs"], [{"id": "rec:s", "version": 1}])
        self.assertEqual(result["items"][0]["support"]["witness"], "present")
        direct = copy.deepcopy(v["query"])
        direct["scope"]["targets"] = [{"id": "rec:a", "version": 1}]
        self.assertEqual(engine(v).read(direct)["items"][0]["source_refs"], [{"id": "rec:s", "version": 1}])
        unrelated = copy.deepcopy(next(r for r in v["initial_state"]["records"] if r["envelope"]["kind"] == "source"))
        unrelated["envelope"]["id"] = "rec:unrelated-copy"
        unrelated["envelope"]["recorded"]["sequence"] = 99
        v["initial_state"]["records"].append(unrelated)
        fact = copy.deepcopy(next(f for f in v["initial_state"]["policy"]["lineage_facts"] if f["output"]["id"] == "rec:s"))
        fact["output"] = ref(unrelated)
        v["initial_state"]["policy"]["lineage_facts"].append(fact)
        result = engine(v).execute(v["operations"], v["query"])["result"]
        self.assertEqual(result["items"][0]["source_refs"], [{"id": "rec:s", "version": 1}])
        unfound = copy.deepcopy(v)
        for r in unfound["initial_state"]["records"]:
            if r["envelope"]["kind"] == "assessment" and r["body"]["target"] is not None:
                r["body"]["result"] = "fail"
        item = engine(unfound).execute(unfound["operations"], unfound["query"])["result"]["items"][0]
        self.assertEqual(item["source_refs"], [])
        self.assertEqual(item["support"]["witness"], "not_found")
        for record in v["initial_state"]["records"]:
            if record["envelope"]["kind"] == "source":
                record["envelope"]["disclosure"]["audiences"] = ["aud:private"]
        result = engine(v).execute(v["operations"], v["query"])["result"]
        self.assertEqual(result["items"][0]["source_refs"], [])
        self.assertEqual(result["items"][0]["support"]["witness"], "not_found")
        self.assertEqual(result["items"][0]["support"]["evaluation"], "complete")
        self.assertEqual(result["cutoffs"], [])

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
