# Panel answer: Q1 (OQ-23), Q2 (OQ-9), Q3 (OQ-8)

**Summary.**
- **Q1:** add a kernel-computed `sources` table to the view. No separate source-read operation, no `withheld` state.
- **Q2:** the directory is a set of signed objects at the adapter level, not kernel records. It is authoritative for naming spaces and their trust anchors, never for access.
- **Q3:** resolvers are keyed by exact subject and default to the space owners. Being named grants nothing. In v1, escalation goes through a board task.

## Q1. Session-excerpt sources

### 1. Recommendation

Add a disclosure-filtered source payload to the view: a new required top-level array, `sources`.

```json
"sources": [
  {"ref": {"id": "src:q1", "version": 1}, "owner": "agent:a1",
   "source_kind": "artifact", "provenance": "direct",
   "original_issuer": "agent:a1", "carrier": null,
   "availability": "unavailable",
   "object": "sha256:9f2c…", "revision": "42", "digest": null,
   "origin": "{\"message\":\"42\",\"runtime\":\"claude-code\",\"session\":\"s-7\"}",
   "excerpt": "Decision: use a bounded durable queue\n",
   "retention_admission": {"id": "retention:q1", "version": 1}},
  {"ref": {"id": "src:old", "version": 1}, "owner": "system:documents",
   "source_kind": "document", "provenance": "canonical",
   "original_issuer": "owner:ivan", "carrier": null, "availability": "erased"}
]
```

The schema is a closed `oneOf` with two variants:
- **Variant A** (`resolvable` or `unavailable`): 13 fields, copied verbatim from the source body.
- **Variant B** (`erased`): only the 7 structural fields.

**New clause K-SRC-1, "Disclosed source payload":**

1. **Membership.** `sources` holds exactly the distinct refs in the union of the items' `source_refs`, sorted by (id, numeric version). Nothing else is described or counted. Audience items already have empty `source_refs` (K-DISC-2), so audience views have no sources.
2. **Effective availability:**
   - `erased` if a current per-record fence or erasure obligation covers the source or its known content-lineage closure, or if its state is `erased`;
   - otherwise `unavailable`, if its state is `unavailable` or an admitted source-access fact marks it unresolvable at the query frontier;
   - otherwise `resolvable`.

   The state is the body value, overridden by the latest query-eligible `availability` revision at or before the cut. K-EVAL-5 uses this same value. It reports the admitted state, never a fresh read.
3. **Payload.** `unavailable` describes only the external original, so a retained excerpt stays disclosed (that is the point of D-016). Variant B carries no object, revision, digest, origin, excerpt or retention ref at any cut (K-ERASE-1).
4. **Independence.** Building the payload costs no logical visit, resolves nothing, and changes no evaluation, cutoff or completeness.
5. **Changes.** An item counts as changed when the entry for any ref in its `source_refs` changed.

| State named in the brief | Kernel value | What a reader with rights sees |
| --- | --- | --- |
| available | `resolvable` | full entry |
| unavailable | `unavailable` (session deleted, no resolver) | full entry, excerpt kept |
| withheld | not a state | — |
| erasure | `erased` | tombstone |

**A reader without the right to a source** sees no ref, no entry, no placeholder and no count:
- The assessment or justification that cites the source is filtered out before accounting, as today (K-AUTH-1). So evaluation and `source_state` come out exactly as if the source did not exist.
- Using the source's id as a query target returns the same empty view as an id that does not exist.
- Audience projections show no sources at all.

**Adapter.** `swarma.md` should adopt the session encoding the CLI already writes (`cli.md`, §Session excerpts):

| Field | Value |
| --- | --- |
| `origin` | canonical `{runtime, session, message}` JSON |
| `object` | `sha256:<raw text digest>` |
| `revision` | message id or index |
| `digest` | `null` |
| `availability` | `unavailable` |

The CLI decodes `origin` for display. That is formatting, not computing disclosure.

