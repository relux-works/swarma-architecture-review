# R7 score

Owner: astra-27 (judge). Status: provisional, round 4; collective active.
Inspected package: **0.1.0-draft**, commit `0ef608a`.

**Current rubric score: 1/2.** The package exists and validates, but kernel v0.2
updates remain open and neither independent full vector report is committed yet.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and released draft | `0ef608a`, 14 schemas, 49 normative clauses | Present; v0.1 source baseline |
| Package validator | Exit 0; 90 JSON files, 14 domain documents, 13 intended violation controls | Structural pass |
| Semantic inventory | 53 vectors: S01–S33, P01–P11, 9 boundary cases | Execution not yet verified; P12–P15 pending |
| Deployment inventory | 8 vectors: B04–B06, B09–B11, B16–B17 | No real deployment execution |
| Source evaluator | Core frozen at `4d4ef45` before package intake; 20 source controls reported | First package run pending |
| Package evaluator | First package-only implementation starting | First full run pending |
| Ledger | [LEDGER.md](LEDGER.md): 6 rejected defect allegations, 3 open spec bugs | Open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md): none established | No source-level decision needed yet |

Validator command: `python3 -B memory/spec/checks/validate.py`. Judge log:
seat work directory `.temp/package-validate-01.log`. This check does not evaluate
evidence semantics. No evaluator pass/fail/unsupported totals are available yet.

No protected-deployment qualification is claimed. A synthetic pass cannot prove
OS isolation, custody-sink deletion, restore completeness, timing, or network
policy enforcement. Score 2 requires no open spec/implementation bug, every
semantic vector executable, both evaluators passing each semantic vector they
support, and every source ambiguity filed. Unsupported scope remains explicit.
