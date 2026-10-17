# astra-23 vector run

Package: **0.2.3-draft** at `23290b3`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 49 | 3 | 0 | 52 |
| deployment | 0 | 0 | 1 | 1 |

Deployment unsupported means no qualification claim; modeled semantic erasure
and publication transitions do not exercise live authentication, storage or delivery.

## Per-vector results

| Vector | Profile | Result |
| --- | --- | --- |
| ASTRA24-08-CHALLENGE | semantic | pass |
| ASTRA24-08-CONTROL | semantic | pass |
| ASTRA24-08-NEXT | semantic | pass |
| ASTRA24-08-STALE | semantic | pass |
| ASTRA24-08 | semantic | pass |
| ASTRA24-10-CONTROL | semantic | pass |
| ASTRA24-10-PRIOR | semantic | fail |
| ASTRA24-10-SAME | semantic | fail |
| ASTRA24-10-TRANSITIVE | semantic | pass |
| ASTRA24-10 | semantic | fail |
| ASTRA24-07 | semantic | pass |
| ASTRA24-04 | semantic | pass |
| ASTRA24-03 | semantic | pass |
| ASTRA24-05 | semantic | pass |
| ASTRA24-01 | semantic | pass |
| ASTRA24-02 | semantic | pass |
| ASTRA24-06 | semantic | pass |
| ASTRA24-09 | semantic | pass |
| ASTRA25-02-DIGEST | semantic | pass |
| ASTRA25-02 | semantic | pass |
| ASTRA25-07-CONTROL | semantic | pass |
| ASTRA25-07-PURPOSE | semantic | pass |
| ASTRA25-07 | semantic | pass |
| ASTRA25-10 | semantic | pass |
| ASTRA25-05-CONTROL | semantic | pass |
| ASTRA25-05 | semantic | pass |
| ASTRA25-01 | semantic | pass |
| ASTRA25-06 | semantic | pass |
| ASTRA25-08-CONTROL | semantic | pass |
| ASTRA25-08-UNKNOWN-CONTROL | semantic | pass |
| ASTRA25-08-UNKNOWN | semantic | pass |
| ASTRA25-08 | semantic | pass |
| ASTRA25-04 | deployment | unsupported |
| ASTRA25-03-CONTROL | semantic | pass |
| ASTRA25-03-FENCE | semantic | pass |
| ASTRA25-03 | semantic | pass |
| ASTRA25-09-CONTROL | semantic | pass |
| ASTRA25-09 | semantic | pass |
| ASTRA26-07 | semantic | pass |
| ASTRA26-10 | semantic | pass |
| ASTRA26-08-CONTROL | semantic | pass |
| ASTRA26-08 | semantic | pass |
| ASTRA26-06 | semantic | pass |
| ASTRA26-01 | semantic | pass |
| ASTRA26-09-CONTROL | semantic | pass |
| ASTRA26-09-UNVERIFIED | semantic | pass |
| ASTRA26-09 | semantic | pass |
| ASTRA26-04 | semantic | pass |
| ASTRA26-02-CONTROL | semantic | pass |
| ASTRA26-02 | semantic | pass |
| ASTRA26-05 | semantic | pass |
| ASTRA26-03-CONTROL | semantic | pass |
| ASTRA26-03 | semantic | pass |

### ASTRA24-10-PRIOR

