# astra-23 vector run

Package: **0.2.4-draft** at `ef0264702d3ff937bd34410ea80660b196b6f1b0`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 56 | 5 | 0 | 61 |
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
| ASTRA24-10-PRIOR | semantic | pass |
| ASTRA24-10-SAME | semantic | pass |
| ASTRA24-10-TRANSITIVE | semantic | pass |
| ASTRA24-10 | semantic | pass |
| ASTRA24-07 | semantic | pass |
| ASTRA24-04 | semantic | pass |
| ASTRA24-03 | semantic | pass |
| ASTRA24-05 | semantic | pass |
| ASTRA24-01 | semantic | pass |
| ASTRA24-11-CONTROL | semantic | pass |
| ASTRA24-11 | semantic | pass |
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
| ASTRA25-11-BEFORE | semantic | pass |
| ASTRA25-11-OWN | semantic | fail |
| ASTRA25-11-REPLAY | semantic | fail |
| ASTRA25-11-BATCH-CONTROL | semantic | pass |
| ASTRA25-11-BATCH | semantic | fail |
| ASTRA25-11-UNKNOWN | semantic | fail |
| ASTRA25-11 | semantic | fail |
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

### ASTRA25-11-OWN

- `/operation_results/0/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"36fcd1f3eda816db746b506a28acac57"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:paraphrase","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/postconditions/record_refs/length`: actual `2`; expected `1`.
- `/postconditions/record_refs/0/id`: actual `"rec:paraphrase"`; expected `"rec:private"`.
- `/postconditions/record_refs/1`: actual `{"id":"rec:private","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":2}

### ASTRA25-11-REPLAY

- `/operation_results/1/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/1/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/1/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/1/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/1/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/1/receipt_handle`: actual `"a4b91ab6990fbfa44d808179d85c5c42"`; expected `"<missing>"`.
- `/operation_results/1/refs`: actual `[{"id":"rec:paraphrase","version":1}]`; expected `"<missing>"`.
- `/operation_results/1/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/1/type`: actual `"receipt"`; expected `"refusal"`.
- forbidden predicate matched: {"path":"/operation_results/1/type","test":"equals","value":"receipt"}

### ASTRA25-11-BATCH

- `/operation_results/0/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"9fcf70801772af1be4c4a578024da6e1"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:paraphrase","version":1},{"id":"rec:private","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/1/code`: actual `"duplicate_record"`; expected `"not_authorized"`.
- `/postconditions/record_refs/length`: actual `2`; expected `0`.
- `/postconditions/record_refs/0`: actual `{"id":"rec:paraphrase","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/1`: actual `{"id":"rec:private","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":2}

### ASTRA25-11-UNKNOWN

- `/operation_results/0/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"b185afc7ded5c5b916ea4d3ef172e8a8"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:paraphrase","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/postconditions/record_refs/length`: actual `3`; expected `2`.
- `/postconditions/record_refs/1/id`: actual `"rec:paraphrase"`; expected `"rec:private"`.
- `/postconditions/record_refs/2`: actual `{"id":"rec:private","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":3}

### ASTRA25-11

- `/operation_results/0/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"e24e7841ee0c08fc44ea8b6b28b01953"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:paraphrase","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/1/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/1/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/1/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/1/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/1/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/1/receipt_handle`: actual `"e24e7841ee0c08fc44ea8b6b28b01953"`; expected `"<missing>"`.
- `/operation_results/1/refs`: actual `[{"id":"rec:paraphrase","version":1}]`; expected `"<missing>"`.
- `/operation_results/1/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/1/type`: actual `"receipt"`; expected `"refusal"`.
- `/postconditions/record_refs/length`: actual `2`; expected `1`.
- `/postconditions/record_refs/0/id`: actual `"rec:paraphrase"`; expected `"rec:private"`.
- `/postconditions/record_refs/1`: actual `{"id":"rec:private","version":1}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/1/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":2}

### ASTRA25-04

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

## Reproducibility

Implementation SHA-256:

- `common.py`: `22a4807a07818eb83109c38838c094c3e4cc5fcc76e74e9e831fd2860f8db033`
- `disclosure.py`: `ae3862f6fadbb8fe602d13bfd5774df0680c7cfba17a131684102d2cacad3366`
- `engine.py`: `8caa70d0090ccecea13846bbfd2180b634255ebb8413a15a4389c595e61aec29`
- `evaluator.py`: `098d8460eb181b881f77ef7aef724d696ae652f680c44cd5905ca7e4a6c11100`
- `run_vectors.py`: `20bf1acc55f090e3c8fbcba71f24dc95ea23cfafcb31abb911138d9fdbf2298a`
- `test_controls.py`: `6cd50b73ef952ba0cc5d14f2fadecbed37a2fbb9bc275644e22c96d8c0c1e083`
- `test_semantics.py`: `85dc6e84bea0a658766ff5fd47f51b2dd8fa24c4d64f7d0156859fe29e000a31`

Full actual reports, exact differences and vector digests are in the adjacent JSON report.
