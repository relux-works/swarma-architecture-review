# astra-25: disclosure and erasure verdict

Status: phase 2, round 12; collective active, NO PARK. Seat identity:
`ivmbp_swarma-memory_astra-25`.

**Current phase-2 score: 1/2.** Full dual semantic coverage and new finding
closure remain incomplete. The prior 2/2 at judge `b1ae299` used the original
supported-vector rubric; it was never a claim that both evaluators passed all 57.

## Seat output and dispositions

Nine case documents and fifteen exact fixtures (fourteen semantic, one deployment)
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
| [ASTRA25-07](../cases/astra-25-erasure-receipt-metadata.md) | Erase authority does not grant hidden derivative metadata | R7-031 spec-bug, editor fix/explicit context pending |
| [ASTRA25-08](../cases/astra-25-retention-authority.md) | Admit/read/use do not silently supply retain | Both evaluators admit a derivative with retain absent; judge classification pending |
| [ASTRA25-09](../cases/astra-25-unknown-lineage-erasure.md) | Unknown lineage keeps its known erasure lower bound | Package pair passes; source erasure unsupported; regression submitted |

## Current evidence

The owned fixtures use package `0.2.1-draft` (`f31d58f`) and pass closed structure,
reference, normalization and forbidden checks. The hidden-quality and global-dirty
violation plants are detected for their intended reasons. Latest structural log:
`.temp/astra25-vector-structure-10.log`. Synthetic integration facts are explicit
trusted fixture inputs, never authority inferred from client citations.

| Current owned semantic corpus | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Package evaluator `f5fdd8b` (report/control update `8b9baf3`) | 12 | 2 | 0 |
| Source evaluator as pinned in `astra22-phase2-unknown-erasure` | 3 | 1 | 10 |

Each evaluator reports the one owned deployment fixture unsupported. The package
failures are ASTRA25-07 hidden receipt ID and ASTRA25-08 missing retain authority;
the source failure is ASTRA25-08. Authorized controls pass. ASTRA25-09's erased
known-input late write is refused, while its independent-input control admits the
private unknown record; both preserve complete A/U fencing and custody purge.

Exact current runs are `astra23-phase2-unknown-erasure` and
`astra22-phase2-unknown-erasure` in the evidence JSON. Earlier phase-1 and phase-2
runs remain immutable entries, pinned by package, evaluator and input hashes.
Working-copy fixture additions at execution are explicitly labeled and identified
by hashes rather than misrepresented as already committed inputs.

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
Phase-1 dual coverage was 43/57; source proof enumeration is expanding it. The
judge owns current collective totals; this seat does not infer success for
unsupported operations or unfinished implementations.

Migrate ASTRA25-07 and all erase fixtures to the released operation-bound receipt
context, verify hidden/authorized/unrelated-purpose and replay controls while
preserving full protected closure, obtain ASTRA25-08 disposition, and rerun the
owned corpus as source release/erasure support arrives. Keep the unknown-lineage
pair for that second implementation. Finalize verdict and park note only after
actual convener PARK.

No real protected-deployment qualification is claimed by semantic publication,
erasure, custody, restore, revocation or delivery traces. Actual witness freshness,
outside-domain trust, sink enforcement and physical purge remain unqualified.
