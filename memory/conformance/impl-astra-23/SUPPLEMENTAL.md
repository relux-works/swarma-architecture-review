# astra-23 vector run

Package: **0.2.5-draft** at `6a04e8cfb1490569cd1de7468d2085dd4840cf51`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 61 | 0 | 0 | 61 |
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
| ASTRA25-11-OWN | semantic | pass |
| ASTRA25-11-REPLAY | semantic | pass |
| ASTRA25-11-BATCH-CONTROL | semantic | pass |
| ASTRA25-11-BATCH | semantic | pass |
| ASTRA25-11-UNKNOWN | semantic | pass |
| ASTRA25-11 | semantic | pass |
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

### ASTRA25-04

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
