# Panel answer: Q1 (OQ 23), Q2 (OQ 9), Q3 (OQ 8)

Three facts from the material decide most of what follows.

- **Q1.** The kernel already authorizes sources. `source_refs` lists only sources that pass read, use, metadata, label, deadline and context checks. A hidden source makes the whole citation ineligible (K-AUTH-1; `associatedSources` and `ruleEligible` in `go/kernel`). K-EVAL-9 already says source metadata follows content visibility. So the fix is to emit the bodies of those same records, not to open a second access path.
- **Q2.** The directory hands out trust anchors (genesis pins). That makes it policy-level, like `space.json`, not knowledge.
- **Q3.** In v1 git spaces `ambiguous_current` cannot occur. The provisional profile has no authority events, so `decision_record` is refused (`cli.md`, `agentprofile/empty.json`). Stage 6 therefore runs on evidence conflicts. Naming someone a resolver gives them no authority; only issuers, or the deciding authority, can supersede.

## Q1. Session-excerpt sources are not visible to readers

### 1. Recommendation

Put a disclosure-filtered source payload in the view: a new required top-level `sources` array, computed in the same authorized read. There is no new operation.

```json
"sources": [{
  "ref": {"id": "rec:queue:source", "version": 1},
  "issuer": "ivan/agent:dev-7", "submitter": "ivan/agent:dev-7", "admission_class": "machine_observation",
  "owner": "runtime:claude-code", "source_kind": "artifact",
  "object": "session:5f2c…", "revision": "message:msg_01H…",
  "digest": {"algorithm": "sha256-bytes-v1", "value": "9b1c…"},
  "provenance": "reported", "origin": "<canonical locator JSON>", "original_issuer": "ivan/agent:dev-7", "carrier": null,
  "availability": "unavailable",
  "excerpt": {"state": "present", "text": "Decision: use a bounded durable queue\n"}
}]
```

`excerpt` takes exactly one of three forms: `{"state":"present","text":…}`, `{"state":"none"}` or `{"state":"erased"}`. All fields are required and the object is closed.

**New clause K-SRC-1:**

1. **Closure.** `sources` is exactly the deduplicated union of the displayed items' `source_refs`, sorted by (id, numeric version). An eligible source that no displayed item cites is left out, so sources cannot be enumerated on their own.
2. **Fields.** The payload carries the source's envelope issuer, submitter and admission class, plus its body without `retention_admission`. `recorded`, `lineage` and `disclosure` stay protected.
3. **Effective `availability`**, judged at the view's source frontier:
   - `erased` if the record is fenced or erased (K-ERASE-1), or its stored or latest *authorized* revised availability is `erased`;
   - otherwise `unavailable` if the stored or revised state is `unavailable`, or a `source_access` fact denies resolution;
   - otherwise `resolvable`.

   Hidden availability revisions are ignored, as `sourceAvailable` already does.
4. **`excerpt`:**
   - `erased` whenever availability is `erased`, which also hides whether an excerpt existed;
   - `none` if no excerpt was retained;
   - otherwise `present`, with the exact bytes.

   `unavailable` never suppresses a retained excerpt (D-016). A retained excerpt is not a resolution: it never satisfies `source_requirement: current` and never raises `source_state`.
5. **Audience projections** carry `sources: []` (this extends K-DISC-2 and K-PUB-1).
6. **Changes.** The payload counts as visible content in `changes`: an item is "changed" when a source it cites changed.
7. **Captures** freeze `sources` together with the items (K-SNAP-1). Delivery rechecks rights exactly as it does today.

| Brief's state | Contract |
|---|---|
| available | `availability: resolvable`: the original resolves at the frontier. This never happens in v1, because the git profile marks every source unresolvable and there is no session-host resolver. |
| unavailable | `availability: unavailable`: the session was deleted, or there is no resolver. The excerpt stays `present`. This is the normal v1 state. |
| erased (added) | The header survives with `excerpt: erased`, and the bytes are never shown. |
| withheld | Not a state on the wire. |

**What a reader without the right sees: nothing.** This applies when the reader lacks read, use or metadata on the source, when the source's labels exclude the query's audience or purpose, or when its retention deadline has passed. Such a reader gets:
- no ref, no payload, no marker and no count;
- no citation that names the source, because that citation becomes ineligible, so the item simply looks uncited.

