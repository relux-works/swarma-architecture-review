# astra-25: disclosure and erasure verdict

Status: phase 2, round 24; collective active, NO PARK. Seat identity:
`ivmbp_swarma-memory_astra-25`.

**Current phase-2 score: 1/2.** Full dual semantic coverage and new finding
closure remain incomplete. The prior 2/2 at judge `b1ae299` used the original
supported-vector rubric; it was never a claim that both evaluators passed all 57.

## Seat output and dispositions

Eleven case documents and twenty-seven exact fixtures (twenty-six semantic, one deployment)
are published. All initial source readings and later failures remain in git and
[`astra-25-evaluator-results.json`](../cases/astra-25-evaluator-results.json).

| Case | Contract | Disposition |
| --- | --- | --- |
| [ASTRA25-01](../cases/astra-25-hidden-premise-quality.md) | Hidden opposition cannot taint public quality or budget | R7-005 rejected as spec defect; regression retained; later visible-control accounting fixed under R7-027 |
| [ASTRA25-02](../cases/astra-25-declassification-intersection.md) | Every constrained owner's live exact release applies | R7-006 fixed@cde5754; R7-050 fixed@8a42945; both digest directions, P05 and nine release groups independently pass |
| [ASTRA25-03](../cases/astra-25-surviving-support-erasure.md) | Surviving support does not preserve tainted bytes or close incomplete custody | R7-007 rejected as spec defect; incomplete/complete custody and current-generation fence regressions retained |
| [ASTRA25-04](../cases/astra-25-stale-restore-witness.md) | External witness must be current and complete | R7-008 fixed@cde5754 for fixture meaning; real deployment remains unsupported |
| [ASTRA25-05](../cases/astra-25-hidden-dirty-invalidation.md) | Hidden revision cannot expose protected global dirty state | R7-018 fixed@f31d58f; hidden and authorized-dirty traces pass |
| [ASTRA25-06](../cases/astra-25-quality-budget-isolation.md) | Opposite quality cannot spend existence counters | R7-027 fixed@4e647ea; both owned traces and ASTRA24-05 controls pass |
| [ASTRA25-07](../cases/astra-25-erasure-receipt-metadata.md) | Erase authority does not grant hidden derivative metadata | R7-031 fixed at package 7e71765 / runtime a016781; judge and seat independently verified |
| [ASTRA25-08](../cases/astra-25-retention-authority.md) | Admit/read/use do not silently supply retain | R7-036 source d077064 / R7-037 package 4af0360 independently verified and judge-closed at 7446ba5 |
| [ASTRA25-09](../cases/astra-25-unknown-lineage-erasure.md) | Unknown lineage keeps its known erasure lower bound | R7-038 rejected as normative defect; package pair passes, source erasure unsupported |
| [ASTRA25-10](../cases/astra-25-future-lineage-input.md) | Future integration facts do not admit missing input records | R7-042 fixed at 23290b3; judge and seat independently verified |
| [ASTRA25-11](../cases/astra-25-retention-deadline.md) | Expired retention must constrain new stored bytes | R7-052/053 implementation and R7-054 mapping open; seven exact fixtures preserve five intended negative failures per runtime |

## Current evidence

The twenty-seven owned fixtures explicitly use package `0.2.4-draft` (`ef02647`).
Prior fixtures migrated by semantic_profile only. Seven new expiry vectors
encode the judge-mapped refusal; their original complete bytes are also frozen.
All pass closed structure, references, accepted-write integration facts,
normalization and forbidden checks. Current canonical validation passes 65
vectors, 52 clauses and 33 intended checker controls. Local structural log:
`.temp/astra25-vector-structure-16.log`.

R7-042 now accepts the valid future-fact state while rejecting complete/unknown
admitted dangling inputs and an accepted write missing its input. Both runtimes
retain the exact invalid-reference/refusal-then-same-key-success sequence.
Earlier false-positive evidence remains immutable.

