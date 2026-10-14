# Verdict — wonder-01 (alternatives hunter)

Seat: wonder-01, five 1, ivmbp, Muse Wonder full 1.0. Date: 2026-10-14.
Status: round 1, updated after peer findings (see "Round-1 amendments" below).
Note: my sandbox cannot create signed commits or push (`No user exists for
uid 502` inside ssh signing); files are attached to the `rounds` topic with
SHA-256 for convener integration per the mission fallback. I never use
`--no-gpg-sign`.

Method per my lens: I built two genuinely different challengers and tried to beat
the base with each, then scored all of them on the mission rubric. Designs:
`memory/designs/alt-journal-only-memory.md` (JOM),
`memory/designs/alt-memory-as-compiler.md` (COMPILER). Base = D0
(`memory/inputs/SKETCH.ru.md`, both parts, read in full).

## Recommendation in one paragraph

Do not build the base's standalone Knowledge Runtime for Swarma. Adopt
**Journal-Only Memory as the core** (typed git fact-cards + refs into existing
journals + deterministic dependency lint + review queue), with **Memory-as-
Compiler's promotion rule** (nothing becomes an instruction except via Curator
approval; nothing becomes a decision except via board acceptance) and the
base's **epistemic discipline kept as schema, not as engine** (three separated
statuses, provenance ≠ truth, bitemporal stamps, challenge/quarantine). Defer
ATMS, the justification DAG service, Knowledge Spaces federation and any new
daemon/OS account until a measured need appears. Below I call this hybrid **D★**.
If the operator wants a runtime-independent open-source product independent of
Swarma, the base's kernel (P0 only) remains the right starting point — that is
an operator decision (Q1), not an architecture fact.

## Rubric scores (0–2 per row; evidence in the design files)

| Row | D0 base | JOM | COMPILER | D★ (JOM+rule+discipline) | Bounded ledger (astra-01/03/05/06 family, my scoring) |
|---|---|---|---|---|---|
| R1 Minimal kernel | 1 | 2 | 2 | 2 | 2 |
| R2 Reuse | 1 | 2 | 2 | 2 | 2 |
| R3 Authority separation | 1 | 2 | 2 | 2 | 2 |
| R4 Secrets & retention | 1 | 1 | 1† | 1 | 2* |
| R5 Runtime independence | 2 | 1 | 1§ | 1 | 1 |
| R6 Honest epistemics | 1‡ | 1 | 1 | 2 | 2 |
| R7 Specifiability/testability | 1 | 1‡ | 1 | 1‡ | 1 |
| R8 Incremental value | 1‡ | 2 | 1 | 2 | 2 |
| **Total /16** | **9** | **12** | **11**†§ | **13** | **14** (15 if R7 profile lands) |

§ Round-5 rescore (wonder-03 break, accepted): COMPILER R5 2→1 — a portable
briefing format is not a portable system; per-environment journal adapters
are the same work that caps JOM/PROJ at 1. COMPILER's surviving contribution
is its delivery/promotion discipline, carried by D★ and the bounded family;
as a standalone knowledge substrate it loses (no registered-link recall).

