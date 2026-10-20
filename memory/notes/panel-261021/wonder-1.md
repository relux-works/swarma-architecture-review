# Panel answer: swarma-memory Q1–Q3

Scope note: I read the book chapter, `DECISIONS.md` (D-001…D-026), `OPEN-QUESTIONS.md` (esp. 8, 9, 20–23), `repo/docs/architecture.md`, the normative package (`kernel/semantics.md`, closed schemas, vector format), the implemented contracts (`git-spaces.md`, `signing-policy.md`, `read-evaluation.md`, `disclosure-erasure.md`, `write-admission.md`, `cli.md`), the Go kernel/space code, and the platform book chapters on keys, grants and the board. Nothing below reopens a D-decision; where a proposal needs one changed, I say so. No decision change is needed for any of the three.

---

## Q1 (OPEN-23): Disclosure-filtered source payload in the view

### 1. Recommendation

**Disclosure-filtered source payload embedded in the view.** Not a separate source-read operation, and not CLI-side reconstruction (already rejected in OPEN-23, correctly: it would compute disclosure outside the kernel).

Extend each view item in `view.schema.json` (new package release, profile `0.2.8-draft`, URNs bumped per OPEN-18) with one new required field, keeping `source_refs` for compatibility:

```json
"sources": [
  {
    "ref":        {"id": "source:…", "version": 1},
    "owner": "…", "source_kind": "document|direct_declaration|publication|mirror|artifact",
    "object": "…", "revision": "…",
    "digest": {"algorithm": "sha256-cjson-v1", "value": "…"} | null,
    "provenance": "canonical|direct|imported|reported",
    "origin": "…", "original_issuer": "…", "carrier": "…" | null,
    "retention_admission": {"id": "…", "version": 1} | null,
    "availability": "available|unavailable|erased",
    "excerpt_state": "present|absent|withheld|unavailable",
    "excerpt": "…" | null
  }
]
```

Semantics, all computed inside the kernel at view time (K-AUTH-1: filtering before computation):