### 2. Why

- **It was promised.** §7.2, §8 and D-016 promise readers the locator and the excerpt. The book's first purpose is to "name the current decision and its exact source". Authority receipts are sources too, so every decision recall needs this.
- **It adds no authority.** The kernel already decides which sources a reader can see (`collectSources`; K-EVAL-9: "Source metadata … obey the same visibility rules as content"). A listed source is one the reader already holds read, use and metadata rights on. K-AUTH-1 has "no partial content-only view shape", so disclosing the body applies the existing rule. Showing retained bytes grants no right to resolve the original (K-REC-1).
- **`withheld` would be exactly that excluded partial shape.** For hidden sources it leaks their existence and count (K-NI-1; `findings/view-inference.md`). In git it is theatre anyway: readers can clone the bytes, which is why D-003 keeps git non-sensitive.
- **One snapshot, one cut.** Payload, availability and evaluation come from the same snapshot, and captured views keep the payload as history (K-SNAP-1).

### 3. Trade-offs and rejected alternatives

- **Separate source-read operation (rejected).** It would keep the existing vectors unchanged and the views small. But it adds a lookup surface by exact ref, which is an existence oracle unless proven indistinguishable. It also needs a protected binding to the view's cut, doubles the number of calls, and still needs a package release with its own non-interference vectors.
- **Payload inside each item (rejected):** it duplicates excerpts.
- **Payload only in `explain` (rejected):** `recall` would name sources it cannot show.
- **Typed `session_message` locator (later):** it changes the canonical bytes of stored records, so it belongs with the session host's admitted export.
- **Costs accepted:** a mechanical change to every expected view, and bigger views. The CLI may shorten excerpts in compact output, but never in the kernel output.

### 4. Changes needed

- **Package, v1 (0.3.0-draft):**
  - `view.schema.json` gains `sources`.
  - K-SRC-1 becomes the 53rd clause, with cross-references in K-EVAL-5, K-EVAL-9, K-DISC-2 and K-ERASE-1.
  - All URNs and `semantic_profile` move to 0.3.0, which also closes OQ-18.
  - `build_vectors.py` derives `sources` from the hand-specified `source_refs`.
  - New vectors S43–S50.
  - `validate.py` checks the invariant `sources = ∪ source_refs`, with a planted violation as a control.
  - COVERAGE, README and RELEASES are updated.
  - `swarma.md` gets the locator convention and a fix for its stale 0.2.5 data-frame profile.
- **Implementation, v1:**
  - The kernel builds `sources` after audience redaction and includes them in the change comparison.
  - Assets and ratchets are regenerated.
  - The CLI passes `sources` through and renders the decoded locator.
  - The limitation notes in `cli.md` and `SKILL.md` are removed.
  - e2e scenario 11 is upgraded, which unblocks TASK-261019-gak2ji.
- **Architecture, v1:** §8 names `sources`.
- **Decisions:** none needed; D-016 already decided the behaviour.
- **Later:** the typed locator, and paging if measured views turn out too large.

### 5. Tests and vectors

