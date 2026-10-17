# ASTRA24-07: Cartesian proof paths are not independent root origins

Status: R7-035 rejected as a defect allegation, accepted as regression coverage.
Source proof extension independently verified; no observed mismatch or source ambiguity.
Owner: astra-24. Package `0.2.1-draft` at `f31d58f`; execution checkout `91163c4`.

## Clauses and two readings

Companion sections 4–5 distinguish AND premises, alternative support and limited
proof rendering. Kernel 6.1/P07 deduplicates copied evidence by root origin for
independence claims. K-EVAL-3 sorts/deduplicates witness origins; K-EVAL-7 instead
enumerates exact sets of root-assessment and justification references. K-EVAL-2
memoizes literals within a bounded evaluation walk before separate rendering.

A convenient reading collapses proofs with the same origin set before rendering.
The required reading deduplicates exact proof-reference sets, while the separate
root-origin qualification remains deduplicated. The first reading cannot preserve
the declared exact explanation contract; this case requests regression coverage,
not a normative change.

## Minimal separating input

```text
A+ roots a1 and a2, both origin:alpha.
C+ roots c1 and c2, both origin:gamma.
One checked A+ AND C+ -> B+ rule, no opposing evidence.
Evaluation bounds: 4 root visits and 1 rule visit.
Capture explain(B) with 4 explanation slots; repeat with 3 slots.
```

The four proof sets are {a1,c1,rule}, {a1,c2,rule}, {a2,c1,rule},
{a2,c2,rule}, each sorted and then ordered by canonical JSON. The rule's certificate
is pinned by the rule and is not an extra proof vertex. Each necessary literal is
visited once per existence walk: forming four proof combinations does not cause
extra root visits. Input root storage order is deliberately reversed.

| Observable | Origin-set collapse | Required exact proof sets |
| --- | --- | --- |
| Full explanation paths | 1 | 4 |
| Explanation cap 3 | complete | partial, explanation_limit, 3 exact paths |
| Support witness/evaluation | present / complete | present / complete |
| Independent root count | 2 | 2 |

Counting four proof paths as four independent roots is a separate forbidden
shortcut. Both full and capped extended support/opposition records must remain
normalized-equal, including clean_path, qualifications, completeness and origins.

## Controls, execution and limits

`astra-24-cartesian-proofs.vector.json` captures all four paths as the positive
control. The final three-slot query checks exact truncation without evaluation
loss, and explicit predicates forbid inflated independence, incomplete evidence,
conflicted-only quality or a falsely complete explanation. Postconditions retain
the exact unchanged record inventory. No expected answer was supplied to execution.

The package evaluator passes the entire fixture, exact order, normalized paired
records and forbidden checks. The source evaluator explicitly reports exact proof
enumeration unsupported; that is neither a pass nor an observed wrong answer.
This new case exercises the S07 Phase 2 coverage gap beside ASTRA24-01, which
already protects clean-alternative quality under truncated rendering.

Fixture SHA-256: `ef2a655c6267a6b6064faee792902989009aa7cc1b35f5dca1521012b63d3570`.
Seat-local reports: `.temp/astra22-owned-cases-15.json`,
`.temp/astra23-owned-cases-08.json`. Closed shape, state references, handle
normalization, inventory and intended independent-count violation plant pass
`.temp/case-vectors-validate-13.log`. Both comparison harnesses' controls pass.
No deployment claim is made, and this small DAG is not a performance bound for
arbitrary proof enumeration.

## Round 14 source proof verification

Judge event `$UZdvnT7Rr6M6qyXZtyxf8uTE5OE3ivlwsPrlANzmCnw`, persisted at
`945096f`, confirms the distinction is already explicit and retains the case
as R7-035 regression coverage. No specification change was requested.

Source extension `4960d24` now passes this unchanged exact fixture and
ASTRA24-01. All seven owned cases pass with zero differences, failed forbidden
predicates or unsupported operations. Report: `.temp/astra22-owned-cases-16.json`.
Four focused source proof controls also pass in
`.temp/astra22-proof-controls-01.log`: finite-set union/join with overlapping
proofs, canonical ordering versus numeric reference versions, hidden/quality
separation, and a bounded prefix of a factored 2**40 proof family. These controls
do not establish a general polynomial space bound for every proof family.

The package implementation has not changed since its recorded exact pass.
Fixture SHA-256 remains unchanged. This closes the source coverage gap for
this regression without turning its earlier unsupported result into a failure.

## Package 0.2.2 profile migration

Round 15 explicitly migrated the vector to `0.2.2-draft` at release `7e71765`.
Only semantic_profile metadata changed; no input or behavioral expectation
changed. This seat has no erase operation requiring the new receipt context.
Normalized equality and old/new hashes are recorded in
`.temp/astra24-profile-022-migration.json`. Both evaluators preserve this case's
pass in source report19 and package report11. Earlier hashes above identify
the historical profile-specific runs.
