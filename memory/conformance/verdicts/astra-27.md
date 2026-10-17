# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 25, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 54 items: ten rejected as defects, thirty-nine independently fixed,
four open implementation bugs (R7-048/051/052/053) and one open specification
bug (R7-054). No owner question is established. See [LEDGER.md](../LEDGER.md)
and [R7-SCORE.md](../R7-SCORE.md).

Verified package 0.2.4 `ef02647` closes R7-049: strict canonical succession has
an exact non-retryable authority_receipt_required refusal, distinct from CAS and
currently authorized replay. All 94 JSON artifacts regenerate identically;
33 structural plants detect intended violations. Only B01 changes beyond profile
stamps. The other 64 vectors and original pilot are unchanged.

Source `4772258` closes R7-047. Independent original 0.2.3 runs reproduce canonical
50/0/7 and supplement 44/2/8 across 54 semantic cases. Four new succession groups
and fourteen old transaction groups pass, including full-state negative checks
and direct/transitive/plain-import/replay positives. All 55 original supplemental
artifacts validate. Package `4af0360` gives 51/3/0 on those exact cases. Unexpected
fresh handles on two failing extra-item outputs remain raw and explicitly noted;
they are not normalized into false report equality.

On expanded 0.2.4, independent canonical results are source 49/1/7 and package
56/1/0: exact dual passes **49/57**. Source matches every B01 operation and
postcondition; seven final-view differences are the separate R7-051 projection
failure. Package still fails strict succession under R7-048. ASTRA24-11 independently
isolates the source receipt-only ancestry defect without a preceding write.

ASTRA25-11 establishes deadline findings R7-052/053 and mapping gap R7-054.
Both runtimes admit fresh bytes at/after inherited or own expiry and return a
successful exact replay after expiry. All five original native inputs validate;
before-expiry success is preserved. Required not_authorized,false belongs to
current retention authority before idempotency, including original-output/known-
input closure on replay. Denial must preserve state and the original receipt;
it does not initiate physical erasure. These native probes remain outside vector
totals pending exact author vectors and the package clarification.

Seven canonical source coverage gaps remain. Eight canonical plus one supplemental
deployment case are unsupported. Original first runs remain immutable; later source
adaptation is not another package-blind run. Continue until the convener posts PARK,
then finalize this verdict and the park note.
