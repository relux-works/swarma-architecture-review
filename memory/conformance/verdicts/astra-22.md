# R7 verdict — astra-22

Status: source-only core frozen; waiting for PACKAGE LANDED before vector intake.

Built `impl-astra-22/evaluator.py` from kernel v0.2, the companion and design only.
The core SHA-256 is
`cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Twenty source-derived controls pass, including explicit forbidden outcomes and
post-refusal state checks (`.temp/astra-22/source-checks-02.log`). Normalization
choices and unsupported deployment guarantees are in the evaluator README.

R7 score: provisional 0/2 while the package is absent from the announced release
boundary. No package semantic or deployment conformance is claimed. A passing
local model cannot qualify a protected deployment. Every package disagreement
will be reported to the judge, with the original core retained as evidence.
