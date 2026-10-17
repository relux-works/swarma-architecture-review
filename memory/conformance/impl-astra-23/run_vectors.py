#!/usr/bin/env python3
"""Run every packaged vector without passing expected output to the evaluator."""

import argparse
import copy
import hashlib
import json
import pathlib
import re
import subprocess
import traceback

from common import Grammar, cjson, strict_loads
from engine import Engine

HERE = pathlib.Path(__file__).resolve().parent
MISSING = object()


def pointer(document, path):
    value = document
    try:
        for part in path.split("/")[1:]:
            part = part.replace("~1", "/").replace("~0", "~")
            value = value[int(part)] if isinstance(value, list) else value[part]
        return value
    except (KeyError, IndexError, TypeError, ValueError):
        return MISSING


def put(document, path, value):
    parent, _, last = path.rpartition("/")
    target = pointer(document, parent)
    if target is MISSING:
        return
    last = last.replace("~1", "/").replace("~0", "~")
    if isinstance(target, list):
        if int(last) < len(target):
            target[int(last)] = value
    elif last in target:
        target[last] = value


def typed_equal(a, b):
    return cjson(a) == cjson(b)


def differences(actual, expected, path=""):
    if type(actual) is not type(expected):
        return [(path or "/", actual, expected)]
    out = []
    if isinstance(expected, dict):
        for name in sorted(actual.keys() | expected.keys()):
            child = path + "/" + name.replace("~", "~0").replace("/", "~1")
            if name not in actual or name not in expected:
                out.append((child, actual.get(name, "<missing>"), expected.get(name, "<missing>")))
            else:
                out.extend(differences(actual[name], expected[name], child))
    elif isinstance(expected, list):
        if len(actual) != len(expected):
            out.append((path + "/length", len(actual), len(expected)))
        for i, (a, e) in enumerate(zip(actual, expected)):
            out.extend(differences(a, e, f"{path}/{i}"))
        for i in range(min(len(actual), len(expected)), max(len(actual), len(expected))):
            out.append((f"{path}/{i}", actual[i] if i < len(actual) else "<missing>", expected[i] if i < len(expected) else "<missing>"))
    elif actual != expected:
        out.append((path or "/", actual, expected))
    return out


def forbidden_matches(report, predicate):
    value = pointer(report, predicate["path"])
    if value is MISSING:
        return False
    test = predicate["test"]
    if test == "exists":
        return True
    if test == "equals":
        return typed_equal(value, predicate["value"])
    if test == "contains":
        return isinstance(value, list) and any(typed_equal(v, predicate["value"]) for v in value)
    if test == "size_equals":
        return isinstance(value, list) and len(value) == predicate["value"]
    raise ValueError("Unknown forbidden predicate: " + test)


def compare(report, vector, grammar=None):
    actual, expected = copy.deepcopy(report), copy.deepcopy(vector["expected"])
    norm = vector["normalization"]
    checks = []
    for path in norm["fresh_handles"]:
        value = pointer(report, path)
        if value is MISSING:
            checks.append(f"handle slot missing: {path}")
        elif not isinstance(value, str) or not re.fullmatch("[0-9a-f]{32}", value):
            checks.append(f"handle is not 128-bit lowercase hex: {path}")
        put(actual, path, "<fresh-handle>")
        put(expected, path, "<fresh-handle>")
    for category in ("equal_handles", "distinct_handles"):
        for group in norm[category]:
            values = [pointer(report, path) for path in group]
            valid = (all(v is not MISSING for v in values)
                     and (len(set(values)) == 1 if category == "equal_handles" else len(set(values)) == len(values)))
            if not valid:
                checks.append(f"{category} violated: {group}")
    for pair in norm["equivalent_outputs"]:
        left, right = pointer(actual, pair["left"]), pointer(actual, pair["right"])
        if left is MISSING or right is MISSING or not typed_equal(left, right):
            checks.append(f"equivalent_outputs violated: {pair['left']} != {pair['right']}")
    for predicate in vector["forbidden"]:
        if forbidden_matches(report, predicate):
            checks.append("forbidden predicate matched: " + cjson(predicate))
    if grammar:
        for i, response in enumerate([*report["operation_results"], report["result"]]):
            typ = response.get("type")
            if typ not in ("view", "receipt", "refusal") or not grammar.matches(response, grammar.schemas[typ]):
                checks.append(f"response {i} violates closed {typ} schema")
    return differences(actual, expected), checks


