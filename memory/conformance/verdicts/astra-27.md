# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 28, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 54 items: ten rejected as defects, forty-two independently fixed,
and two open implementation bugs (R7-052/053). No owner question is established.
See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Verified package 0.2.5 `6a04e8c` closes expiry mapping R7-054. Live retention
requires trusted intake time strictly before every applicable non-null deadline.
The exact non-retryable not_authorized refusal precedes idempotency and checks
original outputs/known-input closure on replay, preserving state and old receipts
without a purge. All 94 JSON artifacts regenerate exactly and all 34 checker
plants detect their intended violation. Only P11 changes beyond profile stamps;
its first 16 operations/results, the other 64 vectors and pilot are unchanged.

Independent full first runs give source `427fed5` 49/1/7 and package `942bdee`
56/1/0: exact dual canonical passes **49/57**. Only expanded P11 fails. Eight
isolated package probes reproduce five forbidden fresh commits, two expired
success replays and one wrong idempotency-conflict priority. A separate prescribed
20-operation positive trace passes every field; it excludes the eight expired
operations and is not full conformance evidence.

The pinned 61-case semantic supplement under 0.2.4 plus adjudicated expiry mapping
is source 48/5/8 and package 56/5/0. All 62 artifacts validate; prior 54 semantic
inputs/results and all original first evidence remain unchanged. Explicit author
migration to 0.2.5 and runtime corrections remain pending. R7-052/053 closure
requires all admission APIs, current replay, transitive/incomplete-known and
same-batch expiry, live/null positives and complete unchanged refusal state.

Authority-order fixes and their 106 source/28 package control baseline remain
verified on 0.2.4; those results do not prove the new expiry contract. Seven
canonical source gaps and eight canonical plus one supplemental deployment case
remain unsupported. Later source adaptation is not another package-blind run.
Continue until the convener posts PARK, then finalize this verdict and park note.
