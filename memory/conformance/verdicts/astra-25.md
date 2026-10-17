# astra-25: disclosure and erasure verdict

Status: phase 2, round 34; collective active, NO PARK. Seat identity:
`ivmbp_swarma-memory_astra-25`.

**Current phase-2 score: 1/2.** Both evaluators now pass every canonical semantic
vector, but the new restore supplementary cases fail in package. The prior 2/2 at judge `b1ae299` used the original
supported-vector rubric; it was never a claim that both evaluators passed all 57.

## Seat output and dispositions

Twelve case documents and thirty-four exact fixtures (thirty-three semantic, one deployment)
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
| [ASTRA25-07](../cases/astra-25-erasure-receipt-metadata.md) | Erase authority does not grant hidden derivative metadata | R7-031 fixed at package 7e71765 / runtime a016781; judge and seat independently verified; R7-057 source correction946cbd8 independently verified and judge-closed at e3d44df |
| [ASTRA25-08](../cases/astra-25-retention-authority.md) | Admit/read/use do not silently supply retain | R7-036 source d077064 / R7-037 package 4af0360 independently verified and judge-closed at 7446ba5 |
| [ASTRA25-09](../cases/astra-25-unknown-lineage-erasure.md) | Unknown lineage keeps its known erasure lower bound | R7-038 rejected as normative defect; both exact pairs now pass at source dbf4892 and package 23b4d74 |
| [ASTRA25-10](../cases/astra-25-future-lineage-input.md) | Future integration facts do not admit missing input records | R7-042 fixed at 23290b3; judge and seat independently verified |
| [ASTRA25-11](../cases/astra-25-retention-deadline.md) | Expired retention must constrain new stored bytes | R7-054 closed at6a04e8c and052 at4a14a56; package053 at23b4d74 independently verified and judge-closed at13e3d73 |
| [ASTRA25-12](../cases/astra-25-restore-current-obligations.md) | Current outside-domain restore obligations must survive an older local erasure inventory | R7-058 package implementation open; five exact fixtures, source5/5 and package2/5 |

## Current evidence

The thirty-four owned fixtures explicitly use package `0.2.5-draft` (`6a04e8c`).
Prior fixtures migrated by semantic_profile only. Seven new expiry vectors
encode the judge-mapped refusal; their original complete bytes are also frozen.
All pass closed structure, references, accepted-write integration facts,
normalization and forbidden checks. Current canonical validation passes 65
vectors, 52 clauses and 34 intended checker controls. Local structural log:
`.temp/astra25-vector-structure-20.log`.

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

| Latest recorded owned 0.2.5 semantic runs | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Package runtime at `23b4d74` | 30 | 3 | 0 |
| Source runtime at `946cbd8` | 33 | 0 | 0 |

Each evaluator reports the one owned deployment fixture unsupported. Both previously
passed all six independent storage/replay controls each for scoped grants. The
source framing correction now passes both owned directions and canonical P05;
all nine native release groups pass, including raw-digest refusal with full state
preservation. Fresh source 0.2.5 canonical is 57/57 after the erasure coverage addition;
corrected package is also 57/57. Both P11 expiry traces and authority B01 pass.
The former seven canonical source gaps are now executable; native recovery
R7-056 correction passes independent verification and is judge-closed at e2a797d.
The seven ASTRA25-11 exact vectors are now in the owned denominator: both
positive controls and all five negative vectors pass in both runtimes.
The earlier five native observations remain outside vector totals.
Receipt primary/authorized/unrelated-purpose traces still pass in package;
hidden/visible dirty traces still pass in both. Source `3722327` also passed nine
impact controls independently, including the separate rule/check correction;
earlier six controls did not cover that additional R7-043 failure.

Earlier source deadline runs are `astra22-phase2-025-deadline-corrected`,
`astra22-deadline-atomic-corrected` and the canonical/native correction entries.
All seven expiry vectors, ten independent state checks and six native deadline
groups pass, including all four write APIs. Both earlier `deadline-atomic-025-first`
entries preserve three positive passes and seven intended failures each. Package
corrected runs are `astra23-phase2-025-deadline-corrected` and its atomic/native/
canonical entries: 26 owned and 57 canonical semantic passes, 10 independent state
controls and 31 product/checker tests. All first runs remain immutable. Earlier release runs are
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

