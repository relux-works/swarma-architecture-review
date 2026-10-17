# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 31, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 56 items: ten rejected as defects, forty-four independently fixed,
one open implementation bug (R7-056), and one owner question (R7-055).
See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Both readers now independently reproduce **57/57 canonical and 61/61 supplemental
semantic passes** on unchanged release 0.2.5 `6a04e8c`. Source runtime is `dbf4892`;
package runtime is `23b4d74`. Complete report rows, input/module hashes and actuals
match their committed evidence after only declared fresh-handle normalization.
All 62 supplemental artifacts validate; the final twenty author migrations at
`27303e4` change only profile stamps and reverse exactly to the original bytes.

R7-053 package expiry closes at `23b4d74`. All 31 product/comparer controls pass,
and ten independent operation checks give three positive admissions and seven
exact atomic deadline refusals, preserving original receipts. All four write
APIs and current original closure/replay use strict trusted-time expiry before
idempotency. Source R7-052 remains fixed at `4a14a56`. First failures are retained.

The source's erasure/restore/load mapping fills all seven former coverage gaps.
Eight new erasure groups and four availability/control groups pass alongside prior
controls, for 124 passing controls including the comparison harness. The added
125th control exposes R7-056: an initially degraded public state acknowledges an
owner's available transition but remains unavailable. Judge reproduction validates
all inputs, isolates that failure among four public-state transitions and verifies
two exact atomic authorization refusals. The native bug remains open despite full
vector success; correction is authorized without changing any canonical oracle.

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
