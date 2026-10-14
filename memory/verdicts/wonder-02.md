# wonder-02 verdict — rubric and proof (living document, round 1)

Seat: `wonder-02` (five 1, ivmbp), Muse Wonder full 1.0. Lens: own the rubric, score every
serious design, mechanically check the base's factual claims about the platform.

Status: round-1 draft. Scores will be revised as alternatives land. Nothing here is final
until PARK.

## 0. Method and rubric stewardship

I score each design **as written**, not as charitably repaired; a repair is scored as an
explicit delta ("base + fix X"). This keeps the "smallest change set from the base" honest:
every point the winner gains over the base must be payable by a named change.

Evidence standard I will apply to every seat's scores, mine included:

- A score of **2** needs a primary-source citation (book file:line, spec section, or
  product documentation URL + access date), not an inference.
- A score of **0** needs a counterexample or a quoted design statement, not a vibe.
- "Proved" per the mission needs two seats from two fives agreeing within one point on
  every row. I will maintain the cross-seat score table in the room and flag any row where
  two fives differ by 2 (the only way proof can fail while totals look close).

Proposed rubric amendments (open for refutation; rubric text itself unchanged so far):

1. **Tie reporting (corrected round 5):** the mission defines optimal by total + no
   gate-zero only. At equal totals I report "no unique optimum" and note operational
   surface (new stores/accounts) as operator-visible context — explicitly a value choice
   for the operator, not a proof input and not a stewardship decision (wonder-04).
2. **R7 evidence floor (corrected round 5, single standard):** R7=2 requires conformance
   vectors published as a file with exact expected outputs (conflict, withdrawal,
   alternative support, delayed correction, cutoff, erasure, view-inference pair,
   metadata invariance). A named list of proposed vectors, however good, scores R7=1.
   (wonder-04 correctly flagged my earlier list-level wording as a dual standard;
   withdrawn — one standard for every design including my own.)
3. **Part-splitting:** the base is two documents (Part 1 universal runtime, Part 2 Swarma
   embedding) and Part 2 explicitly corrects Part 1 (own journal + references instead of
   one global log; smaller first step). I score the combined base, and note where Part 1
   alone would score differently, so the operator can see what Part 2 already fixed.

## 1. Mechanical check of the base's factual claims

Checked against book source v0.12 (`wiki/book/swarma/ru`, `wiki/book/ru`,
`wiki/book/keeper/ru`, `wiki/book/model-router/ru`), `swarm-platform-architecture`,
`curator-spec`, and primary web sources. Verdicts: CONFIRMED / DRIFT (true in substance,
citation moved) / STATUS-INFLATED (true words, stronger status implied than the source
gives) / PARTIAL / OMISSION.

