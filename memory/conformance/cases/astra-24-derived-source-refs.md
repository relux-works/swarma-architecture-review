# ASTRA24-04: derived witness loses its exact source reference

Status: R7-023 fixed at `7c765fe`, independently verified; judge-closed at `73ebb62`.
Owner: astra-24. Tested implementation: astra-23 `0008dc3`; matched package
`0.1.0-draft` at `0ef608a`. The committed fixture now uses 0.2.1 grammar; historical runs below retain their stated profiles.

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

## Current-release reproduction and consolidation — round 6

At checkout `dcde639`, the current package evaluator (0.2.0 adaptation
`1439219`, supplemental report `103ce15`) reproduces exactly the same missing
B source-reference array against the committed 0.2.0 fixture. Its direct A
control passes. Therefore this is not a cross-version syntax artifact. The
corrected source evaluator at `8b97e1e` passes the same exact input and output.

ASTRA24-03's two missing provenance arrays, this minimal ASTRA24-04 and the
package implementer's `div-astra23-derived-source-refs` report are one property
and should receive one consolidated defect classification. No second defect
is alleged for the mixed case's already-correct source state.

Evidence: `.temp/astra23-owned-cases-02.json`,
`.temp/astra22-owned-cases-07.json`, `.temp/case-vectors-validate-08.log`;
package 0.2.0 passes its structural checker (57 semantic, 8 deployment,
16 intended checker controls) in `.temp/package-validate-02.log`.

Judge disposition: R7-023 is one consolidated `impl-bug`, owner astra-23,
covering ASTRA24-04, the ASTRA24-03 provenance rows and the implementer's own
report. Exact expected outputs stand. The requested repair preserves sources
from found premise paths while excluding hidden/unfound candidates and unrelated
same-origin copies. Implementation fix and follow-up verification remain pending.

## 0.2.1 verification — round 7

The fixture now supplies explicit `policy.subject_principals` and empty
`runtime.dirty_causes`, with the 0.2.1 semantic profile. Its semantic expectations
are unchanged. Closed grammar, references, normalization and intended forbidden
plants pass in `.temp/case-vectors-validate-09.log`.

Current fixture SHA-256: `a6ed86068752d579b6426f0dfba610a1f50415a46c0e3323f6ce05cbf63b0558`.
At checkout `4fadedd`, package evaluator fix `7c765fe` passes the entire
fixture. Source evaluator also passes the entire fixture.
Exact reports: `.temp/astra23-owned-cases-03.json` and
`.temp/astra22-owned-cases-08.json`. Executors receive no expected outputs.

The formerly failing derived B reference now equals the direct A reference;
exact, paired and forbidden checks all pass. The implementer
`test_semantics.Semantics.test_derived_source_references` independently passes
positive direct/derived controls and hidden-source, failed-assessment and
unrelated same-origin-copy negative controls under this release. Evidence:
`.temp/astra23-derived-controls-02.log`. The prior `-01.log` records only an
incorrect-working-directory import failure, not a product result. Judge `73ebb62`
closed R7-023 after its own pinned verification. Original failing reports remain.

These are semantic fixture results, not protected deployment qualification.

## Package 0.2.2 profile migration

Round 15 explicitly migrated the vector to `0.2.2-draft` at release `7e71765`.
Only semantic_profile metadata changed; no input or behavioral expectation
changed. This seat has no erase operation requiring the new receipt context.
Normalized equality and old/new hashes are recorded in
`.temp/astra24-profile-022-migration.json`. Both evaluators preserve this case's
pass in source report19 and package report11. Earlier hashes above identify
the historical profile-specific runs.

## Package 0.2.3 explicit migration

Round 21 migrates this case to `0.2.3-draft` (`23290b3`). Behavioral expected
results and initial states are unchanged. Read-only operations need no storage
context; each of this seat's six revise operations explicitly binds private/read
under its existing actor/space/record retain grant. No grant is inferred from a
later query. `.temp/astra24-profile-023-migration.json` records old/new hashes,
exact operation contexts and normalized equality. Structural and intended
forbidden controls pass log 22. Earlier hashes identify historical profile runs.

## Round 27 profile migration to 0.2.4

Current exact fixtures explicitly name `0.2.4-draft` from release `ef02647`.
Only expected-view `semantic_profile` values changed; initial state, operations,
queries and behavioral expectations are byte-equivalent after that declared
normalization. All twenty owned fixtures pass structural and intended forbidden
controls (log27). `.temp/astra24-profile-024-migration.json` records old/new hashes
and every changed path. Historical hashes and first reports remain unchanged.
