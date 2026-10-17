# astra-22 vector results

Package: **0.2.3-draft**, package commit `23290b3a96a469d5190cb71b0e20139896b89236`.
Vector directory: `memory/spec/kernel/vectors` (this inventory only).
Checkout: `bd75f4fa86f1779850713a1b5d64d789427ea4bd`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 47 | 2 | 8 |
| deployment | 0 | 0 | 8 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| B04 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B05 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B06 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B09 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B10 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B11 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B16 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B17 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| B01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B07 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| B08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B12 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B13 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P05 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, revoke_declassification |
| P06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P08 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| P09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P11 | semantic | fail | 67 exact differences |
| P12 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P13 | semantic | fail | 56 exact differences |
| P14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S11 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S12 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S13 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S16 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S17 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S18 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S19 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S20 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| S21 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S22 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S23 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S24 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| S25 | semantic | unsupported | Unmapped frozen-core transaction operations: erase, reconcile_restore, restore |
| S26 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| S27 | semantic | unsupported | Unmapped frozen-core transaction operations: load, set_availability |
| S28 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S29 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S30 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S31 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S32 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S33 | semantic | pass | Exact report and forbidden/normalization checks passed. |

## P11

67 exact differences

- `$.operation_results[0].code`: expected `"not_authorized"`; actual `"<absent>"`.
- `$.operation_results[0].custody`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[0].erasure_status`: expected `"<absent>"`; actual `null`.
- `$.operation_results[0].operation`: expected `"<absent>"`; actual `"admit"`.
- `$.operation_results[0].outcome`: expected `"<absent>"`; actual `"admitted"`.
- `$.operation_results[0].receipt_handle`: expected `"<absent>"`; actual `"e2e2a556b8deb79a77dbf4a2660b3f78"`.
- `$.operation_results[0].refs`: expected `"<absent>"`; actual `[{"id": "rec:scope-probe", "version": 1}]`.
- `$.operation_results[0].retryable`: expected `false`; actual `"<absent>"`.
- `$.operation_results[0].type`: expected `"refusal"`; actual `"receipt"`.
- `$.operation_results[1].code`: expected `"not_authorized"`; actual `"duplicate_record"`.
- `$.operation_results[2].code`: expected `"not_authorized"`; actual `"<absent>"`.
- `$.operation_results[2].custody`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[2].erasure_status`: expected `"<absent>"`; actual `null`.
- `$.operation_results[2].operation`: expected `"<absent>"`; actual `"admit"`.
- `$.operation_results[2].outcome`: expected `"<absent>"`; actual `"admitted"`.
- `$.operation_results[2].receipt_handle`: expected `"<absent>"`; actual `"4fbf083ab62c12d8a5485cbb1ba5683f"`.
- `$.operation_results[2].refs`: expected `"<absent>"`; actual `[{"id": "rec:paraphrase", "version": 1}]`.
- `$.operation_results[2].retryable`: expected `false`; actual `"<absent>"`.
- `$.operation_results[2].type`: expected `"refusal"`; actual `"receipt"`.
- `$.operation_results[3].code`: expected `"not_authorized"`; actual `"idempotency_conflict"`.
- `$.operation_results[4].code`: expected `"not_authorized"`; actual `"idempotency_conflict"`.
- `$.operation_results[5].code`: expected `"not_authorized"`; actual `"idempotency_conflict"`.
- `$.operation_results[6].code`: expected `"not_authorized"`; actual `"idempotency_conflict"`.
- `$.operation_results[7].authorized_snapshot_handle`: expected `"<absent>"`; actual `"3f6efa68e8dc4a4690d9e7908300209d"`.
- `$.operation_results[7].changes`: expected `"<absent>"`; actual `{"state": "initial", "refs": []}`.
- `$.operation_results[7].code`: expected `"invalid_time"`; actual `"<absent>"`.
- `$.operation_results[7].currentness`: expected `"<absent>"`; actual `"none"`.
- `$.operation_results[7].cutoffs`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[7].data_classification`: expected `"<absent>"`; actual `"data"`.
- `$.operation_results[7].evidence_policy`: expected `"<absent>"`; actual `{"id": "evidence:1", "version": 1}`.
- `$.operation_results[7].explanation`: expected `"<absent>"`; actual `{"status": "complete", "paths": [], "reason": null}`.
- `$.operation_results[7].historical`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[7].items`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[7].policy`: expected `"<absent>"`; actual `{"id": "policy:1", "version": 1}`.
- `$.operation_results[7].projection_rule`: expected `"<absent>"`; actual `{"id": "projection:main", "version": 1}`.
- `$.operation_results[7].retryable`: expected `false`; actual `"<absent>"`.
- `$.operation_results[7].review_required`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[7].semantic_profile`: expected `"<absent>"`; actual `"0.2.3-draft"`.
- `$.operation_results[7].type`: expected `"refusal"`; actual `"view"`.
- `$.operation_results[8].code`: expected `"<absent>"`; actual `"idempotency_conflict"`.
- `$.operation_results[8].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[8].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[8].operation`: expected `"admit"`; actual `"<absent>"`.
- `$.operation_results[8].outcome`: expected `"admitted"`; actual `"<absent>"`.
- `$.operation_results[8].receipt_handle`: expected `"@h1"`; actual `"<absent>"`.
- `$.operation_results[8].refs`: expected `[{"id": "rec:paraphrase", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[8].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[8].type`: expected `"receipt"`; actual `"refusal"`.
- `$.operation_results[9].code`: expected `"<absent>"`; actual `"idempotency_conflict"`.
- `$.operation_results[9].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[9].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[9].operation`: expected `"admit"`; actual `"<absent>"`.
- `$.operation_results[9].outcome`: expected `"admitted"`; actual `"<absent>"`.
- `$.operation_results[9].receipt_handle`: expected `"@h1"`; actual `"<absent>"`.
- `$.operation_results[9].refs`: expected `[{"id": "rec:paraphrase", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[9].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[9].type`: expected `"receipt"`; actual `"refusal"`.
- `$.operation_results[11].currentness`: expected `"current"`; actual `"none"`.
- `$.operation_results[11].items.length`: expected `1`; actual `0`.
- `$.operation_results[13].code`: expected `"not_authorized"`; actual `"idempotency_conflict"`.
- `$.operation_results[14].code`: expected `"not_authorized"`; actual `"duplicate_record"`.
- `$.operation_results[15].currentness`: expected `"current"`; actual `"none"`.
- `$.operation_results[15].items.length`: expected `1`; actual `0`.
- `$.postconditions.record_refs.length`: expected `3`; actual `4`.
- `forbidden:/operation_results/0/type`: expected `"predicate false"`; actual `{"path": "/operation_results/0/type", "test": "equals", "value": "receipt"}`.
- `forbidden:/operation_results/2/type`: expected `"predicate false"`; actual `{"path": "/operation_results/2/type", "test": "equals", "value": "receipt"}`.
- `forbidden:/postconditions/record_refs`: expected `"predicate false"`; actual `{"path": "/postconditions/record_refs", "test": "size_equals", "value": 4}`.

