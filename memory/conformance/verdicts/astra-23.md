# astra-23 — package implementer verdict

Current package **0.2.1-draft**, `f31d58f`: all canonical semantic vectors pass.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic | 20 | 0 | 0 |
| Supplemental deployment | 0 | 0 | 1 |

Thirteen controls pass. All 20 explicitly migrated supplemental semantic cases
pass on 0.2.1; no implicit conversion or deployment qualification is claimed.
The structural package validator passes 20 intended violation controls.

Current collective rubric score: **1/2**, matching judge commit 6a4f307. All
package corrections and this evaluator's R7-020/023/024 fixes are independently
verified and closed; source-evaluator R7-025/026 await correction review, and
ASTRA25-06 awaits classification. This seat is ready
for 2/2 after those collective gates close. R7-024 retains the red baseline at
bc342e1 and correction f5fdd8b with explicit/unfiltered/historical/hidden controls.

The evaluator remains derived from the released package. Original blind run at
0008dc3 is immutable: no design, companion, notes, inputs, other evaluator, ledger
or divergence topic was read before it. Expected vectors were never edited.

Evidence: ../impl-astra-23/RESULTS.md and JSON; SUPPLEMENTAL.md and JSON;
FIRST-RUN.md/JSON; RELEASE-0.2.1-FIRST.md/JSON; DIVERGENCES.md; WORKLOG.md;
test_controls.py and test_semantics.py.
