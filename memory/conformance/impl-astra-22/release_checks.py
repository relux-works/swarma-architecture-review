"""Owner intersection, exact digest/pins and live release authority controls."""

import copy
import hashlib
import json
from pathlib import Path
import unittest

from adapter import Adapter
from boundary import Boundary
from evaluator import Refusal, canonical
from transactions import Transactions, key, ref


BASE = Path(__file__).resolve().parent


def fixture():
    return json.loads((BASE.parents[1] / "spec/kernel/vectors/semantic/P05.json").read_text())


class ReleaseControls(unittest.TestCase):
    def denied(self, adapter, op, code="declassification_invalid", boundary=False):
        before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy, adapter.captures))
        with self.assertRaisesRegex(Refusal, "^" + code + "$"):
            (Boundary(adapter) if boundary else Transactions(adapter)).apply(op)
        self.assertEqual((adapter.records, adapter.runtime, adapter.policy, adapter.captures), before)

    # One owner's evidence cannot lift the other owner's restriction. The full
    # batch commits assessments before output, in caller order, exactly once.
    def test_joint_owners_and_order(self):
        v = fixture()
        adapter = Adapter(v["initial_state"], "control")
        self.denied(adapter, v["operations"][0])
        result = Transactions(adapter).apply(v["operations"][1])
        self.assertEqual(result["outcome"], "declassified")
        self.assertEqual([adapter.records[key(r)]["envelope"]["recorded"]["sequence"]
                          for r in [ref(a) for a in v["operations"][1]["assessments"]] + [ref(v["operations"][1]["output"])]],
                         [101, 102, 103])
        self.assertEqual(len(adapter.runtime["idempotency"]), 1)

    # Body bytes, environment, decision owner and transformation must match
    # exactly; a model semantic review cannot supply release evidence.
    def test_exact_pins_and_executor(self):
        for variant in ("body", "environment", "owner", "transformation", "model"):
            v = fixture()
            op = v["operations"][1]
            if variant == "body":
                op["output"]["body"]["content"][0]["value"] += " changed"
            elif variant == "environment":
                op["assessments"][0]["body"]["pins"]["environment"]["version"] += 1
            elif variant == "owner":
                v["initial_state"]["policy"]["declassification_decisions"][0]["owner"] = "principal:other"
            elif variant == "transformation":
                op["assessments"][0]["body"]["declassification"]["transformation"]["version"] += 1
            else:
                op["assessments"][0]["body"].update(executor="model", check_kind="semantic_review")
            self.denied(Adapter(v["initial_state"], "control"), op)
        self.assertEqual(Transactions(Adapter(fixture()["initial_state"], "control")).apply(fixture()["operations"][1])["outcome"], "declassified")

    # K-JSON-2 framing is mandatory, independently of the wire oracle: a raw
    # canonical-body hash shared by both decision and assessment is still wrong.
    def test_framed_body_digest(self):
        for value in ("Synthetic City", "Քաղաք"):
            for framed in (False, True):
                with self.subTest(value=value, framed=framed):
                    v = fixture()
                    op = v["operations"][1]
                    op["output"]["body"]["content"][0]["value"] = value
                    raw = canonical(op["output"]["body"])
                    digest = hashlib.sha256((b"bounded-evidence:cjson-v1\x00" if framed else b"") + raw).hexdigest()
                    if value == "Synthetic City" and framed:
                        self.assertEqual(op["assessments"][0]["body"]["declassification"]["output_digest"], digest)
                    for assessment in op["assessments"]:
                        assessment["body"]["declassification"]["output_digest"] = digest
                    for decision in v["initial_state"]["policy"]["declassification_decisions"]:
                        decision["pins"]["output_digest"] = digest
                    adapter = Adapter(v["initial_state"], "control")
                    if framed:
                        self.assertEqual(Transactions(adapter).apply(op)["outcome"], "declassified")
                    else:
                        self.denied(adapter, op)

    # Revocation is owner-specific, leaves records/cuts and old capture intact,
    # filters new audience reads and refuses delivery of the prepared item.
    def test_current_revocation_and_snapshot(self):
        v = fixture()
        adapter = Adapter(v["initial_state"], "control")
        Transactions(adapter).apply(v["operations"][1])
        binding = {}
        prepared = adapter.query(v["operations"][2]["query"], binding=binding)
        self.assertEqual(len(prepared["items"]), 1)
        adapter.captures[2] = binding
        self.assertEqual(Boundary(adapter).apply(v["operations"][3])["outcome"], "delivered")
        wrong = copy.deepcopy(v["operations"][4])
        wrong["actor"] = "subj:h1"
        self.denied(adapter, wrong, "not_authorized", boundary=True)
        before = copy.deepcopy((adapter.records, adapter.runtime["memory_cut"], adapter.policy))
        Boundary(adapter).apply(v["operations"][4])
        self.assertEqual((adapter.records, adapter.runtime["memory_cut"], adapter.policy), before)
        self.assertEqual(adapter.query(v["query"])["items"], [])
        self.assertEqual(adapter.captures[2]["view"], prepared)
        self.denied(adapter, v["operations"][5], "disclosure_revoked", boundary=True)

    # A caller still needs the other owner's admitted representation. Live
    # inactive/revoked decisions cannot authorize a new atomic release.
    def test_representation_and_live_decisions(self):
        for variant, code in (("representation", "representation_invalid"),
                              ("inactive", "declassification_invalid"), ("revoked", "declassification_invalid")):
            v = fixture()
            if variant == "representation":
                v["initial_state"]["policy"]["representations"] = []
            elif variant == "inactive":
                v["initial_state"]["policy"]["declassification_decisions"][1]["active"] = False
            else:
                v["initial_state"]["runtime"]["revoked_declassifications"] = [v["operations"][4]["decision"]]
            self.denied(Adapter(v["initial_state"], "control"), v["operations"][1], code)

    # Unknown complete-input knowledge at either output or a transitive input
    # cannot be converted into release authority by repeating proposed citations.
    def test_unknown_lineage(self):
        for output_id in ("rec:city", "rec:coordinates"):
            v = fixture()
            next(f for f in v["initial_state"]["policy"]["lineage_facts"] if f["output"]["id"] == output_id)["complete"] = False
            if output_id == "rec:coordinates":
                next(r for r in v["initial_state"]["records"] if r["envelope"]["id"] == output_id)["envelope"]["lineage"] = "unknown"
            self.denied(Adapter(v["initial_state"], "control"), v["operations"][1])

    # A release applies only to its exact audience/purpose and preserves the
    # earliest inherited retention deadline, even when proposed output omits it.
    def test_scope_and_deadline(self):
        v = fixture()
        v["initial_state"]["records"][0]["envelope"]["disclosure"]["retain_until"] = "2026-10-18T00:00:00Z"
        private_rule = copy.deepcopy(v["initial_state"]["projection_rules"][0])
        private_rule.update(id="projection:main", family="issuer_current", audience=None, purpose=None)
        v["initial_state"]["projection_rules"].append(private_rule)
        adapter = Adapter(v["initial_state"], "control")
        Transactions(adapter).apply(v["operations"][1])
        output = adapter.records[key(ref(v["operations"][1]["output"]))]
        self.assertEqual(output["envelope"]["disclosure"]["retain_until"], "2026-10-18T00:00:00Z")
        query = copy.deepcopy(v["query"])
        self.assertEqual(len(adapter.query(query)["items"]), 1)
        query["projection_rule"] = {"id": "projection:main", "version": 1}
        query["purpose"] = "purpose:read"
        self.assertEqual(adapter.query(query)["items"], [])
        query["audience"] = "aud:private"
        self.assertEqual(len(adapter.query(query)["items"]), 1)

    # Admit, declassify and retain rights are independent. Exact later-stamp
    # replay preserves the first receipt but current retain denial blocks it.
    def test_rights_and_replay(self):
        for right in ("admit", "declassify", "retain"):
            v = fixture()
            for grant in v["initial_state"]["policy"]["grants"]:
                grant["rights"] = [r for r in grant["rights"] if r != right]
            self.denied(Adapter(v["initial_state"], "control"), v["operations"][1], "not_authorized")
        v = fixture()
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        first = writer.apply(v["operations"][1])
        retry = copy.deepcopy(v["operations"][1])
        retry["context"]["at"] = "2026-10-17T00:00:01Z"
        before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy))
        self.assertEqual(writer.apply(retry), first)
        self.assertEqual((adapter.records, adapter.runtime, adapter.policy), before)
        adapter.runtime["revocations"].append({"owner": adapter.policy["owner"], "principal": retry["context"]["actor"],
                                                "right": "retain", "at": retry["context"]["at"], **retry["context"]["retention_context"]})
        self.denied(adapter, retry, "not_authorized")
        self.assertEqual(adapter.runtime["idempotency"][0]["receipt"], first)

    # The lifted owner's restriction may originate deeper than direct inputs;
    # both assessments still pin the same exact direct input set and output.
    def test_transitive_constraint_owner(self):
        v = fixture()
        policy = v["initial_state"]["policy"]
        direct = [{"id": "rec:private-preference", "version": 1}]
        ancestor = {"id": "rec:coordinates", "version": 1}
        preference = next(r for r in v["initial_state"]["records"] if ref(r) == direct[0])
        preference["envelope"]["lineage"] = [ancestor]
        preference["envelope"]["disclosure"].update(audiences=["aud:private", "aud:public"], field_classes=["public"])
        for fact in policy["lineage_facts"]:
            if fact["output"]["id"] == "rec:city":
                fact["inputs"] = copy.deepcopy(direct)
            elif fact["output"] == direct[0]:
                fact.update(kind="deterministic", inputs=[ancestor])
        policy["constraint_owners"] = [{"input": ancestor, "owners": ["principal:owner-b"]},
                                         {"input": direct[0], "owners": ["subj:h1"]}]
        op = copy.deepcopy(v["operations"][1])
        op["output"]["envelope"]["lineage"] = copy.deepcopy(direct)
        for assessment in op["assessments"]:
            assessment["body"]["declassification"]["inputs"] = copy.deepcopy(direct)
        for decision in policy["declassification_decisions"]:
            decision["pins"]["inputs"] = copy.deepcopy(direct)
        missing = copy.deepcopy(op)
        missing["assessments"] = missing["assessments"][:1]
        missing["output"]["envelope"]["disclosure"]["declassification"] = [ref(missing["assessments"][0])]
        self.denied(Adapter(v["initial_state"], "control"), missing)
        self.assertEqual(Transactions(Adapter(v["initial_state"], "control")).apply(op)["outcome"], "declassified")


if __name__ == "__main__":
    unittest.main(verbosity=2)
