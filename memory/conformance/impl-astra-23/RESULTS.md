# astra-23 vector run

Package: **0.2.3-draft** at `23290b3`.

The evaluator receives only initial_state, operations and query. Expected outputs,
forbidden predicates and normalization are consumed only by the comparison runner.
Random handles are normalized only at declared paths; their syntax, equality and
distinctness are checked first. No runtime distribution or timing claim is made.

| Profile | Pass | Fail | Unsupported | Total |
| --- | ---: | ---: | ---: | ---: |
| semantic | 55 | 2 | 0 | 57 |
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
| P13 | semantic | fail |
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

- `/operation_results/0/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"e62dbfd26fe5b68a89e329944db67b68"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:scope-probe","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/1/code`: actual `"duplicate_record"`; expected `"not_authorized"`.
- `/operation_results/2/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/2/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/2/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/2/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/2/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/2/receipt_handle`: actual `"e68abdf2de1177bdce7e264e0e8aa520"`; expected `"<missing>"`.
- `/operation_results/2/refs`: actual `[{"id":"rec:paraphrase","version":1}]`; expected `"<missing>"`.
- `/operation_results/2/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/2/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/3/code`: actual `"idempotency_conflict"`; expected `"not_authorized"`.
- `/operation_results/4/code`: actual `"idempotency_conflict"`; expected `"not_authorized"`.
- `/operation_results/5/code`: actual `"idempotency_conflict"`; expected `"not_authorized"`.
- `/operation_results/6/code`: actual `"idempotency_conflict"`; expected `"not_authorized"`.
- `/operation_results/7/authorized_snapshot_handle`: actual `"4a30e01ebdbde115d411087d4f05e0ec"`; expected `"<missing>"`.
- `/operation_results/7/changes`: actual `{"refs":[],"state":"initial"}`; expected `"<missing>"`.
- `/operation_results/7/code`: actual `"<missing>"`; expected `"invalid_time"`.
- `/operation_results/7/currentness`: actual `"none"`; expected `"<missing>"`.
- `/operation_results/7/cutoffs`: actual `[]`; expected `"<missing>"`.
- `/operation_results/7/data_classification`: actual `"data"`; expected `"<missing>"`.
- `/operation_results/7/evidence_policy`: actual `{"id":"evidence:1","version":1}`; expected `"<missing>"`.
- `/operation_results/7/explanation`: actual `{"paths":[],"reason":null,"status":"complete"}`; expected `"<missing>"`.
- `/operation_results/7/historical`: actual `[]`; expected `"<missing>"`.
- `/operation_results/7/items`: actual `[]`; expected `"<missing>"`.
- `/operation_results/7/policy`: actual `{"id":"policy:1","version":1}`; expected `"<missing>"`.
- `/operation_results/7/projection_rule`: actual `{"id":"projection:main","version":1}`; expected `"<missing>"`.
- `/operation_results/7/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/7/review_required`: actual `[]`; expected `"<missing>"`.
- `/operation_results/7/semantic_profile`: actual `"0.2.3-draft"`; expected `"<missing>"`.
- `/operation_results/7/type`: actual `"view"`; expected `"refusal"`.
- `/operation_results/8/code`: actual `"idempotency_conflict"`; expected `"<missing>"`.
- `/operation_results/8/custody`: actual `"<missing>"`; expected `[]`.
- `/operation_results/8/erasure_status`: actual `"<missing>"`; expected `null`.
- `/operation_results/8/operation`: actual `"<missing>"`; expected `"admit"`.
- `/operation_results/8/outcome`: actual `"<missing>"`; expected `"admitted"`.
- `/operation_results/8/receipt_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/operation_results/8/refs`: actual `"<missing>"`; expected `[{"id":"rec:paraphrase","version":1}]`.
- `/operation_results/8/retryable`: actual `false`; expected `"<missing>"`.
- `/operation_results/8/type`: actual `"refusal"`; expected `"receipt"`.
- `/operation_results/9/code`: actual `"idempotency_conflict"`; expected `"<missing>"`.
- `/operation_results/9/custody`: actual `"<missing>"`; expected `[]`.
- `/operation_results/9/erasure_status`: actual `"<missing>"`; expected `null`.
- `/operation_results/9/operation`: actual `"<missing>"`; expected `"admit"`.
- `/operation_results/9/outcome`: actual `"<missing>"`; expected `"admitted"`.
- `/operation_results/9/receipt_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/operation_results/9/refs`: actual `"<missing>"`; expected `[{"id":"rec:paraphrase","version":1}]`.
- `/operation_results/9/retryable`: actual `false`; expected `"<missing>"`.
- `/operation_results/9/type`: actual `"refusal"`; expected `"receipt"`.
- `/operation_results/11/currentness`: actual `"none"`; expected `"current"`.
- `/operation_results/11/items/length`: actual `0`; expected `1`.
- `/operation_results/11/items/0`: actual `"<missing>"`; expected `{"admission_class":"machine_observation","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"synthetic rewording"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:paraphrase","version":1},"representation_ref":null,"source_refs":[],"statement_kind":"fact","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}`.
- `/operation_results/13/code`: actual `"idempotency_conflict"`; expected `"not_authorized"`.
- `/operation_results/14/code`: actual `"duplicate_record"`; expected `"not_authorized"`.
- `/operation_results/15/currentness`: actual `"none"`; expected `"current"`.
- `/operation_results/15/items/length`: actual `0`; expected `1`.
- `/operation_results/15/items/0`: actual `"<missing>"`; expected `{"admission_class":"machine_observation","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"synthetic rewording"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:paraphrase","version":1},"representation_ref":null,"source_refs":[],"statement_kind":"fact","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}`.
- `/postconditions/record_refs/length`: actual `4`; expected `3`.
- `/postconditions/record_refs/3`: actual `{"id":"rec:scope-probe","version":1}`; expected `"<missing>"`.
- handle slot missing: /operation_results/8/receipt_handle
- handle slot missing: /operation_results/9/receipt_handle
- handle slot missing: /operation_results/11/items/0/support/authorized_snapshot_handle
- handle slot missing: /operation_results/11/items/0/oppose/authorized_snapshot_handle
- handle slot missing: /operation_results/15/items/0/support/authorized_snapshot_handle
- handle slot missing: /operation_results/15/items/0/oppose/authorized_snapshot_handle
- equal_handles violated: ['/operation_results/11/authorized_snapshot_handle', '/operation_results/11/items/0/support/authorized_snapshot_handle', '/operation_results/11/items/0/oppose/authorized_snapshot_handle']
- equal_handles violated: ['/operation_results/15/authorized_snapshot_handle', '/operation_results/15/items/0/support/authorized_snapshot_handle', '/operation_results/15/items/0/oppose/authorized_snapshot_handle']
- equal_handles violated: ['/operation_results/8/receipt_handle', '/operation_results/9/receipt_handle']
- distinct_handles violated: ['/operation_results/8/receipt_handle', '/operation_results/11/authorized_snapshot_handle', '/operation_results/12/receipt_handle', '/operation_results/15/authorized_snapshot_handle', '/result/authorized_snapshot_handle']
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/operation_results/2/type","test":"equals","value":"receipt"}
- forbidden predicate matched: {"path":"/postconditions/record_refs","test":"size_equals","value":4}

