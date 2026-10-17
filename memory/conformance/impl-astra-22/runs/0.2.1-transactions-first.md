# astra-22 vector results

Package: **0.2.1-draft**, package commit `f31d58f58d05de2ae4159dedaacfa1e32bdc656d`.
Vector directory: `memory/spec/kernel/vectors` (this inventory only).
Checkout: `c4bd6b3c793baa6ae0bbd9d3102d9cbc67e99d6b`. Source core SHA-256: `8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 42 | 1 | 14 |
| deployment | 0 | 0 | 8 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| B04 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B05 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B06 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B09 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B10 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B11 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B16 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B17 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B01 | semantic | unsupported | Frozen core has no dirty/review-closure output |
| B02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B07 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| B08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B12 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B13 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P02 | semantic | fail | 15 exact differences |
| P03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P05 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, deliver, revoke_declassification |
| P06 | semantic | unsupported | Unmapped frozen-core transaction operations: deliver, revoke |
| P07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P08 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| P09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P11 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P12 | semantic | unsupported | Unmapped frozen-core transaction operations: deliver, revoke |
| P13 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S07 | semantic | unsupported | Frozen core has no exact proof-path enumeration or changes output |
| S08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S11 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S12 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S13 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S16 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S17 | semantic | unsupported | Frozen core has no dirty/review-closure output |
| S18 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S19 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S20 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| S21 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S22 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S23 | semantic | unsupported | Frozen core has no imported-publication currentness state |
| S24 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| S25 | semantic | unsupported | Unmapped frozen-core transaction operations: erase, reconcile_restore, restore |
| S26 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| S27 | semantic | unsupported | Unmapped frozen-core transaction operations: load, set_availability |
| S28 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S29 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S30 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S31 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S32 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S33 | semantic | pass | Exact report and forbidden/normalization checks passed. |

## P02

15 exact differences

- `$.operation_results[1].code`: expected `"invalid_domain_value"`; actual `"<absent>"`.
- `$.operation_results[1].custody`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[1].erasure_status`: expected `"<absent>"`; actual `null`.
- `$.operation_results[1].operation`: expected `"<absent>"`; actual `"admit"`.
- `$.operation_results[1].outcome`: expected `"<absent>"`; actual `"admitted"`.
- `$.operation_results[1].receipt_handle`: expected `"<absent>"`; actual `"3b2d9f0277314883b6aff1f71e2cd436"`.
- `$.operation_results[1].refs`: expected `"<absent>"`; actual `[{"id": "rec:foreign-interest", "version": 1}]`.
- `$.operation_results[1].retryable`: expected `false`; actual `"<absent>"`.
- `$.operation_results[1].type`: expected `"refusal"`; actual `"receipt"`.
- `$.operation_results[3].currentness`: expected `"current"`; actual `"none"`.
- `$.operation_results[3].items.length`: expected `1`; actual `0`.
- `$.postconditions.record_refs.length`: expected `2`; actual `3`.
- `$.postconditions.record_refs[0].id`: expected `"rec:interest"`; actual `"rec:foreign-interest"`.
- `$.postconditions.record_refs[1].id`: expected `"rec:own-interest"`; actual `"rec:interest"`.
- `forbidden:/operation_results/1/type`: expected `"predicate false"`; actual `{"path": "/operation_results/1/type", "test": "equals", "value": "receipt"}`.

Full normalized actual reports and input hashes: `0.2.1-transactions-first.json`.
