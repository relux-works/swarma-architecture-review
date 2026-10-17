"""Independent source-derived model; wire adapters must not supply expected answers.

Sources: kernel v0.2 §§2–9; companion §§3–8. This is an in-memory semantic
model over admitted, normalized inputs, not a protected-service implementation.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass, field
from typing import Any


class Refusal(Exception):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def canonical(value: Any) -> bytes:
    """Model framing only; package framing belongs in the wire adapter."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def strict_json(text: str) -> Any:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise Refusal("duplicate_key")
            result[key] = value
        return result

    def nonfinite(_):
        raise Refusal("invalid_number")

    return json.loads(text, object_pairs_hook=unique, parse_constant=nonfinite)


def literal(value):
    if isinstance(value, str):
        return (value, "support")
    return (value[0], value[1])


def valid_at(interval, instant):
    if instant is None:
        return True
    if interval == "unknown":
        return False
    if not interval:
        return True
    start, end = interval
    return (start is None or start <= instant) and (end is None or instant < end)


def applicable(record, query):
    """Filtering precedes evaluation and its logical accounting."""
    visible = query.get("authorized_ids")
    if visible is not None and record["id"] not in visible:
        return False
    if not record.get("visible", True):
        return False
    if record.get("recorded", 0) > query.get("cut", float("inf")):
        return False
    retired = record.get("withdrawn_at")
    if retired is not None and retired <= query.get("cut", float("inf")):
        return False
    if not valid_at(record.get("valid"), query.get("valid_at")):
        return False
    if record.get("mode", "real") != query.get("mode", "real"):
        return False
    if query.get("perspective") is not None:
        if record.get("perspective", query["perspective"]) != query["perspective"]:
            return False
    return True


@dataclass
class Channel:
    present: bool = False
    complete: bool = True
    clean: bool = False
    unchecked: bool = False
    qualifications: set = field(default_factory=set)
    roots: set = field(default_factory=set)
    source_states: set = field(default_factory=set)
    proof_count: int = 0
    cutoffs: set = field(default_factory=set)
    assessment_refs: set = field(default_factory=set)
    path_qualities: set = field(default_factory=set)
    proofs: int = 0


