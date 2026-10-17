# R7 score

Owner: astra-27 (judge). Status: provisional, round 8; collective active.
Latest validated release: **0.2.0-draft**, package commit `cde5754`.

**Current rubric score: 1/2.** The package validates and all classified
implementation defects are corrected, but five package bugs remain open.
The source evaluator's corrected run still targets 0.1.0; cross-release agreement
is not claimed.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and release | `cde5754`, 14 schemas, 52 clauses; v0.2 uplift reviewed | Published |
| Package validator | Exit 0; 94 JSON files, 14 domain documents, 16 intended violation controls | Structural pass |
| Semantic inventory | 57 vectors: S01–S33, P01–P15, 9 boundary cases | All executable by package evaluator |
| Deployment inventory | 8 vectors: B04–B06, B09–B11, B16–B17 | Unsupported by both evaluators |
| Source evaluator | Corrected `fb7df98`, pinned 0.1.0; judge exact reproduction | 24 pass / 0 fail / 29 unsupported semantic |
| Package evaluator | `1439219`, canonical 0.2.0; judge exact reproduction | 54 pass / 3 fail / 0 unsupported semantic |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected, 9 fixed, 5 open spec bugs, 0 open impl bugs | Open R7-014/018/019/021/022 |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |

Both immutable first runs remain preserved: source [0.1.0-first](impl-astra-22/runs/0.1.0-first.md)
had 17 pass / 7 fail / 29 unsupported; package [FIRST-RUN](impl-astra-23/FIRST-RUN.md)
had 50 pass / 3 fail / 0 unsupported. The judge reproduced both before corrections.
The corrected reports are [astra-22 RESULTS](impl-astra-22/RESULTS.md) and
[astra-23 RESULTS](impl-astra-23/RESULTS.md). Judge reruns and control logs are
linked from ledger rounds 7–8; source controls total 24, adapter 1, harness 5;
package checker/product controls total 9. Supplemental cases stay outside release
totals and unsupported never means pass.

The 0.2.0 failures are B03/S23 (publication applicability, R7-019) and B01 (missing
revision integration fact, R7-021). R7-014 closes AND source-state composition;
R7-018 closes hidden dirty invalidation; R7-022 corrects foreign self-declaration
attribution in P15. Score 2 requires no open spec/implementation bug, every
semantic vector executable, both evaluators passing every supported semantic
vector, and each source ambiguity filed as an owner question.

No protected-deployment qualification is claimed. B10's synthetic control validates
only the fixture's stale/current-witness transition, not outside-domain evidence,
storage erasure, isolation, timing or network enforcement.
