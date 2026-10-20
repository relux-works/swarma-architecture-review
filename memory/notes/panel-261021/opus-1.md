# Panel answer: OQ-23, OQ-9, OQ-8

**Summary.**
- **Q1:** add a disclosure-filtered, deduplicated `sources` table to the closed view. The kernel already decides which sources a reader may see before it lists `source_refs`, and the table reuses that decision, so there is no new authorization path. A source the caller may not see stays absent; it is never shown as "withheld".
- **Q2:** the directory is an owner-signed pointer object at adapter level, kept in the platform space and verified like `space.json`. It hands out locations and genesis pins. It decides no access.
- **Q3:** the space policy routes conflicts with an exact (schema, subject) selector and defaults to the policy owners. Being named a resolver grants no right. v1 escalates through a board task, because Swarm Keeper has no published escalation interface. The CLI emits a packet that carries no record content.

Only Q1 changes the package.

## Q1 (OQ-23): session-excerpt sources in the view

### 1. Recommendation

Package **0.3.0-draft** adds one required top-level view field:

```json
"sources": [{
  "ref": {"id": "src:queue-choice", "version": 1},
  "issuer": "agent:alpha", "submitter": "agent:alpha", "representation_ref": null,
  "perspective": {"kind": "own", "principal": "agent:alpha"},
  "admission_class": "machine_observation",
  "owner": "runtime:claude-code", "source_kind": "artifact",
  "object": "<session id>", "revision": "<message id or index>",
  "digest": {"algorithm": "sha256-cjson-v1", "value": "<hex>"},
  "provenance": "direct", "origin": "<root origin>",
  "original_issuer": "agent:alpha", "carrier": null,
  "availability": "unavailable",
  "excerpt": {"state": "available", "text": "Decision: use a bounded durable queue\n"}
}]
```

`excerpt` is exactly one of `{state: available, text}`, `{state: erased}` or `{state: none}`. The recorded sequence, lineage, disclosure labels and `retention_admission` stay in the protected binding, as `spec/README.md` requires for admission facts.

**New clause K-SRC-1 (disclosed source entries):**

> `sources` is the set, sorted by `(id, numeric version)`, of exactly the references in the items' `source_refs`.
> - Each entry is built from the source record that is eligible under K-AUTH-1 at the query cut: read, use, metadata, audience and purpose disclosure, space, subject, context and validity.
> - An ineligible source yields no entry, no reference, no placeholder, no count and no cutoff.
> - `availability` is `erased` if the source is fenced. Otherwise it is the latest eligible availability revision, else the stored value. A non-resolvable source-access fact turns `resolvable` into `unavailable`.
> - `excerpt` is `available` with the retained text when an excerpt exists and is unfenced. It is `erased` when the source is fenced, and `digest` is then null. It is `none` when nothing was retained. It never depends on `availability`.
> - Entries are data. The kernel never dereferences, resolves or executes a locator, and building entries costs no logical budget.
> - An `audience_projection` has empty `sources`.
> - In `changes`, an item counts as changed when an entry it cites changed.

Four amendments go with it:
- **K-DISC-2:** audience projections have empty `sources`.
- **K-EVAL-9:** `sources` joins the deduplicated outputs and gets the change rule above.
- **K-ERASE-1:** entries of fenced sources carry no bytes and no digest.
- **K-NI-1:** source entries join its list.

| Brief term | Contract | Meaning |
| --- | --- | --- |
| available | `excerpt.state: available` | The retained, unfenced bytes are shown, even when the session is gone |
| unavailable | `availability: unavailable` | The external object cannot be resolved now. Always the case in v1, which has no session resolver. The excerpt is unaffected (D-016) |
| erased | `availability: erased`, `excerpt.state: erased`, `digest: null` | Memory's own erase fence (K-ERASE-1). The header survives as a structural tombstone |
| withheld | not emitted | See below |

**A reader without the right sees nothing of the source.**
- **No read right on the space:** `not_authorized` from the CLI and an empty kernel view, as today.
- **Read right on the assertion but not on the source:** the item lists no such ref. The documentary edge and any assessment naming that source are filtered before accounting (K-AUTH-1), and no `source_unavailable` cutoff appears. After handle normalization the view equals the view of the same corpus without that source and the records filtered with it.