- The array contains exactly the sources in `source_refs` **after tightening `source_refs` itself**: today `collectSources` (in [evaluate.go](bundle/repo/go/kernel/evaluate.go:185)) appends justification `source` premises without an `allowed()` check. In 0.2.8 both `source_refs` and `sources` list only sources the query principal may see: `read`+`use`+`metadata` grants on the source record id for the query audience/purpose, plus `disclosureAllows(source, audience, purpose)` including lineage taint (K-DISC-1) and live declassification checks (K-DISC-2). A source failing this is **omitted entirely — no placeholder, no count**. That is what K-NI-1 requires: a withheld entry whose presence/absence varies with hidden state would leak exactly what the paired-store property forbids. The reader cannot distinguish "no source" from "withheld source"; `source_state` in the polarity record already carries the honest summary.
- `availability` is the **effective** state at the query cut, not the stored body field: stored `availability` overridden by the latest admitted `availability` revision ≤ cut, by `source_access` facts, and by erasure fences — the same computation as `sourceAvailable` (in [read.go](bundle/repo/go/kernel/read.go:339)), mapped as: resolvable → `available`; otherwise `unavailable`; fenced/erased payload → `erased`. This gives the promised `available / unavailable / withheld` trichotomy as `available / unavailable / omitted-withheld`, plus the erasure case the brief's list misses and K-ERASE-1 requires (source headers may survive with erased bytes).
- `excerpt_state`: `present` (excerpt disclosed, string in `excerpt`); `absent` (source record's excerpt is null — nothing to show); `withheld` (excerpt exists but disclosure/retain-derived constraints, field-class `sensitive`, or a fenced content-lineage input block it for this audience/purpose — locator fields still shown if the source itself is disclosed); `unavailable` (source unavailable or erased, so retained excerpt bytes are fenced per K-ERASE-1). Excerpt disclosure additionally requires that no transitive known content input of the source is fenced, mirroring the existing disposition logic in the read evaluator.
- `audience_projection`: unchanged redaction (K-DISC-2, `redact()` (in [projection.go](bundle/repo/go/kernel/projection.go:263))): `sources: []`, `source_refs: []`. A released conclusion never drags its session locator with it.
- Ordering: `sources` sorted by `(id, numeric version)`, deduplicated, identical ordering rule to `source_refs` (K-EVAL-9). Budget: resolving a disclosed source's effective availability costs the existing `source_resolutions` counter; hidden sources cost nothing and produce no cutoff (K-NI-1, K-AUTH-1).

Worked case (architecture §7.2, D-016): a decision citing a session source shows the reader `{runtime, session, message}` — carried today as canonical JSON in the source's `origin`, with `object = sha256:<raw digest>` and `revision = message id` per the CLI's session-excerpt convention — plus the retained excerpt when disclosable. After session deletion, an `availability` revision (or resolver fact) flips `availability` to `unavailable`; the record and its locator remain presentable, which is exactly the §7.2 promise ("the record stays, its source becomes unavailable").

### 2. Why

The view is the only disclosure boundary the kernel has (K-AUTH-1, K-NI-1); every consumer — CLI JSON, compact rendering, promotion — already flows through it. Embedding keeps the payload atomic with the witness evaluation that cites it: same cut, same authorized projection, same fresh handle, no second authorization decision that could disagree with the first. The CLI's closed output projection (in [cli.md](bundle/repo/docs/cli.md)) then just forwards the new field; its "Limitations" paragraph and the stage-3 interim in OPEN-23 are deleted.

### 3. Trade-offs and rejected alternatives

- **Separate `source_read` operation (rejected for v1).** Cleaner payload size control, but it needs its own query schema, cut/handle binding to a prior view, pagination, and a second non-interference surface ("does this source exist?" as an oracle). It also breaks atomicity: the source can be revised between `recall` and `source_read`. It remains a legitimate *later* addition for large excerpts; the view field does not preclude it.
- **Always show locator, gate only the excerpt (rejected).** [view-inference.md](bundle/design/findings/view-inference.md) is explicit: content locators, digests and source-author identities are protected outputs. A session id is a locator.
- **Placeholder `withheld` entries (rejected).** They leak the count and identity-adjacency of hidden sources and change with hidden appends, violating K-NI-1.

Cost accepted: views grow by the excerpt bytes of disclosed sources. Bounded by policy `max_field_bytes` per record already; no new limit needed in v1.

### 4. Changes needed

| Change | Where | When |
| --- | --- | --- |
| `sources` field + tightened `source_refs`; clauses K-EVAL-5a (payload disclosure) referencing K-AUTH-1/K-NI-1/K-ERASE-1 | package `view.schema.json`, `semantics.md`, URN/profile bump | **v1 (package 0.2.8)** |
| Kernel: build `sources` in item construction, reuse `sourceAvailable` + fence logic; `redact()` keeps it empty for audience projections | `go/kernel` | **v1** |
| CLI closed projection forwards `sources`; remove limitation note; SKILL line "readers see source refs, not the excerpt" updated | `go/cmd/memory`, `docs/cli.md`, `SKILL.md` | **v1** |
| Stage-3 gate scenario 11 re-asserted on locator + excerpt (unblocks TASK-261019-gak2ji) | e2e/CLI tests | **v1** |
| Standalone source-read operation for bulk excerpt export | package + kernel | later, only if measured need |

### 5. Tests and vectors

New semantic vectors (continuing the S-series), each also run as a paired non-interference pair per K-NI-1/K-VEC-2:

- **S43** positive: authorized reader, session source `resolvable` → locator + `excerpt_state: present`, excerpt bytes exact.
- **S44** unavailable: same corpus + `availability` revision → `availability: unavailable`, locator still shown, excerpt `unavailable`; witness/`source_state` unchanged in meaning (no manufactured opposition, K-EVAL-5).
- **S45** withheld/NI pair: two snapshots identical in authorized records, differing only in a hidden session source cited by a hidden justification. Normalized views byte-equal; `source_refs`, counts, cutoffs, `evaluation` all equal; hidden source consumes no `source_resolutions` budget.
- **S46** erased: source in erasure closure → header survives, `availability: erased`, excerpt null, no payload bytes anywhere in the view (forbidden predicates on the excerpt string).
- **S47** audience projection: released decision shows `sources: []` even though the private view of the same corpus shows the locator.
- **S48** negative: reader with `read` but no `metadata` grant on the source (K-AUTH-1: no partial content-only shape) sees the source omitted, and the item's witness evaluation is computed as if the root depending on it were filtered — no `source_unavailable` cutoff naming a hidden object.

Gate check: all 66 existing vectors still pass unchanged except any that assert exact `source_refs` for undisclosed sources (expected: none; if one does, that is a package bug to flag, not to silently edit). `go run ./cmd/memory conformance` 66/66 plus the new vectors; CLI scenario-11 test asserts locator and excerpt, not just the ref.

### 6. Risks and confidence

Risk: excerpt bytes in every `recall` tempt consumers to treat the view as a transcript store; mitigated by the existing `non-sensitive` ceiling (D-003) and size caps, not by new machinery. Risk: implementers disclose the locator but forget lineage-fenced excerpts — S46 covers it. **Confidence: high.** This is the smallest change that satisfies §7.2/§8 inside the kernel's existing disclosure model.

---

## Q2 (OPEN-9): The space directory — adapter-level signed objects in the platform space

### 1. Recommendation

**Adapter-level signed objects, not a kernel record kind.** The kernel's five kinds are closed (K-SCOPE-1, K-JSON-1); a directory entry names no assertion about the world, only where a git repository lives. It belongs with `space.json`: signed deployment metadata verified by the space layer. Architecture §5.2 already reserves `directory/` in the platform space, and [history.go](bundle/repo/go/space/history.go:166) already walks `directory/` paths, diagnosing non-platform spaces and otherwise ignoring content. Stage 5 gives that hook its contract.

One file per space: `directory/<lowercase-hex(utf8(space_id))>.json` (same path encoding as record files, so ids stay opaque), containing:

```json
{
  "entry": {
    "format": "swarma-memory-directory/1",
    "space_id": "project:example",
    "kind": "project",
    "version": 3,
    "previous": "sha256:<digest of previous entry payload or null>",
    "owners": ["owner:ivan"],
    "remote": "git@host:owner/project-example.git",
    "branch": "main",
    "genesis_digest": "sha256:<pinned genesis policy digest>",
    "visibility": "listed",
    "status": "active",
    "issued_at": "2026-…Z"
  },
  "signatures": [
    {"purpose": "swarma-memory-directory/1", "by": "space-owner", "key": "ed25519:sha256:…", "alg": "ed25519", "value": "…"},
    {"purpose": "swarma-memory-directory/1", "by": "platform-owner", "key": "ed25519:sha256:…", "alg": "ed25519", "value": "…"}
  ]
}
```

- **Two signatures, two different claims.** The *space owner's* signature (key registered in that space's own current policy, or in its genesis for a first listing) says "this remote and genesis are my space." The *platform owner's* signature (key registered in the platform space's policy) says "I list it." Neither signature alone is sufficient for auto-configuration. Purpose tag `swarma-memory-directory/1` joins the existing purpose-separated family (record/policy/key-registration/write) so no signature can be retagged across domains.
- **Who owns and writes the directory:** the platform space's owners own the directory as a whole, exactly as they own `space.json` transitions. Writing an entry means: the space owner signs the entry payload; a platform owner countersigns and commits it through the normal signed-commit + push path. New CLI: `memory directory publish --space <platform> --entry <file>` and `memory directory revoke --space <platform> --space-id <id>` (owner-only, same UX family as `keys register` / `policy grant`).
- **Reader verification** (in `space.Repository` sync of the platform space, first-parent order, mirroring record replay): (a) closed shape; (b) both signatures verify — platform signature against the platform policy chain in force at that commit, space-owner signature against a key registered for a listed owner in the *target* space's genesis or current verified policy; (c) `version` increments by exactly 1 and `previous` chains, first accepted version at a first-parent position wins, competing forks diagnosed (the D-025 / policy-fork rule, applied to entries); (d) on use: fetch the target remote, pin `genesis_digest` exactly as `spaces add` already requires an out-of-band genesis pin — the entry *supplies* that pin, it does not replace verification — then verify the target policy chain from genesis and require `space_id`, `kind` and current `owners` to still be consistent with the entry (owner-set changes via legitimate policy transitions are fine; a genesis mismatch is fatal).
- **Authoritative for / not authoritative for.** Authoritative *only* for discovery: "a space with this id and genesis is said to live at this remote; its owner consented to listing." Explicitly **not** authoritative for read/write grants, keys, resolvers, ceilings or current owners — all of that is read from the target space's own verified `space.json` chain, and actual read access still requires git hosting permission plus a reader grant in that policy. This preserves the brief's constraint: access truth stays in each space's owner-signed policy and in git access. A directory entry can therefore never *grant* anything; the worst a forged-but-countersigned entry does is point at a repository whose genesis will not verify.
- **Stale and revoked.** `status: "revoked"` (new version, signed by *either* owner — space owner withdraws consent, platform owner delists) means: do not offer for new configuration; existing configured spaces are unaffected (their trust anchor is their own pinned genesis, not the listing). Staleness is a computed reader state, not a stored claim: if the target's current verified policy no longer lists any entry owner, or the remote no longer serves the pinned genesis, the CLI reports the entry `stale` with the diagnostic, keeps the last verified data, and never silently substitutes a new remote or genesis from a later unverified source. History rewrite rules apply unchanged: a platform-space head that does not descend from the reader's cursor yields `history_rewritten` (existing behaviour in [git-spaces.md](bundle/repo/docs/git-spaces.md)).

