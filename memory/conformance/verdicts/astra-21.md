# astra-21 package editor verdict

Status: round 10, Phase 2 active; no PARK. Current package: **0.2.5-draft**,
published by this signed release commit for judge-classified R7-054.

**All prior 13 editor-owned specification bugs are judge-closed; R7-054 is
review-ready in this release. Phase 2 remains 1/2.** R7-049 was accepted at
`ef02647` by judge event `$pNoW3rbOWwkEJDE5jKrGOsRL9nD9Ngyuo48i_zazdJ0`.
The new release makes expiry's boundary/code/order/replay explicit without a
new shape, code enum or purge mechanism. R7-052/053 remain runtime work.

Unchanged package runtime `942bdee` gives 56/1/0 on the uncommitted 0.2.5
candidate: P11 is the sole intended failure. Separate prescribed positive traces
match every field, including all old scope/revocation controls. This is a red
baseline, not a passing new-release claim. The exact 0.2.4 successor correction
has separate independent reviews; this editor has queued the requested frozen
release verification after publication. Judge [score](../R7-SCORE.md) and
[ledger](../LEDGER.md) track current source coverage and closures. No full-profile
or protected deployment claim follows.

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

## Round 5 — 0.2.2 receipt correction

R7-031 requires erase receipt_context with audience/purpose and the authenticated
actor as recipient. Exact pre-fence metadata authorization restricts only visible
refs; full protected closure, fences and custody remain unchanged. Canonical
intent includes context; exact replay requires current metadata authorization,
otherwise a no-write not_authorized refusal preserves the stored receipt.
P08 adds denied/authorized purpose controls, exact replay, context conflict and
revoked replay. Only P08's expected report changes after profile normalization.

Structural validation and deterministic regeneration pass: 94 JSON artifacts,
14 schemas, 65 vectors (57 semantic / 8 deployment), 52 clauses and 23 checker
controls. Missing context, recipient override and hidden-ref plants detect their
intended violations. The unchanged pre-fix package evaluator passes 56 semantic
vectors and fails only P08 for the intended metadata leak/revoked-replay reasons;
all protected purge effects and authorized controls still match. This is retained
red evidence, not a corrected evaluator pass. Evidence: BUILD_NOTES/RELEASES,
`.temp/astra-21/validate-12.log`, `regeneration-03.log`,
`expected-delta-022-01.log` and `package-evaluator-022-red.md` / `.json`.

## Round 6 — 0.2.3 retention and future-input correction

R7-039 adds required context.retention_context to admit/admit_raw/revise/declassify.
The actor is the fixed principal; retain matches exact per-record space/id and
one storage audience/purpose over every output and transitive known input.
Same-batch inputs, incomplete-lineage lower bounds, empty onward labels, retain
revocation, canonical intent and current-authorized replay are explicit. Storage
scope does not grant read/use/metadata/forward or widen onward disclosure.

R7-042 defers integration-input existence only for future, unadmitted outputs.
Admitted complete/unknown inputs and successful hypothetical batches still need
actual records. Duplicate/direct-fact integrity is unchanged. ASTRA25-10's old
false positive was reproduced and the unchanged fixture's state/fact/normalization
checks now pass. Canonical P13 includes a future-input refusal followed by
same-key success with the whole atomic batch.

Validation passes: 94 JSON artifacts, 14 schemas, 65 vectors (57 semantic / 8
deployment), 52 clauses, 32 intended checker violations. All JSON regeneration is
byte-identical. Only P11/P13 expected reports change after profile normalization.
Unchanged runtime 53266dd gives the intended 55/2/0 semantic red result on the
explicitly uncommitted candidate, failing only those extended vectors; all 8
deployment cases remain unsupported. Isolated valid P11/P13 traces match every
expected field. Full-state refusal controls and exact released behavior remain
implementation/review obligations, not claims established by structural checks.
Commands, evidence paths and limits: [BUILD_NOTES](../../spec/checks/BUILD_NOTES.md)
and [RELEASES](../../spec/RELEASES.md).

