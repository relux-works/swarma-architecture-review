# ASTRA24-04: derived witness loses its exact source reference

Status: observed package-evaluator divergence; judge classification requested.
Owner: astra-24. Tested implementation: astra-23 `0008dc3`; matched package
`0.1.0-draft` at `0ef608a`. The committed fixture uses current 0.2.0 grammar.

## Clauses and two readings

K-EVAL-1 defines a rule witness through its required premise witnesses;
K-EVAL-3 preserves qualifications for found paths; K-EVAL-5 describes source
state over those paths and exact disclosed source references. Companion §4
preserves witness qualification and §7 preserves item provenance.

One reading collects source references only from assessments attached directly
to the displayed assertion. The other also retains authorized exact sources of
the found premise witness paths. The first loses the provenance at a rule edge.

## Minimal input

```text
S is an authorized, resolvable exact source.
A+ has a passing, current-required semantic assessment naming S.
Checked rule A+ -> B+ is the only witness for B.
Capture A, then recall B; all budgets suffice, no opposing evidence.
```

Expected A and B both disclose `source_refs: [{id: "rec:s", version: 1}]`.
B additionally carries the rule's `formal_entailment` qualification, but the
source itself stays the same exact source. No extra witness is invented.

## Actual execution

The package-only evaluator correctly reports B support as present, complete,
clean, and resolvable, with the expected qualifications and origin. A's direct
source reference is present. Only the derived B provenance disappears:

| JSON path | Expected | Actual |
| --- | --- | --- |
| `/result/items/0/source_refs/length` | 1 | 0 |
| `/result/items/0/source_refs/0` | `{"id":"rec:s","version":1}` | missing |

The declared equivalent-output comparison of A/B source refs and the explicit
forbidden empty source-ref predicate both fail for their intended reason.
The same omission appeared on the more complex ASTRA24-03 AND/OR fixture; this
case removes erasure and mixed source state from the reproducer.

## Recommendation and controls

Collect exact separately authorized source references through found proof paths,
then deduplicate and sort them. Do not collect hidden or failed proof candidates,
add unsupported roots, or invent source-corpus completeness. This is the
provenance-transitivity extension already accepted in source-adapter R7-013;
classification for the independent package evaluator remains the judge's.

The direct-root capture is the nearby positive control. The corrected source
adapter at `fb7df98` passes the entire current-grammar fixture. A package-only
run on its matching original schemas and a syntactically 0.1.0 version of the
same synthetic input reproduces the exact failure. That old-format reproduction
was built from original S03/S32 templates, never by relaxing the grammar.

## Evidence and limits

- Current fixture: `astra-24-derived-source-refs.vector.json`, SHA-256
  `1549f43f6bee45e9b98c71d0d7fec233c949460b4e9f217257747877a670bb36`.
- Seat-local `.temp/astra23-derived-source-refs-01.json` records original-release
  actual output, exact field differences and forbidden/pair failures.
- `.temp/derived-source-refs-0.1.vector.json` and
  `.temp/probe-package-0.1-owned-cases.py` preserve the matched old grammar lane.
- `.temp/astra22-owned-cases-06.json` records the source evaluator's exact pass;
  `.temp/case-vectors-validate-07.log` records current closed grammar, references,
  inventory, handle normalization and intended forbidden-value control.

No expected answer is passed into either executor. The package evaluator's
separate 0.2.0 syntax migration is pending; its list/null incompatibility is not
misreported here as this semantic failure. No deployment claim is made.