A visible `withheld` belongs to a later release in which a header and its payload carry separate disclosure, which means the protected service. Even then it may only be derived from a header the caller is authorized to see.

**Locator mapping.** This goes in the adapter contract and the CLI; the record wire does not change. For `--source-session runtime:session:message`:

| Field | Value |
| --- | --- |
| `owner` | `runtime:<runtime>`, the system that owns the session; later the session host |
| `object` | the session id |
| `revision` | the message id or index |
| `digest` | `sha256-cjson-v1` of the quoted message text, encoded as a JSON string |
| `origin` | the canonical locator: one root origin per message (K-DISC-3) |
| `availability` | `unavailable` |

Today the CLI puts the locator JSON in `origin`, a raw hash in `object` and the agent in `owner` (`docs/cli.md`, "Session excerpts"). The new mapping puts each locator part in its own typed field. Old records stay valid and display as they were recorded.

### 2. Why

- **The eligibility check already exists.** The kernel decides per record whether a source is eligible before it lists a ref (`kernel/read.go` `visible`; `evaluate.go` `collectSources`). An assessment contributes its sources only if all of them are eligible, and a justification only if all its premises are. K-EVAL-9 already says source metadata obeys the visibility rules for content. The table therefore adds payload only for records the reader already sees by reference. There is no new right, budget, binding or cut.
- **"Withheld" would leak.** A withheld marker reveals that a hidden source exists, which K-AUTH-1 forbids ("a hidden premise … MUST NOT … appear as a gap, or change any public field"), and so does K-NI-1. `findings/view-inference.md` says the same: "Reveal the distinction only when the caller is allowed to know it", and "content locators, digests and source-author identities are protected outputs too."
- **v1 cannot hide a source inside a readable space anyway.** Anyone who can read the git space can read every file, and the write CLI has no per-record disclosure input (`go/e2e/README.md`). Partial disclosure matters for the protected service; the vectors pin the property now.
- **The record wire can stay.** The stored source schema is closed and has no version tag, so a new required field would invalidate records that are already signed. The `owner`, `object`, `revision` and `digest` fields already are the locator (K-REC-1).

### 3. Trade-offs and rejected alternatives

- **Separate source-read operation: rejected.** It needs a new query kind and scope, a protected binding to the citing view's cut, an answer for a probed hidden id that is indistinguishable from "does not exist", and its own vectors. It would also duplicate the eligibility check the view already runs. Keep it for later, and only if a live resolver (a session-host export) has to fetch external bytes on demand. That is resolution, not presentation.
- **Payload inside each item:** duplicates bytes when several items cite one source.
- **Sources as query targets:** breaks the item shape and the polarity semantics.
- **Typed `locator` field in the record:** cleaner, but it forces a record-wire migration.
- **CLI reconstruction from the raw snapshot:** already rejected in OQ-23.
- **Cost of the chosen option:** larger views, bounded by the policy field limits, and every expected view in the package changes.

### 4. Changes needed

| Area | Change | When |
| --- | --- | --- |
| Package | `sources` in the view schema; K-SRC-1 and the four amendments; URNs and labels move to 0.3.0, which also closes OQ-18; COVERAGE rows; the vectors below | v1 |
| Adapter `swarma.md` | Session-locator mapping; data-frame profile label | v1 |
| Architecture | §7.2 and §8 cite K-SRC-1 | v1 |
| Implementation | Kernel builds `sources`; CLI emits it and uses the new mapping; remove the limitation from `docs/cli.md` and `SKILL.md`; full scenario 11; unblocks TASK-261019-gak2ji | v1 |
| Decisions | None change; record the choice as a new decision | v1 |
| Later | `withheld` with per-payload disclosure; a resolve operation for live external bytes | later |

### 5. Tests and vectors

