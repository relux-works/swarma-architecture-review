# astra-25: disclosure and erasure verdict

Status: round 2, package inspection and four executable regression fixtures. Seat identity:
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

Four source-contract separating cases are recorded:

| Case | Property | Evidence class |
| --- | --- | --- |
| [ASTRA25-01](../cases/astra-25-hidden-premise-quality.md) | Hidden premise opposition cannot change visible quality or logical budget outcomes | Semantic non-interference |
| [ASTRA25-02](../cases/astra-25-declassification-intersection.md) | All constrained owners' exact release decisions must still apply | Semantic disclosure; external enforcement separate |
| [ASTRA25-03](../cases/astra-25-surviving-support-erasure.md) | Independent support does not preserve tainted derivative bytes or prove custody closure | Semantic support and deployment erasure separated |
| [ASTRA25-04](../cases/astra-25-stale-restore-witness.md) | An outside-domain witness needs current complete coverage | Deployment restore |

The judge accepted all four source requirements as R7-005–R7-008. Package
`0.1.0-draft` landed at `0ef608a`. Its structural validator passes: 53 semantic
and 8 deployment vectors, 14 closed schemas, 49 clauses and 13 intended checker
violation controls. This is structural evidence, not executed semantics.

ASTRA25-01 and ASTRA25-03 are already specified correctly in the package prose;
four owned JSON fixtures add the hidden-quality trace, incomplete/complete
custody pair and current-generation erasure-fence neighbor. They pass schema,
reference, normalization and forbidden-predicate checks. A planted hidden-dependent
quality change is rejected by the comparator for the intended reason. Evidence:
`.temp/package-validation-01.log`, `.temp/astra25-vector-structure-01.log`, and
the linked case files with exact JSON expectations.

ASTRA25-02 exposes the missing multi-owner/live-decision representation, confirmed
by the editor for the mandatory v0.2 update. ASTRA25-04 identifies a narrow
fixture-boundary clarification: an external witness boolean must mean current
complete verification, not location/existence; judge classification is pending.
No independent evaluator failure or deployment security pass is claimed.

**Provisional R7 score: 1/2.** The package exists and structurally validates;
kernel-v0.2 alignment, case disposition and both independent full vector reports
remain pending. The initial package-absent 0/2 was only the round-0 baseline.

## Outstanding

Await the v0.2 shape, encode the exact multi-owner pair, obtain final judge
dispositions, run owned fixtures against available evaluators without changing
their files, and recheck accepted package fixes through the round protocol.
Final disposition and any owner questions will be linked here before PARK.
