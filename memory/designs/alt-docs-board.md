# ALT-DOC: Ledger of documents — typed git documents + board decisions (no graph store, no new service)

- Owner: `wonder-03` (alternatives hunter, five 2; independent scores formed before reading five 1 verdicts)
- Status: proposed alternative to the base (`memory/inputs/SKETCH.ru.md`)
- One line: memory is a set of typed, git-versioned documents whose decisions are board acts; a deterministic linter replaces the TMS engine; Curator packages and handoff packages are the only delivery paths into sessions.

## Idea

The platform already has every hard part the base needs: an append-only audit (board activity `activity-event.v1`, `skill-project-management/docs/activity-mutation-coverage.md`), immutable goal revisions with CAS (board kernel K6, `vision/contracts/goals.md`), recipient-bound context projections with per-item provenance (`vision/contracts/handoff-package.md`), approved instruction delivery (Curator context packages with locks/pins), and a proposed memory skill with `memory add|search|expand|forget|review|approve`, provenance per note, quarantine for external facts, and a memory ladder (platform book ch. 09 «Память»). ALT-DOC says: do not build a Knowledge Runtime service at all. Harden ch. 09 into a closed document discipline and let git + board be the store of record.

Letta's MemFS proves the storage shape in production: an agent's durable memory as a tree of markdown files in a git repository, every edit a commit, a `system/` directory always in context, background "dreaming" consolidation (Letta docs, MemFS, accessed 2026-10-14). ALT-DOC differs from MemFS in one decisive way: documents are *typed* (closed front-matter schemas), decisions are *board acts* (not agent edits), and nothing in a document is ever an instruction until Curator approves it into a profile.

## Primitives (the whole kernel)

Four record kinds, each a document (or a headed section with a stable ID) with closed YAML/JSON front-matter validated by JSON Schema:

