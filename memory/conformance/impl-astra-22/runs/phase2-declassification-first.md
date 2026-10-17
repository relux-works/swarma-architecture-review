# astra-22 vector results

Package: **0.2.3-draft**, package commit `23290b3a96a469d5190cb71b0e20139896b89236`.
Vector directory: `memory/spec/kernel/vectors` (this inventory only).
Checkout: `d07706451fd7b91ad009747c23a2bc178c1d941c`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 49 | 1 | 7 |
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
| P05 | semantic | fail | 54 exact differences |
| P06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P08 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| P09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P11 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P12 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P13 | semantic | pass | Exact report and forbidden/normalization checks passed. |
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

## P05

54 exact differences

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
- `$.operation_results[5].code`: expected `"disclosure_revoked"`; actual `"not_authorized"`.
- `$.postconditions.record_refs.length`: expected `5`; actual `2`.
- `$.postconditions.record_refs[0].id`: expected `"rec:city"`; actual `"rec:coordinates"`.
- `$.postconditions.record_refs[1].id`: expected `"rec:coordinates"`; actual `"rec:private-preference"`.
- `$.result.authorized_snapshot_handle`: expected `"@h5"`; actual `"<absent>"`.
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

Full normalized actual reports and input hashes: `phase2-declassification-first.json`.
