# ASTRA24-02: an expired checked rule cannot carry a current witness

Status: submitted source-contract regression case; package not yet landed.
Source baseline: `cca7b6e`; kernel v0.2. Owner: astra-24.

## Clauses

Companion §3 assigns every registered rule its own applicability interval;
§4 permits only currently applicable witnesses under the same query Q.
Claim valid intervals are half-open and unknown time cannot silently answer a
point-in-time query. Kernel §§2 and 6 preserve these time distinctions. S10
mentions adjacent assertion intervals, but does not explicitly exercise an
expired rule with still-valid premises and conclusion.

## Minimal separating input

```text
A, B assertions: valid [2026-10-01T00:00:00Z, unbounded)
root A+: valid [2026-10-01T00:00:00Z, unbounded)
r1: A+ -> B+, checked sufficient_support
r1 applicability: [2026-10-10T00:00:00Z, 2026-10-11T00:00:00Z)
query B at 2026-10-11T00:00:00Z
```

All records are authorized, real, admitted before the memory cut, and evaluated
with enough budget. There is no independent root for B and no opposing root.

## Two readings and separating output

| Field | A: check assertion/premise time only | B: check every rule's applicability |
| --- | --- | --- |
| B support witness | present | not_found |
| B support evaluation | complete | complete |
| B oppose witness | not_found | not_found |

A rule whose deterministic assessment remains historically valid is not thereby
applicable at every future valid time. The checked relation and its temporal
applicability are separate.

## Recommendation and controls

Use B. At the exact exclusive endpoint r1 cannot provide support. Losing this
path supplies no opposing witness and changes no external decision.

Nearby positive control: query at 2026-10-10T23:59:59Z; support is present.
Alternative-path control: add an independent, currently applicable B+ root;
B remains supported after r1 expires. The old proof may be returned as history
at its named earlier cut, never as a current witness.

## Evidence and limits

This is a proposed separating fixture, not a reported evaluator failure.
Package-format JSON and concrete package clauses will be added after release.
If the package has no way to express a rule applicability interval, that is a
representation gap to classify, not a reason to silently make every rule eternal.