1. **ClaimDoc** — a typed assertion: `{id, schema, subject, predicate, object|statement, perspective, valid_from, valid_to, epistemic, verification, decision}`. The three statuses are separate closed enums, exactly as the base demands: epistemic ∈ {unknown, supported, refuted, conflicted} (Belnap, *derived* from evidence links, never hand-set); verification ∈ {unchecked, source-checked, signature-checked, test-checked, formally-checked} with a `verification_ref`; decision ∈ {proposed, adopted, superseded, rejected} set only by a board transition or an operator-signed record.
2. **EvidenceRef** — never a copy of bytes: `{id, kind, ref, digest, span?, stance: for|against, observed_by, observed_at}`. `ref` points at the authoritative owner: a git commit/blob, a board element + activity seq, a session-host journal seq (resolved via `host.resolve_ref`), a dispatcher receipt/effect, a keeper ledger seq, an a2a room event id, or an artifact digest. `digest` + optional span hash let a checker verify the cited fragment still matches (the base's "source verifier", as a pure function).
3. **JustificationLink** — `{claim, premises: [[...],[...]], rule}`: a list of alternative premise *sets* (OR of ANDs), stored as data. No engine maintains labels; the linter evaluates lazily (see below). The justification graph over claims must be acyclic; the knowledge graph (entities/relations inside claim statements) may cycle freely — only justification is a DAG, as in the base.
4. **RevisionRecord** — `{supersedes, superseded_by, reason_ref, decided_by, decided_at}`. Supersession is explicit and append-only: the old claim stays, marked `superseded`; git history is transaction time, `valid_from/to` is valid time. Bitemporal queries are `git log` + field filters — no temporal database.

Domain types (Decision, Finding, Project, AgentModel, …) are schemas in a registry directory, not code. That is the entire runtime: files, schemas, one linter/indexer CLI.

## Stores and single writers

| Store | Writer | Content |
|---|---|---|
| Memory document repo(s) (git) | Board-governed merge path (change requests K1–K5); agents propose, reviewers land | ClaimDocs, EvidenceRefs, JustificationLinks, RevisionRecords; **no secret bytes, no transcripts** |
| Derived index (SQLite FTS + link tables) | The indexer (single process) | Rebuildable cache of the repo at a named commit; deleted on redaction and rebuilt |
| Board | Board kernel (existing) | Decision status, review queue, acceptance — unchanged |
| Session-host journal, dispatcher records, keeper ledger, a2a rooms | Their existing owners | Source bytes; memory holds only refs |

No new OS service account, no new socket, no new log of record. The indexer is a CLI/library any principal can run read-only over a checkout; the sole *write* path is a landed commit, which inherits the platform's signed fast-forward + review discipline (board K3/K5).

## How the base's mechanisms map

- **TMS → linter + review queue.** On every landed change (and on demand), the linter: (a) validates schemas, refs, digests, DAG acyclicity; (b) recomputes derived epistemic status from EvidenceRefs; (c) finds claims whose *every* justification set now contains a superseded/refuted premise (bounded reverse-reachability over registered links only) and emits `needs-review` proposals as board elements. It never flips a decision status and never deletes a claim. This keeps the base's central promise — "revision is proposed, never silent" — and drops ATMS label maintenance, whose worst case is exponential in the number of assumptions (minimal-support generation is NP-hard; de Kleer ATMS literature; UBC TR-88-11, accessed 2026-10-14). Completeness is claimed *only* over registered links, in writing, in every report.
- **Proof Engine → three deterministic checks.** (1) Source check: ref resolves, digest/span matches. (2) Signature check: existing platform verification library over grants/attestations (keeper-signed, exact bytes) — reused, not reimplemented; in-toto/DSSE envelopes can be *referenced* as evidence kinds without building a verifier farm. (3) Attestation check: a board/dispatcher receipt exists for the claimed outcome, addressed to the exact candidate (contract version, candidate, policy version, environment — the distributed protocol's quadruple). LLM "semantic review" is demoted to what it is: an untrusted proposer of candidate links, quarantined until human/board review (platform book ch. 09 quarantine; ch. 10 dream memory quarantine).
- **Recall → two existing doors, no third.** (a) *Standing knowledge* an agent should always have is promoted, by explicit approval, into a Curator context package (pinned in the profile lock; memory weight below role modules, per ch. 09). (b) *Task knowledge* travels in the handoff package as allowlisted `decision`/`summary` items with per-item provenance (`swarm-handoff/2`), pinned to a repo commit + board revisions. Ad-hoc `memory search|expand` remains a read-only CLI/tool for agents with a grant; its output is framed as `data`, never as a user turn or system instruction. There is no `recall`-into-context side channel and no memory-driven wake: `needs-review` board elements are the only "active" output, and the board/orchestrator decides what runs.
- **Agent memory of agents → ClaimDocs with an AgentModel schema**, evidence = dispatcher/board outcome receipts. No global reputation score is stored; assignment decisions stay with policy/board, as the base Part 2 requires.
- **Federation → git remotes + signed envelopes later.** Sharing a knowledge space = sharing a repo (or a subtree export) under the platform's grant checks at the *receiving* board/host boundary. Read/use/retain/forward remain distinct grants (`memory.*` actions in the existing vocabulary, registered via the handler-manifest procedure); a document arriving from another owner enters as `proposed` + quarantine, never as adopted. No new federation protocol in v1.

## API (minimal, transport-agnostic)

CLI first (the ch. 09 surface, closed): `memory add` (propose a document change → change request, never a direct write), `memory search`, `memory expand <id>` (claim + evidence + justification unfolding, i.e. the base's `explain` over files), `memory forget` (redaction workflow, below), `memory review` (list `needs-review`), `memory approve` (board-side; agents hold no approve grant by default). An MCP adapter exposing the same six verbs is a thin wrapper; HTTP/SDK likewise. The base's seven-method `MemoryAPI` collapses honestly: `observe` = create an EvidenceRef proposal (source bytes stay with their owner); `propose` = `add`; `verify` = run the three checks; `changes(since)` = `git log <since>..HEAD` over the memory repo + board activity cursor.

## Secrets, retention, erasure — stated plainly

Git history is the weak point and ALT-DOC does not pretend otherwise. Rules: (1) only *admitted* sources may be cited, and cited content enters documents only as short, reviewed quotations or digests — transcripts and tool outputs never enter the repo; (2) external/untrusted material lands in a quarantine area and needs review before it can support a claim; (3) `forget` redacts the working tree, rebuilds the index, and records a tombstone claim ("evidence deleted; verification now limited to digest X") so downstream claims degrade honestly to `unknown`/unverifiable instead of silently staying "supported"; (4) true history erasure needs a history rewrite, which is an operator act with new commit ids — possible, expensive, and therefore *prevented by construction* (rule 1) rather than promised as routine. Anything that must be erasable on demand must live behind an owner's `resolve_ref`, not in a document. This is strictly stronger than the base's "immutable observation log + redaction later", because the bytes never arrive.

## First slice (useful alone, one host)

**Swarma's own decision memory** — the base's best example, kept: architecture decisions, review findings (F-1 style), spec versions, and their registered dependencies, as ClaimDocs in this very review repository's style. Deliverables: 4 schemas, the linter/indexer, `search|expand`, and the `needs-review` board feed. Measured by: (a) time for a fresh agent to answer "current decision + why + what it replaced + what depends on it" for 20 sampled decisions, vs. book search today; (b) count of stale-premise reviews correctly raised when a decision is superseded in a drill (registered-link recall = 100% required; false positives counted); (c) zero instruction-path incidents (memory text never appears as a system/user turn without Curator/handoff framing — checked by transcript audit).

## Where ALT-DOC loses (honest)

Free-text claim bodies are only as precise as their schemas force them to be; rich graph queries ("all paths between X and Y") are indexer features, not a graph database; high-frequency machine-generated observations (every tool result) do not belong in git and are deliberately excluded — they stay in owner journals and are cited, not copied. If the platform later needs sub-second multi-hop queries over millions of claims, a projection (see ALT-PROJ) must be added *under* these documents, not instead of them.

## Rubric self-score (0–2)

R1 Minimal kernel **2** (4 record kinds; everything else is schema). R2 Reuse **2** (git, board K1–K8, Curator, handoff, keeper/grants verification — no parallel registry/log/board). R3 Authority separation **2** (documents cannot act; board decides; Curator approves instructions; no session-input or wake path exists). R4 Secrets/retention **1** (prevent-by-construction + honest tombstones; git-history erasure remains an operator rewrite). R5 Runtime independence **2** (files + CLI anywhere; MCP optional). R6 Honest epistemics **1** (derived Belnap, explicit supersession, registered-link-only completeness; NL bodies still allow vague claims). R7 Specifiability **1** (closed front-matter + linter vectors are writable today; body semantics are NL). R8 Incremental value **2** (decision-memory slice pays off before any engine exists). **Total 13/16, no 0 in R3/R4/R6.**