A reader without access to the space gets `not_authorized`, as today.

**Adapter mapping for session excerpts** (`swarma.md` and the CLI):

| Source field | Value |
|---|---|
| `owner` | `runtime:<runtime>` |
| `object` | `session:<id>` |
| `revision` | `message:<id>` or `index:<n>` |
| `digest` | `sha256-bytes-v1` of the raw message text |
| `origin` | the canonical locator, so there is one root origin per message and copies never count as independent (K-DISC-3) |
| `provenance` | `reported`: the text is the agent's transcription, and nothing authenticates it against the session host |
| availability | `unavailable` until an admitted session-host export exists |

### 2. Why

- **No new access decision.** The payload is the content of records that are already eligible. Closure makes it a function of `source_refs`, which already goes through the eligibility path that S13, S24 and B07 constrain.
- **Absence instead of a marker.** `findings/view-inference.md` treats locators, digests and source authors as protected outputs. It also requires that denied, unknown and erased stay indistinguishable unless the caller may know the difference.
- **There is no partial state to build on.** K-AUTH-1 explicitly has no metadata-only shape, so a real `withheld` would need a second label.
- **One read keeps views self-contained.** Frozen views and the later D-001 snapshot carry their sources, and `changes` sees availability changes.
- **It fixes the general case too.** Decision readers finally see the exact receipt or document revision — the book's «назвать действующее решение и его точный источник».

### 3. Trade-offs and rejected alternatives

| Alternative | Verdict and reason |
|---|---|
| Separate source-read operation | Rejected. It needs a new query kind, scope semantics (sources have no schema or perspective), its own capture, changes and delivery rules, and protection against an oracle for guessed refs. Once bound to a citing item, it is this design plus an extra round trip. |
| Payload inside each item | Rejected. It duplicates shared sources and changes the `source_refs` shape in every vector. |
| A `withheld` marker | Rejected. It leaks existence and count, and fails S13-style pairs. A label-based `withheld` excerpt, shown only to readers already authorized for the header, belongs to the later protected profile. |

**Costs of the chosen design:**
- views get bigger, bounded by `max_field_bytes` and by cited sources only;
- every expected view in the package must be regenerated, which is mechanical and cross-checked by both evaluators.

### 4. Changes needed

**v1:**
- **Package release 0.3.0-draft:**
  - add `sources` to `view.schema`;
  - add `sha256-bytes-v1` to the digest enum in `source.schema` (K-JSON-2: SHA-256 of the exact bytes, no framing);
  - add K-SRC-1, and amend K-EVAL-9, K-DISC-2 and K-ERASE-1;
  - regenerate the expected views;
  - fix the URN and version labels in the same release (OQ 18);
  - add a closure check to `validate.py`.
- **Adapter:** the mapping above.
- **Implementation:**
  - the kernel read builds `sources` and the CLI passes it through;
  - delete the limitation in `cli.md` and the line "readers see source refs" in `SKILL.md`;
  - legacy records, which carry the locator in `origin` and the digest in `object`, stay valid and render as stored.
- **Architecture:** add the mapping to §7.2; §8 then says views carry source payloads.
- **Decisions:** none.

**Later:** a session-host export as resolver, excerpt labels with `withheld`, and erasable excerpts in the protected service.

### 5. Tests and vectors

| Vector | Claim | Expected / forbidden |
|---|---|---|
| S43 | Locator and excerpt are disclosed with their citation | Payload as above. Forbidden: support witness `present` (documentary basis, S22), `availability: resolvable`, `source_state: resolvable_now`. |
| S44 | Deleting the session keeps the retained excerpt | The issuer's `availability` revision moves it from resolvable to unavailable; the excerpt stays `present`; `changes` reports `changed` with the citing ref. Forbidden: excerpt `erased`, oppose `present`. |
| S45 | A fenced source keeps its header but never its bytes | `erased` / `erased`. Forbidden: `/result/sources/0/excerpt/text` exists. Add the same predicate to S12. |
| S46 (NI) | A hidden extra citation changes nothing for the public reader | Public capture, then hidden `aud:private` source and basis admitted, then public result: these are `equivalent_outputs`. A private capture shows both (positive control). Forbidden: `sources` or `source_refs` of size 2. |
| S47 (NI) | A visible source cited only by a hidden justification stays absent | Paired with a control state that has no such source. |
| S48 | An audience projection discloses no source | `sources: []` (or extend P05). |
| S49 (NI) | A hidden availability revision is ignored | No change; a private capture shows `unavailable`. |
| S50 | Write-side refusals | An excerpt without `retention_admission` gives `invalid_reference`; a malformed or unknown digest gives `invalid_shape`. |

