"""Independent atomic admission mapping; no package evaluator code is imported."""

import copy
import datetime
import json
from pathlib import Path
import re
import secrets

from evaluator import Refusal, canonical, strict_json


def key(reference):
    return json.dumps([reference["id"], reference["version"]], separators=(",", ":"))


def ref(record):
    e = record["envelope"]
    return {"id": e["id"], "version": e["version"]}


def receipt(operation, outcome, references=()):
    return {"type": "receipt", "operation": operation, "outcome": outcome,
            "receipt_handle": secrets.token_hex(16),
            "refs": sorted(references, key=lambda r: (r["id"], r["version"])),
            "custody": [], "erasure_status": None}


class Shapes:
    """The finite JSON Schema vocabulary actually used by this package."""

    def __init__(self, root):
        self.schemas = {}
        for path in root.glob("*.schema.json"):
            schema = json.loads(path.read_text())
            self.schemas[schema["$id"]] = schema
        self.vector = next(s for k, s in self.schemas.items() if k.endswith(":vector"))

    def valid(self, value, schema):
        if "$ref" in schema:
            if schema["$ref"] not in self.schemas:
                raise Refusal("invalid_shape")
            return self.valid(value, self.schemas[schema["$ref"]])
        if "oneOf" in schema and sum(self.valid(value, s) for s in schema["oneOf"]) != 1:
            return False
        if "anyOf" in schema and not any(self.valid(value, s) for s in schema["anyOf"]):
            return False
        if "allOf" in schema and not all(self.valid(value, s) for s in schema["allOf"]):
            return False
        types = {"object": dict, "array": list, "string": str, "integer": int, "boolean": bool, "null": type(None)}
        if "type" in schema and type(value) is not types[schema["type"]]:
            return False
        if "const" in schema and (type(value) is not type(schema["const"]) or value != schema["const"]):
            return False
        if "enum" in schema and not any(type(value) is type(v) and value == v for v in schema["enum"]):
            return False
        if isinstance(value, dict):
            props = schema.get("properties", {})
            if any(k not in value for k in schema.get("required", [])):
                return False
            if schema.get("additionalProperties") is False and any(k not in props for k in value):
                return False
            if any(k in props and not self.valid(v, props[k]) for k, v in value.items()):
                return False
        if isinstance(value, list):
            if len(value) < schema.get("minItems", 0) or len(value) > schema.get("maxItems", float("inf")):
                return False
            if "items" in schema and not all(self.valid(v, schema["items"]) for v in value):
                return False
            if schema.get("uniqueItems") and len({canonical(v) for v in value}) != len(value):
                return False
        if type(value) is int and not schema.get("minimum", -float("inf")) <= value <= schema.get("maximum", float("inf")):
            return False
        if isinstance(value, str) and "pattern" in schema and not re.search(schema["pattern"], value):
            return False
        return True


def json_values(value):
    if type(value) is float or type(value) is int and abs(value) > 9007199254740991:
        raise Refusal("invalid_json")
    if isinstance(value, str) and any(0xD800 <= ord(c) <= 0xDFFF for c in value):
        raise Refusal("invalid_json")
    if isinstance(value, dict):
        for k, v in value.items():
            json_values(k)
            json_values(v)
    if isinstance(value, list):
        for v in value:
            json_values(v)


def timestamp(value):
    if value is None:
        return
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", value):
        raise Refusal("invalid_time")
    try:
        datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        raise Refusal("invalid_time") from None


