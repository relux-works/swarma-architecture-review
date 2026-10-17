# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 27, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 54 items: ten rejected as defects, forty-one independently fixed,
two open implementation bugs (R7-052/053) and one open specification bug (R7-054).
No owner question is established. See [LEDGER.md](../LEDGER.md) and
[R7-SCORE.md](../R7-SCORE.md).

On verified package 0.2.4 `ef02647`, source `427fed5` gives canonical 50/0/7
and package `942bdee` gives 57/0/0. Exact dual canonical passes are **50/57**.
The expanded 61-case semantic supplement gives source 48/5/8 and package 56/5/0.
All 62 artifacts validate. The previous 54 semantic inputs and outputs remain
unchanged after declared normalization. Seven exact expiry vectors add two
positive passes and five failures in each implementation; their original bytes
are frozen and the native first evidence is unchanged.

R7-048 package strict succession and R7-051 source receipt-only projection close.
Expanded B01, original forbidden successor inputs, transitive positive and the
read-only ancestry pair now pass. All 106 source and 28 package controls were
rerun successfully. Negative controls preserve complete state; direct/transitive,
plain-import, replay and CAS neighbors retain their distinct required outcomes.
Long ancestry, candidate eligibility and genuine incomparability are covered.
Original failures and explicit fixture setup maintenance remain preserved.

Retention-deadline findings R7-052/053 and exact mapping R7-054 remain open.
Independent per-operation controls now reproduce three positive passes and seven
forbidden successes in each runtime, including both batch orders, unknown-lineage
known ancestry and expired replay. Full state is preserved in the evidence;
returning an unauthorized success remains wrong even without a state mutation.
These probes supplement the seven exact vectors under the adjudicated mapping;
the normal package clarification and corrections remain pending.
The mapped non-retryable not_authorized refusal belongs before idempotency and
must preserve original receipts and full state, without an erasure side effect.

Package validation and byte-exact regeneration remain verified with 33 intended
checker controls. Seven canonical source coverage gaps remain. Eight canonical
plus one supplemental deployment case are unsupported. Later source adaptation is
not another package-blind run. Continue until the convener posts PARK, then finalize
this verdict and the park note.