| Vector | Proves | Expected | Forbidden |
| --- | --- | --- | --- |
| S43 | A retained excerpt of an unavailable session is presentable; one entry per source | Two assertions cite one session source by documentary basis; `availability: unavailable`, `excerpt.state: available` with the exact text; both items cite it; both channels `not_found` | `/result/sources/1` exists; `/result/items/0/support/witness` = `present` |
| S44 | Erasure leaves a header without bytes | Capture, erase the source, recall: `erased`, `digest` null, `excerpt.state: erased`; the capture is unchanged (K-SNAP-1) | `/result/sources/0/excerpt/text` exists; `/result/sources/0/digest/value` exists |
| S45 | Non-interference across a hidden source append, a hidden availability revision and a hidden erase | The public capture equals the final public recall (`equivalent_outputs`). Positive control: a private capture shows two entries, with the public source `unavailable` | `/result/sources/1` exists; `/result/items/0/source_refs/1` exists; `/result/sources/0/availability` = `unavailable` |
| S46 | A root that names a hidden source is filtered without a gap | Public reader: `not_found`, `complete`, `cutoffs: []`, `sources: []`. Private control: `present` with one entry | `/result/cutoffs/0` exists; `/result/sources/0` exists |
| S47 | Audience projections show no entries | `source_refs: []` and `sources: []`, even for a public source | `/result/sources/0` exists |
| S48 | `changes` reacts only to visible entry changes | Hidden availability revision: `no_change`. Visible one: `changed`, with the citing item | `/operation_results/2/changes/state` = `changed` |

- **Existing vectors:** all 74 gain `sources` in every expected view. About two dozen have non-empty `source_refs` and must be checked by hand, not regenerated.
- **Gate:** e2e scenario 11 asserts B's byte-exact multiline excerpt, the four locator fields and `unavailable`. After B's read grant is revoked, B still gets `not_authorized` with no data.
- **Non-interference in v1:** the CLI cannot create a hidden source inside a readable space. S45–S47 therefore carry the property, together with a `space.Read` library test that uses crafted disclosure labels.

### 6. Risks and confidence

- Views grow with excerpts.
- Checking about two dozen expected views by hand invites mistakes; require both evaluators to agree again.
- Whether the digest covers the full message or only the excerpt is a convention; the adapter contract must say which.
- Session ids become visible to every reader of the space.

**Confidence:** high on the shape, the states and non-interference; medium on the locator mapping.

## Q2 (OQ-9): the space directory

### 1. Recommendation

**What it is.** An entry is a signed object at adapter level, in the policy layer next to `space.json`, signed under a fifth purpose tag, `swarma-memory-directory/1`. It is not a kernel record kind and not a domain assertion.

**Owner and signer.** The directory belongs to the owners of the platform space that holds it. An entry is valid only if:
- it is signed by an identity listed in `owners` of the platform policy in force at the entry's first-parent position;
- the signing key is registered in that same policy.

Agents that can write records to the platform space cannot publish entries.

**Format.** One immutable file per version, at `directory/<hex(space_id)>/<version>.json`:

```json
{"entry": {
   "directory": "space:platform:ivan",
   "space_id": "space:project:x", "version": 2, "previous": "sha256:<prior version digest>",
   "author": "owner:ivan", "status": "active",
   "kind": "project", "owners": ["owner:ivan"],
   "remote": "ssh://git@example/x-memory.git", "branch": "main",
   "genesis_digest": "sha256:<genesis of the listed space>",
   "identities": [], "projects": ["project:x"]},
 "signature": {"purpose": "swarma-memory-directory/1", "key": "ed25519:sha256:...", "alg": "ed25519", "value": "..."}}
```

- `identities` names the agents whose memory an agent space holds; `projects` names the projects a project space serves. Both are lookup keys, not access lists.
- `status` is `active` or `retired`.

**How a reader verifies an entry.**
1. The platform space is configured with its genesis pin obtained out of band, exactly as today. This is the one trust root an agent needs.
2. Sync replays `directory/` in first-parent order under the platform policy in force at each position. Each entry is checked for:
   - the closed schema;
   - `directory` equal to the platform space id, so an entry cannot be moved into another platform space;
   - the purpose tag, a registered key, and an author who is a listed owner;
   - a clean version chain: version 1 has a null `previous`, each later version is +1 and names the digest of the prior one;
   - forks: the first accepted version wins;
   - rewrites: changing or deleting an accepted path yields `directory_rewritten`.
