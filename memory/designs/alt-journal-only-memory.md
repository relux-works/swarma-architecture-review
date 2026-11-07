# ALT — Journal-Only Memory (JOM): memory as projections over existing journals + git fact-cards

Owner: wonder-01 (alternatives hunter). Status: proposed challenger to the base.
Discussion: journal-only memory alternative.

## One sentence

There is no `swarma-memory` service, no second event log and no graph store:
durable memory is only typed fact-cards in git (the apiary memory skill's ladder),
and everything else is a rebuildable read-only projection over the journals the
platform already owns.

## Why this can beat the base

The base (SKETCH.ru.md) builds a universal Knowledge Runtime: own append-only log,
typed knowledge graph, justification DAG, ATMS, proof plugins, Knowledge Spaces.
In Swarma that duplicates three things that already exist:

1. The apiary book chapter 09 «Память» already specifies a memory skill:
   `memory add|search|expand|forget|review|approve`, git-backed store by default,
   per-note provenance, daily write budget, quarantine for external sources, and a
   multi-level ladder (Level 0 journals → session/day/week digests → fact-cards),
   with a per-session pinned snapshot and "this is not instructions" weight.
2. The session-host journal, board activity (K7: every mutation writes an audit
   row in the same transaction), keeper custody/ledger, a2a room archives and git
   history are already authoritative, single-writer journals.
3. `swarm-handoff/2` already defines how derived knowledge crosses a boundary:
   a projection at a committed watermark for one recipient, allowlist fields only,
   per-item provenance and verdict, secrets staying in protected source storage,
   and audited `resolve_ref` gated by grant and clearance.

JOM says: memory should be a *reader and indexer* of those journals plus a narrow,
human-reviewable write surface (cards), not a new writer of record.

## Primitives (the whole kernel)

Four primitives. Everything domain-specific is frontmatter ontology, as in the base.

1. **Card** — one markdown file in a git repository (per project `memory/`, or the
   apiary `~/apiary/memory/`): `{id, schema, subject, predicate, object|text,
   perspective (principal), valid_from/to, recorded_at, source_refs[], depends_on[],
   supersedes[], sensitivity}`. A card is a claim, but it carries no authority.
2. **Ref** — `{store, id/range, digest, sensitivity}` pointing into an authoritative
   store (session-host journal seq, board element/revision, git commit, room event,
   keeper receipt, verification-runner result). Cards reference evidence; they never
   copy it. This is the handoff-package §2 `refs` pattern reused verbatim.
3. **Supersession** — an explicit `supersedes` edge written by a named principal in a
   signed commit. There is no other way for knowledge to "change": old cards stay,
   marked superseded by the new card (bitemporal: `valid_*` vs `recorded_at`/commit time).
4. **Review verdict** — card lifecycle state derived from review, not stored as a flag
   the author sets: `proposed → quarantined|accepted → superseded`. `accepted` means
   "a named reviewer (human or role with a board review grant) accepted this card as a
   working statement for perspective P" — the base's decision status. Epistemic status
   is *derived at read time* from refs: supported / refuted / conflicted / unknown
   (Belnap lattice as a read-time function over registered refs, never a stored flag).
   Verification status is the list of verifier receipts reachable via refs
   (source exists+digest matches; test result bound to exact candidate; signature valid).

Justifications are card-to-card `depends_on` edges with one closed combinator set:
`all_of` (default) or `any_of` groups. That is the entire "justification language".
There is no ATMS: ATMS environment computation is exponential in the number of
assumptions in general (de Kleer 1986; complexity results surveyed in UBC TR-88-11),
and in this platform the alternative-support case is rare and human-decided anyway
(board acceptance). Instead, a deterministic **dependency lint** walks `depends_on`
from every newly superseded card and marks registered dependents `needs-review`,
opening board review tasks as *proposals* (goals contract: outcomes are proposals;
the board/kernel decides). LLM-found *implicit* dependencies are only lint
candidates, labelled `suggested`, never edges. Completeness is claimed only over
registered edges — the same bound the sketch's part 2 already accepts.

## Stores and single writers

| Store | Writer | Memory's role |
|---|---|---|
| Session-host journal + transcripts | session host | read via refs; content via audited `resolve_ref` only |
| Board elements, goals, activity, audit (K1–K8) | board kernel | read; memory files review-task proposals through the normal board API |
| Keeper ledger / receipts, grants, identities | keeper / trust layer | read refs only; never consulted for live authorization |
| Git card repositories + ladder digests | memory skill commands (`memory add/review/approve/forget`), signed commits | the *only* durable memory-owned bytes |
| Search/FTS/embedding indexes, dependency graph cache | indexer (memory skill) | disposable; rebuildable from journals+cards at any time; never cited as evidence |
| Curator profiles, overlays, machine base context (CIP-0013) | Curator + operator approval | injection path only (see below) |

No new OS account, no new egress row, no new daemon. The indexer is a CLI/library
run by the agent that needs it (or by the night-cycle dream session, chapter 10),
which keeps memory an optional client like the board itself (swarma book ch. 13).

## API (CLI first, MCP as an adapter)

The apiary chapter-09 commands, narrowed to a closed grammar:

- `memory propose --card <file>` → validates schema, checks every `source_ref`
  resolves and its digest matches, writes card as `proposed` (or `quarantined` if
  any source is external/untrusted), commits signed. Never writes `accepted`.
- `memory search <query> [--as-of T] [--perspective P]` → cards + ladder lines with
  derived epistemic status, conflicts shown, never hidden. Unknown stays unknown.
- `memory expand <id>` → follows refs one level down the ladder (card → digest →
  journal range), each hop re-checking the caller's grant/clearance at the owning
  store (check where the action happens, trust-and-isolation §1.4).
- `memory explain <card-id>` → the `depends_on`/`supersedes` chain + verifier
  receipts, rendered from cards+refs. No stored proof object to go stale.
- `memory lint [--since <rev>]` → deterministic: broken/digest-mismatched refs,
  dependents of superseded cards, expired cards, cards whose verifier receipt no
  longer binds (e.g. test bound to an old candidate). Output: `needs-review` list.
- `memory forget <card-id> --reason R` → redaction commit (content replaced by a
  tombstone with digest of the redaction act) + index rebuild + a `source deleted`
  marker so dependents report "evidence unavailable", never a silent pass.
  *Limitation stated plainly:* git history retains the pre-redaction bytes on every
  clone; therefore cards must be refs-and-summaries only, and sensitive source
  material must never be copied into a card (handoff-package §1 rule 3). True
  erasure of a card that violated this rule requires history rewrite on all clones
  and is an operator act, not a memory feature.

## How memory reaches a session (never as an instruction)

Memory output enters a session only through paths that already exist:
(a) the Curator operator overlay snapshot (chapter 09: pinned per session, weight
below every role module, "not instructions"); or (b) items inside a
`swarm-handoff/2` package / task snapshot, with per-item provenance and verdict
labels preserved (`agent_authored`, `data`, `quarantine` excluded by default).
The exact card-set digest used is pinned in the launch/task record, so "what the
agent was told" is replayable. Memory has no path to session stdin, no wake, no
goal authorship (goals contract, D-GOALS), and no grant relevance: a card saying
"X usually approves this" is data; the action boundary re-checks live grants.

## Federation

Cards are files; sharing is git push/fetch of a shared card repository or an
exported bundle = cards + resolvable-ref metadata + sender signature (SSHSIG /
keeper identity). Read / use / retain / forward are still distinct rights, but
enforcement is honest: once exported, retention cannot be enforced — so export is
by perspective and sensitivity allowlist (handoff projections), and `restricted`
cards never leave `same_session`/same-owner. Independent owners keep different
perspectives on the same subject; there is no consensus over truth (distributed
consensus stays limited to deterministic predicates, as the sketch part 2 says).

## Off-the-shelf note (Graphiti / Letta)

Letta's MemFS (git-backed markdown memory with background "dreaming" consolidation,
accessed 2026-10-14: docs.letta.com/letta-code/memory) is direct evidence the
card+git shape works in production agent systems. Graphiti (temporal context
graphs: bitemporal facts, episodes with provenance, hybrid retrieval; accessed
2026-10-14: github.com/getzep/graphiti) is *not* needed as a store here, but is a
candidate *indexer/projection* behind `memory search` if graph traversal queries
outgrow FTS — adopted as a replaceable cache, never as the record. That keeps the
sketch's "Graphiti as swappable Knowledge Projection" idea without its service.

## Where JOM loses to the base (stated honestly)

- No multi-context ATMS reasoning: "C survives on (D∧E) though B died" is expressed
  only via `any_of` groups and resolved by a reviewer, not computed. If the
  platform later needs machine-checked alternative-support reasoning at scale, the
  base's justification engine wins and JOM must grow it.
- Cross-runtime standalone use degrades to "git cards + FTS" — still useful, but
  the base's single runtime-independent service API is cleaner for non-Swarma hosts.
- Query power is search+traversal, not a graph query language.

## First slice

On one host, for one named use case — *the architecture-decision memory of Swarma
itself* (the sketch's own F-1 example: "archive home by default" → "delete home"):
seed ~50 decision/finding cards from the book and review registers with
`supersedes`/`depends_on` edges, run `memory lint` in the review playbook, and
measure: (1) stale-assumption findings caught per review cycle vs the current
manual baseline ("almost half of 44 findings were text-vs-decision drift",
sketch part 2 §5); (2) false `needs-review` rate; (3) time-to-explain for a sampled
decision. Useful alone, blocks no platform gate, needs no new service.
