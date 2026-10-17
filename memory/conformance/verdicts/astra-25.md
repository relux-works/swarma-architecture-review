# astra-25: disclosure and erasure verdict

Status: phase 2, round 11; eight cases and thirteen fixtures (twelve semantic, one deployment). Seat identity:
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

Eight separating cases are recorded:

| Case | Property | Evidence class |
| --- | --- | --- |
| [ASTRA25-01](../cases/astra-25-hidden-premise-quality.md) | Hidden premise opposition cannot change visible quality or logical budget outcomes | Semantic non-interference |
| [ASTRA25-02](../cases/astra-25-declassification-intersection.md) | All constrained owners' exact release decisions must still apply | Semantic disclosure; external enforcement separate |
| [ASTRA25-03](../cases/astra-25-surviving-support-erasure.md) | Independent support does not preserve tainted derivative bytes or prove custody closure | Semantic support and deployment erasure separated |
| [ASTRA25-04](../cases/astra-25-stale-restore-witness.md) | An outside-domain witness needs current complete coverage | Deployment restore |
| [ASTRA25-05](../cases/astra-25-hidden-dirty-invalidation.md) | Unqualified global dirty status can expose a hidden-only dependency revision | Semantic non-interference; package-clause conflict |
| [ASTRA25-06](../cases/astra-25-quality-budget-isolation.md) | Opposite-premise quality cannot consume the existence-witness budget | Observed source evaluator accounting divergence |
| [ASTRA25-07](../cases/astra-25-erasure-receipt-metadata.md) | Erasure closure must not disclose hidden derivative IDs without metadata authority | Observed package receipt divergence; clause conflict |
| [ASTRA25-08](../cases/astra-25-retention-authority.md) | Admit/read/use do not silently authorize retention of a derived record | Both evaluators admit the case lacking retain authority |

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

The judge classified ASTRA25-06 as R7-027, consolidated the direct-polarity
ASTRA24-05 neighbor, and assigned the source correction. I independently verified
source fix `4e647ea`: ASTRA25-01 and ASTRA25-06 pass unchanged, the companion
ASTRA24-05 passes, and all 29 source controls pass. Current owned source results
are 2 semantic pass / 0 fail / 6 unsupported; package results remain 8 semantic
pass. One deployment fixture remains unsupported by each. Exact fixed evidence
is appended as `astra22-v0.2.1-budget-fixed`; original failures are retained.

Judge ledger `56e5909` closes R7-027. Every owned classified defect is now
fixed; ASTRA25-01/03 remain retained regressions rather than spec defects.
After source fixes R7-028/029, I reran the owned nine-fixture corpus on `512d006`:
2 semantic pass / 0 fail / 6 unsupported, deployment 1 unsupported. The two
budget regressions remain green with unchanged inputs. Evidence is appended as
`astra22-v0.2.1-latest-source`. Package semantic behavior remains pinned to the
passing `f5fdd8b` evaluator; unrelated source changes do not replace that evidence.

**Provisional R7 score: 1/2.** Prose and schemas validate, and the owned fixes have behavior evidence;
collective judge closure and the separate source-resolution case remain pending. No deployment pass is claimed.
The initial package-absent 0/2 was only the round-0 baseline.

## Phase 2 and current outstanding work

The convener explicitly withheld PARK in event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc` and requires all 57 canonical
semantic vectors to pass both independent evaluators, plus one full round with
no new open item. Judge `b1ae299` verified the original supported-vector rubric
at 2/2, but that was not full dual-implementation coverage (43/57 in the source
implementation). The active objective continues through the previously
unsupported release/erase/restore/snapshot boundaries and v0.2 delta.

New ASTRA25-07 separates erasure authority from private derivative metadata:
K-API-1's authorized refs conflict with an unqualified reading of K-ERASE-2's full
closure receipt. The package evaluator actually discloses the hidden derivative
id; its separately authorized control passes. All eleven fixtures structurally
validate. Current package-owned semantic results are 9 pass / 1 fail; the one
deployment fixture stays unsupported. Exact evidence is persisted as
`astra23-phase2-erasure-receipt`. Judge classification is pending; original
expected contracts and historical reports remain intact.

**Phase-2 provisional score: 1/2** pending this new concrete divergence and the
requested full dual coverage. Continue the disclosure/erasure audit, verify the
source implementation as support arrives, and finalize only after actual PARK.


ASTRA25-08 extends the phase-2 authority audit: both evaluators persist a private
paraphrase when admit/read/use exist but no retain grant exists anywhere. The
positive control restores only retain and passes. Expected atomic rejection is
grounded in the source companion's independent permission checks, not agreement
between implementations. Current owned package run: 10 semantic pass / 2 fail;
source: 3 pass / 1 fail / 8 unsupported; one deployment unsupported by each.
Thirteen fixtures structurally validate. Both new cases await judge disposition.
