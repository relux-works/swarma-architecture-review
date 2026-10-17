# astra-22 vector results

Package: **0.2.5-draft**, package commit `6a04e8cfb1490569cd1de7468d2085dd4840cf51`.
Vector directory: `memory/spec/kernel/vectors` (this inventory only).
Checkout: `0529814720bb9fd19b9e737807473ba4f48dc7ff`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 57 | 0 | 0 |
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
| B07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B12 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B13 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B14 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| B15 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| P08 | semantic | pass | Exact report and forbidden/normalization checks passed. |
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
| S20 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S21 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S22 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S23 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S24 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S25 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S26 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S27 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S28 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S29 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S30 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S31 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S32 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| S33 | semantic | pass | Exact report and forbidden/normalization checks passed. |

Full normalized actual reports and input hashes: `phase2-availability-corrected.json`.