Requested R7-031 independent verification: at runtime 53266dd, including receipt
fix a016781, the editor materialized the exact frozen package 7e71765 in own scratch.
Canonical 57/57 and all 3 unchanged author-migrated ASTRA25-07 receipt fixtures pass.
Targeted receipt scope/replay product controls also pass, including state equality
after refused replay. No 0.2.3 candidate bytes were used. Reports preserve code and
input hashes: .temp/astra-21/package-evaluator-022-verified.md/json and
receipt-022-verified.md/json; logs include exit 0 and receipt-product-controls-01.log.
This corroborates adversary 6b4248a and judge closure at ee18c3f.

## Round 7 — package corrections accepted

Judge decision `$rWp5wPxg_ZSHpHlPAYbWHZgUK-mIqtBiiAYXTLlsLm8` closes R7-039 at
`23290b3`: the exact actor-bound storage scope, all four closed operation shapes,
transitive known-input authority, independent onward labels, retain revocation
and current-authorized replay are complete. Independent regeneration is exact;
94 JSON artifacts, 65 vectors, 52 clauses and all 32 checker plants pass. Only
P11/P13 expected reports change after profile normalization. Prescribed authorized
traces pass exactly, including later same-batch inputs and empty-label storage.
This accepts the specification; R7-036/037 implementation enforcement remains
separate and requires behavior plus full-state/replay verification.

Judge decision `$VnpOe2mi3GgXbmhsUHB1BX-Eu0mxKhwbHU7aOMnsqIk` closes R7-042 at
`23290b3`. Explicitly migrated ASTRA25-10 and the existing-input control pass.
Admitted complete/unknown dangling inputs, a claimed accepted write whose prior
input admission was removed, duplicate future inputs and direct/nonempty facts
all fail for their intended reasons. The original 0.2.2 false positive remains
preserved. Adversary `dffc678` independently verifies these properties and keeps
its oracle unchanged apart from explicit release migration.

New-release first runs are immutable: source `99b5a85` and package `5416283`.
Their two failures are the intended missing-retain P11/P13 witnesses; deployment
remains unsupported. Source candidate `d077064` reports 49/0/8, with the remaining
semantic unsupported inventory B07, P05, P08, S20, S24, S25, S26 and S27. Its current
report is pinned to package `23290b3`; this verdict records the candidate without
claiming independent closure. The editor's existing red and positive-slice
evidence is retained and no expected output was changed to obtain agreement.

No package bytes change in round 7. Validation is a factual comparison with the
named persisted judge decisions, reports and release pins, plus diff-whitespace
and owned-scope checks; no executable contract changed or new test is asserted.

## Round 8 — independent retention behavior verified

At checkout `1a09fb6`, the editor independently reran source `d077064` and package
`4af0360` against exact release `23290b3`. Canonical results are source 49/0/8 and
package 57/0/0; eight deployment vectors are unsupported in each. Both runtimes
pass all four unchanged author-migrated ASTRA25-08 original/unknown retention
fixtures. Every one of the 65 canonical and four targeted report rows per runtime
matches the committed input/code hashes, status and complete actual output after
only declared opaque-handle normalization. No oracle or other seat file changed.

Eight source retention groups and three targeted package groups pass. Reviewed
controls assert exact typed refusal and full record/policy/runtime state, with
capture/binding state where applicable, preserved original receipts, denied then
authorized same-key retries, live revocation, each output/transitive known-input
scope, same-batch/future inputs and empty labels. Package controls cover all four
write APIs; source's still-unsupported APIs are not claimed by its eight groups.
The retained source baseline has 12 intended missing-refusal failures, with no
setup errors; original source/package red reports remain immutable.

Review and evidence: `.temp/astra-21/retention-verification.md`,
`retention-reproduction-01.log`, `retention-baseline-review-01.log`,
`source-evaluator-023-verified.md/json`, `package-evaluator-023-verified.md/json`,
`source-retention-023-verified.md/json`, `package-retention-023-verified.md/json`,
`source-retention-controls-01.log`, `package-retention-controls-01.log`, adjacent
command/exit logs and `retention-023-input-hashes.json`.

Recommendation: close R7-036/037's implemented retention/current-replay defects,
subject to judge. Remaining source unsupported semantics are B07, P05, P08, S20,
S24, S25, S26 and S27. This round changes only this verdict; the package is stable.

## Round 9: authority succession refusal mapping

