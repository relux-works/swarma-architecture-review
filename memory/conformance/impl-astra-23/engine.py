"""Atomic synthetic state transitions. These operations do not perform external effects."""

import copy

from common import Grammar, Refused, cjson, digest, key, receipt, ref, refs, stamp, strict_loads
from evaluator import Evaluation
from disclosure import effective_label, lineage_complete, lineage_inputs, record_grant, release_valid


class Engine:
    def __init__(self, initial_state, grammar, version):
        self.initial = copy.deepcopy(initial_state)
        self.state = copy.deepcopy(initial_state)
        self.grammar, self.version = grammar, version
        self.captures = {}
        self.view_bindings = {}
        self.dirty_since = {key(r): self.state["runtime"]["memory_cut"] for r in self.state["runtime"]["dirty"]}
        for record in self.state["records"]:
            self.validate_self_declaration(record)

    def validate_self_declaration(self, record, admission_class=None):
        e, b = record["envelope"], record["body"]
        bindings = self.state["policy"].get("subject_principals")
        if bindings is None or e["kind"] != "assertion":
            return
        if b["statement_kind"] != "self_declaration" and (admission_class or e.get("admission_class")) != "self_declaration":
            return
        if ({"subject": e["subject"], "principal": e["issuer"]} not in bindings
                or e["perspective"] != {"kind": "own", "principal": e["issuer"]}):
            raise Refused("invalid_domain_value")

    @staticmethod
    def impacts(records):
        edges = []
        for r in records:
            e, b = r["envelope"], r["body"]
            if e["kind"] == "justification" and b["role"] in ("sufficient_support", "review_on_change"):
                inputs = {key(x["source"] if x["kind"] == "source" else x["literal"]["assertion"]) for x in b["premises"]}
                inputs.add(key(r))
                if b["check"]:
                    inputs.add(key(b["check"]))
                edges.append((r, inputs, key(b["target"]["assertion"])))
            elif e["kind"] == "assessment" and b["target"]:
                edges.append((r, {key(r)} | {key(x) for x in b["sources"]}, key(b["target"]["assertion"])))
        return edges

    def index(self):
        return {key(r): r for r in self.state["records"]}

    def disclosure(self, record, query=None):
        return effective_label(self, record, query)

    def read(self, query):
        try:
            evaluation = Evaluation(self, query)
            result = evaluation.run()
            self.view_bindings[result["authorized_snapshot_handle"]] = evaluation.selected_refs
            return result
        except Refused as error:
            return error.response()

    def write_right(self, actor, space, right):
        return any(g["principal"] == actor and (space is None or g["space"] == space)
                   and right in g["rights"] for g in self.state["policy"]["grants"])

    def operation(self, operation, operation_index):
        before, dirty = copy.deepcopy(self.state), copy.deepcopy(self.dirty_since)
        try:
            result = self._operation(copy.deepcopy(operation), operation_index)
            return result
        except Refused as error:
            self.state, self.dirty_since = before, dirty
            return error.response()

    def _operation(self, op, operation_index):
        kind = op["op"]
        p, rt = self.state["policy"], self.state["runtime"]
        if kind == "capture":
            result = self.read(op["query"])
            self.captures[operation_index] = (copy.deepcopy(op["query"]), copy.deepcopy(result))
            return result
        if kind == "request_check":
            raise Refused("execution_required")
        if kind == "admit_raw":
            raw = strict_loads(op.pop("raw_json"))
            if type(raw) is not dict or set(raw) != {"proposals"} or type(raw["proposals"]) is not list:
                raise Refused("invalid_shape")
            op["op"], op["proposals"] = "admit", raw["proposals"]
            kind = "admit"
        if kind in ("admit", "revise", "declassify"):
            return self.admission(op)
        if kind == "control":
            rt["control_observations"] = sorted(set(rt["control_observations"]) | {op["action"] + "_proceeded"})
            return receipt(kind, "proceeded")
        if kind == "load":
            rt["hidden_work"] = op["hidden_work"]
            return receipt(kind, "proceeded")
        if kind == "set_availability":
            if op["actor"] != p["owner"] or p["availability_disclosure"] != "coarse_unavailable":
                raise Refused("not_authorized")
            p["public_availability"] = op["state"]
            return receipt(kind, "availability_changed")
        if kind == "revoke":
            if op["actor"] != p["owner"]:
                raise Refused("not_authorized")
            rt["revocations"].append({k: op[k] for k in ("principal", "audience", "purpose", "right", "at")} | {"owner": op["actor"]})
            return receipt(kind, "revoked")
        if kind == "revoke_declassification":
            decision = next((d for d in p.get("declassification_decisions", []) if d["ref"] == op["decision"]), None)
            if decision is None or decision["owner"] != op["actor"]:
                raise Refused("not_authorized")
            rt["revoked_declassifications"] = refs([*rt["revoked_declassifications"], op["decision"]])
            return receipt(kind, "revoked")
        if kind == "deliver":
            captured = self.captures.get(op["view_operation"])
            if captured is None or captured[1]["type"] != "view":
                raise Refused("not_authorized")
            q, view = copy.deepcopy(captured)
            ev = Evaluation(self, q)
            if ev.rule["family"] != "audience_projection" or op["audience"] != q["audience"] or op["purpose"] != q["purpose"]:
                raise Refused("not_authorized")
            if any(v["principal"] == q["principal"] and v["audience"] == q["audience"]
                   and v["purpose"] == q["purpose"] and v["right"] in ("read", "use", "forward") for v in rt["revocations"]):
                raise Refused("disclosure_revoked")
            selected = self.view_bindings[view["authorized_snapshot_handle"]]
            q["scope"]["targets"] = refs(selected)
            q["cut"]["memory"], q["now"] = rt["memory_cut"], op["at"]
            current = self.read(q)
            if current["type"] != "view" or self.view_bindings.get(current.get("authorized_snapshot_handle")) != selected:
                raise Refused("disclosure_revoked")
            if any(i[s]["freshness"] == "stale" for i in current["items"] for s in ("support", "oppose")) or any(i["currentness"] in ("historical", "last_received") for i in current["items"]):
                raise Refused("publication_stale")
            if [i["content"] for i in current["items"]] != [i["content"] for i in view["items"]]:
                raise Refused("publication_stale")
            ev = Evaluation(self, q)
            for selected_ref in selected:
                record = ev.records.get(selected_ref)
                if record is None or not ev.grant(record, "forward"):
                    raise Refused("disclosure_revoked")
            return receipt(kind, "delivered")
        if kind == "erase":
            if op["actor"] != p["owner"] or not self.write_right(op["actor"], None, "erase"):
                raise Refused("not_authorized")
            replay, identity, request = self.idempotency(op, op["actor"], self.operation_space(op))
            if replay is not None:
                if not all(self.receipt_metadata_authorized(self.index().get(key(r)), op)
                           for r in replay["refs"]):
                    raise Refused("not_authorized")
                return replay
            if any(key(t) not in self.index() for t in op["targets"]):
                raise Refused("invalid_reference")
            closure = self.erasure_closure({key(t) for t in op["targets"]})
            disclosed = {k for k in closure if self.receipt_metadata_authorized(self.index()[k], op)}
            rt["fences"] = refs([*rt["fences"], *closure])
            rt["erased"] = refs([*rt["erased"], *closure])
            rt["erasure_generation"] += 1
            affected = [c for c in rt["custody"] if c["controlled"] and any(key(r) in closure for r in c["inputs"])]
            accounted = []
            for c in affected:
                if c["id"] in op["boundary"] and c["reachable"]:
                    c["present"] = False
                    accounted.append(c["id"])
            complete = all(c["id"] in accounted for c in affected)
            result = receipt(kind, "purged" if complete else "incomplete", disclosed, accounted,
                             "purged_within_boundary" if complete else "purge_pending")
            self.remember(identity, request, result)
            return result
        if kind in ("restore", "reconcile_restore"):
            if op["actor"] != p["owner"]:
                raise Refused("not_authorized")
            if kind == "restore":
                if op["restore_cut"] != self.initial["runtime"]["memory_cut"]:
                    raise Refused("invalid_time")
                initial_custody = {c["id"]: c for c in self.initial["runtime"]["custody"]}
                for c in rt["custody"]:
                    if c["id"] in initial_custody:
                        c["present"] = initial_custody[c["id"]]["present"]
                rt["restore"] = {"status": "fenced", "external_witness": op["external_witness"], "obligations": op["obligations"]}
                return receipt(kind, "fenced", status="access_closed")
            obligations = {key(r) for r in rt["erased"]}
            if not op["external_witness"] or not obligations <= self.erasure_closure({key(r) for r in op["obligations"]}):
                raise Refused("erasure_incomplete")
            closure = self.erasure_closure(obligations)
            affected = [c for c in rt["custody"] if c["controlled"] and any(key(r) in closure for r in c["inputs"])]
            if any(not c["reachable"] for c in affected):
                raise Refused("erasure_incomplete")
            for c in affected:
                c["present"] = False
            rt["restore"] = {"status": "open", "external_witness": True, "obligations": refs(closure)}
            return receipt(kind, "reconciled", custody=[c["id"] for c in affected], status="purged_within_boundary")
        raise Refused("unsupported_operation")

    def receipt_metadata_authorized(self, record, operation):
        if record is None:
            return False
        context = {"principal": operation["actor"], "now": operation["at"],
                   **operation["receipt_context"]}
        label = self.disclosure(record, context)
        return (record_grant(self, record, context, "read")
                and record_grant(self, record, context, "use")
                and context["audience"] in label["audiences"]
                and context["purpose"] in label["purposes"]
                and (label["retain_until"] is None or context["now"] < label["retain_until"]))

    def operation_space(self, op):
        for r in op.get("targets", []):
            if key(r) in self.index():
                return self.index()[key(r)]["envelope"]["space"]
        return ""

    def idempotency(self, op, actor, space):
        intent = copy.deepcopy(op)
        identity = {"actor": actor, "space": space, "key": intent.pop("idempotency_key")}
        if "context" in intent:
            intent["context"].pop("at", None)
        if intent["op"] == "erase":
            intent.pop("at", None)
        request = cjson(intent)
        prior = next((i for i in self.state["runtime"]["idempotency"] if all(i[k] == v for k, v in identity.items())), None)
        if prior:
            if prior["canonical_request"] != request:
                raise Refused("idempotency_conflict")
            return copy.deepcopy(prior["receipt"]), identity, request
        return None, identity, request

    def remember(self, identity, request, result):
        self.state["runtime"]["idempotency"].append({**identity, "canonical_request": request, "receipt": copy.deepcopy(result)})

    def erasure_closure(self, targets):
        closure = set(targets)
        while True:
            before = set(closure)
            for r in self.state["records"]:
                if any(key(x) in closure for x in lineage_inputs(self, r)):
                    closure.add(key(r))
            if closure == before:
                return closure

    def admission(self, op):
        kind, ctx = op["op"], op["context"]
        p, rt = self.state["policy"], self.state["runtime"]
        if kind == "admit":
            proposed = op["proposals"]
        elif kind == "revise":
            proposed = ([op["replacement"]] if op["replacement"] else []) + [op["revision"]]
        else:
            proposed = op.get("assessments", [op.get("assessment")]) + [op["output"]]
        if not proposed:
            raise Refused("invalid_shape")
        for r in proposed:
            record_kind = r.get("envelope", {}).get("kind")
            if record_kind not in ("assertion", "source", "assessment", "justification", "revision"):
                raise Refused("invalid_shape")
            self.grammar.check(r, record_kind, proposal=True)
        if p["profile"] not in ("protected", "embedded", "documentary"):
            raise Refused("unknown_profile")
        space, actor = proposed[0]["envelope"]["space"], ctx["actor"]
        if not self.write_right(actor, space, kind) or (kind == "declassify" and (not self.write_right(actor, space, "admit") or not self.write_right(actor, space, "retain"))):
            raise Refused("not_authorized")
        replay, identity, request = self.idempotency(op, actor, space)
        if replay is not None:
            return replay
        relation = op["revision"]["body"]["relation"] if kind == "revise" else "admit"
        for r in proposed:
            e = r["envelope"]
            representation = e["representation_ref"]
            if actor == e["issuer"]:
                if representation is not None:
                    raise Refused("representation_invalid")
            elif not any(key(g["ref"]) == key(representation) and g["issuer"] == e["issuer"]
                         and g["submitter"] == actor and g["space"] == space and relation in g["relations"] and g["valid"]
                         for g in p["representations"]):
                raise Refused("representation_invalid")
            if not any(key(v["record"]) == key(r) and v["result"] == "allow" for v in p["reviews"]):
                raise Refused("quarantined")
        if "lineage_facts" in p:
            for r in proposed:
                facts = [f for f in p["lineage_facts"] if key(f["output"]) == key(r)]
                if len(facts) != 1:
                    raise Refused("invalid_reference")
                r["envelope"]["lineage"] = copy.deepcopy(facts[0]["inputs"]) if facts[0]["complete"] else "unknown"
        if op["expected_generation"] != rt["erasure_generation"]:
            raise Refused("stale_generation")
        fences = {key(x) for x in rt["fences"] + rt["erased"]}
        if any(key(x) in fences for r in proposed for x in lineage_inputs(self, r)):
            raise Refused("erasure_fenced")
        original = self.index()
        combined = {**original, **{key(r): r for r in proposed}}
        schemas = {key(s): s for s in self.state["domain_schemas"]}
        stamp(ctx["at"])
        for r in proposed:
            e, b = r["envelope"], r["body"]
            if e["space"] != space:
                raise Refused("cross_scope")
            if e["version"] < 1:
                raise Refused("invalid_reference")
            if e["valid"]["kind"] == "known":
                stamp(e["valid"]["from"])
                if e["valid"]["to"] is not None and stamp(e["valid"]["to"]) <= stamp(e["valid"]["from"]):
                    raise Refused("invalid_time")
            if e["confirmed_at"] is not None:
                stamp(e["confirmed_at"])
            dependencies = list(lineage_inputs(self, r))
            if e["kind"] == "assertion":
                self.validate_self_declaration(r, ctx["admission_class"])
                domain = schemas.get(key(e["schema"]))
                if domain is None:
                    raise Refused("unknown_schema")
                fields = {f["name"]: f for f in domain["fields"]}
                content = {x["field"]: x["value"] for x in b["content"]}
                if b["statement_kind"] != domain["statement_kind"] or len(content) != len(b["content"]) or not content.keys() <= fields.keys() or any(f["required"] and f["name"] not in content for f in fields.values()):
                    raise Refused("invalid_domain_value")
                if [x["field"] for x in b["content"]] != sorted(content):
                    raise Refused("invalid_domain_value")
                for name, value in content.items():
                    typ = fields[name]["type"]
                    if type(value) is not {"string": str, "integer": int, "boolean": bool, "string_set": list}[typ]:
                        raise Refused("invalid_domain_value")
                    if typ == "string_set" and (any(type(x) is not str for x in value) or value != sorted(set(value))):
                        raise Refused("invalid_domain_value")
                expected_slot = cjson([content[f] for f in domain["cardinality"]["slot_fields"]]) if domain["cardinality"]["mode"] == "single" else "[]"
                if b["slot"] != expected_slot:
                    raise Refused("invalid_domain_value")
                if ctx["admission_class"] == "semantic_inference" and b["statement_kind"] not in ("proposal", "assessment_summary"):
                    raise Refused("invalid_domain_value")
                if b["authority_receipt"]:
                    dependencies.append(b["authority_receipt"])
            elif e["kind"] == "assessment":
                dependencies += b["sources"] + [b["pins"]["subject"]]
                if b["executor"] == "model" and b["check_kind"] != "semantic_review":
                    raise Refused("assessment_kind_invalid")
                if b["target"]:
                    target = combined.get(key(b["target"]["assertion"]))
                    if target and e["context"] != target["envelope"]["context"]:
                        raise Refused("mode_mismatch")
            elif e["kind"] == "justification":
                dependencies += [b["target"]["assertion"]]
                dependencies += [x["source"] if x["kind"] == "source" else x["literal"]["assertion"] for x in b["premises"]]
                if b["check"]:
                    dependencies.append(b["check"])
            elif e["kind"] == "revision":
                dependencies += [b["target"]] + ([b["replacement"]] if b["replacement"] else [])
            for dependency in dependencies:
                if key(dependency) not in combined:
                    raise Refused("invalid_reference")
                if combined[key(dependency)]["envelope"]["space"] != space:
                    raise Refused("cross_scope")
        if kind == "revise":
            b, e = op["revision"]["body"], op["revision"]["envelope"]
            target = original.get(key(b["target"]))
            if target is None:
                raise Refused("invalid_reference")
            if relation != "challenge":
                if e["issuer"] != target["envelope"]["issuer"]:
                    raise Refused("representation_invalid")
                head = ref(target)
                for r in sorted(original.values(), key=lambda r: r["envelope"]["recorded"]["sequence"]):
                    if r["envelope"]["kind"] == "revision" and r["body"]["relation"] != "challenge" and r["body"]["target"]["id"] == b["target"]["id"]:
                        head = r["body"]["replacement"] or ref(r)
                if op["expected_version"] != head:
                    raise Refused("version_conflict")
                if op["replacement"]:
                    replacement = op["replacement"]
                    if key(replacement) != (b["target"]["id"], b["target"]["version"] + 1):
                        raise Refused("invalid_reference")
                    if any(replacement["envelope"][k] != target["envelope"][k] for k in ("issuer", "subject", "space", "schema", "perspective")):
                        raise Refused("invalid_domain_value")
        for r in proposed:
            if key(r) in original:
                raise Refused("duplicate_record")
            e, b = r["envelope"], r["body"]
            if e["kind"] == "assertion" and b["statement_kind"] == "decision_record":
                if not any(ev["canonical"] and ev["issuer"] == e["issuer"] and ev["receipt"] == b["authority_receipt"] for ev in p["authority_events"]):
                    raise Refused("authority_receipt_required")
        if kind == "declassify":
            if not release_valid(self, op["output"], proposed[:-1]):
                raise Refused("declassification_invalid")
        graph = {}
        for r in combined.values():
            e, b = r["envelope"], r["body"]
            if e["kind"] != "justification" or b["role"] != "sufficient_support":
                continue
            check = combined.get(key(b["check"]))
            if not check or b["rule_kind"] != "checked_entailment" or any(x["kind"] != "assertion" for x in b["premises"]):
                raise Refused("rule_unqualified")
            cb = check["body"]
            if cb["check_kind"] != "formal_entailment" or cb["executor"] != "deterministic" or cb["result"] != "pass" or cb["pins"]["subject"] != ref(r) or cb["pins"]["rule"] != b["rule"] or cb["target"] is not None:
                raise Refused("rule_unqualified")
            graph.setdefault(key(b["target"]["assertion"]), set()).update(key(x["literal"]["assertion"]) for x in b["premises"])
        complete, active = set(), set()
        def acyclic(node):
            if node in active:
                raise Refused("cycle")
            if node in complete:
                return
            active.add(node)
            for premise in graph.get(node, ()):
                acyclic(premise)
            active.remove(node)
            complete.add(node)
        for node in graph:
            acyclic(node)
        limits = p["limits"]
        if (len(combined) > limits["max_records"] or len(cjson(proposed).encode()) > limits["max_payload_bytes"]
                or any(r["envelope"]["kind"] == "justification" and len(r["body"]["premises"]) > limits["max_fan_in"] for r in proposed)):
            raise Refused("limit_exceeded")
        for r in proposed:
            e = r["envelope"]
            rt["memory_cut"] += 1
            e.update(submitter=actor, admission_class=ctx["admission_class"], recorded={"sequence": rt["memory_cut"], "at": ctx["at"]})
            if e["representation_ref"]:
                e["representation_ref"]["checked"] = True
            self.state["records"].append(r)
        rt["committed_cuts"] = sorted(set(rt["committed_cuts"]) | {rt["memory_cut"]})
        if kind == "revise" and relation != "challenge":
            affected, discovered = {key(op["revision"]["body"]["target"])}, set()
            while True:
                prior = set(affected)
                for _, dependencies, conclusion in self.impacts(original.values()):
                    if affected & dependencies:
                        affected.add(conclusion)
                        discovered.add(conclusion)
                if affected == prior:
                    break
            rt["dirty"] = refs([*rt["dirty"], *discovered])
            for r in discovered:
                self.dirty_since[r] = rt["memory_cut"]
            if "dirty_causes" in rt:
                causes = rt["dirty_causes"] + [{"assertion": ref(r), "revision": ref(op["revision"])} for r in discovered]
                rt["dirty_causes"] = [value for _, value in sorted({cjson(c): c for c in causes}.items())]
        outcome = {"admit": "admitted", "revise": "challenged" if relation == "challenge" else "availability_changed" if relation == "availability" else "revised", "declassify": "declassified"}[kind]
        result = receipt(kind, outcome, proposed)
        self.remember(identity, request, result)
        return result

    def execute(self, operations, query):
        results = [self.operation(op, i) for i, op in enumerate(operations)]
        result = self.read(query)
        rt = self.state["runtime"]
        return {"operation_results": results, "result": result, "postconditions": {
            "record_refs": refs(self.state["records"]), "erased_refs": refs(rt["erased"]),
            "custody_present": sorted(c["id"] for c in rt["custody"] if c["present"]),
            "dirty": refs(rt["dirty"]), "control_observations": sorted(rt["control_observations"]),
            "external_effects": sorted(rt["external_effects"])}}
