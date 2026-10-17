# astra-23 vector run

Package: **0.2.5-draft** at `6a04e8cfb1490569cd1de7468d2085dd4840cf51`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 56 | 1 | 0 | 57 |
| deployment | 0 | 0 | 8 | 8 |

Deployment unsupported means no qualification claim; modeled semantic erasure
and publication transitions do not exercise live authentication, storage or delivery.

## Per-vector results

| Vector | Profile | Result |
| --- | --- | --- |
| B04 | deployment | unsupported |
| B05 | deployment | unsupported |
| B06 | deployment | unsupported |
| B09 | deployment | unsupported |
| B10 | deployment | unsupported |
| B11 | deployment | unsupported |
| B16 | deployment | unsupported |
| B17 | deployment | unsupported |
| B01 | semantic | pass |
| B02 | semantic | pass |
| B03 | semantic | pass |
| B07 | semantic | pass |
| B08 | semantic | pass |
| B12 | semantic | pass |
| B13 | semantic | pass |
| B14 | semantic | pass |
| B15 | semantic | pass |
| P01 | semantic | pass |
| P02 | semantic | pass |
| P03 | semantic | pass |
| P04 | semantic | pass |
| P05 | semantic | pass |
| P06 | semantic | pass |
| P07 | semantic | pass |
| P08 | semantic | pass |
| P09 | semantic | pass |
| P10 | semantic | pass |
| P11 | semantic | fail |
| P12 | semantic | pass |
| P13 | semantic | pass |
| P14 | semantic | pass |
| P15 | semantic | pass |
| S01 | semantic | pass |
| S02 | semantic | pass |
| S03 | semantic | pass |
| S04 | semantic | pass |
| S05 | semantic | pass |
| S06 | semantic | pass |
| S07 | semantic | pass |
| S08 | semantic | pass |
| S09 | semantic | pass |
| S10 | semantic | pass |
| S11 | semantic | pass |
| S12 | semantic | pass |
| S13 | semantic | pass |
| S14 | semantic | pass |
| S15 | semantic | pass |
| S16 | semantic | pass |
| S17 | semantic | pass |
| S18 | semantic | pass |
| S19 | semantic | pass |
| S20 | semantic | pass |
| S21 | semantic | pass |
| S22 | semantic | pass |
| S23 | semantic | pass |
| S24 | semantic | pass |
| S25 | semantic | pass |
| S26 | semantic | pass |
| S27 | semantic | pass |
| S28 | semantic | pass |
| S29 | semantic | pass |
| S30 | semantic | pass |
| S31 | semantic | pass |
| S32 | semantic | pass |
| S33 | semantic | pass |

### B04

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### B05

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### B06

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### B09

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### B10

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### B11

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### B16

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### B17

Requires a real protected deployment; this evaluator implements synthetic state transitions only.

### P11

