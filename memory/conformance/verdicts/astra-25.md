# astra-25: disclosure and erasure verdict

Status: PARK, authorized by the convener at 2026-10-17T06:33Z after round 37.
Seat identity: `ivmbp_swarma-memory_astra-25`.

**R7 score: 2/2.** Signed judge closure `9d2cdd4` verifies full dual semantic
coverage and closes R7-058 at `104fbe8`. The 58-item ledger has 47 fixed findings,
10 rejected findings and the filed unresolved owner question R7-055. No
specification or implementation bug remains open. The convener verified the
completion gate at `1f92e91` and issued PARK in rounds event
`$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg`.

## Current evidence

The release is **0.2.5-draft**, signed `6a04e8c`: 65 canonical vectors split into
57 semantic and eight deployment, 14 closed schemas, 52 clauses and 34 intended
checker controls. Canonical validation and explicit supplemental structure
checks pass. The collective has 69 supplemental artifacts: 68 semantic and one
deployment. All current owned fixtures explicitly use the released profile.

| Evaluator | Runtime | Canonical semantic | Owned semantic | Collective supplemental semantic |
| --- | --- | ---: | ---: | ---: |
| Source | `946cbd8` | 57/57 | 33/33 | 68/68 |
| Package | `104fbe8` | 57/57 | 33/33 | 68/68 |

This seat independently ran both complete canonical inventories and all owned
fixtures. The full collective supplemental totals are independently verified by
the judge in `9d2cdd4`; source expanded report/test evidence is `b8189ba`.
Source control coverage is 129, with 12 erasure groups rerun and 117 unchanged
controls retaining prior evidence. Package's full 30 product plus four comparer
tests were rerun and pass. Source129 is coverage, not a claim that all129 tests
were rerun in this seat's last round.

Both readers report all eight canonical deployment vectors and the one owned
deployment fixture unsupported. Synthetic erasure, custody, restore, revocation,
release and delivery do not qualify physical purge, current real external
witnesses, outside-domain trust, sink enforcement or deployment isolation.

## Seat output and dispositions

Twelve case documents and 34 exact fixtures (33 semantic, one deployment) are
published. The [evidence aggregate](../cases/astra-25-evaluator-results.json)
contains 90 append-only run records, preserving original failures, profile
migrations, exact input/module hashes and later correction checks. Original
fixture bytes and native firsts remain recoverable from their signed commits;
no failing expected output was silently rewritten.

| Case | Contract and disposition |
| --- | --- |
| [ASTRA25-01](../cases/astra-25-hidden-premise-quality.md) | Hidden opposition cannot alter public quality/budget. R7-005 rejected as a spec defect; regression retained; later budget defect R7-027 fixed at4e647ea. |
| [ASTRA25-02](../cases/astra-25-declassification-intersection.md) | Every constrained owner's live exact release applies. R7-006 fixed atcde5754; source canonical-body framing R7-050 fixed at8a42945. Both digest directions and nine native release groups verified. |
| [ASTRA25-03](../cases/astra-25-surviving-support-erasure.md) | Surviving logical support does not preserve tainted payloads or close incomplete custody. R7-007 rejected as a spec defect; exact incomplete/complete/current-generation regressions pass in both readers. |
| [ASTRA25-04](../cases/astra-25-stale-restore-witness.md) | External witness must be current and complete. R7-008 fixture meaning fixed atcde5754; real deployment remains unsupported. |
| [ASTRA25-05](../cases/astra-25-hidden-dirty-invalidation.md) | Hidden revisions cannot expose protected dirty state. R7-018 fixed atf31d58f; hidden and visible controls pass. Additional source R7-043 impact controls independently verified. |
| [ASTRA25-06](../cases/astra-25-quality-budget-isolation.md) | Opposite quality cannot spend existence counters. R7-027 fixed at4e647ea; paired owned traces and native accounting controls pass. |
| [ASTRA25-07](../cases/astra-25-erasure-receipt-metadata.md) | Erase authority does not grant hidden closure metadata. R7-031 fixed at7e71765/a016781. Later changed-context priority R7-057 fixed at946cbd8, preserving exact replay authorization and original receipt. |
| [ASTRA25-08](../cases/astra-25-retention-authority.md) | Admit/read/use do not supply retain. R7-036 source d077064 and R7-037 package4af0360 independently verified and judge-closed; transitive unknown-lineage and unrelated-purpose controls retained. |
| [ASTRA25-09](../cases/astra-25-unknown-lineage-erasure.md) | Unknown lineage retains its known erasure lower bound. R7-038 rejected as a normative defect; both known-dependency and independent controls pass. |
| [ASTRA25-10](../cases/astra-25-future-lineage-input.md) | Future integration facts do not admit missing records. R7-042 checker correction fixed at23290b3; valid future facts and intended dangling-input rejection verified. |
| [ASTRA25-11](../cases/astra-25-retention-deadline.md) | Current deadlines constrain storage and replay before idempotency. R7-054 release6a04e8c, R7-052 source4a14a56 and R7-053 package23b4d74 are closed; seven exact fixtures and full state/receipt controls pass. |
| [ASTRA25-12](../cases/astra-25-restore-current-obligations.md) | Current external obligations absent from an old backup must be reconciled before reopening. R7-058 fixed at104fbe8; five exact fixtures and original restore/late-writer controls pass with full protected state verified. |

Native initial-availability recovery R7-056, raised by the source implementer,
was independently reproduced and its87beb46 correction verified by this seat.
The four initial/requested state combinations change only current availability
facts and preserve records, policy pins, grants, cuts, receipts and captures.

## Final restore correction evidence

R7-058 first evidence is signed `644c793`; exact fixtures are `1cefcf9`;
late-writer first is `1138c5d`; independent correction verification is `b949afb`.
The [original recovery snapshots](../cases/astra-25-restore-current-obligations-first.json),
[original late-writer snapshots](../cases/astra-25-restore-late-writer-first.json)
and [corrected snapshots](../cases/astra-25-restore-correction.json) retain complete
inputs, actuals and lossless content-addressed states.

All four original recovery inputs and all three late-writer inputs are unchanged,
as are both independent harness hashes. Current complete witness obligations
enter the full closure, fences and erased inventory; newly learned obligations
advance generation. Unreachable affected custody refuses atomically and keeps
the global read fence. Known/empty/repeated recovery remain valid; independent
content and custody survive. Old-generation writes and current-generation erased
dependencies refuse exactly without mutation; reviewed unrelated current writes
succeed. Exact first failures, original receipts and all90 prior run records are
preserved. Judge's seven intended old-engine failures establish that the added
product checks detect the failure class without setup errors.

## Remaining boundary and PARK

[R7-055](../OWNER-QUESTIONS.md) asks whether H1's canonical predecessor edge
endorses a foreign H2 event's ordering transitively. The owner has not chosen
between issuer-local and global ordering. Its exact native pair remains outside
pass/fail denominators; no authority option or evaluator correction was invented.
It is the one filed owner question permitted by the rubric, not an open bug.

Round 37 introduced no case, divergence, runtime change, package change or fixture
change. Required correction reviews are complete and evidence is published.
The convener accepted all seven post-closure quiet rounds and issued explicit
PARK. This finalization changes only the verdict and [park note](../parked/astra-25.md);
all fixtures, native firsts and 90 run records remain unchanged. No assigned
correction, unclassified intake or directed review remains pending for this seat.
