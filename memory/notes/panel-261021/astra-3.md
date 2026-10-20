I recommend a package release that adds source presentation to the existing view, signed adapter objects for the directory, and escalation through the existing task board. Preserve issuer-local decision order. D-020 needs clarification for cross-owner conflicts, but none of D-001–D-026 needs reversal.

The tests below are proposed acceptance requirements. The supplied package’s structural checker passes; that does not establish the proposed behavior.

**Q1. Expose sources through the kernel view**

**1. Recommendation**

Add a deduplicated source table to `View`. Keep assertions as the only read items and retain each item’s existing `source_refs`.

The following is a closed schema grammar: all fields are required, unknown fields fail, and `Part<T>` is a `oneOf`.

```text
Part<T> =
    {state: "available", value: T}
  | {state: "unavailable"}
  | {state: "withheld"}

SourceView = {
  ref: VersionRef,
  attribution: {
    issuer, submitter, representation_ref,
    perspective, admission_class
  },
  locator: Part<SourceLocator>,
  resolution: "available" | "unavailable",
  excerpt: Part<string>
}

View += {
  sources: [SourceView],
  source_output: {
    status: "complete" | "partial",
    reason: null | "source_output_limit"
  }
}
```

`attribution` reuses the corresponding envelope types. `SourceLocator` contains exactly the existing source-body fields `owner`, `source_kind`, `object`, `revision`, `digest`, `provenance`, `origin`, `original_issuer`, and `carrier`, with their existing types.

Construct `sources` only from the union of the **already disclosure-filtered** `source_refs` of displayed items. Sort by exact reference. Never enumerate the underlying source inventory to produce placeholders.

Add a closed trusted-policy table:

```text
source_presentations[] = {
  source: VersionRef,
  principal, space, audience, purpose,
  locator: boolean,
  excerpt: boolean
}
```

Duplicate scope keys are invalid; missing entries mean both permissions are false. These permissions supplement—and cannot bypass—current read/use/metadata rights, inherited disclosure restrictions, and disposition checks. In v1, an owner-signed policy can authorize presentation of a reader’s admitted non-sensitive source class; the trusted profile expands that authorization into exact kernel facts. This requires no per-record human approval.

Apply the states as follows:

| Component | `available` | `unavailable` | `withheld` |
| --- | --- | --- | --- |
| Locator | Authorized surviving locator fields | Locator bytes cannot be presented, including after applicable erasure | Locator presentation is not permitted |
| Excerpt | Authorized retained text exists | No retained text, or applicable disposition prevents presentation | Excerpt presentation is not permitted |
| Resolution | Admitted current facts establish resolution | No admitted current resolution | No separate withholding variant; see below |

Resolution is already part of source metadata and evidence semantics. Do not claim to hide availability while letting it alter visible evidence. A source lacking metadata authorization is excluded under K-AUTH-1.

A completely hidden source produces **no reference, row, placeholder, count, or source-specific error**. A reader authorized for its metadata but not its payload sees an authorized reference and `withheld` payload parts. Permission is checked before payload existence, so withholding does not reveal whether an excerpt exists.

A deleted session can therefore produce:

```json
{
  "resolution": "unavailable",
  "excerpt": {"state": "available", "value": "The retained passage"}
}
```

This is the essential D-016 case. “Unavailable” means unavailable under the admitted resolution profile; it does not prove that the session was deleted.

Keep `sources: []` for `audience_projection`, preserving K-DISC-2’s prohibition on exposing internal source references and hidden derivations. Publishing an excerpt later requires a separately admitted output.

Add independent `source_items` and `source_bytes` output bounds, clamped by policy. Count only authorized presentations, emit a deterministic prefix, and report truncation through `source_output`. Never silently truncate text or turn a rendering limit into evidence incompleteness.

**2. Why**

