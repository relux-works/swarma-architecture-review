# MCP servers as skill dependencies: synthesis of the parked collective

> Provenance: this synthesis was drafted by an in-session subagent of the convener and then checked by the convener against the verdict files before commit 9e534c0. Recorded under swarm rule R91 B.

Scope: everything under `mcp-deps/` as of the integration commit `f3a04ce`: the mission, the base design, seven findings, fourteen verdicts and eleven parked records. Seats by five: five 1 = astra-01..03, wonder-01..02; five 2 = astra-04..06, wonder-03 (wonder-04 left no verdict); five 3, the cross-host mini pass = astra-11..13, wonder-11..12. Every seat read the same source pins: curator-spec `a9c03be`, curator `5234cf3`. All scores are design scores. Nobody ran a build, test, client or auth probe.

## 1. Verdict

The base design as written is **beaten**, not elegant. Its consensus is 7/16 under the amended E3 row (range 5–10 across 14 seats) and 6/16 under the original row. Its "one optional field" claim and its "never reads a credential" claim are both refuted (`findings/f-schema-budget.md`, `findings/f-secret-boundary.md`). Repaired while keeping authoritative `server` identity, the base reaches only 10/16 (range 10–12).

The winning design is **N**: unchanged named skill requirements (`dependencies.mcp_servers` keeps its v5 bytes), plus one protected, operator-local binding and evidence contract whose results are scoped to the selected launch. N scores **13/16 amended and 11/16 original** (consensus `[1,1,2,2,2,2,1,2]`). It ties with **N+A**, which adds an inert, skill-shipped `agent-mcp.json` (schema 1) as a recommendation only. Every seat's final preference is N or N+A; wonder-12 reached that position after first preferring a repaired base (§3).

Structurally, the base is close to the winner. N keeps its Require/Provide/Bind separation, client-owned authentication, the no-health-check rule and consent before writes. N is reached mostly by **deleting** parts of the base: `server`, the identity conjunct, the auth class and project-homed aliases.

Two caveats limit the result:
- "Elegant" holds only at sketch fidelity. E7 is 1 on every seat until governed text and conformance vectors exist.
- No native-inspecting design passes the original literal E3 gate, so the proof stands on the convener's amended E3 row.

## 2. Score table

Values are the median of each seat's **final** row; ranges across seats are shown in parentheses where seats differ. E3 is the amended row. "Orig" is the total under the original E3 row.

| Design | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | Total amended | Total orig | Seats scoring it |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Base as written | 1 (0–1) | 1 | 1 | 1 (0–2) | 1 (1–2) | 1 | 0 (0–1) | 1 (1–2) | **7 (5–10)** | 6 (4–9) | all 14 |
| Repaired base, authoritative identity kept (B1/R/B+/I/BASE′) | 0 (0–1) | 1 | 2 | 2 (1–2) | 1 (1–2) | 2 | 1 | 1 (1–2) | **10 (10–12)** | 8 (8–10) | a01–a06, a11–a13, w02, w12 |
| Repaired base, `server` demoted to guidance (B2) | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 12 | 10 | a01 (w02 echoes it) |
| **N**: names + protected scoped evidence | 1 | 1 | 2 | 2 (1–2) | 2 | 2 (1–2)ᶜ | 1 | 2 (1–2)ᵉ | **13 (12–13)** | 11 (10–11) | all 14 (w03 via ALT-A/composite) |
| **N+A**: N + inert shipped declaration | 1 | 1 | 2 | 2 (1–2) | 2 | 2 (1–2)ᶜ | 1 | 2 (1–2)ᵉ | **13 (12–13)** | 11 (10–11) | all 14 |
| A alone: recommendation + legacy §6 check | 2 | 2 | 2 | 0 (0–1) | 2 | 1 | 1 (1–2)ˢ | 1 (1–2) | **11 (11–13)** | 9 (9–11) | a01–a06, a11–a13, w01, w02, w03, w12 |
| L / S-only: N without arbitrary native reads | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 12 | 12 | a01, a03 |
| C: context-package (`requires.mcp`) only | 2 | 2 | 2 | 0 (0–1) | 1 | 2 (1–2) | 2 | 1 (0–1) | 11 (11–12) | 10 (9–11) | a01, a04, a12 (P), w12 (ALT-CTX), w11 (ALT-B) |
| T: tool/capability requirements, no probe | 1 (0–1) | 1 (0–1) | 2 | 1 | 1 | 1 | 0 (0–1) | 1 | 8 (6–9) | 6 (4–7) | a01–a04, a11, w01, w02, w03 |
| G: manager-owned authenticated gateway | 0 | 0 | 0 | 0 (0–1) | 1 (0–1) | 1 (0–1) | 1 (0–1) | 1 (0–2) | 4 (2–5); disqualified (E3=0) | 4 (2–5) | a01–a04, a11, w01, w02, w03, w12 |
| Status quo (calibration only; fails the goal) | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 0 | 11 | 10 | w01, w02 |

