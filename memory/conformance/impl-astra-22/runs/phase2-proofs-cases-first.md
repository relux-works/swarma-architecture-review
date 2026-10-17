# astra-22 vector results

Package: **0.2.1-draft**, package commit `f31d58f58d05de2ae4159dedaacfa1e32bdc656d`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `b1ae29958027ec67ecadae310a2e78838fcca09c`. Source core SHA-256: `999b53173fb7fe7127b5a1370b31f988e71f1f8a1fecfa922c4febb3eee6b0cc`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 15 | 0 | 7 |
| deployment | 0 | 0 | 1 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-02 | semantic | unsupported | Unmapped frozen-core transaction operations: declassify, deliver, revoke_declassification |
| ASTRA25-05-CONTROL | semantic | unsupported | Frozen core has no dirty/review-closure output |
| ASTRA25-05 | semantic | unsupported | Frozen core has no dirty/review-closure output |
| ASTRA25-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-04 | deployment | unsupported | No protected deployment; a semantic simulator cannot qualify this boundary. |
| ASTRA25-03-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03-FENCE | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA26-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02 | semantic | unsupported | Frozen core has no imported-publication currentness state |
| ASTRA26-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |

Full normalized actual reports and input hashes: `phase2-proofs-cases-first.json`.