This directly closes architecture §§7.2–8 without creating another authorization endpoint. It preserves the distinction between retained content, current source resolution, and evidence qualification established by K-REC-1, K-EVAL-5, K-AUTH-1 and K-ERASE-1. See [the normative semantics](bundle/repo/spec/kernel/semantics.md).

The current session locator already exists in `body.origin`, with the raw supplied-text digest in `body.object`. Exposing those approved fields requires no session-specific kernel record kind. A renderer may parse the documented adapter convention **after** kernel disclosure, solely for presentation.

There is also an intake qualification to fix: the CLI hashes supplied text, which may be only an excerpt. That is not necessarily D-016’s whole-message digest. New records claiming a message digest must obtain it from the actual message evidence; legacy records must label their hash as a supplied-text digest. See [CLI session excerpts](bundle/repo/docs/cli.md:234).

**3. Trade-offs and rejected alternatives**

The view grows, hence separate output bounds. Explicit presentation permissions add a small policy surface but prevent automatically releasing previously undisclosed locators and excerpts.

Reject a separate source-read operation for v1: it adds probing behavior, authorization bindings and another finite-API operation to solve a requirement already attached to selected assertions. Reject adapter reads from cached records: they bypass kernel disclosure.

**4. Changes needed**

- **Package, v1:** release a consistently versioned profile, schemas and vectors; extend view, query bounds and trusted-policy shape. Specify source presentation, disposition and `changes` behavior. An authorized presentation change must participate in change detection.
- **Architecture, v1:** document retained excerpt versus external resolution, permission defaults and rendering limits.
- **Decisions, v1:** implement D-016; no reversal.
- **Implementation, v1:** kernel projection/disclosure, policy-derived presentation facts, renderers, embedded assets and skill examples.
- **Later:** live session resolvers and independently released source publications.

**5. Tests and vectors**

Add positive and negative cases covering:

- Available original plus excerpt; unavailable original plus surviving excerpt; no retained excerpt.
- Metadata allowed but locator/excerpt withheld; denied metadata with no observable source existence.
- Locator digests and session coordinates absent whenever their presentation is withheld.
- Fences, erasure and revoked permissions honored at historical cuts; captured responses remain historical and confer no new delivery rights.
- Hidden-source append/revise/erase and hidden payload changes preserve normalized views, ordering, budgets, evidence and `changes`; an authorized control changes appropriately.
- Zero and exhausted presentation bounds leave evidence fields unchanged; compact output preserves states.
- Instruction-like excerpt text remains data.

The scenario-11 gate must read back the actual locator and exact retained text through the CLI, including after original resolution becomes unavailable. A source-reference-only assertion is insufficient.

**6. Risks and confidence**

Git readers can inspect repository bytes directly; these are kernel/API disclosure guarantees, not protected storage. Legacy provenance and output amplification need explicit handling. **Confidence: high.**

**Q2. Make the directory a signed discovery catalogue**

**1. Recommendation**

Use adapter-level signed objects under:

```text
directory/<encoded-space-id>/<version>.json
```

Do not add a sixth kernel record kind.

Use two nested objects:

```text
Advertisement = {
  format: "space-advertisement/1",
  space_id, kind,
  bindings: [{kind: "identity" | "project", id}],
  git: {remote, branch},
  genesis_digest,
  policy: {version, digest},
  access_hint: "public" | "named",
  expires_at,
  author
}

DirectoryEntry = {
  format: "space-directory-entry/1",
  directory_space,
  space_id,
  version,
  previous,
  state: "active" | "revoked",
  advertisement: SignedAdvertisement,
  author
}
```

All objects are closed. Bindings are sorted and unique. `previous` is the preceding entry digest, or null for version 1. An active entry requires an unexpired advertisement.

A target-space owner signs the complete advertisement under a new purpose, `swarma-memory-space-advertisement/1`. A platform-space owner signs the complete directory entry, including that signed advertisement, under `swarma-memory-directory-entry/1`.

