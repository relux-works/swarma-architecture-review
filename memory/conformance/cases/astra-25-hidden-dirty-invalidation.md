# ASTRA25-05: global dirty state can expose a hidden revision

Status: R7-018 spec-bug accepted; first package evaluator reproduces the leak.
Owner: astra-25. Package: `0.1.0-draft` at `0ef608a`.

## Clauses

Source kernel §7.3 and companion §4/S24 require hidden-only revisions to leave
disclosed status, coverage and change notices unchanged. Package K-AUTH-1 filters
hidden premises/rules before computation; K-NI-1 explicitly protects quality,
completeness and hidden revisions. However, K-EVAL-8 requires global transitive
dirty marking, then says dirty items give both channels `not_found + incomplete`,
appear in `review_required`, and set `needs_review`; it does not scope the dirty
reason to the requesting audience. `runtime.dirty` is an unqualified ref list.

## Minimal separating input

```text
Public: assertion B; independent admissible root B+.
Private in the SAME space: assertion A@1; root A+;
  checked rule A@1+ -> B+ and its certificate.
The public B text has no content lineage to A; the private rule is an extra
  epistemic path, not public evidence or a content source for B.
Operation 0: capture the public B projection at cut 100.
Operation 1: authorized private replace of A@1 by A@2 at committed cut 102.
Final query: identical public B projection at cut 102.
```

Revision and replacement remain private. Public policy, resource envelope and
availability are unchanged. No public dependency or evidence changed. The
protected global reverse index can mark B dirty for the private projection.

## Two readings and outputs

| Public B observation after the hidden revision | Literal unqualified K-EVAL-8 dirty short-circuit | K-AUTH-1/K-NI-1 scoped invalidation |
| --- | --- | --- |
| support witness / evaluation | not_found / incomplete | present / complete |
| support premise_quality | not_fully_checked | clean_path |
| needs_review | true | false |
| review_required | B | empty |
| cutoffs | dirty | empty |

The first reading leaks that hidden registered evidence changed without exposing
its id or payload. Calling the dirty bit protected does not protect these derived
public fields. Hiding only the review list is insufficient.

## Recommendation and controls

Clarify that invalidation affects a disclosed projection only through eligible
dependencies or separately authorized impact. Keep private/global invalidation
and conservative private processing; do not weaken the dirty-before-fresh rule
for an audience whose evidence actually changed. Query-scoped recomputation or
adequate protected invalidation provenance may implement this requirement; this
case does not prescribe a new scheduler or data store.

[`astra-25-hidden-dirty-invalidation.vector.json`](astra-25-hidden-dirty-invalidation.vector.json)
requires exact equivalence of the two public views while the protected
postcondition still records B dirty. Its positive control,
[`astra-25-hidden-dirty-invalidation-visible-control.vector.json`](astra-25-hidden-dirty-invalidation-visible-control.vector.json),
admits the entire path/revision to the public audience and expects K-EVAL-8's
explicit dirty/incomplete result. Thus unconditional suppression of dirty state
cannot satisfy the pair. Historical cut behavior remains governed by K-TIME-1.

## Evidence and limits

The pair uses the actual closed package grammar, not a hypothetical extra field.
Expected observations are derived from the source non-interference requirement;
the competing dirty result follows the package's explicit operational clause.
The judge classified this contradiction as R7-018 during review; astra-21 accepted the fix.
No physical timing or protected-deployment qualification is claimed.

Both vectors pass the released package's schema, reference, normalization and
forbidden-predicate checks. Replacing the hidden trace's final expected view by
the visible control's dirty view is a bounded checker plant: normalization must
reject it as `normalized paired outputs differ`. The unmodified hidden trace is
the valid control. Evidence: `.temp/astra25-vector-structure-04.log`.

## Independent execution evidence

The untouched astra-23 first evaluator (`0008dc3`) was run on the six owned
0.1.0 fixtures from `3045117`, using the original 0.1.0 schemas from `0ef608a`.
Five pass. This hidden trace fails with 14 field-level differences, a failed
paired-output equality check and both forbidden incomplete/review outcomes.
The visible-path dirty control passes, so suppressing every dirty result is not
the required fix. Exact differences, input hashes and evaluator hashes are in
[`astra-25-evaluator-results.json`](astra-25-evaluator-results.json), run
`astra23-first`. Its actual result changes public support from present to
not_found, complete to incomplete, and clean_path to not_fully_checked; loses
its public root and qualification; adds needs_review, review_required and dirty
cutoff. The source evaluator's first adapter explicitly does not support these
mutating operations and reports all six cases unsupported.

The owned fixtures are now migrated to the 0.2.0 grammar with explicit synthetic
integration facts. The observed failure above is pinned to the old fixture and
implementation versions, not represented as a run of the migrated fixtures.
The editor's next release and independent behavior recheck remain pending.

## Candidate fix verification: 0.2.1-draft

At `f31d58f`, K-EVAL-8 now retains unresolved `{assertion, revision}` causes in
protected state and requires an eligible dependency/impact path for a disclosed
effect. It explicitly filters the revision, changed input, path, premises and
certificates by current rights and query context before charging logical work.
Historical queries before the cause stay unaffected, resolved causes are not
reconstructed from history, and hidden-only causes leave the public projection
unchanged while protected global dirtiness remains. The visible affected control
still requires dirty/incomplete output. This closes the competing prose readings.

The owned pair is migrated to the 0.2.1 grammar with initially empty
`dirty_causes` and explicit synthetic subject/principal identity, preserving all
previous semantic expected results. All eight owned fixtures pass structural
checks and both leak plants (`.temp/astra25-vector-structure-06.log`). The package
validator also passes 57 semantic / eight deployment vectors and 20 checker
controls. Updated evaluator execution is pending; the old evaluator failure is
not reclassified as a pass on the strength of these structural/prose checks.


Independent execution on astra-23 `f5fdd8b` with exact package `f31d58f` now
passes both owned hidden/visible traces. Global B dirtiness remains in the
protected postcondition, public output remains equivalent, and the visible-path
control remains dirty/incomplete. Run `astra23-v0.2.1` in the evidence JSON pins
inputs at `0fa73fd` and evaluator hashes. This supplies behavior verification for
R7-018; no deployment timing/isolation pass is implied.

## Phase-2 source coverage verification

Source implementation `e38c37c` now passes both unchanged hidden and visible
controls under explicit package `0.2.2`. Independent rerun also passes its six
impact controls for protected causes, hidden paths/premises/certificates, hidden
AND siblings/context, historical/resolved causes, later withdrawals and
cross-schema review. Protected dirty causes remain recorded; public reads do
not clear them. Exact owned run is `astra22-phase2-dirty-coverage` in the owned
evidence JSON; control log is `.temp/astra25-source-impact-controls-01.log`.
This expands source execution coverage; it does not qualify timing or deployment.

Source `3722327` preserves both owned traces after its separate R7-043 correction.
All nine impact controls pass independently, including newly added rule/check
withdrawals, private-positive/public-hidden outcomes, challenge non-invalidation,
transitive closure, historical cut and cleared recomputation. These specifically
extend the earlier six-control evidence; that earlier green suite did not cover
R7-043. Log `.temp/astra25-source-impact-controls-02.log`; exact owned result
`astra22-phase2-rule-check-dirty`. Judge owns R7-043 closure.