class Evaluator:
    """Finite signed AND/OR DAG evaluator with independent polarity channels."""

    def __init__(self, assertions=(), roots=(), rules=(), sources=(), associated_sources=None):
        self.assertions = {r["id"]: copy.deepcopy(r) for r in assertions}
        self.roots = copy.deepcopy(list(roots))
        self.rules = copy.deepcopy(list(rules))
        self.sources = {r["id"]: copy.deepcopy(r) for r in sources}
        self.associated_sources = copy.deepcopy(associated_sources or {})
        self._validate()

    def _validate(self):
        graph = {key: set() for key in self.assertions}
        for root in self.roots:
            if literal(root["target"])[0] not in graph:
                raise Refusal("unknown_reference")
        for rule in self.rules:
            target = literal(rule["target"])[0]
            if target not in graph or not rule.get("premises"):
                raise Refusal("invalid_rule")
            for premise in rule["premises"]:
                claim, sign = literal(premise)
                if claim not in graph:
                    raise Refusal("unknown_reference")
                if sign not in ("support", "oppose"):
                    raise Refusal("invalid_polarity")
                graph[target].add(claim)
            if (rule.get("edge_role", "sufficient_support") == "sufficient_support"
                    and (rule.get("kind", "checked_entailment") != "checked_entailment"
                         or not rule.get("checked", False))):
                raise Refusal("unqualified_rule")
        active, done, order = set(), set(), []

        def visit(key):
            if key in active:
                raise Refusal("cycle")
            if key in done:
                return
            active.add(key)
            for parent in sorted(graph[key]):
                visit(parent)
            active.remove(key)
            done.add(key)
            order.append(key)

        for key in sorted(graph):
            visit(key)
        self.order = order

    def evaluate(self, target, query=None):
        query = query or {}
        if target not in self.assertions:
            raise Refusal("unknown_reference")
        visible = {k for k, r in self.assertions.items() if applicable(r, query)}
        rules = [r for r in self.rules if applicable(r, query)
                 and literal(r["target"])[0] in visible
                 and all(literal(p)[0] in visible for p in r["premises"])
                 and r.get("edge_role", "sufficient_support") == "sufficient_support"]
        roots = [r for r in self.roots if applicable(r, query)
                 and literal(r["target"])[0] in visible
                 and (not r.get("source") or (r["source"] in self.sources
                      and applicable(self.sources[r["source"]], query)))
                 and all(s in self.sources and applicable(self.sources[s], query)
                         for s in r.get("source_members", []))]
        root_budget = query.get("root_budget", float("inf"))
        rule_budget = query.get("rule_budget", float("inf"))
        source_budget = query.get("source_budget", float("inf"))
        order = lambda record: tuple(record.get("reference_order", (record["id"], 0)))
        root_index, rule_index = {}, {}
        for root in sorted(roots, key=order):
            pins, expected = root.get("pins", {}), query.get("pins", {})
            if (not root.get("admitted", True) or root.get("result", "pass") != "pass"
                    or any(pins.get(k) != v for k, v in expected.items())
                    or root.get("qualification") not in query.get(
                        "qualifications", ["semantic_review", "test_result", "formal_entailment",
                                           "independent_attestation", "direct_declaration"])):
                continue
            root_index.setdefault(literal(root["target"]), []).append(root)
        for rule in sorted(rules, key=order):
            rule_index.setdefault(literal(rule["target"]), []).append(rule)
        include_paths = query.get("include_paths", False)
        proofs = None
        if include_paths:
            from proofs import Proofs
            proofs = Proofs(roots + rules)
            if type(query.get("explanation_budget")) is not int or query["explanation_budget"] < 0:
                raise Refusal("invalid_bound")

        # Only results from a fresh independent walk can be reused across walks.
        # The local memo below shares a literal within one bounded existence walk.
        full_walks = {}

        def walk(requested, collect_proofs=False):
            cache_key = (requested, collect_proofs)
            if cache_key in full_walks:
                return full_walks[cache_key]
            used = {"roots": 0, "rules": 0}
            resolved_sources = set()
            memo = {}

            def visit(current):
                if current in memo:
                    return memo[current]
                state = Channel()
                memo[current] = state
                if current[0] not in visible:
                    return state
                for root in root_index.get(current, []):
                    if used["roots"] >= root_budget:
                        state.complete = False
                        state.cutoffs.add("root_limit")
                        continue
                    used["roots"] += 1
                    if not root.get("retained", True) and not root.get("independent", False):
                        members = root.get("source_members", [root["source"]] if root.get("source") else [])
                        limited = False
                        for source_id in sorted(set(members), key=lambda s: order(self.sources[s])):
                            if source_id in resolved_sources:
                                continue
                            if len(resolved_sources) >= source_budget:
                                limited = True
                                state.complete = False
                                state.cutoffs.add("source_limit")
                            else:
                                resolved_sources.add(source_id)
                        if limited:
                            continue
                    source = self.sources.get(root.get("source"), {})
                    availability = source.get("availability", "resolvable")
                    if availability != "resolvable" and not root.get("retained", True):
                        state.complete = False
                        state.cutoffs.add("source_unavailable")
                        continue
                    state.present = True
                    state.path_qualities.add("clean")
                    state.qualifications.add(root["qualification"])
                    state.roots.add(root.get("origin", root["id"]))
                    state.assessment_refs.add(root["id"])
                    state.source_states.add(
                        "resolvable_now" if availability == "resolvable"
                        else "independent_attestation" if root.get("independent", False)
                        else "prior_assessment_only")
                    state.proof_count += 1
                    if collect_proofs:
                        state.proofs = proofs.union(state.proofs, proofs.singleton(root["id"]))
                for rule in rule_index.get(current, []):
                    if used["rules"] >= rule_budget:
                        state.complete = False
                        state.cutoffs.add("rule_limit")
                        continue
                    used["rules"] += 1
                    literals = sorted((literal(p) for p in rule["premises"]),
                                      key=lambda p: (order(self.assertions[p[0]]), p[1]))
                    # Evaluate every necessary premise, including after a miss.
                    premises = [visit(p) for p in literals]
                    state.complete = state.complete and all(p.complete for p in premises)
                    for premise in premises:
                        state.cutoffs.update(premise.cutoffs)
                    if not all(p.present for p in premises):
                        continue
                    state.present = True
                    qualities = {"clean"}
                    for reference, premise in zip(literals, premises):
                        opposite = walk((reference[0], "oppose" if reference[1] == "support" else "support"))
                        alternatives = {"tainted" if opposite.present or q == "tainted"
                                        else "unchecked" if not opposite.complete or q == "unchecked"
                                        else "clean" for q in premise.path_qualities}
                        # This finite three-state join preserves taint over
                        # uncertainty on one path and clean OR alternatives.
                        qualities = {"tainted" if "tainted" in (a, b)
                                     else "unchecked" if "unchecked" in (a, b)
                                     else "clean" for a in qualities for b in alternatives}
                        state.qualifications.update(premise.qualifications)
                        state.roots.update(premise.roots)
                        state.assessment_refs.update(premise.assessment_refs)
                    state.path_qualities.update(qualities)
                    ranks = {"prior_assessment_only": 0, "independent_attestation": 1, "resolvable_now": 2}
                    path_rank = min(max(ranks[s] for s in p.source_states) for p in premises)
                    state.source_states.add(next(s for s, rank in ranks.items() if rank == path_rank))
                    state.qualifications.add("checked_entailment")
                    state.proof_count += 1
                    if collect_proofs:
                        family = proofs.singleton(rule["id"])
                        for premise in premises:
                            family = proofs.join(family, premise.proofs)
                        state.proofs = proofs.union(state.proofs, family)
                state.clean = "clean" in state.path_qualities
                state.unchecked = "unchecked" in state.path_qualities
                return state

            result = visit(requested)
            full_walks[cache_key] = result
            return result

        channels = {(target, sign): walk((target, sign), include_paths) for sign in ("support", "oppose")}
        assertion = self.assertions[target]
        until = query.get("usable_until", assertion.get("usable_until"))
        now = query.get("now", query.get("valid_at"))
        freshness = ("not_applicable" if until is None else
                     "stale" if now is not None and now >= until else "fresh")

        def render(sign):
            state = channels.get((target, sign), Channel())
            if state.clean:
                quality = "clean_path"
            elif state.present and not state.unchecked and state.complete:
                quality = "conflicted_premises_only"
            else:
                quality = "not_fully_checked"
            source_state = ("resolvable_now" if "resolvable_now" in state.source_states
                            else "independent_attestation" if "independent_attestation" in state.source_states
                            else "prior_assessment_only" if state.source_states else "resolvable_now")
            if not state.present:
                associated = set(self.associated_sources.get(target, []))
                associated.update(r["source"] for r in roots
                                  if literal(r["target"])[0] == target and r.get("source"))
                if any(s in self.sources and applicable(self.sources[s], query)
                       and self.sources[s].get("availability", "resolvable") != "resolvable"
                       for s in associated):
                    source_state = "prior_assessment_only"
            return {"witness": "present" if state.present else "not_found",
                    "evaluation": "complete" if state.complete else "incomplete",
                    "corpus_coverage": query.get("corpus_coverage", "unknown"),
                    "premise_quality": quality,
                    "evidence_qualification": sorted(state.qualifications),
                    "source_state": source_state,
                    "freshness": freshness,
                    "authorized_snapshot_handle": "<fresh-authorized-handle>",
                    "dependency_coverage": "registered_only",
                    "root_origins": sorted(state.roots),
                    "witness_assessments": sorted(state.assessment_refs)}

        result = {"support": render("support"), "oppose": render("oppose")}
        proof_count = sum(channels.get((target, p), Channel()).proof_count
                          for p in ("support", "oppose"))
        result["explanation"] = {"complete": proof_count <= query.get("explanation_budget", float("inf")),
                                 "count": min(proof_count, query.get("explanation_budget", proof_count))}
        if include_paths:
            budget = query["explanation_budget"]
            family = proofs.union(channels[(target, "support")].proofs, channels[(target, "oppose")].proofs)
            paths = proofs.take(family, budget + 1)
            result["proof_paths"] = paths[:budget]
            result["explanation"] = {"complete": len(paths) <= budget, "count": len(paths[:budget])}
        result["cutoffs"] = sorted(set().union(*(channels.get((target, p), Channel()).cutoffs
                                                for p in ("support", "oppose"))))
        return result