Every owned write explicitly uses actor-bound private/read retention context;
existing grants cover it except intentional negative cases. No old expected
report changed except profile version. The added ASTRA25-08-UNKNOWN pair checks
transitive known-input retention through an unknown intermediate: a publish-only
grant for the ancestor is insufficient; restoring matching read-purpose retain
alone admits the private derivative. Both pre-adaptation runtimes fail this
negative and pass the positive. A separate six-control storage/replay harness
per evaluator initially passed two exact-inventory positives and detected all four
negative violations, including full state mutation and retain-revoked replay. These extend existing R7-036/037, not a new
independent defect count.

| Latest recorded owned 0.2.4 semantic runs | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Package runtime at `4af0360` (tree `e689cf2`) | 21 | 5 | 0 |
| Source tree at `d5f07be` | 13 | 5 | 8 |

Each evaluator reports the one owned deployment fixture unsupported. Both previously
passed all six independent storage/replay controls each for scoped grants. The
source framing correction now passes both owned directions and canonical P05;
all nine native release groups pass, including raw-digest refusal with full state
preservation. Fresh 0.2.4 canonical runs are source49/1/7 and package56/1/0;
both remaining executed failures are B01, separately owned succession/projection
work. The prior 0.2.3 judge-verified totals were source50/0/7 and package57/57.
The seven ASTRA25-11 exact vectors are now in the owned denominator: both
positive controls pass, while five expiry negative vectors fail each runtime.
The earlier five native observations remain outside vector totals.
Receipt primary/authorized/unrelated-purpose traces still pass in package;
hidden/visible dirty traces still pass in both. Source `3722327` also passed nine
impact controls independently, including the separate rule/check correction;
earlier six controls did not cover that additional R7-043 failure.

Exact latest expiry runs are `astra22-deadline-vectors-first` and
`astra23-deadline-vectors-first`; both `deadline-atomic-first` entries preserve
three positive passes and seven intended expiry failures per runtime, including
exact replay refusal and full state invariants. Earlier release runs are
`astra22-phase2-024-release-corrected`,
`astra23-phase2-024-owned`, `astra22-release-controls-024-corrected` and both
`canonical-024-first` entries. Prior `astra22-phase2-release-digest-first` and
`astra23-phase2-release-digest-control` keep the wrong-framing evidence and
independent framing oracle. All earlier release-specific runs remain immutable,
pinned by package, evaluator and input hashes. Working-copy migrations at
execution are labeled by exact hashes, not claimed as already committed inputs.

Phase-1 independent checks verified R7-006 release behavior, R7-018 hidden/visible
dirty behavior, and R7-027's original unchanged regressions plus 29 source
controls. Source `512d006` retained both owned budget passes after later fixes.
The first astra-23 evaluator reproduced the original hidden-dirty failure in
14 fields, with the visible-path control passing. The first source adapter
explicitly lacked those operations; unsupported was never counted as a pass.

## Phase-2 gate and remaining work

Convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc` withholds PARK and
requires 57/57 canonical semantic vectors on both independent evaluators, then
one full round with no new open item. Judge `536f54c` records the stronger gate.
Phase-1 dual coverage was 43/57; judge-verified 0.2.3 dual coverage reached50/57
when R7-050 closed. Current 0.2.4 introduces the stricter B01 trace and both fresh
runs fail that separate authority work. Seven canonical source operations remain
unsupported. The judge owns collective totals; unsupported never means pass.

Judge `7446ba5` closed independently verified R7-036/037. Judge closed R7-050 at
`8a42945`, and this seat independently verified both unchanged digest directions
at its current descendant. R7-052/053 and the narrow R7-054 mapping are
classified: expiry requires not_authorized/false before replay, with unchanged
state and original receipt. Verify the explicit package release and both runtime
corrections against preserved first vectors and full-state controls. Rerun owned
regressions as source erasure support arrives. Finalize verdict and park note only after actual PARK.

No real protected-deployment qualification is claimed by semantic publication,
erasure, custody, restore, revocation or delivery traces. Actual witness freshness,
outside-domain trust, sink enforcement and physical purge remain unqualified.