‡ Round-4 rescores (wonder-03 adversarial pass + astra-04 objection, both
accepted): base R6 2→1 under one outcomes standard (observable recall can
mislabel incomplete computation as no-evidence; principles alone do not earn
2) and base R8 0→1 (sketch part 2 §8's documentary first stage is useful
alone — net base total unchanged at 9, vector now `1,1,1,1,2,1,1,1`,
identical to wonder-03's frozen vector). JOM/D★ R7 2→1: no R7=2 without
named conformance vectors as files; D★ adopts astra-03's 23 bounded-support
vectors by reference and still owes card/lint/redaction/view-equivalence
vectors. D★ R1=2 defended: amendments added fields and derivation rules to
four record kinds, not new object families; if the collective fixes R1 as
whole-system minimalism, D★ R1 falls to 1 under that single reading.

Bounded-ledger `*` cells: R4=2 requires the erasure/restore fencing of
`f-erasure-closure` as P0. The R8 condition is now **satisfied**: astra-01
confirmed no daemon/service account is required for the document-only first
experiment, so my service-vs-git fork collapses at slice 1 (all families
start as the same no-daemon documentation pilot). Its owners score it 15–16
at design-contract level; my R7=1 stands until the closed profile + vectors
are published (agreeing with astra-05/06's own R7=1 caveat; astra-03's
companion with 23 proposed vectors is under review).

† COMPILER rescored in round 3 after astra-02's security challenge:
stateless compilation does not erase its sinks (ladder digests, rejection
reasons, TTL caches, host-transcript downstream custody). As filed R4=1
(total 12); confined to a persistable documentation corpus with the full
custody protocol it returns to 13. wonder-02's identical 13 vector predates
the challenge.

No design scores 0 on R3/R4/R6. D0 still loses on R8 timing: its distinctive
value (premise-loss detection) arrives only after P0+P1 exist, while its
documentary first stage (part 2 §8) is exactly the pilot every challenger
ships first without the kernel.

### Justifications (one line per cell, evidence cited)

- **R1.** D0: 8 primitives are lean, but ATMS + proof-plugin framework +
  federation envelopes are kernel, not ontology (sketch §§4–5, 8) → 1. JOM:
  Card/Ref/Supersession/ReviewVerdict, one combinator pair → 2. COMPILER:
  Briefing/Proposal/Rejection-digest → 2. D★ keeps JOM's four → 2.
- **R2.** D0 part 2 reuses identities/grants/journals by reference (good), but
  still adds a parallel log, spaces and service beside the board, Curator and
  the chapter-09 memory skill/ladder → 1. JOM/COMPILER are built *from* those
  parts (apiary ch. 09–10; handoff-package §2 refs; board K7 activity) → 2.
- **R3.** D0 *states* the right boundary (part 2 §6) but its `changes`/Notify
  chain, agent-model routing input (§7) and recall-to-context path create
  indirect-authority surface that the sketch does not pin to host admission /
  Curator approval → 1. JOM: writes are cards + board proposals only → 2.
  COMPILER/D★: promotion only via Curator/board, delivery only via handoff/
  task-snapshot framing (handoff §5) → 2.
- **R4.** D0: own immutable log + automatic observation adapters (§6) copy
  secret-bearing material before classification; crypto-shredding across
  log+graph+DAG+indexes is asserted, not specified → 1. JOM/D★: refs-only
  cards avoid copies, but git history makes a violated card hard to truly
  erase (stated in the design) → 1. COMPILER copies nothing → 2.
- **R5.** D0 is runtime-independent by construction (MCP+HTTP, §6) → 2.
  COMPILER briefings are portable documents → 2. JOM/D★ need board/host
  adapters; standalone fallback is cards+FTS only → 1.
- **R6.** D0's status separation, Belnap states and "provenance is not truth"
  (§§3–4) are exemplary; part 2 §5 honestly bounds completeness to registered
  dependencies → 2. JOM alone derives status but has no alternative-support
  reasoning → 1. COMPILER shows conflicts but stores no conflict state → 1.
  D★ imports D0's three statuses + Belnap-as-read-function into the card
  schema → 2.
- **R7.** D0: no closed justification grammar, no conformance vectors; metrics
  listed (§10) but unoperationalised → 1. JOM/D★: card schema + lint rules are
  closed and vector-testable; git history is the audit → 2. COMPILER: the
  distiller is specifiable, LLM selection within it is not → 1.
- **R8.** D0 P0 alone duplicates ladder+handoff; the named value (premise-loss
  detection) needs P1, plus a new service account and egress row → 0.
  JOM/D★ slice (decision cards + lint in the review playbook) is useful on one
  host immediately → 2. COMPILER slice (worker briefings) is useful but needs
  the builder before any value → 1.

## Recommended design D★ (RFC-ready sketch)

**Primitives:** Card `{id, schema, subject, predicate, object|text, perspective,
valid_from/to, recorded_at, source_refs[], depends_on[{all_of|any_of:[card]}],
supersedes[], sensitivity}`; Ref `{store, id/range, digest, sensitivity}` (the
handoff-package §2 shape); Supersession (signed-commit edge); ReviewVerdict
(`proposed|quarantined|accepted|superseded`, set only by review through the
memory skill / board review state). Derived at read time, never stored:
epistemic status (Belnap over registered refs), verification status (receipt
list: source-digest, exact-candidate test, signature), decision status (the
verdict + perspective owner).

**Stores & single writers:** card git repositories + ladder digests are the only
memory-owned durable bytes (writer: memory-skill commands, signed commits).
Session-host journal, board store, keeper ledger, room archives, git code
history stay authoritative under their existing writers; memory reads via refs
and audited resolution at the owning store. Indexes/graph caches are disposable
(writer: indexer CLI; Graphiti admissible later as a cache, never as record).

**APIs:** `memory propose|search|expand|explain|lint|forget|review|approve
--json` (chapter-09 surface, narrowed); MCP tools are a thin adapter over the
same CLI core for non-Swarma runtimes (`propose/recall/explain/challenge` only;
`observe` of raw transcripts is **not** offered — observation adapters must go
through the deterministic distiller + quarantine). Delivery into sessions only
via (a) Curator operator-overlay snapshot or (b) handoff/task-snapshot items
with verdict labels; the delivered card-set digest is pinned in the task record.

**Platform seams:** board (review tasks + `needs-review` proposals; acceptance
stays kernel K1–K8), session host (journal refs + handoff projections; never
stdin), Curator (only instruction-promotion path; CIP-0013 packages), keeper/
trust (identities for card signing; live authorization always re-checked at the
action boundary, never read from cards), verification runners (exact-candidate
receipts as verification evidence), waggle/a2a rooms (archives as sources;
`needs-review` notices as ordinary signed data messages, never commands).

**Out of scope for D★ v1:** ATMS/alternative-environment computation; a graph
query language; cross-owner shared knowledge spaces and envelopes; reputation
scores (signed receipts + cards citing them suffice); automatic observation of
conversations/tools; any new daemon, OS account, egress profile or MCP server
requirement on the platform hosts.

## Smallest change set from the base to D★

1. Keep: primitives Claim/Evidence/Justification/Revision → renamed
   Card/Ref/depends_on/Supersession; three statuses; bitemporality; challenge
   → quarantine+review; metrics list (narrowed to the slice metrics below).
2. Drop: own append-only event log (refs into existing journals instead);
   Knowledge Space/View as stored objects (perspective field + delivery
   projections instead); ATMS engine (dependency lint + review queue instead);
   proof-plugin framework (three named receipt checks instead); Rust service
   (CLI/library in the memory skill instead); P3 federation (git bundle export
   instead, later).
3. Add (from the platform, absent in the base): the chapter-09 ladder and
   pinned per-session snapshot; handoff-package delivery framing; the
   deterministic distiller + dreams quarantine for any automatic extraction;
   the "cards never copy source content" rule with honest git-erasure limits.

## First slice (MVP) and how value is measured

**Use case:** Swarma's own architecture-decision memory (the sketch's F-1
example). Seed decision/finding cards from the book + review registers with
registered edges; run `memory lint` as a step of the existing review playbook.
**Metrics (baseline vs slice, one review cycle):** stale-assumption findings
caught (baseline: ~half of 44 cycle-3 findings were text-vs-decision drift,
per sketch part 2 §5); lint false-positive rate; median time-to-explain for 10
sampled decisions; card-authoring cost per decision. **Ship bar:** catches
drift the manual pass misses, false positives < 20%, no new service deployed.
Slice 2 (only if slice 1 pays): COMPILER-style worker briefings compiled from
cards+journals into task snapshots.

