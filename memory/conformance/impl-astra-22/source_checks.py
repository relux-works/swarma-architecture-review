"""Source-derived controls; no package imports, vectors or expected outputs."""

import copy
import unittest

from evaluator import Evaluator, Memory, Refusal, field_differences, strict_json, incompatibilities


def claim(key, **extra):
    return {"id": key, "kind": "assertion", "issuer": "owner", "subject": "subject",
            "schema": "fact/1", "perspective": "own", "slot": key, **extra}


def root(key, target, sign="support", **extra):
    return {"id": key, "target": [target, sign], "qualification": "semantic_review", **extra}


def rule(key, target, *premises, **extra):
    return {"id": key, "target": [target, "support"], "premises": [[p, "support"] for p in premises],
            "checked": True, **extra}


class SourceClaims(unittest.TestCase):
    # On these finite examples, neither absence nor conflicting premises invents
    # opposition; the positive rule retains its conflicted-premise qualification.
    def test_independent_channels_and_no_explosion(self):
        model = Evaluator([claim(k) for k in "ABC"],
                          [root("a+", "A"), root("a-", "A", "oppose")], [rule("ab", "B", "A")])
        b = model.evaluate("B")
        self.assertEqual(b["support"]["witness"], "present")
        self.assertEqual(b["support"]["premise_quality"], "conflicted_premises_only")
        self.assertEqual(b["oppose"]["witness"], "not_found")
        self.assertEqual(model.evaluate("C")["support"]["witness"], "not_found")

    # ASTRA25-06: an opposite-quality root cannot consume the existence walk's
    # one-root allowance. Both polarities also receive independent allowances.
    def test_quality_and_polarity_budgets_are_independent(self):
        for conclusion in ("support", "oppose"):
            for premise in ("support", "oppose"):
                with self.subTest(conclusion=conclusion, premise=premise):
                    edge = rule("ab", "B", "A")
                    edge.update(target=["B", conclusion], premises=[["A", premise]])
                    model = Evaluator([claim(k) for k in "AB"],
                                      [root("a-", "A", "oppose"), root("a+", "A")], [edge])
                    one = model.evaluate("B", {"root_budget": 1, "rule_budget": 1})
                    two = model.evaluate("B", {"root_budget": 2, "rule_budget": 1})
                    self.assertEqual(one, two)
                    self.assertEqual(one[conclusion]["witness"], "present")
                    self.assertEqual(one[conclusion]["premise_quality"], "conflicted_premises_only")
                    self.assertEqual(one["cutoffs"], [])
                    for zero, cutoff in (("root_budget", "root_limit"), ("rule_budget", "rule_limit")):
                        stopped = model.evaluate("B", {"root_budget": 1, "rule_budget": 1, zero: 0})
                        self.assertEqual(stopped[conclusion]["witness"], "not_found")
                        self.assertEqual(stopped[conclusion]["evaluation"], "incomplete")
                        self.assertEqual(stopped["cutoffs"], [cutoff])
        for sign in ("support", "oppose"):
            channel = model.evaluate("A", {"root_budget": 1})[sign]
            self.assertEqual(channel["witness"], "present")
            self.assertEqual(channel["evaluation"], "complete")

    # An exhausted opposite lookup makes quality uncertain without changing the
    # independently found witness or own completeness. A found opposite taints it.
    def test_quality_uncertainty_does_not_spend_existence(self):
        opposite = rule("cd-a", "A", "C", "D")
        opposite["target"][1] = "oppose"
        model = Evaluator([claim(k) for k in "ABCD"],
                          [root(k, k) for k in "ACD"],
                          [rule("ab", "B", "A"), opposite])
        limited = model.evaluate("B", {"root_budget": 1, "rule_budget": 1})
        self.assertEqual(limited["support"]["witness"], "present")
        self.assertEqual(limited["support"]["evaluation"], "complete")
        self.assertEqual(limited["support"]["premise_quality"], "not_fully_checked")
        self.assertEqual(limited["cutoffs"], [])
        sufficient = model.evaluate("B", {"root_budget": 2, "rule_budget": 1})
        self.assertEqual(sufficient["support"]["premise_quality"], "conflicted_premises_only")

    # A shared premise is charged once in one DFS walk. Exhaustion elsewhere is
    # still recorded after an earlier missing premise, and reference order wins
    # over insertion order (including numeric versions).
    def test_within_walk_memo_and_stable_order(self):
        model = Evaluator([claim(k) for k in "ABCD"], [root("a", "A")],
                          [rule("bd", "D", "B"), rule("cd", "D", "C"),
                           rule("ab", "B", "A"), rule("ac", "C", "A")])
        result = model.evaluate("D", {"root_budget": 1, "rule_budget": 4})
        self.assertEqual(result["support"]["witness"], "present")
        self.assertEqual(result["support"]["evaluation"], "complete")
        self.assertEqual(result["support"]["witness_assessments"], ["a"])
        model = Evaluator([claim(k) for k in "ABC"], [root("b", "B")], [rule("abc", "C", "A", "B")])
        result = model.evaluate("C", {"root_budget": 0})
        self.assertEqual(result["support"]["evaluation"], "incomplete")
        self.assertEqual(result["cutoffs"], ["root_limit"])
        model = Evaluator([claim("A")], [root("ten", "A", reference_order=["r", 10]),
                                         root("two", "A", reference_order=["r", 2])])
        result = model.evaluate("A", {"root_budget": 1})
        self.assertEqual(result["support"]["witness_assessments"], ["two"])
        self.assertEqual(result["support"]["evaluation"], "incomplete")

    # Separate quality accounting does not make existence unbounded. A second
    # necessary positive root exceeds one slot; with two slots the AND succeeds.
    def test_existence_budget_still_bounds_required_roots(self):
        model = Evaluator([claim(k) for k in "ABC"],
                          [root("a+", "A"), root("b+", "B")],
                          [rule("abc", "C", "A", "B")])
        limited = model.evaluate("C", {"root_budget": 1, "rule_budget": 1})
        self.assertEqual(limited["support"]["witness"], "not_found")
        self.assertEqual(limited["support"]["evaluation"], "incomplete")
        self.assertEqual(limited["cutoffs"], ["root_limit"])
        valid = model.evaluate("C", {"root_budget": 2, "rule_budget": 1})
        self.assertEqual(valid["support"]["witness"], "present")
        self.assertEqual(valid["support"]["evaluation"], "complete")

    # Withdrawal removes only the selected support path, never creates opposition.
    def test_alternatives_and_withdrawal(self):
        roots = [root(k, k, withdrawn_at=2 if k == "B" else None) for k in "ABDE"]
        rules = [rule("abc", "C", "A", "B"), rule("dec", "C", "D", "E")]
        model = Evaluator([claim(k) for k in "ABCDE"], roots, rules)
        self.assertEqual(model.evaluate("C", {"cut": 2})["support"]["witness"], "present")
        only = Evaluator([claim(k) for k in "ABCDE"], roots, rules[:1]).evaluate("C", {"cut": 2})
        self.assertEqual(only["support"]["witness"], "not_found")
        self.assertEqual(only["oppose"]["witness"], "not_found")

    # Opposing necessary-looking premises do not contrapose a one-way rule.
    def test_no_completion(self):
        model = Evaluator([claim(k) for k in "ABC"], [root("a-", "A", "oppose")],
                          [rule("abc", "C", "A", "B")])
        self.assertEqual(model.evaluate("C")["oppose"]["witness"], "not_found")

    # Evaluation truncation and explanation truncation have different promises.
    def test_distinct_budgets(self):
        model = Evaluator([claim("A")], [root("one", "A"), root("two", "A")])
        limited = model.evaluate("A", {"root_budget": 1})
        self.assertEqual(limited["support"]["witness"], "present")
        self.assertEqual(limited["support"]["evaluation"], "incomplete")
        rendered = model.evaluate("A", {"explanation_budget": 1})
        self.assertEqual(rendered["support"]["evaluation"], "complete")
        self.assertFalse(rendered["explanation"]["complete"])

    # Hidden roots are filtered before logical work; this checks semantics only,
    # not wall time, resource isolation or real handle randomness.
    def test_hidden_work_has_no_semantic_budget_effect(self):
        base = Evaluator([claim("A")], [root("visible", "A")])
        hidden = Evaluator([claim("A")], [root("hidden", "A", "oppose", visible=False),
                                         root("visible", "A")])
        self.assertEqual(base.evaluate("A", {"root_budget": 1}), hidden.evaluate("A", {"root_budget": 1}))

    # A known cycle and an unqualified rule are rejected before a model exists.
    def test_graph_and_qualification_rejections(self):
        with self.assertRaisesRegex(Refusal, "cycle"):
            Evaluator([claim("A"), claim("B")], [], [rule("ab", "B", "A"), rule("ba", "A", "B")])
        with self.assertRaisesRegex(Refusal, "unqualified_rule"):
            Evaluator([claim("A"), claim("B")], [], [rule("ab", "B", "A", checked=False)])
        Evaluator([claim("A"), claim("B")], [], [rule("ab", "B", "A")])

    # Learned-at cuts, half-open boundaries, mode and exact assessment pins each
    # exclude the mismatched root while an adjacent matching query admits it.
    def test_time_mode_and_pins(self):
        model = Evaluator([claim("A", mode="simulated")], [root("r", "A", recorded=20, valid=[1, 2],
                                             mode="simulated", pins={"artifact": "D"})])
        good = {"cut": 20, "valid_at": 1, "mode": "simulated", "pins": {"artifact": "D"}}
        self.assertEqual(model.evaluate("A", good)["support"]["witness"], "present")
        for change in ({"cut": 19}, {"valid_at": 2}, {"mode": "real"}, {"pins": {"artifact": "D2"}}):
            self.assertEqual(model.evaluate("A", good | change)["support"]["witness"], "not_found")

    # Documentary/review relations do not become support; complete registered
    # graph traversal does not invent full source-corpus coverage.
    def test_attribution_and_coverage(self):
        model = Evaluator([claim("A"), claim("B")], [root("a", "A")],
                          [rule("ab", "B", "A", edge_role="documentary_basis", checked=False)])
        self.assertEqual(model.evaluate("B")["support"]["witness"], "not_found")
        a = model.evaluate("A")["support"]
        self.assertEqual(a["evaluation"], "complete")
        self.assertEqual(a["corpus_coverage"], "unknown")

    # Erasure changes retained evidence's source state, not its polarity; an
    # unretained assessment is no longer a witness in this in-memory model.
    def test_retained_assessment_and_freshness(self):
        model = Evaluator([claim("A", usable_until=7)], [root("r", "A", source="S")],
                          sources=[{"id": "S", "availability": "erased"}])
        out = model.evaluate("A", {"now": 30})
        self.assertEqual(out["support"]["source_state"], "prior_assessment_only")
        self.assertEqual(out["support"]["freshness"], "stale")
        self.assertEqual(out["oppose"]["witness"], "not_found")
        model.roots[0]["retained"] = False
        self.assertEqual(model.evaluate("A")["support"]["witness"], "not_found")

    # R7-011: a failed current-source check is incomplete; retained/independent
    # assessments remain usable, while hidden source inputs produce no cutoff.
    def test_current_source_failure_is_not_completed_absence(self):
        for requirement in ("current", "retained", "independent"):
            r = root("r", "A", source="S", retained=requirement != "current", independent=requirement == "independent")
            for availability in ("resolvable", "unavailable", "erased"):
                model = Evaluator([claim("A")], [r], sources=[{"id": "S", "availability": availability}])
                out = model.evaluate("A")
                failed = requirement == "current" and availability != "resolvable"
                self.assertEqual(out["support"]["evaluation"], "incomplete" if failed else "complete")
                self.assertEqual(out["support"]["witness"], "not_found" if failed else "present")
                self.assertEqual(out["cutoffs"], ["source_unavailable"] if failed else [])
        hidden = Evaluator([claim("A")], [root("r", "A", source="S", retained=False)],
                           sources=[{"id": "S", "availability": "erased", "visible": False}])
        self.assertEqual(hidden.evaluate("A"), Evaluator([claim("A")]).evaluate("A"))

    # R7-012: an authorized non-root signature association keeps unavailable
    # source state on both empty channels, without fabricating signed support.
    def test_empty_channel_preserves_source_association(self):
        model = Evaluator([claim("A")], [root("sig", "A", qualification="signature", source="S")],
                          sources=[{"id": "S", "availability": "erased"}])
        for sign in ("support", "oppose"):
            result = model.evaluate("A")[sign]
            self.assertEqual(result["witness"], "not_found")
            self.assertEqual(result["evaluation"], "complete")
            self.assertEqual(result["source_state"], "prior_assessment_only")
        self.assertEqual(Evaluator([claim("A")]).evaluate("A")["support"]["source_state"], "resolvable_now")
        model.sources["S"]["visible"] = False
        self.assertEqual(model.evaluate("A"), Evaluator([claim("A")]).evaluate("A"))

    # R7-013: exact premise assessment provenance follows a found rule path;
    # an unrelated assessment sharing the same origin is not that path's input.
    def test_exact_assessment_provenance(self):
        model = Evaluator([claim(k) for k in "ABC"],
                          [root("a", "A", origin="same"), root("c", "C", origin="same")],
                          [rule("ab", "B", "A")])
        result = model.evaluate("B")["support"]
        self.assertEqual(result["root_origins"], ["same"])
        self.assertEqual(result["witness_assessments"], ["a"])

    # R7-015: an AND path retains its weakest necessary source-state limit;
    # complete stronger OR alternatives can win without deleting the weaker path.
    def test_and_source_states_before_or_preference(self):
        states = ["resolvable_now", "independent_attestation", "prior_assessment_only"]
        for left in states:
            for right in states:
                roots, sources = [], []
                for target, state in (("A", left), ("B", right)):
                    roots.append(root(target, target, source="S" + target, retained=True,
                                      independent=state == "independent_attestation"))
                    sources.append({"id": "S" + target, "availability": "resolvable" if state == "resolvable_now" else "erased"})
                model = Evaluator([claim(k) for k in "ABC"], roots, [rule("abc", "C", "A", "B")], sources)
                expected = states[max(states.index(left), states.index(right))]
                result = model.evaluate("C")["support"]
                self.assertEqual(result["source_state"], expected)
                self.assertEqual(result["witness"], "present")
                self.assertEqual(result["evaluation"], "complete")
                model.roots.append(root("strong", "C", independent=True))
                strong = model.evaluate("C")["support"]["source_state"]
                self.assertEqual(strong, "resolvable_now" if expected == "resolvable_now" else "independent_attestation")

    # Copies of an origin do not increase the distinct root-origin set.
    def test_root_origin_deduplication(self):
        model = Evaluator([claim("A")], [root(str(i), "A", origin="declaration") for i in range(3)])
        self.assertEqual(model.evaluate("A")["support"]["root_origins"], ["declaration"])

    # Representation failure and a stale version both leave all state unchanged;
    # the first authorized revision from that version succeeds.
    def test_revision_and_representation_atomicity(self):
        memory = Memory([claim("v1", slot="s")], ["fact/1"])
        next_record = claim("v2", slot="s", replaces="v1")
        before = copy.deepcopy(memory.__dict__)
        with self.assertRaisesRegex(Refusal, "representation_required"):
            memory.admit(next_record, submitter="agent", expected_version="v1")
        self.assertEqual(before, memory.__dict__)
        memory.admit(next_record, submitter="agent", representation_valid=True, expected_version="v1")
        before = copy.deepcopy(memory.__dict__)
        with self.assertRaisesRegex(Refusal, "version_conflict"):
            memory.admit(claim("v3", slot="s", replaces="v1"), expected_version="v1")
        self.assertEqual(before, memory.__dict__)
        self.assertEqual(memory.project({})["current"], ["v2"])

    # Repeating a canonical request returns one receipt; a changed request under
    # the same identity does not overwrite it or add another record.
    def test_idempotency(self):
        memory = Memory(schemas=["fact/1"])
        record = claim("A")
        first = memory.admit(record, idempotency_key="retry")
        self.assertEqual(first, memory.admit(record, idempotency_key="retry"))
        with self.assertRaisesRegex(Refusal, "idempotency_conflict"):
            memory.admit(claim("B"), idempotency_key="retry")
        self.assertEqual(list(memory.records), ["A"])

    # A foreign issuer's replacement and an unknown schema fail without writes.
    def test_authority_and_schema(self):
        memory = Memory([claim("A", slot="s")], ["fact/1"])
        for record, code in ((claim("B", issuer="observer", slot="s", replaces="A"), "revision_authority"),
                             (claim("B", schema="fact/2"), "unknown_schema")):
            before = copy.deepcopy(memory.__dict__)
            with self.assertRaisesRegex(Refusal, code):
                memory.admit(record, expected_version="A")
            self.assertEqual(before, memory.__dict__)

    # Authority order survives reversed arrival; two unordered receipted heads
    # remain ambiguous and do not create a write or evidence conflict.
    def test_decision_order(self):
        old = claim("D1", slot="decision", statement_kind="decision_record", authority_receipt="r1", recorded=30)
        new = claim("D2", slot="decision", statement_kind="decision_record", authority_receipt="r2",
                    authority_after=["D1"], recorded=20)
        memory = Memory([new, old])
        self.assertEqual(memory.project({})["current"], ["D2"])
        del memory.records["D2"]["authority_after"]
        self.assertEqual(memory.project({})["status"], "ambiguous_current")
        self.assertEqual(memory.project({})["current"], ["D1", "D2"])

    # Integration-supplied inputs, including uncited private inputs, determine
    # constraints. Unknown lineage is never publishable by default.
    def test_lineage_and_unknown(self):
        memory = Memory([claim("private", constraints=["owner"]), claim("public")])
        out = memory.derive(claim("summary"), ["private", "public"])
        self.assertEqual(out["constraints"], ["owner"])
        self.assertFalse(memory.deliverable(out, "public", "discovery"))
        unknown = memory.derive(claim("summary"), ["public"], complete=False)
        self.assertFalse(memory.deliverable(unknown, "public", "discovery"))
        self.assertTrue(memory.deliverable(memory.derive(claim("ok"), ["public"]), "public", "discovery"))

    # Each owner's decision discharges only its own constraint and only for the
    # exact transformation, schema, inputs, audience and purpose.
    def test_declassification_exact_scope(self):
        memory = Memory()
        record = claim("city", constraints=["owner1", "owner2"], lineage=["coords"], transformation="city")
        decision = {"owner": "owner1", "authorized": True, "current": True,
                    "inputs": ["coords"], "transformation": "city", "output_schema": "fact/1",
                    "audience": "public", "purpose": "discovery"}
        self.assertFalse(memory.deliverable(record, "public", "discovery", [decision]))
        both = [decision, decision | {"owner": "owner2"}]
        self.assertTrue(memory.deliverable(record, "public", "discovery", both))
        self.assertFalse(memory.deliverable(record, "public", "contact", both))

    # A snapshot stays byte-equivalent after a revocation, while a new delivery
    # is refused. This does not recall already-delivered bytes.
    def test_snapshot_and_send_time_recheck(self):
        memory = Memory([claim("A")])
        snapshot = memory.snapshot({})
        original = copy.deepcopy(snapshot)
        self.assertTrue(memory.deliverable(memory.records["A"], "public", "card"))
        memory.revoke("A", "public")
        self.assertFalse(memory.deliverable(memory.records["A"], "public", "card"))
        self.assertEqual(snapshot, original)

    # Erasure follows content lineage without justification edges; stale
    # extraction cannot commit and unreconciled restore cannot deliver.
    def test_erasure_closure_and_fences(self):
        memory = Memory([claim("A"), claim("summary", lineage=["A"]), claim("cache", lineage=["summary"])],
                        ["fact/1"])
        self.assertEqual(memory.erase(["A"]), ["A", "cache", "summary"])
        with self.assertRaisesRegex(Refusal, "erasure_fence"):
            memory.admit(claim("late", lineage=["A"]))
        with self.assertRaisesRegex(Refusal, "stale_derivative"):
            memory.admit(claim("late", extraction_epoch=0))
        self.assertNotIn("late", memory.records)
        memory.restore_ready = False
        self.assertFalse(memory.deliverable(claim("else"), "public", "card"))

    # Exclusion affects only the projection and does not rewrite the issuer's
    # record or sequence.
    def test_projection_exclusion(self):
        memory = Memory([claim("org", issuer="organisation")])
        original = copy.deepcopy(memory.records)
        query = {"family": "audience_projection", "excluded": ["org"]}
        self.assertEqual(memory.project(query)["current"], [])
        self.assertEqual(memory.records, original)
        self.assertEqual(memory.project({})["current"], ["org"])

    # Declared incompatibility needs exact schema/scope and overlapping validity;
    # adjacent intervals, distinct slots and missing rules do not create links.
    def test_declared_incompatibility_scope(self):
        a = claim("A", slot="s", space="space", statement_kind="fact", valid=[1, 3], content={"value": "one"})
        b = claim("B", slot="s", space="space", statement_kind="fact", valid=[2, 4], content={"value": "two"})
        relations = [{"relation": "unequal", "field": "value", "statement_kinds": ["fact"]}]
        self.assertEqual(incompatibilities([a, b], relations), {"A": ["B"], "B": ["A"]})
        for change in ({"valid": [3, 4]}, {"valid": "unknown"}, {"slot": "else"},
                       {"perspective": "observer"}, {"space": "else"}, {"content": {"value": "one"}}):
            self.assertEqual(incompatibilities([a, b | change], relations), {"A": [], "B": []})
        self.assertEqual(incompatibilities([a, b], []), {"A": [], "B": []})
        self.assertEqual(Evaluator([a, b]).evaluate("A")["oppose"]["witness"], "not_found")

    # The harness catches a planted field change and unexpected output field;
    # duplicate JSON keys and nonfinite numbers cannot silently normalize.
    def test_instrument_controls(self):
        self.assertEqual(field_differences({"a": 1}, {"a": 1}), [])
        self.assertEqual(field_differences({"a": 1}, {"a": 2})[0]["path"], "$.a")
        self.assertEqual(field_differences({}, {"extra": 1})[0]["expected"], "<absent>")
        with self.assertRaisesRegex(Refusal, "duplicate_key"):
            strict_json('{"a":1,"a":2}')
        with self.assertRaisesRegex(Refusal, "invalid_number"):
            strict_json('{"a":NaN}')


if __name__ == "__main__":
    unittest.main(verbosity=2)