3. `memory spaces add ID --from-directory` clones `remote` and runs the existing `VerifyChain` from `genesis_digest`. `space_id`, `kind` and `owners` must match the verified listed policy; on mismatch it reports `directory_mismatch` and saves nothing.
4. Reading still requires a reader grant for the agent in the listed space's policy, plus git access. Nothing changes there.

**What the directory is authoritative for.**

| The directory is authoritative for | It is not authoritative for |
| --- | --- |
| The directory owner's binding of `space_id` to `genesis_digest` | Read, write or admin rights: those live in the listed space's policy and on the git host |
| The last published remote and branch | Key validity: the listed policy decides (later, the owner registry) |
| Lookup from identities and projects to spaces | Content, currentness or conflicts |
| Discovery status (`active` or `retired`) | Reachability, or a foreign owner's consent beyond the checked `owners` claim |

I read "access" in D-018 and §5.4 as access coordinates (remote, branch, pin), not rights. If rights were meant, D-018 must be amended: a second copy of rights contradicts D-019.

**Stale and revoked entries.**

| Case | Behavior |
| --- | --- |
| Entry retired | New adds refuse with `directory_retired`. Spaces already configured keep working, because their anchor is their own pin, and they report a diagnostic |
| Remote moved, same genesis | Applied only by an explicit `memory spaces update ID --from-directory`. Cursor descent still guards continuity (`history_rewritten`) |
| Same `space_id`, new genesis | Never applied (`directory_anchor_changed`). Changing a trust root needs the operator to remove the space and add it again |
| Listed owners no longer match | `directory_mismatch` |
| Signer later removed from `owners` | Earlier entries stay valid history, as records do after a key rotation; current owners may retire them |
| Unsharing a space | Revoke the reader grant and the git access. Retiring the entry alone revokes nothing |

**Meeting the stage-5 gate with a second owner.** Owners A and B each have their own platform space. To share space S_A with B:
1. A registers the public key of B's agent and grants it reader in S_A (D-024; `memory keys register`, `memory policy grant`), and grants git read on the host.
2. B's owner publishes an entry for S_A in B's directory, using the genesis digest received from A.

B's agents trust only B's platform pin, so a foreign pin reaches them only through their own owner's signature. In v1 the two owners exchange one genesis digest and the agent public keys directly. This stands in for the platform's admission path for outside identities (platform book ch. 05, «Внешние агенты»: invitation, then root-signed admission). Until identity cells exist (D-010), identity strings must be qualified by owner, or two owners' agents could collide on the same name.

### 2. Why

- **It is trust-anchor distribution, consumed before any kernel read.** A memory record cannot do that job: memory is data and never authority (K-SCOPE-1). Any platform writer could sign such an assertion, and the kernel would only report competing issuers without choosing between them (K-PROJ-1).
- **The policy layer already has what this needs:** owner signatures, purpose separation, first-parent history and genesis pins (`docs/signing-policy.md`, `docs/git-spaces.md`).
- **No new trust relationship.** Each owner's agents trust only that owner's directory.
- **The kernel stays free of Swarma terms (D-007).**

### 3. Trade-offs and rejected alternatives

- **A sixth kernel record kind:** contradicts the five-record kernel and portability.
- **A domain-schema assertion:** turns memory content into trust configuration, and lets agent writers publish pins.
- **One shared directory for both owners:** B's agents would have to trust A's signer. The format still works if the owner prefers a co-owned platform space.
- **Reader lists copied into entries:** a second source of access truth that will drift.
- **Adding every listed space automatically:** surprising, and it widens the attack surface.
- **Co-signature by the listed space's owner:** adds nothing while every key roots in the same owner; revisit with the owner registry.

### 4. Changes needed

| Area | Change | When |
| --- | --- | --- |
| Kernel package | None | — |
| Adapter `swarma.md` | Directory binding: an owner-signed pointer that is not authority | v1 (text only) |
| Architecture | §5.2 layout, §5.4 format and rules, §6.1 fifth purpose tag, §11 commands, §14 stage-5 detail | v1 |
| Decisions | New decision: directory format, owner, non-authority, one directory per platform space | v1 |
| Implementation | Entry schema, replay and diagnostics in `space/`; `memory directory` list, show, publish and retire; `spaces add` and `spaces update` with `--from-directory` | v1 |
| Later | Identity cells and the owner registry; delegated publishing in the style of D-024; reading another owner's directory | later |

