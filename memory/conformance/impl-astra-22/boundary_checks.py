"""Frozen-view and current selected-delivery controls; no external bytes sent."""

import copy
import hashlib
import json
from pathlib import Path
import unittest

from adapter import Adapter, key
from boundary import Boundary
from evaluator import Refusal
from run_vectors import compare


BASE = Path(__file__).resolve().parent
PROFILE = json.loads((BASE.parents[1] / "spec/kernel/schemas/view.schema.json").read_text())["properties"]["semantic_profile"]["const"]


def fixture():
    return json.loads((BASE.parents[1] / "spec/kernel/vectors/semantic/P12.json").read_text())


def prepared(vector=None):
    vector = fixture() if vector is None else vector
    adapter = Adapter(vector["initial_state"], "control")
    adapter.execute(vector["operations"][:1], vector["operations"][0]["query"])
    return adapter, copy.deepcopy(vector["operations"][1])


def state(adapter):
    return copy.deepcopy((adapter.records, adapter.runtime, adapter.policy, adapter.captures))


class BoundaryControls(unittest.TestCase):
    # The same exact binding delivers before revocation and refuses afterwards;
    # neither revocation nor a later query rewrites captured bytes or policy pins.
    def test_frozen_capture_and_current_revocation(self):
        vector = fixture()
        adapter, op = prepared(vector)
        saved = copy.deepcopy(adapter.captures)
        policy = copy.deepcopy(adapter.policy)
        self.assertEqual(Boundary(adapter).apply(op)["outcome"], "delivered")
        self.assertEqual(Boundary(adapter).apply(vector["operations"][2])["outcome"], "revoked")
        before = state(adapter)
        with self.assertRaisesRegex(Refusal, "disclosure_revoked"):
            Boundary(adapter).apply(op)
        self.assertEqual(state(adapter), before)
        self.assertEqual(adapter.captures, saved)
        self.assertEqual(adapter.policy, policy)
        self.assertEqual(adapter.query(vector["query"])["items"], [])

    # Each selected read/use/forward right is independently necessary; restoring
    # that right restores delivery. Refusal changes no protected or public state.
    def test_each_selected_right(self):
        for right in ("read", "use", "forward"):
            with self.subTest(right=right):
                adapter, op = prepared()
                grants = copy.deepcopy(adapter.policy["grants"])
                for grant in adapter.policy["grants"]:
                    if grant["audience"] == op["audience"] and grant["purpose"] == op["purpose"]:
                        grant["rights"] = [r for r in grant["rights"] if r != right]
                before = state(adapter)
                with self.assertRaisesRegex(Refusal, "disclosure_revoked"):
                    Boundary(adapter).apply(op)
                self.assertEqual(state(adapter), before)
                adapter.policy["grants"] = grants
                self.assertEqual(Boundary(adapter).apply(op)["outcome"], "delivered")

    # Unselected same-schema records cannot veto delivery; the paired fixture
    # also requires selected revocation refusal. Only expected profile metadata
    # is migrated from the frozen 0.2.5 fixtures to the tested 0.2.6 release.
    def test_excluded_record_has_no_forwarding_effect(self):
        for suffix in ("", "-control"):
            with self.subTest(suffix=suffix):
                path = BASE.parent / ("cases/astra-26-excluded-forward-right" + suffix + ".vector.json")
                original_bytes = path.read_bytes()
                original = json.loads(original_bytes)
                vector = copy.deepcopy(original)
                self.assertEqual(PROFILE, "0.2.6-draft")
                for view in (vector["expected"]["operation_results"][0], vector["expected"]["result"]):
                    self.assertEqual(view["semantic_profile"], "0.2.5-draft")
                    view["semantic_profile"] = PROFILE
                restored = copy.deepcopy(vector)
                for view in (restored["expected"]["operation_results"][0], restored["expected"]["result"]):
                    view["semantic_profile"] = "0.2.5-draft"
                self.assertEqual(restored, original)  # Recursive equality excludes every other change.
                scratch = BASE.parents[2] / ".temp/astra-22/r7-059"
                scratch.mkdir(parents=True, exist_ok=True)
                migrated_bytes = (json.dumps(vector, indent=2) + "\n").encode()
                (scratch / path.name).write_bytes(migrated_bytes)
                audit = {
                    "original": str(path.relative_to(BASE.parents[2])),
                    "original_sha256": hashlib.sha256(original_bytes).hexdigest(),
                    "copy_sha256": hashlib.sha256(migrated_bytes).hexdigest(),
                    "old_profile": "0.2.5-draft", "new_profile": PROFILE,
                    "changed_paths": ["expected.operation_results[0].semantic_profile", "expected.result.semantic_profile"],
                    "recursive_other_fields_unchanged": restored == original,
                }
                (scratch / (path.stem + ".audit.json")).write_text(json.dumps(audit, indent=2) + "\n")
                vector = json.loads((scratch / path.name).read_bytes())
                actual = Adapter(vector["initial_state"], PROFILE).execute(vector["operations"], vector["query"])
                self.assertEqual(compare(actual, vector["expected"], vector["normalization"], vector["forbidden"])[1], [])
                self.assertEqual(path.read_bytes(), original_bytes)

    # Exact expiry is stale; fresh delivery does not refresh the saved horizon
    # or mutate the earlier view's freshness claim at its original cut.
    def test_delivery_expiry_and_capture_immutability(self):
        vector = fixture()
        vector["operations"][0]["query"]["usable_until"] = "2026-10-17T00:00:01Z"
        adapter, op = prepared(vector)
        saved = copy.deepcopy(adapter.captures)
        self.assertEqual(Boundary(adapter).apply(op)["outcome"], "delivered")
        for second in (1, 2):
            op["at"] = f"2026-10-17T00:00:0{second}Z"
            before = state(adapter)
            with self.assertRaisesRegex(Refusal, "publication_stale"):
                Boundary(adapter).apply(op)
            self.assertEqual(state(adapter), before)
            self.assertEqual(adapter.captures, saved)

    # Fenced/erased selected payloads and a closed restore gate refuse without
    # substituting a fresh context. Removing only the test condition restores use.
    def test_erasure_and_restore_gates(self):
        for condition in ("fences", "erased", "restore"):
            with self.subTest(condition=condition):
                adapter, op = prepared()
                original = copy.deepcopy(adapter.runtime)
                if condition == "restore":
                    adapter.runtime["restore"]["status"] = "fenced"
                else:
                    adapter.runtime[condition] = copy.deepcopy(adapter.captures[0]["selected"])
                before = state(adapter)
                with self.assertRaisesRegex(Refusal, "disclosure_revoked"):
                    Boundary(adapter).apply(op)
                self.assertEqual(state(adapter), before)
                adapter.runtime = original
                self.assertEqual(Boundary(adapter).apply(op)["outcome"], "delivered")

    # A saved view is bound to its actor, audience and purpose. Neither a guessed
    # operation index nor a different caller can reuse it; revoke needs the owner.
    def test_binding_and_owner_authority(self):
        for field, value in (("actor", "subj:other"), ("audience", "aud:private"),
                             ("purpose", "purpose:read"), ("view_operation", 99)):
            adapter, op = prepared()
            op[field] = value
            before = state(adapter)
            with self.assertRaisesRegex(Refusal, "not_authorized"):
                Boundary(adapter).apply(op)
            self.assertEqual(state(adapter), before)
        adapter, op = prepared()
        revoke = fixture()["operations"][2]
        revoke["actor"] = "subj:other"
        before = state(adapter)
        with self.assertRaisesRegex(Refusal, "not_authorized"):
            Boundary(adapter).apply(revoke)
        self.assertEqual(state(adapter), before)
        self.assertEqual(Boundary(adapter).apply(op)["outcome"], "delivered")

    # Other-principal or other-purpose revocations do not silently widen scope.
    def test_unrelated_revocation_scope(self):
        for field, value in (("principal", "subj:other"), ("purpose", "purpose:read")):
            adapter, op = prepared()
            revoke = fixture()["operations"][2]
            revoke[field] = value
            Boundary(adapter).apply(revoke)
            self.assertEqual(Boundary(adapter).apply(op)["outcome"], "delivered")

    # Capture and returned view values have no mutable aliases to model storage.
    # The direct replacement here checks object isolation, not admission validity.
    def test_capture_has_no_storage_alias(self):
        adapter, _ = prepared()
        saved = copy.deepcopy(adapter.captures)
        record = adapter.records[key(adapter.captures[0]["selected"][0])]
        record["body"]["content"][0]["value"] = "later independent test value"
        self.assertEqual(adapter.captures, saved)


if __name__ == "__main__":
    unittest.main(verbosity=2)
