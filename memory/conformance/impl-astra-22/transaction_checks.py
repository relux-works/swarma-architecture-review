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