| Id | Claim | Setup | Must hold | Forbidden / pair |
| --- | --- | --- | --- | --- |
| S43 | A retained excerpt and its locator are disclosed while the original is unavailable; one entry per source | a1 and a2 cite `src:sess` (CLI encoding, excerpt); a2 also cites `src:doc`, which is resolvable | `sources=[doc,sess]` verbatim; items `not_found`/`complete` with `prior_assessment_only` | sess `resolvable`; excerpt `null`; `sources` size 3; `cutoffs ∋ source_unavailable` |
| S44 | A hidden excerpt source leaves no trace (non-interference) | op0: public capture. op1: admit a private-only, unavailable `src:h` plus a documentary link. op2: private capture (control). Final query is op0's | result ≡ op0; op2 lists `src:h` | `/result/sources/0` exists; `/result/items/0/source_refs/0` exists; result shows `prior_assessment_only`; pair op0↔result |
| S45 | A hidden availability revision changes nothing visible (non-interference) | op0: public capture. op1: private-only revision to `unavailable`. op2: private capture | result ≡ op0; op2 shows `unavailable` | result `unavailable`; op2 `resolvable` |
| S46 | A change confined to a source's availability is reported as a change, not as a gap | `a` has support and oppose roots without sources, plus documentary `src:s`. op0: capture. op1: public revision to `unavailable`. Query: `changes` since 0 | `changed`, refs `[a]`; polarity records unchanged; excerpt kept | `no_change`; excerpt `null`; support `not_found`; `cutoffs ∋ source_unavailable` |
| S47 | Erasure leaves a tombstone, also at an earlier cut | excerpt custody; an extra record at cut 101. op0: capture. op1: erase `src:s`. Query at cut 100 | op0 stays frozen in full; result has the 7-field tombstone; `erased_refs [s]` | `excerpt`, `origin`, `object` or `digest` exists |
| S48 | Audience views disclose no sources | op0: issuer_current capture (control) | empty `source_refs` and `sources` | `/result/sources/0` exists |
| S49 | Source ids cannot be probed | query targets `[visible, hidden, rec:none]`; op0 targets `[rec:none]`; op1 targets `[]` (control) | `items []`, `sources []`, result ≡ op0 | `/result/items/0` or `/result/sources/0` exists |
| S50 | The payload spends no source budget | a current-required root on `src:r`, plus documentary `src:sess`. op0 with bounds 32; query with `source_resolutions: 0` | support incomplete (`source_limit`); `sources` identical to op0 | `sources` size 0; `src:r` `unavailable`; pair op0↔result `sources` |

Existing vectors that change:
- S12 gets a tombstone and also forbids `/result/sources/0/excerpt`.
- S30 shows its excerpt.
- B13 shows an `unavailable` entry.

**Gate:**
- All 74 semantic vectors pass, and the planted violation in `validate.py` fails.
- Scenario 11: B's recall and explain show runtime, session, message, digest and the multiline excerpt byte-for-byte, with availability `unavailable`.
- After revocation B gets `not_authorized` and no data; regranting restores everything.

### 6. Risks

- **Errors in regenerated expectations.** Mitigation: generate them, check the invariant, and run two evaluators.
- **View size.** Mitigation: let the CLI shorten excerpts, and measure.
- **`origin` is overloaded.** Also, the digest covers the retained text, which is the whole message only if the whole message was kept. Document this now; the typed locator fixes it later.
- **Confidentiality inside a space is semantic only.** The CLI writes a source with its assertion's envelope, so a reader sees both or neither.

**Confidence:** high on putting the payload in the view and on dropping `withheld`; medium on the exact tombstone fields.

## Q2. Space directory

### 1. Recommendation

The directory is a set of signed objects at the adapter level, stored under the platform space's reserved `directory/` (§5.2). The space layer verifies them; the kernel never admits them. The platform space's policy owners own the directory. Publishers write entries, each only in the sections they are admitted to.

**Platform policy field** (empty in other space kinds; signed like any policy version):

```json
"directory_publishers": [
  {"identity": "owner:ivan", "sections": ["owner:ivan"]},
  {"identity": "orch:ivan-memory", "sections": ["owner:ivan"]},
  {"identity": "owner:alexey", "sections": ["owner:alexey"]}]
```

A section is an owner identity. An owner can have delegates, as in D-024.

**Entry.** Each entry lives at `directory/<hex section>/<type>/<hex key>/<version>.json` and is never rewritten. It is signed under a fifth signature purpose, `swarma-memory-directory/1`:

