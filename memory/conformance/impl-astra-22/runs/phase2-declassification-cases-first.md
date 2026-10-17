# astra-22 vector results

Package: **0.2.3-draft**, package commit `23290b3a96a469d5190cb71b0e20139896b89236`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `d07706451fd7b91ad009747c23a2bc178c1d941c`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 37 | 1 | 8 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-08-CHALLENGE | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08-NEXT | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08-STALE | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-02 | semantic | fail | 70 exact differences |
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

## ASTRA25-02

70 exact differences

- `$.operation_results[1].code`: expected `"<absent>"`; actual `"declassification_invalid"`.
- `$.operation_results[1].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[1].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[1].operation`: expected `"declassify"`; actual `"<absent>"`.
- `$.operation_results[1].outcome`: expected `"declassified"`; actual `"<absent>"`.
- `$.operation_results[1].receipt_handle`: expected `"@h1"`; actual `"<absent>"`.
- `$.operation_results[1].refs`: expected `[{"id": "rec:city", "version": 1}, {"id": "rec:release-a", "version": 1}, {"id": "rec:release-b", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[1].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[1].type`: expected `"receipt"`; actual `"refusal"`.
- `$.operation_results[2].authorized_snapshot_handle`: expected `"@h2"`; actual `"<absent>"`.
- `$.operation_results[2].changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.operation_results[2].code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.operation_results[2].currentness`: expected `"current"`; actual `"<absent>"`.
- `$.operation_results[2].cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[2].data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.operation_results[2].evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[2].explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.operation_results[2].historical`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[2].items`: expected `[{"ref": null, "subject": "subj:public-a", "issuer": "subj:public-a", "submitter": "subj:public-a", "perspective": {"kind": "own", "principal": "subj:public-a"}, "representation_ref": null, "admission_class": "self_declaration", "statement_kind": "self_declaration", "content": [{"field": "value", "value": "Synthetic City"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": "2026-10-24T00:00:00Z", "currentness": "current", "authority_receipt": null, "incompatible_with": [], "needs_review": false, "source_refs": [], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "fresh", "authorized_snapshot_handle": "@h2", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "fresh", "authorized_snapshot_handle": "@h2", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `$.operation_results[2].policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[2].projection_rule`: expected `{"id": "projection:public", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[2].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[2].review_required`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[2].semantic_profile`: expected `"0.2.3-draft"`; actual `"<absent>"`.
- `$.operation_results[2].type`: expected `"view"`; actual `"refusal"`.
- `$.operation_results[3].code`: expected `"<absent>"`; actual `"not_authorized"`.
- `$.operation_results[3].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[3].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[3].operation`: expected `"deliver"`; actual `"<absent>"`.
- `$.operation_results[3].outcome`: expected `"delivered"`; actual `"<absent>"`.
- `$.operation_results[3].receipt_handle`: expected `"@h3"`; actual `"<absent>"`.
- `$.operation_results[3].refs`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[3].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[3].type`: expected `"receipt"`; actual `"refusal"`.
- `$.operation_results[5].authorized_snapshot_handle`: expected `"@h4"`; actual `"<absent>"`.
- `$.operation_results[5].changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.operation_results[5].code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.operation_results[5].currentness`: expected `"current"`; actual `"<absent>"`.
- `$.operation_results[5].cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[5].data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.operation_results[5].evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[5].explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.operation_results[5].historical`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[5].items`: expected `[{"ref": null, "subject": "subj:public-a", "issuer": "subj:public-a", "submitter": "subj:public-a", "perspective": {"kind": "own", "principal": "subj:public-a"}, "representation_ref": null, "admission_class": "self_declaration", "statement_kind": "self_declaration", "content": [{"field": "value", "value": "Synthetic City"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": "2026-10-24T00:00:00Z", "currentness": "current", "authority_receipt": null, "incompatible_with": [], "needs_review": false, "source_refs": [], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "fresh", "authorized_snapshot_handle": "@h4", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "fresh", "authorized_snapshot_handle": "@h4", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `$.operation_results[5].policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[5].projection_rule`: expected `{"id": "projection:public", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[5].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[5].review_required`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[5].semantic_profile`: expected `"0.2.3-draft"`; actual `"<absent>"`.
- `$.operation_results[5].type`: expected `"view"`; actual `"refusal"`.
- `$.operation_results[7].code`: expected `"disclosure_revoked"`; actual `"not_authorized"`.
- `$.postconditions.record_refs.length`: expected `5`; actual `2`.
- `$.postconditions.record_refs[0].id`: expected `"rec:city"`; actual `"rec:coordinates"`.
- `$.postconditions.record_refs[1].id`: expected `"rec:coordinates"`; actual `"rec:private-preference"`.
- `$.result.authorized_snapshot_handle`: expected `"@h6"`; actual `"<absent>"`.
- `$.result.changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.result.code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.result.currentness`: expected `"none"`; actual `"<absent>"`.
- `$.result.cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.result.data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.result.evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.result.explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.result.historical`: expected `[]`; actual `"<absent>"`.
- `$.result.items`: expected `[]`; actual `"<absent>"`.
- `$.result.policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.result.projection_rule`: expected `{"id": "projection:public", "version": 1}`; actual `"<absent>"`.
- `$.result.retryable`: expected `"<absent>"`; actual `false`.
- `$.result.review_required`: expected `[]`; actual `"<absent>"`.
- `$.result.semantic_profile`: expected `"0.2.3-draft"`; actual `"<absent>"`.
- `$.result.type`: expected `"view"`; actual `"refusal"`.

Full normalized actual reports and input hashes: `phase2-declassification-cases-first.json`.
