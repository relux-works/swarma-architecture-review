# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 17, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 38 items: ten retained regressions rejected as defects, twenty-four
fixed with independent evidence, one open specification bug (R7-031) and three
open implementation bugs (R7-032/036/037). No owner question is established.
See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

On fully verified package 0.2.1 `f31d58f`, source `1f3180d` passes 44 canonical
semantic vectors, fails none and leaves 13 unsupported. Package `f10c7ba` passes
all 57. Dual coverage is **44/57**. Current 32-case supplemental semantic runs:
source 17/2/13 and package 30/2/0 (pass/fail/unsupported). R7-030 snapshot replay
and package R7-033/034 import/delivery corrections are independently closed.
Source has 58 passing controls including reused unchanged groups; package has 16.
Original failed runs and exact witnesses remain preserved.

Package 0.2.2 `7e71765` and source import candidate `1f35727` are the next review
unit, outside those pinned counts. The initial source-derived and package-only
reading boundaries remain recorded; later source adaptation is not presented as
a second package-blind run. Both evaluators leave eight canonical and one
supplemental deployment vector unsupported; no real deployment qualification is
claimed. Continue case intake, correction review and coverage verification until
the convener posts PARK, then finalize the verdict and park note.