```json
{"entry": {"directory": "platform:swarma", "section": "owner:alexey",
   "type": "space", "key": "project:x", "version": 2,
   "previous": "sha256:<digest of v1>", "author": "owner:alexey", "status": "active",
   "body": {"kind": "project", "genesis": "sha256:<genesis policy digest>",
            "remotes": [{"url": "git@host:alexey/x-memory.git", "branch": "main"}],
            "serves": [{"type": "project", "id": "project:x"},
                       {"type": "identity", "id": "agent:x1"}]}},
 "signature": {"purpose": "swarma-memory-directory/1", "key": "ed25519:sha256:…",
               "alg": "ed25519", "value": "…"}}
```

- An `identity` entry has the body `{"keys": [...]}`: the owner's signed statement "these are my agent's keys". It is a temporary stand-in for the owner registry.
- Withdrawal is a new version with `status: withdrawn` and a null body.

**How a reader verifies:**

1. Verify the platform space's policy chain from its out-of-band genesis pin. That pin is the only out-of-band anchor left.
2. Check each entry at its first-parent position:
   - schema and path;
   - the signature, made with a key registered for `author` in the policy in force at that position;
   - `author` is a publisher for `section`;
   - `previous` and the version continue the chain, and `genesis` is unchanged;
   - the first listing of an id binds it to its section; a later listing elsewhere gets `directory_conflict`;
   - between competing versions, the first in first-parent order wins and the other gets `version_conflict` (as in D-025);
   - forged or rewritten files are diagnosed, but never hide their valid neighbours.
3. A head entry is current only while it is `active` and its author is still a publisher for that section in the current platform policy.
4. `spaces add ID --from-directory` verifies the target space's chain against `genesis`, and requires `space_id = key`, the same `kind`, and the section among the target's owners. Otherwise it fails with `directory_mismatch` and saves nothing.

**What the directory is authoritative for:** which genesis and section a space id names, owner-attested keys, which spaces serve a subject, and remote hints.

**What it is not authoritative for:**
- Access. That comes from the target space's policy plus git access control. Entries carry no access field; the "access" in §5.4 means that policy.
- A target's policy beyond the genesis pin.
- Content, currentness, or whether a space is still alive.

**Stale and revoked entries:**
- **Withdrawn space entry:** new lookups fail with `directory_withdrawn`. Spaces already configured keep their pin and keep syncing.
- **Publisher removed from the platform policy:** its entries go stale immediately, because configuration needs current endorsement (just as the broker re-checks caller grants on every lease, ch. 06). New lookups fail with `directory_stale`.
- **Withdrawn or stale identity entry:** `keys register --from-directory` fails. Keys already registered stay until that space's owner removes them; the directory never edits a space policy.

**Sharing is done per space:** `keys register --space S --identity x1 --from-directory`, then `policy grant --role reader`, then git read access.

**Stage-5 gate:**
1. Ivan creates the platform space, registers Alexey's owner key once (out of band) and admits both of them as publishers.
2. Each owner publishes its project space and its agent's identity.
3. Each owner registers the other's agent and grants it the reader role.
4. x1 runs `spaces add S_I --from-directory`, syncs and recalls i1's records; i1 does the same for S_X.

### 2. Why

- **It is configuration, upstream of the kernel.** Authority comes only from owner-signed policy, and records never create configuration (OQ-20, D-019). As kernel records, directory entries would cause three problems:
  - any platform writer could redirect readers' trust anchors;
  - reading the directory would depend on the kernel that the directory is supposed to configure;
  - entries would inherit challenge and `ambiguous_current` semantics.

  K-SCOPE-1 also fixes the number of record kinds at five.
- **Only the genesis binding needs trust.** Everything else in an entry can be checked against the target space itself.
- **It needs one key exchange per owner, not per agent.** This matches confirming the owner root once (ch. 05).
- **An access field would only go stale.** It would be an unauthenticated copy of the target policy.

### 3. Trade-offs and rejected alternatives