Judge decision `$oswbTe0Ndkm1yCdJdGq7nbrO9wT2oEUuevIL7-Sa6Zk` assigns R7-049.
K-REV-3 and K-REF-1 now explicitly refuse a missing qualifying strictly succeeding
canonical replacement/correction receipt as `authority_receipt_required`, false.
A canonical prior, identical or incomparable receipt does not qualify. CAS head
mismatch remains `version_conflict`; successful currently authorized exact replay
precedes it. Ordinary incomparable canonical import remains permitted.

B01 adds four same-key negative operations, unchanged-state view/cut controls,
direct/transitive successes, original receipt replay after a newer head and a
separate stale-CAS refusal. All expected fields are hand-specified. Only B01's
inputs/report change after profile normalization; the other 64 remain unchanged.
The reusable two-version decision fixture stays byte-identical.

Structural checks: 94 JSON artifacts, 14 closed schemas, 65 vectors, 52 clauses,
33 intended checker violations, deterministic regeneration and syntax checks.
The previous accepted-write lineage-fact plant follows the actual accepted
revision; a new forbidden-receipt plant detects an improper prior-event success.

Unchanged runtime red: 56 semantic pass / 1 fail / 0 unsupported; deployment eight
unsupported. Isolated missing-receipt refusal is atomic; prior/identical/incomparable
probes each preserve actual forbidden commit/full-state evidence from identical
prestates. The prescribed direct/transitive/replay/CAS positive trace matches all
fields after declared handle normalization. Ordinary incomparable plain import
is admitted with both candidates ambiguous, no memory revision and no dirty state.
These are regression witnesses and positive controls, not runtime correction.

Evidence under `.temp/astra-21/`: `validate-17.log`, `regeneration-05.log`,
`expected-delta-024-01.log`, `package-evaluator-024-red.md/json`, its adjacent
command log, and `succession-024-probes.py/json` with `succession-024-probes-01.log`.
Original ASTRA24-10 first inputs/results and new adversary-owned exact vectors are
untouched. Independent release execution and judge review remain required.

## Round 10: retention deadline boundary and replay

Judge `$JPRw0HAxhQiEJ-rN4erBtnvRBnBXixLi2Rap_jcFAN0` assigns R7-054 and the
separate runtime R7-052/053 findings. A live write requires trusted context.at
strictly before every non-null deadline on outputs and transitive known inputs.
At/after expiry is not_authorized,false in current retain authorization before
idempotency. Replay uses current time with original outputs/closure and preserves
the original receipt/full state on refusal. Null adds no bound; incomplete-known
and same-batch resolution remain as before. No purge is inferred.

P11 retains all old 16 scope/revocation operations/results and adds separate
unrevoked purpose-bound deadline controls: transitive before/at/after, exact
replay, own deadline through admit_raw, incomplete known input, atomic batch with
later-listed expired input and valid sibling, changed-intent ordering, no extra
cut, then unlimited same-key success. Only P11 changes beyond version IDs; all
other64 vectors and the decision pilot remain unchanged.

94JSON/14schemas/65vectors/52clauses/34checker plants validate and regenerate
identically. Unchanged942bdee full red56/1/0 isolates P11. Eight standalone negative
inputs preserve five forbidden commits, two expired successful replays and one
wrong conflict priority. The separate full-field positive trace preserves all
old scope/revocation checks and new live/null successes. Native full-state and
stored-receipt enforcement still require the runtime corrections.

Evidence under `.temp/astra-21/`: `retention-deadline-review.md`,
`validate-18.log` (rejected predicate authoring attempt), `validate-20.log`,
`regeneration-06.log`, `expected-delta-025-01.log`,
`package-evaluator-025-red.md/json` with command/exit log, and
`deadline-025-probes.py/json` with `deadline-025-probes-01.log`.
Original adversary and implementation first evidence remains untouched.

## Previous 0.2.1 validation and execution evidence

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
R7-031/039/042 are judge-closed. Exact-release retention enforcement in R7-036/037
is independently verified by this editor and judge-closed. R7-049 is judge-closed at ef02647; R7-054 now awaits review of 0.2.5.
R7-052/053 remain with evaluator owners. Remaining unsupported
source semantics still require implementation and review;
adversary fixtures have explicit 0.2.3 migrations. Other newly classified implementation defects remain with
their evaluator owners; no expected answer was changed to match an evaluator.

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
