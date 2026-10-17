"""Atomic wire transaction controls; package inputs are fixtures, not oracles."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter
from evaluator import Refusal
from transactions import Transactions, key, ref


ROOT = Path(__file__).resolve().parents[2] / "spec/kernel/vectors/semantic"


def fixture(name):
    return json.loads((ROOT / (name + ".json")).read_text())


class AtomicControls(unittest.TestCase):
    # R7-040 NEXT: after withdrawing the unique current authority record, the
    # next active receipt candidate is writable. Frozen captures remain history.
    def test_authority_next_after_withdrawal(self):
        path = Path(__file__).resolve().parents[1] / "cases/astra-24-ambiguous-cas-next.vector.json"
        v = json.loads(path.read_text())
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        receipts = []
        for op in v["operations"]:
            if op["op"] == "revise":
                receipts.append(writer.apply(op))
        self.assertEqual([r["outcome"] for r in receipts], ["revised", "revised"])
        self.assertEqual(adapter.runtime["memory_cut"], 102)
        self.assertEqual(len(adapter.runtime["idempotency"]), 2)
        self.assertEqual(len(adapter.records), 8)

    # R7-040: ambiguous and historical authority candidates refuse atomically;
    # a uniquely ordered current candidate and challenge exemption still succeed.
    def test_authority_slot_cas(self):
        base = Path(__file__).resolve().parents[1] / "cases"
        for suffix, outcome in (("", None), ("-stale", None), ("-control", "revised"),
                                ("-challenge", "challenged")):
            with self.subTest(suffix=suffix):
                v = json.loads((base / ("astra-24-ambiguous-cas" + suffix + ".vector.json")).read_text())
                adapter = Adapter(v["initial_state"], "control")
                writer = Transactions(adapter)
                before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy))
                if outcome is None:
                    with self.assertRaisesRegex(Refusal, "version_conflict"):
                        writer.apply(v["operations"][-1])
                    self.assertEqual((adapter.records, adapter.runtime, adapter.policy), before)
                else:
                    self.assertEqual(writer.apply(v["operations"][-1])["outcome"], outcome)
                    self.assertEqual(adapter.runtime["dirty"], [])
                    self.assertEqual(len(adapter.records), len(before[0]) + 1)

    # A later admitted authority event can resolve incomparable candidates.
    # Exact old receipt replay precedes a newly advanced authority head/CAS.
    def test_authority_advancement_and_replay(self):
        base = Path(__file__).resolve().parents[1] / "cases"
        v = json.loads((base / "astra-24-ambiguous-cas-control.vector.json").read_text())
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        original_op = v["operations"][-1]
        first = writer.apply(original_op)
        source = copy.deepcopy(adapter.records[key({"id": "rec:receipt3", "version": 1})])
        decision = copy.deepcopy(adapter.records[key({"id": "rec:d", "version": 3})])
        source["envelope"]["id"] = "rec:receipt4"
        source["body"]["object"] = "object:receipt4"
        decision["envelope"]["version"] = 4
        decision["body"]["authority_receipt"] = ref(source)
        for proposal in (source, decision):
            for field in ("recorded", "submitter", "admission_class"):
                proposal["envelope"].pop(field)
            adapter.policy["reviews"].append({"record": ref(proposal), "reviewer": "subj:h1", "result": "allow"})
            adapter.policy["lineage_facts"].append({"output": ref(proposal), "profile": {"id": "integration:synthetic", "version": 1},
                                                    "kind": "direct", "inputs": [], "complete": True})
        adapter.policy["authority_events"].append({"receipt": ref(source), "issuer": "subj:h1",
                                                   "predecessors": [{"id": "rec:receipt2", "version": 1},
                                                                    {"id": "rec:receipt3", "version": 1}], "canonical": True})
        admission = {"op": "admit", "context": copy.deepcopy(original_op["context"]), "idempotency_key": "key:later-authority",
                     "proposals": [source, decision], "expected_generation": 0}
        self.assertEqual(writer.apply(admission)["outcome"], "admitted")
        before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy))
        self.assertEqual(writer.apply(original_op), first)
        self.assertEqual((adapter.records, adapter.runtime, adapter.policy), before)
        later = copy.deepcopy(original_op)
        later["idempotency_key"] = "key:latest-withdraw"
        later["expected_version"] = ref(decision)
        later["revision"]["envelope"]["id"] = "rec:withdraw-latest"
        later["revision"]["body"]["target"] = ref(decision)
        proposal = later["revision"]
        adapter.policy["reviews"].append({"record": ref(proposal), "reviewer": "subj:h1", "result": "allow"})
        adapter.policy["lineage_facts"].append({"output": ref(proposal), "profile": {"id": "integration:synthetic", "version": 1},
                                               "kind": "direct", "inputs": [], "complete": True})
        self.assertEqual(writer.apply(later)["outcome"], "revised")
        # The same common successor also produces one head from the original
        # incomparable receipt graph, independently of memory arrival order.
        adapter.policy["authority_events"][2]["predecessors"] = [{"id": "rec:receipt1", "version": 1}]
        self.assertEqual(writer.head(decision, adapter.records), {"id": "rec:d", "version": 2})

    # R7-030: an admitted snapshot replays the exact old receipt across intake
    # times, rejects changed intent, and preserves all records/runtime state.
    def test_initial_idempotency_snapshot(self):
        data = json.loads((Path(__file__).parent / "fixtures/persisted-idempotency-judge-first.json").read_text())
        adapter = Adapter(data["initial_state"], "control")
        writer = Transactions(adapter)
        before = copy.deepcopy((adapter.records, adapter.runtime))
        for op in data["operations"][:2]:
            self.assertEqual(writer.apply(op), data["expected_operation_results"][0])
        with self.assertRaisesRegex(Refusal, "idempotency_conflict"):
            writer.apply(data["operations"][2])
        self.assertEqual((adapter.records, adapter.runtime), before)

    # A successful write persists a complete replay entry. Reconstructing the
    # semantic adapter retains the handle and first recorded time; this is not
    # a process crash/durable-storage qualification.
    def test_successful_idempotency_reconstruction(self):
        v = fixture("S14")
        adapter = Adapter(v["initial_state"], "control")
        result = Transactions(adapter).apply(v["operations"][0])
        self.assertEqual(len(adapter.runtime["idempotency"]), 1)
        self.assertEqual(adapter.runtime["idempotency"][0]["receipt"], result)
        snapshot = copy.deepcopy(v["initial_state"])
        snapshot.update(records=list(adapter.records.values()), runtime=adapter.runtime)
        restored = Adapter(snapshot, "control")
        before = copy.deepcopy((restored.records, restored.runtime))
        self.assertEqual(Transactions(restored).apply(v["operations"][1]), result)
        self.assertEqual((restored.records, restored.runtime), before)
        e = restored.records[key(result["refs"][0])]["envelope"]
        self.assertEqual(e["recorded"]["at"], v["operations"][0]["context"]["at"])

    # Actor, space and key each isolate an existing receipt. Each different
    # identity admits a valid neighboring record and preserves the original entry.
    def test_idempotency_identity_scope(self):
        data = json.loads((Path(__file__).parent / "fixtures/persisted-idempotency-judge-first.json").read_text())
        for dimension in ("actor", "space", "key"):
            with self.subTest(dimension=dimension):
                adapter = Adapter(data["initial_state"], "control")
                original = copy.deepcopy(adapter.runtime["idempotency"][0])
                op = copy.deepcopy(data["operations"][0])
                proposal = op["proposals"][0]
                proposal["envelope"]["id"] = "rec:neighbor"
                if dimension == "actor":
                    op["context"]["actor"] = "subj:other"
                    proposal["envelope"]["issuer"] = "subj:other"
                    proposal["envelope"]["perspective"]["principal"] = "subj:other"
                elif dimension == "space":
                    proposal["envelope"]["space"] = "space:other"
                else:
                    op["idempotency_key"] = "key:other"
                grant = copy.deepcopy(adapter.policy["grants"][0])
                grant.update(principal=op["context"]["actor"], space=proposal["envelope"]["space"])
                adapter.policy["grants"].append(grant)
                fact = copy.deepcopy(adapter.policy["lineage_facts"][0])
                fact["output"] = ref(proposal)
                adapter.policy["lineage_facts"].append(fact)
                adapter.policy["reviews"].append({"record": ref(proposal), "reviewer": op["context"]["actor"], "result": "allow"})
                result = Transactions(adapter).apply(op)
                self.assertEqual(result["outcome"], "admitted")
                self.assertEqual(result["refs"], [ref(proposal)])
                self.assertEqual(adapter.runtime["idempotency"][0], original)
                self.assertEqual(len(adapter.runtime["idempotency"]), 2)

    # Current actor/space admission authority precedes replay; unrelated rights
    # cannot reveal an old receipt and refusal changes no state.
    def test_idempotency_current_authorization(self):
        data = json.loads((Path(__file__).parent / "fixtures/persisted-idempotency-judge-first.json").read_text())
        adapter = Adapter(data["initial_state"], "control")
        grants = copy.deepcopy(adapter.policy["grants"])
        for grant in adapter.policy["grants"]:
            grant["rights"].remove("admit")
        neighbor = copy.deepcopy(grants[0])
        neighbor["principal"] = "subj:other"
        adapter.policy["grants"].append(neighbor)
        before = copy.deepcopy((adapter.records, adapter.runtime))
        with self.assertRaisesRegex(Refusal, "not_authorized"):
            Transactions(adapter).apply(data["operations"][0])
        self.assertEqual((adapter.records, adapter.runtime), before)
        adapter.policy["grants"] = grants
        self.assertEqual(Transactions(adapter).apply(data["operations"][0]), data["expected_operation_results"][0])

    # R7-026: wrong-subject, equal-spelling-without-binding and non-own
    # self-declarations refuse atomically. Distinct bound identities are valid.
    def test_self_declaration_identity(self):
        v = fixture("P02")
        for case in ("wrong_subject", "equal_without_binding", "observer"):
            with self.subTest(case=case):
                adapter = Adapter(v["initial_state"], "control")
                writer = Transactions(adapter)
                op = copy.deepcopy(v["operations"][1 if case == "wrong_subject" else 2])
                if case == "equal_without_binding":
                    op["proposals"][0]["envelope"]["subject"] = op["context"]["actor"]
                    adapter.policy["subject_principals"] = []
                if case == "observer":
                    op["proposals"][0]["envelope"]["perspective"]["kind"] = "observer"
                before = copy.deepcopy((adapter.records, adapter.runtime, writer.idempotency))
                with self.assertRaisesRegex(Refusal, "invalid_domain_value"):
                    writer.apply(op)
                self.assertEqual((adapter.records, adapter.runtime, writer.idempotency), before)
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        result = writer.apply(v["operations"][2])
        self.assertEqual(result["outcome"], "admitted")
        e = adapter.records[key(result["refs"][0])]["envelope"]
        self.assertEqual(e["subject"], "subj:separate-handle")
        self.assertEqual(e["issuer"], "principal:person")
        self.assertEqual(adapter.runtime["memory_cut"], 101)

    # Representation changes the submitter only; a valid bound self-declaration
    # remains accepted with the original subject, issuer and own perspective.
    def test_represented_self_declaration(self):
        v = fixture("P10")
        adapter = Adapter(v["initial_state"], "control")
        op = v["operations"][0]
        self.assertEqual(Transactions(adapter).apply(op)["outcome"], "revised")
        e = adapter.records[key(ref(op["replacement"]))]["envelope"]
        original = op["replacement"]["envelope"]
        for field in ("subject", "issuer", "perspective"):
            self.assertEqual(e[field], original[field])
        self.assertEqual(e["submitter"], op["context"]["actor"])
        self.assertNotEqual(e["submitter"], e["issuer"])

    # Exact retries (including a fresh intake timestamp) reuse the receipt and
    # original sequence. Changed intent fails and leaves all state unchanged.
    def test_idempotency_and_atomic_conflict(self):
        v = fixture("S14")
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        first = writer.apply(v["operations"][0])
        original = copy.deepcopy((adapter.records, adapter.runtime, writer.idempotency))
        self.assertEqual(writer.apply(v["operations"][1]), first)
        with self.assertRaisesRegex(Refusal, "idempotency_conflict"):
            writer.apply(v["operations"][2])
        self.assertEqual((adapter.records, adapter.runtime, writer.idempotency), original)

    # Missing review does not reserve an idempotency key or sequence; the same
    # request succeeds when its real review fact is restored.
    def test_quarantine_has_no_partial_effects(self):
        v = fixture("S14")
        adapter = Adapter(v["initial_state"], "control")
        reviews = adapter.policy["reviews"]
        adapter.policy["reviews"] = []
        writer = Transactions(adapter)
        before = copy.deepcopy((adapter.records, adapter.runtime))
        with self.assertRaisesRegex(Refusal, "quarantined"):
            writer.apply(v["operations"][0])
        self.assertEqual((adapter.records, adapter.runtime), before)
        self.assertEqual(writer.idempotency, {})
        adapter.policy["reviews"] = reviews
        self.assertEqual(writer.apply(v["operations"][0])["outcome"], "admitted")

    # Only the first representative's same-head replacement commits. The stale
    # attempt creates no record, dirty state, sequence or idempotency receipt.
    def test_compare_and_set(self):
        v = fixture("P10")
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        writer.apply(v["operations"][0])
        before = copy.deepcopy((adapter.records, adapter.runtime, writer.idempotency))
        with self.assertRaisesRegex(Refusal, "version_conflict"):
            writer.apply(v["operations"][2])
        self.assertEqual((adapter.records, adapter.runtime, writer.idempotency), before)
        self.assertEqual(adapter.runtime["committed_cuts"], [100, 102])

    # The entire mutually recursive batch is refused for cycle, while removing
    # one rule and its certificate permits the adjacent acyclic batch.
    def test_cycle_batch_is_atomic(self):
        v = fixture("S08")
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        before = copy.deepcopy((adapter.records, adapter.runtime))
        with self.assertRaisesRegex(Refusal, "cycle"):
            writer.apply(v["operations"][0])
        self.assertEqual((adapter.records, adapter.runtime), before)
        op = copy.deepcopy(v["operations"][0])
        rules = [p for p in op["proposals"] if p["envelope"]["kind"] == "justification"]
        removed = {key(ref(rules[-1])), key(rules[-1]["body"]["check"])}
        op["proposals"] = [p for p in op["proposals"] if key(ref(p)) not in removed]
        self.assertEqual(writer.apply(op)["outcome"], "admitted")

    # Complete integration input facts override a public-only client label and
    # keep the private input's audience restriction in the admitted derivative.
    def test_lineage_taint(self):
        v = fixture("P11")
        adapter = Adapter(v["initial_state"], "control")
        writer = Transactions(adapter)
        result = writer.apply(v["operations"][0])
        derivative = adapter.records[key(result["refs"][0])]
        self.assertEqual(derivative["envelope"]["lineage"], [{"id": "rec:private", "version": 1}])
        self.assertNotIn("aud:public", derivative["envelope"]["disclosure"]["audiences"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
