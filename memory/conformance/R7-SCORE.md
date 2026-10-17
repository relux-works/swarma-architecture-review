# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 22; no PARK.
Current verified release: **0.2.3-draft**, `23290b3`.

**Current phase-2 score: 1/2.** Current exact dual canonical passes: **49/57**.
Retention and actor-binding corrections are verified. A new authority-succession
probe exposes forbidden writes in both evaluators and a missing exact refusal
mapping. Full 57/57 dual coverage plus one full round without a new open item is
required for early PARK. The original score 2/2 at `b1ae299` is historical and
used the narrower supported-vector rubric.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `23290b3`, 14 schemas, 52 clauses | R7-049 successor-refusal mapping remains open |
| Package validator | 94 JSON files, 14 domains, 32 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Every vector executable |
| Current dual exact passes | Source `d077064`, package `4af0360`, package 0.2.3 | **49/57; 8 source-unsupported** |
| Source evaluator | Exact independent full canonical report | 49 pass / 0 fail / 8 unsupported semantic |
| Package evaluator | Exact independent full canonical report | 57 pass / 0 fail / 0 unsupported semantic |
| Current supplemental corpus | 46 semantic vectors, author-migrated 0.2.3 | Source 37/0/9; package 46/0/0 |
| Additional native probes | ASTRA24-10, three validated input triples | Ordered positive passes; two forbidden succession writes in both runtimes |
| Runtime and harness controls | All groups rerun at verified heads | Source 89; package 26 pass |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 36 fixed | R7-047/048 impl and R7-049 spec open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

R7-036/037 retention and R7-046 actor binding close on exact behavioral and
state-preservation evidence. Current receipts recheck scoped retain authority;
all four package write APIs have atomic denial and same-key recovery controls.
Original actor fixtures also pass against the frozen 0.2.2 correction commit.
Every supplemental vector validates. The native succession probes remain outside
the exact-vector denominator until their typed mapping is published; their
observed forbidden writes still keep the score at 1/2.

Remaining canonical source gaps: B07, P05, P08, S20, S24, S25, S26 and S27.
First failures, exact pins, input hashes and setup errors remain preserved in the
ledger. Unsupported inputs never count as passes. Synthetic erasure, restore,
release or delivery does not qualify a real deployment. Phase 2 follows convener
event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; the 13:00Z hard cap
remains. Continue until the convener posts PARK.
