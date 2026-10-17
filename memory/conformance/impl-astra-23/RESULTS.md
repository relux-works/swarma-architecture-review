# astra-23 vector run

Package: **0.2.0-draft** at `cde5754d523b98c93cf2b1777fe80e15b9efa74c`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 54 | 3 | 0 | 57 |
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
| B01 | semantic | fail |
| B02 | semantic | pass |
| B03 | semantic | fail |
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
| S23 | semantic | fail |
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

### B01

- `/operation_results/0/code`: actual `"invalid_reference"`; expected `"<missing>"`.
- `/operation_results/0/custody`: actual `"<missing>"`; expected `[]`.
- `/operation_results/0/erasure_status`: actual `"<missing>"`; expected `null`.
- `/operation_results/0/operation`: actual `"<missing>"`; expected `"revise"`.
- `/operation_results/0/outcome`: actual `"<missing>"`; expected `"revised"`.
- `/operation_results/0/receipt_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/operation_results/0/refs`: actual `"<missing>"`; expected `[{"id":"rec:d","version":2},{"id":"rec:decision-replace","version":1}]`.
- `/operation_results/0/retryable`: actual `false`; expected `"<missing>"`.
- `/operation_results/0/type`: actual `"refusal"`; expected `"receipt"`.
- `/postconditions/dirty/length`: actual `0`; expected `1`.
- `/postconditions/dirty/0`: actual `"<missing>"`; expected `{"id":"rec:dependent","version":1}`.
- `/postconditions/record_refs/length`: actual `5`; expected `7`.
- `/postconditions/record_refs/1/id`: actual `"rec:dependent"`; expected `"rec:d"`.
- `/postconditions/record_refs/1/version`: actual `1`; expected `2`.
- `/postconditions/record_refs/2/id`: actual `"rec:receipt1"`; expected `"rec:decision-replace"`.
- `/postconditions/record_refs/3/id`: actual `"rec:receipt2"`; expected `"rec:dependent"`.
- `/postconditions/record_refs/4/id`: actual `"rec:review-dependent"`; expected `"rec:receipt1"`.
- `/postconditions/record_refs/5`: actual `"<missing>"`; expected `{"id":"rec:receipt2","version":1}`.
- `/postconditions/record_refs/6`: actual `"<missing>"`; expected `{"id":"rec:review-dependent","version":1}`.
- `/result/authorized_snapshot_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/result/changes`: actual `"<missing>"`; expected `{"refs":[],"state":"initial"}`.
- `/result/code`: actual `"invalid_time"`; expected `"<missing>"`.
- `/result/currentness`: actual `"<missing>"`; expected `"current"`.
- `/result/cutoffs`: actual `"<missing>"`; expected `[]`.
- `/result/data_classification`: actual `"<missing>"`; expected `"data"`.
- `/result/evidence_policy`: actual `"<missing>"`; expected `{"id":"evidence:1","version":1}`.
- `/result/explanation`: actual `"<missing>"`; expected `{"paths":[],"reason":null,"status":"complete"}`.
- `/result/historical`: actual `"<missing>"`; expected `[{"id":"rec:d","version":1}]`.
- `/result/items`: actual `"<missing>"`; expected `[{"admission_class":"machine_observation","authority_receipt":{"id":"rec:receipt2","version":1},"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"delete_home"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:d","version":2},"representation_ref":null,"source_refs":[{"id":"rec:receipt2","version":1}],"statement_kind":"decision_record","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}]`.
- `/result/policy`: actual `"<missing>"`; expected `{"id":"policy:1","version":1}`.
- `/result/projection_rule`: actual `"<missing>"`; expected `{"id":"projection:main","version":1}`.
- `/result/retryable`: actual `false`; expected `"<missing>"`.
- `/result/review_required`: actual `"<missing>"`; expected `[{"id":"rec:dependent","version":1}]`.
- `/result/semantic_profile`: actual `"<missing>"`; expected `"0.2.0-draft"`.
- `/result/type`: actual `"refusal"`; expected `"view"`.
- handle slot missing: /operation_results/0/receipt_handle
- handle slot missing: /result/authorized_snapshot_handle
- handle slot missing: /result/items/0/support/authorized_snapshot_handle
- handle slot missing: /result/items/0/oppose/authorized_snapshot_handle
- equal_handles violated: ['/result/authorized_snapshot_handle', '/result/items/0/support/authorized_snapshot_handle', '/result/items/0/oppose/authorized_snapshot_handle']
- distinct_handles violated: ['/operation_results/0/receipt_handle', '/result/authorized_snapshot_handle']

### B03

- `/result/currentness`: actual `"last_received"`; expected `"current"`.
- `/result/items/0/currentness`: actual `"last_received"`; expected `"current"`.

### S23

- `/result/currentness`: actual `"last_received"`; expected `"current"`.
- `/result/items/0/currentness`: actual `"last_received"`; expected `"current"`.

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