- **Listings inside `space.json` (rejected):** every listing would need a platform-owner policy version, and a second owner could not list its own spaces.
- **Kernel assertions (rejected):** see above.
- **An entry per share (rejected):** one reading of §5.4, but it duplicates access truth.
- **No identity entries (rejected):** the registering owner would have to trust an unauthenticated key, which D-024 already rejected.
- **First come, first served for ids (accepted):** squatting is visible and limited to admitted publishers. Self-certifying cell ids, still pending under D-010, would remove it.
- **Entry expiry and re-signing (deferred).**

### 4. Changes needed

- **Adapter and CLI, v1:**
  - A revision of the policy schema adding `directory_publishers`. `readers.spaces` must never become a transitive grant.
  - The entry schema, the fifth signature purpose, replay of `directory/` during sync, and the diagnostics above.
  - Commands: `directory publish|withdraw|list|show`, `spaces add --from-directory`, `keys register --from-directory`, `policy publisher grant|revoke`.
- **Architecture, v1:** add the field to §5.3, rewrite §5.4, list the five signature purposes in §6.1 (OQ-21), and update the related documents.
- **Decision:** a new D-027.
- **Package:** none.
- **Later:**
  - owner-registry cells replace identity entries (D-010);
  - entries are signed under the key holder's owner root;
  - federation.

### 5. Tests

**e2e Phase C** uses four homes and signed commits.

**Positive:**
- The gate in both directions.
- A key registration endorses exactly the attested key id.

**Negative,** each paired with a valid neighbouring entry:

| Case | Expected result |
| --- | --- |
| A foreign author writes in section ivan | `directory_unauthorized`; the genuine entry still resolves |
| Wrong genesis, or the section doesn't own the target | `directory_mismatch`; config unchanged |
| Withdrawn entry | `directory_withdrawn` |
| Removed publisher | `directory_stale`, while the already-configured S_X keeps syncing |
| Identity id bound twice | `directory_conflict` |
| Competing versions | first in first-parent order wins |
| Rewritten file | diagnosed |

**Independence:**
- Changes to S_I's listing leave every kernel view of S_I byte-identical.
- A listing without a reader grant, or after revocation, still returns `not_authorized`.
- File remotes don't exercise hosting access control. Run one pass against a real host, or record the gap.

### 6. Risks

- **A compromised or squatting publisher.** The damage is bounded and visible, and revocation ends it. A compromised platform-owner key compromises the directory, as it already compromises the policy.
- **Cross-owner promotion.** `promote` needs only a source reader and a target writer. Refuse it across owners unless the promoter has a forward role (K-AUTH-1, in the spirit of D-022 step 5).
- **Identity entries mistaken for the registry.** Label them temporary.

**Confidence:** high on the adapter-level design and on naming without access; medium on sections and identity entries.

## Q3. Resolvers and escalation

### 1. Recommendation

**Policy** (in the same schema revision as Q2):

```json
"resolvers": [
  {"area": "topic:agent-retirement", "identities": ["owner:ivan", "orch:platform"],
   "route": {"board": "board:swarma", "section": "platform-decisions"}},
  {"area": "*", "identities": ["owner:ivan"], "route": null}]
```

- **`area`** is an exact subject id or `*`, unique within the policy. Lookup tries the exact subject first, then `*`, then the default.
- **Default:** the space's policy owners, which can never be empty. `spaces init` writes it explicitly; an agent space may name the agent itself.
- **`route`** is an opaque pointer to a board section. `null` means the dependent task's own board.
- **Subjects:** the skill makes topic decisions use `--subject topic:…`, because the CLI's default subject is the writer.

**Authority: being named grants nothing.** Resolution uses only existing powers, and grants and keys still apply:
- **R1, supersede within the sequence.** The issuer replaces or corrects its record (K-REV-1); v1 has no representatives. A `decision_record` also needs a receipt that strictly succeeds every candidate in ≺_H (K-REV-3, D-009).
- **R2, retract evidence.** The assessment's issuer withdraws it.
- **R3, decide above.** An identity with authority over the work records its own decision, and the task owner re-points the dependency to it.

`spaces show` flags resolvers that hold no reader or writer grant.

