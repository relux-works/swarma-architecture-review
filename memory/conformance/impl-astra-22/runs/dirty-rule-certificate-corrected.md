# astra-22 vector results

Package: **0.2.2-draft**, package commit `7e71765317088d4ac1ea6946fdfb4b2f8012643c`.
Vector directory: `memory/conformance/impl-astra-22/fixtures/dirty-rule-certificate` (this inventory only).
Checkout: `4744e62e3d93228a438daae8ad6610c58ea7b14d`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 3 | 0 | 0 |
| deployment | 0 | 0 | 0 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| JUDGE-DIRTY-CERTIFICATE | semantic | pass | Exact report and forbidden/normalization checks passed. |
| JUDGE-DIRTY-PREMISE-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| JUDGE-DIRTY-RULE | semantic | pass | Exact report and forbidden/normalization checks passed. |

Full normalized actual reports and input hashes: `dirty-rule-certificate-corrected.json`.