**Controls.**
- `validate.py` must reject a planted vector whose `sources` holds a ref that no item cites.
- In Go, the mutation "build sources from all scope sources" must fail S46 and S47.
- The mutation "emit text while fenced" must fail S45.

**Gate: upgraded e2e scenario 11.**
- B's recall and explain show the exact runtime, session, message and digest, the multiline excerpt bytes, and `unavailable`.
- After revocation B gets `not_authorized` with no data.
- Re-granting access restores it.

### 6. Risks and confidence

- **Excerpts reach model context more often.** They are verbatim and may contain imperatives; they remain data only (B04).
- **Excerpts live forever in git** (D-003). The scanner and the non-sensitive rule therefore matter more now.
- **Fencing through hidden lineage** reveals that something upstream was erased. This is already accepted for assertions.

**Confidence:** high on the choice and on the absence rule; medium on field naming and on `provenance: reported`.

## Q2. The space directory: format and owner

### 1. Recommendation

Each owner keeps their own directory of owner-signed entries in their platform space. Each entry is an adapter-level signed object with a fifth purpose, `swarma-memory-directory/1`. It is not a kernel record.

Entries live at `directory/<hex(space_id)>/<version>.json` and are valid only in spaces of the platform kind.

```json
{"entry": {"directory": "space:platform:ivan", "space_id": "space:project:alpha", "version": 2,
  "previous": "sha256:…", "author": "ivan/owner", "kind": "project", "subject": "project:alpha",
  "home": "local", "remote": "ssh://git@github.com/relux-works/alpha-memory.git", "branch": "main",
  "genesis": "sha256:…", "status": "active", "observed_policy": {"version": 7, "digest": "sha256:…"},
  "owners_hint": ["ivan/owner"], "readers_hint": ["ivan/agent:a1", "b/agent:b1"]},
 "signature": {"purpose": "swarma-memory-directory/1", "key": "ed25519:sha256:…", "alg": "ed25519", "value": "…"}}
```

`subject` is the agent identity for agent spaces, the project-registry id for project spaces, and the platform id for platform spaces.

**Ownership and signing:**
- **Owner of the directory:** the platform space's `owners`, that is, the installation owner.
- **Author:** must be an owner in the policy in force at the entry's first-parent position, with a registered key. One signature suffices.
- **No agent-written entries in v1.** An injected agent must not be able to redirect discovery.
- **How entries are built:** the owner's CLI builds each entry from a verified clone. It copies genesis, kind, id, policy digest and hints, so nothing is typed by hand.

**Verification by a reader:**
1. **Pin.** The reader pins its own owner's platform space out of band, once. This is today's `--genesis`, and it is the only manual pin an agent needs.
2. **Replay.** Entries are replayed in first-parent order, like records:
   - schema and purpose check;
   - `directory` must equal the platform id;
   - the author must be an owner in force, with a registered key;
   - version chain: version 1 has `previous: null`, and each later version names the digest of the accepted previous one;
   - the first accepted version wins, as in D-025; a competitor gets `directory_sequence`;
   - an edited file gets `directory_rewritten`.
3. **`spaces add ID --from-directory`:**
   - clones the remote and verifies the policy chain against `genesis`;
   - requires equal `space_id` and `kind`;
   - requires the verified policy version to be at least `observed_policy.version` (a rollback floor for the first clone).

   Otherwise it refuses with `directory_mismatch` and configures nothing.
4. **No silent re-pin.** A space that is already pinned is never re-pinned silently (`genesis_conflict`). The same genesis with a new remote is a safe relocation.
5. **Remotes are data.** Only ssh and https are allowed (plus file in tests), via `protocol.allow`, and the remote is passed after `--`.