### P13

- `/operation_results/0/code`: actual `"<missing>"`; expected `"not_authorized"`.
- `/operation_results/0/custody`: actual `[]`; expected `"<missing>"`.
- `/operation_results/0/erasure_status`: actual `null`; expected `"<missing>"`.
- `/operation_results/0/operation`: actual `"admit"`; expected `"<missing>"`.
- `/operation_results/0/outcome`: actual `"admitted"`; expected `"<missing>"`.
- `/operation_results/0/receipt_handle`: actual `"6b8d7c3baa75cd539f3e639f76dddd7e"`; expected `"<missing>"`.
- `/operation_results/0/refs`: actual `[{"id":"rec:model-unknown","version":1}]`; expected `"<missing>"`.
- `/operation_results/0/retryable`: actual `"<missing>"`; expected `false`.
- `/operation_results/0/type`: actual `"receipt"`; expected `"refusal"`.
- `/operation_results/1/code`: actual `"idempotency_conflict"`; expected `"invalid_reference"`.
- `/operation_results/2/code`: actual `"idempotency_conflict"`; expected `"<missing>"`.
- `/operation_results/2/custody`: actual `"<missing>"`; expected `[]`.
- `/operation_results/2/erasure_status`: actual `"<missing>"`; expected `null`.
- `/operation_results/2/operation`: actual `"<missing>"`; expected `"admit"`.
- `/operation_results/2/outcome`: actual `"<missing>"`; expected `"admitted"`.
- `/operation_results/2/receipt_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/operation_results/2/refs`: actual `"<missing>"`; expected `[{"id":"rec:model-clean","version":1},{"id":"rec:model-empty","version":1},{"id":"rec:model-stage","version":1},{"id":"rec:model-tainted","version":1},{"id":"rec:model-unknown","version":1}]`.
- `/operation_results/2/retryable`: actual `false`; expected `"<missing>"`.
- `/operation_results/2/type`: actual `"refusal"`; expected `"receipt"`.
- `/operation_results/3/authorized_snapshot_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/operation_results/3/changes`: actual `"<missing>"`; expected `{"refs":[],"state":"initial"}`.
- `/operation_results/3/code`: actual `"invalid_time"`; expected `"<missing>"`.
- `/operation_results/3/currentness`: actual `"<missing>"`; expected `"current"`.
- `/operation_results/3/cutoffs`: actual `"<missing>"`; expected `[]`.
- `/operation_results/3/data_classification`: actual `"<missing>"`; expected `"data"`.
- `/operation_results/3/evidence_policy`: actual `"<missing>"`; expected `{"id":"evidence:1","version":1}`.
- `/operation_results/3/explanation`: actual `"<missing>"`; expected `{"paths":[],"reason":null,"status":"complete"}`.
- `/operation_results/3/historical`: actual `"<missing>"`; expected `[]`.
- `/operation_results/3/items`: actual `"<missing>"`; expected `[{"admission_class":"semantic_inference","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"candidate with private context"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:model-tainted","version":1},"representation_ref":null,"source_refs":[],"statement_kind":"proposal","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}},{"admission_class":"semantic_inference","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"candidate without complete input tracking"}],"currentness":"current","incompatible_with":[],"issuer":"subj:h1","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:h1"},"ref":{"id":"rec:model-unknown","version":1},"representation_ref":null,"source_refs":[],"statement_kind":"proposal","subject":"subj:h1","submitter":"subj:h1","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}]`.
- `/operation_results/3/policy`: actual `"<missing>"`; expected `{"id":"policy:1","version":1}`.
- `/operation_results/3/projection_rule`: actual `"<missing>"`; expected `{"id":"projection:main","version":1}`.
- `/operation_results/3/retryable`: actual `false`; expected `"<missing>"`.
- `/operation_results/3/review_required`: actual `"<missing>"`; expected `[]`.
- `/operation_results/3/semantic_profile`: actual `"<missing>"`; expected `"0.2.3-draft"`.
- `/operation_results/3/type`: actual `"refusal"`; expected `"view"`.
- `/postconditions/record_refs/length`: actual `3`; expected `7`.
- `/postconditions/record_refs/0/id`: actual `"rec:model-unknown"`; expected `"rec:model-clean"`.
- `/postconditions/record_refs/1/id`: actual `"rec:private-input"`; expected `"rec:model-empty"`.
- `/postconditions/record_refs/2/id`: actual `"rec:public-input"`; expected `"rec:model-stage"`.
- `/postconditions/record_refs/3`: actual `"<missing>"`; expected `{"id":"rec:model-tainted","version":1}`.
- `/postconditions/record_refs/4`: actual `"<missing>"`; expected `{"id":"rec:model-unknown","version":1}`.
- `/postconditions/record_refs/5`: actual `"<missing>"`; expected `{"id":"rec:private-input","version":1}`.
- `/postconditions/record_refs/6`: actual `"<missing>"`; expected `{"id":"rec:public-input","version":1}`.
- `/result/authorized_snapshot_handle`: actual `"<missing>"`; expected `"<fresh-handle>"`.
- `/result/changes`: actual `"<missing>"`; expected `{"refs":[],"state":"initial"}`.
- `/result/code`: actual `"invalid_time"`; expected `"<missing>"`.
- `/result/currentness`: actual `"<missing>"`; expected `"current"`.
- `/result/cutoffs`: actual `"<missing>"`; expected `[]`.
- `/result/data_classification`: actual `"<missing>"`; expected `"data"`.
- `/result/evidence_policy`: actual `"<missing>"`; expected `{"id":"evidence:1","version":1}`.
- `/result/explanation`: actual `"<missing>"`; expected `{"paths":[],"reason":null,"status":"complete"}`.
- `/result/historical`: actual `"<missing>"`; expected `[]`.
- `/result/items`: actual `"<missing>"`; expected `[{"admission_class":"semantic_inference","authority_receipt":null,"confirmed_at":"2026-10-17T00:00:00Z","content":[{"field":"value","value":"candidate from only public context"}],"currentness":"current","incompatible_with":[],"issuer":"subj:model-output","needs_review":false,"oppose":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"perspective":{"kind":"own","principal":"subj:model-output"},"ref":null,"representation_ref":null,"source_refs":[],"statement_kind":"proposal","subject":"subj:model-output","submitter":"subj:model-output","support":{"authorized_snapshot_handle":"<fresh-handle>","corpus_coverage":{"kind":"unknown"},"dependency_coverage":"registered_only","evaluation":"complete","evidence_qualification":[],"freshness":"not_applicable","independent_root_count":0,"premise_quality":"not_fully_checked","source_state":"resolvable_now","witness":"not_found","witness_roots":[]},"usable_until":null,"valid":{"from":"2026-09-01T00:00:00Z","kind":"known","precision":"second","to":null}}]`.
- `/result/policy`: actual `"<missing>"`; expected `{"id":"policy:1","version":1}`.
- `/result/projection_rule`: actual `"<missing>"`; expected `{"id":"projection:public","version":1}`.
- `/result/retryable`: actual `false`; expected `"<missing>"`.
- `/result/review_required`: actual `"<missing>"`; expected `[]`.
- `/result/semantic_profile`: actual `"<missing>"`; expected `"0.2.3-draft"`.
- `/result/type`: actual `"refusal"`; expected `"view"`.
- handle slot missing: /operation_results/2/receipt_handle
- handle slot missing: /operation_results/3/authorized_snapshot_handle
- handle slot missing: /operation_results/3/items/0/support/authorized_snapshot_handle
- handle slot missing: /operation_results/3/items/0/oppose/authorized_snapshot_handle
- handle slot missing: /operation_results/3/items/1/support/authorized_snapshot_handle
- handle slot missing: /operation_results/3/items/1/oppose/authorized_snapshot_handle
- handle slot missing: /result/authorized_snapshot_handle
- handle slot missing: /result/items/0/support/authorized_snapshot_handle
- handle slot missing: /result/items/0/oppose/authorized_snapshot_handle
- equal_handles violated: ['/operation_results/3/authorized_snapshot_handle', '/operation_results/3/items/0/support/authorized_snapshot_handle', '/operation_results/3/items/0/oppose/authorized_snapshot_handle', '/operation_results/3/items/1/support/authorized_snapshot_handle', '/operation_results/3/items/1/oppose/authorized_snapshot_handle']
- equal_handles violated: ['/result/authorized_snapshot_handle', '/result/items/0/support/authorized_snapshot_handle', '/result/items/0/oppose/authorized_snapshot_handle']
- distinct_handles violated: ['/operation_results/2/receipt_handle', '/operation_results/3/authorized_snapshot_handle', '/result/authorized_snapshot_handle']
- forbidden predicate matched: {"path":"/operation_results/0/type","test":"equals","value":"receipt"}

## Reproducibility

Implementation SHA-256:

- `common.py`: `22a4807a07818eb83109c38838c094c3e4cc5fcc76e74e9e831fd2860f8db033`
- `disclosure.py`: `ae3862f6fadbb8fe602d13bfd5774df0680c7cfba17a131684102d2cacad3366`
- `engine.py`: `a6926a1a49a65b20cc670f3910e3cdab598a5dd8431f100ee5e34d088a51111f`
- `evaluator.py`: `098d8460eb181b881f77ef7aef724d696ae652f680c44cd5905ca7e4a6c11100`
- `run_vectors.py`: `20bf1acc55f090e3c8fbcba71f24dc95ea23cfafcb31abb911138d9fdbf2298a`
- `test_controls.py`: `6cd50b73ef952ba0cc5d14f2fadecbed37a2fbb9bc275644e22c96d8c0c1e083`
- `test_semantics.py`: `20d7b7b82b6adc1cc3fb12a7ea406f9995f0511f0ec922a152a4e4e81c3644c7`

Full actual reports, exact differences and vector digests are in the adjacent JSON report.
