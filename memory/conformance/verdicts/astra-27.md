# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 23, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 50 items: ten rejected as defects, thirty-six fixed with independent
evidence, three open implementation bugs (R7-047/048/050), and one open
specification bug (R7-049). No owner question is established. See [LEDGER.md](../LEDGER.md) and
[R7-SCORE.md](../R7-SCORE.md).

On package 0.2.3 `23290b3`, source first expansion `36983de` exactly reproduces
canonical 49/1/7 and current supplemental 37/1/8; package `4af0360` reproduces
canonical 57/57 and supplemental 46/46. Current exact dual canonical passes are
**49/57**. Last verified full controls remain
89 at source `d077064` and 26 at package `4af0360`; new source release controls
await correction. All 47 supplemental artifacts, including one deployment vector, pass structural checks. R7-036/037 retention
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

R7-050 records incorrect source digest framing: the valid joint release refuses
in P05/ASTRA25-02. Four independently validated ASCII/non-ASCII controls prove
both directions: framed digests falsely refuse and raw digests falsely admit.
Package runtime passes the required verdicts and atomicity checks. K-JSON-2
already defines the prefix/NUL framing, so no specification or owner change
is needed. First `36983de` reports remain immutable.

Package validation and byte-exact regeneration remain verified with 32 intended
checker controls. Earlier failures, read boundaries and exact input/code hashes
are preserved. Later source adaptation is not a second package-blind run.
Eight canonical and one supplemental deployment case remain unsupported.
Continue until the convener posts PARK, then finalize this verdict and park note.