def package_version(root):
    text = (root / "README.md").read_text()
    return re.search(r"Version: \*\*([^*]+)\*\*", text).group(1)


def run(spec, commit):
    version = package_version(spec)
    grammar = Grammar(spec / "kernel/schemas")
    rows = []
    for path in sorted((spec / "kernel/vectors").glob("*/*.json")):
        vector = strict_loads(path.read_text())
        row = {"id": vector["id"], "profile": vector["profile"], "path": str(path.relative_to(spec)),
               "vector_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        if vector["profile"] == "deployment":
            row.update(status="unsupported", reason="Requires a real protected deployment; this evaluator implements synthetic state transitions only.")
        else:
            try:
                engine = Engine(vector["initial_state"], grammar, version)
                actual = engine.execute(vector["operations"], vector["query"])
                diffs, checks = compare(actual, vector, grammar)
                row.update(status="fail" if diffs or checks else "pass", differences=diffs, checks=checks, actual=actual)
            except Exception as error:
                row.update(status="fail", error=f"{type(error).__name__}: {error}", traceback=traceback.format_exc())
        rows.append(row)
    return {"package_version": version, "package_commit": commit,
            "implementation_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.glob("*.py"))},
            "vectors": rows}


def markdown(report):
    lines = ["# astra-23 vector run", "", f"Package: **{report['package_version']}** at `{report['package_commit']}`.",
             "", "The evaluator receives only initial_state, operations and query. Expected outputs,",
             "forbidden predicates and normalization are consumed only by the comparison runner.",
             "Random handles are normalized only at declared paths; their syntax, equality and",
             "distinctness are checked first. No runtime distribution or timing claim is made.", "",
             "| Profile | Pass | Fail | Unsupported | Total |", "| --- | ---: | ---: | ---: | ---: |"]
    for profile in ("semantic", "deployment"):
        rows = [r for r in report["vectors"] if r["profile"] == profile]
        counts = [sum(r["status"] == s for r in rows) for s in ("pass", "fail", "unsupported")]
        lines.append(f"| {profile} | {counts[0]} | {counts[1]} | {counts[2]} | {len(rows)} |")
    lines += ["", "Deployment unsupported means no qualification claim; modeled semantic erasure",
              "and publication transitions do not exercise live authentication, storage or delivery.", "",
              "## Per-vector results", "", "| Vector | Profile | Result |", "| --- | --- | --- |"]
    for row in report["vectors"]:
        lines.append(f"| {row['id']} | {row['profile']} | {row['status']} |")
    for row in report["vectors"]:
        if row["status"] == "pass":
            continue
        lines += ["", "### " + row["id"], ""]
        if "reason" in row:
            lines.append(row["reason"])
        if "error" in row:
            lines += ["Execution failure (not a semantic pass):", "```text", row["traceback"].rstrip(), "```"]
        for path, actual, expected in row.get("differences", []):
            lines.append(f"- `{path}`: actual `{cjson(actual)}`; expected `{cjson(expected)}`.")
        for check in row.get("checks", []):
            lines.append("- " + check)
    lines += ["", "## Reproducibility", "", "Implementation SHA-256:", ""]
    for name, sha in report["implementation_sha256"].items():
        lines.append(f"- `{name}`: `{sha}`")
    lines += ["", "Full actual reports, exact differences and vector digests are in the adjacent JSON report.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec-root", type=pathlib.Path, default=HERE.parents[1] / "spec")
    parser.add_argument("--package-commit")
    parser.add_argument("--output", type=pathlib.Path, default=HERE / "RESULTS.md")
    args = parser.parse_args()
    commit = args.package_commit or subprocess.check_output(
        ["git", "log", "-1", "--format=%H", "--", "memory/spec"], cwd=HERE.parents[2], text=True).strip()
    report = run(args.spec_root, commit)
    args.output.write_text(markdown(report))
    args.output.with_suffix(".json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    for profile in ("semantic", "deployment"):
        rows = [r for r in report["vectors"] if r["profile"] == profile]
        print(profile + ": " + ", ".join(f"{sum(r['status'] == s for r in rows)} {s}" for s in ("pass", "fail", "unsupported")))
    print("Report: " + str(args.output))
    return int(any(r["status"] == "fail" for r in report["vectors"]))


if __name__ == "__main__":
    raise SystemExit(main())
