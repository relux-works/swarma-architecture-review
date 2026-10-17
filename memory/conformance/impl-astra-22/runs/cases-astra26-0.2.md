# astra-22 vector results

Package: **0.2.0-draft**, package commit `cde5754d523b98c93cf2b1777fe80e15b9efa74c`.
Vector directory: `.temp/astra-22/cases-astra26-02` (this inventory only).
Checkout: `56e45ed34d0c619aa76943892fa16b32677b73ca`. Source core SHA-256: `8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 4 | 0 | 4 |
| deployment | 0 | 0 | 0 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA26-06 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| ASTRA26-01 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| ASTRA26-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02 | semantic | unsupported | Frozen core has no imported-publication currentness state |
| ASTRA26-05 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| ASTRA26-03-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |

Full normalized actual reports and input hashes: `cases-astra26-0.2.json`.