def sequence_key(record):
    return tuple(record.get(k) for k in ("issuer", "subject", "schema", "perspective", "slot"))


def incompatibilities(assertions, relations):
    """Declared unequal fields relate current assertions, never signed evidence."""
    result = {r["id"]: set() for r in assertions}
    for index, left in enumerate(assertions):
        for right in assertions[index + 1:]:
            if left["schema"] != right["schema"]:
                continue
            for relation in relations:
                if relation["relation"] != "unequal":
                    raise Refusal("unknown_incompatibility")
                if any(left.get(k) != right.get(k) for k in ("subject", "space", "perspective")):
                    continue
                if left.get("schema_slot", left.get("slot")) != right.get("schema_slot", right.get("slot")):
                    continue
                if any(r["statement_kind"] not in relation["statement_kinds"] for r in (left, right)):
                    continue
                a, b = left.get("valid"), right.get("valid")
                if a == "unknown" or b == "unknown" or a is None or b is None:
                    continue
                if (a[1] is not None and b[0] is not None and a[1] <= b[0]
                        or b[1] is not None and a[0] is not None and b[1] <= a[0]):
                    continue
                field = relation["field"]
                if canonical(left["content"][field]) != canonical(right["content"][field]):
                    result[left["id"]].add(right["id"])
                    result[right["id"]].add(left["id"])
    return {k: sorted(v) for k, v in result.items()}


