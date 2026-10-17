# astra-22 vector results

Package: **0.2.3-draft**, package commit `23290b3a96a469d5190cb71b0e20139896b89236`.
Vector directory: `memory/conformance/cases` (this inventory only).
Checkout: `64ef86efc3e8e75d5d1f4f0f35f47bbaa7079c4a`. Source core SHA-256: `7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.

The core is source-derived; the original frozen run is preserved under runs/0.1.0-first.*.
Judge-classified corrections are recorded in DIVERGENCES.md; the adapter is an independent wire mapping.
Every vector was loaded. Unsupported is neither a pass nor evidence of a package defect.
Deployment cases require actual boundary qualification and are reported separately.

| Category | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| semantic | 44 | 2 | 8 |
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
| ASTRA24-10-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-10-PRIOR | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-10-SAME | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-10-TRANSITIVE | semantic | fail | 9 exact differences |
| ASTRA24-10 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-07 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-04 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-03 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-05 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-01 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-11-CONTROL | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-11 | semantic | fail | 10 exact differences |
| ASTRA24-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-06 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA24-09 | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-02-DIGEST | semantic | pass | Exact report and forbidden/normalization checks passed. |
| ASTRA25-02 | semantic | pass | Exact report and forbidden/normalization checks passed. |
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

## ASTRA24-10-TRANSITIVE

9 exact differences

- `$.result.currentness`: expected `"current"`; actual `"ambiguous_current"`.
- `$.result.historical.length`: expected `1`; actual `0`.
- `$.result.items.length`: expected `1`; actual `2`.
- `$.result.items[0].authority_receipt.id`: expected `"rec:receipt2"`; actual `"rec:receipt1"`.
- `$.result.items[0].content[0].value`: expected `"delete_home"`; actual `"archive_home"`.
- `$.result.items[0].currentness`: expected `"current"`; actual `"ambiguous_current"`.
- `$.result.items[0].ref.version`: expected `2`; actual `1`.
- `$.result.items[0].source_refs[0].id`: expected `"rec:receipt2"`; actual `"rec:receipt1"`.
- `forbidden:/result/items/0/content/0/value`: expected `"predicate false"`; actual `{"path": "/result/items/0/content/0/value", "test": "equals", "value": "archive_home"}`.

## ASTRA24-11

10 exact differences

- `$.result.currentness`: expected `"current"`; actual `"ambiguous_current"`.
- `$.result.historical.length`: expected `1`; actual `0`.
- `$.result.items.length`: expected `1`; actual `2`.
- `$.result.items[0].authority_receipt.id`: expected `"rec:receipt3"`; actual `"rec:receipt1"`.
- `$.result.items[0].content[0].value`: expected `"retain_home"`; actual `"archive_home"`.
- `$.result.items[0].currentness`: expected `"current"`; actual `"ambiguous_current"`.
- `$.result.items[0].ref.version`: expected `3`; actual `1`.
- `$.result.items[0].source_refs[0].id`: expected `"rec:receipt3"`; actual `"rec:receipt1"`.
- `forbidden:/result/currentness`: expected `"predicate false"`; actual `{"path": "/result/currentness", "test": "equals", "value": "ambiguous_current"}`.
- `forbidden:/result/items`: expected `"predicate false"`; actual `{"path": "/result/items", "test": "size_equals", "value": 2}`.

Full normalized actual reports and input hashes: `phase2-succession-corrected.json`.
