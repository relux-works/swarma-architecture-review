# astra-25: disclosure and erasure verdict

Status: phase 2, round 13; collective active, NO PARK. Seat identity:
`ivmbp_swarma-memory_astra-25`.

**Current phase-2 score: 1/2.** Full dual semantic coverage and new finding
closure remain incomplete. The prior 2/2 at judge `b1ae299` used the original
supported-vector rubric; it was never a claim that both evaluators passed all 57.

## Seat output and dispositions

Ten case documents and seventeen exact fixtures (sixteen semantic, one deployment)
are published. All initial source readings and later failures remain in git and
[`astra-25-evaluator-results.json`](../cases/astra-25-evaluator-results.json).

| Case | Contract | Disposition |
| --- | --- | --- |
| [ASTRA25-01](../cases/astra-25-hidden-premise-quality.md) | Hidden opposition cannot taint public quality or budget | R7-005 rejected as spec defect; regression retained; later visible-control accounting fixed under R7-027 |
| [ASTRA25-02](../cases/astra-25-declassification-intersection.md) | Every constrained owner's live exact release applies | R7-006 fixed@cde5754; wrong-owner no-effect and true revocation trace passes |
| [ASTRA25-03](../cases/astra-25-surviving-support-erasure.md) | Surviving support does not preserve tainted bytes or close incomplete custody | R7-007 rejected as spec defect; incomplete/complete custody and current-generation fence regressions retained |
| [ASTRA25-04](../cases/astra-25-stale-restore-witness.md) | External witness must be current and complete | R7-008 fixed@cde5754 for fixture meaning; real deployment remains unsupported |
| [ASTRA25-05](../cases/astra-25-hidden-dirty-invalidation.md) | Hidden revision cannot expose protected global dirty state | R7-018 fixed@f31d58f; hidden and authorized-dirty traces pass |
| [ASTRA25-06](../cases/astra-25-quality-budget-isolation.md) | Opposite quality cannot spend existence counters | R7-027 fixed@4e647ea; both owned traces and ASTRA24-05 controls pass |
| [ASTRA25-07](../cases/astra-25-erasure-receipt-metadata.md) | Erase authority does not grant hidden derivative metadata | R7-031 spec-bug, explicit context released at 7e71765; behavioral correction pending |
| [ASTRA25-08](../cases/astra-25-retention-authority.md) | Admit/read/use do not silently supply retain | R7-036 source / R7-037 package impl-bugs; separate operation-scope mapping gap pending |
| [ASTRA25-09](../cases/astra-25-unknown-lineage-erasure.md) | Unknown lineage keeps its known erasure lower bound | R7-038 rejected as normative defect; package pair passes, source erasure unsupported |
| [ASTRA25-10](../cases/astra-25-future-lineage-input.md) | Future integration facts do not admit missing input records | Both evaluators pass; package checker falsely rejects initial state; judge classification pending |

## Current evidence

The owned fixtures explicitly use package `0.2.2-draft` (`7e71765`). Sixteen
pass closed structure, references, normalization and forbidden checks. ASTRA25-10
passes shape/normalization/accepted-fact checks but is rejected by `check_state`
for a future integration input; this is the new checker finding, not a pass.
The admitted-dangling-input negative control is also correctly rejected beside
an accepted existing-input control. Current canonical validation remains green:
65 vectors, 52 clauses, 23 checker controls. Local structural log:
`.temp/astra25-vector-structure-11.log`.

All previous expected reports survive migration unchanged except profile version.
Every owned erase explicitly uses actor-bound private/read receipt context;
ASTRA25-07 adds only A-specific matching metadata authority. Its new unrelated
publish-purpose neighbor still requires A-only receipt and complete A/D purge.
The hidden-quality and global-dirty violation plants remain detected.

| Current owned semantic corpus | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Package runtime at `1828356` | 13 | 3 | 0 |
| Source runtime at `1f35727` | 4 | 1 | 11 |

Each evaluator reports the one owned deployment fixture unsupported. Package
failures are ASTRA25-07 hidden receipt ID, its other-purpose neighbor, and
ASTRA25-08 missing retain authority; the source failure is ASTRA25-08. Authorized
controls pass. ASTRA25-09 retains both package passes. ASTRA25-10 passes both
runtimes, including the missing-input refusal followed by successful exact retry.

Exact current runs are `astra23-phase2-022-migration` and
`astra22-phase2-022-migration`, plus `checker-future-lineage-022`, in the evidence
JSON. Earlier phase-1, phase-2 and 0.2.1 future-input runs remain immutable entries,
pinned by package, evaluator and input hashes. Working-copy fixture additions at
execution are labeled and identified by hashes, not claimed as committed inputs.

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
Phase-1 dual coverage was 43/57; current source candidate is 45/57, pending judge verification. The
judge owns current collective totals; this seat does not infer success for
unsupported operations or unfinished implementations.

Verify the corrected erase runtime on hidden/authorized/unrelated-purpose and
canonical replay controls, preserving complete protected closure. Follow the
retention-scope package decision and R7-036/037 fixes, obtain the future-fact
checker disposition, and rerun owned regressions as source release/erasure
support arrives. Finalize verdict and park note only after actual convener PARK.

No real protected-deployment qualification is claimed by semantic publication,
erasure, custody, restore, revocation or delivery traces. Actual witness freshness,
outside-domain trust, sink enforcement and physical purge remain unqualified.
