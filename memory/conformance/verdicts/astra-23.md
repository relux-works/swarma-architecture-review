# astra-23 — package implementer verdict

Latest tested package **0.2.2-draft**, `7e71765`: unchanged runtime passes
56/57 canonical semantic vectors; P08 requires the newly released receipt-context
and current-authorized replay behavior. Immutable RELEASE-0.2.2-FIRST.md/JSON
records this baseline before adaptation. Its eight deployment vectors remain
unsupported. Package structural validation passes all 23 violation controls.

The previous **0.2.1-draft**, `f31d58f`, results remain separately labeled:

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic | 28 | 2 | 0 |
| Supplemental deployment | 0 | 0 | 1 |

Sixteen checker/product controls pass. R7-033 import-expiry and R7-034
selected-delivery corrections pass their exact witnesses and neighboring
positive/negative controls, independently closed by the judge at f10c7ba. Their immutable
pre-fix report remains PHASE2-IMPORT-DELIVERY-FIRST at f83268d. ASTRA24-07
Cartesian proof sets/truncation and separately deduplicated origins pass.

Two supplemental failures remain: R7-031 erasure receipt metadata (spec-bug,
0.2.2 adaptation in progress; first report at 127bc0b) and
ASTRA25-08 unauthorized derivative retention (R7-037 impl-bug; first evidence
PHASE2-RETENTION-FIRST.md/JSON). The complete scoped correction requires an
explicit retention-scope binding: current closed write context has no audience/
purpose. The exact gap and separating grant neighbor are recorded in DIVERGENCES.md. Both authorized positive controls pass.
The prior 0.2.1 package validator evidence remains 20 intended violation controls;
no implicit fixture migration or deployment qualification is claimed.

Phase 1 supported-vector score: **2/2**, independently verified by judge
`b1ae299` (21 fixed, 8 rejected, no open bug or owner question). The convener
started Phase 2 instead of PARK: full dual-evaluator coverage is now required.
Current seat recommendation under that stronger gate: **1/2, Phase 2 active**.
Last judge-verified dual canonical baseline is **43/57**, from source `512d006` and package runtime
`f5fdd8b` / report-controls `8b9baf3`. The remaining 14 have package evidence only:
B01, B07, P05, P06, P08, P12, S07, S17, S20, S23, S24, S25, S26 and S27.
No unsupported source result is counted as a pass. Early PARK requires source
57/57 and no new open item for one complete round; hard cap remains 13:00Z.

All Phase 1 defects and R7-033/034 are independently closed. Source seat reports
45/57 coverage at 1f35727, pending expanded-head judge verification. R7-024 retains
red baseline bc342e1 and corrected f5fdd8b with explicit/unfiltered/historical/
hidden controls. New Phase 2 cases and releases will be run without changing
expected values; every disagreement will go to the judge before correction.

The evaluator remains derived from the released package. Original blind run at
0008dc3 is immutable: no design, companion, notes, inputs, other evaluator, ledger
or divergence topic was read before it. Expected vectors were never edited.

Evidence: ../impl-astra-23/RESULTS.md and JSON; SUPPLEMENTAL.md and JSON;
FIRST-RUN.md/JSON; RELEASE-0.2.1-FIRST.md/JSON; RELEASE-0.2.2-FIRST.md/JSON; DIVERGENCES.md; WORKLOG.md;
test_controls.py and test_semantics.py.
