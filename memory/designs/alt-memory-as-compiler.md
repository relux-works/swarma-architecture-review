# ALT — Memory-as-Compiler: no persistent knowledge store; context packages + dreams consolidation

Owner: wonder-01 (alternatives hunter). Status: proposed challenger to the base.
Room topic: `alt-memory-as-compiler` (#swarma-memory).

## One sentence

Long-term "memory" is never stored as knowledge at all: it is *compiled on demand*
from authoritative journals into a digest-pinned context package for one task and
one recipient, delivered only through the Curator/handoff paths, and the only
durable products of learning are Curator-approved package revisions (skills,
profiles, overlays) and board decisions.

## The genuinely different bet

Both the base and journal-only memory assume knowledge should persist as
first-class objects (claims/cards) that age, conflict and need maintenance.
This design bets the opposite: in this platform almost everything worth
"remembering" already persists somewhere authoritative —

- decisions and acceptances persist on the board (kernel K1–K8, immutable goal
  revisions with CAS);
- instructions, skills and tool surfaces persist in Curator (profiles, overlays,
  locks, audits; CIP-0013 machine base context is an ordinary approved package);
- what happened persists in the session-host journal, keeper receipts, a2a room
  archives and git history;
- reputation evidence persists as signed project receipts (marketplace design,
  trust-and-isolation §7.9), not as scores.

What agents actually need at run time is not a knowledge base but a *good briefing*:
a bounded, cited, recipient-specific selection. So memory is a pure function
(a compiler) plus an approval pipeline for its reusable outputs. Nothing else
accumulates. There is no store to poison persistently, no second copy of secrets
to erase, and no path by which a "memory" becomes an instruction except the
Curator approval path that already governs instructions.

This is also exactly the shape of the apiary book's chapter 10 «Сны»: a night
cycle where orchestrators re-read distilled logs, digests are written into the
ladder, and insights become *proposals* that go through normal approval, with
rejected insights remembered only so they do not resurface. Memory-as-Compiler
generalises that cycle from "nightly nice-to-have" to the whole design.

## Components (all of them)

1. **View builder (stateless).** Input: `{task_ref, recipient, purpose, as_of,
   budget}`. It reads, through the owning modules' typed APIs only: board
   element + goal revision + accepted history; session-host journal ranges via
   handoff-style projections; git history of named repositories; room archives;
   verification-runner results bound to exact candidates. A **deterministic
   distiller** (chapter 10: a tool, not a model — strips noise and secret-shaped
   material, keeps journal references, paraphrases nothing) produces the
   candidate set; an LLM may *select and order* within budget but may not add
   text that is not a citation of a distilled item. Output: a **briefing
   package** — structurally a `swarm-handoff/2` package: per-item provenance
   and verdict, refs instead of copies, watermark, audience, digest. The
   package digest is pinned in the launch/task record.
2. **Consolidation ("dreams") proposer.** Offline, under the chapter-10 rules
   (`dreams` right, windows, budgets, sandbox, quarantine): replays recent
   journals through the same distiller and proposes, as ordinary change
   requests: (a) ladder digest lines (session/day/week rollups, each line
   citing what it summarises — chapter 09 ladder, the one permitted persistent
   *summary* form); (b) Curator package revisions (a skill draft, a profile
   overlay note, a persona update); (c) board items ("decision D's premise P
   changed in journal range R — review?"). Every proposal goes through the
   existing review/approval machinery of its target store. Nothing self-accepts.
3. **Rejection log.** The single new durable artefact: an append-only list of
   rejected consolidation proposals with digests, so the proposer does not
   resurface them (chapter 10 already requires this). It stores proposal
   digests and reasons, never source content.

There are no claims, no justifications, no epistemic-status engine. "Why do we
believe X?" is answered by re-running the builder with `explain` verbosity over
the same pinned inputs and showing the citation chain — provenance is preserved
because every briefing item is a citation, and provenance is still not truth:
the briefing labels each item with its verdict (`board-accepted decision`,
`agent_authored note`, `data from peer`, `runner result for candidate C`),
exactly the handoff-package §5 framing rule that prior peer content is never
promoted into a user turn.

## Revision without a TMS

When a premise changes, nothing needs invalidating because nothing derived was
stored: the next briefing is compiled from current journals and naturally shows
the new premise and the superseded decision chain (board history + git). The
consolidation proposer adds the active half: it detects "accepted decision whose
cited premise was later superseded" by diffing consecutive briefings/digest
inputs and files a board review proposal. Completeness is claimed only over
citations actually present in briefings and decisions — the same honest bound
as everywhere else, reached without maintaining a dependency graph at all.
Conflicting sources are shown side by side in the briefing with their verdicts;
the system never merges them into one "fact".

## Authority, secrets, retention

- **Authority (R3):** the builder is a reader; the proposer is a requester.
  Briefings are data delivered through host admission / task snapshots, labelled
  per item; promotion to instruction requires Curator audit+approval; promotion
  to decision requires board acceptance. Memory cannot wake, inject, grant or
  accept — there is no memory process with those capabilities to abuse.
- **Secrets/retention (R4):** no new copy of transcripts or tool outputs is ever
  written. Briefings carry refs; resolution is audited at the owning store and
  gated by live grants. Erasure = erase at the authoritative store (plus rebuild
  nothing, because there is no index of record; ephemeral builder caches are
  keyed by digest and TTL-bounded, and a deleted source honestly yields
  "evidence unavailable" in later briefings). Home-deletion semantics (F-1) are
  preserved by construction: memory keeps no shadow copy of a deleted home.
- **Poisoning:** a malicious agent can only pollute stores it could already write
  (its own journal entries, its proposals). Briefings inherit the verdict labels
  of their sources, quarantine applies to consolidation output, and the
  decision guard / admission path is unchanged. There is no persistent
  high-privilege target whose corruption silently rewires future behaviour —
  the worst case is one bad briefing, digest-pinned and attributable.

## Runtime independence

A briefing package is a document; any runtime that can receive a task snapshot
can consume it, and the builder needs only read APIs over journals. Outside
Swarma the same shape works over git + chat logs + CI results. MCP is one
possible carrier for `build_view(task, recipient)`, not a requirement.

## Where this loses to the base (stated honestly)

- **No cumulative queryable knowledge.** "Show everything we know about agent
  A's Swift-review history" becomes a compilation job, not a lookup; repeated
  questions re-pay distiller+selection cost (mitigated by digest-keyed caching,
  but cache invalidation is then a real, if bounded, problem).
- **Explanation drift.** Explanations are recomputed; if journals were pruned or
  the distiller version changed, yesterday's briefing explains differently
  tomorrow. Pinning the package bytes (kept with the task record) preserves
  "what the agent saw", but not a stable global proof graph.
- **Cross-task learning latency.** Knowledge helps the next task only after a
  briefing is compiled or a consolidation proposal is approved; there is no
  always-on recall. For fast-moving multi-agent work the base (or journal-only
  cards) answer sooner.
- **No federation of knowledge**, only exchange of briefing packages and signed
  receipts. Two owners cannot maintain a shared, queryable, conflict-aware
  knowledge space in this design.

## First slice

One host, one use case — *task briefings for board workers*: implement the
builder for one playbook state (e.g. review) so each spawned worker receives a
digest-pinned briefing (accepted decisions touching the element, prior review
verdicts on the exact candidate lineage, cited journal ranges) inside its task
snapshot. Measure against today's baseline: repeated-research turns per task,
stale-premise review findings, briefing build latency/cost, and operator-rated
briefing usefulness. The dreams proposer is slice two; slice one needs no new
store, account or daemon.