### 5. Tests (adapter and e2e)

There are no kernel vectors, because the kernel does not change.
- **Stage-5 gate:** two owner homes, two platform spaces, and shared spaces S_A and S_B on local bare remotes. Each owner lists the other's space. Agent a1 adds S_B and agent b1 adds S_A, each from its own directory. Each recalls the other owner's decision with its original issuer.
- **Negative cases:**
  - entry signed by an agent writer: `directory_signer`;
  - wrong genesis, `owners`, `kind` or `space_id`: `directory_mismatch`;
  - entry moved into another platform space;
  - rewritten file;
  - fork, where the first version must win;
  - retired entry;
  - anchor change.
- **Non-authority:**
  - with the entry present, revoking b1 in S_A gives `not_authorized`;
  - with no entry, a manual `spaces add` with the right pin and grant still reads;
  - a listed but unshared space gives `not_authorized`.
- **Instrument control:** disabling the signer check must make the forged-entry test fail.

### 6. Risks and confidence

- A compromised platform owner key can list a fake pin. The `owners` check limits the damage, and the v1 trust root is the owner anyway.
- Manual exchange of pins and keys invites mistakes; the binding checks catch mismatches.
- Identities can collide across owners until identity cells exist.

**Confidence:** high on the adapter object and on non-authority; medium on per-owner directories, which are the owner's choice.

## Q3 (OQ-8, D-020): resolvers and escalation

### 1. Recommendation

**Policy fields.** Replace the free-text `area` with an exact selector:

```json
"resolvers": [
  {"area": "queue-design",
   "schemas": ["schema:assumption", "schema:decision"],
   "subjects": ["topic:queue"],
   "identities": ["owner:ivan", "agent:architect"]}
]
```

- `area` is unique.
- `schemas` are sorted ids of accepted schemas, version-agnostic; `[]` means any schema.
- `subjects` are sorted exact subject ids; `[]` means any subject.
- No patterns, because ids are opaque (K-ENV-1).
- Every identity listed must have a registered key, a reader grant and a writer grant in the same policy version, so that it can both inspect and record. Otherwise that policy version is refused and the previous one stays in force.
- **Specificity order:** subject and schema, then subject only, then schema only, then catch-all. Entries of equal specificity must not overlap, and there is at most one catch-all. So every conflict maps to exactly one area.
- **Routing:** a conflict on an item is routed by that item's space policy at the reader's verified cursor, using the item's schema and subject.
- **Default resolver:** when nothing matches, the policy `owners`, flagged `defaulted: true`.

No CLI command writes `resolvers` today, and genesis writes `[]` (`cmd/memory/cli.go`), so the new entry shape breaks no existing policy. Add `memory policy resolvers set` and `remove` as owner commands.

**Resolver authority.** Being named a resolver grants no memory right: no grant, no representation, no revision authority, no receipt. A resolver entry does two things only: it routes the escalation, and it says whose ruling a blocked step may accept. The resolution itself uses rights that already exist:

| Path | Who | Rule | Effect |
| --- | --- | --- | --- |
| Replace, correct or withdraw | The issuer of the conflicted assertion | K-REV-1 | The new version becomes current; assessments pinned to the old version stop qualifying (K-REC-2). This is D-020 literally |
| Withdraw evidence | The issuer of an assessment | K-REV-1 | That witness disappears |
| Ruling | A resolver who is not the issuer | An ordinary write in the resolver's own sequence, optionally with `challenge` | The conflicted record stays attributed and conflicted; the blocked step resumes on the ruling |
| Receipt (later) | The deciding authority H | A canonical event that succeeds every maximum (K-REV-3) | The only fix for `ambiguous_current`. The v1 profile has no receipts (`docs/cli.md`), so this outcome cannot arise in v1 spaces |

A non-resolver can still assess or challenge, but cannot unblock anything.