The **platform space’s existing owners own the catalogue**. For v1, only they publish entries. Ordinary memory writer grants do not imply directory publication rights. Delegated catalogue editors can come later through an explicit policy capability.

The two signatures express different things: the target owner advertises the endpoint; the platform owner endorses its identity/project binding and inclusion. One owner signature on each side suffices under the existing policy-chain contract; this introduces no threshold rule.

**Reader verification flow:**

1. Start from an independently trusted platform-space genesis pin; verify its policy chain and first-parent history.
2. Verify the directory entry’s signature and publisher authority at its history position, revision chain, expiry and current publication status.
3. Use the platform-endorsed target genesis pin to verify the target policy chain and the advertisement signer’s owner authority at its pinned policy.
4. Verify the target’s actual space ID and latest policy. Ownership changes require refreshed endorsement; key rotation does not invalidate historical signatures.
5. Apply current target reader authorization and Git transport access independently.

Neither an arbitrary self-signed advertisement nor a remote URL bootstraps trust. Use approved Git transports; an entry must not install credentials, hooks or executable configuration.

The catalogue is authoritative for **what the platform has endorsed for discovery**. It is not authoritative for current read/write rights, delegation, decision authority, task ownership or source truth. `access_hint` is explicitly a hint; `readers[].spaces` must remain non-authoritative.

**2. Why**

This follows D-018 and architecture §5.4 while retaining the existing genesis-pinned trust chain. Discovery must operate before opening a target kernel corpus, making it adapter configuration rather than evidence evaluation. Existing policy verification already requires trusted genesis distribution and distinguishes owners from reader/writer grants; see [signing and policy](bundle/repo/docs/signing-policy.md).

The second endorsement prevents a target’s arbitrary key from claiming another project’s directory binding.

**3. Trade-offs and rejected alternatives**

Two signatures cost more than one, but separate target consent from catalogue governance. Owner-only publication is deliberately small and adequate for the two-owner gate.

Reject unsigned configuration, trust-on-first-use registration, and directory ACLs that compete with `space.json`. Reject a kernel assertion as the authoritative directory entry: it would entangle discovery with evidence projections and create bootstrap problems.

Expired or unreachable entries remain last-verified historical information, not current discovery results. Never substitute another repository merely because its name matches.

Revocation appends a signed tombstone; it does not delete history. A platform owner can unlist an entry without obtaining another target signature. A target owner can request withdrawal with signed evidence, but must revoke actual policy/Git access directly when access must stop. Unlisting alone cannot revoke existing clones or configured access.

**4. Changes needed**

- **Package, v1:** no kernel change; add closed adapter schemas and purpose-separated signature contracts.
- **Architecture, v1:** specify endorsements, trust bootstrap, freshness, tombstones and the limits of access hints.
- **Decisions, v1:** close question 9 by assigning catalogue custody to platform-space owners; preserve D-018/D-019/D-024.
- **Implementation, v1:** directory administration, replay verification, discovery and explicit registration of verified targets.
- **Later:** delegated publishers, automated refresh and registry-backed identity validation.

**5. Tests and vectors**

The stage-5 gate must use two independent owners and their persistent agents:

1. Each owner registers the other agent’s temporary public key in the shared target’s signed policy and grants named read access.
2. Git access is granted separately.
3. Both spaces receive valid advertisements and directory endorsements.
4. Each agent discovers, verifies and reads the other owner’s shared space without knowing its remote beforehand.

Use shared project spaces; this does not create personal memory for ephemeral external workers.

Negative controls must reject forged endorsements, wrong genesis pins, substituted repositories, unauthorized publishers, expired entries, rollback and conflicting revisions. A listed space with denied policy or Git access must remain unreadable.

Test withdrawal separately from access revocation. Test that unrelated or rejected advertisements cannot alter an already configured space’s kernel evidence, grant authority or introduce hidden source metadata. All catalogue contents must be suitable for disclosure to every reader of its Git repository.

**6. Risks and confidence**

