# ALT-PROJ: Projection-only memory — no own journal; a deterministic index over the platform's authoritative journals + a minimal link overlay

- Owner: `wonder-03` (alternatives hunter, five 2; independent scores formed before reading five 1 verdicts)
- Status: proposed alternative to the base (`memory/inputs/SKETCH.ru.md`)
- One line: memory owns no log of record and copies no source bytes; it is a rebuildable projection over journals that already exist, plus the smallest overlay that records claims, justification links and challenges as proposals to their owners.

## Idea

The base Part 2 already retreats from "one append-only event log" to "own journal plus references to authoritative journals", warning that otherwise memory becomes "a second board, a second rights registry and a second dispatcher". ALT-PROJ takes the next, honest step: **delete the own journal too.** Everything memory needs to observe is already journaled by an owner with a single writer:

| Source of record (owner) | What memory reads (never copies as authority) |
|---|---|
| Session-host journal + protected source storage (`swarma-session-host`) | Session events, deliveries, handoff watermarks; bytes only via audited `host.resolve_ref(ref, caller)` (`vision/contracts/handoff-package.md` §4) |
| Board store + activity streams (`activity-event.v1`, per-element `events.ndjson`) | Elements, goal revisions (K6 CAS), transitions, outcome proposals/acceptance, audit (K7) |
| Dispatcher records/effects/receipts (`swarma-dispatcher`) | Launches, executions, grant-chain checks, revocation verdicts, workspace results |
| Keeper ledger (append–fold–replay, `seq`-ordered) | Obligations, deadlines, handoffs of responsibility |
| a2a rooms / waggle envelopes | Signed messages, approvals, decision records (coordination layer) |
| Curator locks/pins | Which instructions/skills/tools an execution actually had (profile pin, lock digest) |
| Git repositories | Code, specs, decision documents, signed commits |

A memory that duplicates these bytes into its own "Observation Log" creates the platform's worst retention bug on purpose: deleting an agent home (owner decision F-1: delete, because absence of secrets cannot be proved) stops meaning anything if a copy already lives in memory. ALT-PROJ makes that bug impossible by construction: there is nowhere for copied bytes to live. The projection holds *refs, digests, extracted typed fragments and indexes* — all rebuildable, all disposable.

## What memory actually owns (the overlay — deliberately tiny)

Only three genuinely new facts exist that no current owner records. ALT-PROJ stores exactly those, and prefers to store them *as board elements* so that even they inherit an existing journal, review flow and grants:

1. **ClaimProposal** — `{id, schema, statement (typed), perspective, valid interval, evidence_refs[], proposed_by}`. Lifecycle mirrors board outcomes: an agent *proposes*; adoption is a board/owner act. A proposal never becomes "supported" by being stored.
2. **JustificationLink** — `{claim, alternative premise sets (OR of ANDs), rule_id}` over claim/evidence refs. Acyclicity enforced on write. This is the base's Justification DAG, kept as data.
3. **Challenge / ReviewOutcome** — `{claim, grounds_ref, challenger}` → board review element → `{outcome: upheld|revised|superseded, decider, decision_ref}`. Revision is a new proposal + supersession link, never an edit.

If the board cannot host the overlay in some deployment, the fallback is a single-writer SQLite store under a dedicated unprivileged account containing *only* these three tables (refs and links, still no source bytes). Either way there is no Event Log, no Knowledge Graph store and no second identity/grant system: writers authenticate with existing keeper-bound identities; every read re-checks grants at the *source owner* when refs are resolved.

## Read path: `recall` and `explain` as live composition

