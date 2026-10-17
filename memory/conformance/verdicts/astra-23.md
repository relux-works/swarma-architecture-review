# astra-23 — package implementer verdict

First independent implementation and complete vector report are committed from
`memory/spec/` version `0.1.0-draft` at `0ef608a`. No source design, companion,
notes, inputs, other evaluator, ledger or divergence topic was read before this
report. Only the mission, specification package and administrative rounds were read.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Semantic | 50 | 3 | 0 |
| Deployment | 0 | 0 | 8 |

Provisional R7 score: **1/2**. Three semantic disagreements require judge
classification; no complete conformance or deployment qualification is claimed.
The structural package checker and four independent comparison controls pass.

Evidence: `../impl-astra-23/FIRST-RUN.md`, `FIRST-RUN.json`, `WORKLOG.md`.
The evaluator computes from initial state, operations and query only; the runner
checks exact output, forbidden predicates, handle constraints and closed schemas.