| # | Base claim (sketch location) | Verdict | Evidence |
|---|---|---|---|
| C-1 | Book distinguishes working code / decisions / specs / proposals; module specs win on conflict (P2 §1) | CONFIRMED | Five status marks defined, `swarma/ru/00-dlya-kogo.md:32-42`; "if book and spec diverge, the spec is right" at `00:7`. Nuance: marks "do not form a ladder" (`00:42`). |
| C-2 | One installation = four layers (launch/retention, I/O, trust, processes); larger scheme = runtime + distributed protocol + substrate; substrate is only a discussed concept (P2 §1) | CONFIRMED, page uncheckable | Four layers verbatim `02-sistema-celikom.md:7-13`; three layers + substrate "no paper yet" `16-postskriptum.md:5,13,55`. "Page 95" is PDF pagination, not present in source. |
| C-3 | "Session is a cache", ch. 7; authoritative: session-host journal, parking note, board task + goal (P2 §2) | CONFIRMED text, DRIFT chapter | Verbatim at `08-host-sessiy.md:5` in v0.12 (chapter 8, not 7). The apiary book carries the same heading at `ru/07-zapusk-i-session-host.md:65`, so the "chapter 7" citation matches the other book or v0.10 numbering. |
| C-4 | Attestation addressed to (contract version, candidate, policy version, environment); approval not transferable to another candidate (P2 §2) | CONFIRMED | `16-postskriptum.md:27` (quad verbatim, three outcomes); non-transferability is load-bearing in the cited model check, `16:33`. |
| C-5 | Stable identity ≠ UID / path / run; account move/recreate without identity change (P2 §2) | CONFIRMED | Derivation path encodes stable identity, not FS path or UID, `05-klyuchi.md:27`; retirement does not revoke identity, `05:51-53`. |
| C-6 | One writer per store, typed APIs, no shared mutable files; session journal + receipts → session host; execution records + cleanup → dispatcher (P2 §3) | CONFIRMED, STATUS-INFLATED | Rule verbatim `02:21` but marked ⟦предложено⟧ (proposed), while the sketch leans on it as established principle. Ownership split verbatim `08:158`. The single-writer-of-input instance is ⟦решено⟧ (`08:49`). |
| C-7 | Context engine is a package inside the session host: adapters, event normalization, journal, single writer of input, handoff packages (P2 §4) | CONFIRMED | Item-for-item match, `08:53-59`. |
| C-8 | Curator owns approved launch configuration; project content does not become instruction or permission without approval (P2 §4) | CONFIRMED | `10-zapusk.md:43` (CIP-0002, marked ⟦решено⟧ in book); curator-spec CIP-0002 is still Draft with "no acceptance decision" (`CIP-0002…md:62`) — book/spec status tension worth knowing, direction agreed. |
| C-9 | Handoff package built at a fixed moment for a named recipient, per-item provenance marks so foreign text never becomes a user command (P2 §4) | CONFIRMED, incomplete | `08:91`; contract adds allowlist-only fields, "never raw transcripts", and full re-authorization at seed (`handoff-package.md` §§1,5). The sketch does not carry these strengtheners into its own KnowledgeView. |
| C-10 | F-1: owner decision 12 Oct — delete home on retirement, replacing archive-by-default, because absence of secrets is unprovable (agent can hide a token copy anywhere) (P2 §5) | CONFIRMED | `03-polzovatel-na-agenta.md:101-103`, incl. the token-hiding argument nearly verbatim. |
| C-11 | Almost half of the 44 confirmed findings of the third review cycle were text-vs-decision divergences (P2 §5) | CONFIRMED | `15-gde-my.md:79`. This is the base's best quantified motivation; it survives checking. |
| C-12 | Verification happens where the action happens; orchestrator is petitioner, not judge (P2 §6) | CONFIRMED | `06-granty.md:47,59` nearly verbatim. |
| C-13 | Narrow promise for post-retirement service metadata; git acceptance does not prove absence of secrets (P2 §6) | CONFIRMED | `03:110` (closed-schema export from the service's own records, no agent strings; export disabled until schema published), `03:114`. |
| C-14 | Single writer of session input = session host; goals belong to board or caller; operator-stopped sessions must not be woken (P2 §6) | CONFIRMED | `08:49`, `08:101` (owner decision 10 Oct), `08:133,139`. |
| C-15 | Board is declared a superstructure, not a platform dependency (P2 §6) | CONFIRMED | Chapter title itself, `13-doska.md:1,5`; also `02:13`, `08:105`. |
| C-16 | Exchange reputation = signed project receipts for accepted results, no central rating; outcome attestations portable across projects, reputation bound to long-term identity (P2 §7) | CONFIRMED | Exchange: `12-udalennoe-rabochee-mesto.md:179` verbatim (status ⟦открыто⟧, "idea for the future" — the sketch's "в замысле" is honest). Portability + identity binding: `16:29`. |
| C-17 | Model-router choice is a pure reproducible function (P2 §7) | CONFIRMED | "Selector is a pure function of frozen inputs: no network, files, clocks, model calls", `model-router/ru/06-zapis-resheniya.md:24`; same in `swarma/ru/10:161`. |
| C-18 | Distributed consensus limited to deterministic predicates; model judgments stay outside; heavy content off-chain (P2 §7) | CONFIRMED | `16:21` (predicates enumerated), `16:63` (pointers on-chain, content outside). |
| C-19 | Book's sequence: contracts + secure launch → single-host MVP → forced network → external donor; memory must not block these gates (P2 §8) | CONFIRMED in substance | Plan: P0 contracts/stand → S0a Claude → S1 Codex → S0b owner MVP one machine → S2 forced network → T board delivery → A first external donor, `15:79`. Critical context the sketch underplays: platform modules (user-manager, dispatcher, broker, session-host service) are spec-stage with **no code yet** (`02:52`); ch. 8's service design is SH2+ target, today sessions live in `tb-sessiond` inside the board (`08:7`). Any memory MVP that assumes SH2+ seams is building on a gate that has not passed. |
| C-20 | MCP 2026-07-28 uses a stateless core; long-term state must live in the memory service, not the MCP session (P1 §1) | CONFIRMED (web, 2026-10-14) | Spec revision 2026-07-28 retired `initialize` handshake and `Mcp-Session-Id`; per-request `_meta` (SEP-2575/2567): https://modelcontextprotocol.io/specification/2026-07-28/changelog (via search index, accessed 2026-10-14). Consequence the sketch mostly respects: MCP cannot push; `changes(since)` polling is the compatible shape for notifications. |
| C-21 | MCP gives a memory server no hidden access to full host history/state — deliberate security limitation (P1 §6) | CONFIRMED as design fact | Consistent with MCP's host-mediated tool model; the sketch correctly derives "minimal API + adapters" instead of total capture. No primary-text contradiction found. |
| C-22 | OpenTelemetry is developing GenAI semantic conventions for inference, tool execution, retrieval **and memory** (P1 §6) | CONFIRMED with stability caveat (corrected round 5) | Memory operations/attributes are merged in semantic-conventions-genai (`create_memory`/`search_memory`/…, `gen_ai.memory.store.id`, `gen_ai.memory.record.count`, opted-in query/records). The entire GenAI set carries Development (unstable) status, memory included — so "being developed" covers all four accurately; do not pin kernel contracts to unstable names. Correction by wonder-04, independently re-verified by me 2026-10-14. My round-1 PARTIAL overstated the gap. |
| C-23 | Graphiti already has episodes, provenance, temporal intervals, typed relations, incremental graph updates (P1 §9) | CONFIRMED (web, 2026-10-14) | Zep/Graphiti docs + arXiv 2501.13956: episodic ingestion with provenance, bi-temporal edge validity, non-destructive invalidation, incremental updates. Note for differentiation: Graphiti **does** react to changed facts (invalidation); the base's defensible delta is first-class justifications with alternative sufficient sets + verifiers, not invalidation as such. The sketch itself flags this as a hypothesis needing audit (P1 §9) — honest. |
| C-24 | Letta MemFS: agent-editable file memory, git versioning, consolidation, shared repositories (P1 §9) | CONFIRMED (web, 2026-10-14) | Letta docs (docs.letta.com MemFS): git-backed markdown memory, every edit committed, `system/` pinned into context, background "dreaming" consolidation, shared context repositories. |
| C-25 | **(Omission)** The sketch never mentions the platform book's own memory chapters: `ru/09-pamyat.md` «Память» and `ru/10-sny.md` «Сны» (P2 passim) | OMISSION, material | Ch. 09 already proposes: four memory kinds; a memory **skill** with `memory add|search|expand|forget|review|approve` as the only write path; git-files default store; per-note provenance; daily write budget; **quarantine** for external-source facts until human review ("otherwise a planted instruction can persist"); a summary ladder (journal → session → day → week) where every summary line references what it retells; immutable per-session snapshot; "notes grant nothing" ⟦решено⟧ (`09:41`). Ch. 10 adds a night consolidation cycle with a deterministic log distiller and dream-memory quarantine (`10:24-31`). A design claiming platform fit must either build on this or explicitly supersede it; the base does neither. This caps the base's R2 (see §2) and is my finding candidate `f-platform-memory-chapters` (peer confirmation requested; astra-01 already builds on `ru/09` in `f-memory-data-channel`). |

**Summary of the check:** the base's platform reading is unusually accurate — 19 of 19
checkable Part-2 claims are confirmed in substance. The failures are of a different kind:
one chapter-number drift (C-3), one status inflation (C-6), readiness understatement
(C-19), and one material omission (C-25). (C-22 was initially scored PARTIAL by me; corrected to CONFIRMED-with-caveat in round 5 — the error was mine, not the base's.) The base
does not need fact repair; it needs scope repair. That is good news for proof: scores can
argue about design, not about what the platform says.

## 2. Rubric scores

Scale 0–2 per mission. "Optimal" = highest total with no 0 in R3/R4/R6.

### 2.1 The base (Part 1 + Part 2 combined, as written)

| Row | Score | Justification (evidence) |
|---|---|---|
| R1 Minimal kernel | **1** | Eight primitives (P1 §2) with domain types pushed to ontology is a good start, but the same document also puts full ATMS with alternative-assumption sets (P1 §4), five verifier families (P1 §5), federation envelopes with four distinct rights (P1 §8) and three product lines (Kernel/TMS/Bridge, P1 §12) into the proposal. The kernel is small; the design is not. Part 2 §8 walks scale back rhetorically but does not redraw the kernel boundary. 2 requires "a handful of primitives with closed semantics" — semantics are not closed (see R7). |
| R2 Reuse | **1** | Part 2 genuinely reuses: stable identities, grants checked at action point, authoritative journals stay authoritative, own journal + references instead of one global log (P2 §3), handoff-style knowledge packages, board-as-superstructure precedent for optionality. Held at 1 by: (a) a new service under a new service account with its own journal, API and MCP server (P1 §10 P0) proposed without engaging the platform's own memory skill + ladder + snapshot design (C-25); (b) no use of waggle signed envelopes for the federation envelope, keeper single-writer journal precedent, or the router's frozen-input snapshot pattern it itself cites (C-17). Parallel machinery, even well-mannered, is still parallel. |
| R3 Authority separation | **1** | The denials are explicit and repeated: memory never grants (P2 §6), never writes session input or wakes (P2 §6), never becomes a system instruction (P2 §4), `propose` creates candidates not truths (P1 §6), TMS notifies but does not launch (P1 §11, P2 §5). Why not 2: R3's 2-bar includes "or becomes an instruction **without the existing approval path**", and the base never names the delivery contract that enforces this for KnowledgeView — no audience/purpose/verdict binding, no re-authorization at seed, while proposing a "compact text representation for the LLM" (P1 §6). The platform already solved this shape once (handoff §§1,5; C-9); the base states the rule but does not inherit the mechanism. Rule stated + mechanism missing = 1. (Peer candidate: `f-memory-data-channel`, astra-01.) |
| R4 Secrets and retention | **1** | Strong stance: rejects "store everything first" (P2 §6), logical (not physical-forever) immutability, redaction + key destruction + index rebuild, honest reporting when evidence is deleted. Held at 1 by: Part 1's four automatic capture adapters (conversation/tool/runtime/external, P1 §6) pull toward bulk ingestion with no admission contract; no derivation/custody inventory showing deletion reaches embeddings, summaries, cached views, telemetry (peer candidate `f-erasure-closure`, astra-02); no quarantine for external-source facts, which ch. 09 already requires (C-25). No 0: an erasure path and explicit sources are at least designed-in as requirements. |
| R5 Runtime independence | **2** | Core explicitly independent of any agent environment (P1 §1, §11); MCP is one adapter among HTTP/SDK/CLI (P1 §6); three integration tiers with honest statement of what Basic cannot guarantee (P1 §6); stateless-MCP consequence correctly absorbed (C-20). Same API ≠ same isolation promise is stated (P2 §3) — exactly the honesty this row rewards. |
| R6 Honest epistemics | **2** | The base's strongest row. Provenance ≠ truth as an architectural primitive (P1 §3); epistemic / verification / decision status separated (P1 §3); Belnap four values, no global consistency demand (P1 §4); LLM semantic review explicitly not a proof (P1 §5); invalidation completeness promised **only for registered dependencies**, LLM-found semantic dependents go to a review queue (P2 §5); "delivered to agent" ≠ "used as premise" must be marked assumed (P2 §4). Peer candidates `f-bounded-inference` and `f-conflict-semantics` (astra-03) identify real gaps, but they are precision gaps in an honest stance — I charge them to R7, not R6. If a peer argues bounded-inference mislabelling is an R6 violation, that is the row to watch for a 2-point split. |
| R7 Specifiability and testability | **1** | For 1: a typed API sketch (7 operations, P1 §6), an evaluation metric table (P1 §10), and a named open fork (central model / source of truth / deployment, P1 §12). Against 2: no closed grammar for claims/justifications; ATMS × Belnap consequence rules undefined (nogood filtering vs dual-channel preservation give different answers — `f-conflict-semantics`); no evaluation-completeness label under bounded inference (`f-bounded-inference`); claim identity, scope and interval-overlap semantics undefined; no conformance vectors; no governance path for ontology/schema evolution. Per my proposed R7 floor (§0.2), prose semantics caps at 1. |
| R8 Incremental value | **2** | Part 2 §8 defines a first stage that is useful alone: memory of decisions and evidence over documentation, architecture decisions and admitted board results, on one host, explicitly parallel to (not blocking) platform gates, with a named use case — Swarma's own architecture memory — and a measured pain (C-11: ~half of 44 findings were text-vs-decision drift) plus a product hypothesis to measure (fewer re-investigations and forgotten decisions). Caveat recorded, not scored down: Part 1's P0 (Rust core + SQLite + MCP server, P1 §10) is heavier than this stage needs; scored on Part 1 alone this row would be 1. The combined base contains its own correction, so 2. |
| **Total** | **11 / 16** | No zeros; gate rows R3=1, R4=1, R6=2. The base is **admissible but beatable**: an alternative wins by buying R1/R2/R7 points without spending R3/R4/R6. |

### 2.2 Alternatives scored (round 2)

Scored as written in the round-1 design files / topic posts; round-2 author amendments
noted separately. My scores, wonder-02:

| Design | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | Total | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Base (§2.1) | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 11 | — |
| JOM — journal-only, git cards (wonder-01) | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 11 | R3: delivery path (a) "Curator operator overlay snapshot" is the unsafe lane per `f-memory-data-channel` (weights order chapters, do not demote instruction meaning); path (b) handoff is sound. Author self-scores R3=2, total 13. R6: read-time Belnap over *all* registered refs leaks via status (`f-view-inference`); author amended to view-relative derivation in round 2, which would raise R6 only together with a completeness label. R7: downgraded 2→1 in round 3 — lint rules are closed but card/derivation schemas and vectors are not published (astra-04 caps its own document design at R7=1 for the same reason; my §0.2 floor applied uniformly). astra-04 also notes Letta MemFS puts root memory files into the system prompt every turn — the card shape must not import that activation semantics. |
| COMPILER — briefings + dreams (wonder-01) | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 11 | Initially 13 (identical to author's vector). Round 4: R4 2→1 as filed, accepting astra-02's challenge — ladder digests, rejection reasons/digests, pinned package bytes, TTL caches and host-transcript/telemetry sinks are persisted derivatives without an erase fence; "stateless compilation" alone does not earn R4=2. The author's refs-only pinning clarification closes one sink, not all. Scoped to persistable documents only, R4=2 is recoverable. R6=1: conflicts shown, never tracked; explanation drift conceded. |
| D★ — JOM + promotion rule + base statuses (wonder-01 verdict) | 2 | 2 | 1 | 1 | 1 | 2 | 1 | 2 | 12 | As defined in the verdict file (overlay delivery retained; R7=1 per the round-3 floor above). With the author's round-2 amendments (data-only handoff seam as blocking requirement, view-relative derivation, refs-only admission, custody inventory): R3 1→2, total 13 (author says 14 with R7=2; the one-cell difference is exactly the unpublished-vectors question). R4 stays 1 by the author's own honest accounting (git clones escape the managed boundary). |
| ALT-DOC — typed git documents + board (wonder-03, five 2) | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 13 | Identical vector to the author's self-score, independently reached. Stronger than JOM as filed on R3 (Curator-package promotion, not overlay snapshot) and R5 (files+CLI anywhere). Still needs mirror-assurance typing on board refs (`f-mirror-origin`). |
| ALT-PROJ — projection over journals, no own log (wonder-03) | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 11 | Author self-scores 12 with R4=2. Round 5 (wonder-04, accepted): no conditional gate 2s — as written, projected fragments/sinks lack a specified custody inventory, so R4=1; the author's later hybrid amendments adopt that inventory, which is scored there. |
| Hybrid "refs, not copies" (wonder-03 recommendation) | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 13 | Author: 15, self-discounted to 14 (R7 conditional). My extra delta is R4: the hybrid keeps the DOC git surface whose claim bodies may carry "short reviewed quotations" — by ALT-DOC's own accounting that caps R4 at 1 (git-history erasure is an operator rewrite). PROJ-style re-derivation erases the *index*, not committed quotations. All other rows match the author within the R7 condition. |
| Bounded evidence memory (astra-01; semantics astra-03/06, custody astra-02/05) | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 14 | **Provisional**: scored from topic posts + published score vectors; I have not yet read the design file (sandbox cannot pull main). Matches astra-01's self-score vector exactly. R4/R7 held at 1 by the authors themselves until custody contracts and conformance vectors publish — that self-restraint is what good R7 hygiene looks like. astra-03's "16 at design-contract level" would require R4=R7=2; I do not confirm those two cells until I can read the vectors. |
| Base-minus (§3, mine) | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 14 | Self-score under the single R7 standard: R7=1 (vector list, not a published file with exact outputs). One number: 14 as a standalone text; superseded as a separate entry by the family profiles (§7–§8). The tie-break (§0.1) then decides: bounded-evidence and base-minus both posit one new journal + one service account; D★ posits none. |

Reading of the table: the frontier is 13–14, the base at 9–13 depending on seat (§2.3).
Every serious challenger beats the base mainly on R1/R2/R7/R8 and ties or slightly beats
it on gate rows. The remaining real fork, named by wonder-01 and confirmed by my scoring:
**one managed service journal (bounded-evidence / base-minus) vs git cards with no service
(D★)**. The service buys enforceable R4 (erasure receipts inside one boundary,
view-relative inference at one writer); git buys R8/R2 immediacy. My tie-break prefers
fewer new stores, but R4 is a gate row and the mission only forbids 0 there — both are
admissible. The decider is empirical and belongs to the MVP: if the first corpus is
documents+board records (non-secret by construction), D★'s R4=1 costs nothing and it wins
on tie-break; if transcripts enter scope, only the managed journal can honestly reach
R4=2. Operator question Q4 in §6 is therefore load-bearing, not administrative.

### 2.3 Cross-seat proof tracker

"Proved" needs two seats from two fives within one point on **every row** for the winner.
Base scores published so far (per-row where given, else total):

| Seat (five) | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | Total |
|---|---|---|---|---|---|---|---|---|---|
| wonder-02 (1) | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 11 |
| wonder-01 (1) | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 0 | 9 |
| wonder-03 (2) | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 9 |
| astra-01 (1) | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 13 |
| astra-02 (1), astra-03 (1), astra-04 (2), astra-05 (2) | — | — | — | — | — | — | — | — | 13 each (vectors not yet readable by me; astra-03/06 stated base R6=1 in-room) |
| astra-06 (2) | — | — | — | — | — | 1 | 1 | — | 12 |

Round-3 tracker updates:

- **First cross-five per-row proof exists — for bounded-evidence, not for the base.**
  astra-04 (five 2) scored the published bounded-evidence design (e8ab519)
  `2,2,2,1,2,2,1,2 = 14`, "matching astra-01 row for row" (five 1). If the collective
  designates that design the winner, its *score* already meets the mission's proof
  condition (two seats, two fives, every row within one) — with astra-04's own caveat
  that agreement on a paper score is not empirical superiority. My provisional 14
  (same vector) would make it three seats, but mine is scored from topic text, so I do
  not count it until the design file is attached in-room.
- **R6 convention settled within tolerance.** astra-03/astra-06 charge missing
  incomplete-evaluation output semantics to base R6 (=1); wonder-01/astra-01/I credit
  the principles (=2). Both sides stated the convention explicitly in-room; the spread
  is one point, proof-safe. No rubric change needed; record the convention with scores.
- **Base R8 remains the only 2-point split** (wonder-01 0 vs astra-01/wonder-02 2;
  wonder-03 at 1 bridges both). Open for wonder-01's response to the §2.3.1 convention.
- **The fork is dissolving into staged profiles.** astra-01/03/04/06 now accept a
  no-daemon documentary register as M0 (read-only adapter over reviewed records), with
  the single-writer service as a later profile for private/multi-proposer admission;
  wonder-01 accepts the service *iff* R4=2-with-receipts is required, with git as
  export/projection. Remaining disagreement is sequencing and R4 accounting for git
  quotations (my hybrid delta, §2.2), not architecture family.
- My claim-check corroborations: wonder-03 independently flagged C-6 (one-writer rule
  ⟦предложено⟧) and confirmed C-3/C-4/C-9/C-15/C-12 equivalents; wonder-01 and
  wonder-03 independently audited Graphiti/Letta (C-23/C-24) with the same result.

Findings from the tracker:

1. **Proof-blocking split on base R8**: wonder-01 scores 0 ("value needs P1; P0 duplicates
   ladder+handoff"), astra-01 and I score 2 (Part-2 stage-1 stands alone). A 2-point row
   spread means *the base's* score cannot currently be "proved" between any wonder+astra
   pair. The disagreement is definitional — which Part defines the first slice — not
   factual. Proposed convention for the room: score the base on its Part-2-corrected
   staging (Part 2 is part of the base and explicitly supersedes Part 1 scale), and record
   "Part 1 alone: R8 0–1" as a footnote. Under that convention wonder-01's evidence still
   lands (P0 Rust service is overweight) without a proof-blocking 0.
2. **R2/R3 one-point spreads** (wonders 1, astra-01 2) are proof-safe but systematic:
   the two Wonder seats charge missing mechanisms to the row that states the value;
   astra-01 credits stated boundaries. Either convention is defensible; mixing them
   silently is not. I ask every seat to state its convention in one line with its vector.
3. **Leader convergence**: three independent seat families (astra-01/03/05/06
   bounded-evidence ~14–15, wonder-01 D★ 14, my base-minus 14 conservative) land within
   one point *in total*, but per-row proof for a single named winner does not yet exist:
   the designs differ on R4/R5 by construction (git vs service). Proof will require the
   collective to first pick the fork (§2.2) — totals cannot substitute for that choice.
4. Request to all seats: post your per-row vector in the room (as astra-01 did). Verdict
   files on main are unreachable from sandboxed Muse seats (no pull), so room vectors are
   currently the only universally readable score source.

## 3. Recommended design (amended base, "base-minus"; round-3 convergence note)

Round-3 note: base-minus has converged with the collective's bounded-evidence family
(astra-01/03/06 semantics + astra-02/05 custody) and with the documentary-register M0
now accepted across fives 1–2. I no longer defend base-minus as a separate design; I
defend it as the *service profile* of that family, entered only when private or
multi-proposer admission requires a controlled writer. The M0 entry point is the
documentary register (ALT-DOC/D★-amended shape) under the same semantics and view
contract. What follows is the service-profile contract, unchanged in substance.

I recommend keeping the base's semantics and cutting its machinery — the smallest change
set in §4. In RFC-startable detail:

**Primitives (kernel, closed list).** `ObservationRef` (reference to an authoritative
journal entry or an admitted document — memory stores its own journal only for records it
itself originates), `Claim` (typed subject/predicate/object + schema id + perspective +
valid-time + transaction-time), `Evidence` (directed link claim↔observation/claim with
polarity), `Justification` (named rule + premise set; multiple justifications = alternative
sufficient sets, stored explicitly, **no ATMS environment enumeration in v1**),
`Revision` (supersedes/retracts, append-only), `KnowledgeSpace` (ownership + admission
policy), `KnowledgeView` (audience-, purpose-, epoch-bound projection, §below).
`Principal` is **not** redefined: it is the platform's stable identity (C-5) referenced
by id. Three statuses (epistemic Belnap-4, verification kind, decision owner+state) as in
the base, plus two honesty fields the base lacks: `completeness` (complete / cutoff at N /
source-unavailable / unregistered-dependencies-possible) on every computed status, and
`evidence_state` distinguishing withdrawn-evidence from counter-evidence.

**Stores and single writers.** One new store only: the memory journal (claims, evidence,
justifications, revisions, view receipts), single writer = the memory service under its own
service account, API-only access (no shared SQLite file — base P2 §3 already says this).
Everything else is referenced, not copied: session-host journal, dispatcher records, board
activity, keeper ledger, a2a rooms stay authoritative in place. Derived indexes (graph
projection, embeddings, summaries) are rebuildable caches registered in a derivation
inventory so erasure can enumerate them. The apiary memory ladder (C-25) is the summary
mechanism, not a competitor: ladder lines are claims whose evidence is the level below.

**APIs.** The base's seven operations, tightened: `observe` (admitted sources only, per-space
admission policy; external-source material enters quarantine per ch. 09 and cannot support
a claim until released), `propose` (candidate only), `recall` (returns a KnowledgeView
bound to recipient + purpose + policy epoch + source revisions; inference computed **inside**
the authorized view so hidden records cannot leak through status/counts — `f-view-inference`),
`explain` (justification DAG under the same authorization), `challenge`, `verify`
(verifier plugins: source/attestation/test/logic deterministic; LLM reviewer output typed as
opinion, never proof), `changes(since)` (polling; the only MCP-compatible notification shape,
C-20). Transport: local socket API first; MCP adapter and HTTP/SDK are projections of the
same contract. Delivery into a session goes through the existing paths only — as a handoff
package reference or a board goal revision — with handoff §§1,5 semantics (allowlist,
per-item verdicts, re-authorization at seed, never promoted to user/system authority).

**Semantics (the R7 purchase).** Signed-literal evidence propagation with dual channels
preserved (no ATMS nogood deletion of conflicted environments in v1); recomputation is
local, bounded and **labelled** (cutoff ⇒ status carries `completeness: cutoff`, never a
silent flip to unsupported — `f-bounded-inference`); claim identity = (schema, subject,
predicate, object, perspective, valid-interval), with interval-overlap rules stated;
withdrawal of evidence recomputes support, it is not counter-evidence. Conformance vectors
required before any second implementation: conflict, unsupported cycle, withdrawal,
alternative support (the (A∧B)∨(D∧E) case), delayed correction (bitemporal), cutoff,
erasure-then-verify, view-inference pair (identical authorized records, different hidden
records ⇒ identical public semantics).

**TMS scope.** v1 is "TMS-lite": explicit justifications + dependency traversal +
needs-review proposals. Full ATMS, theorem provers (Z3/Datalog) and a graph database are
deferred behind evidence that explicit justification sets hurt (measured false-invalidation
and missed-invalidation rates on the MVP corpus). Graphiti, if used, is a replaceable
projection behind the conformance vectors — never the journal of record (base P1 §9 already
wants this; I make it a scored requirement).

**Out of scope (explicitly).** Granting or inferring permissions; accepting results;
writing session input; waking sessions; reputation scores that feed authorization;
federation beyond signed envelope export of admitted claims (waggle envelope, four rights
checked at the service boundary, disclosed-is-irrevocable stated); any dependency of
stop/revoke/reconcile/recovery paths on memory availability.

**Score of base-minus as written in §3:** R1 2, R2 2, R3 2, R4 1 (derivation inventory
required in text; erasure vectors not published), R5 2, R6 2, R7 1 (single standard,
§0.2), R8 2 — total 14/16. With the family's published custody clauses and watermark
fix it is the P-managed profile at 15 (§8); the delta must be earned in text, not claimed. Any alternative beating this must show its work row by row; that is the
proof game I am refereeing.

## 4. Smallest change set from the base

1. **Import ch. 09/10** (C-25): memory skill write-path discipline, quarantine, ladder,
   per-session snapshot, night consolidation as the extraction scheduler. Deletes the need
   for Part 1's four always-on capture adapters; admission becomes per-space and explicit.
2. **Bound the TMS**: ATMS → explicit justification sets + labelled local recomputation;
   add `completeness` to every computed status.
3. **Give KnowledgeView the handoff contract**: audience/purpose/epoch binding, allowlist,
   per-item verdicts, re-authorization at seed, inference inside the authorized view.
4. **Add a derivation/custody inventory** separate from the epistemic graph; erasure =
   fenced per-store receipts; restore applies erasure state before serving;
   evidence-unavailable ≠ refuted ≠ verified.
5. **Close the semantics**: signed-literal rules, claim identity + interval overlap,
   withdrawal semantics, eight conformance vectors (§3).
6. **Shrink P0**: decisions-and-evidence memory over git documents + board records first
   (no Rust kernel, no graph DB, no MCP server required for value); engines replaceable
   behind vectors afterwards.
7. **Reuse waggle envelopes** for federation export; reuse router-style frozen snapshots
   for any consumer that must stay a pure function.

## 5. First slice (MVP)

**Use case (named):** Swarma's own architecture memory — decisions, review findings,
spec versions and their dependencies — the base's own best example (F-1 supersession,
C-10/C-11), on one host, over sources that already exist as git documents and board
records. No SH2+ dependency (C-19): the slice reads committed documents, so it works
while platform modules are still spec-stage, and blocks no gate.

**Slice contents:** memory journal with Claim/Evidence/Justification/Revision;
admission = named document sets + board exports; `propose/recall/explain/challenge`;
supersession chains with bitemporal stamps; needs-review list on premise change
(registered dependencies only, completeness labelled); KnowledgeView delivered as a
handoff-referenced data payload; conformance vectors for the five semantic cases.

**Value measurement (pre-registered, so the result can falsify the design):**
(1) divergence catch rate — replay the third review cycle: of the ~22 text-vs-decision
divergences (C-11), how many does dependency traversal flag before human review?
(2) false-invalidation rate on the same corpus; (3) time-to-answer for "what replaced
decision X, why, and what still assumes the old rule?" vs manual grep, measured on the
F-1 case; (4) zero authority incidents: no MVP output path can write session input,
change a goal, or alter a spec (checked by construction + one red-team prompt-injection
pass through a planted memory). If (1) is near zero, TMS-lite is wrong and the
supersession+review-queue alternative should win — I will rescore accordingly.

## 6. Questions only the operator can decide

1. **Supersede or absorb ch. 09/10?** Is the apiary memory skill + ladder the personal-memory
   layer under this design (my assumption), or does the operator want it replaced?
2. **Product shape:** one open-source Knowledge Runtime with a Swarma adapter (base's
   choice), or Swarma-module-first with extraction later? This decides where the journal
   format is standardized and who governs ontology evolution.
3. **Admission default:** which sources may memory ingest without per-item human release —
   board records and git documents only, or also session transcripts (with what retention)?
   Ch. 09's quarantine says external facts wait for a human; does that extend to agent
   transcripts?
4. **Erasure promise:** is crypto-shredding + derivation-inventory erasure the required
   bar from v1, or is "admitted sources are non-secret by construction" (documents/board
   only) acceptable for the first slice, deferring transcript-grade erasure?
5. **Decision-status ownership:** when memory records "decision adopted", whose signature
   makes it so — board kernel, orchestrator, operator — and may memory ever *display* a
   decision state fresher than the board's own record?
6. **Graphiti probe:** authorize a time-boxed spike (projection-only, behind vectors) as
   part of the first slice, or keep the MVP engine-free until semantics vectors pass?



## 7. Round-4 addendum (proof state and mirror reconciliation)

**Mirror check (wonder-04, five 2, independent).** Their mechanical check (21 claims,
none false in substance) and base vector `1,1,1,1,2,2,1,1 = 10` agree with mine
(`11`) within one point on every row (sole difference R8). Two independent rubric seats
thus corroborate §1, including C-6 status inflation. I adopt their two finer catches:
the gate sequence in the base is *compressed* (actual plan P0 → S0a → S1 → S0b → S2 →
T → A; base omits S1/T and merges S0a/S0b — harmless prose, unusable for scheduling),
and the keeper/waggle omission (memory `Notify` must not become a second keeper;
waggle's untrusted-data framing is the delivery precedent). Their `f-two-bases`
convention (Part 2 normative, Part 1 background) is the same convention I proposed in
§2.3.1; I confirm it, plus `f-platform-memory-omitted` (independent duplicate of my
C-25 finding — two seats, same omission, strengthens it) and `f-status-blind-seams`
(my C-19, generalized).

**Complete base tracker (per-row, all seats that published vectors).**

| Seat | Vector R1..R8 | Total |
|---|---|---|
| wonder-01 (1) | 1,1,1,1,2,2,1,0 | 9 |
| wonder-03 (2) | 1,1,1,1,2,1,1,1 | 9 |
| wonder-04 (2) | 1,1,1,1,2,2,1,1 | 10 |
| wonder-02 (1) | 1,1,1,1,2,2,1,2 | 11 |
| astra-06 (2) | (R6=1, R7=1 stated) | 12 |
| astra-01/02/05 | 1,2,2,1,2,2,1,2 | 13 |
| astra-03 (1) | 1,2,2,2,2,1,1,2 | 13 |

Every row's cross-seat spread is ≤1 except R8 (0..2). Under the two-bases convention
(Part 2 normative), wonder-01's R8 evidence is preserved as "Part 1 alone: 0" and the
base's proved band is **9–13, centre 11–13**; no convention makes the base the winner.

**Winner and proof.** The bounded-evidence family with staged profiles (documentary
register M0, no daemon → single-writer service profile for private/multi-proposer
admission) is the emerging winner. Proof state by the mission definition:

- Bare bounded-evidence design (e8ab519): `2,2,2,1,2,2,1,2 = 14`, identical vectors
  from astra-01 (five 1) and astra-04 (five 2) on the same revision. **Proved score.**
- Full family with semantic companion (astra-03, 23 proposed vectors) + security
  profile (astra-02/05): `2,2,2,2,2,2,1,2 = 15`, identical vectors from astra-02/03
  (five 1) and astra-05/06 (five 2). **Proved score at design-contract level**, with
  two explicit conditions the authors themselves state: R7 stays 1 until closed
  schemas + exact vector outputs publish, and R4=2 holds only with the custody/view
  clauses — now including the round-4 watermark extension (public views must not
  expose global journal cuts/cursors/digests/dirty-generations; audience-scoped
  counters or a stated declassification only — `f-view-inference`, confirmed by
  astra-02/05/06 and by me). My score for the full family is 14 until that extension
  lands in the companion text (R4 one cell below the authors; within proof tolerance).
- Documents family (JOM-amended/D★/ALT-DOC): 12–14 depending on R3/R7 conventions;
  wonder-01 and wonder-03 agree within one point per row on base and hybrid. It is the
  M0 profile of the winner, not a rival family, once pull-only delivery and
  view-relative derivation are adopted (both now accepted by wonder-01).
- Disqualified shapes (wonder-04, unrefuted): Graphiti-as-store-of-record (R4=0) and
  MemFS-as-store (R3=R4=0). `f-graphiti-erasure` (pinned-source verified by two seats)
  independently confirms: Graphiti deletion cannot certify erasure custody; projection
  only, exact-version qualification required.

**What would still change my scores:** publication of closed schemas + executed
vectors (R7 1→2 for the family, to 16 — nobody should claim this yet); the watermark
fix in companion text (my family R4 1→2, to 15); wonder-01's answer on base R8 under
the two-bases convention; five-3 (mini) vectors, which would upgrade proof to two
hosts. Absent those, my recommendation stands: build the documentary M0 first on
working seams (board + git), semantics and view contract as in §3–§5, service profile
only on measured need with its own admitted service boundary
(`f-memory-service-admission`, confirmed).

## 8. Round-5 addendum (convergence)

- The watermark condition in §7 is met in text: astra-03's refreshed companion
  (signed 476ec36, 26 proposed vectors incl. S24 metadata mutation, S25 stale
  restore, S26 late derivative writer) keeps internal global cuts protected and
  requires external handle/cursor behaviour independent of hidden mutations;
  astra-01's revised design (56d18ee) adopts the same projection-token rule.
  I therefore raise my full-family score to **15** (`2,2,2,2,2,2,1,2`), joining
  astra-01/02/03/05/06 and astra-04's exact-revision score of the protected-service
  profile, with the documentary P0 profile at **14** (R4=1) agreed by astra-01,
  astra-04, wonder-03 (provisional) and me. R7 remains 1 everywhere until closed
  schemas and exact expected outputs are published and executed — the last point
  on the table, and no seat claims it.
- COMPILER: author and I now agree at 12 as filed (13 for the amended
  persistable-corpus scope). JOM/D★: author accepted R7=1 (vectors unpublished);
  the slice-1 fork collapsed — all documentary variants start as the same
  no-daemon pilot. Remaining named differences: R4 boundary for later sensitive
  scopes, R5 standalone-product question (operator), R7 publication work.
- My finding `platform-memory-chapters` gained a second confirmation (wonder-03).
- Unchanged open items: five-3 (mini) scores — would upgrade the proof to two
  hosts; wonder-01's base R8 under the two-bases convention (astra-04's objection
  to R8=0 for the complete sketch is on record and matches my reading); closed
  schemas + executed vectors (R7). My scores are stable unless one of these lands.
- Postscript (same round): wonder-01's final vectors (base `1,1,1,1,2,1,1,1`,
  COMPILER as-filed 11 with R5=1) resolve the last 2-point split: base R8 is now
  1–2 across all seats (R8=0 withdrawn under the two-bases evidence), and I adopt
  R5=1 for COMPILER (portable format ≠ portable system), giving 11 in agreement
  with the author. Every rubric row for the base and for the winning family now
  has cross-seat spread ≤ 1. Scores stable; awaiting five-3 or PARK.
