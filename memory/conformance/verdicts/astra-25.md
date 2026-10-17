# astra-25: disclosure and erasure verdict

Status: round 7, six cases and nine fixtures (eight semantic, one deployment). Seat identity:
`ivmbp_swarma-memory_astra-25`. Baseline: `95f974b` (2026-10-17).

## Scope and evidence

Read `memory/MISSION-R7.md` in full after the required initial pull; read owner
decisions D-001–D-008, kernel v0.2, the semantic companion, the bounded-evidence
design, and the existing erasure-closure and view-inference findings. No other
seat's evaluator has been used as an oracle.

The audit targets S13/S24/S27 non-interference; content lineage versus cited
evidence; multi-owner declassification evidence and current applicability;
historical snapshots versus new disclosures; custody closure, restore and late
derivative commits. Cases will include minimal separating inputs, both readings
and positive controls, with package-format vectors when the grammar exists.

## Current result

Six separating cases are recorded:

| Case | Property | Evidence class |
| --- | --- | --- |
| [ASTRA25-01](../cases/astra-25-hidden-premise-quality.md) | Hidden premise opposition cannot change visible quality or logical budget outcomes | Semantic non-interference |
| [ASTRA25-02](../cases/astra-25-declassification-intersection.md) | All constrained owners' exact release decisions must still apply | Semantic disclosure; external enforcement separate |
| [ASTRA25-03](../cases/astra-25-surviving-support-erasure.md) | Independent support does not preserve tainted derivative bytes or prove custody closure | Semantic support and deployment erasure separated |
| [ASTRA25-04](../cases/astra-25-stale-restore-witness.md) | An outside-domain witness needs current complete coverage | Deployment restore |
| [ASTRA25-05](../cases/astra-25-hidden-dirty-invalidation.md) | Unqualified global dirty status can expose a hidden-only dependency revision | Semantic non-interference; package-clause conflict |
| [ASTRA25-06](../cases/astra-25-quality-budget-isolation.md) | Opposite-premise quality cannot consume the existence-witness budget | Observed source evaluator accounting divergence |

The initial package `0.1.0-draft` landed at `0ef608a`. The judge rejected
ASTRA25-01/R7-005 and ASTRA25-03/R7-007 as spec defects because the prose already
requires the intended behavior; their executable regressions remain useful.
The judge classified ASTRA25-02/R7-006, ASTRA25-04/R7-008 and ASTRA25-05/R7-018
as spec-bugs.

Package `0.2.0-draft` at `cde5754` passes its structural validator: 57 semantic
and eight deployment vectors, 52 clauses, 16 intended checker controls. I verified
the R7-006 multi-owner/current-decision representation and R7-008 trusted-current-
complete restore-witness clarification against the source requirements. Owned
fixtures add wrong-owner revocation with an unchanged-view control and an omitted
stale erase inventory. These checks close the representation concerns. Deployment qualification is unproven.

All eight owned fixtures were validated with the 0.2.0 closed grammar and pass schema,
reference, normalization and forbidden-predicate checks. A planted hidden-quality
change and a planted global-dirty response are both rejected for the intended
paired-output mismatch. Evidence: `.temp/astra25-vector-structure-05.log` and the
linked exact JSON cases. Synthetic integration facts are explicit fixture inputs,
not a claim that a real adapter may trust author-supplied lineage.

The first independent runs used the SIX ORIGINAL 0.1.0 fixtures from `3045117`
and matching 0.1.0 schemas. They do not claim to test the migrated 0.2.0 inputs.
Exact field differences and implementation/input hashes are persisted in
[`astra-25-evaluator-results.json`](../cases/astra-25-evaluator-results.json).

| Evaluator | Pass | Fail | Unsupported | Evidence |
| --- | ---: | ---: | ---: | --- |
| astra-22 first adapter | 0 | 0 | 6 | These mutating operations are not implemented |
| astra-23 first evaluator `0008dc3` | 5 | 1 | 0 | ASTRA25-05: 14 field differences, paired equality and two forbidden outcomes |

A separate current-version run uses the eight fixtures at `9222266`, package
`cde5754`, and astra-23 `1439219`. It passes six semantic fixtures and fails only
the still-open R7-018 hidden-dirty trace (14 differences). In particular, the
joint-declassification wrong-owner/live-revocation trace passes exactly, supplying
behavior evidence for R7-006. The source adapter reports all seven mutating
semantic cases unsupported. Both report the one deployment case unsupported.
The runs `astra22-v0.2` and `astra23-v0.2` retain exact hashes and results.

The hidden-dirty failure reproduces the R7-018 contradiction. Its visible-path
control passes. The editor accepted a fix preserving protected invalidation
causes and filtering disclosed dirty/review/cutoff effects through eligible paths.
The protected global dirty inventory may remain unchanged.

The judge closed R7-006 and R7-008 at `cde5754`, with semantic joint-release
behavior verified and restore qualification still explicitly unsupported.
The next package `0.2.1-draft` at `f31d58f` closes R7-018's prose contradiction
using protected unresolved dirty causes and authorized-path eligibility. I verified
that the hidden/public and visible/dirty requirements both remain explicit.
All eight owned fixtures are migrated to 0.2.1 without changing their semantic
expected results, adding only the required empty initial dirty-cause inventory,
subject/principal identity and profile-version fields. They pass structural
checks and both leak controls; the package passes 20 intended checker controls.
The corrected independent evaluator `f5fdd8b` now passes all seven semantic
fixtures at `0fa73fd`, including both hidden/visible dirty traces. This verifies
R7-018 behavior against the owned case. The deployment fixture remains unsupported.

The newly extended source evaluator `df499a1` reveals a separate accounting
failure in ASTRA25-01's visible positive control. New ASTRA25-06 isolates it:
A+, A-, A+ -> B+ and roots=1; the opposite quality check consumes the shared root
counter and loses B support. The roots=2 capture passes; expected equivalence is
explicit under K-EVAL-2/4. The package evaluator passes both. The source trace
fails in seven fields plus the paired check and forbidden predicates, and is
submitted for classification without changing either evaluator or the expected
contract. With this new fixture, current owned results are package 8 semantic
pass; source 2 semantic fail / 6 unsupported; deployment 1 unsupported each.
Exact reports and hashes are appended as `astra22-v0.2.1[-budget]` and
`astra23-v0.2.1[-budget]`. No hidden leak is inferred from the new accounting
failure: ASTRA25-01's hidden/non-hidden captures remain equal.

**Provisional R7 score: 1/2.** Prose and schemas validate, but classified open
bugs and independent semantic failures remain. No deployment pass is claimed.
The initial package-absent 0/2 was only the round-0 baseline.

## Outstanding

Obtain judge classification and correction of ASTRA25-06's accounting divergence;
recheck both its narrow positive/negative controls and the original trace after
any fix. Follow collective exact-release runs and final ledger disposition.
Finalize the verdict and park note only after the convener's PARK.
