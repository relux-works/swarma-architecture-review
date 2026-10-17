# astra-22 vector results

Package: **0.2.3-draft**, package commit `23290b3a96a469d5190cb71b0e20139896b89236`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `97990250ecd826ee6dee5ba0aba0543e7981ca1d`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 24 | 13 | 9 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-08-CHALLENGE | semantic | fail | 51 exact differences |
| ASTRA24-08-CONTROL | semantic | fail | 28 exact differences |
| ASTRA24-08-NEXT | semantic | fail | 53 exact differences |
| ASTRA24-08-STALE | semantic | fail | 4 exact differences |
| ASTRA24-08 | semantic | fail | 4 exact differences |
| ASTRA24-07 | semantic | fail | 2 exact differences |
| ASTRA24-04 | semantic | fail | 2 exact differences |
| ASTRA24-03 | semantic | fail | 3 exact differences |
| ASTRA24-05 | semantic | fail | 3 exact differences |
| ASTRA24-01 | semantic | fail | 2 exact differences |
| ASTRA24-02 | semantic | fail | 4 exact differences |
| ASTRA24-06 | semantic | fail | 2 exact differences |
| ASTRA24-09 | semantic | fail | 2 exact differences |
| ASTRA25-02 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, revoke_declassification |
| ASTRA25-07-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-07-PURPOSE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-07 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-05-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08-UNKNOWN-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08-UNKNOWN | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-04 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| ASTRA25-03-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03-FENCE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-09-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-09 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA26-07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-09-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-09-UNVERIFIED | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |

## ASTRA24-08-CHALLENGE

