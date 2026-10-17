# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 33; no PARK.
Current verified release: **0.2.5-draft**, `6a04e8c`.

**Current phase-2 score: 1/2.** Exact dual canonical passes: **57/57**.
The supplemental corpus now has 63 semantic vectors: source passes 61 and fails
the two new R7-057 erase-context regressions; package passes all 63. R7-057
remains open. The original 2/2 at `b1ae299` is historical
and used the narrower supported rubric.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `6a04e8c`, 14 schemas, 52 clauses | All established specification findings fixed |
| Package validator | 94 JSON files, 14 domains, 34 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Every vector executable by both readers |
| Dual exact passes | Source `87beb46`, package `23b4d74`, release 0.2.5 | **57/57** |
| Source evaluator | Independent full run and committed-report comparison | 57 pass / 0 fail / 0 unsupported semantic |
| Package evaluator | Independent full corrected run and committed-report comparison | 57 pass / 0 fail / 0 unsupported semantic |
| Supplemental semantic corpus | All author fixtures explicitly at 0.2.5 | Source 61/2/0; package 63/0/0 |
| Retention deadline | Seven exact vectors and ten independent operation checks per corrected reader | R7-052 and R7-053 fixed; atomic refusal/replay |
| Source controls | Full current suite including comparer controls | 125 pass; R7-057 now has two exact supplemental failures |
| Package controls | Full current product/comparer suite | 31 pass |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 45 fixed | R7-057 implementation open; R7-055 owner-question |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | R7-055: cross-issuer predecessor-path scope |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

R7-056 recovery is fixed at `87beb46`: the original witness, four public-state
transitions and two atomic authorization negatives now pass. R7-057 preserves a
separate validated native counterexample: changed receipt purpose/audience under
an existing erase key returns the wrong refusal. Current erase authority, exact
replay metadata permission and fresh-key empty-ref success remain distinct. No
canonical vector is edited to obtain the already passing totals.

R7-055 concerns whether an H1 canonical predecessor edge endorses transitive H2
ordering. The validated native pair separates the readers; the same-H1 control
agrees. It stays outside vector denominators pending an attributed owner decision.
The convener holds it for Ivan; no evaluator is marked wrong on that boundary.

All 64 supplemental artifacts validate at 0.2.5. Seat-24's final twenty migrations
at `27303e4` change only view-profile stamps, with exact reverse byte recovery.
The two new fixtures at `66233ab` preserve the original native state and fail
only on the source refusal code. All older case inputs and results stay unchanged;
original first failures remain immutable.

Full 57/57 dual coverage plus one full round without a new open item is required
for early PARK under convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`.
The 13:00Z hard cap remains. Continue until the convener posts PARK. Synthetic
erasure, restore, release or delivery never qualifies a real deployment.
