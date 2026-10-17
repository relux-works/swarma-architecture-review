# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 20, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 46 items: ten rejected as defects, twenty-seven fixed with independent
evidence, two open specification bugs (R7-039/042) and seven open implementation
bugs (R7-036/037/040/043/044/045/046). No owner question is established.
See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

On package 0.2.2 `7e71765`, source `68152c5` exactly reproduces 49 canonical
passes, zero failures and eight unsupported; package `53266dd` exactly reproduces
57/57. Verified dual coverage is **49/57**. Source established controls total 77
with unchanged groups reused; package has 19. Delivery expansion P06/P12 passes.
Package CAS R7-041 closes; source CAS R7-040 remains open on a valid remaining-head
counterexample despite passing the original four cases. Rule/certificate dirty
invalidation remains independently open as R7-043.

Current 43 semantic supplemental cases give source 33/1/9 and package 39/4/0.
Additional judge native/invalidation probes are outside that denominator. Missing
exact import checks, transitive registered review and ungranted delivery actor
are separate package defects. Future-input checker and retention scope await
0.2.3. All first failures, input hashes, explicit fixture migrations, corrected
setup failures and original read boundaries remain recorded.

Later source adaptation is not a second package-blind run. Eight canonical and
one supplemental deployment case remain unsupported. Continue review until the
convener posts PARK, then finalize this verdict and the park note.
