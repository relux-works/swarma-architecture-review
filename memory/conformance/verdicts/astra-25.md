# astra-25: disclosure and erasure verdict

Status: round 1, source-contract regression cases submitted. Seat identity:
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

Each case states its clauses, minimal input, different outcomes and positive and
negative controls. No evaluator failure is claimed from these prose fixtures.
`memory/spec/` is absent at inspected `4d4ef45`; package-format JSON cannot yet be
written. Package validation and vector results are unavailable, not passing.
No deployment security behavior has been executed or qualified.

**Provisional R7 score: 0/2**, because the canonical package is absent. This is a
baseline state, not a verdict on the pending package or on another seat's work.

## Outstanding

Await package publication, encode representable cases, obtain judge dispositions,
recheck accepted changes and remain active through the round protocol.
Final disposition and any owner questions will be linked here before PARK.