class Transactions:
    def __init__(self, adapter, schema_root=None):
        self.adapter = adapter
        root = schema_root or Path(__file__).resolve().parents[2] / "spec/kernel/schemas"
        self.shapes = Shapes(root)

    @property
    def idempotency(self):
        # A derived lookup, never a second store: initial snapshots and newly
        # committed receipts follow exactly the same replay path.
        return {(entry["actor"], entry["space"], entry["key"]):
                (entry["canonical_request"].encode("utf-8"), entry["receipt"])
                for entry in self.adapter.runtime["idempotency"]}

    def sequence(self, record):
        e, b = record["envelope"], record["body"]
        result = [e["issuer"], e["subject"], e["space"], e["schema"], e["perspective"], b.get("slot")]
        if e["kind"] == "assertion" and self.adapter.schemas[key(e["schema"])]["cardinality"]["mode"] == "multi":
            result.append(e["id"])
        return canonical(result)

    def head(self, target, state):
        if target["body"].get("statement_kind") == "decision_record":
            sequence = self.sequence(target)
            events = {key(e["receipt"]): e for e in self.adapter.policy["authority_events"]
                      if e["canonical"] and e["issuer"] == target["envelope"]["issuer"]}
            candidates = [r for r in state.values() if r["envelope"]["kind"] == "assertion"
                          and r["body"]["statement_kind"] == "decision_record" and self.sequence(r) == sequence
                          and r["body"]["authority_receipt"] is not None
                          and key(r["body"]["authority_receipt"]) in events]
            old = set()
            for candidate in candidates:
                frontier = list(events[key(candidate["body"]["authority_receipt"])]["predecessors"])
                seen = set()
                while frontier:
                    parent = key(frontier.pop())
                    if parent in seen:
                        continue
                    seen.add(parent)
                    old.add(parent)
                    if parent in events:
                        frontier.extend(events[parent]["predecessors"])
            heads = [r for r in candidates if key(r["body"]["authority_receipt"]) not in old]
            if len(heads) != 1:
                return None
            # Local transitions advance this unique authority head's CAS token;
            # a historical candidate's transition cannot replace that selection.
            target = heads[0]
        token = ref(target)
        for record in sorted(state.values(), key=lambda r: r["envelope"]["recorded"]["sequence"]):
            if record["envelope"]["kind"] != "revision":
                continue
            body = record["body"]
            if body["relation"] != "challenge" and (body["target"] == token or body["target"] == ref(target)):
                token = body["replacement"] or ref(record)
        return token

    def apply(self, operation):
        op = copy.deepcopy(operation)
        if op["op"] == "admit_raw":
            try:
                raw = strict_json(op.pop("raw_json"))
            except (ValueError, Refusal):
                raise Refusal("invalid_json") from None
            if not isinstance(raw, dict) or set(raw) != {"proposals"}:
                raise Refusal("invalid_shape")
            op.update(op="admit", proposals=raw["proposals"])
        json_values(op)
        if not self.shapes.valid(op, self.shapes.vector["properties"]["operations"]["items"]):
            raise Refusal("invalid_shape")
        mode = op["op"]
        proposals = op["proposals"] if mode == "admit" else ([op["replacement"]] if op["replacement"] else []) + [op["revision"]]
        policy, runtime = self.adapter.policy, self.adapter.runtime
        actor, at = op["context"]["actor"], op["context"]["at"]
        spaces = {p["envelope"]["space"] for p in proposals}
        if len(spaces) != 1:
            raise Refusal("cross_scope")
        space = next(iter(spaces))
        if not any(g["principal"] == actor and g["space"] == space and mode in g["rights"] for g in policy["grants"]):
            raise Refusal("not_authorized")
        identity = (actor, space, op["idempotency_key"])
        intent = copy.deepcopy(op)
        intent.pop("idempotency_key")
        intent["context"].pop("at")
        digest = canonical(intent)
        if identity in self.idempotency:
            old_digest, old_receipt = self.idempotency[identity]
            if old_digest != digest:
                raise Refusal("idempotency_conflict")
            return copy.deepcopy(old_receipt)
        relation = op["revision"]["body"]["relation"] if mode == "revise" else "admit"
        for proposal in proposals:
            e = proposal["envelope"]
            representation = e["representation_ref"]
            if e["issuer"] != actor:
                if not any(f["ref"] == representation and f["issuer"] == e["issuer"] and f["submitter"] == actor
                           and f["space"] == space and relation in f["relations"] and f["valid"]
                           for f in policy["representations"]):
                    raise Refusal("representation_invalid")
            elif representation is not None:
                raise Refusal("representation_invalid")
            if not any(f["record"] == ref(proposal) and f["result"] == "allow" for f in policy["reviews"]):
                raise Refusal("quarantined")
        if op["expected_generation"] != runtime["erasure_generation"]:
            raise Refusal("stale_generation")
        state = copy.deepcopy(self.adapter.records)
        proposed = {key(ref(p)): p for p in proposals}
        if len(proposed) != len(proposals):
            raise Refusal("duplicate_record")
        future = state | proposed
        erased = {key(r) for r in runtime["erased"]}
        timestamp(at)
        for proposal in proposals:
            e, b = proposal["envelope"], proposal["body"]
            facts = [f for f in policy.get("lineage_facts", []) if f["output"] == ref(proposal)]
            if "lineage_facts" in policy:
                if len(facts) != 1:
                    raise Refusal("invalid_reference")
                inputs = facts[0]["inputs"]
                e["lineage"] = copy.deepcopy(inputs) if facts[0]["complete"] else "unknown"
            else:
                inputs = e["lineage"] if e["lineage"] != "unknown" else []
            for source in inputs:
                if key(source) in erased:
                    raise Refusal("erasure_fenced")
                if key(source) not in future:
                    raise Refusal("invalid_reference")
            self.inherit(proposal, inputs, future)
            timestamp(e["confirmed_at"])
            validity = e["valid"]
            if validity["kind"] == "known":
                timestamp(validity["from"])
                timestamp(validity["to"])
                if validity["to"] is not None and validity["from"] >= validity["to"]:
                    raise Refusal("invalid_time")
            if e["perspective"]["kind"] in ("own", "observer") and e["perspective"]["principal"] != e["issuer"]:
                raise Refusal("invalid_domain_value")
            if e["kind"] == "assertion":
                self.assertion(proposal)
                if b["statement_kind"] == "self_declaration" or op["context"]["admission_class"] == "self_declaration":
                    bound = any(f["subject"] == e["subject"] and f["principal"] == e["issuer"]
                                for f in policy.get("subject_principals", []))
                    if not bound or e["perspective"] != {"kind": "own", "principal": e["issuer"]}:
                        raise Refusal("invalid_domain_value")
                if op["context"]["admission_class"] == "semantic_inference" and b["statement_kind"] not in ("proposal", "assessment_summary"):
                    raise Refusal("assessment_kind_invalid")
            if e["kind"] == "assessment":
                if (b["executor"] == "model" or op["context"]["admission_class"] == "semantic_inference") and b["check_kind"] != "semantic_review":
                    raise Refusal("assessment_kind_invalid")
                if key(b["pins"]["subject"]) not in future:
                    raise Refusal("invalid_reference")
                for source in b["sources"]:
                    if key(source) not in future or future[key(source)]["envelope"]["kind"] != "source":
                        raise Refusal("invalid_reference")
            if e["kind"] == "justification":
                if key(b["target"]["assertion"]) not in future:
                    raise Refusal("invalid_reference")
                for premise in b["premises"]:
                    source = premise["source"] if premise["kind"] == "source" else premise["literal"]["assertion"]
                    if key(source) not in future:
                        raise Refusal("invalid_reference")
                    if future[key(source)]["envelope"]["space"] != e["space"]:
                        raise Refusal("cross_scope")
        if mode == "revise":
            revision = op["revision"]
            body = revision["body"]
            if key(body["target"]) not in state:
                raise Refusal("invalid_reference")
            target = state[key(body["target"])]
            if relation != "challenge":
                if revision["envelope"]["issuer"] != target["envelope"]["issuer"]:
                    raise Refusal("not_authorized")
                if op["expected_version"] != self.head(target, state):
                    raise Refusal("version_conflict")
            replacement = op["replacement"]
            if replacement:
                if (body["replacement"] != ref(replacement) or self.sequence(replacement) != self.sequence(target)
                        or replacement["envelope"]["id"] != target["envelope"]["id"]
                        or replacement["envelope"]["version"] != target["envelope"]["version"] + 1):
                    raise Refusal("invalid_domain_value")
        if any(k in state for k in proposed):
            raise Refusal("duplicate_record")
        for proposal in proposals:
            e, b = proposal["envelope"], proposal["body"]
            if e["kind"] == "assertion" and b["statement_kind"] == "decision_record":
                self.authority(proposal, future)
            if mode == "admit" and e["kind"] == "assertion" and b["statement_kind"] != "decision_record":
                schema = self.adapter.schemas[key(e["schema"])]
                if schema["cardinality"]["mode"] == "single" and any(
                        r["envelope"]["kind"] == "assertion" and self.sequence(r) == self.sequence(proposal)
                        and self.head(r, state) == ref(r) for r in state.values()):
                    raise Refusal("version_conflict")
        self.graph(future)
        limits = policy["limits"]
        if len(future) > limits["max_records"] or len(canonical(proposals)) > limits["max_payload_bytes"]:
            raise Refusal("limit_exceeded")
        if any(p["envelope"]["kind"] == "justification" and len(p["body"]["premises"]) > limits["max_fan_in"] for p in proposals):
            raise Refusal("limit_exceeded")
        # All checks above operate on copies. Only this final block commits.
        sequence = runtime["memory_cut"]
        for proposal in proposals:
            sequence += 1
            e = proposal["envelope"]
            e.update(submitter=actor, admission_class=op["context"]["admission_class"], recorded={"sequence": sequence, "at": at})
            if e["representation_ref"]:
                e["representation_ref"]["checked"] = True
            state[key(ref(proposal))] = proposal
        self.adapter.records = state
        runtime["memory_cut"] = sequence
        runtime["committed_cuts"] = sorted(set(runtime["committed_cuts"] + [sequence]))
        if mode == "revise" and relation != "challenge":
            self.mark_dirty(op["revision"], state)
        result = receipt(mode, "admitted" if mode == "admit" else
                         "challenged" if relation == "challenge" else
                         "availability_changed" if relation == "availability" else "revised",
                         [ref(p) for p in proposals])
        runtime["idempotency"].append({"actor": actor, "space": space,
                                       "key": op["idempotency_key"],
                                       "canonical_request": digest.decode("utf-8"),
                                       "receipt": copy.deepcopy(result)})
        return result

    def inherit(self, proposal, inputs, state):
        disclosure = proposal["envelope"]["disclosure"]
        seen = set()

        def inherit_one(reference):
            k = key(reference)
            if k in seen:
                return
            seen.add(k)
            source = state[k]["envelope"]
            other = source["disclosure"]
            for dimension in ("audiences", "purposes"):
                disclosure[dimension] = sorted(set(disclosure[dimension]) & set(other[dimension]))
            disclosure["field_classes"] = sorted(set(disclosure["field_classes"]) | set(other["field_classes"]))
            dates = [d for d in (disclosure["retain_until"], other["retain_until"]) if d is not None]
            disclosure["retain_until"] = min(dates) if dates else None
            lineage = source["lineage"]
            if lineage == "unknown":
                facts = [f for f in self.adapter.policy.get("lineage_facts", []) if f["output"] == reference]
                lineage = facts[0]["inputs"] if facts else []
            for parent in lineage:
                if key(parent) not in state:
                    raise Refusal("invalid_reference")
                inherit_one(parent)
        for reference in inputs:
            inherit_one(reference)

    def assertion(self, proposal):
        e, b = proposal["envelope"], proposal["body"]
        if key(e["schema"]) not in self.adapter.schemas:
            raise Refusal("unknown_schema")
        schema = self.adapter.schemas[key(e["schema"])]
        if b["statement_kind"] != schema["statement_kind"]:
            raise Refusal("invalid_domain_value")
        fields = {f["name"]: f for f in schema["fields"]}
        values = {f["field"]: f["value"] for f in b["content"]}
        if len(values) != len(b["content"]) or any(k not in fields for k in values) or any(f["required"] and name not in values for name, f in fields.items()):
            raise Refusal("invalid_domain_value")
        types = {"string": str, "integer": int, "boolean": bool, "string_set": list}
        for name, value in values.items():
            if type(value) is not types[fields[name]["type"]]:
                raise Refusal("invalid_domain_value")
            if isinstance(value, list) and (not all(isinstance(v, str) for v in value) or value != sorted(set(value))):
                raise Refusal("invalid_domain_value")
        slots = schema["cardinality"]["slot_fields"] if schema["cardinality"]["mode"] == "single" else []
        if b["slot"] != canonical([values[name] for name in slots]).decode():
            raise Refusal("invalid_domain_value")
        disclosure = e["disclosure"]
        defaults = {d["field_class"]: d for d in schema["disclosure_defaults"]}
        classes = {fields[name]["disclosure_class"] for name in values}
        disclosure["field_classes"] = sorted(set(disclosure["field_classes"]) | classes)
        for cls in classes:
            if cls in defaults:
                for dimension in ("audiences", "purposes"):
                    disclosure[dimension] = sorted(set(disclosure[dimension]) & set(defaults[cls][dimension]))

    def authority(self, proposal, state):
        e, b = proposal["envelope"], proposal["body"]
        citation = b["authority_receipt"]
        if citation is None or key(citation) not in state or not any(
                a["receipt"] == citation and a["issuer"] == e["issuer"] and a["canonical"]
                for a in self.adapter.policy["authority_events"]):
            raise Refusal("authority_receipt_required")

    def graph(self, state):
        edges = {}
        for record in state.values():
            if record["envelope"]["kind"] != "justification":
                continue
            e, b = record["envelope"], record["body"]
            if b["role"] != "sufficient_support":
                if b["rule_kind"] != "declared_rationale" or b["check"] is not None:
                    raise Refusal("rule_unqualified")
                continue
            if b["rule_kind"] != "checked_entailment" or b["check"] is None or key(b["check"]) not in state:
                raise Refusal("rule_unqualified")
            cert = state[key(b["check"])]
            cb = cert["body"]
            evidence = self.adapter.policy["evidence"]
            if (cert["envelope"]["kind"] != "assessment" or cb["check_kind"] != "formal_entailment"
                    or cb["executor"] != "deterministic" or cb["result"] != "pass" or cb["target"] is not None
                    or cb["pins"]["subject"] != ref(record) or cb["pins"]["rule"] != b["rule"]
                    or cb["pins"]["policy"] != evidence["policy_pin"] or cb["pins"]["environment"] != evidence["environment_pin"]):
                raise Refusal("rule_unqualified")
            if cert["envelope"]["context"] != e["context"]:
                raise Refusal("mode_mismatch")
            target = key(b["target"]["assertion"])
            for premise in b["premises"]:
                if premise["kind"] != "assertion":
                    raise Refusal("rule_unqualified")
                edges.setdefault(target, set()).add(key(premise["literal"]["assertion"]))
        active, done = set(), set()

        def visit(k):
            if k in active:
                raise Refusal("cycle")
            if k in done:
                return
            active.add(k)
            for parent in edges.get(k, set()):
                visit(parent)
            active.remove(k)
            done.add(k)
        for k in edges:
            visit(k)

    def mark_dirty(self, revision, state):
        from impact import global_dependents
        affected = global_dependents(state, revision)
        dirty = {key(r) for r in self.adapter.runtime["dirty"]}
        dirty.update(affected)
        self.adapter.runtime["dirty"] = sorted([ref(state[k]) for k in dirty], key=lambda r: (r["id"], r["version"]))
        causes = self.adapter.runtime["dirty_causes"]
        for k in sorted(affected):
            cause = {"assertion": ref(state[k]), "revision": ref(revision)}
            if cause not in causes:
                causes.append(cause)
        causes.sort(key=lambda c: (c["assertion"]["id"], c["assertion"]["version"],
                                   c["revision"]["id"], c["revision"]["version"]))
