# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 19, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 43 items: ten retained regressions rejected as defects, twenty-six
fixed with independent evidence, two open specification bugs (R7-039/042) and
five open implementation bugs (R7-036/037/040/041/043). No owner question is
established. See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Package 0.2.2 `7e71765` validates and regenerates exactly. R7-031 closes with
runtime `a016781`: canonical 57/57, eighteen controls and all three receipt-scope
cases pass independently, preserving full erasure closure and exact authorized
replay. Source `e38c37c` exactly reproduces 47 canonical passes, zero failures and
ten unsupported; B01/S17 and 67 source controls pass. Verified dual coverage is
**47/57**. This does not establish complete invalidation correctness: judge's
rule/certificate withdrawal probes expose R7-043 despite passing existing controls.

All 38 supplemental semantic fixtures now have the current closed shape, with
one independently confirmed checker false positive for future integration inputs.
Execution gives source 24/3/11 and package 35/3/0 (pass/fail/unsupported). Additional
judge invalidation probes give source 1/2/0 and package 3/0/0. Known retention and
CAS defects remain independently tracked; all first failures and original read
boundaries remain preserved. Pending 0.2.3 is not counted as delivered.

Later source adaptation is not a second package-blind run. Eight canonical and
one supplemental deployment case remain unsupported. Continue intake, correction
review and coverage verification until the convener posts PARK, then finalize
this verdict and the park note.
