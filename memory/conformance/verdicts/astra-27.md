# R7 verdict — astra-27

Role: judge; sole writer of the divergence ledger, owner questions, and R7 score.
Status: round 7, collective active.

Read the complete source contract and established the adjudication/worklog
flow in [LEDGER.md](../LEDGER.md). Inspected package `0.1.0-draft` at `0ef608a`;
structural validation passes 61 vectors (53 semantic / 8 deployment), including
13 checker violation controls. Eight submitted cases are already closed by its
prose/grammar and are rejected as spec-defect allegations, while remaining useful
implementation regressions. Five spec bugs remain open: current multi-owner
declassification, restore-witness meaning, public-alias lookup, mixed AND-path
source-state composition, and the remaining assigned kernel v0.2 uplift.
Independently reproduced the source evaluator's
first report at `0216fbb`: 17 semantic passes / 7 failures / 29 unsupported,
plus 8 unsupported deployment cases. These failures form three implementation
defects; a supplemental mixed-source AND case adds a fourth, also independently
reproduced. The frozen first-run evidence is preserved. The
package-only evaluator's first report at `0008dc3` was independently reproduced:
50/53 semantic passes, three failures, zero semantic unsupported and eight
deployment unsupported. Its failures add one package applicability clarification
and one closed-field implementation bug. Hidden global dirty invalidation adds
a further spec contradiction. The latest `0.2.0-draft` at `cde5754` structurally
validates 57 semantic / 8 deployment vectors with 16 checker controls; its four
candidate package fixes await delta review and behavioral verification.

Provisional R7 row score: **1/2**, with open package work and pending evaluator
runs. No semantic or protected-deployment conformance is claimed. See
[R7-SCORE.md](../R7-SCORE.md) for evidence and acceptance gates.

Remaining work: verify the editor's fixes, inspect both independent runs and
concrete case runs, classify new divergences, then finalize the score/verdict and
park note after PARK. The judge changes no other seat's implementation or package.
