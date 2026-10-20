## Q1. Expose source payloads through the existing kernel view

**1. Recommendation**

Add a required, deduplicated `sources` table to `View`. Keep `items[].source_refs` as its links. Sources remain one of the five stored record kinds; they do not become assertion items.

Use this closed shape, with existing package types and enums:

```typescript
View.sources: SourceView[]

SourceView = {
  ref: VersionRef,
  attribution: {
    issuer: string,
    submitter: string,
    perspective: Perspective,
    admission_class: AdmissionClass
  },
  availability: "available" | "unavailable",
  locator: Cell<{
    owner: string,
    source_kind: SourceKind,
    object: string,
    revision: string,
    digest: SourceDigest | null,
    provenance: Provenance,
    origin: string,
    original_issuer: string,
    carrier: string | null
  }>,
  excerpt: Cell<string>
}

Cell<T> =
  { state: "available", value: T } |
  { state: "unavailable", value: null }
```

All objects reject additional fields. Entries are sorted by `(id, numeric version)`. The table contains exactly the union of the source references disclosed by displayed items, with one entry per exact reference.

**Disclosure and availability are separate:**

| Situation | Reader sees |
| --- | --- |
| Authorized source, original resolves | Locator, any retained excerpt, `availability: available` |
| Original session unavailable, admitted excerpt survives | Locator and excerpt, `availability: unavailable` |
| Authorized structural source reference survives erasure | Reference and permitted attribution; unavailable cells contain no bytes |
| Source or association is unauthorized | No source entry, reference, placeholder, count or source-specific error |
| `audience_projection` | `sources: []`, preserving its existing suppression of internal provenance |

**Withheld means omission, not an entry saying “withheld.”** Such an entry would disclose the existence and possibly the number of hidden sources. An empty table makes no claim that undisclosed sources do not exist.

The kernel must:

- Apply existing read/use/metadata, disclosure, lineage, revision and disposition checks before constructing the table.
- Preserve the current rules that filter an assessment or justification with inaccessible sources.
- Suppress erased locator material, including digests and `origin`, rather than treating everything except `excerpt` as harmless metadata.
- Include disclosed source payloads and availability in `changes` comparisons.
- Preserve both evidence channels unchanged. Reading an excerpt creates neither a witness nor a fresh source check.

`availability` reports effective original-source resolution at the admitted frontier. `excerpt.state` reports whether the retained excerpt can be returned. This distinction is essential: deleting a session must not make its independently retained excerpt unreadable.

No network resolution happens inside this projection. The CLI renders the kernel’s output and never supplements it from `Snapshot()`.

**2. Why**

This directly repairs OQ23 and fulfills D-016 without adding another read protocol. It follows [the normative contract](bundle/repo/spec/kernel/semantics.md): K-AUTH-1, K-EVAL-5, K-EVAL-9, K-DISC-2, K-NI-1 and K-ERASE-1.

The implementation already computes authorized associations in `go/kernel/evaluate.go`. Extending that result is smaller than introducing an independently addressable source endpoint.

Existing session locators are recoverable without changing stored source schemas: `docs/cli.md` documents canonical locator JSON in `body.origin`, the raw-text digest in `body.object`, and text in `body.excerpt`.

**3. Trade-offs and rejected alternatives**

Inline payloads enlarge responses. A view-level table avoids repeating excerpts for every citing assertion; existing record and field limits bound admitted inputs.

Reject an adapter-side lookup: it would create a second disclosure implementation. Defer a separate source-read operation until response-size measurements justify its additional authorization, snapshot and error contracts.

Do not expand audience publication to expose source provenance. Releasing a conclusion does not release its inputs.

**4. Changes needed**

