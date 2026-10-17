# astra-22 vector results

Package: **0.2.1-draft**, package commit `f31d58f58d05de2ae4159dedaacfa1e32bdc656d`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `26d8cc680d502f01e202561b3e2b497897a27c3a`. Source core SHA-256: `8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 10 | 2 | 8 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-01 | semantic | unsupported | Frozen core has no exact proof-path enumeration or changes output |
| ASTRA24-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-02 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, deliver, revoke_declassification |
| ASTRA25-05-CONTROL | semantic | unsupported | Frozen core has no dirty/review-closure output |
| ASTRA25-05 | semantic | unsupported | Frozen core has no dirty/review-closure output |
| ASTRA25-01 | semantic | fail | 7 exact differences |
| ASTRA25-06 | semantic | fail | 16 exact differences |
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

## ASTRA25-01

7 exact differences

- `$.result.cutoffs.length`: expected `0`; actual `1`.
- `$.result.items[0].support.evaluation`: expected `"complete"`; actual `"incomplete"`.
- `$.result.items[0].support.evidence_qualification.length`: expected `2`; actual `0`.
- `$.result.items[0].support.independent_root_count`: expected `1`; actual `0`.
- `$.result.items[0].support.premise_quality`: expected `"conflicted_premises_only"`; actual `"not_fully_checked"`.
- `$.result.items[0].support.witness`: expected `"present"`; actual `"not_found"`.
- `$.result.items[0].support.witness_roots.length`: expected `1`; actual `0`.

## ASTRA25-06

16 exact differences

- `$.result.cutoffs.length`: expected `0`; actual `1`.
- `$.result.items[0].support.evaluation`: expected `"complete"`; actual `"incomplete"`.
- `$.result.items[0].support.evidence_qualification.length`: expected `2`; actual `0`.
- `$.result.items[0].support.independent_root_count`: expected `1`; actual `0`.
- `$.result.items[0].support.premise_quality`: expected `"conflicted_premises_only"`; actual `"not_fully_checked"`.
- `$.result.items[0].support.witness`: expected `"present"`; actual `"not_found"`.
- `$.result.items[0].support.witness_roots.length`: expected `1`; actual `0`.
- `pair:/operation_results/0=/result.cutoffs.length`: expected `0`; actual `1`.
- `pair:/operation_results/0=/result.items[0].support.evaluation`: expected `"complete"`; actual `"incomplete"`.
- `pair:/operation_results/0=/result.items[0].support.evidence_qualification.length`: expected `2`; actual `0`.
- `pair:/operation_results/0=/result.items[0].support.independent_root_count`: expected `1`; actual `0`.
- `pair:/operation_results/0=/result.items[0].support.premise_quality`: expected `"conflicted_premises_only"`; actual `"not_fully_checked"`.
- `pair:/operation_results/0=/result.items[0].support.witness`: expected `"present"`; actual `"not_found"`.
- `pair:/operation_results/0=/result.items[0].support.witness_roots.length`: expected `1`; actual `0`.
- `forbidden:/result/items/0/support/witness`: expected `"predicate false"`; actual `{"path": "/result/items/0/support/witness", "test": "equals", "value": "not_found"}`.
- `forbidden:/result/items/0/support/evaluation`: expected `"predicate false"`; actual `{"path": "/result/items/0/support/evaluation", "test": "equals", "value": "incomplete"}`.

Full normalized actual reports and input hashes: `cases-0.2.1-first.json`.
