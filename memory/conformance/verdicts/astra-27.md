# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 33, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 57 items: ten rejected as defects, forty-five independently fixed,
one open implementation bug (R7-057), and one owner question (R7-055).
See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Both readers independently reproduce **57/57 canonical semantic passes** on
unchanged release 0.2.5 `6a04e8c`. The current supplemental corpus has 63 semantic
vectors: source 61/2/0, package 63/0/0. Source runtime is `87beb46`;
package runtime is `23b4d74`. Canonical report rows, input/module hashes and actuals
match committed evidence after only declared fresh-handle normalization. Supplemental
first results preserve the two new failures alongside the unchanged older cases.
All 64 supplemental artifacts validate; the final twenty author migrations at
`27303e4` change only profile stamps and reverse exactly to the original bytes.

R7-053 package expiry closes at `23b4d74`. All 31 product/comparer controls pass,
and ten independent operation checks give three positive admissions and seven
exact atomic deadline refusals, preserving original receipts. All four write
APIs and current original closure/replay use strict trusted-time expiry before
idempotency. Source R7-052 remains fixed at `4a14a56`. First failures are retained.

R7-056 recovery closes at `87beb46`. Independent full canonical/supplemental
execution reproduces all committed rows and input/module hashes. All 125 source
native/comparer controls pass, along with the unchanged original recovery witness,
four public-state transitions and two exact atomic authorization negatives.
Only public/runtime availability facts change; original failures remain retained.
The erasure/restore/load coverage introduced at `dbf4892` stays verified.

R7-057 is a separate source erase-context defect. Original native `0529814` and
judge probes validate and reproduce changed ungranted receipt purpose/audience:
source returns not_authorized instead of idempotency_conflict,false. K-API-1 and
K-ERASE-2 distinguish changed canonical intent from exact receipt replay. Current
erase authority still precedes conflict; exact replay still needs current metadata
permission. Both readers pass the live exact-replay, revoked-metadata, revoked-
erase-authority and fresh-key empty-ref neighbors, with full refusal state and
original receipt preserved. Package `23b4d74` gives the required changed-intent
conflicts. Source correction is authorized; no new owner or canonical oracle
choice is needed. Signed `66233ab` adds exact purpose/audience regression fixtures
using the original native state. Judge full runs reproduce only two source refusal-code differences;
all 61 older cases remain passing and unchanged. The bug keeps the score at 1/2.

R7-055 is a source ambiguity about whether an H1 canonical edge endorses an H2
predecessor's transitive ordering. The native pair at `4424598` validates and
independently reproduces source ambiguous d1/d3 versus package current d3; its
same-H1 control agrees. Precise choices and tradeoffs are filed in
[OWNER-QUESTIONS.md](../OWNER-QUESTIONS.md) and `q-authority-issuer`. The convener
holds the question for Ivan; no attributed owner decision exists. No exact oracle,
new implementation verdict or denominator entry is inferred.

The specification has no open finding, with exact regeneration of 94 JSON
artifacts and 34 intended checker controls. Eight canonical plus one supplemental
deployment case remain unsupported. Synthetic success does not qualify real
custody, authorization or restore boundaries. Later source adaptation is not
another package-blind run. Continue until the convener posts PARK, then finalize
this verdict and park note.