**What the directory is authoritative for, inside one installation:**
- space id → endorsed genesis and fetch location;
- the owner's lifecycle status;
- the mapping from identity or project to space.

**What it is not authoritative for:**
- read and write rights (the space policy);
- git access (the hosting ACL);
- key ownership;
- record validity and currentness.

`readers_hint` is a cache pinned to `observed_policy`. A mismatch is only a diagnostic, and the space policy wins.

**Stale and revoked entries:**

| Situation | Behaviour |
|---|---|
| Newer version | Supersedes the old one; history remains. |
| `retired` | Readable as history; the CLI refuses new writes (`space_retired`). |
| `revoked` | Terminal. Directory-provisioned clones stop syncing and reading (`space_revoked`). Bytes already fetched cannot be recalled. Reuse needs a new id and genesis. |
| Remote unreachable or access lost | `git_failed` for that space only. The last verified state is kept, and this is never treated as negative evidence. |

**Cross-owner sharing (stage 5).** Each agent trusts only its own owner's directory. For A's space P1 and B's agent b1:
1. **Out-of-band exchange.** v1 has no owner registry, so B sends A the qualified id and public key of b1, and A sends B P1's remote and genesis (`spaces show`).
2. **A grants access.** As owner of P1, A runs `keys register` for b1 and `policy grant --role reader` (the authoritative step), grants git read (the physical gate), and refreshes P1's own entry.
3. **B vouches for P1.** B adds an entry with `home: foreign` for P1 to B's directory, vouching for its genesis.
4. **b1 reads.** b1 syncs B's platform space, runs `spaces add P1 --from-directory`, and reads P1 as itself.

Conditions:
- v1 cross-owner access is **read-only**; guest writes come later via D-022.
- Ids are **owner-qualified** (`<owner>/<id>`). `keys register` refuses a foreign key on an unqualified or local id; otherwise B could add a key to A's identity.
- No platform space is shared across owners just to expose its directory.

This corrects architecture §5.4: sharing means a reader grant and key in the space policy, git access, and an entry in the other owner's directory.

### 2. Why

- **No registries inside the kernel.** «Участники и пространства знаний не образуют собственных реестров», and the kernel must stay portable (D-002). Signed records must never manufacture trust anchors (`git-spaces.md`), so the directory belongs beside `space.json` and key registrations.
- **The anchor already exists.** Genesis is already the out-of-band anchor (`cli.md`). The directory moves pinning from each agent to the owner, while chain verification keeps it checkable.
- **Returning agents find their space.** A returning persistent agent (D-026) needs only the platform pin to rediscover its agent space.
- **Access truth stays where it lives** (D-019).
- **One owner, one root.** One installation has one owner and one root of trust (platform book ch. 16), and v1 excludes cross-owner federation (book).

### 3. Trade-offs and rejected alternatives

| Alternative | Verdict and reason |
|---|---|
| Directory entry as a kernel record kind | Rejected. Trust bootstrap would depend on evaluating the very spaces being bootstrapped, and knowledge grants nothing. |
| Entries inside the platform `space.json` | Rejected. Every change would re-endorse every key registration. |
| One shared directory, or reading the other owner's directory | Rejected. It shares the whole platform repo and amounts to federation. |
| Authoritative `access` field in entries | Rejected. It creates two sources of truth. |
| `public` reader plus git ACL | Fallback only. It mislabels non-public data and loses per-identity revocation. |

### 4. Changes needed

**v1:**
- **Adapter:**
  - closed `directory-entry` schema and the fifth purpose;
  - replay and verification;
  - the diagnostics listed above;
  - config records which directory provisioned each space.
- **CLI:**
  - `directory put|list|show` and `spaces add --from-directory`;
  - the qualified-id check in `keys register`;
  - the protocol allowlist.
- **Architecture and docs:**
  - rewrite §5.4 and add the path to §5.2;
  - in §6.1, name the fifth purpose next to the write purpose from OQ 21;
  - update `git-spaces.md`.

No package or decision changes are needed.

**Later:**
- identity cells and the owner registry replace qualified strings and the manual key exchange;
- delegated `directory_writers`;
- the key holder signs entries;
- federation.

### 5. Tests and vectors

These are adapter and e2e tests only; the kernel is unchanged.

