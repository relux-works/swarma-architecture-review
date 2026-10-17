# astra-23 vector run

Package: **0.2.6-draft** at `77b951eb86d5ba9198921d058930884918a39942`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 64 | 2 | 0 | 66 |
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
| S34 | semantic | fail |
| S35 | semantic | pass |
| S36 | semantic | pass |
| S37 | semantic | pass |
| S38 | semantic | pass |
| S39 | semantic | fail |
| S40 | semantic | pass |
| S41 | semantic | pass |
| S42 | semantic | pass |

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

### S34

- `/result/currentness`: actual `"current"`; expected `"ambiguous_current"`.
- `/result/historical/length`: actual `1`; expected `0`.
- `/result/historical/0`: actual `{"id":"rec:d","version":1}`; expected `"<missing>"`.
- `/result/items/length`: actual `1`; expected `2`.
- `/result/items/0/authority_receipt/id`: actual `"rec:receipt3"`; expected `"rec:receipt1"`.
- `/result/items/0/content/0/value`: actual `"retain_home"`; expected `"archive_home"`.
- `/result/items/0/currentness`: actual `"current"`; expected `"ambiguous_current"`.
- `/result/items/0/ref/version`: actual `3`; expected `1`.
- `/result/items/0/source_refs/0/id`: actual `"rec:receipt3"`; expected `"rec:receipt1"`.
- `/result/items/1`: actual `"<missing>"`; expected `{"admission_class":"machine_observation","authority_receipt":{"id":"rec:receipt3","version":1},"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"retain_home"}],"currentness":"ambiguous_current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:d","version":3},"representation_ref":null,"source_refs":[{"id":"rec:receipt3","version":1}],"statement_kind":"decision_record","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}`.
- handle slot missing: /result/items/1/support/authorized_snapshot_handle
- handle slot missing: /result/items/1/oppose/authorized_snapshot_handle
- equal_handles violated: ['/result/authorized_snapshot_handle', '/result/items/0/support/authorized_snapshot_handle', '/result/items/0/oppose/authorized_snapshot_handle', '/result/items/1/support/authorized_snapshot_handle', '/result/items/1/oppose/authorized_snapshot_handle']
- forbidden predicate matched: {"path":"/result/currentness","test":"equals","value":"current"}
- forbidden predicate matched: {"path":"/result/historical","test":"size_equals","value":1}
- forbidden predicate matched: {"path":"/result/items","test":"size_equals","value":1}

### S39