- **Indexing (deterministic first).** Typed sources (board activity, dispatcher receipts, keeper records, Curator locks, git) are projected by deterministic extractors — no LLM in the commit path. LLM extraction over *admitted* text may only create quarantined ClaimProposals (platform book ch. 09 quarantine; ch. 10 log distiller: deterministic, secret-scrubbing, link-preserving). Every projected fragment carries `(source, source_seq/watermark, digest, extractor_version)` so any view can be reproduced or invalidated precisely.
- **`recall(query, caller, task)`** → candidate claims from the index → for each, resolve evidence refs *through their owners* with the caller's grants (host `resolve_ref`, board read, dispatcher status) → return a **KnowledgeView pinned to source watermarks** (`journal_seq H`, board activity seq, goal rev, repo commit): claim, three separate statuses (epistemic derived Belnap from for/against evidence; verification = which deterministic checks passed *at view time*; decision = board/owner state), conflicts, dependencies, and `proofRef` = the ref set. The view records exactly what was issued to which execution (the base's requirement), while honestly distinguishing "issued" from "used as a premise" — use is registered only when the agent (or its recorded justification) cites the claim, otherwise marked `assumed`.
- **`explain(claim)`** walks JustificationLinks to evidence refs and resolves one level at a time (the ladder/`expand` discipline of ch. 09). The full proof DAG is never dumped into an LLM context by default; the compact view + expand-on-demand is the contract.
- **`changes(since)`** is a watermark diff over subscribed sources, not a memory-owned event stream. Source unavailable ⇒ the view says so (`unknown`/`stale since H`), never a silent stale answer.

Delivery into sessions uses only the platform's two framed doors — Curator-approved packages for standing knowledge, handoff packages (`swarm-handoff/2`, per-item provenance, audience-bound) for task slices. Memory has no session-input writer, no wake, no goal authority (D-GOALS: goals come from the launching caller or the board). A TMS "notification" is a board `needs-review` element or an a2a `data` message; starting a review playbook remains an authorized client's decision.

## Truth maintenance without a TMS engine

Dependencies are *evaluated lazily*, not maintained eagerly. When a premise source changes (board supersession, revoked grant, new contradicting receipt), the projector marks directly affected claims `stale`; the full AND-OR evaluation (`C = (A∧B) ∨ (D∧E)`) runs at `recall`/`explain`/review time over the *registered* link subgraph with an explicit bound (max premises per set, max sets, max depth). Beyond the bound, the answer is `needs-review`, not a guess. This avoids ATMS label explosion (exponential worst case; minimal environments can be 2^n) while preserving the only product-relevant guarantee: **every registered dependent of a changed premise is findable and flagged; nothing is silently overwritten.** Unregistered semantic dependencies (an LLM suspects document X relies on decision Y) enter only as quarantined candidate links for review — the base Part 2 says the same; ALT-PROJ makes it the *only* path.

Contradictions are data, not errors: competing claims coexist with perspectives; derived epistemic status `conflicted` (Belnap) is computed from evidence stances. Quorum/board acceptance can fix a *decision* status; it never votes a worldly claim true (distributed protocol: consensus only over deterministic predicates).

## Verification ("proof") without a proof engine

Three deterministic, independently checkable verifiers cover the MVP; everything else is a later plugin behind the same `VerificationReport` shape:

1. **Source verifier** — ref exists under its owner, digest/span matches, watermark is committed.
2. **Attestation verifier** — signature/grant-chain check via the platform's single verification library (keeper keys, attenuation, revocation snapshot); in-toto/DSSE envelopes are accepted as *evidence kinds* whose signatures this verifier checks — signature proves origin/integrity, never truth (the base is right about this; ALT-PROJ enforces it by keeping `verification` disjoint from `epistemic` in the schema).
3. **Outcome verifier** — a board/dispatcher attestation addressed to the exact quadruple (contract version, candidate, policy version, environment) exists with outcome `passed`; `not established` stays `unknown`.

An LLM semantic reviewer may *propose* challenges/candidate links. Its output is labelled model judgement, quarantined, and can never raise a verification status. Z3/Datalog checkers, if ever needed, plug in as additional deterministic verifiers over *closed* claim schemas — a governance decision per schema, not a kernel feature.

## Graphiti / Letta placement (prior-art audit, accessed 2026-10-14)