**What conflicts can arise in v1.** Authority receipts are not integrated, and git races become `version_conflict` (D-025), so `ambiguous_current` cannot arise in git spaces. Two kinds are live:
- **Evidence conflicts.** `semantic_review` is a root kind, so a single opposing review of a supported decision creates one.
- **Incompatibility** (recommended): a declared domain relation, which is exactly the "two parallel views" D-020 rules out.

**Across spaces and owners.**
- The kernel computes conflicts per space, and no space outranks another.
- The packet has one block per space, each addressed to that space's resolvers.
- Nobody revises another owner's sequence; our resolvers decide how our work proceeds (R3).
- Under D-020's "trusted system", v1 files only to resolvers of spaces owned by the raiser's owner. Blocks for other owners' spaces go to our owner.
- A disagreement the kernel cannot see is made explicit with an attributed opposing review, or filed as a `reported` packet.

**Escalation path.**
- **Exists today:** the board (ch. 13, ch. 15).
- **Does not exist:** a Keeper escalation. The Keeper obligation ledger is target design only (`bounded-evidence.md`), and in the platform book «кипер» is the top-level orchestrator role (ch. 00).
- **v1 uses a board task:**
  1. The guard command `memory escalation DEP… --task T --step S` re-reads the exact refs. It exits 0 if there is no conflict, or 7 with the packet. `explain` also gets `--require-current`.
  2. The agent stops the dependent step.
  3. The agent or its orchestrator files one task per conflict block, in the block's route, addressed to its resolvers, with the packet attached and `conflict_key` as the dedupe key, and marks the dependent task blocked.
  4. The board notifies the resolvers.
  5. The resolvers apply R1–R3 and close the task with references to the new records.
  6. The guard now exits 0, and the step resumes.

**Packet** (closed schema, references only):

```json
{"format": "swarma-memory-escalation/1", "data_classification": "data",
 "raised_by": "agent:a3", "raised_at": "2026-10-21T10:00:00Z",
 "dependent": {"task": "TASK-…", "step": "enable-retirement-hook"},
 "dependency": [{"space": "project:swarma", "ref": {"id": "record:retire-rule", "version": 2}}],
 "conflicts": [{"conflict_key": "sha256:…", "space": "project:swarma",
   "cursor": "<verified commit>", "policy": {"version": 7, "digest": "sha256:…"},
   "kind": "evidence_conflict",
   "items": [{"ref": {"id": "record:retire-rule", "version": 2},
     "subject": "topic:agent-retirement", "schema": {"id": "schema:rule", "version": 1},
     "issuer": "agent:a1", "currentness": "current", "support": "present",
     "oppose": "present", "incompatible_with": []}],
   "owners": ["owner:ivan"],
   "resolvers": {"area": "topic:agent-retirement", "basis": "named",
     "identities": [{"identity": "owner:ivan", "reader": true, "writer": true}],
     "route": {"board": "board:swarma", "section": "platform-decisions"}}}]}
```

- `kind` is one of `ambiguous_current`, `evidence_conflict`, `incompatible` or `reported`.
- `basis` is one of `named`, `wildcard` or `default_owners`.
- `conflict_key` hashes `{space, kind, sorted refs}` without the cursor or the raiser, so different raisers of the same conflict converge on one task.
- The packet carries no record content.

### 2. Why

- **D-020 and §10 already fix who stops and who records.** This design adds only addressing, so revision authority is unchanged (K-REV-1, K-REV-3, D-009).
- **The subject is the only exact key the kernel exposes for a decision slot** (K-DOM-2). Prefixes or free text would mean parsing ids or prose (K-ENV-1).
- **Owners are always present and accountable.**
- **The board is the escalation path that works today.** Memory may not enqueue work or wake anyone (`swarma.md`), and «оркестратор просит, а не судит» (ch. 13).
- **References, not content.** Forwarding content would need a separate right (K-AUTH-1).

