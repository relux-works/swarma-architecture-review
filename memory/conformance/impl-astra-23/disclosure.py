"""Package disclosure and owner-release rules, including the 0.2 grammar."""

import copy

from common import digest, key, ref, refs


def record_grant(engine, record, context, right, metadata=True):
    e = record["envelope"]
    if any(v["principal"] == context["principal"] and v["audience"] == context["audience"]
           and v["purpose"] == context["purpose"] and v["right"] == right
           for v in engine.state["runtime"]["revocations"]):
        return False
    return any(g["principal"] == context["principal"] and g["space"] == e["space"]
               and g["audience"] == context["audience"] and g["purpose"] == context["purpose"]
               and right in g["rights"] and ("*" in g["records"] or e["id"] in g["records"])
               and (not metadata or g["metadata"]) for g in engine.state["policy"]["grants"])


def lineage_inputs(engine, record):
    lineage = record["envelope"]["lineage"]
    if isinstance(lineage, list):
        return lineage
    fact = next((f for f in engine.state["policy"].get("lineage_facts", []) if key(f["output"]) == key(record)), None)
    return fact["inputs"] if fact else []


def closure(engine, record, seen=None):
    seen = set() if seen is None else set(seen)
    if key(record) in seen:
        return []
    seen.add(key(record))
    records = engine.index()
    result = [record]
    for source in lineage_inputs(engine, record):
        if key(source) in records:
            result += closure(engine, records[key(source)], seen)
    return list({key(r): r for r in result}.values())


def lineage_complete(engine, record):
    return all(r["envelope"]["lineage"] != "unknown" for r in closure(engine, record))


def own_label(engine, record):
    e = record["envelope"]
    label = copy.deepcopy(e["disclosure"])
    domain = next((s for s in engine.state["domain_schemas"] if key(s) == key(e["schema"])), None)
    if domain:
        for field in domain["fields"]:
            defaults = next(d for d in domain["disclosure_defaults"] if d["field_class"] == field["disclosure_class"])
            for dimension in ("audiences", "purposes"):
                label[dimension] = sorted(set(label[dimension]) & set(defaults[dimension]))
            label["field_classes"] = sorted(set(label["field_classes"]) | {field["disclosure_class"]})
    return label


def release_refs(record):
    value = record["envelope"]["disclosure"]["declassification"]
    return value if isinstance(value, list) else [value] if value else []


def release_valid(engine, output, assessments=None, query=None):
    policy, runtime = engine.state["policy"], engine.state["runtime"]
    records = engine.index()
    named = release_refs(output)
    assessments = assessments if assessments is not None else [records.get(key(r)) for r in named]
    if not assessments or any(a is None for a in assessments) or not lineage_complete(engine, output):
        return False
    if refs(assessments) != named:
        return False
    oe = output["envelope"]
    provided, pins = set(), None
    for a in assessments:
        ae, b = a["envelope"], a["body"]
        pin = b.get("declassification")
        if (not pin or b["check_kind"] != "declassification" or b["result"] != "pass"
                or b["executor"] not in ("human", "deterministic") or b["pins"]["subject"] != ref(output)
                or b["pins"]["policy"] != policy["evidence"]["policy_pin"]
                or b["pins"]["environment"] != policy["evidence"]["environment_pin"]
                or pin["inputs"] != oe["lineage"] or pin["output_schema"] != oe["schema"]
                or pin["output_digest"] != digest(output["body"])):
            return False
        common_pin = {k: v for k, v in pin.items() if k != "decision"}
        if pins is not None and pins != common_pin:
            return False
        pins = common_pin
        if query and (query["audience"] != pin["audience"] or query["purpose"] != pin["purpose"]
                      or (b["usable_until"] is not None and query["now"] >= b["usable_until"])):
            return False
        if "decision" in pin:
            decision = next((d for d in policy.get("declassification_decisions", []) if d["ref"] == pin["decision"]), None)
            if (decision is None or decision["owner"] != ae["issuer"] or decision["pins"] != common_pin
                    or not decision["active"] or pin["decision"] in runtime.get("revoked_declassifications", [])):
                return False
        elif ae["issuer"] != policy["owner"]:
            return False
        provided.add(ae["issuer"])
    needed = set()
    for r in closure(engine, output):
        label = own_label(engine, r)
        if (pins["audience"] not in label["audiences"] or pins["purpose"] not in label["purposes"]
                or not set(label["field_classes"]) <= set(oe["disclosure"]["field_classes"])):
            owners = next((entry["owners"] for entry in policy.get("constraint_owners", []) if key(entry["input"]) == key(r)), [policy["owner"]])
            needed.update(owners)
    return needed <= provided


def effective_label(engine, record, query=None, seen=None):
    seen = set() if seen is None else set(seen)
    out = own_label(engine, record)
    if key(record) in seen:
        out["audiences"], out["purposes"] = [], []
        return out
    seen.add(key(record))
    records = engine.index()
    for source in lineage_inputs(engine, record):
        if key(source) not in records:
            out["audiences"], out["purposes"] = [], []
            continue
        label = effective_label(engine, records[key(source)], query, seen)
        for part in ("audiences", "purposes"):
            out[part] = sorted(set(out[part]) & set(label[part]))
        out["field_classes"] = sorted(set(out["field_classes"]) | set(label["field_classes"]))
        deadlines = [d for d in (out["retain_until"], label["retain_until"]) if d is not None]
        out["retain_until"] = min(deadlines) if deadlines else None
    if query and release_valid(engine, record, query=query):
        out["audiences"] = sorted(set(out["audiences"]) | {query["audience"]})
        out["purposes"] = sorted(set(out["purposes"]) | {query["purpose"]})
    return out
