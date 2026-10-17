# R7 verdict — astra-22

Status: first full package inventory run complete; three divergence groups await judge classification.

Built `impl-astra-22/evaluator.py` from kernel v0.2, the companion and design only.
The core SHA-256 is
`cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Twenty source-derived controls pass, including explicit forbidden outcomes and
post-refusal state checks (`.temp/astra-22/source-checks-02.log`). Normalization
choices and unsupported deployment guarantees are in the evaluator README.

Package 0.1.0-draft at `0ef608a`: semantic 17 pass / 7 fail / 29 unsupported;
deployment 0 pass / 0 fail / 8 unsupported. Exact evidence is in
`impl-astra-22/runs/0.1.0-first.md` and `.json`; ASTRA22-01..03 in DIVERGENCES.md
group every observed disagreement. The frozen core remains byte-identical.

R7 score: **1/2**. Published grammar and vectors exist, but evaluator disagreements
and unsupported semantic coverage remain. No full semantic conformance or
protected deployment qualification is claimed. The first report is preserved;
corrections require the judge's classification, never a silent expected-value fix.
