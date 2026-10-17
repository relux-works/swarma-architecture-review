# ASTRA24-02: an expired checked rule cannot carry a current witness

Status: source requirement accepted; released prose closes the choice; exact regression vector supplied.
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

## Package inspection and exact fixture — round 2

Release `0.1.0-draft` at `0ef608a` already closes the prose choice in
K-RULE-2 (rule validity participates in applicability) and K-TIME-1 (half-open
time). Its common envelope represents the interval. This is regression coverage,
not a confirmed package bug. Judge intake is R7-002.

The accompanying `.vector.json` captures support at the rule's inclusive start
and one second before its end, then queries at the exclusive endpoint. Premise,
conclusion and retained certificate remain valid. Both earlier outputs are
normalized-equal; the final output must have no support and no opposition.

Structural validation passed using the package validator on the exact owned
fixture: closed shape, initial references, handle normalization and forbidden
predicates. Planting a surviving endpoint witness triggers the intended forbidden
predicate. No independent evaluator run yet. Evidence: seat-local
`.temp/case-vectors-validate-01.log`; whole-package validation is recorded in
`.temp/package-validate-01.log`. No deployment execution is claimed.

Judge disposition, round 3: R7-002 rejected as a spec defect in `0.1.0-draft`;
existing prose is explicit. Regression fixture retained. Any future evaluator
mismatch requires a separate implementation-bug row.

## Source evaluator execution — round 4

The exact fixture passes against the frozen astra-22 evaluator at `3045117`.
It now includes the requested surviving-alternative control: a separate B+
root becomes applicable after r1 expires, and a later query returns that root
with `semantic_review` qualification and `origin:survivor`. The endpoint query
still has no witness, while both in-interval controls remain positive.

Fixture SHA-256:
`3266f571fe64c7e510a4e0d223a9c2ca25e3a9d141b271dabcfde79bb8ee4585`.
Evidence: seat-local `.temp/astra22-owned-cases-03.json` and
`.temp/case-vectors-validate-04.log`. This is one evaluator's exact semantic
pass; it does not qualify a protected deployment.

## 0.2.0 migration and independent rerun — round 5

The owned vector now uses 0.2.0 grammar: release version, disclosure decisions,
projection exclusions and explicit direct synthetic integration-lineage facts.
An initial migration check caught missing facts for added fixture records; the
complete corrected fixture passes `.temp/case-vectors-validate-07.log`. Earlier
semantic hashes above refer to their stated historical fixture revisions.

Both independent evaluators pass all interval and surviving-alternative
expectations: source `fb7df98` on current 0.2.0 syntax, package evaluator
`0008dc3` on the matched original 0.1.0 fixture and schemas. Evidence:
`.temp/astra22-owned-cases-06.json` and `.temp/astra23-owned-cases-0.1.json`.

Round 6: both current implementations pass this identical 0.2.0 fixture,
including all interval boundaries and the surviving-root control. Evidence:
`.temp/astra23-owned-cases-02.json` and `.temp/astra22-owned-cases-07.json`.

## 0.2.1 verification — round 7

The fixture now supplies explicit `policy.subject_principals` and empty
`runtime.dirty_causes`, with the 0.2.1 semantic profile. Its semantic expectations
are unchanged. Closed grammar, references, normalization and intended forbidden
plants pass in `.temp/case-vectors-validate-09.log`.

Current fixture SHA-256: `6c618f4103b240083cc87d94a79469accf91f44e1dcfd25f73c04ec1b066a41b`.
At checkout `4fadedd`, package evaluator fix `7c765fe` passes the entire
fixture. Source evaluator also passes the entire fixture.
Exact reports: `.temp/astra23-owned-cases-03.json` and
`.temp/astra22-owned-cases-08.json`. Executors receive no expected outputs.

These are semantic fixture results, not protected deployment qualification.

## Package 0.2.2 profile migration

Round 15 explicitly migrated the vector to `0.2.2-draft` at release `7e71765`.
Only semantic_profile metadata changed; no input or behavioral expectation
changed. This seat has no erase operation requiring the new receipt context.
Normalized equality and old/new hashes are recorded in
`.temp/astra24-profile-022-migration.json`. Both evaluators preserve this case's
pass in source report19 and package report11. Earlier hashes above identify
the historical profile-specific runs.

## Package 0.2.3 explicit migration

Round 21 migrates this case to `0.2.3-draft` (`23290b3`). Behavioral expected
results and initial states are unchanged. Read-only operations need no storage
context; each of this seat's six revise operations explicitly binds private/read
under its existing actor/space/record retain grant. No grant is inferred from a
later query. `.temp/astra24-profile-023-migration.json` records old/new hashes,
exact operation contexts and normalized equality. Structural and intended
forbidden controls pass log 22. Earlier hashes identify historical profile runs.