**Conflicts across spaces and owners.**
- **Kernel conflicts live in one space.** A query pins one space and cross-space premises are refused (K-RULE-1), so each space's policy routes its own conflicts.
- **Contradictions between two readable spaces** are never a kernel outcome and never produce exit 7. If a dependent step relies on both, the agent files an explicit packet with `kind: cross_space` and `detected_by: agent`. It is routed to the union of both areas' resolvers, and no space wins by default.
- **Between owners,** the agent files only on its own owner's board. The foreign routing is included so the two owners can coordinate directly. Memory never transfers or merges authority between owners (D-009 scope).

**The escalation path.**

| Mechanism | Status in the material |
| --- | --- |
| Task board | Runs today (platform book ch. 15) and holds statuses and resources (ch. 13). "Blocked never moves a task; the board notifies the orchestrator or a human" is decided design (ch. 09) |
| Swarm Keeper | Only a role: a long-lived top-level orchestrator (ch. 00). Its obligation ledger is target design (`designs/bounded-evidence.md`), and no escalation interface or format is published |

**v1 uses a board task.** A keeper can be named as a resolver identity, or can watch the board. Later, a Keeper obligation can cite the board task, and a board revision can become the authority receipt for the resolution (memory book, «Порядок решений»).

**The packet.** `memory conflicts --id ID --space S --task T --json` is a pure read and produces:

```json
{"type": "memory_escalation", "format": 1, "data_classification": "data",
 "conflict_key": "sha256:<canonical kind + sorted (space, ref)>",
 "kind": "evidence_conflict", "detected_by": "kernel",
 "items": [{"space": "space:project:x", "ref": {"id": "rec:queue", "version": 1},
   "subject": "topic:queue", "schema": {"id": "schema:assumption", "version": 1},
   "issuer": "owner:ivan", "currentness": "current", "support": "present", "oppose": "present",
   "evidence": {"support": [{"id": "rec:a1", "version": 1}], "oppose": [{"id": "rec:a2", "version": 1}]}}],
 "spaces": [{"id": "space:project:x", "cursor": "<commit>", "policy_version": 7, "policy_digest": "sha256:..."}],
 "routing": [{"space": "space:project:x", "area": "queue-design", "defaulted": false, "resolvers": ["owner:ivan"]}],
 "dependent": {"agent": "agent:w", "task": "TASK-..."},
 "resume": {"space": "space:project:x", "id": "rec:queue", "rule": "issuer_current"}}
```

- **No content.** The packet carries no record content, no excerpt and no prose, only typed ids and enumerations. A poisoned record therefore cannot write instructions into a resolver's task.
- **Unsigned, a pointer only.** Every claim in it can be checked against the spaces, and the resolver re-reads them with `memory explain`.
- **Deduplication.** `conflict_key` gives one escalation task per conflict, however many agents hit it.

**Flow, as written into the skill.**
1. `explain ID --require-current` (new, for an exact dependency) or `recall --require-current` exits 7. The agent stops the dependent step.
2. The agent builds the packet.
3. Through the board (the agent itself if its grants allow, otherwise its orchestrator): the task is marked blocked with the packet attached as a data resource. If an open escalation task with the same `conflict_key` exists, it is reused; otherwise one is created and addressed to the routed resolvers.
4. A resolver records the resolution and closes the escalation task, naming the record that resolves it.
5. Work resumes when the `resume` check exits 0. After a ruling, two checks must pass:
   - `explain RULING --require-current` exits 0;
   - `memory resolvers --space S --schema SCHEMA --subject SUBJECT` lists the ruling's issuer.

### 2. Why

- **D-020 and §10 hold.** Memory reports, the agent stops, and the platform path carries the escalation.
- **Routing is deterministic.** The selector uses only fields that readers see and that the kernel defines in the sequence key (K-DOM-2). A free-text area would force the agent to classify the conflict.
- **Owners as the default.** They are the only authority every space has by construction (D-019).
- **Trusted resolvers.** Requiring keys and grants is the v1 meaning of "when they are part of the trusted system" in D-020.

### 3. Trade-offs and rejected alternatives

