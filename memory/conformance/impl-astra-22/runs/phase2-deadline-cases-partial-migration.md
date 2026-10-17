# astra-22 vector results

Package: **0.2.5-draft**, package commit `6a04e8cfb1490569cd1de7468d2085dd4840cf51`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `50238bc067cf88246e3a309e3f9661807bf417fd`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 33 | 20 | 8 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-08-CHALLENGE | semantic | fail | 2 exact differences |
| ASTRA24-08-CONTROL | semantic | fail | 2 exact differences |
| ASTRA24-08-NEXT | semantic | fail | 3 exact differences |
| ASTRA24-08-STALE | semantic | fail | 2 exact differences |
| ASTRA24-08 | semantic | fail | 2 exact differences |
| ASTRA24-10-CONTROL | semantic | fail | 2 exact differences |
| ASTRA24-10-PRIOR | semantic | fail | 2 exact differences |
| ASTRA24-10-SAME | semantic | fail | 2 exact differences |
| ASTRA24-10-TRANSITIVE | semantic | fail | 2 exact differences |
| ASTRA24-10 | semantic | fail | 2 exact differences |
| ASTRA24-07 | semantic | fail | 2 exact differences |
| ASTRA24-04 | semantic | fail | 2 exact differences |
| ASTRA24-03 | semantic | fail | 3 exact differences |
| ASTRA24-05 | semantic | fail | 3 exact differences |
| ASTRA24-01 | semantic | fail | 2 exact differences |
| ASTRA24-11-CONTROL | semantic | fail | 1 exact differences |
| ASTRA24-11 | semantic | fail | 1 exact differences |
| ASTRA24-02 | semantic | fail | 4 exact differences |
| ASTRA24-06 | semantic | fail | 2 exact differences |
| ASTRA24-09 | semantic | fail | 2 exact differences |
| ASTRA25-02-DIGEST | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-07-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-07-PURPOSE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-07 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-05-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08-UNKNOWN-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08-UNKNOWN | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-11-BEFORE | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-11-OWN | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-11-REPLAY | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-11-BATCH-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-11-BATCH | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-11-UNKNOWN | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-11 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-04 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| ASTRA25-03-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03-FENCE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-09-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-09 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA26-07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
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

## ASTRA24-08-CHALLENGE

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-08-CONTROL

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-08-NEXT

3 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.operation_results[2].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-08-STALE

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-08

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-10-CONTROL

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-10-PRIOR

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-10-SAME

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-10-TRANSITIVE

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-10

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-07

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-04

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-03

3 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.operation_results[1].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-05

3 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.operation_results[1].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-01

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-11-CONTROL

1 exact differences

- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-11

1 exact differences

- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-02

4 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.operation_results[1].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.operation_results[2].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-06

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

## ASTRA24-09

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.
- `$.result.semantic_profile`: expected `"0.2.4-draft"`; actual `"0.2.5-draft"`.

Full normalized actual reports and input hashes: `phase2-deadline-cases-corrected.json`.