**Positive cases:**
- an entry signed by an owner is listed;
- `--from-directory` configures the space and reads work;
- a relocation with the same genesis keeps the cursor;
- after its home is wiped, a persistent agent rediscovers its space with only the platform pin.

**Negative cases** (each next to a valid neighbour):

| Case | Expected result |
|---|---|
| Entry signed with an agent key | `directory_unauthorized` |
| Wrong genesis | `directory_mismatch`, nothing configured |
| Competing version 2 | `directory_sequence` |
| Edited entry file | `directory_rewritten` |
| Entry inside a project space | Ignored |
| Existing pin against a different genesis | `genesis_conflict` |
| `ext::` remote or remote starting with `-` | Refused before git runs |
| Identity listed in `readers_hint` without a grant | `not_authorized` |
| Entry `revoked` | `space_revoked` for that space only |
| Remote rolled back below `observed_policy` | Refused |

**Non-interference.**
- P1's views are identical, modulo handles, whether P1 was pinned by hand or from the directory.
- Writes to the directory change no kernel view.

**Gate (e2e).** Setup: owners O1 and O2, each with a platform space and a project space; agents a1 and b1 with separate homes; the key and genesis exchange described above.
- Each agent finds the other owner's project only through its own directory, and recalls the other agent's assertion with the correct issuer.
- When O2 revokes a1, a1 gets `not_authorized` on P2 while its own spaces keep working.
- When O1 removes b1's git access, b1 gets `git_failed` and keeps its last verified view.
- A write by b1 to P1 gets `not_authorized`.

### 6. Risks and confidence

- **A compromised owner key redirects new clones.** Mitigated by refusing silent re-pins, by the rollback floor and by `revoked`.
- **Manual exchange is error-prone.** Skipping the qualified-id rule makes impersonation possible.
- **Revocation does not recall history** that was already fetched.
- **Sharing becomes visible.** Foreign entries reveal sharing relationships to every reader of the platform space.

**Confidence:** high that the directory is adapter-level and not access truth; medium on the exact field set and the status semantics.

## Q3. Who resolves which conflicts, and the escalation path

### 1. Recommendation

**Resolvers in the space policy** (adapter schema `space:2`):

```json
"resolvers": [
 {"area": "lifecycle", "match": {"schemas": [{"id": "schema:rule", "version": 1}], "subjects": ["subject:home-retention"], "kinds": []}, "identities": ["ivan/owner"]},
 {"area": "reviews", "match": {"schemas": [], "subjects": [], "kinds": ["evidence_conflict"]}, "identities": ["ivan/owner", "ivan/agent:architect"]}]
```

**Selector.**
- **Schemas:** exact schema refs.
- **Subjects:** exact subject ids. No prefixes, because ids are opaque (K-ENV-1).
- **Kinds:** `ambiguous_current`, `evidence_conflict`, `incompatible` or `reported`.
- **Empty list:** means any.
- **Matching:** the first matching entry in the signed policy order wins.
- **Default:** the space `owners`.

**Validation when the policy is signed.**
- `area` is unique.
- Every resolver holds both reader and writer grants in the space, so it can verify the conflict and record a resolution.
- Every schema ref in a selector is listed in `schemas`.

Legacy `space:1` entries are read as catch-alls.

**Resolver authority.** Being named grants nothing: no right, no representation, no override. Recording a resolution takes a writer grant plus existing revision authority:

| Conflict kind | Who can end it | How |
|---|---|---|
| `ambiguous_current` | Only the deciding authority (K-REV-3) | A new canonical event that strictly succeeds both candidates, imported as the next version. Memory-side replacement cannot do this (B02, S39). Not producible in v1. |
| `evidence_conflict` | The assertion's issuer, or the issuer of an assessment | `replace` or `correct` (the old assessments stay pinned to the old version, K-REC-2), or `withdraw` one's own assessment |
| `incompatible` | Either assertion's issuer | replace or withdraw |
| `reported` (across spaces or owners) | Nobody can order these in memory (D-009) | A decision in the space that owns the dependent work, citing the other one as a source |

**When the resolver is not the issuer.** A resolver who is not the issuer still decides the question. Then either the issuer records that decision, or the resolver records its own decision and the step switches to it, as stated in the board outcome. The conflicted sequence stays visible and blocks nothing else (D-020).