51 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[1].code`: expected `"<absent>"`; actual `"invalid_shape"`.
- `$.operation_results[1].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[1].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[1].operation`: expected `"revise"`; actual `"<absent>"`.
- `$.operation_results[1].outcome`: expected `"challenged"`; actual `"<absent>"`.
- `$.operation_results[1].receipt_handle`: expected `"@h2"`; actual `"<absent>"`.
- `$.operation_results[1].refs`: expected `[{"id": "rec:challenge-candidate", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[1].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[1].type`: expected `"receipt"`; actual `"refusal"`.
- `$.postconditions.record_refs.length`: expected `7`; actual `6`.
- `$.postconditions.record_refs[0].id`: expected `"rec:challenge-candidate"`; actual `"rec:d"`.
- `$.postconditions.record_refs[1].version`: expected `1`; actual `2`.
- `$.postconditions.record_refs[2].version`: expected `2`; actual `3`.
- `$.postconditions.record_refs[3].id`: expected `"rec:d"`; actual `"rec:receipt1"`.
- `$.postconditions.record_refs[3].version`: expected `3`; actual `1`.
- `$.postconditions.record_refs[4].id`: expected `"rec:receipt1"`; actual `"rec:receipt2"`.
- `$.postconditions.record_refs[5].id`: expected `"rec:receipt2"`; actual `"rec:receipt3"`.
- `$.result.authorized_snapshot_handle`: expected `"@h3"`; actual `"<absent>"`.
- `$.result.changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.result.code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.result.currentness`: expected `"ambiguous_current"`; actual `"<absent>"`.
- `$.result.cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.result.data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.result.evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.result.explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.result.historical`: expected `[{"id": "rec:d", "version": 1}]`; actual `"<absent>"`.
- `$.result.items`: expected `[{"ref": {"id": "rec:d", "version": 2}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "machine_observation", "statement_kind": "decision_record", "content": [{"field": "value", "value": "delete_home"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "ambiguous_current", "authority_receipt": {"id": "rec:receipt2", "version": 1}, "incompatible_with": [], "needs_review": false, "source_refs": [{"id": "rec:receipt2", "version": 1}], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}, {"ref": {"id": "rec:d", "version": 3}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "machine_observation", "statement_kind": "decision_record", "content": [{"field": "value", "value": "retain_home"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "ambiguous_current", "authority_receipt": {"id": "rec:receipt3", "version": 1}, "incompatible_with": [], "needs_review": false, "source_refs": [{"id": "rec:receipt3", "version": 1}], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `$.result.policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.result.projection_rule`: expected `{"id": "projection:main", "version": 1}`; actual `"<absent>"`.
- `$.result.retryable`: expected `"<absent>"`; actual `false`.
- `$.result.review_required`: expected `[]`; actual `"<absent>"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"<absent>"`.
- `$.result.type`: expected `"view"`; actual `"refusal"`.
- `pair:/operation_results/0=/result.authorized_snapshot_handle`: expected `"<fresh>"`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.code`: expected `"<absent>"`; actual `"invalid_time"`.
- `pair:/operation_results/0=/result.currentness`: expected `"ambiguous_current"`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.cutoffs`: expected `[]`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.data_classification`: expected `"data"`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.historical`: expected `[{"id": "rec:d", "version": 1}]`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.items`: expected `[{"ref": {"id": "rec:d", "version": 2}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "machine_observation", "statement_kind": "decision_record", "content": [{"field": "value", "value": "delete_home"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "ambiguous_current", "authority_receipt": {"id": "rec:receipt2", "version": 1}, "incompatible_with": [], "needs_review": false, "source_refs": [{"id": "rec:receipt2", "version": 1}], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "<fresh>", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "<fresh>", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}, {"ref": {"id": "rec:d", "version": 3}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "machine_observation", "statement_kind": "decision_record", "content": [{"field": "value", "value": "retain_home"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "ambiguous_current", "authority_receipt": {"id": "rec:receipt3", "version": 1}, "incompatible_with": [], "needs_review": false, "source_refs": [{"id": "rec:receipt3", "version": 1}], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "<fresh>", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "<fresh>", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.projection_rule`: expected `{"id": "projection:main", "version": 1}`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.retryable`: expected `"<absent>"`; actual `false`.
- `pair:/operation_results/0=/result.review_required`: expected `[]`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.semantic_profile`: expected `"0.2.3-draft"`; actual `"<absent>"`.
- `pair:/operation_results/0=/result.type`: expected `"view"`; actual `"refusal"`.
- `forbidden:/operation_results/1/type`: expected `"predicate false"`; actual `{"path": "/operation_results/1/type", "test": "equals", "value": "refusal"}`.

## ASTRA24-08-CONTROL

28 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[1].code`: expected `"<absent>"`; actual `"invalid_shape"`.
- `$.operation_results[1].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[1].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[1].operation`: expected `"revise"`; actual `"<absent>"`.
- `$.operation_results[1].outcome`: expected `"revised"`; actual `"<absent>"`.
- `$.operation_results[1].receipt_handle`: expected `"@h2"`; actual `"<absent>"`.
- `$.operation_results[1].refs`: expected `[{"id": "rec:withdraw-candidate", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[1].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[1].type`: expected `"receipt"`; actual `"refusal"`.
- `$.postconditions.record_refs.length`: expected `7`; actual `6`.
- `$.result.authorized_snapshot_handle`: expected `"@h3"`; actual `"<absent>"`.
- `$.result.changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.result.code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.result.currentness`: expected `"current"`; actual `"<absent>"`.
- `$.result.cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.result.data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.result.evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.result.explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.result.historical`: expected `[{"id": "rec:d", "version": 1}]`; actual `"<absent>"`.
- `$.result.items`: expected `[{"ref": {"id": "rec:d", "version": 2}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "machine_observation", "statement_kind": "decision_record", "content": [{"field": "value", "value": "delete_home"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "current", "authority_receipt": {"id": "rec:receipt2", "version": 1}, "incompatible_with": [], "needs_review": false, "source_refs": [{"id": "rec:receipt2", "version": 1}], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `$.result.policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.result.projection_rule`: expected `{"id": "projection:main", "version": 1}`; actual `"<absent>"`.
- `$.result.retryable`: expected `"<absent>"`; actual `false`.
- `$.result.review_required`: expected `[]`; actual `"<absent>"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"<absent>"`.
- `$.result.type`: expected `"view"`; actual `"refusal"`.
- `forbidden:/operation_results/1/type`: expected `"predicate false"`; actual `{"path": "/operation_results/1/type", "test": "equals", "value": "refusal"}`.

## ASTRA24-08-NEXT

53 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[1].code`: expected `"<absent>"`; actual `"invalid_shape"`.
- `$.operation_results[1].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[1].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[1].operation`: expected `"revise"`; actual `"<absent>"`.
- `$.operation_results[1].outcome`: expected `"revised"`; actual `"<absent>"`.
- `$.operation_results[1].receipt_handle`: expected `"@h2"`; actual `"<absent>"`.
- `$.operation_results[1].refs`: expected `[{"id": "rec:withdraw-candidate", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[1].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[1].type`: expected `"receipt"`; actual `"refusal"`.
- `$.operation_results[2].authorized_snapshot_handle`: expected `"@h3"`; actual `"<absent>"`.
- `$.operation_results[2].changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.operation_results[2].code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.operation_results[2].currentness`: expected `"current"`; actual `"<absent>"`.
- `$.operation_results[2].cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[2].data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.operation_results[2].evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[2].explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.operation_results[2].historical`: expected `[{"id": "rec:d", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[2].items`: expected `[{"ref": {"id": "rec:d", "version": 2}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "machine_observation", "statement_kind": "decision_record", "content": [{"field": "value", "value": "delete_home"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "current", "authority_receipt": {"id": "rec:receipt2", "version": 1}, "incompatible_with": [], "needs_review": false, "source_refs": [{"id": "rec:receipt2", "version": 1}], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `$.operation_results[2].policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[2].projection_rule`: expected `{"id": "projection:main", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[2].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[2].review_required`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[2].semantic_profile`: expected `"0.2.2-draft"`; actual `"<absent>"`.
- `$.operation_results[2].type`: expected `"view"`; actual `"refusal"`.
- `$.operation_results[3].code`: expected `"<absent>"`; actual `"invalid_shape"`.
- `$.operation_results[3].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[3].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[3].operation`: expected `"revise"`; actual `"<absent>"`.
- `$.operation_results[3].outcome`: expected `"revised"`; actual `"<absent>"`.
- `$.operation_results[3].receipt_handle`: expected `"@h4"`; actual `"<absent>"`.
- `$.operation_results[3].refs`: expected `[{"id": "rec:withdraw-next", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[3].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[3].type`: expected `"receipt"`; actual `"refusal"`.
- `$.postconditions.record_refs.length`: expected `8`; actual `6`.
- `$.result.authorized_snapshot_handle`: expected `"@h5"`; actual `"<absent>"`.
- `$.result.changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.result.code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.result.currentness`: expected `"current"`; actual `"<absent>"`.
- `$.result.cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.result.data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.result.evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.result.explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.result.historical`: expected `[]`; actual `"<absent>"`.
- `$.result.items`: expected `[{"ref": {"id": "rec:d", "version": 1}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "machine_observation", "statement_kind": "decision_record", "content": [{"field": "value", "value": "archive_home"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "current", "authority_receipt": {"id": "rec:receipt1", "version": 1}, "incompatible_with": [], "needs_review": false, "source_refs": [{"id": "rec:receipt1", "version": 1}], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h5", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h5", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `$.result.policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.result.projection_rule`: expected `{"id": "projection:main", "version": 1}`; actual `"<absent>"`.
- `$.result.retryable`: expected `"<absent>"`; actual `false`.
- `$.result.review_required`: expected `[]`; actual `"<absent>"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"<absent>"`.
- `$.result.type`: expected `"view"`; actual `"refusal"`.
- `forbidden:/operation_results/3/type`: expected `"predicate false"`; actual `{"path": "/operation_results/3/type", "test": "equals", "value": "refusal"}`.

## ASTRA24-08-STALE

4 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[1].code`: expected `"version_conflict"`; actual `"invalid_shape"`.
- `$.operation_results[1].retryable`: expected `true`; actual `false`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-08

4 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[1].code`: expected `"version_conflict"`; actual `"invalid_shape"`.
- `$.operation_results[1].retryable`: expected `true`; actual `false`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-07

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-04

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-03

3 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[1].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-05

3 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[1].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-01

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-02

4 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[1].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.operation_results[2].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-06

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

## ASTRA24-09

2 exact differences

- `$.operation_results[0].semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.
- `$.result.semantic_profile`: expected `"0.2.2-draft"`; actual `"0.2.3-draft"`.

Full normalized actual reports and input hashes: `phase2-retention-mixed-profile-first.json`.
