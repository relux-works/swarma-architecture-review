# astra-22 vector results

Package: **0.2.2-draft**, package commit `7e71765317088d4ac1ea6946fdfb4b2f8012643c`.
Vector directory: `memory/conformance/impl-astra-22/fixtures/dirty-rule-certificate` (this inventory only).
Checkout: `68152c58c1d19eb50ce42d5cddb93cc4b8cc6216`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 1 | 2 | 0 |
| deployment | 0 | 0 | 0 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| JUDGE-DIRTY-CERTIFICATE | semantic | fail | 7 exact differences |
| JUDGE-DIRTY-PREMISE-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| JUDGE-DIRTY-RULE | semantic | fail | 7 exact differences |

## JUDGE-DIRTY-CERTIFICATE

7 exact differences

- `$.postconditions.dirty.length`: expected `1`; actual `0`.
- `$.result.cutoffs.length`: expected `1`; actual `0`.
- `$.result.items[0].needs_review`: expected `true`; actual `false`.
- `$.result.items[0].oppose.evaluation`: expected `"incomplete"`; actual `"complete"`.
- `$.result.items[0].support.evaluation`: expected `"incomplete"`; actual `"complete"`.
- `$.result.review_required.length`: expected `1`; actual `0`.
- `forbidden:/result/items/0/support/evaluation`: expected `"predicate false"`; actual `{"path": "/result/items/0/support/evaluation", "test": "equals", "value": "complete"}`.

## JUDGE-DIRTY-RULE

7 exact differences

- `$.postconditions.dirty.length`: expected `1`; actual `0`.
- `$.result.cutoffs.length`: expected `1`; actual `0`.
- `$.result.items[0].needs_review`: expected `true`; actual `false`.
- `$.result.items[0].oppose.evaluation`: expected `"incomplete"`; actual `"complete"`.
- `$.result.items[0].support.evaluation`: expected `"incomplete"`; actual `"complete"`.
- `$.result.review_required.length`: expected `1`; actual `0`.
- `forbidden:/result/items/0/support/evaluation`: expected `"predicate false"`; actual `{"path": "/result/items/0/support/evaluation", "test": "equals", "value": "complete"}`.

Full normalized actual reports and input hashes: `dirty-rule-certificate-first.json`.