**No delegation through the policy.** Representation-based resolution waits for registry grants (D-010). Putting delegations into the space policy would create the second delegation registry that the adapter forbids.

**Triggers:**
- `ambiguous_current`;
- both witnesses `present`;
- a non-empty `incompatible_with`, which I add within D-020: it is the kernel's deterministic statement that two current assertions disagree on one slot.

Use an exact scope: `recall --subject S --schema X --require-current`. Substring matching causes false stops.

**Across spaces and across owners.**
- The kernel evaluates each space on its own, so the agent reports such conflicts with `memory conflicts --ref SPACE:ID:VERSION …` (`kind: reported`).
- The resolvers of the space that owns the dependent work decide; other local spaces' resolvers are informed.
- Resolvers of `home: foreign` spaces (from the Q2 directory) are informational only, since they are not "part of the trusted system" (D-020).
- v1 cross-owner access is read-only, so no cross-owner conflict can form inside one space.

**Escalation path.**
- **Exists today:**
  - the task board, with tasks, roles, review and a `blocked` status (ch. 15 ⟦работает сегодня⟧; the memory board's TASK-261019-gak2ji is blocked);
  - Matrix bells;
  - a decided behaviour that «Заблокировано» notifies the orchestrator or a human (ch. 09).
- **Does not exist:** a Swarm Keeper escalation. «Кипер» is a top-level orchestrator role (ch. 00). The obligation ledger is target design, with no spec and no module (`bounded-evidence.md`), and the adapter forbids a second obligation ledger inside memory.
- **v1: a board task addressed to the resolvers.**
  1. The agent stops the dependent step, marks its own task `blocked` and attaches the packet. With no board task, it returns the packet to its caller.
  2. The orchestrator opens a resolver task assigned to `resolvers` and links it as the blocker.
  3. The resolver reproduces the conflict from the pins and records the resolution, citing the board task as a source (owner `board:…`, object the task id, revision the board revision).
  4. The orchestrator unblocks, and the agent reruns the check, continuing on exit 0.
- **What memory does in this path:** memory makes no board call and stores no escalation records.
- **Later:** Keeper tracks the escalation as an obligation with a deadline. The packet does not change.

**The packet** is the `data.conflicts` field returned with exit 7, and also the output of `memory conflicts`:

```json
{"format": "swarma-memory-conflict/1", "data_classification": "data", "raised_by": "ivan/agent:dev-7",
 "step": "board:alpha/TASK-261021-k2", "read_at": "2026-10-21T12:00:00Z", "cursor": "memory:1:…",
 "conflicts": [{"kind": "evidence_conflict", "space": "space:project:alpha", "commit": "…",
   "policy": {"version": 7, "digest": "sha256:…"},
   "scope": {"subject": "subject:home-retention", "schema": {"id": "schema:rule", "version": 1}, "issuer": "ivan/owner", "perspective": {"kind": "own", "principal": "ivan/owner"}},
   "items": [{"ref": {"id": "rec:home-rule", "version": 1}, "issuer": "ivan/owner", "currentness": "current"}],
   "related": [], "proofs": [[{"id": "rec:review-a", "version": 1}], [{"id": "rec:review-b", "version": 1}]],
   "area": "lifecycle", "resolvers": ["ivan/owner"], "resolver_basis": "policy_area"}]}
```

- **No content.** The packet carries refs and pins only. Resolvers are readers by validation, and forwarding content to the board's audience would need `forward` (K-AUTH-1).
- **Built only from the caller's authorized views:**
  - `items[].issuer` names who can supersede;
  - `proofs` come from an authorized `explain`;
  - `step` is opaque caller data;
  - there are no command strings.

### 2. Why

- **"Under the existing order rules" decides it.** D-020 says the resolution supersedes the conflicting decisions under the existing order rules. K-REV-1, K-REV-3 and D-009 let only issuers, checked representatives or the deciding authority supersede. Anything else would be an override the kernel forbids.
- **The default works.** Owners are always present and accountable, and validation guarantees that named resolvers can actually act.
- **The board is the only real path.** It is the only existing path that is durable, assignable and visible to humans.

### 3. Trade-offs and rejected alternatives

| Alternative | Verdict and reason |
|---|---|
| Resolvers that override other issuers | Rejected. It breaks K-REV-1 («поздняя заметка агента … не заменяет решение владельца»). |
| Representations in the space policy | Rejected. It creates a second registry, against D-010. |
| Prefix selectors on subjects | Rejected. They parse ids. |
| Board ids in the memory policy | Rejected. It couples memory to the transport. |
| Content in the packet | Rejected. It is disclosure to the board's audience. |
| Keeper first | Rejected. It is not built. |

### 4. Changes needed

**v1:**
- **Package:** none. K-REV-4, S02, S28 and P14 already cover the outcomes.
- **Adapter:** policy `space:2` with `match`, validation and legacy reading.
- **CLI:**
  - exact-scope recall;
  - the exit-7 packet and `--step`;
  - `memory conflicts --ref`;
  - the `incompatible` trigger;
  - `policy resolvers set|show`.
- **Skill:** the steps above. Never self-resolve unless you are both a resolver and the issuer.
- **Architecture:** update the resolvers row in §5.3; §10 step 3 becomes a board task in v1 and Keeper later; mark Keeper as target design in §2.
- **Decisions:** none change. The owner confirms the route (see below).

**Later:**
- Keeper;
- registry representations;
- authority-receipt integration from the board or the decision register, which makes `ambiguous_current` real;
- role-based resolvers;
- platform-level defaults.

### 5. Tests and vectors

**Positive cases:**
- an evidence conflict exits 7, and the packet carries the area's resolvers;
- with no matching entry, the packet names the owners (`space_owners`);
- after the issuer's `replace`, the recheck exits 0 and version 2 is current;
- withdrawing the opposing assessment makes the recheck exit 0;
- incompatible team-perspective rule facts exit 7;
- an `ambiguous_current` packet can be built from a test-profile snapshot that has authority events (unit test; kernel S28).

**Negative cases:**
- a conflict on another subject leaves the result at exit 0;
- a `replace` by a resolver who is not the issuer gets `representation_invalid`, and the result stays exit 7;
- such a resolver's own decision does not override the original;
- a resolver without reader and writer grants is refused when the policy is signed;
- resolvers from a forged policy or a losing fork are ignored;
- `memory conflicts --ref` returns the same `record_not_found` for a hidden ref and a nonexistent ref.

**Non-interference.** Paired states that differ only by a hidden opposing assessment give identical recall data and exit 0, with no packet.

**Gate (stage 6).**
1. **CLI e2e.** O writes a rule; R1 assesses it in support and R2 in opposition. A runs `recall --subject … --require-current --step T1`, gets exit 7, and the packet is addressed to O. O replaces the rule, and A's recheck exits 0.
2. **Platform acceptance on the real board.** The installed agent stops before the dependent write. The orchestrator files the resolver task with the packet, the resolver records the decision, and the task resumes. Evidence stays on the board.

### 6. Risks and confidence

- **Any writer can stall dependent work** by writing an opposing passing `semantic_review`, because model executors count as roots.
- **`ambiguous_current` cannot be tested end to end in v1.**
- **Stopping is enforced only by the skill.** Measure it in stage 7.
- **Escalations can stall** when resolvers lack authority. This is mitigated by `items[].issuer` and by validation.

**Confidence:** high on the authority rules and the route; medium on the selector and on precedence.

## For the owner

1. **Escalation route for v1.** Should it be a board task (with Keeper later), where agents only block their task and attach the packet, and orchestrators open the resolver tasks? OQ 8 left this open, and it changes board and orchestrator workflows that memory does not own.
2. **May a model-made opposing review alone stop dependent work?** The alternative is to let only human, test or formal evidence stop work. This trades safety against denial of service by autonomous writers (D-011), and the book leaves it to «политика потребителя».
3. **Cross-owner trust in v1.** Do you accept a manual exchange of genesis pins and agent keys, foreign agents as named readers in our spaces, and owner-qualified ids — or should this wait for the owner registry? This is a trust decision between owners.
4. **Precedence when a platform decision and a project decision conflict.** My default is that the project's resolvers decide and the platform's resolvers are informed. This is a governance call.
5. **Approve package 0.3.0.** Every reader of a space will then see retained excerpts and exact sources in recall. The e2e README already marks this as the owner's call.
