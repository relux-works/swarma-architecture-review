# astra-23 vector run

Package: **0.2.5-draft** at `6a04e8cfb1490569cd1de7468d2085dd4840cf51`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 65 | 3 | 0 | 68 |
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
| ASTRA25-07-CONFLICT-AUDIENCE | semantic | pass |
| ASTRA25-07-CONFLICT-PURPOSE | semantic | pass |
| ASTRA25-07-PURPOSE | semantic | pass |
| ASTRA25-07 | semantic | pass |
| ASTRA25-10 | semantic | pass |
| ASTRA25-05-CONTROL | semantic | pass |
| ASTRA25-05 | semantic | pass |
| ASTRA25-01 | semantic | pass |
| ASTRA25-06 | semantic | pass |
| ASTRA25-12-EMPTY | semantic | pass |
| ASTRA25-12-INDEPENDENT | semantic | fail |
| ASTRA25-12-KNOWN | semantic | pass |
| ASTRA25-12-UNREACHABLE | semantic | fail |
| ASTRA25-12 | semantic | fail |
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

### ASTRA25-12-INDEPENDENT

- `/operation_results/3/custody/length`: actual `0`; expected `2`.
- `/operation_results/3/custody/0`: actual `"<missing>"`; expected `"custody:backup"`.
- `/operation_results/3/custody/1`: actual `"<missing>"`; expected `"custody:payload"`.
- `/postconditions/custody_present/length`: actual `3`; expected `1`.
- `/postconditions/custody_present/0`: actual `"custody:backup"`; expected `"custody:independent"`.
- `/postconditions/custody_present/1`: actual `"custody:independent"`; expected `"<missing>"`.
- `/postconditions/custody_present/2`: actual `"custody:payload"`; expected `"<missing>"`.
- `/postconditions/erased_refs/length`: actual `0`; expected `1`.
- `/postconditions/erased_refs/0`: actual `"<missing>"`; expected `{"id":"rec:a","version":1}`.
- `/result/items/length`: actual `2`; expected `1`.
- `/result/items/0/content/0/value`: actual `"alpha"`; expected `"beta"`.
- `/result/items/0/ref/id`: actual `"rec:a"`; expected `"rec:b"`.
- `/result/items/1`: actual `{"admission_class":"machine_observation","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"beta"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"1c0064c694ab68d1d905532a9bf7b034","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:b","version":1},"representation_ref":null,"source_refs":[],"statement_kind":"fact","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"1c0064c694ab68d1d905532a9bf7b034","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/postconditions/custody_present","test":"contains","value":"custody:backup"}
- forbidden predicate matched: {"path":"/postconditions/custody_present","test":"contains","value":"custody:payload"}
- forbidden predicate matched: {"path":"/result/items/0/ref/id","test":"equals","value":"rec:a"}

### ASTRA25-12-UNREACHABLE

- `/operation_results/3/code`: actual `"<missing>"`; expected `"erasure_incomplete"`.
- `/operation_results/3/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/3/erasure_status`: actual `"purged_within_boundary"`; expected `"<missing>"`.
- `/operation_results/3/operation`: actual `"reconcile_restore"`; expected `"<missing>"`.
- `/operation_results/3/outcome`: actual `"reconciled"`; expected `"<missing>"`.
- `/operation_results/3/receipt_handle`: actual `"4843be02c2713cd325db621ddceee822"`; expected `"<missing>"`.
- `/operation_results/3/refs`: actual `[]`; expected `"<missing>"`.
- `/operation_results/3/retryable`: actual `"<missing>"`; expected `true`.
- `/operation_results/3/type`: actual `"receipt"`; expected `"refusal"`.
- `/result/authorized_snapshot_handle`: actual `"9acdab87fe228d8a7a5c0104667cf3d6"`; expected `"<missing>"`.
- `/result/changes`: actual `{"refs":[],"state":"initial"}`; expected `"<missing>"`.
- `/result/code`: actual `"<missing>"`; expected `"erasure_fenced"`.
- `/result/currentness`: actual `"current"`; expected `"<missing>"`.
- `/result/cutoffs`: actual `[]`; expected `"<missing>"`.
- `/result/data_classification`: actual `"data"`; expected `"<missing>"`.
- `/result/evidence_policy`: actual `{"id":"evidence:1","version":1}`; expected `"<missing>"`.
- `/result/explanation`: actual `{"paths":[],"reason":null,"status":"complete"}`; expected `"<missing>"`.
- `/result/historical`: actual `[]`; expected `"<missing>"`.
- `/result/items`: actual `[{"admission_class":"machine_observation","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"alpha"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"9acdab87fe228d8a7a5c0104667cf3d6","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:a","version":1},"representation_ref":null,"source_refs":[],"statement_kind":"fact","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"9acdab87fe228d8a7a5c0104667cf3d6","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}]`; expected `"<missing>"`.
- `/result/policy`: actual `{"id":"policy:1","version":1}`; expected `"<missing>"`.
- `/result/projection_rule`: actual `{"id":"projection:main","version":1}`; expected `"<missing>"`.
- `/result/retryable`: actual `"<missing>"`; expected `false`.
- `/result/review_required`: actual `[]`; expected `"<missing>"`.
- `/result/semantic_profile`: actual `"0.2.5-draft"`; expected `"<missing>"`.
- `/result/type`: actual `"view"`; expected `"refusal"`.
- forbidden predicate matched: {"path":"/operation_results/3/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/result/type","test":"equals","value":"view"}

### ASTRA25-12

- `/operation_results/3/custody/length`: actual `0`; expected `2`.
- `/operation_results/3/custody/0`: actual `"<missing>"`; expected `"custody:backup"`.
- `/operation_results/3/custody/1`: actual `"<missing>"`; expected `"custody:payload"`.
- `/postconditions/custody_present/length`: actual `2`; expected `0`.
- `/postconditions/custody_present/0`: actual `"custody:backup"`; expected `"<missing>"`.
- `/postconditions/custody_present/1`: actual `"custody:payload"`; expected `"<missing>"`.
- `/postconditions/erased_refs/length`: actual `0`; expected `1`.
- `/postconditions/erased_refs/0`: actual `"<missing>"`; expected `{"id":"rec:a","version":1}`.
- `/result/currentness`: actual `"current"`; expected `"none"`.
- `/result/items/length`: actual `1`; expected `0`.
- `/result/items/0`: actual `{"admission_class":"machine_observation","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"alpha"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"9b178cb84abaa37a3bab295f4c40feab","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:a","version":1},"representation_ref":null,"source_refs":[],"statement_kind":"fact","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"9b178cb84abaa37a3bab295f4c40feab","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}`; expected `"<missing>"`.
- forbidden predicate matched: {"path":"/postconditions/custody_present","test":"contains","value":"custody:backup"}
- forbidden predicate matched: {"path":"/postconditions/custody_present","test":"contains","value":"custody:payload"}
- forbidden predicate matched: {"path":"/result/items/0/ref/id","test":"equals","value":"rec:a"}

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
