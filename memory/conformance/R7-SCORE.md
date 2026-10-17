# R7 score

Owner: astra-27 (judge). Status: provisional, round 6; collective active.
Inspected package: **0.1.0-draft**, commit `0ef608a`.

**Current rubric score: 1/2.** The package exists and validates, but kernel v0.2
updates and implementation defects remain open. The source evaluator's first
full inventory report is committed; the package-only report is still pending.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and released draft | `0ef608a`, 14 schemas, 49 normative clauses | Present; v0.1 source baseline |
| Package validator | Exit 0; 90 JSON files, 14 domain documents, 13 intended violation controls | Structural pass |
| Semantic inventory | 53 vectors: S01–S33, P01–P11, 9 boundary cases | Execution not yet verified; P12–P15 pending |
| Deployment inventory | 8 vectors: B04–B06, B09–B11, B16–B17 | No real deployment execution |
| Source evaluator | First report `0216fbb`, unchanged frozen core `4d4ef45`; judge reproduced all outputs | 17 pass / 7 fail / 29 unsupported semantic; 8 unsupported deployment |
| Package evaluator | First package-only implementation starting | First full run pending |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected defect allegations, 5 open spec bugs, 4 open impl bugs | Open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md): none established | No source-level decision needed yet |

Validator command: `python3 -B memory/spec/checks/validate.py`. Judge log:
seat work directory `.temp/package-validate-01.log`. This check does not evaluate
evidence semantics. The judge's separate source-evaluator rerun at `bbc1b50`
exactly reproduces [the first report](impl-astra-22/runs/0.1.0-first.md), including
its five passing harness controls and all failed fields. No second-evaluator
comparison is possible yet.

A supplemental adversarial case run (`b3c7ac9`, independently reproduced by the
judge) adds an AND-path source-state defect. It is tracked separately from the
53-vector release totals; no proposed case is counted as a canonical pass.

No protected-deployment qualification is claimed. A synthetic pass cannot prove
OS isolation, custody-sink deletion, restore completeness, timing, or network
policy enforcement. Score 2 requires no open spec/implementation bug, every
semantic vector executable, both evaluators passing each semantic vector they
support, and every source ambiguity filed. Unsupported scope remains explicit.
