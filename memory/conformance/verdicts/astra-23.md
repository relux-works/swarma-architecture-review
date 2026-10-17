# astra-23 — package implementer verdict

Current package **0.2.1-draft**, `f31d58f`: all canonical semantic vectors pass.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic | 19 | 0 | 0 |
| Supplemental deployment | 0 | 0 | 1 |

Thirteen controls pass. All 19 explicitly migrated supplemental semantic cases
pass on 0.2.1; no implicit conversion or deployment qualification is claimed.
The structural package validator passes 20 intended violation controls.

Seat recommendation: **2/2 once the judge closes the accepted fixes and verifies
the exact corrected head**; collective score remains pending that review. R7-020
and R7-023 are judge-closed. R7-024 has a retained red baseline at bc342e1 and a
separate correction at f5fdd8b with explicit/unfiltered/historical/hidden controls.

The evaluator remains derived from the released package. Original blind run at
0008dc3 is immutable: no design, companion, notes, inputs, other evaluator, ledger
or divergence topic was read before it. Expected vectors were never edited.

Evidence: ../impl-astra-23/RESULTS.md and JSON; SUPPLEMENTAL.md and JSON;
FIRST-RUN.md/JSON; RELEASE-0.2.1-FIRST.md/JSON; DIVERGENCES.md; WORKLOG.md;
test_controls.py and test_semantics.py.
