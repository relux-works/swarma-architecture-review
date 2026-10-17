# astra-21 package editor verdict

Status: round 3, active; review snapshot at `80a217a`, awaiting convener PARK.

**Released package: 0.2.1-draft at `f31d58f`. Provisional R7 score: 1/2.**
All nine editor-owned spec bugs are judge-closed. Source corrections and a new
budget case await judge review; no owner question is established.
The judge owns the final [score](../R7-SCORE.md) and [ledger](../LEDGER.md).

## Scope and independence

Sole writer of `memory/spec/`, identity `ivmbp_swarma-memory_astra-21`.
Read the mission, decisions D-001–D-008, kernel v0.2, normative companion and
design, and the landed package. Initial baseline: `0ef608a`, package 0.1.0.
No source design was amended. Only the package and this seat's verdict/park note
are production write scope; scratch evidence and task tracking stay in `.temp/`.

## Released corrections

Signed `cde5754` publishes 0.2.0: normalized query inputs; distinct write refusal,
projection ambiguity and evidence conflict; immutable snapshots with current
delivery checks; complete/unknown integration-established lineage; live per-owner
declassification; projection exclusion; exact public role aliases; and current,
complete restore-witness meaning. P12–P15 are added, P05/B10 extended.
Judge-closed R7-006/008/009/010. Of 61 original expected reports, 59 are unchanged
apart from the profile version; P05/B10 intentionally add boundary controls.

Signed `f31d58f` publishes 0.2.1: weakest necessary AND source state followed by
strongest complete OR state; projection-eligible unresolved dirty causes;
actual-publication currentness; B01's missing integration fact; and explicit
subject/principal identity with correctly typed organisation assertions.
Judge-closed R7-014/018/019/021/022 at `6a4f307`. Release and migration details:
[RELEASES.md](../../spec/RELEASES.md). B01's semantic expected report is unchanged;
only B03/B07/P02/P15/S23/S24/S32 intentionally change expectations in this release.

## Validation and execution evidence

`python3 memory/spec/checks/validate.py` passes: 94 JSON artifacts, 14 closed
schemas, 14 domain documents, one fixture corpus, 52 normative clauses and
20 checker controls detecting their intended violations. Inventory: **65 vectors,
57 semantic and 8 deployment**. Deterministic schema/domain/vector regeneration
passes. Commands and limits: [BUILD_NOTES.md](../../spec/checks/BUILD_NOTES.md).
Local logs: `.temp/astra-21/validate-10.log`, `regeneration-02.log` and the retained
B01 missing-fact witness `lineage-regression-01.log`.

Package evaluator `f5fdd8b` passes **57/57 canonical semantic vectors**, with
13 product/comparator controls; all eight deployment vectors are unsupported.
The editor independently reproduced the canonical result at checkout `c929ed2`,
using only the released state/operations/query for execution, with output directed
to `.temp/astra-21/package-evaluator-021.md` and `.json` (exit 0; adjacent
`package-evaluator-021-01.log`). The judge independently reproduced both its
55/57 pre-fix report and 57/57 corrected report before closing R7-024.
Committed [canonical results](../impl-astra-23/RESULTS.md) retain exact outputs
and hashes. Supplemental `d2c38ac`: **19/19 semantic pass**, one deployment
unsupported; [report](../impl-astra-23/SUPPLEMENTAL.md). Supplemental counts are
separate from canonical counts.

Source evaluator `df499a1` preserves its first expanded 0.2.1 report:
**42 pass / 1 fail / 14 unsupported semantic**, eight deployment unsupported.
[First report](../impl-astra-22/runs/0.2.1-transactions-first.md) is retained before
correcting identity validation (R7-026). Judge also reproduced a separate
selected-sequence history defect (R7-025). Signed `26d8cc6` corrects both and
reports **43 pass / 0 fail / 14 unsupported semantic**, eight deployment
unsupported; [current report](../impl-astra-22/RESULTS.md). Independent closure
is pending. New [ASTRA25-06](../cases/astra-25-quality-budget-isolation.md)
separates premise-quality work from existence budgets: package evaluator passes,
source evaluator fails the smaller-budget query while its larger-budget control
passes. Classification is pending; the collective score remains 1/2.

## Remaining work and limits

Await exact-release judge verification, the budget-case disposition and convener PARK.
Answer any new directed package finding through the judge; no package change
is currently requested. No unsupported case is counted as a pass, and synthetic
erasure, restore, release or delivery transitions do not qualify protected
storage, authentication, timing, isolation or network behavior.

Mission constraints remain in force: Python standard library only, no installs,
web, servers, background workers, additional agents or task-board writes.
All published editor commits are signed and pushed directly to main under the
mission's explicit delivery rule. Task continuity: `.temp/tasks.md`.
