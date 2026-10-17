# astra-22 vector results

Package: **0.1.0-draft**, package commit `0ef608ae279a9bc209ad78ffdc72dbbbdc828f8f`.
Checkout: `0ef608ae279a9bc209ad78ffdc72dbbbdc828f8f`. Source core SHA-256: `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.

The core is the source-only frozen implementation. The adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 17 | 7 | 29 |
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
| B01 | semantic | unsupported | Unmapped frozen-core transaction operations: revise |
| B02 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| B03 | semantic | fail | 1 exact differences |
| B07 | semantic | unsupported | Unmapped frozen-core transaction operations: admit, erase, revise |
| B08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B12 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| B13 | semantic | fail | 4 exact differences |
| B14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P02 | semantic | unsupported | Unmapped frozen-core transaction operations: revise |
| P03 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| P04 | semantic | unsupported | Frozen core has no cross-assertion incompatible_with computation |
| P05 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify |
| P06 | semantic | unsupported | Unmapped frozen-core transaction operations: deliver, revoke |
| P07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P08 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| P09 | semantic | unsupported | Frozen core has no full audience item redaction/alias output |
| P10 | semantic | unsupported | Unmapped frozen-core transaction operations: revise |
| P11 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| S01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S07 | semantic | unsupported | Frozen core has no exact proof-path enumeration or changes output |
| S08 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| S09 | semantic | unsupported | Frozen core has no cross-assertion incompatible_with computation |
| S10 | semantic | unsupported | Frozen core has no cross-assertion incompatible_with computation |
| S11 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S12 | semantic | fail | 4 exact differences |
| S13 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| S14 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| S15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S16 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| S17 | semantic | unsupported | Unmapped frozen-core transaction operations: revise |
| S18 | semantic | unsupported | Unmapped frozen-core transaction operations: admit_raw |
| S19 | semantic | unsupported | Unmapped frozen-core transaction operations: revise |
| S20 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| S21 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S22 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S23 | semantic | fail | 1 exact differences |
| S24 | semantic | unsupported | Unmapped frozen-core transaction operations: admit, erase, revise |
| S25 | semantic | unsupported | Unmapped frozen-core transaction operations: erase, reconcile_restore, restore |
| S26 | semantic | unsupported | Unmapped frozen-core transaction operations: admit, erase |
| S27 | semantic | unsupported | Unmapped frozen-core transaction operations: load, set_availability |
| S28 | semantic | fail | 2 exact differences |
| S29 | semantic | fail | 1 exact differences |
| S30 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S31 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S32 | semantic | fail | 5 exact differences |
| S33 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |

## B03

1 exact differences

- `$.result.items[0].source_refs.length`: expected `1`; actual `0`.

## B13

4 exact differences

- `$.result.cutoffs.length`: expected `1`; actual `0`.
- `$.result.items[0].oppose.source_state`: expected `"prior_assessment_only"`; actual `"resolvable_now"`.
- `$.result.items[0].support.evaluation`: expected `"incomplete"`; actual `"complete"`.
- `$.result.items[0].support.source_state`: expected `"prior_assessment_only"`; actual `"resolvable_now"`.

## S12

4 exact differences

- `$.result.cutoffs.length`: expected `1`; actual `0`.
- `$.result.items[0].oppose.source_state`: expected `"prior_assessment_only"`; actual `"resolvable_now"`.
- `$.result.items[0].support.evaluation`: expected `"incomplete"`; actual `"complete"`.
- `$.result.items[0].support.source_state`: expected `"prior_assessment_only"`; actual `"resolvable_now"`.

## S23

1 exact differences

- `$.result.items[0].source_refs.length`: expected `1`; actual `0`.

## S28

2 exact differences

- `$.result.items[0].source_refs.length`: expected `1`; actual `0`.
- `$.result.items[1].source_refs.length`: expected `1`; actual `0`.

## S29

1 exact differences

- `$.result.items[0].source_refs.length`: expected `1`; actual `0`.

## S32

5 exact differences

- `$.operation_results[0].items[0].oppose.source_state`: expected `"prior_assessment_only"`; actual `"resolvable_now"`.
- `$.operation_results[0].items[1].oppose.source_state`: expected `"prior_assessment_only"`; actual `"resolvable_now"`.
- `$.result.items[0].oppose.source_state`: expected `"prior_assessment_only"`; actual `"resolvable_now"`.
- `$.result.items[0].support.source_state`: expected `"prior_assessment_only"`; actual `"resolvable_now"`.
- `forbidden:/result/items/0/support/source_state`: expected `"predicate false"`; actual `{"path": "/result/items/0/support/source_state", "test": "equals", "value": "resolvable_now"}`.

Full normalized actual reports and input hashes: `RESULTS.json`.