Footnotes:
- ᶜ wonder-11 and wonder-12 give E6=2 only if status always shows the evidence source and grade, for example "configured by name; provider identity and authentication not checked" or "operator-asserted". A variant that renders a bare "satisfied" gets E6=1 from them (`verdicts/wonder-11.md` PARK §2, `verdicts/wonder-12.md` §13).
- ᵉ E8=2 assumes the common case: a suitable provider is already configured. For cold first setup every seat scores E8=1, which puts N and N+A at 12 amended / 10 original. wonder-01 and wonder-03 score the cold case in their main table (`verdicts/wonder-01.md`, `verdicts/wonder-03.md`).
- ˢ A alone's E7=2 and its 13 total survive only in the wonder-01 and wonder-02 files. Both files predate the round-9/10 correction that the ordinary-skill audit contract is not closed, which every later seat applied (`verdicts/astra-03.md` E7; `verdicts/astra-13.md` rounds 5–6). A's E4 is 0 under the strict exclusion anchor and 1 under wonder-02's partial-coverage interpolation (`verdicts/wonder-02.md`, scores note).
- The repaired base's ranges come from wonder-12's revised BASE′ (12, E1=1, E8=2) and astra-11 (11, E1=1). astra-13's R row exists only in its initial table.
- Designs scored by one seat only: operator-root declarations ALT-E at 12, initial (`verdicts/wonder-11.md`); csk as frozen ALT-CSK at 6/5 (`verdicts/wonder-12.md`); ship-with-provisioning ALT-E at 10 and the strong capability-probing variant at 4 (`verdicts/wonder-03.md`).
- C ties or beats N on raw points in some sheets but fails the zoo goal (E4=0). wonder-12 §5 and wonder-02's G0 precondition use this to argue that "elegant" needs a goal-coverage gate.

## 3. Proof status

**Rule** (MISSION-MCP amendment `b5e7dab`): two seats from two independent fives agree within one point on every row of the winning design. The second five froze its scores before reading any first-five verdict. Each such seat records a signed checkpoint or a frozen `rounds` post in its verdict.

### First five × second five (the required proof)

| Pair | First-five N vector | Second-five frozen initial vector | Rows differing (by 1) | Final vectors | Evidence |
|---|---|---|---|---|---|
| **astra-02 × astra-05** | `[1,1,2,2,2,2,1,2]` | `[0,1,2,2,2,2,1,2]` | E1 only | identical, 13 | `verdicts/astra-02.md` "Confirmation…"; `verdicts/astra-05.md` "Round 1 comparison" |
| astra-01 × astra-04 | `[1,1,2,2,2,2,1,2]` | `[0,1,2,2,2,2,2,1]` | E1, E7, E8 | identical, 13 | `verdicts/astra-01.md` "Independent agreement"; `verdicts/astra-04.md` post-freeze |
| astra-03 × astra-06 | `[1,1,2,2,2,2,1,2]` | `[0,1,2,2,2,2,1,1]` (L) | E1, E8 | identical, 13 | `verdicts/astra-03.md` agreement; `verdicts/astra-06.md` "Evidence of agreement" |
| wonder-02 × wonder-03 | `[1,1,2,2,2,2,1,2]` | `[1,2,2,2,2,2,1,1]` (ALT-A) | E2, E8 | w03 `[1,1,2,2,2,2,1,1]` (cold E8) | `verdicts/wonder-03.md` "Proof statement" |

