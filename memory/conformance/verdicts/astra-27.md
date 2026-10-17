# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 24, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 51 items: ten rejected as defects, thirty-seven fixed with independent
evidence, three open implementation bugs (R7-047/048/051), and one open
specification bug (R7-049). No owner question is established. See
[LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

On package 0.2.3 `23290b3`, source `8a42945` exactly reproduces canonical 50/0/7;
package `4af0360` remains verified at 57/57. Exact dual canonical passes are
**50/57**. All 98 source controls were rerun; 26 package controls remain verified.
R7-050 digest framing closes with exact P05/ASTRA25-02 and independent framed/raw
ASCII/non-ASCII positive and atomic-negative controls. First reports and the
producer's excluded test-setup failure remain explicit.

The expanded 52-semantic-case supplement gives source 40/4/8 and package 49/3/0.
All 53 artifacts, including one deployment case, validate. Both runtimes fail the
three forbidden successor replacements, tracked as R7-047/048. R7-049 requires
the adjudicated non-retryable authority_receipt_required mapping in the package.
Source alone also fails transitive successor projection through an admitted
receipt-only intermediate event. Fresh read-only snapshots independently isolate
this as R7-051: source direct control and both package reads pass; semantic state
is unchanged. Earlier CAS and digest closures remain separate.

Package validation and byte-exact regeneration remain verified with 32 intended
checker controls. Original failures, read boundaries and exact input/code hashes
are preserved. Later source adaptation is not a second package-blind run.
Seven canonical source gaps and eight canonical plus one supplemental unsupported
deployment case remain. Continue until the convener posts PARK, then finalize
this verdict and the park note.