Consumer flow: `memory spaces discover` syncs the platform space, verifies entries, lists them (id, kind, owners, remote, status — data only); `memory spaces add` gains `--from-directory <space_id>`, which clones using the entry's remote+branch and pins its genesis digest, then proceeds through the existing verified-policy path.

### 2. Why

D-018 requires the directory in the platform space; architecture §5.4 requires that sharing = git access + a directory entry. Making entries kernel records would force a sixth record kind, a domain schema, disclosure treatment and vectors for what is transport metadata — and would put locator data under kernel disclosure rules designed for evidence, where (per Q1) locators are protected outputs. The adapter already has the right machinery: purpose-separated signatures, first-parent replay, genesis pinning, per-file diagnostics (`directory_not_platform` exists today). Reusing it keeps the kernel closed and the change proportional.

### 3. Trade-offs and rejected alternatives

- **Kernel record kind (rejected).** Violates the closed five-kind model; needs a package release, projection semantics and erasure treatment for git URLs. No benefit: directory reads are not evidence queries.
- **Unsigned directory (rejected).** A plain file in the platform repo would be trusted on git-write access alone, contradicting D-019 ("trust comes from signatures; git is transport").
- **Single platform-owner signature (rejected).** Proves listing, not consent; a platform owner could list a victim's repository under a misleading id. The space-owner signature is the consent and the genesis binding.
- **Directory as access authority (rejected).** Would create a second grant registry, contradicting the adapter contract's "no second registry" rule (in [swarma.md](bundle/repo/spec/adapters/swarma.md)) and the brief's constraint.

