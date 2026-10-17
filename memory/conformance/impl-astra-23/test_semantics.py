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

    # K-EVAL-5: resolved or empty sources precede independent/retained fallbacks without
    # upgrading evidence. These S32 neighbors also preserve policy denial and current-source limits.
    def test_source_state_availability_precedence(self):
        cases = []
        for requirement, fallback in (("independent", "independent_attestation"),
                                      ("retained", "prior_assessment_only")):
            for availability in ("available", "denied", "lost", "empty"):
                state = "resolvable_now" if availability in ("available", "empty") else fallback
                cases.append((requirement, availability, 0, state, []))
        cases.extend([
            ("current", "available", 1, "resolvable_now", []),
            ("current", "available", 0, "resolvable_now", ["source_limit"]),
            ("current", "empty", 0, "resolvable_now", []),
            ("current", "lost", 1, "prior_assessment_only", ["source_unavailable"]),
        ])
        for requirement, availability, bound, expected_state, cutoffs in cases:
            with self.subTest(requirement=requirement, availability=availability, bound=bound):
                v = vector("S32")
                records = {r["envelope"]["id"]: r for r in v["initial_state"]["records"]}
                assessment = records["rec:att"]["body"]
                assessment["source_requirement"] = requirement
                if availability == "empty":
                    assessment["sources"] = []
                records["rec:s"]["body"]["availability"] = (
                    "resolvable" if availability in ("available", "denied") else "erased")
                v["initial_state"]["policy"]["source_access"][0]["resolvable"] = availability in ("available", "lost")
                v["query"]["scope"]["targets"] = [{"id": "rec:attested", "version": 1}]
                v["query"]["bounds"]["source_resolutions"] = bound
                e = engine(v)
                self.assertTrue(e.grammar.matches(e.state, e.grammar.schemas["fixture"]["properties"]["initial_state"]))
                before = copy.deepcopy(e.state)
                result = e.read(v["query"])
                support = result["items"][0]["support"]
                self.assertEqual(support["source_state"], expected_state)
                self.assertEqual(support["witness"], "not_found" if cutoffs else "present")
                self.assertEqual(support["evaluation"], "incomplete" if cutoffs else "complete")
                self.assertEqual(support["evidence_qualification"], [] if cutoffs else ["semantic_review"])
                self.assertEqual(result["items"][0]["oppose"]["witness"], "not_found")
                self.assertEqual(result["cutoffs"], cutoffs)
                self.assertEqual(e.state, before)

    # R7-033: an admitted checked import expires at the exclusive horizon without changing
    # evidence or old captures; absent checks/replacement facts and ordinary documents stay distinct.
    def test_import_currentness_horizon(self):
        v = strict_loads((SPEC.parent / "conformance/cases/astra-26-checked-import-expiry.vector.json").read_text())
        e = engine(v)
        saved = e.operation(v["operations"][0], 0)
        frozen, before = copy.deepcopy(saved), copy.deepcopy(e.state)
        for now, expected, freshness in (("2026-10-17T00:00:00Z", "current", "fresh"),
                                         ("2026-10-17T00:00:01Z", "last_received", "stale"),
                                         ("2026-10-17T00:00:02Z", "last_received", "stale")):
            with self.subTest(now=now):
                q = copy.deepcopy(v["query"])
                q["now"] = now
                result = e.read(q)
                self.assertEqual(result["currentness"], expected)
                item = result["items"][0]
                self.assertEqual(item["currentness"], expected)
                self.assertEqual(item["support"]["freshness"], freshness)
                self.assertEqual(result["historical"], [])
                self.assertEqual(item["source_refs"], frozen["items"][0]["source_refs"])
                for sign in ("support", "oppose"):
                    for field in ("witness", "evaluation", "premise_quality", "evidence_qualification",
                                  "witness_roots", "independent_root_count"):
                        self.assertEqual(item[sign][field], frozen["items"][0][sign][field])
                self.assertEqual(e.captures[0][1], frozen)
                self.assertEqual(e.state, before)
        missing = copy.deepcopy(v)
        missing["initial_state"]["policy"]["imports"] = []
        self.assertEqual(engine(missing).read(v["operations"][0]["query"])["currentness"], "last_received")
        replaced = copy.deepcopy(v)
        replaced["initial_state"]["policy"]["imports"][0].update(
            status="replaced", successor={"id": "rec:copy2", "version": 1})
        historical = engine(replaced).read(replaced["query"])
        self.assertEqual(historical["items"], [])
        self.assertEqual(historical["historical"], [{"id": "rec:interest", "version": 1}])
        document = copy.deepcopy(v)
        for record in document["initial_state"]["records"]:
            if record["envelope"]["kind"] == "source":
                record["body"]["source_kind"] = "document"
        ordinary = engine(document).read(document["query"])
        self.assertEqual(ordinary["currentness"], "current")
        self.assertEqual(ordinary["items"][0]["support"]["freshness"], "stale")

    # R7-034: an unrelated excluded record cannot veto selected delivery; selected read/use/
    # forward revocation, an erasure fence and expiry still refuse without changing stored state.
    def test_delivery_uses_selected_binding(self):
        base = SPEC.parent / "conformance/cases"
        v = strict_loads((base / "astra-26-excluded-forward-right.vector.json").read_text())
        for name in ("astra-26-excluded-forward-right", "astra-26-excluded-forward-right-control"):
            case = strict_loads((base / (name + ".vector.json")).read_text())
            self.assertEqual(compare(engine(case).execute(case["operations"], case["query"]), case,
                                     Grammar(SPEC / "kernel/schemas")), ([], []))
        for right in ("read", "use", "forward"):
            with self.subTest(missing_selected_right=right):
                e = engine(v)
                e.operation(v["operations"][0], 0)
                for grant in e.state["policy"]["grants"]:
                    if (grant["audience"] == "aud:public" and grant["purpose"] == "purpose:publish"
                            and "rec:interest" in grant["records"]):
                        grant["rights"] = [r for r in grant["rights"] if r != right]
                before = copy.deepcopy(e.state)
                self.assertEqual(e.operation(v["operations"][1], 1)["code"], "disclosure_revoked")
                self.assertEqual(e.state, before)
        e = engine(v)
        e.operation(v["operations"][0], 0)
        for field in ("fences", "erased"):
            e.state["runtime"][field].append({"id": "rec:interest", "version": 1})
        before = copy.deepcopy(e.state)
        self.assertEqual(e.operation(v["operations"][1], 1)["code"], "disclosure_revoked")
        self.assertEqual(e.state, before)
        e = engine(v)
        capture, delivery = copy.deepcopy(v["operations"][:2])
        capture["query"]["usable_until"] = "2026-10-17T00:00:01Z"
        delivery["at"] = "2026-10-17T00:00:01Z"
        e.operation(capture, 0)
        before = copy.deepcopy(e.state)
        self.assertEqual(e.operation(delivery, 1)["code"], "publication_stale")
        self.assertEqual(e.state, before)

    # K-ERASE-2: scoped metadata filters only receipt refs; erase-only authority, missing
    # use/metadata, foreign grants and disclosure expiry cannot expose refs or shrink purge.
    def test_erasure_receipt_scope(self):
        v = vector("P08")
        complete = [{"id": "rec:sensitive", "version": 1}, {"id": "rec:summary", "version": 1}]
        e = engine(v)
        self.assertEqual(compare(e.execute(v["operations"], v["query"]), v,
                                 Grammar(SPEC / "kernel/schemas")), ([], []))
        for variant in ("erase_only", "no_use", "no_metadata", "other_principal",
                        "other_space", "other_record", "other_audience", "other_purpose",
                        "disclosure_audience", "expired"):
            with self.subTest(variant=variant):
                e = engine(v)
                op = copy.deepcopy(v["operations"][0])
                for grant in e.state["policy"]["grants"]:
                    # Preserve operation-level erase authority separately from metadata grants.
                    if "erase" in grant["rights"]:
                        e.state["policy"]["grants"] = [copy.deepcopy(grant)]
                        e.state["policy"]["grants"][0]["rights"] = ["erase"]
                        break
                authorized = {"principal": op["actor"], "space": "space:personal",
                              "audience": op["receipt_context"]["audience"],
                              "purpose": op["receipt_context"]["purpose"],
                              "rights": ["read", "use"], "metadata": True,
                              "records": ["rec:sensitive", "rec:summary"]}
                authorized["space"] = v["initial_state"]["records"][0]["envelope"]["space"]
                if variant == "no_use": authorized["rights"] = ["read"]
                if variant == "no_metadata": authorized["metadata"] = False
                for suffix, field, value in (("principal", "principal", "subj:other"),
                                              ("space", "space", "space:other"),
                                              ("record", "records", ["rec:other"]),
                                              ("audience", "audience", "aud:other"),
                                              ("purpose", "purpose", "purpose:other")):
                    if variant == "other_" + suffix: authorized[field] = value
                if variant != "erase_only": e.state["policy"]["grants"].append(authorized)
                if variant in ("disclosure_audience", "expired"):
                    for record in e.state["records"]:
                        if variant == "disclosure_audience":
                            record["envelope"]["disclosure"]["audiences"] = ["aud:other"]
                        else:
                            record["envelope"]["disclosure"]["retain_until"] = op["at"]
                result = e.operation(op, 0)
                self.assertEqual(result["refs"], [])
                self.assertEqual(result["outcome"], "purged")
                self.assertEqual(e.state["runtime"]["erased"], complete)
                self.assertEqual(e.state["runtime"]["fences"], complete)
                self.assertEqual(e.state["runtime"]["erasure_generation"], 1)
                self.assertTrue(all(not c["present"] for c in e.state["runtime"]["custody"]
                                    if c["controlled"]))

    # K-API-1: later intake stamps replay the immutable receipt; newly broader rights do not
    # expand it. Changed intent conflicts and expired/revoked current rights refuse atomically.
    def test_erasure_receipt_replay(self):
        v = vector("P08")
        e = engine(v)
        op = copy.deepcopy(v["operations"][0])
        first = e.operation(op, 0)
        retry = copy.deepcopy(op)
        retry["at"] = "2026-10-17T00:00:01Z"
        before = copy.deepcopy(e.state)
        self.assertEqual(e.operation(retry, 1), first)
        self.assertEqual(e.state, before)
        broader = copy.deepcopy(next(g for g in e.state["policy"]["grants"]
                                      if g["purpose"] == "purpose:publish" and "read" in g["rights"]))
        broader["purpose"] = "purpose:read"
        e.state["policy"]["grants"].append(broader)
        before = copy.deepcopy(e.state)
        self.assertEqual(e.operation(retry, 2), first)
        self.assertEqual(e.state, before)
        retry["receipt_context"]["purpose"] = "purpose:publish"
        self.assertEqual(e.operation(retry, 3)["code"], "idempotency_conflict")
        self.assertEqual(e.state, before)
        for variant in ("deadline", "read", "use", "metadata"):
            with self.subTest(replay_loss=variant):
                e = engine(v)
                op = copy.deepcopy(v["operations"][0])
                if variant == "deadline":
                    e.state["records"][0]["envelope"]["disclosure"]["retain_until"] = "2026-10-17T00:00:01Z"
                first = e.operation(op, 0)
                retry = copy.deepcopy(op)
                retry["at"] = "2026-10-17T00:00:01Z"
                if variant == "metadata":
                    for grant in e.state["policy"]["grants"]: grant["metadata"] = False
                elif variant != "deadline":
                    e.state["runtime"]["revocations"].append({"principal": op["actor"],
                        "audience": op["receipt_context"]["audience"],
                        "purpose": op["receipt_context"]["purpose"], "right": variant,
                        "owner": op["actor"], "at": retry["at"]})
                before = copy.deepcopy(e.state)
                self.assertEqual(e.operation(retry, 1),
                                 {"type": "refusal", "code": "not_authorized", "retryable": False})
                self.assertEqual(e.state, before)
                self.assertEqual(e.state["runtime"]["idempotency"][0]["receipt"], first)

    # R7-041: incomparable and historical authority candidates refuse atomically; current
    # receipt order, challenge exemption and exact replay remain valid independently of arrival.
    def test_authority_slot_cas(self):
        base = SPEC.parent / "conformance/cases"
        cases = {suffix: strict_loads((base / ("astra-24-ambiguous-cas" + suffix + ".vector.json")).read_text())
                 for suffix in ("", "-stale", "-control", "-challenge")}
        for suffix, case in cases.items():
            with self.subTest(case=suffix):
                e = engine(case)
                before, dirty = copy.deepcopy(e.state), copy.deepcopy(e.dirty_since)
                report = e.execute(case["operations"], case["query"])
                self.assertEqual(compare(report, case, Grammar(SPEC / "kernel/schemas")), ([], []))
                if suffix in ("", "-stale"):
                    self.assertEqual(report["operation_results"][1],
                                     {"type": "refusal", "code": "version_conflict", "retryable": True})
                    self.assertEqual(e.state, before)
                    self.assertEqual(e.dirty_since, dirty)
        # Same admitted receipts with the later unique ordering accept the exact earlier request.
        e = engine(cases[""])
        e.state["policy"]["authority_events"] = copy.deepcopy(cases["-control"]["initial_state"]["policy"]["authority_events"])
        e.state["records"].reverse()
        op = copy.deepcopy(cases[""]["operations"][1])
        first = e.operation(op, 1)
        self.assertEqual(first["outcome"], "revised")
        op["context"]["at"] = "2026-10-17T00:00:01Z"
        before = copy.deepcopy(e.state)
        self.assertEqual(e.operation(op, 2), first)
        self.assertEqual(e.state, before)
        op["expected_version"] = {"id": "rec:d", "version": 2}
        self.assertEqual(e.operation(op, 3)["code"], "idempotency_conflict")
        self.assertEqual(e.state, before)
        # With the former unique head withdrawn, the remaining maximal receipt is now d2.
        op["idempotency_key"] = "key:withdraw-next"
        op["revision"]["envelope"]["id"] = "rec:withdraw-next"
        op["revision"]["body"]["target"] = {"id": "rec:d", "version": 2}
        e.state["policy"]["reviews"].append({"record": ref(op["revision"]), "result": "allow"})
        fact = copy.deepcopy(next(f for f in e.state["policy"]["lineage_facts"]
                                  if f["output"]["id"] == "rec:withdraw-candidate"))
        fact["output"] = ref(op["revision"])
        e.state["policy"]["lineage_facts"].append(fact)
        final = e.operation(op, 4)
        self.assertEqual(final.get("outcome"), "revised", final)

    # K-PUB-2/K-DISC-3: every exact associated publication needs its own current check;
    # same-origin copies keep evidence/source identity while missing checks downgrade currentness.
    def test_import_check_coverage(self):
        base = SPEC.parent / "conformance/cases"
        for suffix in ("", "-unverified", "-control"):
            with self.subTest(fixture=suffix):
                case = strict_loads((base / ("astra-26-import-check-coverage" + suffix + ".vector.json")).read_text())
                self.assertEqual(compare(engine(case).execute(case["operations"], case["query"]), case,
                                         Grammar(SPEC / "kernel/schemas")), ([], []))
        v = strict_loads((base / "astra-26-import-check-coverage-control.vector.json").read_text())
        complete = engine(v).read(v["query"])
        for source in ("rec:copy1", "rec:copy2", "rec:copy3"):
            with self.subTest(missing_exact_check=source):
                e = engine(v)
                e.state["policy"]["imports"] = [i for i in e.state["policy"]["imports"] if i["source"]["id"] != source]
                before = copy.deepcopy(e.state)
                result = e.read(v["query"])
                self.assertEqual(result["currentness"], "last_received")
                self.assertEqual(result["items"][0]["currentness"], "last_received")
                for part in ("support", "oppose"):
                    self.assertEqual({k: v for k, v in result["items"][0][part].items() if k != "authorized_snapshot_handle"},
                                     {k: v for k, v in complete["items"][0][part].items() if k != "authorized_snapshot_handle"})
                    self.assertEqual(result["items"][0][part]["authorized_snapshot_handle"], result["authorized_snapshot_handle"])
                self.assertEqual(result["items"][0]["source_refs"], complete["items"][0]["source_refs"])
                self.assertEqual(e.state, before)
                # An ordinary document does not require a publication current-version check.
                next(r for r in e.state["records"] if r["envelope"]["id"] == source)["body"]["source_kind"] = "document"
                self.assertEqual(e.read(v["query"])["currentness"], "current")

        e = engine(v)
        e.state["policy"]["imports"] = [i for i in e.state["policy"]["imports"] if i["source"]["id"] != "rec:copy3"]
        next(r for r in e.state["records"] if r["envelope"]["id"] == "rec:copy3")["envelope"]["disclosure"]["audiences"] = []
        hidden = e.read(v["query"])
        self.assertEqual(hidden["currentness"], "current")
        self.assertEqual(hidden["items"][0]["source_refs"], [{"id": "rec:copy1", "version": 1}, {"id": "rec:copy2", "version": 1}])
        self.assertEqual(hidden["items"][0]["support"]["independent_root_count"], 1)

    # K-EVAL-8: a recomputed snapshot retains transitive eligible review paths across schemas;
    # hiding any necessary path element filters downstream refs without recreating dirty evidence.
    def test_transitive_review_paths(self):
        v = strict_loads((SPEC.parent / "conformance/cases/astra-24-transitive-review.vector.json").read_text())
        e = engine(v)
        baseline = e.execute(v["operations"], v["query"])
        with self.subTest(exact_fixture=True):
            self.assertEqual(compare(baseline, v, Grammar(SPEC / "kernel/schemas")), ([], []))
        b = {"id": "rec:dependent", "version": 1}
        for hidden, expected in (("rec:review-dependent", []), ("rec:review-second", [b]),
                                 ("rec:dependent", []), ("rec:dependent-c", [b]), ("rec:d", [])):
            with self.subTest(hidden=hidden):
                e = engine(v)
                r = next(r for r in e.state["records"] if r["envelope"]["id"] == hidden)
                r["envelope"]["disclosure"]["audiences"] = ["aud:public"]
                before = copy.deepcopy(e.state)
                result = e.read(v["query"])
                self.assertEqual(result["review_required"], expected)
                for item, original in zip(result["items"], baseline["result"]["items"]):
                    for part in ("ref", "content", "currentness", "needs_review"):
                        self.assertEqual(item[part], original[part])
                    for part in ("support", "oppose"):
                        self.assertEqual({k: v for k, v in item[part].items() if k != "authorized_snapshot_handle"},
                                         {k: v for k, v in original[part].items() if k != "authorized_snapshot_handle"})
                        self.assertEqual(item[part]["authorized_snapshot_handle"], result["authorized_snapshot_handle"])
                self.assertEqual(len(result["items"]), len(baseline["result"]["items"]))
                self.assertEqual(result["cutoffs"], [])
                self.assertEqual(e.state, before)
                self.assertEqual(e.state["runtime"]["dirty"], [])
                self.assertEqual(e.state["runtime"]["dirty_causes"], [])
        # Registered review edges may cycle; the finite reached set still contains B and C once.
        e = engine(v)
        edge = copy.deepcopy(next(r for r in e.state["records"] if r["envelope"]["id"] == "rec:review-second"))
        edge["envelope"]["id"] = "rec:review-cycle"
        edge["envelope"]["recorded"]["sequence"] = e.state["runtime"]["memory_cut"] + 1
        edge["body"]["target"]["assertion"] = b
        edge["body"]["premises"][0]["literal"]["assertion"] = {"id": "rec:dependent-c", "version": 1}
        e.state["records"].append(edge)
        fact = copy.deepcopy(next(f for f in e.state["policy"]["lineage_facts"] if f["output"]["id"] == "rec:review-second"))
        fact["output"] = ref(edge)
        e.state["policy"]["lineage_facts"].append(fact)
        e.state["runtime"]["memory_cut"] += 1
        e.state["runtime"]["committed_cuts"].append(e.state["runtime"]["memory_cut"])
        q = copy.deepcopy(v["query"])
        q["cut"]["memory"] = e.state["runtime"]["memory_cut"]
        before = copy.deepcopy(e.state)
        result = e.read(q)
        self.assertEqual(result["review_required"], [b, {"id": "rec:dependent-c", "version": 1}])
        self.assertEqual(e.state, before)

    # K-EVAL-8/K-RULE-2: mixed impact paths carry a review obligation only after a review
    # edge; sufficient-only/documentary paths and hidden necessary certificates do not create one.
    def test_mixed_review_paths(self):
        v = strict_loads((SPEC.parent / "conformance/cases/astra-24-transitive-review.vector.json").read_text())
        certificate = next(r for r in vector("S17")["initial_state"]["records"] if r["envelope"]["id"] == "cert:j")
        b, c = {"id": "rec:dependent", "version": 1}, {"id": "rec:dependent-c", "version": 1}
        for roles, expected in ((("review_on_change", "sufficient_support"), [b, c]),
                                (("sufficient_support", "review_on_change"), [c]),
                                (("sufficient_support", "sufficient_support"), []),
                                (("documentary_basis", "review_on_change"), [])):
            with self.subTest(roles=roles):
                e = engine(v)
                certs = []
                for name, role in zip(("rec:review-dependent", "rec:review-second"), roles):
                    edge = next(r for r in e.state["records"] if r["envelope"]["id"] == name)
                    edge["body"]["role"] = role
                    if role != "sufficient_support": continue
                    cert = copy.deepcopy(certificate)
                    cert["envelope"]["id"] = "cert:" + name
                    e.state["runtime"]["memory_cut"] += 1
                    cert["envelope"]["recorded"]["sequence"] = e.state["runtime"]["memory_cut"]
                    cert["body"]["pins"]["subject"] = ref(edge)
                    cert["body"]["pins"]["rule"] = edge["body"]["rule"]
                    edge["body"]["rule_kind"] = "checked_entailment"
                    edge["body"]["check"] = ref(cert)
                    e.state["records"].append(cert)
                    fact = copy.deepcopy(next(f for f in e.state["policy"]["lineage_facts"] if f["output"] == ref(edge)))
                    fact["output"] = ref(cert)
                    e.state["policy"]["lineage_facts"].append(fact)
                    certs.append(cert)
                e.state["runtime"]["committed_cuts"] = sorted(set(e.state["runtime"]["committed_cuts"]) | {e.state["runtime"]["memory_cut"]})
                q = copy.deepcopy(v["query"])
                q["cut"]["memory"] = e.state["runtime"]["memory_cut"]
                before = copy.deepcopy(e.state)
                result = e.read(q)
                self.assertEqual(result["review_required"], expected)
                self.assertEqual(result["items"][0]["support"]["witness"], "not_found")
                self.assertEqual(result["items"][0]["oppose"]["witness"], "not_found")
                self.assertEqual(e.state, before)
                if roles == ("sufficient_support", "review_on_change"):
                    certs[0]["envelope"]["disclosure"]["audiences"] = []
                    self.assertEqual(e.read(q)["review_required"], [])

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