- `/operation_results/0/code`: actual `"<missing>"`; expected `"authority_receipt_required"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"revise"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"revised"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"e6cd2fc21895256d2490fb0786c36c4c"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:d","version":2},{"id":"rec:local-replace","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/1/code`: actual `"idempotency_conflict"`; expected `"authority_receipt_required"`.
- `/operation_results/3/authorized_snapshot_handle`: actual `"dddc3637b6e46f9d62e5c7fdcb195444"`; expected `"<missing>"`.
- `/operation_results/3/changes`: actual `{"refs":[],"state":"initial"}`; expected `"<missing>"`.
- `/operation_results/3/code`: actual `"<missing>"`; expected `"invalid_time"`.
- `/operation_results/3/currentness`: actual `"current"`; expected `"<missing>"`.
- `/operation_results/3/cutoffs`: actual `[]`; expected `"<missing>"`.
- `/operation_results/3/data_classification`: actual `"data"`; expected `"<missing>"`.
- `/operation_results/3/evidence_policy`: actual `{"id":"evidence:1","version":1}`; expected `"<missing>"`.
- `/operation_results/3/explanation`: actual `{"paths":[],"reason":null,"status":"complete"}`; expected `"<missing>"`.
- `/operation_results/3/historical`: actual `[{"id":"rec:d","version":1}]`; expected `"<missing>"`.
- `/operation_results/3/items`: actual `[{"admission_class":"machine_observation","authority_receipt":{"id":"rec:receipt3","version":1},"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"retain_home"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"dddc3637b6e46f9d62e5c7fdcb195444","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:d","version":2},"representation_ref":null,"source_refs":[{"id":"rec:receipt3","version":1}],"statement_kind":"decision_record","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"dddc3637b6e46f9d62e5c7fdcb195444","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}]`; expected `"<missing>"`.
- `/operation_results/3/policy`: actual `{"id":"policy:1","version":1}`; expected `"<missing>"`.
- `/operation_results/3/projection_rule`: actual `{"id":"projection:main","version":1}`; expected `"<missing>"`.
- `/operation_results/3/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/3/review_required`: actual `[{"id":"rec:dependent","version":1}]`; expected `"<missing>"`.
- `/operation_results/3/semantic_profile`: actual `"0.2.6-draft"`; expected `"<missing>"`.
- `/operation_results/3/type`: actual `"view"`; expected `"refusal"`.
- `/operation_results/4/code`: actual `"idempotency_conflict"`; expected `"<missing>"`.
- `/operation_results/4/custody`: actual `"<missing>"`; expected `[]`.
- `/operation_results/4/erasure_status`: actual `"<missing>"`; expected `null`.
- `/operation_results/4/operation`: actual `"<missing>"`; expected `"admit"`.
- `/operation_results/4/outcome`: actual `"<missing>"`; expected `"admitted"`.
- `/operation_results/4/receipt_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/operation_results/4/refs`: actual `"<missing>"`; expected `[{"id":"rec:d","version":2}]`.
- `/operation_results/4/retryable`: actual `false`; expected `"<missing>"`.
- `/operation_results/4/type`: actual `"refusal"`; expected `"receipt"`.
- `/operation_results/6/code`: actual `"idempotency_conflict"`; expected `"<missing>"`.
- `/operation_results/6/custody`: actual `"<missing>"`; expected `[]`.
- `/operation_results/6/erasure_status`: actual `"<missing>"`; expected `null`.
- `/operation_results/6/operation`: actual `"<missing>"`; expected `"admit"`.
- `/operation_results/6/outcome`: actual `"<missing>"`; expected `"admitted"`.
- `/operation_results/6/receipt_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/operation_results/6/refs`: actual `"<missing>"`; expected `[{"id":"rec:d","version":2}]`.
- `/operation_results/6/retryable`: actual `false`; expected `"<missing>"`.
- `/operation_results/6/type`: actual `"refusal"`; expected `"receipt"`.
- `/postconditions/dirty/length`: actual `1`; expected `0`.
- `/postconditions/dirty/0`: actual `{"id":"rec:dependent","version":1}`; expected `"<missing>"`.
- `/postconditions/record_refs/length`: actual `8`; expected `7`.
- `/postconditions/record_refs/3/id`: actual `"rec:local-replace"`; expected `"rec:receipt1"`.
- `/postconditions/record_refs/4/id`: actual `"rec:receipt1"`; expected `"rec:receipt2"`.
- `/postconditions/record_refs/5/id`: actual `"rec:receipt2"`; expected `"rec:receipt3"`.
- `/postconditions/record_refs/6/id`: actual `"rec:receipt3"`; expected `"rec:review-dependent"`.
- `/postconditions/record_refs/7`: actual `{"id":"rec:review-dependent","version":1}`; expected `"<missing>"`.
- `/result/authorized_snapshot_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/result/changes`: actual `"<missing>"`; expected `{"refs":[],"state":"initial"}`.
- `/result/code`: actual `"invalid_time"`; expected `"<missing>"`.
- `/result/currentness`: actual `"<missing>"`; expected `"ambiguous_current"`.
- `/result/cutoffs`: actual `"<missing>"`; expected `[]`.
- `/result/data_classification`: actual `"<missing>"`; expected `"data"`.
- `/result/evidence_policy`: actual `"<missing>"`; expected `{"id":"evidence:1","version":1}`.
- `/result/explanation`: actual `"<missing>"`; expected `{"paths":[],"reason":null,"status":"complete"}`.
- `/result/historical`: actual `"<missing>"`; expected `[]`.
- `/result/items`: actual `"<missing>"`; expected `[{"admission_class":"machine_observation","authority_receipt":{"id":"rec:receipt1","version":1},"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"archive_home"}],"currentness":"ambiguous_current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:d","version":1},"representation_ref":null,"source_refs":[{"id":"rec:receipt1","version":1}],"statement_kind":"decision_record","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}},{"admission_class":"machine_observation","authority_receipt":{"id":"rec:receipt3","version":1},"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"retain_home"}],"currentness":"ambiguous_current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:d","version":2},"representation_ref":null,"source_refs":[{"id":"rec:receipt3","version":1}],"statement_kind":"decision_record","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}]`.
- `/result/policy`: actual `"<missing>"`; expected `{"id":"policy:1","version":1}`.
- `/result/projection_rule`: actual `"<missing>"`; expected `{"id":"projection:main","version":1}`.
- `/result/retryable`: actual `false`; expected `"<missing>"`.
- `/result/review_required`: actual `"<missing>"`; expected `[]`.
- `/result/semantic_profile`: actual `"<missing>"`; expected `"0.2.6-draft"`.
- `/result/type`: actual `"refusal"`; expected `"view"`.
- handle slot missing: /operation_results/4/receipt_handle
- handle slot missing: /operation_results/6/receipt_handle
- handle slot missing: /result/authorized_snapshot_handle
- handle slot missing: /result/items/0/support/authorized_snapshot_handle
- handle slot missing: /result/items/0/oppose/authorized_snapshot_handle
- handle slot missing: /result/items/1/support/authorized_snapshot_handle
- handle slot missing: /result/items/1/oppose/authorized_snapshot_handle
- equal_handles violated: ['/result/authorized_snapshot_handle', '/result/items/0/support/authorized_snapshot_handle', '/result/items/0/oppose/authorized_snapshot_handle', '/result/items/1/support/authorized_snapshot_handle', '/result/items/1/oppose/authorized_snapshot_handle']
- equal_handles violated: ['/operation_results/4/receipt_handle', '/operation_results/6/receipt_handle']
- distinct_handles violated: ['/operation_results/2/authorized_snapshot_handle', '/operation_results/4/receipt_handle', '/result/authorized_snapshot_handle']
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/3/type","test":"equals","value":"view"}
- forbidden predicate matched: {"path":"/postconditions/dirty","test":"size_equals","value":1}

## Reproducibility

Implementation SHA-256:

- `common.py`: `22a4807a07818eb83109c38838c094c3e4cc5fcc76e74e9e831fd2860f8db033`
- `disclosure.py`: `ae3862f6fadbb8fe602d13bfd5774df0680c7cfba17a131684102d2cacad3366`
- `engine.py`: `7f5be6d7c1f2dbe0233b717b4f399f4d1975ed8d49e5888145f6813849845a4f`
- `evaluator.py`: `098d8460eb181b881f77ef7aef724d696ae652f680c44cd5905ca7e4a6c11100`
- `run_vectors.py`: `20bf1acc55f090e3c8fbcba71f24dc95ea23cfafcb31abb911138d9fdbf2298a`
- `test_controls.py`: `6cd50b73ef952ba0cc5d14f2fadecbed37a2fbb9bc275644e22c96d8c0c1e083`
- `test_semantics.py`: `3570d7f37ead854217c76128cf566794b2d7943b3a13b49a45ad583a5d1e871b`

Full actual reports, exact differences and vector digests are in the adjacent JSON report.
