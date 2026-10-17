# astra-23 — package implementer verdict

Current adapted pre-fix report: package **0.2.1-draft**, `f31d58f`.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Semantic | 55 | 2 | 0 |
| Deployment | 0 | 0 | 8 |

R7 score: **1/2** until R7-024 is corrected. B07/S24 private captures include
an unrelated multi-sequence historical ref; all other canonical outputs agree.
The judge classified this as an evaluator omission, with unchanged expectations.
Twelve controls pass; its exact regression is intentionally red at this checkpoint.
The structural package validator passes all 20 intended violation controls.

R7-020 and R7-023 are judge-closed. Currentness, integration lineage, joint
release/revocation, frozen delivery, projection exclusion, scoped dirty causes
and explicit self-declaration identity evidence are implemented from the package.
First-run independence remains preserved at 0008dc3; no design, companion, notes,
inputs, other evaluator, ledger or divergence topic was read before that commit.
No deployment qualification is claimed.

Evidence: ../impl-astra-23/RELEASE-0.2.1-FIRST.md and JSON, FIRST-RUN.md and JSON,
DIVERGENCES.md, WORKLOG.md, the test modules and versioned supplemental reports.
