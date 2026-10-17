"""Package-only evaluator. No vector identifiers or expected results enter this module."""

import copy
import datetime
import itertools
import secrets

from common import Refused, applicable, cjson, key, ref, refs, stamp
from disclosure import lineage_complete, record_grant


class Evaluation:
    def __init__(self, engine, query):
        self.engine, self.q = engine, query
        self.p, self.rt = engine.state["policy"], engine.state["runtime"]
        self.records = {key(r): r for r in engine.state["records"]
                        if r["envelope"]["recorded"]["sequence"] <= query["cut"]["memory"]}
        self.schemas = {key(s): s for s in engine.state["domain_schemas"]}
        self.rule = next((r for r in engine.state["projection_rules"]
                          if key(r) == key(query["projection_rule"])), None)
        self.revisions = sorted((r for r in self.records.values() if r["envelope"]["kind"] == "revision"),
                                key=lambda r: r["envelope"]["recorded"]["sequence"])
        self.withdrawn, self.replaced = set(), set()
        for r in self.revisions:
            b = r["body"]
            if b["relation"] == "withdraw":
                self.withdrawn.add(key(b["target"]))
            if b["relation"] in ("replace", "correct"):
                self.replaced.add(key(b["target"]))
        self.fenced = {key(x) for x in self.rt["fences"] + self.rt["erased"]}
        self.bounds = {k: min(v, self.p["limits"]["read"][k]) for k, v in query["bounds"].items()}
        self.walk_cache = {}
        self.dirty_cache = None

    def impact_eligible(self, record, historical_inputs=False):
        if not self.visible(record) or record["envelope"]["perspective"] != self.rule["perspective"]:
            return False
        e, b = record["envelope"], record["body"]
        if e["kind"] == "justification":
            inputs = [x["source"] if x["kind"] == "source" else x["literal"]["assertion"] for x in b["premises"]]
            if not all(self.visible(self.records.get(key(x)), active=not historical_inputs)
                       and self.records[key(x)]["envelope"]["perspective"] == self.rule["perspective"] for x in inputs):
                return False
            if b["role"] == "sufficient_support":
                check = self.records.get(key(b["check"]))
                return (check is not None and self.check(check, ref(record), b["rule"])
                        and check["body"]["check_kind"] == "formal_entailment"
                        and check["body"]["executor"] == "deterministic")
            return b["role"] == "review_on_change"
        if e["kind"] == "assessment" and b["target"]:
            return self.check(record, b["target"]["assertion"])
        return False

    def affected_dirty(self):
        if self.dirty_cache is not None:
            return self.dirty_cache
        if "dirty_causes" not in self.rt:
            self.dirty_cache = {key(x) for x in self.rt["dirty"] if self.q["cut"]["memory"] >= self.engine.dirty_since.get(key(x), self.rt["memory_cut"])}
            return self.dirty_cache
        affected = set()
        for cause in self.rt["dirty_causes"]:
            revision = self.records.get(key(cause["revision"]))
            if (revision is None or not self.visible(revision, active=False)
                    or revision["envelope"]["perspective"] != self.rule["perspective"]):
                continue
            before_query = copy.deepcopy(self.q)
            before_query["cut"]["memory"] = revision["envelope"]["recorded"]["sequence"] - 1
            before = Evaluation(self.engine, before_query)
            target = before.records.get(key(revision["body"]["target"]))
            if target is None or not before.visible(target) or target["envelope"]["perspective"] != self.rule["perspective"]:
                continue
            reached = {key(target)}
            edges = [edge for edge in self.engine.impacts(before.records.values()) if before.impact_eligible(edge[0])]
            while True:
                prior = set(reached)
                for _, inputs, conclusion in edges:
                    if inputs & reached:
                        reached.add(conclusion)
                if reached == prior:
                    break
            if key(cause["assertion"]) in reached and self.visible(self.records.get(key(cause["assertion"]))):
                affected.add(key(cause["assertion"]))
        self.dirty_cache = affected
        return affected

    def grant(self, r, right, metadata=True):
        return record_grant(self.engine, r, self.q, right, metadata)

    def visible(self, r, active=True, time=True):
        if r is None:
            return False
        e, k = r["envelope"], key(r)
        if self.rule and self.rule["family"] == "audience_projection" and not lineage_complete(self.engine, r):
            return False
        if e["recorded"]["sequence"] > self.q["cut"]["memory"]:
            return False
        if active and (k in self.withdrawn or k in self.replaced):
            return False
        if k in self.fenced and e["kind"] != "source":
            return False
        if e["space"] != self.q["scope"]["space"] or e["context"] != self.q["mode"]:
            return False
        if time and not applicable(e["valid"], self.q["valid_at"]):
            return False
        d = self.engine.disclosure(r, self.q)
        if self.q["audience"] not in d["audiences"] or self.q["purpose"] not in d["purposes"]:
            return False
        if d["retain_until"] is not None and self.q["now"] >= d["retain_until"]:
            return False
        return self.grant(r, "read") and self.grant(r, "use")

    def source_available(self, source):
        k = key(source)
        r = self.records.get(k)
        if r is None or k in self.fenced:
            return False
        availability = r["body"]["availability"]
        for revision in self.revisions:
            b = revision["body"]
            if b["relation"] == "availability" and key(b["target"]) == k:
                availability = b["availability"]
        return availability == "resolvable" and any(key(f["source"]) == k and f["resolvable"]
                                                    for f in self.p["source_access"])

    def check(self, assessment, subject, rule=None):
        if not self.visible(assessment):
            return False
        e, b = assessment["envelope"], assessment["body"]
        pins = b["pins"]
        return (b["result"] == "pass" and pins["subject"] == subject
                and pins["policy"] == self.p["evidence"]["policy_pin"]
                and pins["environment"] == self.p["evidence"]["environment_pin"]
                and (rule is None or pins["rule"] == rule)
                and (b["usable_until"] is None or self.q["now"] < b["usable_until"])
                and (b["executor"] != "model" or b["check_kind"] == "semantic_review")
                and e["perspective"] == self.rule["perspective"]
                and all(self.visible(self.records.get(key(s))) for s in b["sources"]))

    def eligible_rules(self, literal):
        out = []
        for r in self.records.values():
            e, b = r["envelope"], r["body"]
            if e["kind"] != "justification" or b["role"] != "sufficient_support":
                continue
            if b["target"] != literal or not self.visible(r) or e["perspective"] != self.rule["perspective"]:
                continue
            if b["rule_kind"] != "checked_entailment":
                continue
            check = self.records.get(key(b["check"]))
            if check is None or not self.check(check, ref(r), b["rule"]):
                continue
            cb = check["body"]
            if cb["check_kind"] != "formal_entailment" or cb["executor"] != "deterministic" or cb["target"] is not None:
                continue
            if not all(x["kind"] == "assertion" and self.visible(self.records.get(key(x["literal"]["assertion"])))
                       and self.records[key(x["literal"]["assertion"])]["envelope"]["perspective"] == self.rule["perspective"]
                       for x in b["premises"]):
                continue
            out.append(r)
        return sorted(out, key=key)

    def walk(self, assertion, polarity):
        cachekey = key(assertion), polarity
        if cachekey in self.walk_cache:
            return self.walk_cache[cachekey]
        counters = {"roots": 0, "rules": 0, "source_resolutions": 0}
        sources_seen, memo = set(), {}

        def visit(k, p):
            lk = k, p
            if lk in memo:
                return memo[lk]
            result = {"paths": [], "cutoffs": set()}
            memo[lk] = result
            target = self.records.get(k)
            if not self.visible(target):
                return result
            if k in self.affected_dirty():
                result["cutoffs"].add("dirty")
                return result
            literal = {"assertion": ref(k), "polarity": p}

            def charge(component, cutoff):
                if counters[component] >= self.bounds[component]:
                    result["cutoffs"].add(cutoff)
                    return False
                counters[component] += 1
                return True

            roots = sorted((r for r in self.records.values() if r["envelope"]["kind"] == "assessment"
                            and r["body"]["target"] == literal), key=key)
            for r in roots:
                b = r["body"]
                if b["check_kind"] not in self.p["evidence"]["root_kinds"] or not self.check(r, ref(k)):
                    continue
                if not charge("roots", "root_limit"):
                    continue
                available, capped = True, False
                for s in b["sources"]:
                    sk = key(s)
                    if b["source_requirement"] == "current" and sk not in sources_seen:
                        if not charge("source_resolutions", "source_limit"):
                            capped = True
                            continue
                        sources_seen.add(sk)
                    available = available and self.source_available(s)
                if capped:
                    continue
                if not available and b["source_requirement"] == "current":
                    result["cutoffs"].add("source_unavailable")
                    continue
                source_state = ("resolvable_now" if available else
                                "independent_attestation" if b["source_requirement"] == "independent" else "prior_assessment_only")
                result["paths"].append({"nodes": {key(r)}, "origins": {b["origin"]},
                                        "qualifications": {b["check_kind"]}, "source_state": source_state,
                                        "sources": {key(s) for s in b["sources"]}, "premises": set()})
            for r in self.eligible_rules(literal):
                if not charge("rules", "rule_limit"):
                    continue
                literals = sorted((x["literal"] for x in r["body"]["premises"]),
                                  key=lambda x: (key(x["assertion"]), x["polarity"]))
                children = [visit(key(x["assertion"]), x["polarity"]) for x in literals]
                for ch in children:
                    result["cutoffs"].update(ch["cutoffs"])
                if not children or any(not ch["paths"] for ch in children):
                    continue
                for combination in itertools.product(*(ch["paths"] for ch in children)):
                    ranks = {"resolvable_now": 0, "independent_attestation": 1, "prior_assessment_only": 2}
                    result["paths"].append({
                        "nodes": {key(r)} | set().union(*(p["nodes"] for p in combination)),
                        "origins": set().union(*(p["origins"] for p in combination)),
                        "qualifications": {"formal_entailment"} | set().union(*(p["qualifications"] for p in combination)),
                        "source_state": max((p["source_state"] for p in combination), key=ranks.get),
                        "sources": set().union(*(p["sources"] for p in combination)),
                        "premises": {(key(x["assertion"]), x["polarity"]) for x in literals}
                                    | set().union(*(p["premises"] for p in combination))})
            return result

        result = visit(key(assertion), polarity)
        self.walk_cache[cachekey] = result
        return result

    def associated_sources(self, assertion):
        out = set()
        for r in self.records.values():
            e, b = r["envelope"], r["body"]
            if not self.visible(r):
                continue
            if e["kind"] == "assessment" and b["target"] and key(b["target"]["assertion"]) == key(assertion):
                out.update(key(s) for s in b["sources"] if self.visible(self.records.get(key(s))))
            if e["kind"] == "justification" and key(b["target"]["assertion"]) == key(assertion):
                out.update(key(x["source"]) for x in b["premises"] if x["kind"] == "source"
                           and self.visible(self.records.get(key(x["source"]))))
        receipt = assertion["body"]["authority_receipt"]
        if receipt and self.visible(self.records.get(key(receipt))):
            out.add(key(receipt))
        return out

    def freshness(self, r):
        horizon = self.q["usable_until"]
        default = self.schemas[key(r["envelope"]["schema"])]["freshness_default"]
        if horizon is None and default["kind"] != "none":
            if r["envelope"]["confirmed_at"] is None:
                return "stale", None
            horizon = (stamp(r["envelope"]["confirmed_at"]) + datetime.timedelta(seconds=default["seconds"])).strftime("%Y-%m-%dT%H:%M:%SZ")
        return ("not_applicable" if horizon is None else "fresh" if self.q["now"] < horizon else "stale"), horizon

    def channel(self, r, polarity, handle):
        walk = self.walk(r, polarity)
        paths = walk["paths"]
        qualities = []
        for path in paths:
            tainted, unchecked = False, False
            for premise, sign in path["premises"]:
                other = self.walk(ref(premise), "oppose" if sign == "support" else "support")
                tainted |= bool(other["paths"])
                unchecked |= bool(other["cutoffs"]) and not other["paths"]
            qualities.append("tainted" if tainted else "unchecked" if unchecked else "clean")
        quality = ("clean_path" if "clean" in qualities else "conflicted_premises_only"
                   if qualities and not walk["cutoffs"] and all(q == "tainted" for q in qualities)
                   else "not_fully_checked")
        coverage = {"kind": "unknown"}
        declarations = [c["declaration"] for c in self.p["coverage"] if key(c["assertion"]) == key(r)
                        and self.visible(self.records.get(key(c["declaration"])))]
        if len(declarations) > 1:
            raise Refused("invalid_reference")
        if declarations:
            coverage = {"kind": "declared", "ref": declarations[0]}
        roots = sorted(set().union(*(p["origins"] for p in paths)))
        ranks = {"resolvable_now": 0, "independent_attestation": 1, "prior_assessment_only": 2}
        source_state = (min((p["source_state"] for p in paths), key=ranks.get) if paths else
                        "prior_assessment_only" if any(not self.source_available(ref(s)) for s in self.associated_sources(r))
                        else "resolvable_now")
        return {"witness": "present" if paths else "not_found", "evaluation": "incomplete" if walk["cutoffs"] else "complete",
                "corpus_coverage": coverage, "premise_quality": quality,
                "evidence_qualification": sorted(set().union(*(p["qualifications"] for p in paths))),
                "source_state": source_state, "freshness": self.freshness(r)[0],
                "authorized_snapshot_handle": handle, "dependency_coverage": "registered_only",
                "witness_roots": roots, "independent_root_count": len(roots)}

    def sequence(self, r):
        return self.engine.sequence(r)

    def statuses(self, candidates):
        statuses, groups = {}, {}
        for r in candidates:
            groups.setdefault(self.sequence(r), []).append(r)
        for group in groups.values():
            if group[0]["body"]["statement_kind"] == "decision_record":
                heads = self.engine.authority_heads(group)
                for r in group:
                    statuses[key(r)] = ("historical" if r not in heads else
                                        "ambiguous_current" if len(heads) > 1 else "current")
            else:
                for r in group:
                    statuses[key(r)] = "historical" if key(r) in self.replaced else "current"
        for r in candidates:
            if statuses[key(r)] == "historical":
                continue
            sources = self.associated_sources(r)
            sources = {s for s in sources if self.records[s]["body"]["source_kind"] == "publication"}
            if not sources:
                continue
            imports = [i for i in self.p["imports"] if key(i["source"]) in sources]
            if any(i["status"] == "replaced" for i in imports):
                statuses[key(r)] = "historical"
            elif (self.freshness(r)[0] == "stale" or {key(i["source"]) for i in imports} != sources
                  or any(i["status"] != "current" or i["checked_at"] is None for i in imports)):
                statuses[key(r)] = "last_received"
        return statuses

    def review_required(self):
        required = set(self.affected_dirty())
        reached, reviewed = self.withdrawn | self.replaced, set()
        edges = [edge for edge in self.engine.impacts(self.records.values())
                 if self.impact_eligible(edge[0], historical_inputs=True)]
        while True:
            before = len(reached), len(reviewed)
            for record, inputs, target in edges:
                if inputs & reached:
                    reached.add(target)
                    if record["body"].get("role") == "review_on_change" or inputs & reviewed:
                        reviewed.add(target)
            if before == (len(reached), len(reviewed)):
                break
        return {k for k in required | reviewed if self.visible(self.records.get(k))}

    def incompatible(self, target, candidates, statuses):
        e, b = target["envelope"], target["body"]
        domain = self.schemas[key(e["schema"])]
        found = set()
        for rule in domain["incompatibilities"]:
            for other in candidates:
                oe, ob = other["envelope"], other["body"]
                if key(other) == key(target) or statuses[key(other)] == "historical":
                    continue
                if any(e[k] != oe[k] for k in ("schema", "subject", "space", "perspective")) or b["slot"] != ob["slot"]:
                    continue
                if b["statement_kind"] not in rule["statement_kinds"] or ob["statement_kind"] not in rule["statement_kinds"]:
                    continue
                v, ov = e["valid"], oe["valid"]
                if v["kind"] != "known" or ov["kind"] != "known":
                    continue
                if (v["to"] is not None and ov["from"] >= v["to"]) or (ov["to"] is not None and v["from"] >= ov["to"]):
                    continue
                content = {x["field"]: x["value"] for x in b["content"]}
                oc = {x["field"]: x["value"] for x in ob["content"]}
                if rule["relation"] == "unequal" and content[rule["field"]] != oc[rule["field"]]:
                    found.add(key(other))
        return refs(found)

    def run(self):
        q = self.q
        self.engine.grammar.check(q, "query")
        if key(q["scope"]["schema"]) not in self.schemas:
            raise Refused("unknown_schema")
        if self.rule is None:
            raise Refused("unknown_rule")
        if q["policy"] != self.p["revision"] or q["evidence_policy"] != self.p["evidence"]["ref"]:
            raise Refused("policy_mismatch")
        if not self.rt["memory_available"] or self.p["public_availability"] == "degraded":
            raise Refused("unavailable")
        if self.rt["restore"]["status"] != "open":
            raise Refused("erasure_fenced")
        if q["cut"]["memory"] not in self.rt["committed_cuts"] or q["cut"]["memory"] > self.rt["memory_cut"] or q["cut"]["sources"] != self.rt["source_cuts"]:
            raise Refused("invalid_time")
        stamp(q["now"])
        if q["valid_at"] != "any":
            stamp(q["valid_at"])
        public = self.rule["family"] == "audience_projection"
        if public and (q["audience"] != self.rule["audience"] or q["purpose"] != self.rule["purpose"]):
            raise Refused("not_authorized")
        candidates = [r for r in self.records.values() if r["envelope"]["kind"] == "assertion"
                      and key(r) not in self.withdrawn and self.visible(r, active=False)
                      and r["envelope"]["subject"] == q["scope"]["subject"]
                      and r["envelope"]["perspective"] == self.rule["perspective"]]
        statuses = self.statuses(candidates)
        chosen_scope = [r for r in candidates if r["envelope"]["schema"] == q["scope"]["schema"]
                        and r["envelope"]["issuer"] == self.rule["issuer"]]
        targets = {key(t) for t in q["scope"]["targets"]}
        selected = sorted((r for r in chosen_scope if (key(r) in targets if targets else statuses[key(r)] != "historical")), key=key)
        excluded = {key(r) for r in self.rule.get("excluded_refs", [])} if public else set()
        selected = [r for r in selected if key(r) not in excluded]
        selected_keys = {key(r) for r in selected}
        self.selected_refs = selected_keys
        selected_sequences = {self.sequence(r) for r in selected}
        historical = refs(key(r) for r in chosen_scope if statuses[key(r)] == "historical"
                          and key(r) not in selected_keys | excluded
                          and (not targets or self.sequence(r) in selected_sequences))
        required = self.review_required() - excluded
        handle = secrets.token_hex(16)
        view = {"type": "view", "semantic_profile": self.engine.version, "projection_rule": q["projection_rule"],
                "evidence_policy": q["evidence_policy"], "policy": q["policy"], "authorized_snapshot_handle": handle,
                "data_classification": "data", "items": [], "currentness": "none", "historical": historical,
                "review_required": refs(required), "explanation": {"status": "complete", "paths": [], "reason": None},
                "cutoffs": [], "changes": {"state": "initial", "refs": []}}
        cutoffs, proofs = set(), {}
        for r in selected:
            e, b = r["envelope"], r["body"]
            item = {k: copy.deepcopy(e[k]) for k in ("subject", "issuer", "submitter", "perspective", "representation_ref",
                                                        "admission_class", "valid", "confirmed_at")}
            item.update({"ref": ref(r), "statement_kind": b["statement_kind"], "content": b["content"],
                         "usable_until": self.freshness(r)[1], "currentness": statuses[key(r)],
                         "authority_receipt": b["authority_receipt"], "incompatible_with": self.incompatible(r, candidates, statuses),
                         "needs_review": key(r) in required, "source_refs": refs(self.associated_sources(r))})
            found_sources = set()
            for polarity in ("support", "oppose"):
                item[polarity] = self.channel(r, polarity, handle)
                w = self.walk(r, polarity)
                cutoffs.update(w["cutoffs"])
                for path in w["paths"]:
                    found_sources.update(path["sources"])
                    proof = refs(path["nodes"])
                    proofs[cjson(proof)] = proof
            item["source_refs"] = refs([*item["source_refs"], *found_sources])
            if public:
                def alias(principal):
                    found = next((h["handle"] for h in self.p["handles"] if h["subject"] == principal
                                  and h["space"] == e["space"] and h["audience"] == q["audience"]), None)
                    if found is None:
                        raise Refused("not_authorized")
                    return found
                for k in ("subject", "issuer", "submitter"):
                    item[k] = alias(item[k])
                item["perspective"]["principal"] = alias(item["perspective"]["principal"])
                item.update(ref=None, representation_ref=None, authority_receipt=None, source_refs=[], incompatible_with=[])
                for polarity in ("support", "oppose"):
                    item[polarity]["witness_roots"] = []
            view["items"].append(item)
        if selected:
            states = {item["currentness"] for item in view["items"]}
            view["currentness"] = "ambiguous_current" if "ambiguous_current" in states else "last_received" if "last_received" in states else "current"
        view["cutoffs"] = sorted(cutoffs)
        if q["kind"] == "explain":
            ordered = [proofs[k] for k in sorted(proofs)]
            limit = self.bounds["explanations"]
            reason = "explanation_limit" if len(ordered) > limit else "evaluation_limit" if cutoffs else None
            view["explanation"] = {"status": "partial" if reason else "complete", "paths": ordered[:limit], "reason": reason}
        if public:
            view["historical"], view["review_required"] = [], []
            view["explanation"]["paths"] = []
        if q["kind"] == "changes" and q["since"] is not None:
            saved = self.engine.captures.get(q["since"])
            if saved is None or saved[1]["type"] != "view":
                raise Refused("not_authorized")
            oldq, oldview = saved
            if any(q[k] != oldq[k] for k in ("principal", "purpose", "audience", "projection_rule")) or any(q["scope"][k] != oldq["scope"][k] for k in ("space", "subject", "schema")):
                raise Refused("not_authorized")
            def stable(v):
                v = copy.deepcopy(v)
                v.pop("authorized_snapshot_handle", None)
                v.pop("changes", None)
                for item in v["items"]:
                    for polarity in ("support", "oppose"):
                        item[polarity].pop("authorized_snapshot_handle", None)
                return v
            changed = stable(view) != stable(oldview)
            olditems = {cjson(i["ref"]): i for i in stable(oldview)["items"]}
            changed_refs = [i["ref"] for i in stable(view)["items"] if i["ref"] is not None and olditems.get(cjson(i["ref"])) != i]
            view["changes"] = {"state": "changed" if changed else "unchanged", "refs": refs(changed_refs)}
        return view
