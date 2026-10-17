# astra-23 vector run

Package: **0.2.2-draft** at `7e71765317088d4ac1ea6946fdfb4b2f8012643c`.

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
| P08 | semantic | fail |
| P09 | semantic | pass |
| P10 | semantic | pass |
| P11 | semantic | pass |
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

### P08

- `/operation_results/0/refs/length`: actual `2`; expected `1`.
- `/operation_results/0/refs/1`: actual `{"id":"rec:summary","version":1}`; expected `"<missing>"`.
- `/operation_results/1/refs/length`: actual `2`; expected `1`.
- `/operation_results/1/refs/1`: actual `{"id":"rec:summary","version":1}`; expected `"<missing>"`.
- `/operation_results/5/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/5/custody`: actual `["custody:backup","custody:cache","custody:export","custody:payload","custody:summary","custody:telemetry"]`; expected `"<missing>"`.
- `/operation_results/5/erasure_status`: actual `"purged_within_boundary"`; expected `"<missing>"`.
- `/operation_results/5/operation`: actual `"erase"`; expected `"<missing>"`.
- `/operation_results/5/outcome`: actual `"purged"`; expected `"<missing>"`.
- `/operation_results/5/receipt_handle`: actual `"cec721fc0aa01e6f645507aed8da8103"`; expected `"<missing>"`.
- `/operation_results/5/refs`: actual `[{"id":"rec:sensitive","version":1},{"id":"rec:summary","version":1}]`; expected `"<missing>"`.
- `/operation_results/5/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/5/type`: actual `"receipt"`; expected `"refusal"`.
- forbidden predicate matched: {"path":"/operation_results/0/refs/1/id","test":"equals","value":"rec:summary"}
- forbidden predicate matched: {"path":"/operation_results/5/type","test":"equals","value":"receipt"}

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