The main risks are stale discovery, incorrect initial trust binding and advertising an endpoint unsuitable for automatic transport. Offline readers cannot prove they have seen the latest revocation; report the verified position and freshness. **Confidence: high on the contract, medium on operational freshness.**

**Q3. Route responsibility explicitly; preserve decision authority**

**1. Recommendation**

Replace the current free-form resolver area with a deterministic selector:

```json
{
  "area": "agent-home-retirement",
  "match": {
    "subject": "subject:agent-home",
    "schema": {"id": "schema:decision", "version": 1},
    "issuer": null,
    "perspective": null,
    "slot": "[]"
  },
  "identities": ["principal:owner"],
  "route": {
    "kind": "board",
    "board": "board:platform",
    "parent": "task:architecture"
  }
}
```

Space is implicit in the enclosing owner-signed policy. Non-null selectors use exact equality; null means unrestricted. No text classification, prefix inference or model-selected priority.

Reject overlapping non-default selectors at policy validation. Permit one all-null default. Resolve using the current verified policy, not a remembered appointment. V1 names concrete identities; role expansion requires the platform’s separately authenticated role bindings later.

With no matching appointment, notify **all current space owners** through the owner-configured default board route. Do not choose `owners[0]`. Missing routing configuration produces a local actionable packet and leaves the dependent step stopped.

Resolver appointment grants responsibility to receive and coordinate the issue. It grants **no** reader, writer, representation, board mutation or decision authority:

- Reading requires current access.
- Recording requires the appropriate writer and retention grants.
- Revising another issuer’s sequence requires checked representation under K-ENV-2/K-REV-1.
- An adopted decision requires an authenticated canonical receipt.
- Board actions use the board’s existing authorization.

The current profile supplies neither representation facts nor authority events. Therefore, v1 should have the deciding issuer sign its resolution, with appointed agents preparing recommendations where necessary.

For authoritative ambiguity, publish a new canonical receipt that succeeds **every conflicting maximum in that issuer’s graph**, then admit the corresponding decision. Do not call ordinary CAS revision against an ambiguous head: K-REV-1 correctly rejects that. K-REV-3 expressly permits canonical decision import.

For evidence conflict, preserve both historical witnesses. Record the authorized resolution and reassess the dependent step; a resolver’s appointment does not make opposing evidence disappear.

**Cross-space and cross-owner conflicts.** Keep separate verified views and their exact scopes. A consumer may report that two governing decisions conflict for its task, but must label that as a consumer-reported dependency conflict—not manufacture cross-space `ambiguous_current` or opposing kernel witnesses.

Route to each affected space’s resolvers; the task owner coordinates. Each issuer resolves its own sequence. There is no implicit platform-over-project precedence, majority vote or foreign-event ordering. A common arbitrator needs explicit authority from the affected owners. Otherwise the legitimate outcome is continued blockage, or an independently authorized change to the task’s governing scope.

This is the necessary clarification to D-020: one resolver receipt cannot supersede decisions belonging to unrelated issuers.

**Concrete escalation path.** Use a board task in v1. The platform book identifies the existing board, CLI, roles and workflow machinery. It describes broader playbook/grant machinery as architecture; it supplies no callable Keeper escalation contract. See [the board chapter](bundle/platform-book/13-doska.md) and [current platform status](bundle/platform-book/15-gde-my.md:5).

The flow is:

1. Recall the decision dependencies explicitly with `--require-current`; exit 7 stops the dependent step.
2. CLI/skill prepares a data packet.
3. The authorized agent/orchestrator creates or reuses a board task addressed to the resolvers and links the blocked step.
4. Verify the resolver can retrieve and acknowledge that exact task revision.
5. Record the resolution through normal authority/admission rules.
6. Sync and re-evaluate before resuming.

Memory performs none of the board mutations or wakeups.

**Packet shape:**

