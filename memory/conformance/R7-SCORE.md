# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 18; no PARK.
Current release: **0.2.2-draft**, `7e71765`. Structure and regeneration verified;
erasure behavioral alignment remains open. Last fully accepted release: 0.2.1.

**Current phase-2 score: 1/2.** Verified dual canonical coverage is **45/57**.
Full 57/57 coverage plus one full round without a new open item is required for
early PARK. Two specification bugs and four implementation bugs remain open.
The original supported-vector score 2/2 at `b1ae299` is historical and narrower.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package and release | `7e71765`, 14 schemas, 52 clauses | R7-031 exact-release behavior pending; R7-039 scope missing |
| Package validator | 94 JSON files, 14 domain documents, 23 intended violation controls; exact regeneration | Pass |
| Semantic inventory | 57 canonical vectors | Every vector executable |
| Dual implementation coverage | Source `1f35727`, package runtime `f10c7ba`, package 0.2.2 | **45/57; 12 source-unsupported** |
| Source evaluator | Exact independent canonical reproduction | 45 pass / 0 fail / 12 unsupported semantic |
| Package evaluator | Independent unchanged-runtime 0.2.2 baseline | 56 pass / 1 fail / 0 unsupported semantic; P08 intended red witness |
| Migrated supplemental subset | 20 semantic fixtures validate against 0.2.2 | Source 17/1/2; package 19/1/0 (pass/fail/unsupported) |
| Pending supplemental migration | 14 semantic plus 1 deployment fixture | Old grammar/profile; excluded from current compatible subset |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 25 fixed | R7-031/039 spec; R7-036/037/040/041 impl open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical, plus prior supplemental case | Unsupported; no deployment qualification |

S23 now passes both implementations. R7-032 import-horizon correction is closed;
new ambiguous-authority CAS failures are independently tracked. Source controls:
33 source, 8 adapter, 11 transaction, 4 proof and 5 harness (61 passing, unchanged
groups reused). The prior package baseline has 16 passing controls; they do not
establish the new erasure behavior. Immutable first failures and corrections
remain linked from the ledger. Supplemental migration is explicit and incomplete;
raw mixed-version failures are not counted as new semantic defects or passes.

Remaining canonical source gaps: B01, B07, P05, P06, P08, P12, S17, S20, S24,
S25, S26 and S27. Source/package coverage is distinct from agreement on newly
filed adversarial cases. Unsupported inputs never count as passes. Synthetic
erasure, restore, release or delivery does not qualify a real protected deployment.
Phase 2 follows convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`;
13:00Z hard cap remains. Continue until the convener posts PARK.
