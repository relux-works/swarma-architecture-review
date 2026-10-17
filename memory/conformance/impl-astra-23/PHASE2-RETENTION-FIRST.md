# astra-23 vector run

Package: **0.2.1-draft** at `f31d58f58d05de2ae4159dedaacfa1e32bdc656d`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 28 | 2 | 0 | 30 |
| deployment | 0 | 0 | 1 | 1 |

Deployment unsupported means no qualification claim; modeled semantic erasure
and publication transitions do not exercise live authentication, storage or delivery.

## Per-vector results

| Vector | Profile | Result |
| --- | --- | --- |
| ASTRA24-07 | semantic | pass |
| ASTRA24-04 | semantic | pass |
| ASTRA24-03 | semantic | pass |
| ASTRA24-05 | semantic | pass |
| ASTRA24-01 | semantic | pass |
| ASTRA24-02 | semantic | pass |
| ASTRA24-06 | semantic | pass |
| ASTRA25-02 | semantic | pass |
| ASTRA25-07-CONTROL | semantic | pass |
| ASTRA25-07 | semantic | fail |
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
| ASTRA26-07 | semantic | pass |
| ASTRA26-08-CONTROL | semantic | pass |
| ASTRA26-08 | semantic | pass |
| ASTRA26-06 | semantic | pass |
| ASTRA26-01 | semantic | pass |
| ASTRA26-04 | semantic | pass |
| ASTRA26-02-CONTROL | semantic | pass |
| ASTRA26-02 | semantic | pass |
| ASTRA26-05 | semantic | pass |
| ASTRA26-03-CONTROL | semantic | pass |
| ASTRA26-03 | semantic | pass |

### ASTRA25-07

- `/operation_results/0/refs/length`: actual `2`; expected `1`.
- `/operation_results/0/refs/1`: actual `{"id":"rec:summary","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/0/refs/1/id","test":"equals","value":"rec:summary"}

### ASTRA25-08

- `/operation_results/0/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"b0bca81d663ef710fd097d619e8341a2"`; expected `"<missing>"`.
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

## Reproducibility

Implementation SHA-256:

- `common.py`: `22a4807a07818eb83109c38838c094c3e4cc5fcc76e74e9e831fd2860f8db033`
- `disclosure.py`: `b0f057b04b8e1776c9cefea638607c4cea88df2b4477e78d7d8144104a6bd079`
- `engine.py`: `073f1f66f6440b370535d10182fe1ebf7a247319a872e4983762f34702674a5c`
- `evaluator.py`: `ff349c1fd1ae0feb398776069c4e43dbe348678268a3e2e0745e2eb62d8023ce`
- `run_vectors.py`: `20bf1acc55f090e3c8fbcba71f24dc95ea23cfafcb31abb911138d9fdbf2298a`
- `test_controls.py`: `6cd50b73ef952ba0cc5d14f2fadecbed37a2fbb9bc275644e22c96d8c0c1e083`
- `test_semantics.py`: `d02f2da07331dc46389816acb747b3bb8f08069d57948a0ea5caa7f9cbfa4154`

Full actual reports, exact differences and vector digests are in the adjacent JSON report.