- **Package — v1:** Release a new profile, preferably `0.3.0-draft`, updating the view schema, relevant semantic clauses, expected views, coverage and normalization checks. Align all profile constants and URNs; resolve OQ18’s version mismatch.
- **Architecture — v1:** Update §§7.2 and 8 with the two availability dimensions and source-table contract.
- **Decisions — v1:** Close OQ23. No decided owner decision changes.
- **Implementation — v1:** Kernel projection, source disposition handling, change comparison, CLI rendering and embedded assets. Replace scenario 11’s reference-only assertion with locator/excerpt checks.
- **Intake correction — v1:** The CLI currently hashes the supplied excerpt, which is not necessarily the entire message. Label that digest accurately. A new record claiming D-016’s message digest must receive the actual message digest; legacy records must not be relabelled.
- **Later:** Independently authenticated live session resolution; separate bounded source retrieval if needed.

**5. Tests and vectors**

Add exact-output semantic vectors covering:

1. Authorized retained excerpt and locator, including Unicode and trailing-newline preservation.
2. Original source unavailable while excerpt remains readable; current-required evidence remains unavailable, while retained assessments retain their existing qualification.
3. Read/use/metadata denial, hidden associations and audience projection: no source existence leakage.
4. Initial fences, erasure and historical reads: no excerpt, locator digest or `origin` resurrection.
5. Released assertion with restricted inputs, followed by release withdrawal: no provenance laundering.
6. Hidden-source append, revision, erasure and size changes: identical normalized views, change results, cutoffs, ordering and completeness. Pair these with an authorized-reader control that observes the change.

Extend S12/S30/S32, P05/P12/P13 and the existing non-interference cases. Include OQ19’s relevant regression witnesses. Plant a forbidden excerpt and an extra normalization path to verify that the harness detects each intended violation.

**Gate:** A fresh reader recalls the recorded session statement, sees the exact locator and retained excerpt, and can still read that excerpt after original-session availability becomes unavailable.

**6. Risks and confidence**

**High confidence** in the contract. Risks are larger responses, misleading digest labels, and accidentally treating an erased locator as harmless metadata. Git remains unsuitable for sensitive excerpts or guaranteed erasure.

## Q2. Use owner-endorsed discovery objects in the platform space

**1. Recommendation**

Make directory entries **adapter-level signed objects**, outside `records/` and outside kernel evaluation.

Use immutable files:

```text
directory/<encoded-space-id>/<revision>.json
```

The closed payload is:

```typescript
Entry = {
  format: "swarma-memory-directory/1",
  directory_space: string,
  space_id: string,
  revision: PositiveInteger,
  previous: Digest | null,
  status: "active" | "revoked",
  bindings: Array<{ kind: "identity" | "project", id: string }>,
  kind: "agent" | "project" | "platform",
  owners: string[],
  git: { remote: string, branch: string },
  anchor: {
    genesis_digest: Digest,
    policy_version: PositiveInteger,
    policy_digest: Digest
  },
  access_hint: {
    public: boolean,
    reader_identities: string[]
  },
  valid_until: UTCTimestamp
}
```

Bindings and identity arrays are canonical sorted sets. Revision 1 has `previous: null`; later revisions name the previous accepted entry digest.

An active entry requires two endorsements:

- **Space endorsement:** one owner of the advertised space confirms its binding, location and advertisement.
- **Directory endorsement:** one platform-space owner accepts that advertisement into the directory.

Each endorsement binds the complete entry, signing identity, role and applicable policy digest, using distinct purposes such as `swarma-memory-space-advertisement/1` and `swarma-memory-directory-publication/1`. Use existing Ed25519 framing and registered keys. Commit signatures alone are insufficient.

The **platform-space owners own the directory**. In v1, they also publish entries; ordinary memory writers cannot publish trusted directory mappings. Agents may prepare the exact payload. Dedicated delegated directory maintainers can come later.

A directory owner may publish a revocation without the target owner’s signature: withdrawing a discovery listing grants no access or control over that target.

**Verification flow:**

