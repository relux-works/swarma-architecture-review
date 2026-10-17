# astra-23 vector run

Package: **0.2.5-draft** at `6a04e8cfb1490569cd1de7468d2085dd4840cf51`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 57 | 0 | 0 | 57 |
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

## Reproducibility

Implementation SHA-256:

- `common.py`: `22a4807a07818eb83109c38838c094c3e4cc5fcc76e74e9e831fd2860f8db033`
- `disclosure.py`: `ae3862f6fadbb8fe602d13bfd5774df0680c7cfba17a131684102d2cacad3366`
- `engine.py`: `f2877f373db6c83f9fe4ba2e30ae4a6c08c35833618052c8209456e650a4b1c8`
- `evaluator.py`: `098d8460eb181b881f77ef7aef724d696ae652f680c44cd5905ca7e4a6c11100`
- `run_vectors.py`: `20bf1acc55f090e3c8fbcba71f24dc95ea23cfafcb31abb911138d9fdbf2298a`
- `test_controls.py`: `6cd50b73ef952ba0cc5d14f2fadecbed37a2fbb9bc275644e22c96d8c0c1e083`
- `test_semantics.py`: `b229816cd606ff766cb65c6f962bb6434b4f600f1aeb58392995fb316c1dd3bd`

Full actual reports, exact differences and vector digests are in the adjacent JSON report.
