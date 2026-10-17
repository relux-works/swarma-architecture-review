# astra-22 vector results

Package: **0.2.1-draft**, package commit `f31d58f58d05de2ae4159dedaacfa1e32bdc656d`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `945096f65013c22ccc5095ecd4da5783e0e78e0f`. Source core SHA-256: `999b53173fb7fe7127b5a1370b31f988e71f1f8a1fecfa922c4febb3eee6b0cc`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 17 | 2 | 11 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-02 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, deliver, revoke_declassification |
| ASTRA25-07-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-07 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-05-CONTROL | semantic | unsupported | Frozen core has no dirty/review-closure output |
| ASTRA25-05 | semantic | unsupported | Frozen core has no dirty/review-closure output |
| ASTRA25-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08 | semantic | fail | 13 exact differences |
| ASTRA25-04 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| ASTRA25-03-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03-FENCE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA26-07 | semantic | fail | 4 exact differences |
| ASTRA26-08-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: deliver, revoke |
| ASTRA26-08 | semantic | unsupported | Unmapped frozen-core transaction operations: deliver, revoke |
| ASTRA26-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02 | semantic | unsupported | Frozen core has no imported-publication currentness state |
| ASTRA26-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |

## ASTRA25-08

13 exact differences

- `$.operation_results[0].code`: expected `"not_authorized"`; actual `"<absent>"`.
- `$.operation_results[0].custody`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[0].erasure_status`: expected `"<absent>"`; actual `null`.
- `$.operation_results[0].operation`: expected `"<absent>"`; actual `"admit"`.
- `$.operation_results[0].outcome`: expected `"<absent>"`; actual `"admitted"`.
- `$.operation_results[0].receipt_handle`: expected `"<absent>"`; actual `"049b815dfaafebd6ba66fa252a1e6c4c"`.
- `$.operation_results[0].refs`: expected `"<absent>"`; actual `[{"id": "rec:paraphrase", "version": 1}]`.
- `$.operation_results[0].retryable`: expected `false`; actual `"<absent>"`.
- `$.operation_results[0].type`: expected `"refusal"`; actual `"receipt"`.
- `$.postconditions.record_refs.length`: expected `1`; actual `2`.
- `$.postconditions.record_refs[0].id`: expected `"rec:private"`; actual `"rec:paraphrase"`.
- `forbidden:/operation_results/0/type`: expected `"predicate false"`; actual `{"path": "/operation_results/0/type", "test": "equals", "value": "receipt"}`.
- `forbidden:/postconditions/record_refs/0/id`: expected `"predicate false"`; actual `{"path": "/postconditions/record_refs/0/id", "test": "equals", "value": "rec:paraphrase"}`.

## ASTRA26-07

4 exact differences

- `$.result.currentness`: expected `"last_received"`; actual `"current"`.
- `$.result.items[0].currentness`: expected `"last_received"`; actual `"current"`.
- `forbidden:/result/currentness`: expected `"predicate false"`; actual `{"path": "/result/currentness", "test": "equals", "value": "current"}`.
- `forbidden:/result/items/0/currentness`: expected `"predicate false"`; actual `{"path": "/result/items/0/currentness", "test": "equals", "value": "current"}`.

Full normalized actual reports and input hashes: `phase2-expanded-first.json`.