1. Start from an independently pinned platform-space genesis.
2. Verify platform policy history, directory endorsement, entry revision chain, expiry and first-parent position.
3. Treat its target genesis as a trust introduction authorized by the trusted directory owner.
4. Fetch through an already permitted transport; verify the target’s policy chain against that genesis and through the advertised policy pin.
5. Verify the space endorsement against that historical target policy.
6. Evaluate access using the target’s **current** verified policy and actual Git permissions.

Reject remote-helper execution forms, embedded credentials and malformed branch/path inputs. An advertised URL is not permission to open a new transport.

The directory is authoritative for **accepted discovery mappings and their withdrawal**. It is not authoritative for identity ownership globally, current readers, writer grants, representation, decision currentness or content disclosure.

**Staleness and revocation:**

- Expired entries cannot establish new automatic discovery bindings.
- A newer target policy makes copied access hints historical; current target policy wins.
- Directory revocation prevents future discovery through that listing. Actual access revocation requires target-policy and Git ACL changes.
- Existing configured spaces remain independently pinned; delisting does not destroy their configuration or silently change their roots.
- History rewrites and replayed older entries preserve the last verified state and report failure. A new client still cannot prove that a valid, unexpired advertisement is the newest possible advertisement.

**2. Why**

D-013/D-018 and architecture §5.4 require discovery, not another authority registry. The [implemented signing contract](bundle/repo/docs/signing-policy.md) already supplies genesis pins, owner transitions, historical key verification and single-owner policy signatures.

`docs/git-spaces.md` explicitly reserves `directory/`. It also states that `Reader.Spaces` currently grants no authority; directory implementation must not quietly turn that metadata into group membership.

Two endorsements distinguish the target owner’s advertisement from the platform owner’s trust introduction.

**3. Trade-offs and rejected alternatives**

Two signatures add administrative work, but directory changes are infrequent trust changes.

Reject a sixth kernel record kind: discovery is deployment configuration, not evidence evaluation. Also reject unsigned configuration and a directory-maintained access ledger. Neither can establish trustworthy mappings without duplicating existing policy ownership.

A Git directory cannot hide individual entries from people who can clone it. Admit only metadata suitable for every directory reader.

**4. Changes needed**

- **Package — v1:** No kernel semantic change. Document the discovery boundary in the Swarma adapter.
- **Architecture — v1:** Specify entry verification and correct “sharing means Git access plus entry” to include the target’s signed reader policy and required key registration.
- **Decisions — v1:** Close OQ9; preserve D-018/D-019/D-024.
- **Implementation — v1:** Closed adapter schemas, endorsement verification, immutable entry replay, discovery commands and tests. Preserve existing signed write-transaction checks from OQ21.
- **Later:** Scoped maintainer delegation, registry-backed identity resolution and richer discovery. No new memory server.

**5. Tests and gate**

Positive cases include publication, location update under the same genesis, historical-key verification and independent cache rebuild.

Negative cases include forged endorsements, signature-purpose substitution, self-introduced roots, altered remotes, wrong space IDs, policy forks, expired/replayed entries, unsafe transport forms and an advertisement claiming access absent from target policy. Refusals must leave trusted configuration unchanged.

Non-interference tests vary undisclosed target records while holding directory metadata and authorized projections constant. Discovery must not inspect or summarize target contents. Access failure must not disclose target record IDs or counts.

**Stage-5 gate:**

- Owners A and B have separately configured persistent agents with independently registered temporary keys.
- Each owner grants the other agent Git read access, registers its public key where required, and grants the signed memory reader role.
- Both spaces receive valid directory entries.
- Each agent discovers and verifies the other space, then reads an attributed record and its Q1 source payload.
- An ungranted third identity fails. Revocation in either direction prevents subsequent authorized reads despite a cached directory advertisement.

These agents remain agents of their respective owners; this does not create personal memory for visiting external workers or change D-021.

**6. Risks and confidence**

**High confidence** in the ownership and authority separation; **medium confidence** in operational bootstrap until exercised between actual owners. Main risks are compromised directory signing keys, stale advertisements and metadata exposure. Previously cloned Git history cannot be recalled.

