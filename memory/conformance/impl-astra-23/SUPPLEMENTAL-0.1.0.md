# astra-23 vector run

Package: **0.1.0-draft** at `0ef608a`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 7 | 2 | 8 | 17 |
| deployment | 0 | 0 | 0 | 0 |

Deployment unsupported means no qualification claim; modeled semantic erasure
and publication transitions do not exercise live authentication, storage or delivery.

## Per-vector results

| Vector | Profile | Result |
| --- | --- | --- |
| ASTRA24-03 | semantic | fail |
| ASTRA24-01 | semantic | pass |
| ASTRA24-02 | semantic | pass |
| ASTRA25-05-CONTROL | semantic | pass |
| ASTRA25-05 | semantic | fail |
| ASTRA25-01 | semantic | pass |
| ASTRA25-03-CONTROL | semantic | pass |
| ASTRA25-03-FENCE | semantic | pass |
| ASTRA25-03 | semantic | pass |
| ASTRA26-06 | semantic | unsupported |
| ASTRA26-01 | semantic | unsupported |
| ASTRA26-04 | semantic | unsupported |
| ASTRA26-02-CONTROL | semantic | unsupported |
| ASTRA26-02 | semantic | unsupported |
| ASTRA26-05 | semantic | unsupported |
| ASTRA26-03-CONTROL | semantic | unsupported |
| ASTRA26-03 | semantic | unsupported |

### ASTRA24-03

- `/operation_results/1/items/0/source_refs/length`: actual `0`; expected `1`.
- `/operation_results/1/items/0/source_refs/0`: actual `"<missing>"`; expected `{"id":"rec:s","version":1}`.
- `/result/items/0/source_refs/length`: actual `0`; expected `1`.
- `/result/items/0/source_refs/0`: actual `"<missing>"`; expected `{"id":"rec:s","version":1}`.

### ASTRA25-05

- `/result/cutoffs/length`: actual `1`; expected `0`.
- `/result/cutoffs/0`: actual `"dirty"`; expected `"<missing>"`.
- `/result/items/0/needs_review`: actual `true`; expected `false`.
- `/result/items/0/oppose/evaluation`: actual `"incomplete"`; expected `"complete"`.
- `/result/items/0/support/evaluation`: actual `"incomplete"`; expected `"complete"`.
- `/result/items/0/support/evidence_qualification/length`: actual `0`; expected `1`.
- `/result/items/0/support/evidence_qualification/0`: actual `"<missing>"`; expected `"semantic_review"`.
- `/result/items/0/support/independent_root_count`: actual `0`; expected `1`.
- `/result/items/0/support/premise_quality`: actual `"not_fully_checked"`; expected `"clean_path"`.
- `/result/items/0/support/witness`: actual `"not_found"`; expected `"present"`.
- `/result/items/0/support/witness_roots/length`: actual `0`; expected `1`.
- `/result/items/0/support/witness_roots/0`: actual `"<missing>"`; expected `"origin:eb"`.
- `/result/review_required/length`: actual `1`; expected `0`.
- `/result/review_required/0`: actual `{"id":"rec:b","version":1}`; expected `"<missing>"`.
- equivalent_outputs violated: /operation_results/0 != /result
- forbidden predicate matched: {"path":"/result/items/0/support/evaluation","test":"equals","value":"incomplete"}
- forbidden predicate matched: {"path":"/result/items/0/needs_review","test":"equals","value":true}

### ASTRA26-06

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA26-01

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA26-04

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA26-02-CONTROL

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA26-02

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA26-05

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA26-03-CONTROL

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA26-03

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

## Reproducibility

Implementation SHA-256:

- `common.py`: `22a4807a07818eb83109c38838c094c3e4cc5fcc76e74e9e831fd2860f8db033`
- `disclosure.py`: `b0f057b04b8e1776c9cefea638607c4cea88df2b4477e78d7d8144104a6bd079`
- `engine.py`: `601939ae52a7ecd7ed7395c27f40862ec5b756f2be78fa020a3e9644a681bda2`
- `evaluator.py`: `381e1da34e86c193cf8a15c5057a6171aa0727428a35b0bca37744598a9e8eca`
- `run_vectors.py`: `20bf1acc55f090e3c8fbcba71f24dc95ea23cfafcb31abb911138d9fdbf2298a`
- `test_controls.py`: `6cd50b73ef952ba0cc5d14f2fadecbed37a2fbb9bc275644e22c96d8c0c1e083`
- `test_semantics.py`: `113cb8012ce6fdd50524bd914efb9f4791e00e13abba3e703dea89bb0fa0856d`

Full actual reports, exact differences and vector digests are in the adjacent JSON report.
