"""Authorized synthetic availability and control observations, not deployment."""

import copy
import unittest

from adapter import Adapter
from erasure import Erasure
from erasure_checks import fixture, snapshot, NOW
from evaluator import Refusal


def normalized(view):
    view = copy.deepcopy(view)
    view["authorized_snapshot_handle"] = "<fresh>"
    for item in view["items"]:
        for sign in ("support", "oppose"):
            item[sign]["authorized_snapshot_handle"] = "<fresh>"
    return view


class AvailabilityControls(unittest.TestCase):
    def denied(self, adapter, op, code):
        before = snapshot(adapter)
        with self.assertRaisesRegex(Refusal, "^" + code + "$"):
            Erasure(adapter).apply(op)
        self.assertEqual(snapshot(adapter), before)

    # Hidden-work stimuli change only their protected counter and preserve the
    # whole public view modulo explicitly named fresh snapshot handles.
    def test_hidden_load_has_no_logical_effect(self):
        v = fixture("S27")
        a = Adapter(v["initial_state"], "control")
        initial_view = a.query(v["query"])
        for amount in (0, 1, 9000, 1000000):
            before = snapshot(a)
            self.assertEqual(Erasure(a).apply({"op": "load", "actor": "subj:h1", "hidden_work": amount})["outcome"], "proceeded")
            before[1]["hidden_work"] = amount
            self.assertEqual(snapshot(a), before)
            after_view = a.query(v["query"])
            self.assertNotEqual(after_view["authorized_snapshot_handle"], initial_view["authorized_snapshot_handle"])
            self.assertEqual(normalized(after_view), normalized(initial_view))

    # A predeclared owner availability transition produces the one coarse
    # refusal and can recover without changing policy pins, records or counts.
    def test_coarse_availability_and_recovery(self):
        v = fixture("S27")
        a = Adapter(v["initial_state"], "control")
        before = snapshot(a)
        view = a.query(v["query"])
        op = copy.deepcopy(v["operations"][3])
        Erasure(a).apply(op)
        self.assertEqual(a.query(v["query"]), {"type": "refusal", "code": "unavailable", "retryable": True})
        op["state"] = "available"
        Erasure(a).apply(op)
        self.assertEqual(snapshot(a), before)
        self.assertEqual(normalized(a.query(v["query"])), normalized(view))

    # Non-owner, undeclared degradation and malformed state cannot create a
    # public availability signal or any protected state change.
    def test_unauthorized_availability_is_atomic(self):
        v = fixture("S27")
        for change, code in (("owner", "not_authorized"), ("declaration", "not_authorized"),
                             ("shape", "invalid_shape")):
            with self.subTest(change=change):
                a = Adapter(v["initial_state"], "control")
                op = copy.deepcopy(v["operations"][3])
                if change == "owner":
                    op["actor"] = "other:actor"
                elif change == "declaration":
                    a.policy["availability_disclosure"] = "none"
                else:
                    op["state"] = "hidden-resource-error"
                self.denied(a, op, code)

    # Owner recovery must also work when degradation is already admitted in the
    # initial public availability state, not only after this process set it.
    def test_initial_degraded_state_can_recover(self):
        v = fixture("S27")
        v["initial_state"]["policy"]["public_availability"] = "degraded"
        a = Adapter(v["initial_state"], "control")
        self.assertEqual(a.query(v["query"])["code"], "unavailable")
        op = copy.deepcopy(v["operations"][3])
        op["state"] = "available"
        self.assertEqual(Erasure(a).apply(op)["outcome"], "availability_changed")
        self.assertEqual(a.query(v["query"])["type"], "view")

    # The harness can observe authorized control while memory is unavailable;
    # it records no external effect and does not enact stop/park/revocation.
    def test_control_observation_is_independent_data(self):
        v = fixture("S27")
        a = Adapter(v["initial_state"], "control")
        Erasure(a).apply(v["operations"][3])
        before = snapshot(a)
        for action in ("stop", "park", "revocation"):
            result = Erasure(a).apply({"op": "control", "actor": "subj:h1", "at": NOW, "action": action})
            self.assertEqual(result["outcome"], "proceeded")
        before[1]["control_observations"] = ["stop", "park", "revocation"]
        self.assertEqual(snapshot(a), before)
        self.assertEqual(a.runtime["external_effects"], [])
        self.denied(a, {"op": "control", "actor": "other:actor", "at": NOW, "action": "stop"}, "not_authorized")


if __name__ == "__main__":
    unittest.main(verbosity=2)