Accepted cost: two-signature ceremony per listing. It happens once per space, by owners, through one CLI command — proportionate.

### 4. Changes needed

| Change | Where | When |
| --- | --- | --- |
| Entry format, signatures, verification, stale/revoked semantics | `docs/architecture.md` §5.4 (expand), new `docs/directory.md` | **v1 (stage 5)** |
| Schemas `directory-entry.schema.json`, signed wrapper; verification in history replay | `go/space/schema/`, `go/space/history.go` | **v1** |
| `spaces discover`, `spaces add --from-directory`, `directory publish/revoke` | `go/cmd/memory`, `docs/cli.md`, SKILL discovery step | **v1** |
| Kernel / normative package | — untouched — | — |
| Signed snapshot of the whole directory for offline bootstrap | — | later, only if per-entry fetch cost is measured |

No D-decision changes. OPEN-QUESTIONS 9 closes.

### 5. Tests and vectors

No kernel vectors (not a kernel change). Space/CLI tests, in the existing real-git style of `go/space/git_test.go`:

- Positive: publish → second home discovers → `spaces add --from-directory` → sync → recall across the shared space.
- **Stage-5 gate test:** two owners, two homes, two bare remotes. Owner A's agent and owner B's agent each read the other's shared project space after mutual grants; each also verifies that the *unshared* space of the other is not readable (git permission + no reader grant), proving the directory granted nothing.
- Negative: entry with only one signature (each way) → diagnostic, not listed as verified; wrong genesis → `spaces add` refuses; retagged record/policy signature → `purpose_mismatch`; competing entry forks at one first-parent position → first wins, second diagnosed (D-025 analogue); revoked entry → not offered, previously configured space still syncs; stale (owners rotated out legitimately, then genesis replaced on remote) → computed `stale`, no silent re-pin; entry file in a non-platform space → existing `directory_not_platform`.
- Non-interference analogue: a malformed entry in the platform space does not suppress valid neighbouring records/entries (existing adapter invariant).

