# astra-22 vector results

Package: **0.2.0-draft**, package commit `cde5754d523b98c93cf2b1777fe80e15b9efa74c`.
Vector directory: `memory/spec/kernel/vectors` (this inventory only).
Checkout: `56e45ed34d0c619aa76943892fa16b32677b73ca`. Source core SHA-256: `8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 29 | 0 | 28 |
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
| B03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B07 | semantic | unsupported | Unmapped frozen-core transaction operations: admit, erase, revise |
| B08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B12 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| B13 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P02 | semantic | unsupported | Unmapped frozen-core transaction operations: revise |
| P03 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| P04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P05 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, deliver, revoke_declassification |
| P06 | semantic | unsupported | Unmapped frozen-core transaction operations: deliver, revoke |
| P07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P08 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| P09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P10 | semantic | unsupported | Unmapped frozen-core transaction operations: revise |
| P11 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| P12 | semantic | unsupported | Unmapped frozen-core transaction operations: deliver, revoke |
| P13 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| P14 | semantic | unsupported | Unmapped frozen-core transaction operations: revise |
| P15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S07 | semantic | unsupported | Frozen core has no exact proof-path enumeration or changes output |
| S08 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| S09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S11 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S12 | semantic | pass | Exact report and forbidden/normalization checks passed. |
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
| S23 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S24 | semantic | unsupported | Unmapped frozen-core transaction operations: admit, erase, revise |
| S25 | semantic | unsupported | Unmapped frozen-core transaction operations: erase, reconcile_restore, restore |
| S26 | semantic | unsupported | Unmapped frozen-core transaction operations: admit, erase |
| S27 | semantic | unsupported | Unmapped frozen-core transaction operations: load, set_availability |
| S28 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S29 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S30 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S31 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S32 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S33 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |

Full normalized actual reports and input hashes: `RESULTS.json`.
