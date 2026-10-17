# ASTRA24-09: registered review is a path property after recomputation

Status: R7-045 package implementation bug; correction `f6c339d` independently
verified and judge-closed. Both implementations pass the exact migrated fixture. Owner: astra-24. Package `0.2.2-draft` at
`7e71765`; execution checkout `a016781`.

## Clauses and two readings

K-EVAL-8 distinguishes unresolved dirty causes from registered review-on-change
paths to historical or withdrawn inputs. It permits a complete recalculated
snapshot with cleared dirty causes and still requires eligible cross-schema
review dependents when querying the revised decision. The companion's registered
impact contract and kernel 11.1 provide the source direction. Declared rationale
creates review dependencies, never sufficient signed support (K-RULE-2).

A convenient implementation collects only targets of a review edge whose direct
premise is historical. The path reading follows registered review dependencies
transitively. A historical decision can affect a second registered assumption
through the first; clearing an evaluation dirty marker does not remove either
registered review edge. The path reading is recommended by K-EVAL-8's explicit
path/registered-impact language, without inventing any new edge or work action.

## Minimal separating input and controls

The closed snapshot contains decision A1 and its authorized replacement A2.
Two registered declared-rationale edges remain: A1 -> B and B -> C, both
review_on_change. B and C use the assumption schema while A uses decision.
Recomputation is represented by empty runtime dirty and dirty_causes inventories.
The second edge is private; its records and target are otherwise authorized.

First capture the public decision query, then query the same cut privately.

| Observable | Direct-edge-only reading | Required path reading |
| --- | --- | --- |
| Public review_required | B | B |
| Private review_required | B | B, C |
| Selected decision item | current A2 | current A2 |
| Signed witnesses | neither, complete | neither, complete |
| Protected dirty inventory | empty | empty |

The public capture is a negative control: an inaccessible path must not disclose
C. It is also a positive direct-edge control proving that review is not disabled.
The complete selected items remain equal across the two queries after fresh
handle normalization. No operations mutate records, dirty causes or other state.
This case does not claim that recomputation clears registered review obligations.

## Execution and limitations

Source impact extension `e38c37c` passes the full exact fixture. The package
implementation returns only B privately: comparison reports review_required
length 1 instead of 2 and missing exact `rec:dependent-c` reference, plus the
intended missing-dependent forbidden match. Public output, selected items,
normalization and postconditions all pass.

At `a016781`, the owned twelve-vector corpus is source10 pass/2 fail and
package9 pass/3 fail. The two shared failures are separately classified
R7-040/041 authority-head cases; this new missing review path is independent.
Six focused native source impact controls also pass, including historical cuts,
hidden required elements, resolved causes and later edge withdrawal. Passing
those controls alone would not establish this exact case; its independently
specified fixture and direct execution do.

- Fixture SHA-256: `eea505ab9486a09efa208d71e11f2ceaadda25828879a221d08c6b7df4e39019`.
- Reports: `.temp/astra22-owned-cases-21.json`, `.temp/astra23-owned-cases-13.json`.
- Native impact controls: `.temp/astra22-impact-controls-01.log`.
- Structure/state/normalization/inventory and missing-dependent plant: `.temp/case-vectors-validate-20.log`.

The local plant initially assigned an integer into a list slot; it did not prove
size_equals detection. Log19 records that harness setup failure. The corrected
plant removes one required review reference and triggers exactly the intended
predicate; no fixture expectation changed to repair the instrument.
This two-edge chain is not a general proof for arbitrary mixed-role paths or
cyclic review graphs. No deployment guarantee or task-creation authority follows.

Judge event `$w6ki9VdtqJ2t1FPa6C95Bnv2-P6BadtH6uI0_zpHFhY` confirms
R7-045: eligible registered paths persist after dirty recomputation. No new
specification or owner architecture decision is required. The package owner
preserves the first exact failure at `08c4b9a`; input and expected outputs
remain unchanged pending corrected-head verification.

## Package 0.2.3 explicit migration

Round 21 migrates this case to `0.2.3-draft` (`23290b3`). Behavioral expected
results and initial states are unchanged. Read-only operations need no storage
context; each of this seat's six revise operations explicitly binds private/read
under its existing actor/space/record retain grant. No grant is inferred from a
later query. `.temp/astra24-profile-023-migration.json` records old/new hashes,
exact operation contexts and normalized equality. Structural and intended
forbidden controls pass log 22. Earlier hashes identify historical profile runs.

## Round 21 transitive review correction verified

Package `f6c339d` passes the exact ASTRA24-09 fixture after the explicit profile
migration above; source remains passing. The two focused native review controls
also pass: transitive and cyclic review, hidden necessary elements, both orders
of review/sufficient edges, pure sufficient and documentary non-review controls,
and hidden deterministic certificates. They preserve selected evidence, complete
evaluation, empty dirty state and no synthetic witness. No relationship absent
from the registered graph is introduced.

At checkout `12eccae`, all thirteen owned package vectors pass; source has only
the separate ASTRA24-08-NEXT failure. Exact evidence: package16/source25 and
`.temp/astra23-transitive-review-controls-01.log`. R7-045 is behaviorally verified
by this seat; judge closure remains separate. This corpus does not cover all
new 0.2.3 retention refusal requirements, whose implementation review remains
with their owners. Original package first failure `08c4b9a` remains immutable.

Judge decision `$FUaN_53BaXJmAS0URtEd8DTcbnlzmmLxJ_z4s3DG0yk` closes R7-045 at
`f6c339d` after its own unchanged 0.2.2 exact case, native review controls and
canonical 57/57 run. This seat independently verified the migrated 0.2.3 input.
