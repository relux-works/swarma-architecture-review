#!/usr/bin/env python3
"""Run every package vector and persist exact, independently computed results."""

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

from adapter import Adapter, Unsupported
from evaluator import field_differences, strict_json


BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
MISSING = object()


def pointer(obj, path):
    current = obj
    try:
        for part in path.split("/")[1:]:
            part = part.replace("~1", "/").replace("~0", "~")
            current = current[int(part)] if isinstance(current, list) else current[part]
    except (KeyError, IndexError, ValueError, TypeError):
        return MISSING
    return current


def assign(obj, path, value):
    prefix, last = path.rsplit("/", 1)
    parent = pointer(obj, prefix)
    if parent is MISSING:
        return
    last = last.replace("~1", "/").replace("~0", "~")
    if isinstance(parent, list):
        parent[int(last)] = value
    else:
        parent[last] = value


def compare(actual, expected, normalization, forbidden):
    errors = []
    normalized = copy.deepcopy(actual)
    expected = copy.deepcopy(expected)
    for path in normalization["fresh_handles"]:
        value = pointer(actual, path)
        if value is MISSING:
            continue  # The exact structural diff below records missing fields.
        if not isinstance(value, str) or re.fullmatch("[0-9a-f]{32}", value) is None:
            errors.append({"path": path, "expected": "fresh 32-character lowercase hex handle", "actual": value})
        assign(normalized, path, "<fresh>")
        if pointer(expected, path) is not MISSING:
            assign(expected, path, "<fresh>")
    for kind in ("equal_handles", "distinct_handles"):
        for group in normalization[kind]:
            values = [pointer(actual, p) for p in group]
            if MISSING in values:
                continue
            valid = len(set(values)) == (1 if kind == "equal_handles" else len(values))
            if not valid:
                errors.append({"path": "normalization." + kind, "expected": group, "actual": values})
    errors.extend(field_differences(expected, normalized))
    for pair in normalization["equivalent_outputs"]:
        left, right = pointer(normalized, pair["left"]), pointer(normalized, pair["right"])
        if left is MISSING or right is MISSING:
            errors.append({"path": "normalization.equivalent_outputs", "expected": pair, "actual": "missing pair endpoint"})
        else:
            errors.extend(field_differences(left, right, "pair:" + pair["left"] + "=" + pair["right"]))
    for predicate in forbidden:
        value = pointer(actual, predicate["path"])
        if value is MISSING:
            continue
        test = predicate["test"]
        matches = (test == "exists" or
                   test == "equals" and type(value) is type(predicate["value"]) and value == predicate["value"] or
                   test == "contains" and isinstance(value, list) and any(type(v) is type(predicate["value"]) and v == predicate["value"] for v in value) or
                   test == "size_equals" and isinstance(value, list) and len(value) == predicate["value"])
        if matches:
            errors.append({"path": "forbidden:" + predicate["path"], "expected": "predicate false", "actual": predicate})
    return normalized, errors


