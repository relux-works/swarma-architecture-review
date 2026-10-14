# Verdict — wonder-04 (rubric and proof; mirror of wonder-02)

- Seat: `wonder-04`, five 2 (adversarial), host ivmbp. Lens: own the rubric, score every serious
  design, mechanically check the base's factual claims about the platform.
- Independence: every score below was fixed from the base sketch, the book and the specs before I
  read any five-1 verdict file or alternative design body. I have seen only topic titles and, after
  scoring, bare totals in `rounds` round markers; no row below was changed by them. The adversarial
  pass against wonder-02 and the named `alt-*` designs follows as a versioned update to this file.
- Base = `memory/inputs/SKETCH.ru.md`, both parts. Where Part 1 (standalone Universal Agent Memory)
  and Part 2 (Swarma embedding) disagree, I score the conjunction and name the disagreement; Part 2
  is the later, platform-aware correction and should govern.

## 1. Mechanical check of the base's factual claims

Checked against book source v0.12 (`platform/wiki/book/swarma/ru/`, dated 13 Oct 2026 in
`00-dlya-kogo.md`), the platform book (`book/ru/`), and the module specs. The base was written
against the v0.10 PDF. Verdicts: **exact** (verbatim or content-identical in v0.12),
**drift** (substance holds, citation/status moved), **compressed** (true but lossy).

| # | Base claim | Verdict | Evidence (v0.12) |
|---|---|---|---|
| C1 | "Session is a cache"; authoritative: session-host journal, parking note, board task+goal | exact, ch. drift | Quote verbatim at `08-host-sessiy.md:5`. Base cites "chapter 7"; the file is `08-…` in v0.12. |
| C2 | Attestation addressed to (contract version, candidate, policy version, environment); approval not transferable | exact, future layer | `16-postskriptum.md:27` verbatim quadruple, three outcomes, head advances only to the attested candidate. Layer status: "designed, not implemented" (`:12`). |
| C3 | Stable identity ≠ UID, path, run; survives account recreation and machine move | exact | `05-klyuchi.md:27` (derivation path encodes identity, not FS path or UID). |
| C4 | One writer per store, typed APIs, no shared mutable files | exact, status drift | `02-sistema-celikom.md` states it verbatim but marks it ⟦proposed⟧, not ⟦decided⟧. Base omits the status. |
| C5 | Session journal+receipts → session-host; execution records+cleanup → dispatcher | exact (target) | `swarma-session-host/spec/session-host.md` §1 ownership table, line 24. It is the gated SH2+ target; spec draft r13, "no implementation claimed". |
| C6 | Context engine is a package inside the session host (adapters, normalization, journal, single input writer, handoff) | exact | `08-host-sessiy.md:53-59` itemises exactly these five parts. |
| C7 | Project content never becomes instruction/tool/permission without approval (Curator) | exact | `10-zapusk.md:43` + CIP-0002, marked ⟦decided⟧. |
| C8 | Handoff package: fixed-moment projection for a named recipient, per-element provenance marks, foreign text never becomes a user command | exact, spec-stage | `08-host-sessiy.md:91` verbatim. But the goal-client interface on the host socket is unpublished (`:107`, ⟦open⟧) and today's host is `tb-sessiond` inside the board (`:7`). |
| C9 | F-1, owner decision 12 Oct: delete the home on deprovision, replacing archive-by-default, because absence of secrets is unprovable | exact | `03-polzovatel-na-agenta.md:101-103`; `15-gde-my.md:56,75`. |
| C10 | Almost half of 44 confirmed cycle-3 findings were text-vs-decision divergences | exact | `15-gde-my.md:79` ("44 confirmed findings… almost half — divergences of text from adopted decisions"). |
| C11 | Checks happen where the act happens; the orchestrator is a petitioner, not a judge | exact | `06-granty.md:47,59` verbatim. |
| C12 | Narrow post-deprovision metadata promise (closed schema, no agent bytes); git acceptance does not prove absence of secrets | exact, stronger | `03-…md:110,114`. Stronger than the base says: the export schema is unpublished and export is **off** until published. |
| C13 | Single session-input writer; operator-stopped sessions are never woken | exact | `08-…md:49` (⟦decided⟧), `:133` ("never wake: operator-stopped or parked session…"). |
| C14 | Board is an add-on, not a platform dependency | exact | `02-…md` layer 4; `08-…md:105` (host MUST work without board/goals/orchestrator); dispatcher is likewise optional (`10-zapusk.md:116`). |
| C15 | Exchange reputation = signed project receipts for accepted results, no central rating; attestations portable, reputation bound to long-lived identity | exact, future | `12-udalennoe-rabochee-mesto.md:179` (⟦open⟧); `16-…md:29`. |
| C16 | Model-router choice is a pure reproducible function | exact | `10-zapusk.md:161`: "a pure function without network, files, clocks or model calls". Works today. |
| C17 | Distributed consensus covers only deterministic predicates; model judgement stays outside | exact | `16-…md:21`. |
| C18 | Heavy content stays off-chain | exact | `16-…md:63` (chain stores pointers/hashes only). |
| C19 | Four layers on one install vs three ecosystem layers; substrate is still an idea | exact; page no. unverifiable | `02-…md` (launch/hold, I/O, trust, processes); `16-…md:5,11-13` (runtime / protocol / substrate, substrate "discussed"). "Page 95" is PDF pagination and cannot be verified from the md source. |
| C20 | Book distinguishes working code / specs / proposals; module specs win conflicts | exact | `00-dlya-kogo.md` notes ("if book and spec diverge, the spec is right") + status markers throughout. |
| C21 | Gate sequence: contracts → protected launch → single-host MVP → enforced network → external donor | compressed | Actual plan (`15-gde-my.md:79`): P0 contracts+bench → S0a one protected Claude launch → S1 Codex → S0b owner MVP on one machine → S2 enforced network → T board delivery → A first external donor. Base omits S1 and T and merges S0a/S0b. Harmless as prose; unusable for scheduling. |