class Memory:
    """Synthetic transaction, projection, lineage and delivery model."""

    def __init__(self, records=(), schemas=()):
        self.records = {r["id"]: copy.deepcopy(r) for r in records}
        self.schemas = set(schemas)
        self.receipts = {}
        self.sequence = max((r.get("recorded", 0) for r in records), default=0)
        self.disclosure_revoked = set()
        self.erased = set()
        self.epoch = 0
        self.restore_ready = True

    def _head(self, key):
        candidates = [r for r in self.records.values() if r.get("kind") == "assertion"
                      and sequence_key(r) == key]
        replaced = {r.get("replaces") for r in candidates}
        heads = [r for r in candidates if r["id"] not in replaced]
        return heads[0]["id"] if len(heads) == 1 else None

    def admit(self, record, *, submitter=None, representation_valid=False,
              expected_version=None, idempotency_key=None):
        record = copy.deepcopy(record)
        submitter = submitter or record.get("issuer")
        identity = (submitter, record.get("space"), idempotency_key)
        digest = hashlib.sha256(canonical(record)).hexdigest()
        if idempotency_key is not None and identity in self.receipts:
            old_digest, receipt = self.receipts[identity]
            if old_digest != digest:
                raise Refusal("idempotency_conflict")
            return copy.deepcopy(receipt)
        if record["id"] in self.records:
            raise Refusal("duplicate_record")
        if record.get("kind") == "assertion" and record.get("schema") not in self.schemas:
            raise Refusal("unknown_schema")
        if record.get("issuer") != submitter and not representation_valid:
            raise Refusal("representation_required")
        if record.get("admission_class") == "semantic_inference" and record.get("kind") == "assessment":
            if record.get("check_kind") != "semantic_review":
                raise Refusal("qualification_laundering")
        relation = record.get("relation")
        prior = self.records.get(record.get("prior"))
        if relation:
            if prior is None:
                raise Refusal("unknown_reference")
            if relation in ("replace", "withdraw", "correct"):
                if record.get("issuer") != prior.get("issuer"):
                    raise Refusal("revision_authority")
                if expected_version != self._head(sequence_key(prior)):
                    raise Refusal("version_conflict")
        if record.get("replaces"):
            prior = self.records.get(record["replaces"])
            if prior is None:
                raise Refusal("unknown_reference")
            if sequence_key(record) != sequence_key(prior):
                raise Refusal("revision_authority")
            if expected_version != self._head(sequence_key(prior)):
                raise Refusal("version_conflict")
        lineage = record.get("lineage", [])
        if lineage != "unknown" and any(ref in self.erased for ref in lineage):
            raise Refusal("erasure_fence")
        if record.get("extraction_epoch", self.epoch) != self.epoch:
            raise Refusal("stale_derivative")
        self.sequence += 1
        record["recorded"] = self.sequence
        record["submitter"] = submitter
        self.records[record["id"]] = record
        receipt = {"status": "admitted", "id": record["id"]}
        if idempotency_key is not None:
            self.receipts[identity] = (digest, copy.deepcopy(receipt))
        return receipt

    def project(self, query):
        selected = [r for r in self.records.values()
                    if r.get("kind") == "assertion" and applicable(r, query)
                    and r["id"] not in self.erased
                    and (query.get("subject") is None or r.get("subject") == query["subject"])
                    and (query.get("issuer") is None or r.get("issuer") == query["issuer"])]
        excluded = set(query.get("excluded", []))
        if query.get("family") == "audience_projection":
            selected = [r for r in selected if r["id"] not in excluded
                        and self.deliverable(r, query.get("audience"), query.get("purpose"))]
        current, historical, ambiguous = [], [], []
        groups = {}
        for record in selected:
            groups.setdefault(sequence_key(record), []).append(record)
        for group in groups.values():
            decision = group[0].get("statement_kind") == "decision_record"
            if decision:
                candidates = [r for r in group if r.get("authority_receipt")]
                ordered = {r["id"]: set(r.get("authority_after", [])) for r in candidates}

                def predecessors(key, seen=None):
                    seen = set() if seen is None else seen
                    for parent in ordered.get(key, set()):
                        if parent not in seen:
                            seen.add(parent)
                            predecessors(parent, seen)
                    return seen

                old = set().union(*(predecessors(k) for k in ordered)) if ordered else set()
                heads = [r["id"] for r in candidates if r["id"] not in old]
                if len(heads) > 1:
                    ambiguous.extend(heads)
                current.extend(heads)
                historical.extend(r["id"] for r in group if r["id"] not in heads)
            else:
                old = {r.get("replaces") for r in group}
                heads = [r["id"] for r in group if r["id"] not in old
                         and not r.get("withdrawn", False)]
                current.extend(heads)
                historical.extend(r["id"] for r in group if r["id"] not in heads)
        return {"current": sorted(current), "historical": sorted(historical),
                "status": "ambiguous_current" if ambiguous else "current",
                "ambiguous": sorted(ambiguous)}

    def derive(self, record, supplied_inputs, *, complete=True):
        record = copy.deepcopy(record)
        constraints = set(record.get("constraints", []))
        for key in supplied_inputs:
            if key not in self.records:
                raise Refusal("unknown_reference")
            constraints.update(self.records[key].get("constraints", []))
        record["constraints"] = sorted(constraints)
        record["lineage"] = list(supplied_inputs) if complete else "unknown"
        record["adapter_inputs"] = list(supplied_inputs)
        record["publishable"] = complete and not constraints
        return record

    def deliverable(self, record, audience, purpose, decisions=()):
        if not self.restore_ready or record["id"] in self.erased:
            return False
        if (record["id"], audience) in self.disclosure_revoked:
            return False
        if record.get("lineage") == "unknown":
            return False
        remaining = set(record.get("constraints", []))
        for decision in decisions:
            if (decision.get("current", False) and decision.get("authorized", False)
                    and decision.get("audience") == audience and decision.get("purpose") == purpose
                    and decision.get("inputs") == record.get("lineage")
                    and decision.get("transformation") == record.get("transformation")
                    and decision.get("output_schema") == record.get("schema")):
                remaining.discard(decision["owner"])
        return not remaining

    def erase(self, targets):
        affected = set(targets)
        while True:
            old = set(affected)
            for key, record in self.records.items():
                lineage = record.get("lineage", [])
                if lineage == "unknown":
                    lineage = record.get("adapter_inputs", [])
                if affected.intersection(lineage):
                    affected.add(key)
            if affected == old:
                break
        self.epoch += 1
        self.erased.update(affected)
        return sorted(affected)

    def revoke(self, record_id, audience):
        self.disclosure_revoked.add((record_id, audience))

    def snapshot(self, query):
        return {"cut": self.sequence, "query": copy.deepcopy(query),
                "view": self.project(query)}


def field_differences(expected, actual, path="$"):
    """Exact comparison, including unexpected fields and list order."""
    differences = []
    if type(expected) is not type(actual):
        return [{"path": path, "expected": expected, "actual": actual}]
    if isinstance(expected, dict):
        for key in sorted(expected.keys() | actual.keys()):
            if key not in expected:
                differences.append({"path": path + "." + key, "expected": "<absent>", "actual": actual[key]})
            elif key not in actual:
                differences.append({"path": path + "." + key, "expected": expected[key], "actual": "<absent>"})
            else:
                differences.extend(field_differences(expected[key], actual[key], path + "." + key))
    elif isinstance(expected, list):
        if len(expected) != len(actual):
            differences.append({"path": path + ".length", "expected": len(expected), "actual": len(actual)})
        for index, (a, b) in enumerate(zip(expected, actual)):
            differences.extend(field_differences(a, b, f"{path}[{index}]"))
    elif expected != actual:
        differences.append({"path": path, "expected": expected, "actual": actual})
    return differences
