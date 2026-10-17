# astra-22 vector results

Package: **0.2.2-draft**, package commit `7e71765317088d4ac1ea6946fdfb4b2f8012643c`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `6b4248a39fb14827f5bcc2476a8762c352ba9ac2`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 26 | 3 | 9 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-08-CHALLENGE | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08-STALE | semantic | fail | 12 exact differences |
| ASTRA24-08 | semantic | fail | 12 exact differences |
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
| ASTRA26-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |

## ASTRA24-08-STALE

12 exact differences

- `$.operation_results[1].code`: expected `"version_conflict"`; actual `"<absent>"`.
- `$.operation_results[1].custody`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[1].erasure_status`: expected `"<absent>"`; actual `null`.
- `$.operation_results[1].operation`: expected `"<absent>"`; actual `"revise"`.
- `$.operation_results[1].outcome`: expected `"<absent>"`; actual `"revised"`.
- `$.operation_results[1].receipt_handle`: expected `"<absent>"`; actual `"c9fd21a17496ea1a4b8f3a5814fe9e38"`.
- `$.operation_results[1].refs`: expected `"<absent>"`; actual `[{"id": "rec:withdraw-candidate", "version": 1}]`.
- `$.operation_results[1].retryable`: expected `true`; actual `"<absent>"`.
- `$.operation_results[1].type`: expected `"refusal"`; actual `"receipt"`.
- `$.postconditions.record_refs.length`: expected `6`; actual `7`.
- `forbidden:/operation_results/1/type`: expected `"predicate false"`; actual `{"path": "/operation_results/1/type", "test": "equals", "value": "receipt"}`.
- `forbidden:/postconditions/record_refs`: expected `"predicate false"`; actual `{"path": "/postconditions/record_refs", "test": "size_equals", "value": 7}`.

## ASTRA24-08

12 exact differences

- `$.operation_results[1].code`: expected `"version_conflict"`; actual `"<absent>"`.
- `$.operation_results[1].custody`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[1].erasure_status`: expected `"<absent>"`; actual `null`.
- `$.operation_results[1].operation`: expected `"<absent>"`; actual `"revise"`.
- `$.operation_results[1].outcome`: expected `"<absent>"`; actual `"revised"`.
- `$.operation_results[1].receipt_handle`: expected `"<absent>"`; actual `"96e039d4d395a7918b5f9a5c14c0a27d"`.
- `$.operation_results[1].refs`: expected `"<absent>"`; actual `[{"id": "rec:withdraw-candidate", "version": 1}]`.
- `$.operation_results[1].retryable`: expected `true`; actual `"<absent>"`.
- `$.operation_results[1].type`: expected `"refusal"`; actual `"receipt"`.
- `$.postconditions.record_refs.length`: expected `6`; actual `7`.
- `forbidden:/operation_results/1/type`: expected `"predicate false"`; actual `{"path": "/operation_results/1/type", "test": "equals", "value": "receipt"}`.
- `forbidden:/postconditions/record_refs`: expected `"predicate false"`; actual `{"path": "/postconditions/record_refs", "test": "size_equals", "value": 7}`.

## ASTRA25-08

13 exact differences

- `$.operation_results[0].code`: expected `"not_authorized"`; actual `"<absent>"`.
- `$.operation_results[0].custody`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[0].erasure_status`: expected `"<absent>"`; actual `null`.
- `$.operation_results[0].operation`: expected `"<absent>"`; actual `"admit"`.
- `$.operation_results[0].outcome`: expected `"<absent>"`; actual `"admitted"`.
- `$.operation_results[0].receipt_handle`: expected `"<absent>"`; actual `"6b2899a80595eb3349c9327ed29eb412"`.
- `$.operation_results[0].refs`: expected `"<absent>"`; actual `[{"id": "rec:paraphrase", "version": 1}]`.
- `$.operation_results[0].retryable`: expected `false`; actual `"<absent>"`.
- `$.operation_results[0].type`: expected `"refusal"`; actual `"receipt"`.
- `$.postconditions.record_refs.length`: expected `1`; actual `2`.
- `$.postconditions.record_refs[0].id`: expected `"rec:private"`; actual `"rec:paraphrase"`.
- `forbidden:/operation_results/0/type`: expected `"predicate false"`; actual `{"path": "/operation_results/0/type", "test": "equals", "value": "receipt"}`.
- `forbidden:/postconditions/record_refs/0/id`: expected `"predicate false"`; actual `{"path": "/postconditions/record_refs/0/id", "test": "equals", "value": "rec:paraphrase"}`.

Full normalized actual reports and input hashes: `phase2-delivery-cases-first.json`.
