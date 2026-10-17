# astra-22 vector results

Package: **0.1.0-draft**, package commit `0ef608ae279a9bc209ad78ffdc72dbbbdc828f8f`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `b3c7ac93d30e9149a252295b0905a63a85a00125`. Source core SHA-256: `eb5bd2b8df171c98f5294ed54f01dcf9e3157bfa4e6253b3824f10167fbc4da6`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 3 | 0 | 11 |
| deployment | 0 | 0 | 0 |

Five bounded harness controls passed (valid comparison, changed value, extra field,
handle reuse, forbidden predicate). Only declared handle paths are normalized;
handle length, equality, distinctness and paired-output invariants are checked.
No randomness-distribution or timing proof is claimed.

| Vector | Category | Result | Evidence / reason |
| --- | --- | --- | --- |
| ASTRA24-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-01 | semantic | unsupported | Frozen core has no exact proof-path enumeration or changes output |
| ASTRA24-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-01 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| ASTRA25-03-CONTROL | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA25-03-FENCE | semantic | unsupported | Unmapped frozen-core transaction operations: admit, erase |
| ASTRA25-03 | semantic | unsupported | Unmapped frozen-core transaction operations: erase |
| ASTRA26-01 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| ASTRA26-04 | semantic | unsupported | Frozen core has no cross-assertion incompatible_with computation |
| ASTRA26-02-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA26-02 | semantic | unsupported | Frozen core has no imported-publication currentness state |
| ASTRA26-05 | semantic | unsupported | Unmapped frozen-core transaction operations: admit |
| ASTRA26-03-CONTROL | semantic | unsupported | Frozen core has no full audience item redaction/alias output |
| ASTRA26-03 | semantic | unsupported | Frozen core has no full audience item redaction/alias output |

Full normalized actual reports and input hashes: `case-corrected.json`.