- `/operation_results/18/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/18/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/18/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/18/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/18/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/18/receipt_handle`: actual `"0f4ffabd8c3b50737893740cb94dd16d"`; expected `"<missing>"`.
- `/operation_results/18/refs`: actual `[{"id":"rec:deadline-live","version":1}]`; expected `"<missing>"`.
- `/operation_results/18/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/18/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/19/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/19/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/19/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/19/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/19/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/19/receipt_handle`: actual `"5c8edcc49a425ceccc3d9a1a0692beea"`; expected `"<missing>"`.
- `/operation_results/19/refs`: actual `[{"id":"rec:deadline-late","version":1}]`; expected `"<missing>"`.
- `/operation_results/19/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/19/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/20/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/20/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/20/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/20/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/20/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/20/receipt_handle`: actual `"712a304ccae273d93fdcca2ffa8ccbc7"`; expected `"<missing>"`.
- `/operation_results/20/refs`: actual `[{"id":"rec:deadline-open","version":1}]`; expected `"<missing>"`.
- `/operation_results/20/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/20/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/21/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/21/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/21/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/21/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/21/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/21/receipt_handle`: actual `"091b8d583324a845c103efa4e657908d"`; expected `"<missing>"`.
- `/operation_results/21/refs`: actual `[{"id":"rec:deadline-unknown","version":1}]`; expected `"<missing>"`.
- `/operation_results/21/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/21/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/22/code`: actual `"idempotency_conflict"`; expected `"not_authorized"`.
- `/operation_results/23/code`: actual `"idempotency_conflict"`; expected `"not_authorized"`.
- `/operation_results/24/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/24/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/24/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/24/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/24/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/24/receipt_handle`: actual `"5c8edcc49a425ceccc3d9a1a0692beea"`; expected `"<missing>"`.
- `/operation_results/24/refs`: actual `[{"id":"rec:deadline-late","version":1}]`; expected `"<missing>"`.
- `/operation_results/24/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/24/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/25/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/25/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/25/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/25/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/25/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/25/receipt_handle`: actual `"0f4ffabd8c3b50737893740cb94dd16d"`; expected `"<missing>"`.
- `/operation_results/25/refs`: actual `[{"id":"rec:deadline-live","version":1}]`; expected `"<missing>"`.
- `/operation_results/25/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/25/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/26/authorized_snapshot_handle`: actual `"e45436af55c40481dff36b94b1d45f02"`; expected `"<missing>"`.
- `/operation_results/26/changes`: actual `{"refs":[],"state":"initial"}`; expected `"<missing>"`.
- `/operation_results/26/code`: actual `"<missing>"`; expected `"invalid_time"`.
- `/operation_results/26/currentness`: actual `"none"`; expected `"<missing>"`.
- `/operation_results/26/cutoffs`: actual `[]`; expected `"<missing>"`.
- `/operation_results/26/data_classification`: actual `"data"`; expected `"<missing>"`.
- `/operation_results/26/evidence_policy`: actual `{"id":"evidence:1","version":1}`; expected `"<missing>"`.
- `/operation_results/26/explanation`: actual `{"paths":[],"reason":null,"status":"complete"}`; expected `"<missing>"`.
- `/operation_results/26/historical`: actual `[]`; expected `"<missing>"`.
- `/operation_results/26/items`: actual `[]`; expected `"<missing>"`.
- `/operation_results/26/policy`: actual `{"id":"policy:1","version":1}`; expected `"<missing>"`.
- `/operation_results/26/projection_rule`: actual `{"id":"projection:main","version":1}`; expected `"<missing>"`.
- `/operation_results/26/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/26/review_required`: actual `[]`; expected `"<missing>"`.
- `/operation_results/26/semantic_profile`: actual `"0.2.5-draft"`; expected `"<missing>"`.
- `/operation_results/26/type`: actual `"view"`; expected `"refusal"`.
- `/operation_results/27/code`: actual `"idempotency_conflict"`; expected `"<missing>"`.
- `/operation_results/27/custody`: actual `"<missing>"`; expected `[]`.
- `/operation_results/27/erasure_status`: actual `"<missing>"`; expected `null`.
- `/operation_results/27/operation`: actual `"<missing>"`; expected `"admit"`.
- `/operation_results/27/outcome`: actual `"<missing>"`; expected `"admitted"`.
- `/operation_results/27/receipt_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/operation_results/27/refs`: actual `"<missing>"`; expected `[{"id":"rec:deadline-open","version":1}]`.
- `/operation_results/27/retryable`: actual `false`; expected `"<missing>"`.
- `/operation_results/27/type`: actual `"refusal"`; expected `"receipt"`.
- `/postconditions/record_refs/length`: actual `9`; expected `7`.
- `/postconditions/record_refs/1/id`: actual `"rec:deadline-late"`; expected `"rec:deadline-live"`.
- `/postconditions/record_refs/2/id`: actual `"rec:deadline-live"`; expected `"rec:deadline-open"`.
- `/postconditions/record_refs/3/id`: actual `"rec:deadline-open"`; expected `"rec:deadline-root"`.
- `/postconditions/record_refs/4/id`: actual `"rec:deadline-root"`; expected `"rec:paraphrase"`.
- `/postconditions/record_refs/5/id`: actual `"rec:deadline-unknown"`; expected `"rec:private"`.
- `/postconditions/record_refs/6/id`: actual `"rec:paraphrase"`; expected `"rec:retained-root"`.
- `/postconditions/record_refs/7`: actual `{"id":"rec:private","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/8`: actual `{"id":"rec:retained-root","version":1}`; expected `"<missing>"`.
- handle slot missing: /operation_results/27/receipt_handle
- distinct_handles violated: ['/operation_results/8/receipt_handle', '/operation_results/11/authorized_snapshot_handle', '/operation_results/12/receipt_handle', '/operation_results/15/authorized_snapshot_handle', '/operation_results/16/receipt_handle', '/operation_results/27/receipt_handle', '/result/authorized_snapshot_handle']
- forbidden predicate matched: {"path":"/operation_results/18/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/19/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/20/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/21/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/24/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/25/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/26/type","test":"equals","value":"view"}
- forbidden predicate matched: {"path":"/postconditions/record_refs/7","test":"exists","value":null}

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
