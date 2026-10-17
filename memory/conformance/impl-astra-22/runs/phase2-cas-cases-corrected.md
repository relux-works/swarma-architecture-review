# astra-22 vector results

Package: **0.2.2-draft**, package commit `7e71765317088d4ac1ea6946fdfb4b2f8012643c`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `5d079be0dbf66b73a03ba61873107ae4782d3f15`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 31 | 1 | 9 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-08-CHALLENGE | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08-STALE | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-02 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, revoke_declassification |
| ASTRA25-07-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-07-PURPOSE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-07 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-05-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08 | semantic | fail | 13 exact differences |
| ASTRA25-04 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| ASTRA25-03-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03-FENCE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-09-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-09 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA26-07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-09-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-09-UNVERIFIED | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
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
- `$.operation_results[0].receipt_handle`: expected `"<absent>"`; actual `"aff576d671f80e4ae917db3cb0af6cdc"`.
- `$.operation_results[0].refs`: expected `"<absent>"`; actual `[{"id": "rec:paraphrase", "version": 1}]`.
- `$.operation_results[0].retryable`: expected `false`; actual `"<absent>"`.
- `$.operation_results[0].type`: expected `"refusal"`; actual `"receipt"`.
- `$.postconditions.record_refs.length`: expected `1`; actual `2`.
- `$.postconditions.record_refs[0].id`: expected `"rec:private"`; actual `"rec:paraphrase"`.
- `forbidden:/operation_results/0/type`: expected `"predicate false"`; actual `{"path": "/operation_results/0/type", "test": "equals", "value": "receipt"}`.
- `forbidden:/postconditions/record_refs/0/id`: expected `"predicate false"`; actual `{"path": "/postconditions/record_refs/0/id", "test": "equals", "value": "rec:paraphrase"}`.

Full normalized actual reports and input hashes: `phase2-cas-cases-corrected.json`.
