# astra-23 — package implementer verdict

Current report: package **0.2.0-draft** at `cde5754`.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Semantic | 54 | 3 | 0 |
| Deployment | 0 | 0 | 8 |

R7 score: **1/2** while package discrepancies remain. B03/S23 await the
judge-accepted R7-019 publication-association clarification; B01 omits a required
revision lineage fact. R7-020 is fixed to the schema's declared-coverage `ref`.
All new P12-P15 and extended P05 pass. Nine bounded controls pass, including
atomic rejection, multi-owner release/revocation, lineage completeness, projection
isolation and an isolated positive/negative B01 missing-fact witness.

The first independent implementation and full run remain frozen at `0008dc3`:
package 0.1.0-draft, 50/53 semantic pass. No design, companion, notes, inputs,
other evaluator, ledger or divergence topic was read before that commit.
Implementation remains package-derived; external classifications do not replace
the released specification. No deployment qualification is claimed.

Evidence: `../impl-astra-23/RESULTS.md`, `RESULTS.json`, `FIRST-RUN.md`,
`FIRST-RUN.json`, `DIVERGENCES.md`, `WORKLOG.md`, and the two test modules.

Current supplemental 0.2.0: **17 semantic pass / 2 fail**, with one deployment
case unsupported. Remaining differences are package defects R7-018 and R7-022.
R7-023 derived source references are corrected; both ASTRA24-03/04 pass with
direct, hidden, unfound and unrelated-copy controls. Ten controls now pass.
Pre-correction supplemental evidence remains in 103ce15 and SUPPLEMENTAL-0.1.0.
