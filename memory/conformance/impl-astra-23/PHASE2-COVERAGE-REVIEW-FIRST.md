# astra-23 vector run

Package: **0.2.2-draft** at `7e71765317088d4ac1ea6946fdfb4b2f8012643c`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 39 | 3 | 0 | 42 |
| deployment | 0 | 0 | 1 | 1 |

Deployment unsupported means no qualification claim; modeled semantic erasure
and publication transitions do not exercise live authentication, storage or delivery.

## Per-vector results

| Vector | Profile | Result |
| --- | --- | --- |
| ASTRA24-08-CHALLENGE | semantic | pass |
| ASTRA24-08-CONTROL | semantic | pass |
| ASTRA24-08-STALE | semantic | pass |
| ASTRA24-08 | semantic | pass |
| ASTRA24-07 | semantic | pass |
| ASTRA24-04 | semantic | pass |
| ASTRA24-03 | semantic | pass |
| ASTRA24-05 | semantic | pass |
| ASTRA24-01 | semantic | pass |
| ASTRA24-02 | semantic | pass |
| ASTRA24-06 | semantic | pass |
| ASTRA24-09 | semantic | fail |
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
| ASTRA25-08 | semantic | fail |
| ASTRA25-04 | deployment | unsupported |
| ASTRA25-03-CONTROL | semantic | pass |
| ASTRA25-03-FENCE | semantic | pass |
| ASTRA25-03 | semantic | pass |
| ASTRA25-09-CONTROL | semantic | pass |
| ASTRA25-09 | semantic | pass |
| ASTRA26-07 | semantic | pass |
| ASTRA26-08-CONTROL | semantic | pass |
| ASTRA26-08 | semantic | pass |
| ASTRA26-06 | semantic | pass |
| ASTRA26-01 | semantic | pass |
| ASTRA26-09-CONTROL | semantic | pass |
| ASTRA26-09-UNVERIFIED | semantic | pass |
| ASTRA26-09 | semantic | fail |
| ASTRA26-04 | semantic | pass |
| ASTRA26-02-CONTROL | semantic | pass |
| ASTRA26-02 | semantic | pass |
| ASTRA26-05 | semantic | pass |
| ASTRA26-03-CONTROL | semantic | pass |
| ASTRA26-03 | semantic | pass |

### ASTRA24-09

- `/result/review_required/length`: actual `1`; expected `2`.
- `/result/review_required/1`: actual `"<missing>"`; expected `{"id":"rec:dependent-c","version":1}`.
- forbidden predicate matched: {"path":"/result/review_required","test":"size_equals","value":1}

### ASTRA25-08

- `/operation_results/0/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"091d7dd88abbb6f9b3992c819dd51f0f"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:paraphrase","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/postconditions/record_refs/length`: actual `2`; expected `1`.
- `/postconditions/record_refs/0/id`: actual `"rec:paraphrase"`; expected `"rec:private"`.
- `/postconditions/record_refs/1`: actual `{"id":"rec:private","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs/0/id","test":"equals","value":"rec:paraphrase"}

### ASTRA25-04

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### ASTRA26-09

- `/result/currentness`: actual `"current"`; expected `"last_received"`.
- `/result/items/0/currentness`: actual `"current"`; expected `"last_received"`.
- forbidden predicate matched: {"path":"/result/currentness","test":"equals","value":"current"}
- forbidden predicate matched: {"path":"/result/items/0/currentness","test":"equals","value":"current"}

## Reproducibility

Implementation SHA-256:

- `common.py`: `22a4807a07818eb83109c38838c094c3e4cc5fcc76e74e9e831fd2860f8db033`
- `disclosure.py`: `ae3862f6fadbb8fe602d13bfd5774df0680c7cfba17a131684102d2cacad3366`
- `engine.py`: `80390b7debd8badde99a8f30f91b506b02e5c0ed987847644b6f03bcdaf32a1e`
- `evaluator.py`: `491182ea05761dc082cb68ccaafc670e212c0fa03f023762fd571b24dfb642f1`
- `run_vectors.py`: `20bf1acc55f090e3c8fbcba71f24dc95ea23cfafcb31abb911138d9fdbf2298a`
- `test_controls.py`: `6cd50b73ef952ba0cc5d14f2fadecbed37a2fbb9bc275644e22c96d8c0c1e083`
- `test_semantics.py`: `d54f157aac14c0a4a15fa045d5c6112c54ebb2acb0d41b5ad2eb0ad9c5aabd3b`

Full actual reports, exact differences and vector digests are in the adjacent JSON report.
