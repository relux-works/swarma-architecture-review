# astra-23 vector run

Package: **0.2.0-draft** at `cde5754d523b98c93cf2b1777fe80e15b9efa74c`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 7 | 1 | 9 | 17 |
| deployment | 0 | 0 | 0 | 0 |

Deployment unsupported means no qualification claim; modeled semantic erasure
and publication transitions do not exercise live authentication, storage or delivery.

## Per-vector results

| Vector | Profile | Result |
| --- | --- | --- |
| ASTRA24-03 | semantic | unsupported |
| ASTRA24-01 | semantic | unsupported |
| ASTRA24-02 | semantic | unsupported |
| ASTRA25-05-CONTROL | semantic | unsupported |
| ASTRA25-05 | semantic | unsupported |
| ASTRA25-01 | semantic | unsupported |
| ASTRA25-03-CONTROL | semantic | unsupported |
| ASTRA25-03-FENCE | semantic | unsupported |
| ASTRA25-03 | semantic | unsupported |
| ASTRA26-06 | semantic | fail |
| ASTRA26-01 | semantic | pass |
| ASTRA26-04 | semantic | pass |
| ASTRA26-02-CONTROL | semantic | pass |
| ASTRA26-02 | semantic | pass |
| ASTRA26-05 | semantic | pass |
| ASTRA26-03-CONTROL | semantic | pass |
| ASTRA26-03 | semantic | pass |

### ASTRA24-03

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA24-01

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA24-02

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA25-05-CONTROL

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA25-05

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA25-01

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA25-03-CONTROL

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA25-03-FENCE

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA25-03

Supplemental fixture does not match this package's closed vector grammar; no implicit conversion performed.

### ASTRA26-06

- `/operation_results/0/code`: actual `"<missing>"`; expected `"invalid_domain_value"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"c37b8118146705c837ed98a004ae9a45"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:org-claim","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/postconditions/record_refs/length`: actual `2`; expected `1`.
- `/postconditions/record_refs/0/id`: actual `"rec:org-claim"`; expected `"rec:self-claim"`.
- `/postconditions/record_refs/1`: actual `{"id":"rec:self-claim","version":1}`; expected `"<missing>"`.
- `/result/currentness`: actual `"none"`; expected `"current"`.
- `/result/items/length`: actual `0`; expected `1`.
- `/result/items/0`: actual `"<missing>"`; expected `{"admission_class":"self_declaration","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"level","value":"stated"},{"field":"skill","value":"gardening"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:self-claim","version":1},"representation_ref":null,"source_refs":[],"statement_kind":"self_declaration","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}`.
- handle slot missing: /result/items/0/support/authorized_snapshot_handle
- handle slot missing: /result/items/0/oppose/authorized_snapshot_handle
- equal_handles violated: ['/result/authorized_snapshot_handle', '/result/items/0/support/authorized_snapshot_handle', '/result/items/0/oppose/authorized_snapshot_handle']
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":2}

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