- `/operation_results/1/code`: actual `"<missing>"`; expected `"authority_receipt_required"`.
- `/operation_results/1/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/1/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/1/operation`: actual `"revise"`; expected `"<missing>"`.
- `/operation_results/1/outcome`: actual `"revised"`; expected `"<missing>"`.
- `/operation_results/1/receipt_handle`: actual `"8ec87e3320788da3ed46642e7a7c73c7"`; expected `"<missing>"`.
- `/operation_results/1/refs`: actual `[{"id":"rec:d","version":2},{"id":"rec:decision-replace","version":1}]`; expected `"<missing>"`.
- `/operation_results/1/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/1/type`: actual `"receipt"`; expected `"refusal"`.
- `/postconditions/dirty/length`: actual `1`; expected `0`.
- `/postconditions/dirty/0`: actual `{"id":"rec:dependent","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/length`: actual `7`; expected `5`.
- `/postconditions/record_refs/1/id`: actual `"rec:d"`; expected `"rec:dependent"`.
- `/postconditions/record_refs/1/version`: actual `2`; expected `1`.
- `/postconditions/record_refs/2/id`: actual `"rec:decision-replace"`; expected `"rec:receipt1"`.
- `/postconditions/record_refs/3/id`: actual `"rec:dependent"`; expected `"rec:receipt2"`.
- `/postconditions/record_refs/4/id`: actual `"rec:receipt1"`; expected `"rec:review-dependent"`.
- `/postconditions/record_refs/5`: actual `{"id":"rec:receipt2","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/6`: actual `{"id":"rec:review-dependent","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/1/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":7}
- forbidden predicate matched: {"path":"/postconditions/dirty","test":"size_equals","value":1}

### ASTRA24-10-SAME

- `/operation_results/1/code`: actual `"<missing>"`; expected `"authority_receipt_required"`.
- `/operation_results/1/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/1/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/1/operation`: actual `"revise"`; expected `"<missing>"`.
- `/operation_results/1/outcome`: actual `"revised"`; expected `"<missing>"`.
- `/operation_results/1/receipt_handle`: actual `"5a43c21c1c81257556f22e91b708c80a"`; expected `"<missing>"`.
- `/operation_results/1/refs`: actual `[{"id":"rec:d","version":2},{"id":"rec:decision-replace","version":1}]`; expected `"<missing>"`.
- `/operation_results/1/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/1/type`: actual `"receipt"`; expected `"refusal"`.
- `/postconditions/dirty/length`: actual `1`; expected `0`.
- `/postconditions/dirty/0`: actual `{"id":"rec:dependent","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/length`: actual `7`; expected `5`.
- `/postconditions/record_refs/1/id`: actual `"rec:d"`; expected `"rec:dependent"`.
- `/postconditions/record_refs/1/version`: actual `2`; expected `1`.
- `/postconditions/record_refs/2/id`: actual `"rec:decision-replace"`; expected `"rec:receipt1"`.
- `/postconditions/record_refs/3/id`: actual `"rec:dependent"`; expected `"rec:receipt2"`.
- `/postconditions/record_refs/4/id`: actual `"rec:receipt1"`; expected `"rec:review-dependent"`.
- `/postconditions/record_refs/5`: actual `{"id":"rec:receipt2","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/6`: actual `{"id":"rec:review-dependent","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/1/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":7}
- forbidden predicate matched: {"path":"/postconditions/dirty","test":"size_equals","value":1}

### ASTRA24-10

- `/operation_results/1/code`: actual `"<missing>"`; expected `"authority_receipt_required"`.
- `/operation_results/1/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/1/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/1/operation`: actual `"revise"`; expected `"<missing>"`.
- `/operation_results/1/outcome`: actual `"revised"`; expected `"<missing>"`.
- `/operation_results/1/receipt_handle`: actual `"a0da0efb9c11f608737b4e4e5e0621f8"`; expected `"<missing>"`.
- `/operation_results/1/refs`: actual `[{"id":"rec:d","version":2},{"id":"rec:decision-replace","version":1}]`; expected `"<missing>"`.
- `/operation_results/1/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/1/type`: actual `"receipt"`; expected `"refusal"`.
- `/postconditions/dirty/length`: actual `1`; expected `0`.
- `/postconditions/dirty/0`: actual `{"id":"rec:dependent","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/length`: actual `7`; expected `5`.
- `/postconditions/record_refs/1/id`: actual `"rec:d"`; expected `"rec:dependent"`.
- `/postconditions/record_refs/1/version`: actual `2`; expected `1`.
- `/postconditions/record_refs/2/id`: actual `"rec:decision-replace"`; expected `"rec:receipt1"`.
- `/postconditions/record_refs/3/id`: actual `"rec:dependent"`; expected `"rec:receipt2"`.
- `/postconditions/record_refs/4/id`: actual `"rec:receipt1"`; expected `"rec:review-dependent"`.
- `/postconditions/record_refs/5`: actual `{"id":"rec:receipt2","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/6`: actual `{"id":"rec:review-dependent","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/1/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":7}
- forbidden predicate matched: {"path":"/postconditions/dirty","test":"size_equals","value":1}

### ASTRA25-04

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

## Reproducibility

Implementation SHA-256:

- `common.py`: `22a4807a07818eb83109c38838c094c3e4cc5fcc76e74e9e831fd2860f8db033`
- `disclosure.py`: `ae3862f6fadbb8fe602d13bfd5774df0680c7cfba17a131684102d2cacad3366`
- `engine.py`: `cca7a0544c903e521b093c0906bc1e6e092bfe90e54284c7c122e522b344b450`
- `evaluator.py`: `098d8460eb181b881f77ef7aef724d696ae652f680c44cd5905ca7e4a6c11100`
- `run_vectors.py`: `20bf1acc55f090e3c8fbcba71f24dc95ea23cfafcb31abb911138d9fdbf2298a`
- `test_controls.py`: `6cd50b73ef952ba0cc5d14f2fadecbed37a2fbb9bc275644e22c96d8c0c1e083`
- `test_semantics.py`: `3189cb141f3d464c3bdc35117b2bfa189557f2920b434f12d634316275516bcb`

Full actual reports, exact differences and vector digests are in the adjacent JSON report.