### 6. Risks and confidence

Risk: owners treat "listed" as "trusted content" — mitigated by docs/SKILL wording: listing is discovery, every record still verifies individually (D-019). Risk: remote URL churn makes entries stale quickly; accepted, staleness is reported, not hidden. **Confidence: high** for format and ownership; medium on the dual-signature ceremony being the owner's preferred UX (flagged below).

---

## Q3 (OPEN-8, D-020): Resolvers per area and the escalation path

### 1. Recommendation

**Policy shape.** The field already exists: `resolvers: [{area: string, identities: […]}]` in the signed policy (in [policy.schema.json](bundle/repo/go/space/schema/policy.schema.json), `space.Resolver` (in [policy.go](bundle/repo/go/space/policy.go:58))). V1 keeps that shape and fixes its semantics rather than extending the schema:

- `area` is an opaque, space-local scope key. A conflict's area is derived deterministically by the CLI from the conflicting item, never free-typed by the agent: `decision:<schema_id>` for a `decision_record` sequence (e.g. `decision:schema:decision`), `schema:<schema_id>` for evidence conflicts on other assertions, and the literal `*` as the catch-all entry. A policy SHOULD name `decision:schema:decision`; matching is: exact item-derived area first, then `*`.
- `identities` is a non-empty set (schema already enforces non-empty, unique). `mode` is deliberately **not** added in v1: escalation is *addressed to all* named identities; resolution takes effect through the normal decision machinery (below), not through a vote counted by memory.

