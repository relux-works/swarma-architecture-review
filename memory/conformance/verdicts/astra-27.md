# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 26, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 54 items: ten rejected as defects, forty-one independently fixed,
two open implementation bugs (R7-052/053) and one open specification bug (R7-054).
No owner question is established. See [LEDGER.md](../LEDGER.md) and
[R7-SCORE.md](../R7-SCORE.md).

On verified package 0.2.4 `ef02647`, source `427fed5` gives canonical 50/0/7
and package `942bdee` gives 57/0/0. Exact dual canonical passes are **50/57**.
The current 54-case semantic supplement gives source 46/0/8 and package 54/0/0.
All 55 supplemental artifacts validate; explicit author profile migrations preserve
every original semantic expectation. All four independent reports match producer
rows/input hashes after declared normalization, with exact runtime module hashes.

R7-048 package strict succession and R7-051 source receipt-only projection close.
Expanded B01, original forbidden successor inputs, transitive positive and the
read-only ancestry pair now pass. All 106 source and 28 package controls were
rerun successfully. Negative controls preserve complete state; direct/transitive,
plain-import, replay and CAS neighbors retain their distinct required outcomes.
Long ancestry, candidate eligibility and genuine incomparability are covered.
Original failures and explicit fixture setup maintenance remain preserved.

Retention-deadline findings R7-052/053 and exact mapping R7-054 remain open.
Original native probes show fresh writes and successful replay at/after expiry;
they remain outside vector totals until the exact release and case vectors land.
The mapped non-retryable not_authorized refusal belongs before idempotency and
must preserve original receipts and full state, without an erasure side effect.

Package validation and byte-exact regeneration remain verified with 33 intended
checker controls. Seven canonical source coverage gaps remain. Eight canonical
plus one supplemental deployment case are unsupported. Later source adaptation is
not another package-blind run. Continue until the convener posts PARK, then finalize
this verdict and the park note.