```text
{
  format: "memory-conflict/1",
  classification: "data",
  task: {id, revision, dependent_step},
  dependencies: [{space, subject, schema, issuer, perspective, slot}],
  conflicts: [{kind, exact_versions, disclosed_evidence}],
  routing: [{space, policy_pin, area, identities, route}],
  requested_outcome,
  deduplication_key
}
```

Use only disclosed evidence and authorized policy metadata. Keep protected cuts and bindings local. Derive deduplication from the task step, exact conflicting references and conflict kind—not timestamps, random handles or whole-repository heads.

Before attaching material, authorize it for the board’s readers and storage context. Source read access alone does not authorize forwarding. If only a minimal routing request is shareable, send that and let resolvers recall under their own identities. The board authenticates its submitting actor; the packet itself grants no authority.

**2. Why**

This implements D-020 without weakening D-009 or turning memory into a workflow engine. K-REV-3/S34–S42 explicitly prohibit ordering through foreign issuers.

A material prerequisite remains: [the provisional CLI profile](bundle/repo/docs/cli.md:316) cannot admit authoritative decisions. Stage 6 must not hide that limitation behind preloaded synthetic authority facts.

**3. Trade-offs and rejected alternatives**

Exact selectors require deliberate configuration but are auditable. Reject fuzzy topic routing, overlapping priority rules, automatic delegation from resolver membership, and “latest timestamp wins.”

Use the existing board now. Keeper can later supervise deadlines and unresolved obligations through its own contract; do not invent a Keeper API or put a scheduler in memory.

**4. Changes needed**

- **Package, v1:** retain revision semantics; add successor-of-all-maxima regression vectors. Any changed kernel behavior requires the same versioned release discipline as Q1.
- **Architecture, v1:** specify selector matching, defaults, packet disclosure, board acknowledgment and cross-owner blockage.
- **Decisions, v1:** close question 8; clarify D-020’s cross-issuer limitation.
- **Implementation, v1:** version the signed-policy resolver schema; add packet generation and skill/board integration.
- **Implementation prerequisite, v1:** implement one owner-policy-pinned verifier for the reviewed Git decision register. Authenticate exact receipt revision/digest, deciding issuer, predecessors, scope and decision content before supplying existing `authority_events`. Ordinary record signatures or `canonical: true` in local configuration cannot supply this authority.
- **Later:** registry-backed representation, role resolution, Keeper routing and explicitly delegated cross-owner arbitration.

**5. Tests and vectors**

Cover both authoritative ambiguity and evidence conflict, with valid controls:

- A dependent effect does not execute; unrelated work remains possible.
- One addressed board task is created despite retry/lost acknowledgment; the resolver retrieves its exact revision.
- A canonical successor of both maxima resolves ambiguity; succeeding only one leaves ambiguity.
- Foreign-issuer succession, unauthorized representation, stale CAS and forged receipts fail without partial writes.
- An unreceipted resolution remains a proposal.
- Two-space disagreement reaches both resolver sets without merging their authority.
- Hidden conflicts create no packet, task, changed deduplication key or visible status; denied forwarding exposes no evidence.
- Closing the board task alone does not resume work. A fresh read must establish that the original dependency requirements are satisfied.

Until receipt verification is implemented, authoritative end-to-end resolution remains an unmet gate. Synthetic fixtures can establish kernel behavior, not that integration.

**6. Risks and confidence**

The largest risks are missing receipt integration, resolver unavailability and legitimate disagreement between owners. The design makes those visible instead of granting authority implicitly. **Confidence: medium**, principally because the bundle does not specify the installed board’s exact routing API or an authenticated decision-register binding.

**For the owner**

- Name the initial catalogue custodians, resolver assignments, board destinations and canonical decision register. The material establishes their roles, but not the actual ownership and trust bindings.
- If cross-owner disputes must always reach one binding answer, appoint an arbitrator and define each owner’s delegation. Without that ownership decision, the system must permit unresolved disagreement and keep the dependent step stopped.