- **Keeper escalation in v1:** there is no published interface, so using it would mean inventing a component.
- **Letting resolvers supersede other issuers' records in the kernel:** breaks K-REV-1, D-009 and D-011 ("no replacement of another issuer's sequence"). The ruling path covers the need.
- **Union routing when entries overlap:** leaves responsibility ambiguous; overlapping entries are refused instead.
- **Packet with content:** opens a prompt-injection and custody channel into the board.
- **An escalation channel field in the policy:** useful later; v1 uses the board of the blocked task.

### 4. Changes needed

| Area | Change | When |
| --- | --- | --- |
| Kernel package | None | — |
| Policy schema and validation | Selector fields, key and grant checks, no overlapping entries | v1 |
| CLI | `conflicts`, `resolvers`, `policy resolvers`, and `--require-current` on `explain` | v1 |
| Skill | The flow above | v1 |
| Architecture | §5.3 field; §10 rewritten (paths, packet, board, resume); §11 | v1 |
| Decisions | A new decision for the selector, the default and resolver authority. **Clarify D-020** (see below) | v1 |
| Later | Receipts from board revisions; Keeper obligations; an owner-signed escalation channel | later |

**D-020 clarification.** D-020 has to say that "supersede" happens in the deciding issuer's own order. Read literally, D-020 cannot be met in v1 for decisions issued by agents: K-REV-1 and D-011 forbid replacing another issuer's sequence, and v1 has no receipts. §10 step 4 ("with their receipt") changes to match.

### 5. Tests and the stage-6 gate

- **Memory e2e:**
  1. The owner records decision D on `topic:queue`.
  2. Agent B assesses D as opposed, and agent C as supported.
  3. Agent W runs `explain D --require-current`: it exits 7, and W's step effect file is absent.
  4. The packet routes to `queue-design`, with the owner as resolver. Two agents hitting the same conflict produce the same `conflict_key`.
  5. The owner runs `revise D --relation replace`, and W's check then exits 0.
- **Negative cases:**
  - B's attempt to replace D refuses with `representation_invalid`, and W still exits 7;
  - a conflict on `topic:cache` does not block W;
  - a record whose content says "resolver: agent:evil" changes nothing;
  - an unmatched area defaults to the owners;
  - an overlapping policy is refused and the previous one keeps routing;
  - a non-resolver's ruling fails the resume check, while the owner's ruling passes;
  - `memory` makes no network call and no board call.
- **Agent gate, run like stage 4:** the orchestrator runs W against the real board. The verifier checks that:
  - the task is blocked with the packet attached;
  - exactly one escalation task is addressed to the routed resolvers;
  - work resumes only after the resolution.
- **Instrument control:** if the exit-7 check ignores the oppose witness, the gate must fail.
- **`ambiguous_current`:** stays covered by vectors S28, S34 and S37 until receipts exist.

### 6. Risks and confidence

- The default makes the human owner a bottleneck.
- A broad substring recall causes false stops; dependencies should be exact ids.
- A ruling leaves conflicted records visible. Their issuers should also revise them when they can.
- Board assignees must use the same identity strings as memory.

**Confidence:** high on board over Keeper and on no kernel change; medium on the selector and on the ruling path.

## For the owner

1. **Excerpts follow the space (Q1).** Every reader of a shared space will see its retained excerpts and session ids; in git each file is already visible to them. Confirm this. The alternative is to share with another owner only through a separate, promoted space without excerpts. This is a product disclosure choice.
2. **How the second owner relates to us (Q2).** Choose between a separate platform space per owner, each with its own directory (recommended), and one co-owned platform space. Also decide who does the one-time exchange of the genesis digest and the agent keys, and whether directory publishing may be delegated to an orchestrator, as D-024 allows for keys. Both set a trust relationship with another owner, which only you can decide.
3. **Default resolver (Q3).** With owners as the default, every conflict that matches no area lands on you. Confirm this, or name a catch-all resolver, such as the keeper identity, in each policy. This delegates both authority and workload.
4. **Ruling path (Q3, the D-020 clarification).** Confirm that blocked work may resume on a named resolver's ruling while another issuer's conflicted record stays conflicted. This decides what "resolved" means for work.
5. **Precedence between spaces (Q3).** My recommendation for v1 is no automatic precedence, with cross-space contradictions routed to both spaces' resolvers. Whether a platform decision should automatically override a project decision is a governance decision.
