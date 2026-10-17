"""Current retention deadlines gate new writes and exact receipt replay."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter
from evaluator import Refusal
from transactions import Transactions, key, ref


BASE = Path(__file__).resolve().parent
LIVE = "2026-10-17T00:00:00Z"
STILL_LIVE = "2026-10-17T00:00:01Z"
DEADLINE = "2026-10-17T00:00:02Z"
AFTER = "2026-10-17T00:00:03Z"


def fixture(name):
    return json.loads((BASE.parents[1] / "spec/kernel/vectors/semantic" / (name + ".json")).read_text())


class DeadlineControls(unittest.TestCase):
    def denied(self, adapter, op, code="not_authorized"):
        before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy))
        with self.assertRaisesRegex(Refusal, "^" + code + "$"):
            Transactions(adapter).apply(op)
        self.assertEqual((adapter.records, adapter.runtime, adapter.policy), before)

    # The five immutable author probes require before-expiry admission and
    # atomic own/input boundary refusals, including expired exact replay.
    def test_original_native_probes(self):
        data = json.loads((BASE / "fixtures/retention-deadline-native-first.json").read_text())
        for case in data["cases"]:
            with self.subTest(case=case["name"]):
                adapter = Adapter(case["initial_state"], "control")
                for i, op in enumerate(case["operations"]):
                    if case["name"] == "before_deadline" or case["name"] == "expired_replay" and i == 0:
                        self.assertEqual(Transactions(adapter).apply(op)["outcome"], "admitted")
                    else:
                        self.denied(adapter, op)

    # Every proposed output of admit/raw/revise/declassify is independently
    # bounded; still-live replay preserves the receipt and expiry cannot refresh
    # it, change recorded time, create an entry under a fresh key, or run a purge.
    def test_all_intake_apis_and_replay(self):
        for mode, name, index in (("admit", "P11", 8), ("admit_raw", "P11", 8),
                                   ("revise", "P10", 0), ("declassify", "P05", 1)):
            initial = fixture(name)
            template = initial["operations"][index]
            templates = (template["proposals"] if mode in {"admit", "admit_raw"} else
                         template["assessments"] + [template["output"]] if mode == "declassify" else
                         [template["replacement"], template["revision"]])
            for selected in range(len(templates)):
                with self.subTest(mode=mode, output=selected):
                    op = copy.deepcopy(template)
                    outputs = (op["proposals"] if mode in {"admit", "admit_raw"} else
                               op["assessments"] + [op["output"]] if mode == "declassify" else
                               [op["replacement"], op["revision"]])
                    outputs[selected]["envelope"]["disclosure"]["retain_until"] = DEADLINE
                    op["context"]["at"] = LIVE
                    if mode == "admit_raw":
                        op["op"] = mode
                        op["raw_json"] = json.dumps({"proposals": op.pop("proposals")})
                    adapter = Adapter(initial["initial_state"], "control")
                    writer = Transactions(adapter)
                    first = writer.apply(op)
                    retry = copy.deepcopy(op)
                    retry["context"]["at"] = STILL_LIVE
                    before = copy.deepcopy((adapter.records, adapter.runtime, adapter.policy))
                    self.assertEqual(writer.apply(retry), first)
                    self.assertEqual((adapter.records, adapter.runtime, adapter.policy), before)
                    retry["context"]["at"] = DEADLINE
                    self.denied(adapter, retry)
                    self.assertEqual(adapter.runtime["idempotency"][0]["receipt"], first)
                    retry["idempotency_key"] += ":fresh-expired"
                    self.denied(adapter, retry)

    # A transitive ancestor bounds storage even when the direct input is unknown
    # but has a tracked lower bound. Before is allowed; equality and after deny.
    def test_complete_and_unknown_ancestors(self):
        for unknown in (False, True):
            if unknown:
                v = json.loads((BASE.parent / "cases/astra-25-retention-authority-transitive-unknown-control.vector.json").read_text())
                op = next(o for o in v["operations"] if o["op"] == "admit")
                intermediate = next(r for r in v["initial_state"]["records"] if r["envelope"]["lineage"] == "unknown")
                ancestor = next(f for f in v["initial_state"]["policy"]["lineage_facts"] if f["output"] == ref(intermediate))["inputs"][0]
            else:
                v = fixture("P11")
                op = v["operations"][8]
                ancestor = {"id": "rec:retained-root", "version": 1}
            next(r for r in v["initial_state"]["records"] if ref(r) == ancestor)["envelope"]["disclosure"]["retain_until"] = DEADLINE
            for at in (STILL_LIVE, DEADLINE, AFTER):
                with self.subTest(unknown=unknown, at=at):
                    adapter = Adapter(v["initial_state"], "control")
                    current = copy.deepcopy(op)
                    current["context"]["at"] = at
                    if at == STILL_LIVE:
                        self.assertEqual(Transactions(adapter).apply(current)["outcome"], "admitted")
                    else:
                        self.denied(adapter, current)

    # A later-array input's deadline constrains the entire atomic batch, in
    # either ordering, without leaving any earlier output or receipt behind.
    def test_same_batch_deadline(self):
        for reverse in (False, True):
            v = fixture("P13")
            op = copy.deepcopy(v["operations"][2])
            next(p for p in op["proposals"] if p["envelope"]["id"] == "rec:model-stage")["envelope"]["disclosure"]["retain_until"] = DEADLINE
            if reverse:
                op["proposals"].reverse()
            op["context"]["at"] = LIVE
            self.assertEqual(Transactions(Adapter(v["initial_state"], "control")).apply(op)["outcome"], "admitted")
            op["context"]["at"] = DEADLINE
            self.denied(Adapter(v["initial_state"], "control"), op)

    # Null imposes no artificial bound; an expired unrelated record cannot
    # veto a write whose own known closure remains authorized and live.
    def test_null_and_unrelated_deadline(self):
        v = fixture("P11")
        op = copy.deepcopy(v["operations"][8])
        op["context"]["at"] = "2030-01-01T00:00:00Z"
        unrelated = copy.deepcopy(v["initial_state"]["records"][0])
        unrelated["envelope"].update(id="rec:unrelated", subject="subj:unrelated", issuer="subj:unrelated",
                                       perspective={"kind": "own", "principal": "subj:unrelated"}, lineage=[])
        unrelated["envelope"]["recorded"]["sequence"] = 99
        unrelated["envelope"]["disclosure"]["retain_until"] = DEADLINE
        v["initial_state"]["records"].append(unrelated)
        v["initial_state"]["policy"]["lineage_facts"].append({"output": ref(unrelated), "profile": {"id": "integration:synthetic", "version": 1},
                                                             "kind": "direct", "inputs": [], "complete": True})
        adapter = Adapter(v["initial_state"], "control")
        self.assertEqual(Transactions(adapter).apply(op)["outcome"], "admitted")
        self.assertEqual(adapter.records[key(ref(unrelated))], unrelated)

    # Current authority checks every proposal before duplicate-reference
    # validation; repeated identities cannot hide an expired proposed envelope.
    def test_duplicate_proposal_authorization_order(self):
        v = fixture("P11")
        op = copy.deepcopy(v["operations"][8])
        op["context"]["at"] = DEADLINE
        op["proposals"].append(copy.deepcopy(op["proposals"][0]))
        self.denied(Adapter(v["initial_state"], "control"), op, "duplicate_record")
        op["proposals"][1]["envelope"]["disclosure"]["retain_until"] = DEADLINE
        self.denied(Adapter(v["initial_state"], "control"), op)


if __name__ == "__main__":
    unittest.main(verbosity=2)
