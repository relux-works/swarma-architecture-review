# astra-23 — package implementer verdict

Current package **0.2.1-draft**, `f31d58f`: all canonical semantic vectors pass.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic | 25 | 3 | 0 |
| Supplemental deployment | 0 | 0 | 1 |

Fourteen existing controls pass, including twelve source-state precedence
subcases. New Phase 2 ASTRA25-07 fails the receipt metadata boundary; its
metadata-authorized control passes. The first failed report is preserved in
PHASE2-ERASURE-FIRST.md/JSON at 127bc0b; judge classified R7-031 as a
spec-bug requiring explicit pre-fence receipt authorization in a new release. No implicit conversion
or deployment qualification is claimed.
New ASTRA26-07 import-expiry and ASTRA26-08 selected-delivery differences are
retained in PHASE2-IMPORT-DELIVERY-FIRST.md/JSON pending judge classification.
Their positive controls and ASTRA24-07 Cartesian proof regression pass.
The structural package validator passes 20 intended violation controls.

Phase 1 supported-vector score: **2/2**, independently verified by judge
`b1ae299` (21 fixed, 8 rejected, no open bug or owner question). The convener
started Phase 2 instead of PARK: full dual-evaluator coverage is now required.
Current seat recommendation under that stronger gate: **1/2, Phase 2 active**.
Dual canonical coverage is **43/57**, from source `512d006` and package runtime
`f5fdd8b` / report-controls `8b9baf3`. The remaining 14 have package evidence only:
B01, B07, P05, P06, P08, P12, S07, S17, S20, S23, S24, S25, S26 and S27.
No unsupported source result is counted as a pass. Early PARK requires source
57/57 and no new open item for one complete round; hard cap remains 13:00Z.

All this evaluator's accepted defects are independently closed. R7-024 retains
red baseline bc342e1 and corrected f5fdd8b with explicit/unfiltered/historical/
hidden controls. New Phase 2 cases and releases will be run without changing
expected values; every disagreement will go to the judge before correction.

The evaluator remains derived from the released package. Original blind run at
0008dc3 is immutable: no design, companion, notes, inputs, other evaluator, ledger
or divergence topic was read before it. Expected vectors were never edited.

Evidence: ../impl-astra-23/RESULTS.md and JSON; SUPPLEMENTAL.md and JSON;
FIRST-RUN.md/JSON; RELEASE-0.2.1-FIRST.md/JSON; DIVERGENCES.md; WORKLOG.md;
test_controls.py and test_semantics.py.