## P13

56 exact differences

- `$.operation_results[0].code`: expected `"not_authorized"`; actual `"<absent>"`.
- `$.operation_results[0].custody`: expected `"<absent>"`; actual `[]`.
- `$.operation_results[0].erasure_status`: expected `"<absent>"`; actual `null`.
- `$.operation_results[0].operation`: expected `"<absent>"`; actual `"admit"`.
- `$.operation_results[0].outcome`: expected `"<absent>"`; actual `"admitted"`.
- `$.operation_results[0].receipt_handle`: expected `"<absent>"`; actual `"586797c45a244a606e21c8e9bb5053be"`.
- `$.operation_results[0].refs`: expected `"<absent>"`; actual `[{"id": "rec:model-unknown", "version": 1}]`.
- `$.operation_results[0].retryable`: expected `false`; actual `"<absent>"`.
- `$.operation_results[0].type`: expected `"refusal"`; actual `"receipt"`.
- `$.operation_results[1].code`: expected `"invalid_reference"`; actual `"idempotency_conflict"`.
- `$.operation_results[2].code`: expected `"<absent>"`; actual `"idempotency_conflict"`.
- `$.operation_results[2].custody`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[2].erasure_status`: expected `null`; actual `"<absent>"`.
- `$.operation_results[2].operation`: expected `"admit"`; actual `"<absent>"`.
- `$.operation_results[2].outcome`: expected `"admitted"`; actual `"<absent>"`.
- `$.operation_results[2].receipt_handle`: expected `"@h1"`; actual `"<absent>"`.
- `$.operation_results[2].refs`: expected `[{"id": "rec:model-clean", "version": 1}, {"id": "rec:model-empty", "version": 1}, {"id": "rec:model-stage", "version": 1}, {"id": "rec:model-tainted", "version": 1}, {"id": "rec:model-unknown", "version": 1}]`; actual `"<absent>"`.
- `$.operation_results[2].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[2].type`: expected `"receipt"`; actual `"refusal"`.
- `$.operation_results[3].authorized_snapshot_handle`: expected `"@h2"`; actual `"<absent>"`.
- `$.operation_results[3].changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.operation_results[3].code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.operation_results[3].currentness`: expected `"current"`; actual `"<absent>"`.
- `$.operation_results[3].cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[3].data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.operation_results[3].evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[3].explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.operation_results[3].historical`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[3].items`: expected `[{"ref": {"id": "rec:model-tainted", "version": 1}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "semantic_inference", "statement_kind": "proposal", "content": [{"field": "value", "value": "candidate with private context"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "current", "authority_receipt": null, "incompatible_with": [], "needs_review": false, "source_refs": [], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h2", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h2", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}, {"ref": {"id": "rec:model-unknown", "version": 1}, "subject": "subj:h1", "issuer": "subj:h1", "submitter": "subj:h1", "perspective": {"kind": "own", "principal": "subj:h1"}, "representation_ref": null, "admission_class": "semantic_inference", "statement_kind": "proposal", "content": [{"field": "value", "value": "candidate without complete input tracking"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "current", "authority_receipt": null, "incompatible_with": [], "needs_review": false, "source_refs": [], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h2", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h2", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `$.operation_results[3].policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[3].projection_rule`: expected `{"id": "projection:main", "version": 1}`; actual `"<absent>"`.
- `$.operation_results[3].retryable`: expected `"<absent>"`; actual `false`.
- `$.operation_results[3].review_required`: expected `[]`; actual `"<absent>"`.
- `$.operation_results[3].semantic_profile`: expected `"0.2.3-draft"`; actual `"<absent>"`.
- `$.operation_results[3].type`: expected `"view"`; actual `"refusal"`.
- `$.postconditions.record_refs.length`: expected `7`; actual `3`.
- `$.postconditions.record_refs[0].id`: expected `"rec:model-clean"`; actual `"rec:model-unknown"`.
- `$.postconditions.record_refs[1].id`: expected `"rec:model-empty"`; actual `"rec:private-input"`.
- `$.postconditions.record_refs[2].id`: expected `"rec:model-stage"`; actual `"rec:public-input"`.
- `$.result.authorized_snapshot_handle`: expected `"@h3"`; actual `"<absent>"`.
- `$.result.changes`: expected `{"state": "initial", "refs": []}`; actual `"<absent>"`.
- `$.result.code`: expected `"<absent>"`; actual `"invalid_time"`.
- `$.result.currentness`: expected `"current"`; actual `"<absent>"`.
- `$.result.cutoffs`: expected `[]`; actual `"<absent>"`.
- `$.result.data_classification`: expected `"data"`; actual `"<absent>"`.
- `$.result.evidence_policy`: expected `{"id": "evidence:1", "version": 1}`; actual `"<absent>"`.
- `$.result.explanation`: expected `{"status": "complete", "paths": [], "reason": null}`; actual `"<absent>"`.
- `$.result.historical`: expected `[]`; actual `"<absent>"`.
- `$.result.items`: expected `[{"ref": null, "subject": "subj:model-output", "issuer": "subj:model-output", "submitter": "subj:model-output", "perspective": {"kind": "own", "principal": "subj:model-output"}, "representation_ref": null, "admission_class": "semantic_inference", "statement_kind": "proposal", "content": [{"field": "value", "value": "candidate from only public context"}], "valid": {"kind": "known", "from": "2026-09-01T00:00:00Z", "to": null, "precision": "second"}, "confirmed_at": "2026-10-17T00:00:00Z", "usable_until": null, "currentness": "current", "authority_receipt": null, "incompatible_with": [], "needs_review": false, "source_refs": [], "support": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}, "oppose": {"witness": "not_found", "evaluation": "complete", "corpus_coverage": {"kind": "unknown"}, "premise_quality": "not_fully_checked", "evidence_qualification": [], "source_state": "resolvable_now", "freshness": "not_applicable", "authorized_snapshot_handle": "@h3", "dependency_coverage": "registered_only", "witness_roots": [], "independent_root_count": 0}}]`; actual `"<absent>"`.
- `$.result.policy`: expected `{"id": "policy:1", "version": 1}`; actual `"<absent>"`.
- `$.result.projection_rule`: expected `{"id": "projection:public", "version": 1}`; actual `"<absent>"`.
- `$.result.retryable`: expected `"<absent>"`; actual `false`.
- `$.result.review_required`: expected `[]`; actual `"<absent>"`.
- `$.result.semantic_profile`: expected `"0.2.3-draft"`; actual `"<absent>"`.
- `$.result.type`: expected `"view"`; actual `"refusal"`.
- `forbidden:/operation_results/0/type`: expected `"predicate false"`; actual `{"path": "/operation_results/0/type", "test": "equals", "value": "receipt"}`.

Full normalized actual reports and input hashes: `0.2.3-first.json`.