## Q3. Route conflicts through the current board; keep decision authority explicit

**1. Recommendation**

Replace the uninterpreted resolver-area string with a versioned, typed selector:

```typescript
ResolverRule = {
  area: string,
  selector: {
    subject: string,
    schema: VersionRef,
    issuer: string,
    perspective: Perspective,
    slot: string
  },
  identities: string[],
  route: {
    kind: "board",
    board_id: string,
    parent_id: string,
    role_id: string
  }
}
```

The space is implicit in the signed policy. All selector fields match exactly; `slot` follows K-DOM-2. The area name is a label, never a natural-language classifier.

For v1, allow neither regexes nor priority rules. Duplicate selectors are invalid. Broader responsibility is expressed through several entries. Legacy free-text areas acquire no inferred meaning.

**Default:** all current verified space owners are responsible when no selector matches. This is a notification set, not a new voting threshold. Use the current task’s configured board route; if it cannot reach those owners, keep the dependent step blocked and expose the routing failure.

The policy owner signs resolver configuration through the existing policy chain. Resolver assignment grants **responsibility only**:

- Reading evidence requires current read/use/metadata rights.
- Writing requires registered signing keys and the applicable writer/retention grants.
- Revising requires the original issuer or a currently checked representative.
- Adopting a decision requires the deciding authority’s canonical receipt.
- Board assignment, task mutation and notification require the board’s existing authority checks.

A resolver without revision authority prepares a proposal for the issuer. Being a space owner, board reviewer or named resolver does not authorize replacing another issuer’s sequence.

**Use the existing board for v1.** `platform-book/13-doska.md` and chapter 15 identify an existing task board with roles, review and integration. The material does not provide an implemented Keeper escalation API. Chapter 06 also explicitly warns that general `grant/1` is architecture, not a usable wire format.

The concrete flow is:

1. The caller declares the decision dependency and queries with `--require-current`.
2. Exit **7 / `currentness_required`** stops that dependent step. Unrelated work continues. Other read failures never count as successful resolution.
3. The agent or orchestrator creates or updates one board task through its existing authorized client, names the resolved identities and routes it through the configured role.
4. Record actual assignment and resolver acknowledgement or retrieval. Task creation alone does not prove delivery.
5. Resolvers decide through the canonical decision authority; the new receipt and decision are admitted.
6. The caller syncs and reevaluates the dependency before resuming. A board “done” status or a reassuring message is insufficient.

Memory commands perform none of steps 3–4.

**A necessary v1 dependency:** the [CLI’s provisional profile](bundle/repo/docs/cli.md) currently supplies no authority events and cannot admit authoritative `decision_record`s.

Add a narrow trusted adapter for the **reviewed Git decision register** already named by K-REV-3. The owner-signed policy must pin the register, deciding issuer and verification authority. Import only authenticated canonical receipt events binding the decision scope/content and predecessor receipts. A signed memory source, scanner approval or board activity mirror cannot manufacture these facts. This is new implementation work, not an existing capability.

For an ambiguous sequence, **do not use ordinary CAS `revise`**: ambiguity produces `version_conflict`. The deciding issuer records a new canonical event succeeding every conflicting maximal receipt, then imports the corresponding decision through K-REV-3’s canonical-import path.

**Across spaces or owners:** retain separate views. K-DOM-3 requires equal space, and D-009 provides no cross-issuer order. An agent may report a `cross_scope_disagreement`, but must not mislabel it kernel `ambiguous_current` or evidence conflict.

Route the issue to each affected space’s resolvers. If work requires agreement from both authorities, each must record its own compatible successor. If existing task authority selects one governing issuer, follow that explicit authority without revising the other owner’s history. If neither rule exists, the owner must choose; timestamps, votes and directory order cannot settle it.

**Escalation packet**

The CLI produces a protected diagnostic packet with:

