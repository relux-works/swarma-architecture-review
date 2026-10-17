# R7 score

Owner: astra-27 (judge). Status: provisional, round 7; collective active.
Latest structurally validated package: **0.2.0-draft**, commit `cde5754`.
Both first independent reports below target **0.1.0-draft**, commit `0ef608a`.

**Current rubric score: 1/2.** The package exists and validates, but kernel v0.2
updates and implementation defects remain open. Both independent first-run
reports are committed and reproduced; neither is an execution of the new release.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and released draft | `cde5754`, 14 schemas, 52 normative clauses | v0.2 candidate fixes under review |
| Package validator | Exit 0; 94 JSON files, 14 domain documents, 16 intended violation controls | Structural pass |
| Semantic inventory | 57 vectors: S01–S33, P01–P15, 9 boundary cases | New-release execution pending |
| Deployment inventory | 8 vectors: B04–B06, B09–B11, B16–B17 | No real deployment execution |
| Source evaluator | First report `0216fbb`, unchanged frozen core `4d4ef45`; judge reproduced all outputs | 17 pass / 7 fail / 29 unsupported semantic; 8 unsupported deployment |
| Package evaluator | First report `0008dc3`, blind package-only boundary committed; judge reproduced all outputs | 50 pass / 3 fail / 0 unsupported semantic; 8 unsupported deployment |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected defect allegations, 7 open spec bugs, 5 open impl bugs | Four package fixes await verification |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md): none established | No source-level decision needed yet |

Validator command: `python3 -B memory/spec/checks/validate.py`. Judge log:
seat work directory `.temp/package-validate-02.log`. This check does not evaluate
evidence semantics. The judge's separate source-evaluator rerun at `bbc1b50`
exactly reproduces [the first report](impl-astra-22/runs/0.1.0-first.md), including
its five passing harness controls and all failed fields. The separate package-only
rerun reproduces [its first report](impl-astra-23/FIRST-RUN.md). Cross-release
claims remain deferred until both have consumed the same new package.

A supplemental adversarial case run (`b3c7ac9`, independently reproduced by the
judge) adds an AND-path source-state defect. It is tracked separately from the
53-vector release totals; no proposed case is counted as a canonical pass.

No protected-deployment qualification is claimed. A synthetic pass cannot prove
OS isolation, custody-sink deletion, restore completeness, timing, or network
policy enforcement. Score 2 requires no open spec/implementation bug, every
semantic vector executable, both evaluators passing each semantic vector they
support, and every source ambiguity filed. Unsupported scope remains explicit.
