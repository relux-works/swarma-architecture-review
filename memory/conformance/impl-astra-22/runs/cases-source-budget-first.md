# astra-22 vector results

Package: **0.2.1-draft**, package commit `f31d58f58d05de2ae4159dedaacfa1e32bdc656d`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `4e647ea02ad8a9f7df18a42925dfe47473c936a5`. Source core SHA-256: `d81a4ae9956802b82d4710d85dfc54efb5679c91eb623e6515e12d8907ba8b9e`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 13 | 1 | 8 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-01 | semantic | unsupported | Frozen core has no exact proof-path enumeration or changes output |
| ASTRA24-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-06 | semantic | fail | 11 exact differences |
| ASTRA25-02 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, deliver, revoke_declassification |
| ASTRA25-05-CONTROL | semantic | unsupported | Frozen core has no dirty/review-closure output |
| ASTRA25-05 | semantic | unsupported | Frozen core has no dirty/review-closure output |
| ASTRA25-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-04 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| ASTRA25-03-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03-FENCE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA26-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02 | semantic | unsupported | Frozen core has no imported-publication currentness state |
| ASTRA26-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |

## ASTRA24-06

11 exact differences

- `$.result.cutoffs.length`: expected `1`; actual `0`.
- `$.result.items[0].source_refs.length`: expected `0`; actual `1`.
- `$.result.items[0].support.evaluation`: expected `"incomplete"`; actual `"complete"`.
- `$.result.items[0].support.evidence_qualification.length`: expected `0`; actual `2`.
- `$.result.items[0].support.independent_root_count`: expected `0`; actual `1`.
- `$.result.items[0].support.premise_quality`: expected `"not_fully_checked"`; actual `"clean_path"`.
- `$.result.items[0].support.witness`: expected `"not_found"`; actual `"present"`.
- `$.result.items[0].support.witness_roots.length`: expected `0`; actual `1`.
- `forbidden:/result/items/0/support/witness`: expected `"predicate false"`; actual `{"path": "/result/items/0/support/witness", "test": "equals", "value": "present"}`.
- `forbidden:/result/items/0/support/evaluation`: expected `"predicate false"`; actual `{"path": "/result/items/0/support/evaluation", "test": "equals", "value": "complete"}`.
- `forbidden:/result/cutoffs`: expected `"predicate false"`; actual `{"path": "/result/cutoffs", "test": "equals", "value": []}`.

Full normalized actual reports and input hashes: `cases-source-budget-first.json`.