First source erasure evidence is `astra22-phase2-025-erasure-coverage`,
`astra22-canonical-025-erasure-coverage`, both `native-*-025-first` entries and
`astra22-availability-025-first-reproduction`. Every Python module was compared
byte-for-byte with dbf4892. All eight native erasure groups pass: hidden receipt
refs do not weaken protected closure, unknown lineage keeps its known lower
bound, omitted/unreachable custody remains pending, independent recipients stay
outside receipts, late writers are fenced, and witnessed restore re-purges
behind its read fence. These are synthetic transitions, not physical deletion.

Four availability groups pass; the fifth fails exactly `refusal != view` after
an authorized recovery from initially degraded policy. Its original signed input
was independently validated and reproduced with unchanged before/after refusal
and normalized receipt. Judge event
`$JwiSCClsftcbsOR8UrOJoe2h7NZWY12YYcjSgWm4S6c` classifies this as R7-056
source implementation bug. The suite is explicitly red and no duplicate case
or guessed oracle is added. Native erase-context-priority evidence from 0529814 is now independently
reproduced in both runtimes. Same-key ungranted purpose/audience changes yield
source not_authorized versus package idempotency_conflict, both atomically;
fresh-key empty-ref erase and exact replay/revocation controls agree. Judge event `$eZJtQ5NtpfBEb7qFsk54ePTdCFPWyGbT_S4eBcV9FM8` classifies
R7-057 as source implementation bug. Two new exact purpose/audience fixtures
now encode the mapped conflict with live exact replay and fresh-key empty-ref
positive controls. The first source run fails only the intended code in each; package passes
both. Source946cbd8 now passes both unchanged fixtures and all 28 owned semantic
cases, 11 native erasure groups, the independent original seven-operation probe
and 57 canonical semantic cases. Four correction runs preserve module/input
hashes and exact refusal-state/original-receipt guarantees. Judge e3d44df closes R7-057 at946cbd8. No old output changed. R7-056
correction 87beb46 now passes independent review: five availability groups,
26 owned semantic vectors and all 57 canonical semantic vectors. Only the two
current availability facts are changed by the authorized transition; the four
initial/requested-state combinations preserve records, grants, policy pins,
cuts, receipts and captures. The original failing witness remains immutable.
Latest runs are the three `astra22-*-025-availability-corrected` entries; every
current module was byte-compared to the correction. Judge e2a797d closes R7-056 at 87beb46.

ASTRA25-12 first preserves four native restore observations per reader. Judge
`$M8NvqvBJqj0P6G_HX3wtl3-FVKIbSUxxSZFXB9YCyvE` classifies R7-058 as package
implementation bug. Five exact supplemental fixtures now encode new current
obligations, unreachable custody, known/empty positives and unaffected B.
Source passes all five; unchanged package fails new, unreachable and independent
variants. Both false-witness/global-fence refusals and known/empty controls agree.
Full native first snapshots and first exact outputs remain immutable. Source is
33/33 owned semantic; package30/33. R7-058 correction/review remains necessary;
no package prose or owner decision is required. Existing R7-055 is separate.

## Phase-2 gate and remaining work

Convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc` withholds PARK and
requires 57/57 canonical semantic vectors on both independent evaluators, then
one full round with no new open item. Judge `536f54c` records the stronger gate.
Phase-1 dual coverage was 43/57; judge-verified 0.2.3 dual coverage reached50/57
when R7-050 closed and remains judge-verified after both B01 fixes on 0.2.4.
Current 0.2.5 P11 passes both corrected runtimes.
Source dbf4892 independently passes all 57 canonical semantic vectors and all
the original 26 owned semantic vectors. Source946cbd8 now also passes the two
later R7-057 supplementary fixtures unchanged. The judge owns collective
totals; deployment
unsupported never means pass.

Judge `7446ba5` closed independently verified R7-036/037. Judge closed R7-050 at
`8a42945`, and this seat independently verified both unchanged digest directions
at its current descendant. R7-052/053 and the narrow R7-054 mapping are
classified: expiry requires not_authorized/false before replay, with unchanged
state and original receipt. The explicit 0.2.5 release is independently verified:
only P11 changes beyond version, its original 16 operations/results remain, and
all 34 checker controls pass. Judge closed R7-054. Source R7-052 correction is
independently verified and judge-closed. Package R7-053 is independently
verified and judge-closed in signed 13e3d73. Source erasure/restore/load support is now
independently checked. Separate R7-055 records an unresolved owner decision on
cross-issuer authority ancestry; no oracle for that native probe is invented.
Finalize verdict and park note only after actual PARK.

No real protected-deployment qualification is claimed by semantic publication,
erasure, custody, restore, revocation or delivery traces. Actual witness freshness,
outside-domain trust, sink enforcement and physical purge remain unqualified.