def controls():
    # Controls prove that the harness detects semantic changes, extra fields,
    # forbidden values and handle-reuse violations without rejecting a valid pair.
    norm = {"fresh_handles": ["/h", "/h2"], "equal_handles": [],
            "distinct_handles": [["/h", "/h2"]], "equivalent_outputs": []}
    expected = {"h": "one", "h2": "two", "value": 1}
    good = {"h": "a" * 32, "h2": "b" * 32, "value": 1}
    assert not compare(good, expected, norm, [])[1]
    assert any(e["path"] == "$.value" for e in compare(good | {"value": 2}, expected, norm, [])[1])
    assert any(e["path"] == "$.extra" for e in compare(good | {"extra": True}, expected, norm, [])[1])
    assert any(e["path"] == "normalization.distinct_handles" for e in compare(good | {"h2": good["h"]}, expected, norm, [])[1])
    assert any(e["path"] == "forbidden:/value" for e in compare(good, expected, norm, [{"path": "/value", "test": "equals", "value": 1}])[1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", type=Path, default=ROOT / "memory/spec")
    parser.add_argument("--out", type=Path, default=BASE / "RESULTS.md")
    args = parser.parse_args()
    controls()
    package = args.package.resolve()
    profile = json.loads((package / "kernel/schemas/view.schema.json").read_text())["properties"]["semantic_profile"]["const"]
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    package_commit = subprocess.check_output(["git", "log", "-1", "--format=%H", "--", str(package)], cwd=ROOT, text=True).strip()
    core_hash = hashlib.sha256((BASE / "evaluator.py").read_bytes()).hexdigest()
    rows, details = [], {}
    totals = {p: {s: 0 for s in ("pass", "fail", "unsupported")} for p in ("semantic", "deployment")}
    for path in sorted((package / "kernel/vectors").rglob("*.json")):
        vector = strict_json(path.read_text())
        category = vector["profile"]
        identifier = vector["id"]
        record = {"file": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        if category == "deployment":
            status, reason = "unsupported", "No protected deployment; a semantic simulator cannot qualify this boundary."
        else:
            try:
                # Deliberately do not give the executor expected answers or IDs.
                actual = Adapter(vector["initial_state"], profile).execute(vector["operations"], vector["query"])
                normalized, differences = compare(actual, vector["expected"], vector["normalization"], vector["forbidden"])
                record.update(actual=normalized, differences=differences)
                status = "fail" if differences else "pass"
                reason = f"{len(differences)} exact differences" if differences else "Exact report and forbidden/normalization checks passed."
            except Unsupported as error:
                status, reason = "unsupported", str(error)
            except Exception as error:
                status, reason = "fail", f"Execution error: {type(error).__name__}: {error}"
        record.update(status=status, reason=reason)
        details[identifier] = record
        totals[category][status] += 1
        rows.append(f"| {identifier} | {category} | {status} | {reason} |")
    report = {"checkout_commit": head, "package_commit": package_commit, "package_version": profile,
              "core_sha256": core_hash, "totals": totals, "vectors": details}
    json_out = args.out.with_suffix(".json")
    json_out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    lines = ["# astra-22 vector results", "", f"Package: **{profile}**, package commit `{package_commit}`.",
             f"Checkout: `{head}`. Source core SHA-256: `{core_hash}`.", "",
             "The core is the source-only frozen implementation. The adapter is an independent wire mapping.",
             "Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.",
             "Deployment cases require actual boundary qualification and are reported separately.", "",
             "| Category | Pass | Fail | Unsupported |", "| --- | ---: | ---: | ---: |"]
    for category, counts in totals.items():
        lines.append(f"| {category} | {counts['pass']} | {counts['fail']} | {counts['unsupported']} |")
    lines += ["", "Five bounded harness controls passed (valid comparison, changed value, extra field,",
              "handle reuse, forbidden predicate). Only declared handle paths are normalized;",
              "handle length, equality, distinctness and paired-output invariants are checked.",
              "No randomness-distribution or timing proof is claimed.", "", "| Vector | Category | Result | Evidence / reason |", "| --- | --- | --- | --- |"] + rows
    for identifier, detail in details.items():
        if detail["status"] != "fail":
            continue
        lines += ["", f"## {identifier}", "", detail["reason"], ""]
        for difference in detail.get("differences", []):
            lines += [f"- `{difference['path']}`: expected `{json.dumps(difference['expected'],ensure_ascii=False)}`; actual `{json.dumps(difference['actual'],ensure_ascii=False)}`."]
    lines += ["", f"Full normalized actual reports and input hashes: `{json_out.name}`.", ""]
    args.out.write_text("\n".join(lines))
    print(json.dumps({"package": profile, "commit": package_commit, "core_sha256": core_hash, "totals": totals}, indent=2))
    return 1 if any(t["fail"] for t in totals.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