The proof condition is **met**. The cleanest pair is astra-02 × astra-05: their frozen vectors differ only in E1, and their final vectors are identical.

### Five 3 (mini, cross-host): confirms

| Pair | Mini frozen initial | Mini final | Max row diff vs first five | Evidence |
|---|---|---|---|---|
| astra-01 × astra-11 | `[1,2,2,2,2,2,1,1]` = 13 | `[1,1,2,2,2,2,1,2]` = 13 | 1 (E2, E8), then 0 | `verdicts/astra-11.md` "Agreement and proof boundary" |
| astra-02 × astra-12 | `[0,2,2,2,2,2,1,1]` = 12 | `[1,1,2,2,2,2,1,2]` = 13 | 1, then 0 | `verdicts/astra-12.md` round 2 |
| astra-03 × astra-13 | `[0,1,2,1,2,2,1,2]` = 11 | `[1,1,2,1,2,2,1,2]` = 12 | 1 (E4 retained) | `verdicts/astra-13.md` round 2 |
| wonder-02 × wonder-12 | ALT-LOCAL `[1,1,2,1,2,1,1,1]` = 10 | `[1,1,2,2,2,2,1,2]` = 13ᶜ | 1 (E4, E6, E8), then 0 | `verdicts/wonder-12.md` §§12–13 |
| wonder-01 × wonder-11 | PREF `[1,1,2,2,2,1,2,1]` = 12 | `[1,1,2,2,2,2,1,2]` = 13ᶜ | 1 (E6, E7), then E8 | `verdicts/wonder-11.md` PARK §4 |

The cross-host pass therefore upgrades the proof to two hosts, using the amended E3 row. wonder-12 explicitly leaves to the convener the ruling that its ALT-LOCAL and N are the same design (`verdicts/wonder-12.md` §12).

### Dissents and qualifications

| Seat | Dissent | Reason |
|---|---|---|
| astra-13 | N E4=1, giving N/N+A 12/10 | Assertion-grade coverage of provider categories is weaker than observed availability. Managed pi, an applied strict Claude channel and managed HTTP header routing stay unsatisfiable (`verdicts/astra-13.md` final table). |
| wonder-11, wonder-12 | E6=1 unless the status wording is mandatory | Name squatting: a wrong server under the right name, or a project-only (repository-controlled) entry, still satisfies a bare name check (`verdicts/wonder-11.md` rev. 3; `verdicts/wonder-12.md` §11). |
| wonder-12 (initial) | Preferred a repaired base, BASE′ at 11, over ALT-LOCAL at 10 | Only a skill-carried identity distinguishes "the server the skill meant" from any same-name server. It later moved to N and defers wire identity until author-pinned provenance becomes a hard requirement (`verdicts/wonder-12.md` §§3, 8, 11). |
| wonder-11 | Scores the base 10 (E4=2, E8=2) | Its explicit operator binding lets every zoo member satisfy, at E8 cost. Even so, it scores the base as beaten (`verdicts/wonder-11.md`). |
| wonder-01, wonder-03 | N+A E8=1, giving 12 | The goal's case is first setup of an unconfigured server. |
| wonder-01, wonder-02, wonder-03 | N+A preferred "on goal fit"; A as the shippable first slice | A is a frontier point on minimality. The astra seats instead treat N as the core and A as optional (`verdicts/wonder-02.md` "Preferred design"). |
| astra-04 (initial) | N E1=0 and E7=2 | Counted a new record family and credited finite states. It corrected both to 1 after the existing-config-family carrier was fixed. |
| All seats | Original E3=0 for every native-inspecting design | Parsing mixed native files reads foreign credential bytes. Only L / S-only reach original E3=2, at the cost of automatic native observation (`findings/f-secret-boundary.md`). |

Two stale files: the wonder-01 file (round 4) still allows a bare stdio command name in the §6 PATH warning and a mandatory marker successor, and the wonder-02 file (round 5) predates the mini results and the A-alone E7 correction. Later seats rejected both positions (`verdicts/astra-11.md` minimality corrections; `parked/wonder-12.md` item 4).

## 4. Smallest change set from the base to N (or N+A)

