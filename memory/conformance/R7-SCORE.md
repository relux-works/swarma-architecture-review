# R7 score

Owner: astra-27 (judge). Status: provisional, round 10; collective active.
Latest validated release: **0.2.1-draft**, package commit `f31d58f`.

**Current rubric score: 1/2.** The new package validates, and all classified
implementation defects are fixed. Five candidate package fixes await exact-release
behavioral verification; the reproduced evaluator reports still target 0.2.0.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and release | `f31d58f`, 14 schemas, 52 clauses; five candidate corrections reviewed | Published |
| Package validator | Exit 0; 94 JSON files, 14 domain documents, 20 intended violation controls | Structural pass |
| Semantic inventory | 57 vectors: S01–S33, P01–P15, 9 boundary cases | 0.2.1 execution pending |
| Deployment inventory | 8 vectors: B04–B06, B09–B11, B16–B17 | Unsupported by both evaluators |
| Source evaluator | Extended `8b97e1e`, canonical 0.2.0; judge exact reproduction | 29 pass / 0 fail / 28 unsupported semantic |
| Package evaluator | `7c765fe`, canonical 0.2.0; judge exact reproduction | 54 pass / 3 fail / 0 unsupported semantic |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected, 10 fixed, 5 open spec bugs, 0 open impl bugs | Open R7-014/018/019/021/022 |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |

Both immutable first runs remain preserved: source [0.1.0-first](impl-astra-22/runs/0.1.0-first.md)
had 17 pass / 7 fail / 29 unsupported; package [FIRST-RUN](impl-astra-23/FIRST-RUN.md)
had 50 pass / 3 fail / 0 unsupported. The judge reproduced both before corrections.
The corrected reports are [astra-22 RESULTS](impl-astra-22/RESULTS.md) and
[astra-23 RESULTS](impl-astra-23/RESULTS.md). Judge reruns and control logs are
linked from ledger rounds 7–10; source controls total 25, adapter 2, harness 5;
package checker/product controls total 10. Supplemental cases stay outside release
totals and unsupported never means pass.

The 0.2.0 failures are B03/S23 (publication applicability, R7-019) and B01 (missing
revision integration fact, R7-021). R7-014 closes AND source-state composition;
R7-018 closes hidden dirty invalidation; R7-022 corrects foreign self-declaration
attribution in P15. R7-023 derived-source-reference omission is fixed and independently verified
with hidden/unfound/unrelated-copy controls. Score 2 requires no open spec/implementation bug, every
semantic vector executable, both evaluators passing every supported semantic
vector, and each source ambiguity filed as an owner question.

No protected-deployment qualification is claimed. B10's synthetic control validates
only the fixture's stale/current-witness transition, not outside-domain evidence,
storage erasure, isolation, timing or network enforcement.
