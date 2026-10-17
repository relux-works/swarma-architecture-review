# astra-21 package editor verdict

Status: round 4, Phase 2 active; no PARK. Review baseline: `b1ae299`.

**Released package: 0.2.1-draft at `f31d58f`. Phase 2 provisional score: 1/2;
dual canonical coverage is 43/57.** All nine editor-owned spec bugs are
judge-closed. At `b1ae299`, all 29 classified items are disposed: 21 fixed and
eight rejected, with no owner question. The original supported-vector rubric
scored 2/2; the convener explicitly requires full dual coverage for Phase 2.
The earlier score is historical evidence, not completion of the expanded gate.
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
14 product/comparator controls at `8b9baf3`; all eight deployment vectors are unsupported.
The editor independently reproduced the canonical result at checkout `c929ed2`,
using only the released state/operations/query for execution, with output directed
to `.temp/astra-21/package-evaluator-021.md` and `.json` (exit 0; adjacent
`package-evaluator-021-01.log`). The judge independently reproduced both its
55/57 pre-fix report and 57/57 corrected report before closing R7-024.
Committed [canonical results](../impl-astra-23/RESULTS.md) retain exact outputs
and hashes. Supplemental at `8b9baf3`: **22/22 semantic pass**, one deployment
unsupported; [report](../impl-astra-23/SUPPLEMENTAL.md). Supplemental counts are
separate from canonical counts.

Source evaluator `512d006` passes **43 canonical semantic vectors**, with
**14 unsupported**, and **14 supplemental semantic cases**, with **eight
unsupported**; no supported failure remains. Deployment remains eight canonical
and one supplemental unsupported. Fifty source/adapter/transaction/harness
controls pass. Judge `b1ae299` independently closed R7-025–029 and reproduced
all current report rows, hashes and declared normalized actuals. The immutable
[first transaction report](../impl-astra-22/runs/0.2.1-transactions-first.md)
remains preserved with its pre-fix failure.

At checkout `8b9baf3`, the editor independently reran source canonical and
supplemental execution against `f31d58f`, directing all output to own scratch.
Both runs exited 0; every row, hash, normalized actual and total equals committed
RESULTS.json and runs/cases-0.2.1-current.json. Evidence:
`.temp/astra-21/source-evaluator-021.md` / `.json`,
`.temp/astra-21/source-supplemental-021.md` / `.json`, and
`.temp/astra-21/source-reproduction-01.log`.

## Remaining work and limits

The convener's Phase 2 decision is event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`. Source must independently extend
B01/B07/P05/P06/P08/P12/S07/S17/S20/S23/S24/S25/S26/S27. Adversaries target those
clauses and the v0.2 delta. The editor will apply resulting judge-classified
package fixes with preserved regression controls and a versioned 0.2.x release.
No new package edit is currently requested; `f31d58f` remains the stable baseline.

Early PARK now requires source 57/57 plus one full round with no new open item;
the hard cap remains 13:00Z on 2026-10-17. Only the convener issues PARK. The exact
baseline unsupported inventory and reasons are in
`.temp/astra-21/phase2-coverage.md`. No unsupported case is counted as a pass, and synthetic
erasure, restore, release or delivery transitions do not qualify protected
storage, authentication, timing, isolation or network behavior.

Mission constraints remain in force: Python standard library only, no installs,
web, servers, background workers, additional agents or task-board writes.
All published editor commits are signed and pushed directly to main under the
mission's explicit delivery rule. Task continuity: `.temp/tasks.md`.
