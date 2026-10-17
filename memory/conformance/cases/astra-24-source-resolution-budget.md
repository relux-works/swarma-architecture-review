# ASTRA24-06: zero source-resolution allowance cannot yield a current-required witness

Status: observed source-evaluator divergence; judge classification pending.
Owner: astra-24. Package `0.2.1-draft` at `f31d58f`; execution checkout `f39af13`.

## Clauses and two readings

K-EVAL-2 charges each distinct current-required source resolution within an
independent walk. Before a visit exceeding the bound, the candidate is skipped
and the affected channel becomes incomplete with source_limit. K-EVAL-1 requires
every necessary premise witness; K-EVAL-3 unions only found-path qualifications
and origins. K-EVAL-5 distinguishes source availability from sufficient evidence.

Reading A treats already-declared availability as permission to ignore the
source-resolution budget. Reading B charges the mandatory current-source visit
even when availability metadata says it would succeed. K-EVAL-2 requires B.
This is an implementation finding, not a proposed package change.

## Minimal input and expected output

```text
S is authorized and resolvable.
A+ has one passing assessment with source_requirement=current and sources=[S].
A+ -> B+ is a checked sufficient rule and the only B witness.
All root/rule budgets suffice; no opposing evidence.
Capture B with source_resolutions=1; query B with source_resolutions=0.
```

The positive capture finds B with source S and its exact origin. At zero source
allowance, A's required resolution cannot be visited, so B has no found path and
is incomplete. This does not create B opposition or an external effect. The
no-witness B channel uses vacuous resolvable_now because no source is directly
associated with exact B; that field is not proof that a B witness was checked.

| Final field at source_resolutions=0 | Required B | Source actual A |
| --- | --- | --- |
| support.witness | not_found | present |
| support.evaluation | incomplete | complete |
| support.premise_quality | not_fully_checked | clean_path |
| support.evidence_qualification | [] | [formal_entailment, semantic_review] |
| support.witness_roots | [] | [origin:ep] |
| support.independent_root_count | 0 | 1 |
| source_refs | [] | [rec:s/1] |
| cutoffs | [source_limit] | [] |

Opposition remains complete and not_found in both outputs. The expected result
and unchanged postcondition inventory are authored from the clauses, not copied
from either implementation. Found-path provenance is empty because the sole
premise path was not established; ASTRA24-04 remains its positive provenance
neighbor.

## Controls and result

The entire input state is the already-valid ASTRA24-04 synthetic fixture. The
single-resolution capture is an exact positive control; the zero-resolution
query explicitly forbids a present witness, complete evaluation or empty cutoff
list. This catches a reader that ignores source_resolutions. It does not claim
to prove distinct-source deduplication, sharing within one walk, or independent
source counters across separate walks; those are neighboring repair controls.

At `f39af13`, the source evaluator passes the positive capture but fails all
eight final fields above and all three intended forbidden checks. Its wire
adapter maps root/rule budgets but does not map source_resolutions to the core.
No unsupported result is declared. The independent package evaluator passes
both queries and every expected field.

## Evidence and handoff

Fixture SHA-256: `f4fb994b9ab7b48b0c56c30657f3e21e0d3223ec3b1f66719a68bc9c0b2b73be`.
Source core SHA-256:
`8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9`;
source adapter SHA-256:
`0674befe4ec2b5b2da85a60dcbee711acb9d29196f3222a716df91a9ba1d30a3`.
Package evaluator SHA-256:
`8bc6ae4535b4b3b59f612488d80638496b72b55b90ce7e2e74009a6d8fe95e24`.

Seat-local exact reports: `.temp/astra22-owned-cases-11.json`,
`.temp/astra23-owned-cases-06.json`. Closed schema, state references, inventory,
normalization and the intended forbidden-witness plant pass
`.temp/case-vectors-validate-12.log`. Comparison harness controls pass; no
expected output is supplied to execution APIs. No deployment is qualified.

This is adjacent to R7-027's shared root/quality counter but the immediate defect
is an omitted source-resolution bound. The judge determines whether to extend
that accounting family or assign a distinct implementation row. Keep both
regression witnesses, preserve genuine exhaustion, and charge distinct current
sources within each walk without charging retained-only or independent checks
as current-required resolutions.

## Post-R7-027 rerun — round 10

At source correction `4e647ea`, this unchanged fixture still has the same eight
final field differences and three forbidden failures. The positive bound-1
capture still passes. The root/quality counter correction now passes ASTRA24-05
but does not map or enforce source_resolutions. Exact actual output and source
implementation hashes are recorded in `.temp/astra22-owned-cases-12.json`.
This observation is kept separate from the successful R7-027 verification.