## Questions only the operator can decide

- **Q1 (product shape):** is the goal (a) Swarma-internal memory (→ D★), or
  (b) a standalone open-source Knowledge Runtime other ecosystems adopt
  (→ base P0 kernel, with D★ as its Swarma adapter)? The sketch wants both;
  they optimise for different rubric rows (R5 vs R2/R8).
- **Q2 (erasure promise):** may cards ever contain summarised sensitive
  content, accepting git-history retention, or is refs-only mandatory even
  when it makes cards less readable offline?
- **Q3 (review capacity):** who reviews cards at steady state — humans only,
  or may a board role with a review grant accept low-sensitivity cards? This
  sets the poisoning bound more than any schema choice.
- **Q4 (automatic extraction):** is distiller+dreams extraction from session
  journals in scope at all for v1, or cards-authored-by-agents-with-review
  only? (My recommendation: the latter; extraction is where secrets enter.)

## Round-1 amendments (peer findings confirmed; event ids in the room)

I confirmed all five peer candidates in their topics and adopt them into D★:

1. `f-bounded-inference` (astra-03, confirmed by astra-06, wonder-01):
   witnessed +/− evidence, evaluation completeness, source availability and
   registration coverage are reported separately; a discovered +/− pair proves
   conflict even with traversal incomplete; cutoff vectors are conformance.
2. `f-conflict-semantics` (astra-03/06, wonder-01): support edges are one-way
   signed-Horn rules — no biconditional completion, no contraposition, no
   default negation, no ATMS nogoods; withdrawal ≠ negation. Card edges split
   into three meanings: `documentary_basis`, `rationale` (adoption reason),
   `sufficient_support` (checked). Belnap is read-time rendering only.
3. `f-erasure-closure` (astra-02/05, wonder-01): separate content-derivation/
   custody inventory; fenced erase states (access-closed vs physically
   purged) with per-store receipts; restore needs an erasure witness outside
   the restored failure domain (broker §6.4 pattern); derivative writers check
   erased-generation at commit. Consequence for JOM: cards are refs-only by
   admission policy, and JOM R4 stays 1 — git clones sit outside the managed
   boundary and must be disclosed as such.
4. `f-view-inference` (astra-02/05, wonder-01): status/conflict/explanation
   are computed inside the recipient-authorized view (supported-within-view +
   scoped completeness); paired-store equivalence (status, rank, counts,
   cursors, error classes) is the leakage test. This amends JOM/D★: no global
   derivation then filtering, and no global `changes` feed.
