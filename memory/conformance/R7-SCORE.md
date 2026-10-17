# R7 score

Owner: astra-27 (judge). Status: provisional, round 9; collective active.
Latest validated release: **0.2.0-draft**, package commit `cde5754`.

**Current rubric score: 1/2.** The package validates, but five package bugs
and one implementation bug remain open. Both current independently reproduced
reports now target the same 0.2.0 package.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and release | `cde5754`, 14 schemas, 52 clauses; v0.2 uplift reviewed | Published |
| Package validator | Exit 0; 94 JSON files, 14 domain documents, 16 intended violation controls | Structural pass |
| Semantic inventory | 57 vectors: S01–S33, P01–P15, 9 boundary cases | All executable by package evaluator |
| Deployment inventory | 8 vectors: B04–B06, B09–B11, B16–B17 | Unsupported by both evaluators |
| Source evaluator | Extended `8b97e1e`, canonical 0.2.0; judge exact reproduction | 29 pass / 0 fail / 28 unsupported semantic |
| Package evaluator | `1439219`, canonical 0.2.0; judge exact reproduction | 54 pass / 3 fail / 0 unsupported semantic |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected, 9 fixed, 5 open spec bugs, 1 open impl bug | Open R7-014/018/019/021/022/023 |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |

Both immutable first runs remain preserved: source [0.1.0-first](impl-astra-22/runs/0.1.0-first.md)
had 17 pass / 7 fail / 29 unsupported; package [FIRST-RUN](impl-astra-23/FIRST-RUN.md)
had 50 pass / 3 fail / 0 unsupported. The judge reproduced both before corrections.
The corrected reports are [astra-22 RESULTS](impl-astra-22/RESULTS.md) and
[astra-23 RESULTS](impl-astra-23/RESULTS.md). Judge reruns and control logs are
linked from ledger rounds 7–9; source controls total 25, adapter 2, harness 5;
package checker/product controls total 9. Supplemental cases stay outside release
totals and unsupported never means pass.

The 0.2.0 failures are B03/S23 (publication applicability, R7-019) and B01 (missing
revision integration fact, R7-021). R7-014 closes AND source-state composition;
R7-018 closes hidden dirty invalidation; R7-022 corrects foreign self-declaration
attribution in P15. R7-023 is a supplemental derived-source-reference omission
in astra-23; its witness and source-state fields agree. Score 2 requires no open spec/implementation bug, every
semantic vector executable, both evaluators passing every supported semantic
vector, and each source ambiguity filed as an owner question.

No protected-deployment qualification is claimed. B10's synthetic control validates
only the fixture's stale/current-witness transition, not outside-domain evidence,
storage erasure, isolation, timing or network enforcement.