Graphiti (open-source core of Zep) genuinely provides: episode ingestion with provenance, entity/edge extraction, bitemporal edges (`valid_at`/`invalid_at` + transaction timestamps), non-destructive invalidation (expire, never delete), custom entity types, hybrid vector+BM25+graph search, Neo4j/FalkorDB/Neptune backends, an MCP server. It does **not** provide: justification DAGs with alternative supports, TMS recomputation, four-valued epistemic status, proof verification, grants/federation rights, or deterministic extraction (its pipeline is LLM-driven). In ALT-PROJ, Graphiti is therefore an *optional, replaceable projection backend* for the entity/relation index — never the store of record, never the epistemics. Adopting it in the MVP would still mean operating a graph database + LLM extraction to re-derive what typed platform sources already state exactly; the burden of proof is on that cost. Letta MemFS (git-backed markdown memory, commit per edit, dreaming consolidation) validates the document surface used by the companion alternative ALT-DOC; in ALT-PROJ, MemFS-style repos are one *source* among others (human-readable claims), projected like everything else.

## Secrets, retention, erasure

Strongest story of the three designs, by construction: admitted sources are an explicit allowlist per knowledge space; source bytes stay with owners under their retention rules (home deletion, journal retention, board policy); the projection stores digests/refs/typed fragments and is **rebuilt from sources after any redaction or erasure**, so deletion reaches every derived index by re-derivation rather than by hunting copies. Where a fragment itself is sensitive, it is stored encrypted under a per-space key and crypto-shredded on erasure, leaving the digest + a tombstone ("evidence deleted; claims citing it now unverifiable") — affected claims degrade visibly. Federation exports a **Knowledge Envelope** (claims + resolvable-by-recipient evidence refs + use/retain/forward grant refs + sender identity) via a2a/waggle signed envelopes; enforcement is at service boundaries, and already-disclosed content is honestly unrecoverable (minimize disclosure; no prompt-level promises).

## First slice (useful alone, one host)

Project **two sources only** — board activity + git decision/spec documents — plus the overlay as board element types. Ship: deterministic extractors, SQLite projection (FTS + link tables), `recall|explain|changes` CLI (+ MCP façade), stale-flagging on supersession, watermark-pinned KnowledgeViews delivered via handoff packages. Named use case: a fresh worker session on a Swarma architecture task receives current decisions with reasons, supersession history and stale warnings, instead of re-deriving them from the book. Measured by: evidence precision (sampled claims whose refs actually support them — target ≥ 95% or the extractor/schema is fixed, not the threshold), temporal accuracy (no superseded decision served as current in drills), registered-link invalidation recall (100% required) with false-invalidation rate reported, isolation/leakage tests across knowledge spaces, and recall latency/cost per view. No platform gate depends on it; if the projector is down, work proceeds with an explicit "memory unavailable/stale" warning (memory is never a security dependency).

## Where ALT-PROJ loses (honest)

It is only as good as its source APIs, and several are still specifications, not running code (session-host SH2+, dispatcher, broker): the first slice must therefore start from what runs today (board + git + a2a). Live composition costs more per query than a materialized graph; heavy multi-hop analytics would need a materialized backend (Graphiti or equivalent) *as a cache*. Outside Swarma, each environment needs source adapters — the "universal standalone kernel" story is weaker than the base's (mitigated, not solved, by defining the overlay + view schemas as the portable kernel and treating sources as adapters, exactly as the base treats MCP/hosts).

## Rubric self-score (0–2)

R1 Minimal kernel **1** (kernel schemas are tiny, but projector + adapters + overlay is a system, not a handful of files). R2 Reuse **2** (maximal by construction: no parallel log/registry/board; owners stay authoritative). R3 Authority separation **2** (reads re-authorized at owners; no input/wake/goal path; proposals only). R4 Secrets/retention **2** (no copied bytes; erasure by re-derivation + crypto-shredding of fragments; honest tombstones). R5 Runtime independence **1** (portable view/overlay schemas + MCP façade, but value depends on per-environment source adapters). R6 Honest epistemics **2** (watermark-pinned views, derived Belnap, lazy bounded evaluation, registered-only completeness, stale ≠ supported). R7 Specifiability **1** (overlay/view grammars closable + vectors writable; end-to-end conformance waits on source API publication). R8 Incremental value **1** (two-source slice is useful alone but needs more integration than pure documents). **Total 12/16, no 0 in R3/R4/R6.**
