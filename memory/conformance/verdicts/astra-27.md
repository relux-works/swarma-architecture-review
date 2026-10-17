# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 22, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 49 items: ten rejected as defects, thirty-six fixed with independent
evidence, two open implementation bugs (R7-047/048), and one open specification
bug (R7-049). No owner question is established. See [LEDGER.md](../LEDGER.md) and
[R7-SCORE.md](../R7-SCORE.md).

On package 0.2.3 `23290b3`, source `d077064` exactly reproduces canonical49/0/8
and current supplemental37/0/9; package `4af0360` reproduces canonical57/57 and
supplemental46/46. Current exact dual canonical passes are **49/57**. All 89
source controls and 26 package controls pass. All 47 supplemental artifacts,
including one deployment vector, pass structural checks. R7-036/037 retention
and R7-046 delivery actor close on exact witnesses and full state-preservation
controls, with original failures retained.

ASTRA24-10 adds two independently reproduced forbidden replacement variants:
incomparable and reused authority receipts each commit records, cut, dirty state
and a replay entry in both runtimes. The ordered positive succeeds. These three
validated native probes are outside the exact-vector denominator. K-REV-3
requires strict authority succession independently of correct CAS head selection;
R7-047/048 track the runtime corrections, and R7-049 requires the precise
`authority_receipt_required` non-retryable mapping and a package regression.
This is a package clarification under the existing design, not an owner choice.

Package validation and byte-exact regeneration remain verified with 32 intended
checker controls. Earlier failures, read boundaries and exact input/code hashes
are preserved. Later source adaptation is not a second package-blind run.
Eight canonical and one supplemental deployment case remain unsupported.
Continue until the convener posts PARK, then finalize this verdict and park note.