### 3. Trade-offs and rejected alternatives

- **Keeper now (rejected):** it would invent a component.
- **Areas by label, prefix or schema (rejected).**
- **Being named equals being authorized (rejected):** it would bypass revision authority.
- **Content in packets (rejected).**
- **Signing packets (deferred to Keeper records):** the board already authenticates whoever files the task, and the refs can be re-checked.
- **Stopping on incompatibility** is my reading of D-020. Drop it if you want the strict minimum of §10.

### 4. Changes needed

- **Adapter and CLI, v1:**
  - area semantics and `route`;
  - the resolver diagnostics;
  - the `escalation` command and its packet schema;
  - `--require-current` on `explain`;
  - the conflicts section in `SKILL.md`.
- **Architecture, v1:**
  - §10 step 3 becomes "board task".
  - §10 step 4 lists R1–R3: "with their receipt" is impossible until receipts are integrated.
  - §5.3 gets a resolvers row.
- **Decisions:** D-020 stands; record the board path as the v1 choice.
- **Package:** none.
- **Later:**
  - receipt integration (board revisions or decision-register commits as canonical events), which makes `ambiguous_current` possible;
  - Keeper obligation records that carry this packet with deadlines.

### 5. Tests

**G6a, memory e2e Phase D.** Setup: owner O; writers a1, a2 and a3; the area `topic:retire` routes to O.

1. a1 records decision D (with supporting evidence), and a2 records an opposing review.
2. a3's guard exits 7. a3's dependent write E is not published. The packet is exact, and its key matches the one a1 gets.
3. a1 replaces D. The guard exits 0 and E is published.

Controls:

| Control | Expected result |
| --- | --- |
| A conflict on another topic | does not block |
| a3 tries to replace D | `representation_invalid`; the guard still exits 7 |
| a3 writes its own competing assertion | does not clear the conflict |
| No matching area | basis `default_owners` |
| Content fields in the packet | forbidden |
| Hidden opposition | does not block (S13, plus a CLI unit test) |
| A snapshot in the S28 state | the unit test exits 7 with `ambiguous_current` |

Whether models actually obey the skill is measured in stage 7.

**G6b, board integration**, run in the board's own test harness:
- the packet lands addressed to O in the route;
- refiling with the same key creates no duplicate;
- the dependent task stays blocked until the conflict is resolved.

The stage-6 gate passes when both G6a and G6b pass.

### 6. Risks

- **Opposition works as a veto.** One review can stop every dependent step. Mitigations: stops apply per dependency, every review is attributed, R1 stays available because assessments pin exact versions, and writers can be revoked. Measure how often this happens.
- **An oppose-only decision does not stop work.** A single opposing review of a documentary decision with no supporting evidence is not a conflict, so dependents proceed. Stopping in that case would widen D-020.
- **Workers may lack board rights.** Their orchestrator files the task instead.
- **Subject discipline.** Areas only work if decisions use the right subjects.
- **`ambiguous_current` stays untested in git** until receipts exist.

**Confidence:** high on "board now, Keeper later" and on naming without authority; medium on subject-based areas and the packet shape.

## For the owner

1. **Q2.** Who owns the platform space, and do you admit a second owner as a publisher? Doing so means trusting their signed statements about their agents' keys.
2. **Q3.** Is a second owner part of D-020's "trusted system", so that our agents may escalate to them? I recommend not in v1.
3. **Q3.** Name the resolvers for the platform-space areas and the board that receives platform escalations. This is governance; the material cannot settle it.
4. **Q3.** Do platform decisions bind project spaces? Memory will not rank spaces. If you want precedence, it has to be a rule the resolvers apply.
5. **Q2.** May readers of a shared space promote its records into their own spaces? I recommend not without a forward grant.
6. **Q1.** Do you approve package 0.3.0? It changes the view's wire format. D-016, §7.2 and §8 already decide the behaviour, but the e2e README asks for your explicit go.
