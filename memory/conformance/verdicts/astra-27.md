# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 21, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 46 items: ten rejected as defects, thirty-three fixed with independent
evidence, and three open implementation bugs (R7-036/037/046). No specification
bug or owner question is open. See [LEDGER.md](../LEDGER.md) and
[R7-SCORE.md](../R7-SCORE.md).

Package 0.2.3 `23290b3` validates with 32 intended checker controls and regenerates
all 94 JSON artifacts exactly. Explicit retention scope and deferred future-input
validation close R7-039/042. Independent positive and negative checker controls
retain actual admitted-input integrity. Only P11/P13 expected reports change
beyond profile stamps, and their isolated authorized traces pass every field.
Current full canonical runs remain red: source 47/2/8 and package 55/2/0; both
fail P11/P13. Exact current dual passes are **47/57**, with 49 source vectors
implemented. Missing retention enforcement remains R7-036/037.

Frozen 0.2.2 verification separately closes source CAS continuation R7-040,
source rule/certificate invalidation R7-043, package exact-import coverage R7-044,
and package transitive review R7-045. Source `99b5a85` reproduces 49/0/8 and
package `f6c339d` reproduces 57/0/0. The 44-case semantic supplement gives source
34/1/9 and package 42/2/0. Source established controls total 81, with unchanged
groups reused; all 22 package controls were rerun. R7-046 actor correction
`3ce8ee3` and current supplemental migration/retention variants are queued next.

Original first failures, read boundaries, exact input/code hashes and explicitly
excluded setup failures remain preserved. Later source adaptation is not a
second package-blind run. Eight canonical and one supplemental deployment case
remain unsupported. Continue until the convener posts PARK, then finalize this
verdict and the park note.