```text
format, classification=data, request_id
task/goal revision, dependent step, originating agent
conflict kind
query and exact schema/rule/evidence-policy versions
per-space policy pins and authorized snapshot bindings
candidate refs, authority receipts and both polarity qualifications
kernel-disclosed source details
matched area, resolver identities and routing-policy revision
requested decision and retry/deduplication binding
```

Persist only under permitted retention. Retries for the same task, step and visible conflict update the existing escalation.

For v1, the board task should carry the work context and authorized routing/query metadata; **resolvers pull evidence through their own authenticated memory reads**. The full local diagnostic packet is not automatically a board attachment. Copying it requires separate forwarding and destination-retention authorization, and any transmitted projection must come from the kernel. Missing permission does not justify copying raw snapshots. Packet text remains data.

**2. Why**

This implements D-020 while preserving D-009 and K-REV-1/3/4. It also respects the platform rule that authority is checked by the component performing the action.

`go/space/policy.go` currently validates only nonempty resolver areas and identities. `go/agentprofile/profile.go` supplies neither representations nor authority events. Those gaps must be explicit; adding a route alone cannot deliver authoritative resolution.

**3. Trade-offs and rejected alternatives**

Exact selectors are less convenient than topic inference, but are deterministic and auditable.

Reject a memory-owned scheduler, automatic Keeper invocation, implicit resolver delegation, cross-owner supersession and “latest timestamp wins.” Defer generic role grants until the platform actually supplies them. Pulling evidence separately adds a read but avoids casually forwarding another principal’s authorized view.

**4. Changes needed**

- **Package — v1:** No new escalation operation or cross-space order. Add resolution/import vectors using existing semantics; any discovered semantic defect requires a package release.
- **Architecture — v1:** Specify typed resolver selection, board routing, delivery evidence and trusted receipt integration.
- **Decisions — v1:** Close OQ8 and clarify that D-020 supersession obeys issuer-local authority. This does not reopen D-009.
- **Implementation — v1:** Versioned adapter policy schema, resolver administration, diagnostic packet generation, receipt importer and skill/board integration.
- **Later:** Keeper deadlines and escalation custody, registry-backed representation, broader selectors if justified, and separately designed multi-authority decision protocols.

**5. Tests and gate**

Test exact matching and owner fallback, duplicate-selector rejection, forged policy, missing route, unregistered identities, revoked rights and resolver-without-revision-authority. Pair rejected replacement with permitted proposal/challenge controls.

Preserve S02, S28–S42 and P14 distinctions. Add canonical successors above both ambiguous maxima, foreign-owner replacement refusal, and two-space disagreement without invented global currentness.

Non-interference tests must show that hidden conflicts neither stop a reader’s step nor change its packet, routing or deduplication identity. Test recipient-specific evidence reads and an unrelated visible conflict that does not block the declared dependency.

**Stage-6 gate:** In an integrated agent run, exercise both ambiguity and evidence conflict. Observe that the dependent action does not execute; the board task reaches the actual configured resolver; an authenticated successor receipt enters memory; and only a fresh satisfactory read permits continuation. Repeat escalation to prove deduplication. Failed delivery, forged receipts and a prematurely closed task must leave the step blocked.

**6. Risks and confidence**

**Medium confidence.** The semantics are clear; receipt integration and actual board-to-resolver delivery remain engineering dependencies. Two owners may legitimately disagree indefinitely. The system must preserve that outcome rather than fabricate consensus.

## For the owner

- **Name the initial platform-directory owners and approve its advertised identity/project bindings.** This establishes a trust-introduction authority and exposes metadata; the material supplies no actual ownership assignment.
- **Assign real area resolvers and board routes.** The selector mechanism is technical, but responsibility belongs to the organization.
- **Choose governing authority where work depends on incompatible decisions from independent owners and no existing rule settles precedence.** That is a product or ownership decision. D-009 deliberately prevents memory from making it.