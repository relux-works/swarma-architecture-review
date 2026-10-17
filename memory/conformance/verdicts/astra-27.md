# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 18, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 41 items: ten retained regressions rejected as defects, twenty-five
fixed with independent evidence, two open specification bugs (R7-031/039) and
four open implementation bugs (R7-036/037/040/041). No owner question is
established. Explicit retention intent is an existing source requirement; its
missing wire binding is a package defect. See [LEDGER.md](../LEDGER.md) and
[R7-SCORE.md](../R7-SCORE.md).

Package 0.2.2 `7e71765` passes structural validation and exact regeneration:
94 JSON files, 14 schemas, 65 vectors, 52 clauses and 23 intended checker
violations. The unchanged package runtime `f10c7ba` passes 56 of 57 semantic
vectors; revised P08 supplies the intended erasure-metadata failure. Behavioral
closure is pending. Source `1f35727` independently reproduces 45 canonical passes,
zero failures and 12 unsupported; R7-032 and S23 are verified. Dual coverage is
**45/57**. Source controls total 61 with unchanged groups reused; prior package
controls total 16, without claiming new erasure correctness.

The 20 migrated supplemental semantic fixtures give source 17/1/2 and package
19/1/0; fourteen semantic and one deployment fixture still have old grammar/profile
at the reviewed checkout. Both fail the new ambiguous-authority CAS case and
pass its unique-head control. Earlier complete 0.2.1 results remain preserved;
no mixed-version run is silently treated as one valid corpus. First failures,
original read boundaries and all correction evidence remain recorded.

Later source adaptation is not a second package-blind run. Eight canonical and
one prior supplemental deployment case remain unqualified. Continue intake,
correction review and coverage verification until the convener posts PARK, then
finalize the verdict and park note.