**Default resolver.** If no entry matches (including `resolvers: []`, today's genesis default), the resolvers are the space's `owners` from the same verified policy version. If that set is somehow empty the policy is already invalid (owners are non-empty by construction). There is no fallback to platform owners for project/agent spaces: escalating sideways to a different authority would misroute the decision. The CLI reports `no_resolver_named` only in the impossible empty case; in practice "default = owners" always yields an addressee, and the packet says whether resolvers came from an explicit area entry or the owner default.

**Resolver authority.** Naming is *routing only*. It grants nothing, and this must be stated in the policy docs because the name invites the opposite reading. To actually resolve, a resolver must, under the existing rules: hold a `writers` grant for the decision schema in that spacePolicy (architecture §5.3, D-019 verification), **and** be the deciding issuer of the conflicting sequence or its checked representative — because a superseding `decision_record` needs a canonical receipt that strictly succeeds the conflicting receipts in the deciding issuer's local order (K-REV-3, D-009), failing which admission refuses `authority_receipt_required`. So the resolvers list should name the deciding authority (or identities who can obtain its receipt, e.g. the owner who signs decisions); if the named resolvers lack receipt authority, their job is to *bring* the deciding authority's new decision into the space, and memory will correctly refuse a self-minted "resolution." Resolvers also need a reader grant to see the conflicting items; the packet respects that (below).

**Cross-space and cross-owner conflicts.** The kernel never merges spaces: `ReadSpaces` returns independent per-space views with no cross-space order (in [git-spaces.md](bundle/repo/docs/git-spaces.md)). V1 keeps that. If the same subject/schema is `ambiguous_current` in one space, or current-but-different across two readable spaces, there is no memory-level winner and the CLI must not pick one by recency, space kind or fetch order. The escalation is raised **per owning space**, addressed to that space's resolvers for the area, each packet scoped to its space (id, cursor, policy digest). Work that depends on the *combination* stays stopped until every space it depends on is resolved; a resolution in space A never edits space B. Where the conflicting decisions live in one shared project space with two owners contributing, that space's policy resolvers govern — which is why the project owner must name resolvers for the decision area when a second owner starts writing decisions (stage-5 checklist item).

**Escalation path — what exists today.** Swarm Keeper, as an escalation/obligation service, **does not exist as a platform component today**: the platform book has no Keeper module or specification; "Keeper" appears as obligation custody in the memory book's platform table and in design history (in [bounded-evidence.md](bundle/design/designs/bounded-evidence.md)), explicitly as target design. The task board **does** exist (platform book ch. 13, decided; goals, lifecycle and acceptance stay with the board per the adapter contract). Therefore:

- **v1: a board task addressed to the resolvers.** The agent (or its orchestrator) creates/updates a board task whose assignees are the resolver identities and whose payload is the escalation packet as data. This uses a real, owned path, keeps memory out of task state (D-020, K-BOUND-1), and gives the resolution an auditable home. Creating the task is the agent's action via the board's existing CLI — memory's CLI does not call the board.
- **Later:** when/if Swarm Keeper ships with an escalation intake, the same packet is delivered there instead; the packet format is transport-neutral so nothing in memory changes. Do not build a Keeper client now against an unspecified interface.

**Escalation packet.** New CLI command `memory escalate --space S --record ID [--version N]` (plus automatic offer from `recall --require-current` on exit 7): it runs the existing verified read, requires the target to be `ambiguous_current` or evidence-conflicted, and emits closed JSON (data classification `data`):

```json
{
  "kind": "memory-escalation/1",
  "space": "project:example",
  "space_cursor": "<verified commit>",
  "policy": {"version": 4, "digest": "sha256:…"},
  "area": "decision:schema:decision",
  "resolvers": ["owner:ivan"],
  "resolvers_source": "area|owner_default",
  "conflict": {
    "kind": "ambiguous_current|evidence_conflict",
    "items": [{"ref": {"id": "…", "version": 2}, "issuer": "…", "currentness": "ambiguous_current",
               "support": {"witness": "present", "…": "…"}, "oppose": {"witness": "present", "…": "…"},
               "source_refs": [{"id": "…", "version": 1}]}],
    "review_required": [{"id": "…", "version": 1}]
  },
  "requested_action": "record a superseding decision_record with a canonical receipt succeeding the conflicting receipts",
  "dependent_step": "<task/session reference supplied by the calling agent, or null>"
}
```

Rules: the packet contains only what the escalating principal's authorized view already disclosed (same kernel filtering as Q1 — hidden candidates never enter it; forwarding to resolvers is a disclosure, so if a resolver lacks a reader grant the packet still carries only refs the escalator may forward, and the resolver reads the space directly for content). `dependent_step` is supplied by the agent/orchestrator (`--task` flag), never invented by memory. Exit codes: `0` packet produced; `3` typed refusal if the record is not in conflict (`not_in_conflict`) or not readable; `7` semantics stay with `recall --require-current` (in [cli.md](bundle/repo/docs/cli.md)). SKILL's conflict paragraph already states the stop rule; it gains one line: on exit 7, run `memory escalate`, file the packet as a board task to `resolvers`, stop the dependent step, resume only after a new view shows the superseding decision current.

### 2. Why

Architecture §10 and D-020 already fix the rule (stop → escalate to policy-named resolvers → superseding decision → continue; memory never escalates). What is missing is only: a deterministic area derivation, a default, an authority clarification, and a concrete transport. The board is the only named transport that exists (ch. 13; the adapter contract in [swarma.md](bundle/repo/spec/adapters/swarma.md) already assigns goals/acceptance to it). Inventing a Keeper escalation client now would violate the brief's "do not invent platform components." Keeping `resolvers` as routing-only preserves K-REV-3: no new authority path is created, so no kernel change and no package release is needed for Q3 at all.

### 3. Trade-offs and rejected alternatives

- **Swarm Keeper escalation as v1 path (rejected for v1).** Right long-term home for obligations/deadlines, but it has no published interface; building against it now means inventing the component. The packet is designed to be re-delivered there unchanged.
- **Richer area selectors in v1 (rejected).** Subject patterns, schema lists and quorums in the policy would need schema-versioning and matching semantics before there is a single real shared space to validate them against. The derived-key convention (`decision:<schema>`, `*`) covers the v1 decision-continuity use case with zero schema change; a `schemas`/`subjects` refinement is a compatible later policy-version bump.
- **Quorum/`all` resolution modes (rejected).** Memory cannot count a vote without becoming a decision authority; the receipt order already defines when a conflict is over (a strictly succeeding canonical receipt). Multiple resolvers are addressees, not a threshold scheme — same stance as the one-owner-signature policy chain.
- **CLI filing the board task itself (rejected).** That would make memory a board client that changes task state, against D-020 and K-BOUND-1. The CLI emits the packet; the agent files it.

### 4. Changes needed

| Change | Where | When |
| --- | --- | --- |
| Area derivation, default-to-owners, routing-only authority, cross-space rule | `docs/architecture.md` §5.3 + §10 | **v1 (stage 6)** |
| `memory escalate` packet command + exit behavior; `recall --require-current` hint | `go/cmd/memory`, `docs/cli.md` | **v1** |
| SKILL: packet → board task flow | `SKILL.md` | **v1** |
| Kernel / normative package / policy schema | — untouched (semantics note only) — | — |
| Keeper intake delivery of the same packet; richer selectors/quorum if a real space needs them | platform + policy v2 | later |

No D-decision changes; D-020 is implemented, not amended. OPEN-QUESTIONS 8 closes for v1.

### 5. Tests and vectors

No kernel vectors (no kernel behaviour changes; `ambiguous_current` and evidence conflict are already pinned by S02/S28/P14-family vectors and CLI tests). CLI/e2e tests:

- **Stage-6 gate test:** seed a project space with two incomparable receipted decisions (ambiguous) and, separately, one assertion with admissible support and opposition. Agent flow: `recall --require-current` → exit `7` (`currentness_required`, already implemented in [read.go](bundle/repo/go/cmd/memory/read.go:247)); `memory escalate` → packet names the area-derived resolvers (and, in a policy with empty `resolvers`, the owners, marked `owner_default`); a board-task stub records the packet addressed to exactly those identities; a resolver with receipt authority records the superseding decision; fresh `recall --require-current` → exit `0`, new decision current, dependents in `review_required` as before.
- Negative: `escalate` on a non-conflicted record → `not_in_conflict`, no task filed; resolver identity without receipt authority attempts a "resolution" decision → kernel `authority_receipt_required`, conflict still flagged (proves routing ≠ authority); packet built by a principal who cannot see one candidate contains no ref/content for it (disclosure check); conflict in a space the agent may read but whose resolvers differ per area → packet addressed per derived area, not per `*` when an exact entry exists.
- Non-blocking control: an unrelated conflict in the same space does not make `recall` for an unaffected topic exit 7 (existing `--require-current` matching behaviour), and stays visible in normal recall.

### 6. Risks and confidence

Risk: policies in the wild keep `resolvers: []`, so "default = owners" silently becomes the universal path and area granularity is never exercised — acceptable for v1, visible in the packet via `resolvers_source`. Risk: board-task-as-escalation has no wakeup guarantee; a parked resolver means stopped work. That is D-020 working as intended (stop, don't guess), but the owner should know v1 has no deadline obligation behind it — that is precisely the future Keeper's job. **Confidence: high** on resolver semantics and authority; **medium** on board-task sufficiency as the v1 transport (it is the only existing one, but its assignee-notification behaviour is the board's, not memory's, to guarantee).

---

## For the owner

1. **Directory listing ceremony (Q2).** I recommend requiring both signatures (space owner + platform owner) before an entry is auto-usable. If you want one-step listing by platform owners alone for convenience, say so — it weakens the consent property but changes no other part of the design. This is an ownership/trust choice, not derivable from the material.
2. **Resolver granularity when sharing starts (Q3).** V1 derives areas as `decision:<schema>` with owners as default. When the first project space gets a second owner, someone must decide who resolves decision conflicts in it, or the owner default silently decides it. The design forces the packet to reveal which path was taken, but naming the resolvers is a product decision per shared space.
3. **Escalation transport commitment (Q3).** V1 uses board tasks because Swarm Keeper has no interface to build against. If Keeper is expected soon, confirm the packet format (`memory-escalation/1`) as the hand-off contract so the later switch is delivery-only; if Keeper is not coming, the board path should be declared the long-term path instead of a placeholder.
4. **Session-excerpt presentability horizon (Q1, overlaps OPEN-10/11).** The mechanism shows locators/excerpts for as long as records live; *how long* session sources must stay presentable, and whether excerpts should ever be availability-revised away while the citing decision is current, is a retention decision the material leaves open. The design supports any answer, but the default (presentable indefinitely in non-sensitive git spaces) should be accepted explicitly, since git cannot erase.


