# astra-25: disclosure and erasure verdict

Status: phase 2, round 22; collective active, NO PARK. Seat identity:
`ivmbp_swarma-memory_astra-25`.

**Current phase-2 score: 1/2.** Full dual semantic coverage and new finding
closure remain incomplete. The prior 2/2 at judge `b1ae299` used the original
supported-vector rubric; it was never a claim that both evaluators passed all 57.

## Seat output and dispositions

Eleven case documents and twenty exact fixtures (nineteen semantic, one deployment)
are published. All initial source readings and later failures remain in git and
[`astra-25-evaluator-results.json`](../cases/astra-25-evaluator-results.json).

| Case | Contract | Disposition |
| --- | --- | --- |
| [ASTRA25-01](../cases/astra-25-hidden-premise-quality.md) | Hidden opposition cannot taint public quality or budget | R7-005 rejected as spec defect; regression retained; later visible-control accounting fixed under R7-027 |
| [ASTRA25-02](../cases/astra-25-declassification-intersection.md) | Every constrained owner's live exact release applies | R7-006 fixed@cde5754; package trace passes; R7-050 source digest-framing mapping fails both valid and invalid controls |
| [ASTRA25-03](../cases/astra-25-surviving-support-erasure.md) | Surviving support does not preserve tainted bytes or close incomplete custody | R7-007 rejected as spec defect; incomplete/complete custody and current-generation fence regressions retained |
| [ASTRA25-04](../cases/astra-25-stale-restore-witness.md) | External witness must be current and complete | R7-008 fixed@cde5754 for fixture meaning; real deployment remains unsupported |
| [ASTRA25-05](../cases/astra-25-hidden-dirty-invalidation.md) | Hidden revision cannot expose protected global dirty state | R7-018 fixed@f31d58f; hidden and authorized-dirty traces pass |
| [ASTRA25-06](../cases/astra-25-quality-budget-isolation.md) | Opposite quality cannot spend existence counters | R7-027 fixed@4e647ea; both owned traces and ASTRA24-05 controls pass |
| [ASTRA25-07](../cases/astra-25-erasure-receipt-metadata.md) | Erase authority does not grant hidden derivative metadata | R7-031 fixed at package 7e71765 / runtime a016781; judge and seat independently verified |
| [ASTRA25-08](../cases/astra-25-retention-authority.md) | Admit/read/use do not silently supply retain | R7-036 source d077064 / R7-037 package 4af0360 independently verified and judge-closed at 7446ba5 |
| [ASTRA25-09](../cases/astra-25-unknown-lineage-erasure.md) | Unknown lineage keeps its known erasure lower bound | R7-038 rejected as normative defect; package pair passes, source erasure unsupported |
| [ASTRA25-10](../cases/astra-25-future-lineage-input.md) | Future integration facts do not admit missing input records | R7-042 fixed at 23290b3; judge and seat independently verified |
| [ASTRA25-11](../cases/astra-25-retention-deadline.md) | Expired retention must constrain new stored bytes | Both runtimes admit at/after expiry; first native inputs/state frozen; classification and exact refusal pending |

## Current evidence

The twenty owned fixtures explicitly use package `0.2.3-draft` (`23290b3`).
All pass closed structure, references, accepted-write integration facts,
normalization and forbidden checks. Current canonical validation passes 65
vectors, 52 clauses and 32 intended checker controls. Local structural log:
`.temp/astra25-vector-structure-14.log`.

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
per evaluator passes two exact-inventory positives and detects all four known
negative violations, including full state mutation and retain-revoked replay. These extend existing R7-036/037, not a new
independent defect count.

| Current owned 0.2.3 semantic runs | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Package runtime at `4af0360` | 19 | 0 | 0 |
| Source release expansion at `36983de` | 9 | 2 | 8 |

Each evaluator reports the one owned deployment fixture unsupported. Both implementations pass all six independent storage/replay controls each.
The new source release expansion fails the valid framed digest and wrongly
accepts the raw digest, committing three forbidden records. Package passes both.
The unchanged source retention implementation passed eight native groups and
canonical49/0/8 before expansion; judge independently reproduced49/1/7 at36983de.
Package passed all26 product/checker controls and canonical57/57. Unsupported
source cases remain explicit.
Receipt primary/authorized/unrelated-purpose traces still pass in package;
hidden/visible dirty traces still pass in both. Source `3722327` also passed nine
impact controls independently, including the separate rule/check correction;
earlier six controls did not cover that additional R7-043 failure.

Exact current digest runs are `astra22-phase2-release-digest-first` and
`astra23-phase2-release-digest-control`, with an independently calculated framing
oracle. Earlier new-release runs are `astra23-phase2-023-retain-corrected`,
`astra22-phase2-023-retain-corrected`, and `checker-future-lineage-023-corrected` in the
evidence JSON. Earlier phase-1, phase-2 and release-specific runs remain immutable,
pinned by package, evaluator and input hashes. Working-copy additions at execution
are labeled and identified by hashes, not claimed as committed inputs.

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
Phase-1 dual coverage was 43/57; last 0.2.2 judge-verified dual coverage is 49/57. Source d077064 independently
passed all 49 supported vectors under 0.2.3; eight remained explicitly unsupported.
The subsequent source declassification expansion exposes the new framing defect. The
judge owns current collective totals; this seat does not infer success for
unsupported operations or unfinished implementations.

Judge `7446ba5` closed independently verified R7-036/037. Both support exact scoped
retention and current-authorized replay on the tested fixtures. Judge classified
the source digest defect as R7-050. Verify its correction against both
unchanged directions. Rerun owned regressions as source erasure support arrives.
Source correction8a42945 is queued for independent verification after this
deadline investigation. Classify ASTRA25-11 before creating its typed vectors.
Finalize verdict and park note only after actual convener PARK.

No real protected-deployment qualification is claimed by semantic publication,
erasure, custody, restore, revocation or delivery traces. Actual witness freshness,
outside-domain trust, sink enforcement and physical purge remain unqualified.
