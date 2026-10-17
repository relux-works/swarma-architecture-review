"""Wire-mapping regression controls, separate from pre-package source controls."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter


class AssociationControls(unittest.TestCase):
    # R7-029 exact wire probes: empty/resolvable named sources use resolvable_now;
    # unavailable independent sources remain attested, with unchanged root kind.
    def test_independent_source_precedence(self):
        base = Path(__file__).resolve().parent / "fixtures"
        fixture = json.loads((base / "independent-resolvable-judge-first.json").read_text())
        for name, state in fixture["states"].items():
            with self.subTest(name=name):
                item = Adapter(state, "control").query(fixture["query"])["items"][0]
                self.assertEqual(item["support"]["source_state"], fixture["expected_support_source_state"][name])
                self.assertEqual(item["support"]["evidence_qualification"], ["semantic_review"])
                self.assertEqual(item["support"]["witness"], "present")
                self.assertEqual(item["support"]["evaluation"], "complete")
                self.assertEqual(item["oppose"]["witness"], "not_found")
        empty = json.loads((base / "independent-vacuous-source-first.json").read_text())
        item = Adapter(empty["initial_state"], "control").query(empty["query"])["items"][0]
        self.assertEqual(item["support"]["source_state"], "resolvable_now")
        self.assertEqual(item["support"]["evidence_qualification"], ["semantic_review"])

    # R7-028: wire source bounds are clamped by policy and count original source
    # references across synthetic groups. Only found paths add derived provenance.
    def test_source_limit_wire_mapping(self):
        path = Path(__file__).resolve().parents[1] / "cases/astra-24-source-resolution-budget.vector.json"
        fixture = json.loads(path.read_text())
        initial = copy.deepcopy(fixture["initial_state"])
        query = copy.deepcopy(fixture["operations"][0]["query"])
        limited = copy.deepcopy(initial)
        limited["policy"]["limits"]["read"]["source_resolutions"] = 0
        result = Adapter(limited, "control").query(query)
        self.assertEqual(result["items"][0]["support"]["witness"], "not_found")
        self.assertEqual(result["cutoffs"], ["source_limit"])
        self.assertEqual(result["items"][0]["source_refs"], [])
        original = next(r for r in initial["records"] if r["envelope"]["kind"] == "assessment" and r["body"]["sources"])
        repeated = copy.deepcopy(original)
        repeated["envelope"]["id"] = "rec:repeated-source-control"
        repeated["envelope"]["recorded"]["sequence"] = 98
        repeated["body"]["origin"] = "origin:repeated-source-control"
        initial["records"].append(repeated)
        fact = copy.deepcopy(next(f for f in initial["policy"]["lineage_facts"]
                                  if f["output"]["id"] == original["envelope"]["id"]))
        fact["output"] = {"id": repeated["envelope"]["id"], "version": repeated["envelope"]["version"]}
        initial["policy"]["lineage_facts"].append(fact)
        result = Adapter(initial, "control").query(query)
        self.assertEqual(result["items"][0]["support"]["independent_root_count"], 2)
        self.assertEqual(result["items"][0]["support"]["evaluation"], "complete")
        original_source = next(r for r in initial["records"] if r["envelope"]["kind"] == "source")
        source = copy.deepcopy(original_source)
        source["envelope"]["id"] = "rec:distinct-source-control"
        source["envelope"]["recorded"]["sequence"] = 97
        initial["records"].append(source)
        fact = copy.deepcopy(next(f for f in initial["policy"]["lineage_facts"]
                                  if f["output"]["id"] == original_source["envelope"]["id"]))
        fact["output"] = {"id": source["envelope"]["id"], "version": source["envelope"]["version"]}
        initial["policy"]["lineage_facts"].append(fact)
        repeated["body"]["sources"] = [{"id": source["envelope"]["id"], "version": source["envelope"]["version"]}]
        result = Adapter(initial, "control").query(query)
        self.assertEqual(result["items"][0]["support"]["independent_root_count"], 1)
        self.assertEqual(result["items"][0]["support"]["evaluation"], "incomplete")
        self.assertEqual(result["cutoffs"], ["source_limit"])
        self.assertNotIn(repeated["body"]["sources"][0], result["items"][0]["source_refs"])
        query["bounds"]["source_resolutions"] = 2
        result = Adapter(initial, "control").query(query)
        self.assertEqual(result["items"][0]["support"]["independent_root_count"], 2)
        self.assertEqual(result["items"][0]["support"]["evaluation"], "complete")

    # R7-025: explicit targets include history only from their own sequences.
    # Unfiltered selection retains other visible history; displayed old targets
    # are not duplicated, and hidden old records do not appear in history.
    def test_selected_sequence_history(self):
        path = Path(__file__).resolve().parent / "fixtures/selected-history.json"
        fixture = json.loads(path.read_text())
        for name, query in fixture["queries"].items():
            with self.subTest(name=name):
                result = Adapter(fixture["state"], "control").query(query)
                self.assertEqual(result["historical"], fixture["expected_historical"][name])
        hidden = copy.deepcopy(fixture["state"])
        for record in hidden["records"]:
            if record["envelope"]["id"] == "rec:other-sequence" and record["envelope"]["version"] == 1:
                record["envelope"]["disclosure"]["audiences"] = ["aud:private"]
        result = Adapter(hidden, "control").query(fixture["queries"]["unfiltered"])
        self.assertEqual(result["historical"], [])
        self.assertTrue(any(item["ref"] == {"id": "rec:a", "version": 1} for item in result["items"]))

    # R7-013: the admitted mirror fixture discloses documentary attribution across
    # source/observer perspectives, without creating a semantic witness. Removing
    # the source's read grant removes its reference without leaking an error.
    def test_documentary_association_obeys_visibility(self):
        path = Path(__file__).resolve().parents[2] / "spec/kernel/vectors/semantic/S23.json"
        vector = json.loads(path.read_text())
        initial, query = vector["initial_state"], vector["query"]
        item = Adapter(initial, "control").query(query)["items"][0]
        self.assertEqual(item["source_refs"], [{"id": "rec:mirror", "version": 1}])
        self.assertEqual(item["support"]["witness"], "not_found")
        self.assertEqual(item["authority_receipt"], None)
        hidden = copy.deepcopy(initial)
        allowed = [r["envelope"]["id"] for r in initial["records"] if r["envelope"]["kind"] != "source"]
        for grant in hidden["policy"]["grants"]:
            grant["records"] = allowed
        item = Adapter(hidden, "control").query(query)["items"][0]
        self.assertEqual(item["source_refs"], [])
        self.assertEqual(item["support"]["witness"], "not_found")
        self.assertEqual(item["support"]["evaluation"], "complete")

    # Basic audience projection uses its own subject handle and hides memory
    # references. A missing exact alias refuses rather than leaking the subject.
    def test_audience_alias_and_missing_mapping(self):
        path = Path(__file__).resolve().parents[2] / "spec/kernel/vectors/semantic/P09.json"
        vector = json.loads(path.read_text())
        initial, query = vector["initial_state"], vector["query"]
        before = copy.deepcopy(initial)
        result = Adapter(initial, "control").query(query)
        item = result["items"][0]
        mapping = next(h for h in initial["policy"]["handles"]
                       if h["subject"] == query["scope"]["subject"] and h["space"] == query["scope"]["space"]
                       and h["audience"] == query["audience"])
        self.assertEqual(item["subject"], mapping["handle"])
        self.assertIsNone(item["ref"])
        self.assertEqual(item["source_refs"], [])
        self.assertNotIn("lineage", item)
        self.assertEqual(initial, before)
        missing = copy.deepcopy(initial)
        missing["policy"]["handles"].remove(mapping)
        self.assertEqual(Adapter(missing, "control").query(query),
                         {"type": "refusal", "code": "not_authorized", "retryable": False})


if __name__ == "__main__":
    unittest.main(verbosity=2)