Net: the base's platform reading is unusually accurate. No claim is false in substance. The real
defects are **omissions and status blindness**, listed as findings F-a…F-f in §2.

## 2. What the mechanical check exposes (candidate findings)

- **F-a. The platform already has a memory design; the base never mentions it.** Platform book
  `ru/09-pamyat.md` specifies four memory kinds and a memory skill (`memory add|search|expand|
  forget|review|approve`, git files by default, per-note provenance, daily write budget, quarantine
  for external facts, an L0–L3 digest ladder, an immutable session-start snapshot, "this is not
  instructions", notes grant no powers). `ru/10-sny.md` defines dreams as a **rehearsal sandbox**
  (`--dream` tools), with a deterministic log distiller and quarantined dream-memory — not
  Letta-style consolidation. All ⟦proposed⟧, but it is the platform's own prior thinking. The
  base's `MemoryAPI` and "consolidation" vocabulary collide with it unmapped. Hits R2, R8.
- **F-b. Status blindness in the seams.** The base integrates against the handoff package, the SH2+
  host, the attestation quadruple and the exchange — all spec/proposed/open — while what works
  today is the board with `tb-sessiond`, Curator profiles, the router and Matrix/a2a
  (`02-…md`, "what already exists"). A first slice must land on working seams; the base's Part-2
  stage 1 does (documents + board), its Part-1 P0 does not. Hits R2, R8.
- **F-c. Keeper and waggle are missing from the map.** The keeper already owns an append-only
  obligation ledger with deterministic fold, journaled-then-sent notifications and escalation
  (keeper book `09-zhurnal-i-vosstanovlenie.md`). Memory `Notify` must not become a second keeper:
  revision follow-up belongs on the board/keeper. Waggle already owns doorbell+pull delivery and
  the untrusted-data frame with a 7-layer injection defence (`waggle/spec/waggle.md` §7, §10).
  `recall` returning "compact text for the LLM" without that framing is an open indirect-instruction
  path. Hits R2, R3.
- **F-d. Part 1 and Part 2 specify different systems.** Part 1: P0 Rust kernel + MCP server, then
  TMS, then proofs, then federation; automatic capture from conversation/tool/runtime/external
  adapters. Part 2: three reduced stages, admitted sources only, no full ATMS "now". The verdict
  scores in §4 penalise the conjunction; the RFC must adopt Part 2 and demote Part 1 to a
  requirements source. Hits R1, R4, R7, R8.
- **F-e. The base's own example convicts its MVP order.** The F-1 story (C9/C10) needs only typed
  claims, explicit supersession, provenance and reverse-dependency listing — none of ATMS, signed
  attestations or federation. The cycle-3 corpus (44 findings, ~22 text-vs-decision) is a
  ready-made evaluation set the base never uses. Hits R8, R7.
- **F-f. "One writer per store" is ⟦proposed⟧, and two of the base's load-bearing formats are
  unpublished** (handoff/goal-client interface, C8; post-deprovision export, C12). The design must
  not assume them; it must degrade to today's board/context path. Hits R2, R7.

## 3. Prior-art audit (web, accessed 2026-10-14; primary sources preferred)

- **MCP 2026-07-28 stateless core — confirmed.** The specification's own overview lists "Stateless,
  self-contained requests" and per-request negotiation; the `initialize` handshake and
  `Mcp-Session-Id` are gone ([specification](https://modelcontextprotocol.io/specification/2026-07-28)).
  Consequence the base underplays: `changes(since)` cursors and view pins must travel as explicit
  tool arguments (the base's signature already does this), and long-running `verify` needs the
  optional Tasks extension or an out-of-band job handle — there are no server-initiated requests to
  lean on. MCP's security principles (explicit user consent and control, host mediation) confirm the
  base's "no hidden access to host history" reading.
- **A2A opacity — confirmed.** Agents collaborate "without needing access to each other's internal
  state, memory…" ([A2A specification](https://a2a-protocol.org/latest/specification/)). The base's
  Knowledge Envelope (filtered claims + provenance + use constraints) is the right shape for that
  boundary; A2A itself defines no knowledge-truth semantics, as the base says.
- **Graphiti/Zep — base's characterisation confirmed, differentiation confirmed.** Episodes are the
  immutable inputs; every derived edge carries bitemporal fields (`valid_at`/`invalid_at` +
  `created_at`/`expired_at`) and episode provenance; contradiction handling expires the old edge;
  extraction is LLM-driven; retrieval is hybrid semantic+BM25+graph
  ([Graphiti](https://github.com/getzep/graphiti); Zep paper, arXiv:2501.13956). Graphiti has **no**
  first-class justifications with alternative-support semantics, no ATMS recomputation, no
  verification/attestation layer, no epistemic/verification/decision status split, and no retention
  machinery beyond `group_id` partitioning. Two properties matter for scoring: (1) auto-expiry on
  contradiction is a *silent revision* by this collective's R6 standard; (2) episodes copy raw inputs
  into a graph database (Neo4j/FalkorDB/…) with per-episode LLM cost. Verdict: admissible only as a
  rebuildable Knowledge Projection fed admitted claims — never as the store of record.
- **Letta MemFS — confirmed, and disqualifying as a store under Swarma rules.** Memory is a
  git-backed tree of markdown files the agent itself edits and commits; `system/` files load into the
  system prompt every turn; background "dreaming" subagents consolidate
  ([Letta context repositories](https://www.letta.com/blog/context-repositories)). As a human-readable
  projection this is attractive (the base frames it correctly). As the store of record it makes memory
  an instruction without the Curator approval path (R3) and puts retention in git history inside or
  beside agent homes that F-1 deletes (R4).
- **OpenTelemetry GenAI conventions — confirmed with a stability caveat.** Inference, embeddings,
  retrieval, tool-execution and memory operations are in the GenAI semantic conventions, whose overall
  status is Development ([OpenTelemetry GenAI semconv](https://opentelemetry.io/docs/specs/semconv/gen-ai/)).
  The base says "being developed" — accurate. Do not pin a kernel contract to unstable attribute names;
  the base's "a trace is not automatically reliable evidence" is correct and should be normative.
- **ATMS / Belnap / PROV-O / in-toto+DSSE — textbook claims confirmed.** ATMS labels (minimal
  assumption sets per datum, de Kleer 1986) are worst-case exponential; the base acknowledges this and
  proposes bounded explanations + local recomputation, but never states the bound or its semantics
  (see R7). Belnap's four values as evidence-presence (told-true × told-false) match the base's table.
  PROV-O's core is Entity/Activity/Agent (W3C Recommendation, 2013). in-toto attestations are signed
  statements about artefacts carried in DSSE envelopes; the base correctly insists a signature proves
  origin/integrity, never truth. JSON Schema/SHACL constrain shape, never secrecy — the base says so.

## 4. Rubric and scores

I keep rows R1–R8 exactly as the mission states them (comparability across seats beats local
improvement) and add two public interpretation notes, applied uniformly below:

- **R4 note:** a view already delivered into an LLM context cannot be un-delivered. R4=2 therefore
  requires no-copy-by-default (references + hashes; excerpts only under an inherited retention class)
  so that everything erasable is erasable, plus honest "evidence deleted" reporting for the rest.
- **R6 note:** "delivered ≠ depended-upon" (the base itself raises this) and "LLM-discovered
  dependencies are review candidates, never auto-invalidations" are part of honest epistemics.

Designs scored (my constructions for D1–D5; peers' named alternatives get scored in the adversarial
update once I read them):

- **D0 BASE** — the sketch as written (kernel + ATMS + proof engine + federation; P0–P3; Rust +
  SQLite; MCP-first).
- **D1 TRIMMED LEDGER** (recommended, §5) — base Part 2 with ATMS/proofs/federation deferred behind
  seams, explicit supersession + review queue instead of truth maintenance in v1, platform seams named.
- **D2 GIT-DOCS** — the platform book ch.09 memory skill built literally: typed git documents, ladder,
  quarantine, board decisions; no new service, no graph store.
- **D3 JOURNAL-REPLAY** — no own log; read-only projections over session-host/board/keeper/a2a journals;
  claims live as board artefacts.
- **D4 GRAPHITI-FIRST** — Graphiti as the store of record plus thin side tables.
- **D5 MEMFS-STYLE** — agent-editable git memory repositories with dreaming consolidation as the store.

| Row | D0 | D1 | D2 | D3 | D4 | D5 |
|---|---|---|---|---|---|---|
| R1 Minimal kernel | 1 | 2 | 1 | 1 | 1 | 1 |
| R2 Reuse | 1 | 2 | 2 | 2 | 1 | 1 |
| R3 Authority separation | 1 | 2 | 1 | 2 | 1 | **0** |
| R4 Secrets and retention | 1 | 2 | 1 | 1 | **0** | **0** |
| R5 Runtime independence | 2 | 2 | 2 | 0 | 1 | 1 |
| R6 Honest epistemics | 2 | 2 | 1 | 1 | 1 | 1 |
| R7 Specifiability/testability | 1 | 1 | 1 | 1 | 1 | 1 |
| R8 Incremental value | 1 | 2 | 2 | 1 | 1 | 1 |
| **Total /16** | **10** | **15** | **11** | **9** | **7†** | **6†** |

† Disqualified as "optimal" by the mission rule (a 0 in R3, R4 or R6), whatever the total.

Row justifications (evidence in §1–§3; only non-obvious cells argued):

- **R1.** D0's eight primitives are genuinely small and domain types are correctly pushed to ontology,
  but the kernel also absorbs open-ended justification "rules", five verifier kinds and federation
  envelopes; semantics are not closed → 1. D1 closes justifications to bounded DNF over references and
  moves verifiers outside the kernel (they produce Evidence) → 2. D2/D5 semantics live in prompt
  conventions → 1. D3 multiplies per-journal projection schemas → 1. D4's extraction is prompt-defined
  and nondeterministic → 1.
- **R2.** D0 Part 2 reuses identities, grants, journals and the handoff idea, but Part 1 builds a
  parallel Principal/space/API surface with no map to ch.09, the keeper, waggle or Curator overlays
  (F-a, F-c) → 1. D2/D3 are reuse-maximal → 2. D4 imports a graph-DB service and string identities → 1.
- **R3.** D0 Part 2's four boundaries are exemplary prose, but the mechanism is missing where it
  matters: unframed `recall` text, Integrated/Native auto-capture, and no Curator weight/pin for the
  knowledge package (F-c) → 1, not 0, because `propose`≠verified, no wake/input/grant power is ever
  claimed, and views are structured with provenance. D5 loads agent-edited memory into the system
  prompt every turn — memory *is* an instruction, bypassing C7 → 0. D3 is read-only over foreign
  journals with acceptance left to the board → 2.
- **R4.** D0 states the right principles (admitted sources, redaction, crypto-shredding, honest
  deletion) while Part 1 auto-captures everything into an append-only log and never enumerates the
  allowlist or the erasure path across graph/embedding/LLM derivatives → 1. D4 copies raw episodes
  into a graph DB with no erasure story → 0. D5 puts retention in git history tied to agent homes
  that F-1 deletes → 0. D2's git history resists erasure (rewrite breaks provenance) → 1.
- **R5.** D3 is Swarma-journal-shaped by construction; there is no portable core to carry elsewhere
  → 0 (not a gate row, but it abandons the operator's stated universality). D4/D5 drag a Python +
  graph-DB + LLM stack or the Letta runtime → 1.
- **R6.** D0/D1 are the only designs with Belnap status, provenance≠truth, the three-way status split,
  proposed-never-silent revision and completeness limited to registered dependencies → 2. D2 has
  provenance and review commands but no conflict/status model, and editing supersedes silently unless
  discipline holds → 1. D4 silently expires contradicted edges → 1 at best.
- **R7.** Nobody earns 2 yet: no design in the room (mine included) has peer-checked conformance
  vectors. D0 additionally leaves the ATMS bound and justification grammar unspecified. Uniform 1 is
  the honest score; §5 lists the vectors that would earn D1 its 2.
- **R8.** D2 is useful this week → 2. D0's Part-1 P0 (Rust kernel + MCP server) precedes any value and
  its headline value sits in P1 → 1, rescued from 0 only by Part 2's stage 1. D1's first slice (§6)
  needs none of TMS/proofs/federation and blocks no P0…A gate → 2.

Where the base wins: R5 and R6 outright; its epistemics are the strongest thing in the room and every
serious alternative should import them. Where it loses: it is beaten *today* by D2 on reuse and
time-to-value, which means the base justifies a new service only if the RFC actually delivers the
R6/R7 machinery (closed justification grammar, statuses, vectors) that documents cannot.

## 5. Recommended design D1: trimmed decision-and-evidence ledger (`swarma-memory`)

Keep the base's heart (proof-carrying claims, three statuses, bitemporal history, own log +
references, Part 2's four boundaries). Cut everything whose value is unproved until the ledger earns
it. One optional service under its own unprivileged account `swarma-memory` (one name per component,
C-table in book ch.02); the platform must run without it, exactly as without the board (C14).

**Primitives (kernel, closed semantics).** Seven record kinds in one append-only log:
`ObservationRef` (pointer to an authoritative journal entry + content hash + retention class;
payload bytes are **not** copied by default), `Claim` (typed subject/predicate/object or a
schema-versioned statement, perspective, valid-time), `Evidence` (supports/refutes + ref +
verification kind), `Justification` (bounded DNF: a disjunction of conjunctions over claim/evidence
refs, max terms fixed by schema — this is the whole "rule" language in v1), `Revision`
(supersedes/retracts with reason ref), `Space` (owner identity + grant-checked membership),
`ViewPin` (immutable record that view V at log position P was issued to execution E).
`Principal` is **not** a kernel record: identities are the platform's keyholder identities (C3),
referenced, never re-registered. Domain types (Decision, Finding, Project…) are versioned ontology
schemas above the kernel, governed like Curator packages (pinned, approved, never silently widened).

**Statuses.** Epistemic status is *derived deterministically* from admitted Evidence (Belnap:
unknown/supported/refuted/conflicted) — never stored as an agent-writable flag. Verification status
is the set of verifier kinds that have produced Evidence (source-hash, signature/attestation in the
C2 quadruple form, test result, logic check, semantic review labelled as model opinion). Decision
status is a separate signed record by the authorised owner (adopted/proposed/rejected); memory
records it, the board/owner decides it. Bitemporal throughout: valid-time on the claim,
transaction-time from log position.

**Stores and single writers.** The memory log (SQLite, service-owned directory) is written only by
`swarma-memory`. Everything else stays home: session journal → session host, run records →
dispatcher, tasks/goals/acceptance → board, obligations → keeper ledger, rooms → a2a/waggle,
launch context → Curator (C5, C14). Projections (search index; optionally a Graphiti graph) are
rebuildable derivatives, dropped and rebuilt on erasure; they are never evidence. LLM extractors are
unprivileged clients that may only `propose`.

**API (typed local socket first; CLI and MCP are adapters over the same contract).**
`observe(ref) → receipt`, `propose(claim) → claimRef` (candidate; enters review if above the
space's auto-admit bar), `evidence(add)`, `justify(add)`, `revise(supersede|retract)`,
`recall(query, asOf) → KnowledgeView`, `explain(claimRef) → proof graph`,
`challenge(claimRef) → reviewRef`, `verify(claimRef) → report` (runs deterministic verifiers only),
`changes(cursor) → batch` (explicit cursor, MCP-stateless-safe), `pin(view, execution) → ViewPin`,
`dependedOn(execution, claimRefs)` (registers actual use, distinct from delivery),
`erase(subject, scope) → tombstone report`. The ch.09 memory-skill verbs map onto these
(`add→propose/observe`, `search→recall`, `expand→explain`, `forget→erase`, `review/approve→`
review-queue operations by authorised identities), so the platform's own skill design survives as
the human/agent-facing surface instead of being replaced.

**Platform seams (the R3 mechanisms, not slogans).**
1. **Context path:** a KnowledgeView reaches an agent only as a *pinned, framed data package* —
   session-start snapshot semantics from ch.09 (immutable during the session, weight below role
   modules), delivered through the Curator-approved launch path (C7) and the session host's single
   input writer (C13), rendered inside the waggle untrusted-data frame with per-claim provenance
   (F-c). Mid-session refresh is a new pin via the normal input path, never a silent mutation.
2. **Revision path:** loss of support (evidence retracted, justification term falsified, claim
   superseded) deterministically lists *registered* dependents and opens board review tasks;
   LLM-suspected dependents are filed as candidates with lower priority. Memory never edits specs,
   accepts results, wakes sessions or starts playbooks (C13); the keeper tracks the obligation if
   the follow-up must not be dropped.
3. **Authority path:** every write is checked at the service boundary against the caller's grant
   chain (C11); writer identity is the authenticated platform identity bound to the calling account
   generation, never a self-asserted string. Read/use/retain/forward are four separate checks;
   federation envelopes (deferred) must carry all four explicitly.
4. **Retention path:** admitted sources are an enumerated allowlist per space (board records,
   accepted artefacts, signed attestations, operator-approved documents); raw transcripts and agent
   homes are **not** admitted (C9/C12). Erasure writes a tombstone, crypto-shreds per-space keys
   where payloads exist, rebuilds projections, and downgrades dependent claims' verification status
   to "evidence deleted" — reported, never hidden and never silently re-supported.
5. **Failure path:** memory down ⇒ work continues with an explicit "no memory" warning pinned in the
   view record; an action that policy says needs fresh evidence fails alone. Stop/revoke/recovery
   paths never call memory.

**Deferred behind seams (explicit non-goals for v1):** ATMS label maintenance (v1 evaluates the
bounded DNF directly over registered dependencies; full assumption-set machinery only if measured
need appears), theorem provers (verifier plugins may add Evidence later), federation and agent
reputation models (C15 seams recorded; no second reputation system), automatic capture adapters
(each is a separate admitted-source decision with its own retention class), any embedding/graph
dependency in the kernel contract.

**Conformance vectors that would earn R7=2** (each: initial log → operation → required view/status):
supersession chains; (A∧B)∨(D∧E) with B retracted (status unchanged, dependents *not* flagged);
conflicting evidence → conflicted, never resolved by recency; evidence erasure → verification
downgrade + projection rebuild proof; cross-space recall leakage (must return nothing, including via
`explain` and `changes`); delivered-without-`dependedOn` (no invalidation obligation claimed);
view-pin reproducibility (same log position → byte-identical view); grant-revoked writer mid-batch
(atomic refusal). Metrics: evidence precision, temporal accuracy, invalidation precision/recall
*over registered dependencies only*, false-invalidation rate, leakage tests, write/recall cost —
the base's metric list, with its invalidation-correctness row scoped honestly.

## 6. First slice (MVP) and how its value is measured

**Slice:** memory of Swarma's own architecture (the base's Part-2 stage 1, made concrete). Ingest,
by reference, this repository's findings/verdicts, book decisions (F-1…F-72) and board outcomes;
typed Decision/Finding claims; explicit supersession; `recall`/`explain`; review queue. No TMS
recompute beyond DNF evaluation, no signatures beyond existing commit/board provenance, no MCP, no
federation. Runs on one host, parallel to gates P0…A, blocking none (C21).

**Named use case:** "What is the current rule for agent homes, what did it replace, why, and what
still assumes the old rule?" (F-1, C9) — answerable in one view with the reason chain and the list
of registered dependents.

**Measurement:** replay the cycle-3 corpus (C10): seed decisions as of their adoption dates, then
measure (a) how many of the ~22 text-vs-decision divergences the dependent-listing surfaces without
human search (recall over registered deps), (b) false positives filed, (c) time-to-answer vs the
grep/read baseline, (d) zero cross-space leakage under the vector suite. If (a) does not beat the
D2 git-docs baseline materially, D1 has not justified its service and D2 should ship instead — that
is the falsifiable bet.

## 7. Smallest change set from the base to D1

1. Adopt Part 2 as normative; demote Part 1 §§4–10 (ATMS-first ordering, P0–P3, Rust/MCP-first) to
   background requirements (F-d).
2. Replace "ATMS with bounded explanations" by the closed bounded-DNF `Justification` + explicit
   supersession + review queue; keep ATMS as a named future seam with an entry criterion (measured
   DNF insufficiency), not a phase.
3. Make `Observation` reference-only by default (ref + hash + retention class); payloads require an
   admitted-source entry. Delete automatic capture from v1 scope (§6 adapters become separate
   decisions).
4. Add the missing mechanisms to Part 2's boundaries: framed/pinned/weighted views via Curator +
   session host; `ViewPin` + `dependedOn` as kernel records (the base suggests both in prose).
5. Name the seams the base omits: ch.09 memory-skill verb mapping, keeper for follow-up custody,
   waggle/a2a doorbell+pull for `changes`, board tasks as the only revision effector (F-a, F-c).
6. Demote Graphiti from "prototype on top of it first" to optional rebuildable projection; forbid
   its auto-expiry from counting as a `Revision` (§3).
7. Enumerate the admitted-source allowlist and the erasure/tombstone semantics in the kernel
   contract (base: principles only), including projection rebuild and honest downgrade.
8. Reorder delivery to §6's slice; drop language/runtime commitments (Rust, SDKs) from the
   architecture — SQLite + typed socket API is the contract, implementation language is free.
9. Fix citations/statuses (C1 chapter, C4 ⟦proposed⟧, C21 full gate list) and mark every seam with
   its book status (works today / specification / proposed / open) so the RFC cannot silently
   depend on unpublished formats (F-b, F-f).

## 8. Questions only the operator can decide

- **Q1 Product shape.** Is the deliverable a standalone open-source Knowledge Runtime that Swarma
  merely adopts (base Part 1), or a Swarma module whose kernel is *extractable* later (D1's
  assumption)? This decides R5's weight, the API's centre of gravity and the repo/license story.
- **Q2 Erasure promise.** May memory ever store payload excerpts, or references+hashes only? The
  former weakens the F-1/C12 posture and must be an explicit, per-source-class decision.
- **Q3 Review capacity.** Who staffs the claim/challenge review queue, and what auto-admit bar (if
  any) lets low-stakes claims skip human review? Without an owner, `propose` becomes a write-only
  swamp or, worse, auto-admission by timeout.
- **Q4 Automatic extraction.** Is LLM extraction from conversations/tools ever admitted, and under
  which retention class and quarantine (ch.09/ch.10 already say: quarantine until human review)?
- **Q5 Ontology governance.** Who approves claim-schema versions and justification bounds, and are
  they Curator packages with pins, or memory-internal migrations?
- **Q6 Federation disclosure.** When federation arrives, which spaces may emit envelopes at all, and
  is `forward` ever grantable for personal spaces? (Disclosure to an independent agent is
  irrevocable; the base is right that only minimisation + contracts help — someone must own that
  risk acceptance.)

## 9. Round-2 amendments (v2; supersedes §5–§6 details where they conflict)

v1 above is frozen as the independence witness (SHA-256
`cb70097c629412db406af25554cb2dac8c37ac8de36279732d64b9daf4d15972`, attached in `rounds`).
After freezing it I read the peer candidates, the named alternatives and my mirror's verdict.
Six peer findings are confirmed (my confirmations with event ids are in their topics); each amends
D1 as follows. None changes my frozen v1 scores for D0–D5; peer-design scores are in §9.3.

### 9.1 Design deltas adopted into D1

- **A1 View-relative inference** (`f-view-inference`, astra-02/05/03/06): epistemic status is
  computed over recipient-eligible records only and reported as supported-within-view with scoped
  completeness text that never reveals whether hidden evidence exists. Global journal
  cuts/watermarks stay in protected audit; public cursors and `changes` are audience-scoped.
  Reauthorization at every disclosure, including historical queries, `explain` and counts/rank.
  (My v1 §5 "derived from admitted Evidence" is replaced by this.)
- **A2 Custody closure** (`f-erasure-closure`, astra-02/05/01/04): a content-derivation and
  custody inventory, separate from epistemic edges, enumerates every excerpt, summary, embedding,
  index, cached view, export and diagnostic. Erasure fences reads and derivative commits per
  disposition generation (late extraction cannot repopulate), distinguishes access-closed /
  purge-pending / purged-within-named-boundary with per-store receipts, and restore reconciles
  erasure obligations against a witness outside the restored failure domain. Host-owned sinks
  (transcripts, tool results, mandatory control floors) are separate custody boundaries: memory
  claims no deletion there without the owner's disposition receipt, and refuses sensitive export
  into unqualified sinks. My D1 R4=2 stands only with A2 in the contract text.
- **A3 Closed rule semantics** (`f-conflict-semantics`, astra-03/06): justification edges have
  three distinct meanings — `documentary_basis` (attribution: supports only source_says),
  `review_on_change` (declared rationale/impact), `sufficient_support` (checked one-way signed
  rules; AND within a premise set, alternatives across sets). No completion/biconditional step
  (¬A, ¬D never license ¬C), no contraposition, no ATMS nogood filtering, withdrawal is never
  negation. Belnap labels are read-time rendering over witnessed +/− channels. My v1 "bounded DNF"
  is replaced by this.
- **A4 Completeness fields** (`f-bounded-inference`, astra-03/06): every computed status ships
  (label, completeness+, completeness−, registration coverage, source availability). Display
  truncation is flagged separately and never weakens a completed evaluation; discovered + and −
  witnesses prove conflict even with traversal incomplete. (Bounded rule evaluation over the
  registered set is exhaustive by construction; the fields still ship.)
- **A5 Data-only channel, pull-first** (`f-memory-data-channel`, astra-01/02/04): overlay weight
  is presentation, not a mechanism (my v1 seam-1 wording corrected). Knowledge reaches agents as
  framed tool-result data with per-item author/verdict preserved through summary, cache, handoff
  and resume; `swarm-handoff/2` is a closed schema with no memory kind, so slice 1 is pull-only
  and any pushed delivery waits for an owned schema revision. The enforceable property is that
  capability/admission gates stay unchanged — never a promise that labels defeat prompt injection.
- **A6 Ingestion assurance** (`f-mirror-origin`, astra-06; mechanically verified by me in
  `skill-project-management/pkg/board/query/activity_ledger.go:53-86`): every source reference
  carries assurance `authoritative | mirror | assertion`. A remote board mirror proves only that
  an authenticated principal submitted it; it supports `source_says` claims until resolved against
  the authoritative ledger or a subject-bound attestation (quadruple form, C2).
- **A7 No-daemon entry (M0)** (astra-01/03/04, wonder-01/03 convergence): the first slice is a
  reviewed documentary register with a read-only adapter — no new daemon or service account. The
  single-writer protected service is a later deployment profile of the *same* semantics, entered
  when private or multi-proposer admission requires controlled custody. This replaces my v1 §6
  service-first framing; the F-1 use case and cycle-3 replay measurement are unchanged, with the
  bounded design's labelled-corpus comparison (vs plain search and vs typed documents, same access
  and question set) adopted as the measurement harness.

### 9.2 Recommendation restated

D1 as amended is the same design family as **bounded evidence memory** (astra-01 design +
astra-03 bounded-support semantics + astra-02/05 custody/view clauses), entered via its documentary
M0 profile. I withdraw D1 as a competing name and recommend that family, pinned at a named
revision, as the collective's winner candidate. My non-duplicate additions, kept as requirements
on that family: the ch. 09 verb mapping as the agent-facing surface (finding
`platform-memory-omitted`), per-seam governing-source status labels (finding `status-blind-seams`),
the Part-2-normative convention (finding `two-bases`), and the pre-registered falsification rule
(§6: if dependent-listing does not materially beat the documents baseline on the labelled corpus,
ship the documents profile alone).

### 9.3 Scores for peers' named designs (wonder-04, as written; convention in my scoreboard post)

| Design | Vector R1..R8 | Total | Note |
|---|---|---|---|
| Bounded-evidence, protected-service (read in full) | 2,2,2,2,2,2,1,2 | 15 | Exact match with five-1/five-2 scorers |
| Bounded-evidence, documentary M0 alone | 2,2,2,1,2,2,1,2 | 14 | Git is not a deletion mechanism (design's own words) |
| ALT-DOC (wonder-03) | 2,2,2,1,2,1,1,2 | 13 | Agree author and wonder-02 exactly |
| D★ amended (wonder-01) | 2,2,2,1,1,2,1,2 | 13 | As filed 12 (R3=1); R4=1 by author's accounting |
| COMPILER (wonder-01) | 2,2,2,1,2,1,1,1 | 12 | Author's own R4=1; conditional 2 rejected |
| JOM as filed (wonder-01) | 2,2,1,1,1,1,1,2 | 11 | R3 overlay lane, R6 global derivation, R7 unpublished |
| ALT-PROJ (wonder-03) | 1,2,2,1,1,2,1,1 | 11 | R4 2→1: mirror typing, view scope, host-sink exclusion not yet in text |

Proof statement: the protected-service profile has at least two seats from two fives agreeing
within one point on every row (in fact exact vector matches across fives 1–2, mine included). That
meets the mission's "proved" condition at design level, provided the winner is named as that exact
profile plus companions at a pinned revision, R7 stays honestly 1 (39 named vectors, schemas and
expected outputs unpublished, nothing executed), and no empirical optimum is claimed. Open
convention splits, all proof-safe (≤1 per row): base R6 charged to R6 (astra-03/06) vs R7
(wonder-02/04); base totals 9–13 explained by the Part-1/Part-2 fork (finding `two-bases`).

Open referee disputes I filed against wonder-02's scoreboard method (event
`$CS-y5wIo5Fwol9c5h6WNmjO3TW-HimaOQ-j7wdsaz8w`): dual claimed/conservative totals under an R7 floor
applied two ways; conditional gate-row 2s (COMPILER/ALT-PROJ R4) against its own as-written
method; a store-count tie-break that double-prices R1/R2. Plus one factual correction in the
base's favour: `gen_ai.memory.*` conventions are merged into the (Development-status) GenAI
semantic conventions ([PR #140](https://github.com/open-telemetry/semantic-conventions-genai/pull/140);
attribute registry on HEAD lists `gen_ai.memory.record.count`; accessed 2026-10-14), so the
sketch's four-item list stands with a uniform instability caveat. These disputes do not block the
proof above; they must be closed before any *unique-optimum* claim across the 13–15 frontier.

### 9.4 Round-3 addendum (exact-assembly ratification; disputes closed)

- **A8 Service-admission gate** (`f-memory-service-admission`, astra-04; verified by me in
  `swarma-user-manager/spec/helper.md` §8.1: "every other non-root platform service — explicit row
  required before v1 enforced readiness; no permissive default"): the protected-service profile is
  deployable only with its own admission contract — published deny-all egress row, socket with
  peer-UID+generation admission, private state custody, start/scheduled readiness qualification,
  installer/operator ownership. A service-account name supplies none of this; no borrowed
  host/broker authority; a source URL mints no network authority. Documentary M0 needs none of it.
  The ratified design below has adopted this gate verbatim.
- **Graphiti erasure, code-verified** (`f-graphiti-erasure`, astra-05): I fetched the pinned source
  (`getzep/graphiti` @ `9d56c190`, accessed 2026-10-14) and read `remove_episode` in full: an edge
  is deleted iff the removed episode is *first* in `edge.episodes` (an [E1,E2] edge dies with E1),
  nodes iff mention-count is 1, and there is no surviving-summary regeneration. The vendor blog's
  last-support cascade description does not describe this code path. D4's R4=0 stands; any Graphiti
  use is disposable-cache-only with custody outside it and exact backend/version qualification.
- **Exact assembly ratified.** I fetched and hash-verified `bounded-evidence.md` at SHA-256
  `9c8f63fd8aad3d44081b93225f727e504468297cadc21ab1d0973903d28c0599` (commit `0ce0094`), read the
  full delta against the revision I originally scored (`ba38ed1d…`), and read the semantics
  companion at SHA-256 `62ae18cbec7c…` (post-`476ec36` revision; closed one-way profile,
  vectors S13/S21/S24–S26 present). Every delta strengthens the design. My scores on these bytes:
  protected-service **[2,2,2,2,2,2,1,2] = 15**, documentary **[2,2,2,1,2,2,1,2] = 14** — exact
  agreement with astra-02/04/05/06 and corrected wonder-02. Design-level proof across two fives
  therefore holds for this pinned assembly; R7 remains 1 (schemas/fixtures are follow-on work by
  the design's own statement); no empirical optimum and no two-host proof is claimed (five 3 on
  the mini had not reported at the time of writing).
- **Referee disputes closed.** wonder-02 accepted all three (event `$GCrR_qi1qymXpcOIEqHj3WfH0PKmxZl6ReaUy_c4Z1s`):
  single file-level R7 standard, dual total withdrawn (base-minus = 14), no conditional gate-row
  2s (ALT-PROJ R4 rescored to 1 there too), tie-break demoted to operator-visible context, C-22
  corrected. I conceded the last cross-seat delta (COMPILER R5 2→1, total 11; journal-adapter
  dependence, consistent with ALT-PROJ). Zero open score deltas remain between the rubric seats.

