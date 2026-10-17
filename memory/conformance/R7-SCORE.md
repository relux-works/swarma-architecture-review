# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 31; no PARK.
Current verified release: **0.2.5-draft**, `6a04e8c`.

**Current phase-2 score: 1/2.** Exact dual canonical passes: **57/57**.
Both evaluators also pass all 61 supplemental semantic vectors. The separate
native source recovery bug R7-056 remains open, so green vector totals do not
satisfy the no-open-bug requirement. The original 2/2 at `b1ae299` is historical
and used the narrower supported rubric.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `6a04e8c`, 14 schemas, 52 clauses | All established specification findings fixed |
| Package validator | 94 JSON files, 14 domains, 34 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Every vector executable by both readers |
| Dual exact passes | Source `dbf4892`, package `23b4d74`, release 0.2.5 | **57/57** |
| Source evaluator | Independent full run and committed-report comparison | 57 pass / 0 fail / 0 unsupported semantic |
| Package evaluator | Independent full corrected run and committed-report comparison | 57 pass / 0 fail / 0 unsupported semantic |
| Supplemental semantic corpus | All author fixtures explicitly at 0.2.5 | **61/61 exact in both readers** |
| Retention deadline | Seven exact vectors and ten independent operation checks per corrected reader | R7-052 and R7-053 fixed; atomic refusal/replay |
| Source controls | Full current suite including comparer controls | 124 pass; 1 native recovery failure (R7-056) |
| Package controls | Full current product/comparer suite | 31 pass |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 44 fixed | R7-056 implementation open; R7-055 owner-question |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | R7-055: cross-issuer predecessor-path scope |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

R7-056 preserves a validated native counterexample outside the canonical corpus:
an authorized available transition acknowledges success but an initially degraded
public memory stays unavailable. Three neighboring transitions and two atomic
authorization refusals pass. Existing full-vector success does not waive this bug.

R7-055 concerns whether an H1 canonical predecessor edge endorses transitive H2
ordering. The validated native pair separates the readers; the same-H1 control
agrees. It stays outside vector denominators pending an attributed owner decision.
The convener holds it for Ivan; no evaluator is marked wrong on that boundary.

All 62 supplemental artifacts validate at 0.2.5. Seat-24's final twenty migrations
at `27303e4` change only view-profile stamps, with exact reverse byte recovery.
Independent runs reproduce all committed rows and input/module hashes. Original
first failures remain immutable.

Full 57/57 dual coverage plus one full round without a new open item is required
for early PARK under convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`.
The 13:00Z hard cap remains. Continue until the convener posts PARK. Synthetic
erasure, restore, release or delivery never qualifies a real deployment.
