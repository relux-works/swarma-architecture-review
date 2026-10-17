"""Package wire adapter for the unchanged source baseline.

This module receives only initial state, operations and query. It cannot inspect
expected answers, vector IDs, forbidden predicates or another implementation.
Unsupported wire operations are reported instead of supplied with canned answers.
"""

import copy
import datetime
import json
import secrets

from evaluator import Evaluator, Memory, Refusal, applicable, incompatibilities, sequence_key


class Unsupported(Exception):
    pass


def key(ref):
    return json.dumps([ref["id"], ref["version"]], separators=(",", ":"))


def ref(record):
    envelope = record.get("envelope", record)
    return {"id": envelope["id"], "version": envelope["version"]}


def sorted_refs(refs):
    return sorted({key(r): r for r in refs}.values(), key=lambda r: (r["id"], r["version"]))


def refusal(code):
    return {"type": "refusal", "code": code,
            "retryable": code in {"version_conflict", "policy_mismatch", "unavailable",
                                   "stale_generation", "erasure_incomplete", "publication_stale"}}


class Adapter:
    def __init__(self, initial, profile):
        self.initial = copy.deepcopy(initial)
        self.policy = self.initial["policy"]
        self.runtime = self.initial["runtime"]
        self.records = {key(ref(r)): r for r in self.initial["records"]}
        self.schemas = {key(s): s for s in self.initial["domain_schemas"]}
        self.rules = {key(r): r for r in self.initial["projection_rules"]}
        self.profile = profile
        self.captures = []
        self.writer = None

    def granted(self, record, query, right):
        envelope = record["envelope"]
        for grant in self.policy["grants"]:
            if (grant["principal"] == query["principal"] and grant["space"] == envelope["space"]
                    and grant["audience"] == query["audience"] and grant["purpose"] == query["purpose"]
                    and right in grant["rights"] and grant["metadata"]
                    and ("*" in grant["records"] or envelope["id"] in grant["records"])):
                return True
        return False

    def normalized(self, record, query):
        e, b = record["envelope"], record["body"]
        valid = e["valid"]
        out = {"id": key(ref(record)), "kind": e["kind"], "issuer": e["issuer"],
               "reference_order": [e["id"], e["version"]],
               "subject": e["subject"], "space": e["space"],
               "perspective": json.dumps(e["perspective"], sort_keys=True),
               "mode": e["context"], "recorded": e["recorded"]["sequence"],
               "valid": "unknown" if valid["kind"] == "unknown" else [valid["from"], valid["to"]],
               "visible": (self.granted(record, query, "read") and self.granted(record, query, "use")
                           and query["audience"] in e["disclosure"]["audiences"]
                           and query["purpose"] in e["disclosure"]["purposes"]
                           and e["space"] == query["scope"]["space"])}
        if e["kind"] == "assertion":
            schema = self.schemas[key(e["schema"])]
            out.update(schema=key(e["schema"]), statement_kind=b["statement_kind"], slot=b["slot"],
                       schema_slot=b["slot"], content={f["field"]: f["value"] for f in b["content"]},
                       authority_receipt=key(b["authority_receipt"]) if b["authority_receipt"] else None)
            # The source's multi sequences use one identity for each coexisting value.
            if schema["cardinality"]["mode"] == "multi":
                out["slot"] = json.dumps([b["slot"], e["id"]])
            until = query["usable_until"]
            horizon = schema["freshness_default"]
            if until is None and horizon["kind"] == "duration":
                if e["confirmed_at"] is None:
                    raise Unsupported("Frozen core has no unknown-confirmation freshness state")
                stamp = datetime.datetime.fromisoformat(e["confirmed_at"].replace("Z", "+00:00"))
                until = (stamp + datetime.timedelta(seconds=horizon["seconds"])).isoformat().replace("+00:00", "Z")
            out["usable_until"] = until
        elif e["kind"] == "source":
            # Documentary source attribution need not be the observer's own
            # perspective; grants still gate it. It is not an assertion premise.
            out.pop("perspective")
            out["availability"] = b["availability"]
            for access in self.policy["source_access"]:
                if access["source"] == ref(record) and not access["resolvable"]:
                    out["availability"] = "unavailable"
        return out

    def query(self, query):
        if query["kind"] != "recall":
            raise Unsupported("Frozen core has no exact proof-path enumeration or changes output")
        if key(query["scope"]["schema"]) not in self.schemas:
            return refusal("unknown_schema")
        if key(query["projection_rule"]) not in self.rules:
            return refusal("unknown_rule")
        if query["policy"] != self.policy["revision"] or query["evidence_policy"] != self.policy["evidence"]["ref"]:
            return refusal("policy_mismatch")
        if self.policy["public_availability"] != "available":
            return refusal("unavailable")
        if self.runtime["restore"]["status"] != "open":
            return refusal("erasure_fenced")
        if query["cut"]["memory"] not in self.runtime["committed_cuts"] or query["cut"]["sources"] != self.runtime["source_cuts"]:
            return refusal("invalid_time")
        if self.runtime["dirty"]:
            raise Unsupported("Frozen core has no dirty/review-closure output")
        if self.runtime["revocations"]:
            raise Unsupported("Live policy revocation event grammar is not mapped in the first adapter")
        rule = self.rules[key(query["projection_rule"])]
        audience = rule["family"] == "audience_projection"
        if audience and (query["audience"] != rule["audience"] or query["purpose"] != rule["purpose"]):
            return refusal("not_authorized")
        if audience and any(r["envelope"]["disclosure"]["declassification"] for r in self.records.values()):
            raise Unsupported("Current multi-owner declassification decisions are not mapped yet")
        schema = self.schemas[key(query["scope"]["schema"])]
        nq = {"cut": query["cut"]["memory"], "valid_at": None if query["valid_at"] == "any" else query["valid_at"],
              "now": query["now"], "mode": query["mode"],
              "perspective": json.dumps(rule["perspective"], sort_keys=True),
              "qualifications": self.policy["evidence"]["root_kinds"],
              "root_budget": min(query["bounds"]["roots"], self.policy["limits"]["read"]["roots"]),
              "rule_budget": min(query["bounds"]["rules"], self.policy["limits"]["read"]["rules"]),
              "source_budget": min(query["bounds"]["source_resolutions"], self.policy["limits"]["read"]["source_resolutions"])}
        normalized = {k: self.normalized(r, query) for k, r in self.records.items()}
        if audience:
            for k, record in self.records.items():
                if record["envelope"]["lineage"] == "unknown":
                    normalized[k]["visible"] = False
        replacements = {}
        for k, record in self.records.items():
            if record["envelope"]["kind"] != "revision" or not applicable(normalized[k], nq):
                continue
            body = record["body"]
            target = key(body["target"])
            relation = body["relation"]
            if relation in {"withdraw", "replace", "correct"}:
                # Initial admitted revisions become normalized applicability data.
                if relation == "withdraw" or normalized[target]["kind"] != "assertion":
                    normalized[target]["withdrawn_at"] = normalized[k]["recorded"]
                if relation in {"replace", "correct"}:
                    replacements[key(body["replacement"])] = target
            elif relation == "availability":
                normalized[target]["availability"] = body["availability"]
        for successor, prior in replacements.items():
            normalized[successor]["replaces"] = prior
        for erased in self.runtime["erased"]:
            k = key(erased)
            if k in normalized:
                if normalized[k]["kind"] == "source":
                    normalized[k]["availability"] = "erased"
                else:
                    normalized[k]["visible"] = False
        assertions = [r for r in normalized.values() if r["kind"] == "assertion"]
        sources = [r for r in normalized.values() if r["kind"] == "source"]
        roots, rules = [], []
        associated = {r["id"]: [] for r in assertions}
        # Provenance is broader than signed roots. Exact subject-pinned checks
        # and authority receipts remain associations without becoming support.
        for k, record in self.records.items():
            e, b = record["envelope"], record["body"]
            if not applicable(normalized[k], nq):
                continue
            if e["kind"] == "assertion" and b["authority_receipt"]:
                receipt = b["authority_receipt"]
                if key(receipt) in normalized and applicable(normalized[key(receipt)], nq):
                    associated[k].append(receipt)
            if e["kind"] == "assessment" and key(b["pins"]["subject"]) in associated:
                target = key(b["pins"]["subject"])
                associated[target].extend(s for s in b["sources"]
                                          if key(s) in normalized and applicable(normalized[key(s)], nq))
        for k in sorted(self.records, key=lambda x: (self.records[x]["envelope"]["id"], self.records[x]["envelope"]["version"])):
            record, nr = self.records[k], normalized[k]
            e, b = record["envelope"], record["body"]
            if e["kind"] == "assessment" and b["target"] is not None:
                target = key(b["target"]["assertion"])
                source_keys = [key(s) for s in b["sources"]]
                source_visible = all(s in normalized and applicable(normalized[s], nq) for s in source_keys)
                if source_visible and applicable(nr, nq):
                    associated[target].extend(b["sources"])
                pins = b["pins"]
                admitted = (pins["subject"] == b["target"]["assertion"]
                            and pins["policy"] == self.policy["evidence"]["policy_pin"]
                            and pins["environment"] == self.policy["evidence"]["environment_pin"]
                            and (b["usable_until"] is None or query["now"] < b["usable_until"]))
                root = dict(nr, target=[target, b["target"]["polarity"]], qualification=b["check_kind"],
                            source_members=source_keys,
                            origin=b["origin"], result=b["result"], admitted=admitted,
                            retained=b["source_requirement"] != "current", independent=b["source_requirement"] == "independent")
                root["visible"] = root["visible"] and source_visible
                if source_keys:
                    # The core accepts one source per root. This synthetic source
                    # represents the conjunctive availability of the pinned inputs.
                    source_id = "adapter-source-group:" + k
                    availability = "resolvable" if all(normalized[s]["availability"] == "resolvable" for s in source_keys) else "unavailable"
                    sources.append({"id": source_id, "availability": availability,
                                    "mode": e["context"], "visible": source_visible})
                    root["source"] = source_id
                roots.append(root)
            elif e["kind"] == "justification":
                target = key(b["target"]["assertion"])
                if b["role"] != "sufficient_support":
                    if applicable(nr, nq):
                        associated[target].extend(p["source"] for p in b["premises"]
                                                  if p["kind"] == "source" and applicable(normalized[key(p["source"])], nq))
                    continue
                cert_key = key(b["check"])
                cert = self.records[cert_key]["body"]
                cert_valid = (applicable(normalized[cert_key], nq) and cert["result"] == "pass"
                              and cert["check_kind"] == "formal_entailment"
                              and cert["pins"]["subject"] == ref(record) and cert["pins"]["rule"] == b["rule"]
                              and cert["pins"]["policy"] == self.policy["evidence"]["policy_pin"]
                              and cert["pins"]["environment"] == self.policy["evidence"]["environment_pin"]
                              and (cert["usable_until"] is None or query["now"] < cert["usable_until"]))
                rules.append(dict(nr, target=[target, b["target"]["polarity"]],
                                  premises=[[key(p["literal"]["assertion"]), p["literal"]["polarity"]] for p in b["premises"]],
                                  checked=True, kind=b["rule_kind"], edge_role=b["role"],
                                  visible=nr["visible"] and cert_valid))
        receipt_to_assertion = {a["authority_receipt"]: a["id"] for a in assertions if a.get("authority_receipt")}
        for assertion in assertions:
            assertion["authority_after"] = []
            for event in self.policy["authority_events"]:
                if key(event["receipt"]) == assertion.get("authority_receipt"):
                    assertion["authority_after"] = [receipt_to_assertion[key(p)] for p in event["predecessors"]
                                                     if key(p) in receipt_to_assertion]
        engine = Evaluator(assertions, roots, rules, sources,
                           {k: [key(s) for s in refs] for k, refs in associated.items()})
        projection_records = [a for a in assertions if a["schema"] == key(query["scope"]["schema"])]
        projection = Memory(projection_records).project(nq | {"issuer": rule["issuer"], "subject": query["scope"]["subject"]})
        all_current = Memory(projection_records).project(nq | {"subject": query["scope"]["subject"]})["current"]
        incompatible = incompatibilities([normalized[k] for k in all_current], schema["incompatibilities"])
        excluded = {key(r) for r in rule.get("excluded_refs", [])} if audience else set()
        projection["historical"] = [k for k in projection["historical"] if k not in excluded]
        selected = ([key(r) for r in query["scope"]["targets"]] if query["scope"]["targets"] else projection["current"])
        selected = [k for k in selected if k in normalized and normalized[k]["kind"] == "assertion"
                    and k not in excluded
                    and applicable(normalized[k], nq) and normalized[k]["issuer"] == rule["issuer"]
                    and normalized[k]["schema"] == key(query["scope"]["schema"])
                    and normalized[k]["subject"] == query["scope"]["subject"]]
        if query["scope"]["targets"]:
            selected_sequences = {(normalized[k]["space"], sequence_key(normalized[k])) for k in selected}
            projection["historical"] = [k for k in projection["historical"]
                                        if (normalized[k]["space"], sequence_key(normalized[k])) in selected_sequences]
        handle = secrets.token_hex(16)
        items, cutoffs = [], set()
        for k in sorted(selected, key=lambda k: (self.records[k]["envelope"]["id"], self.records[k]["envelope"]["version"])):
            record, nr = self.records[k], normalized[k]
            e, b = record["envelope"], record["body"]
            coverage = [c for c in self.policy["coverage"] if key(c["assertion"]) == k
                        and key(c["declaration"]) in normalized and applicable(normalized[key(c["declaration"])], nq)]
            corpus = {"kind": "declared", "ref": coverage[0]["declaration"]} if coverage else {"kind": "unknown"}
            result = engine.evaluate(k, nq | {"corpus_coverage": corpus})
            cutoffs.update(result["cutoffs"])
            # Exact assessment references survive found paths separately from
            # deduplicated origins, so an unrelated copy cannot add provenance.
            found_assessments = set(result["support"]["witness_assessments"] + result["oppose"]["witness_assessments"])
            displayed_sources = list(associated[k])
            for root in roots:
                if root["id"] in found_assessments and applicable(root, nq):
                    body = self.records[root["id"]]["body"]
                    displayed_sources.extend(s for s in body["sources"]
                                             if applicable(normalized[key(s)], nq))
            for sign in ("support", "oppose"):
                channel = result[sign]
                origins = channel.pop("root_origins")
                channel.pop("witness_assessments")
                channel.update(witness_roots=origins, independent_root_count=len(origins), authorized_snapshot_handle=handle)
                channel["evidence_qualification"] = sorted({"formal_entailment" if q == "checked_entailment" else q
                                                           for q in channel["evidence_qualification"]})
            currentness = "historical" if k in projection["historical"] else "ambiguous_current" if k in projection["ambiguous"] else "current"
            for source in associated[k]:
                source_record = self.records[key(source)]
                if source_record["body"].get("source_kind") == "publication":
                    facts = [f for f in self.policy["imports"] if f["source"] == source]
                    if not facts or facts[0]["status"] != "current":
                        raise Unsupported("Frozen core has no imported-publication currentness state")
            items.append({"ref": ref(record), "subject": e["subject"], "issuer": e["issuer"], "submitter": e["submitter"],
                          "perspective": e["perspective"], "representation_ref": e["representation_ref"],
                          "admission_class": e["admission_class"], "statement_kind": b["statement_kind"],
                          "content": b["content"], "valid": e["valid"], "confirmed_at": e["confirmed_at"],
                          "usable_until": nr["usable_until"], "currentness": currentness, "authority_receipt": b["authority_receipt"],
                          "incompatible_with": sorted_refs(ref(self.records[x]) for x in incompatible.get(k, [])),
                          "needs_review": False, "source_refs": sorted_refs(displayed_sources),
                          "support": result["support"], "oppose": result["oppose"]})
            if audience:
                item = items[-1]
                aliases = {(row["subject"], row["space"], row["audience"]): row["handle"]
                           for row in self.policy["handles"]}
                for field in ("subject", "issuer", "submitter"):
                    alias = aliases.get((item[field], e["space"], query["audience"]))
                    if alias is None:
                        return refusal("not_authorized")
                    item[field] = alias
                alias = aliases.get((item["perspective"]["principal"], e["space"], query["audience"]))
                if alias is None:
                    return refusal("not_authorized")
                item["perspective"] = dict(item["perspective"], principal=alias)
                item.update(ref=None, representation_ref=None, authority_receipt=None,
                            source_refs=[], incompatible_with=[])
                for sign in ("support", "oppose"):
                    item[sign]["witness_roots"] = []
        return {"type": "view", "semantic_profile": self.profile, "projection_rule": query["projection_rule"],
                "evidence_policy": query["evidence_policy"], "policy": query["policy"], "authorized_snapshot_handle": handle,
                "data_classification": "data", "items": items,
                "currentness": "none" if not items else "ambiguous_current" if any(i["currentness"] == "ambiguous_current" for i in items) else "current",
                "historical": sorted_refs(ref(self.records[k]) for k in projection["historical"] if k not in selected),
                "review_required": [], "explanation": {"status": "complete", "paths": [], "reason": None},
                "cutoffs": sorted(cutoffs), "changes": {"state": "initial", "refs": []}}

    def execute(self, operations, query):
        unsupported = sorted({o["op"] for o in operations if o["op"] not in {"capture", "admit", "admit_raw", "revise"}})
        if unsupported:
            raise Unsupported("Unmapped frozen-core transaction operations: " + ", ".join(unsupported))
        operation_results = []
        for op in operations:
            if op["op"] == "capture":
                operation_results.append(self.query(op["query"]))
            else:
                if self.writer is None:
                    from transactions import Transactions
                    self.writer = Transactions(self)
                try:
                    operation_results.append(self.writer.apply(op))
                except Refusal as error:
                    operation_results.append(refusal(error.code))
        result = self.query(query)
        return {"operation_results": operation_results, "result": result,
                "postconditions": {"record_refs": sorted_refs(ref(r) for r in self.records.values()),
                                   "erased_refs": sorted_refs(self.runtime["erased"]),
                                   "custody_present": sorted(c["id"] for c in self.runtime["custody"] if c["present"]),
                                   "dirty": sorted_refs(self.runtime["dirty"]),
                                   "control_observations": self.runtime["control_observations"],
                                   "external_effects": self.runtime["external_effects"]}}
