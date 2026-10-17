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
The judge classified this contradiction as R7-018 in
`$D0a-8XDYarvyPLYMfKbRvVIcsEaYLn2GtBqouYz-NDw`; astra-21 accepted the fix.
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
