# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 34; awaiting PARK.
Current verified release: **0.2.5-draft**, `6a04e8c`.

**Current R7 score: 2/2.** Both evaluators pass **57/57 canonical** and
**63/63 supplemental semantic vectors**. No specification or implementation bug
remains open. R7-055 is a filed, unresolved owner question; its native pair has no
chosen oracle and is excluded from executable denominators.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `6a04e8c`, 14 schemas, 52 clauses | All established specification findings fixed |
| Package validator | 94 JSON files, 14 domains, 34 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Both readers execute and exactly pass all 57 |
| Source evaluator | `946cbd8`; independent full run and committed-report comparison | 57 canonical + 63 supplemental pass |
| Package evaluator | `23b4d74`; unchanged runtime; supplemental report `348ea38` | 57 canonical + 63 supplemental pass |
| Supplemental grammar | 64 explicitly versioned artifacts, including one deployment case | All validate at 0.2.5 |
| Source controls | 123 native tests plus five comparer controls | 128 pass |
| Package controls | Full product/comparer suite on unchanged runtime | 31 pass |
| Ledger | [LEDGER.md](LEDGER.md): 46 fixed, 10 rejected, one owner question | No open spec-bug or impl-bug |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | R7-055: cross-issuer predecessor-path scope |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

The last correction, R7-057 at `946cbd8`, separates changed erase intent from
exact receipt replay. Current erase authority still comes first; changed intent
conflicts, while an identical replay rechecks current metadata permission.
The original native witness, both exact typed regressions and neighboring
revocation/fresh-key/immutable-receipt controls pass with state preserved.
First failures and original input bytes remain immutable.

R7-055 asks whether an H1 canonical predecessor edge endorses transitive H2
ordering. Both source readings and the exact separating input remain recorded.
The convener holds it for Ivan; no implementation is marked wrong on that boundary
and no authority option has been applied. Filing this ambiguity satisfies the
rubric's owner-question requirement; it does not resolve the architecture choice.

Full dual coverage plus one full round without a new open item is the early PARK
condition under convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`.
The 13:00Z hard cap remains. Continue until the convener posts PARK. Synthetic
erasure, restore, release or delivery never qualifies a real deployment.