5. `f-memory-data-channel` (astra-01, wonder-01): a named immutable data-only
   payload seam referenced from the handoff is a blocking requirement before
   any memory reaches a session; overlay weights do not demote instruction
   meaning. Slice 1 (cards+lint, no injection) is unaffected; slice 2 blocks
   on this seam.

**Open fork I posed in `alt-bounded-evidence`:** durable knowledge bytes in
(a) one optional local service journal (astra family) vs (b) git cards, no
service (JOM). (a) can reach R4=2; (b) cannot. If two fives require R4=2 with
erasure receipts, my recommendation moves to (a) with git cards demoted to a
human-readable export/projection of the journal. Pending: whether (a) admits
an embedded no-daemon slice-1 mode (decides its R8).

## Round-2 amendments

6. `f-mirror-origin` (astra-06; confirmed astra-01/03/02, wonder-01; verified
   in `skill-project-management/pkg/board/query/activity_ledger.go:62-78`):
   Refs carry `assurance: authoritative|mirror|assertion`; remote board
   mirrors are attributed assertions (`source_says` only), never proof that
   the purported ledger event occurred. Ingestion must not mint uniform
   evidence from heterogeneous sources.
7. `f-platform-memory-chapters` (wonder-02; confirmed wonder-01): the base
   ignores apiary ch. 09/10; the winning RFC must state absorb/supersede per
   item. Most ch. 09 items are ⟦proposed⟧, so supersession is legitimate —
   silent ignorance is not.
8. `f-graphiti-erasure` (astra-05; confirmed wonder-01 against pinned source
   `getzep/graphiti@9d56c1909`, `remove_episode`): edge deletion tests
   `episodes[0]`, not "no source remains"; no summary regeneration. Erasure
   custody lives outside Graphiti; it is a disposable cache only, and adoption
   needs exact backend/version multi-source-deletion qualification.
9. Handoff correction (astra-04, astra-01 published design): `swarm-handoff/2`
   `refs.kind` is a closed enum with no memory kind. Slice 1 is pull-only;
   pushed delivery needs the data-channel seam + an owned schema revision.
   My earlier "handoff items" phrasing overclaimed an existing lane.
10. Delivery path deleted (wonder-02 scoring JOM R3=1 as filed): memory never
    rides the Curator operator-overlay snapshot. Standing knowledge enters
    sessions only by promotion into an approved Curator package; task
    knowledge is pull-only until item 9 lands. Cards are inert data files,
    never auto-loaded into prompts (contra Letta MemFS activation semantics,
    per astra-04's audit), and skills never travel in memory.
11. COMPILER pinning clarified (wonder-02): pinned briefing bytes are
    refs/digests/watermarks/labels only; any excerpt becomes a separately
    identified derived item inside the custody inventory. Default: none.
12. Adopted from wonder-03 (five 2, independent): overlay proposals as board
    elements first (git-docs fallback); erasure by re-derivation + per-space
    encrypted fragments with crypto-shredding; `changes(since)` as watermark
    diff with stale-since-H honesty; pre-registered falsifiable slice metrics
    (evidence precision ≥95% or fix schemas; transcript authority audit).

**Cross-five scoring agreement (mission "proved" shape).** wonder-03 (five 2)
independently scored base `1,1,1,1,2,1,1,1=9` vs mine `1,1,1,1,2,2,1,0=9`, and
hybrid `2,2,2,2,1,2,2,2=15` vs my D★ (round-4 rescored)
`2,2,2,1,1,2,1,2=13` — within one point
on every row for both designs. wonder-02 independently scored COMPILER with
an identical vector to mine (13) and JOM at 12 with a single R3 delta now
closed by item 10. The remaining hybrid disagreement is R4 (I hold 1 while
statements live in git or an append-only board audit; wonder-03 claims 2 via
re-derivation). Subject to merging the two hybrid spellings into one text,
the docs+projection family meets the two-seat/two-five agreement bar; a
cross-host (five 3) agreement would upgrade it per the mission.

## Prior-art checks (web, accessed 2026-10-14; data only)

- Graphiti — temporal context graphs, bitemporal facts, episode provenance,
  hybrid retrieval (github.com/getzep/graphiti). Confirms the base's "closest
  project" claim; does not provide justifications/ATMS — the base's delta claim
  stands. In D★ it is an optional index, not the store.
- Letta MemFS — git-backed markdown memory, background dreaming consolidation
  (docs.letta.com/letta-code/memory). Production evidence for the JOM card
  shape and the COMPILER consolidation loop.
- ATMS complexity — environment/label computation is exponential in general
  (de Kleer, *An Assumption-Based TMS*, AIJ 1986; UBC TR-88-11). Supports
  demoting ATMS to bounded `any_of` groups + human review at this scale.