| # | Change | Supported by |
|---|---|---|
| 1 | Delete `server.package` / `server.endpoint` and the identity conjunct. Keep manifest v5–8 and draft v9 bytes; `transport` stays documentary; `hint` explains setup. | all 14 (wonder-12: deferred, not rejected) |
| 2 | Delete the declaration auth class; no `agent-mcp` schema 2. Authentication stays in native clients: no health checks, no login runs, no credential lookup. | all 14 |
| 3 | Replace aliases and the identity waiver with **one protected operator binding/evidence contract**, homed in a governed successor of the *existing* manager-config family. A new record family would make E1=0. Each record covers an enumerated set of exact requirement identities (skill package + requirement name, batchable, no wildcards), the consumer, the target agent, the selected launch and a provider selector, and is labelled observed or operator-asserted. Repository data may request a binding but never authorize one. | all 14 |
| 4 | Make evidence launch-scoped. Evaluate per agent, scope and native-versus-managed launch. Preserve negative layers until precedence is resolved (OpenCode disable). Apply strict-Claude exclusion only for an applied, non-empty channel. `any`/`all` keep the original target set, and unknown never satisfies. Legacy §6 meaning and `FoundIn` stay unchanged. Status is computed transiently, with no mandatory marker bump. | all; no marker bump: a01, a02, a03, a04, a06, a11, a12, a13 (w01, w02, w03 files still list a marker successor) |
| 5 | Invoke the scoped check as an explicit opt-in at the existing skill-install requirement gate, with a pure recheck available. Add no implicit fatal gate to profile install or resolve. | a01, a02, a03, a04, a06, a11, a12, w03, w11 |
| 6 | Require mandatory status wording: "configured by name; provider identity and authentication not checked" or "operator-asserted". Project-only presence is never rendered as observed-effective. | a02, a03, a04, a05, a06, a11, a12, a13, w03, w11, w12 |
| 7 | State the foreign-byte bound: bounded private parsing and metadata-only diagnostics. Never output raw argv, URL, env, header values, parser snippets or even a bare command name (the §6 PATH check stays private and emits a fixed warning). | bound: all; no raw command: a01, a02, a03, a05, a06, a11, a12, a13 (w01/w03 had allowed it) |
| 8 | Admission or a scoped waiver is not sanitization. Withhold sensitive display, refuse credential-bearing materialization under this feature, and leave an unreviewable plan unapproved. Reconcile with environments §§2.3/5.8/9.1 or narrow the guarantee when delegating to legacy lanes. | a01–a06, a11–a13, w03, w11 |
| 9 | Provision only through operator-selected existing lanes (profile `requires.mcp`, or a separately governed csk native writer), under protected exact-plan consent. Consent covers aggregate launch exposure: env-name union, inheriting recipients and the effective S4 policy. Gates stay cumulative, and native writers never write managed homes. | all 14 |
| 10 | Declare managed HTTP env-header routing unsupported, or govern it separately; `env_names` is not a header binding. | a02, a03, a05, a06, a12, a13, w01, w11 |
| 11 | Add a `url` column to §2.3 surfacing so credential-routing consent is informed. | w01, w02, w03, w11 (a02 via `f-consent-binding`) |
| 12 | *(Optional A)* A skill root MAY ship `agent-mcp.json` (schema 1, unchanged): metadata-only notice on an exact name match; the full remediation tuple (git, revision, directory, name); git-only adoption (path sources informational only); distinct skill and MCP package names; an explicit ordinary-skill audit scope; independent pins; malformed metadata never fails an install. | all 14 support it as optional |
| 13 | Govern the change through a CIP, a decision record, the normative text and positive/negative vectors. Never edit the shared `mcpRequirement` in place. | all 14 |

## 5. Confirmed findings against the base

All seven findings are `proposed`, as the mission requires, and each carries confirmations from all three fives.

| Finding | Effect |
|---|---|
| `f-schema-budget` (astra-01) | "One optional field" hides an identity union, an auth class, binding state and a schema-lane decision; `mcpRequirement` is closed and shared by v5–8 (E1, E2, E7). |
| `f-package-is-not-service` (astra-01) | Declaration digest, recipe equality and a range without a lock owner are not service identity. Provenance needs a lock and admission (E1, E5–E7). |
| `f-launch-universe` (astra-03) | A native name union does not reflect the selected launch: strict Claude excludes native entries, OpenCode overrides or disables are lost, and managed-only providers are missed (E4, E6, E7). |
| `f-opaque-provider` (astra-03) | An operator binding discharges only the identity conjunct. Opaque plugins and cloud connectors need a scoped, labelled assertion, or they stay unknown (E4, E6). |
| `f-consent-binding` (astra-02) | Consent and aliases need protected exact-plan authority. A project alias is authority confusion, and the env-name union is not per-server isolation (E6, E7). |
| `f-secret-boundary` (astra-02) | "Never reads a credential" is false given native parsing, hence the E3 amendment. Raw command echo is a leak, and a waiver is not sanitization (E3). |
| `f-cross-kind-name-collision` (astra-04) | The current resolver cannot hold same-name skill and MCP members in one closure. Base provisioning and optional A need distinct names or must defer (E2, E7, E8). |

## 6. Open questions for the operator

Each of these needs a human product or architecture decision.

1. **Is author-pinned provider identity or provenance a hard requirement?** If yes, N alone does not meet it, and a narrowed identity-bearing base must be reconsidered, with provenance kept in manager-protected state only (`verdicts/wonder-12.md` §11, `parked/astra-12.md` item 5, `parked/wonder-11.md`).
2. **Which secret guarantee is published?** The options are operational non-management (amended E3, N at 13) or literal "never touches credential bytes" (L / S-only at 12, with assertions replacing native observation) (`findings/f-secret-boundary.md` "Proposed change").
3. **Which E4 universe does the proof cite?** Source-category coverage in capable launches gives E4=2; evidence grade in every launch gives E4=1 (astra-13), so N would be 12 (`parked/wonder-12.md` item 3).
4. **May hardened or system policy forbid operator-asserted reliance outright?** (`parked/astra-01.md` item 1, `verdicts/astra-03.md`).
5. **In the stronger lane, does project-only (repository-controlled) presence satisfy, or is it only reported as trust-gated pending?** (`parked/wonder-11.md` item 3).
6. **How does csk D1 (no-consent HTTP without env references) compose with consent before any write?** Should the dependency workflow inherit D1? (`findings/f-consent-binding.md` item 7).
7. **For waived secrets, should environments §§2.3/5.8/9.1 be governed to a stronger rule, or should the feature narrow its guarantee when delegating to the legacy profile lane?** (`parked/astra-03.md` item 6).
8. **Should managed HTTP env-header authentication become a governed names-only header capability, or stay explicitly unsupported?** (`parked/astra-06.md` item 4).
9. **Is a shared launch-level credential trust domain acceptable, or must servers be isolated from each other?** Isolation would need separate launches or future broker work (`verdicts/astra-05.md` §1, `verdicts/astra-12.md` case A).
10. **Sequencing: ship N as the core first (astra seats), or A first as the minimal slice and then N (wonder-01/02/03)?**

### Open threads from parked/

- Governed E7 work that all seats share: the successor config grammar (selectors, scope, revocation); the adapter completeness and precedence table; the opt-in invocation and failure semantics; exact-plan consent over aggregate exposure; reconciliation of §§2.3/5.8/9.1; the optional-A skill-lane audit contract; conformance vectors. See every `parked/*.md`; the most complete lists are `parked/astra-01.md` and `parked/astra-03.md`.
- wonder-01 never responded to two of wonder-11's guards: path-source print-only, and secret-material scope in the skill lane. Peers confirmed both, so neither blocks (`parked/wonder-11.md` item 1).
- The wonder-02 rubric file lags the converged table; wonder-12 asked the convener to confirm the integrated head-to-head table (`parked/wonder-12.md` item 4).
- wonder-12's round-3 `rounds` marker misattributed candidates; its correction supersedes it, and astra-13 acknowledged the correction (`parked/wonder-12.md` item 6).
- Mini-seat and Muse artifacts were delivered as attachments for signed integration by the convener and have been integrated in `f3a04ce`. wonder-01, wonder-02 and wonder-03 left no parked record, and wonder-04 left no files.
