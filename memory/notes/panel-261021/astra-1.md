## Q1 — Disclose source details within the kernel view

### 1. Recommendation

Add a **deduplicated source-detail table to the existing view**. Do not introduce another read operation for v1.

Keep `items[].source_refs`. Add this required field, expressed below as closed tagged unions; every listed field is required and additional properties are forbidden:

```text
View.source_details =
    { state: "withheld" }
  | { state: "available", entries: SourceDetail[] }

SourceDetail = {
  ref: VersionRef,
  subject: Principal,
  issuer: Principal,
  submitter: Principal,
  perspective: Perspective,
  admission_class: AdmissionClass,
  availability: "available" | "unavailable",
  payload:
      { state: "unavailable" }
    | { state: "available", source: SourcePayload }
}
```

`SourcePayload` contains exactly the existing source-body fields **except `availability`**:

```text
owner, source_kind, object, revision, digest, provenance,
origin, original_issuer, carrier, excerpt, retention_admission
```

Their types and nullability remain those in `source.schema.json`. The containing view’s `data` classification applies to these entries.

The kernel constructs the table from the sources already disclosed through selected items’ `source_refs`, sorted and deduplicated by exact reference. It does not enumerate unrelated sources.

Use the states as follows:

| Situation | Result |
| --- | --- |
| Source record and retained payload are authorized | Include the entry and payload |
| Original session cannot currently resolve, but its retained excerpt survives | `availability: unavailable`, **payload available** |
| Memory’s source payload is erased or fenced, but its structural reference remains disclosable | Payload unavailable; no locator, excerpt, origin or digest |
| Reader lacks source read/use/metadata permission | Omit the entry and reference |
| `audience_projection` | Always `source_details: {state: "withheld"}` |

The last rule preserves the existing audience contract. `withheld` describes the projection’s disclosure policy; it **does not signal that a hidden source exists**. An ordinary reader denied a source sees the same empty source set as a reader for whom no eligible source exists—no hidden-source count or placeholder.

`availability: available` requires the kernel’s existing current-resolution conditions. A retained excerpt alone cannot establish it. The kernel performs no network resolution.

For existing session records, expose the documented encoding: locator JSON in `origin`, raw-text SHA-256 in `object`, message position in `revision`, and retained text in `excerpt`. The CLI may format these **after kernel disclosure**. It must label the digest as covering the supplied text; an excerpt hash cannot prove the contents of a longer original message.

### 2. Why

This closes OPEN-QUESTIONS 23 and architecture §§7.2–8 while preserving:

- D-016: a retained piece can survive deletion of its session.
- K-AUTH-1: authorization precedes computation and metadata generation.
- K-EVAL-5: unavailable source bytes differ from retained assessment evidence.
- K-DISC-2: audience projections reveal neither internal source references nor hidden derivations.
- K-ERASE-1: historical reads cannot reconstruct erased payloads.

References: `repo/spec/kernel/semantics.md`; `repo/docs/cli.md`, “Session excerpts”; `repo/docs/disclosure-erasure.md`.

The original signed records remain unchanged. Readers verify them before supplying admitted records to the kernel; the view is a derived, filtered representation, not a newly signed source statement.

### 3. Trade-offs and rejected alternatives

A separate source-read operation would require another authorization, historical-cut, disclosure, error and non-interference contract. It offers little benefit for already-retained, bounded excerpts.

Adapter hydration is unacceptable: fetching a record from the local snapshot after receiving `source_refs` would bypass kernel disclosure.

The table increases response size. Deduplication and existing record/field limits bound v1; later pagination can have its own explicit contract. Payload omission must never silently become “source unavailable” because a renderer hit a size limit.

### 4. Changes needed

- **Package — v1:** release a new semantic profile; update the view schema, K-EVAL-5/9, disclosure and changes semantics, vectors, schema URNs and embedded assets together. Source-detail changes must participate in `changes` comparisons after disclosure.
- **Architecture — v1:** document the two independent facts: original-source availability and retained-payload availability.
- **Decisions — v1:** close question 23; no decided rule needs reopening.
- **Implementation — v1:** kernel table construction, fence handling, CLI rendering and cache comparisons. Keep raw Git history bindings outside the non-interfering view; the current CLI’s exposed Git cursors cannot serve as non-interfering public change tokens.
- **Later:** a typed locator format and optional separately bounded source retrieval. Neither is necessary to expose existing records correctly.

### 5. Tests and vectors

Add vectors covering:

1. Authorized locator and byte-exact excerpt, including Unicode and trailing newlines.
2. Unavailable original session with a readable retained excerpt; no upgrade to fresh source evidence.
3. Hidden source absent versus present, revised or erased: identical normalized views, counts, cutoffs and changes.
4. Many hidden sources under small budgets: unchanged visible evidence and completeness.
5. Erasure/fences at current and historical cuts: no excerpt or digest recovery; eligible retained assessments retain their qualifications.
6. Audience projections, including declassified assertions: the same constant `withheld` branch, without source identities or counts.
7. Revocation after capture: historical bytes remain historical, but new reads/delivery cannot reuse revoked disclosure.
8. Closed-shape rejection, deterministic ordering, deduplication and full/compact parity.

**Gate:** another authorized agent reads a recorded session locator and exact retained excerpt through the installed CLI; a denied reader receives neither. Retain all existing semantic guarantees. These additions do not qualify physical erasure in Git.

### 6. Risks and confidence

**Confidence: high.** Main risks are leaking erased digests through “metadata,” confusing retained text with live resolution, and leaving a disclosure bypass in CLI wrappers.

---

## Q2 — An owner-endorsed discovery directory

### 1. Recommendation

Make directory entries **adapter-level signed administrative objects**, stored under `directory/` in the platform space. They are not a sixth kernel record kind.

Use an immutable, versioned entry payload:

```json
{
  "format": "swarma-memory-directory/1",
  "directory_space": "space:platform",
  "space_id": "space:project-p",
  "kind": "project",
  "version": 1,
  "previous": null,
  "status": "active",
  "bindings": [
    {"kind": "project", "id": "project:p"}
  ],
  "location": {
    "remote": "ssh://git.example/project-p.git",
    "branch": "main"
  },
  "genesis_digest": "sha256:...",
  "access_policy": {
    "version": 4,
    "digest": "sha256:..."
  },
  "owners": ["owner:p"]
}
```

`bindings[].kind` is `identity` or `project`; identifiers are opaque. `access_policy` identifies an observed owner-signed target policy. **Do not copy reader/writer ACLs into the directory.**

An active entry has two signatures over its complete canonical payload:

- A **target-space owner endorsement**, verified against the named target policy.
- A **directory publication signature**, made by a platform-space owner authorized by the preceding platform policy.

Use separate purpose tags for these signatures. Temporary owner-registered keys suffice; no key holder is assumed.

The platform space’s policy owners own the directory. For v1, they publish entries directly; delegation to directory maintainers can wait. This administrative endorsement does not introduce review gates for ordinary memory writes.

A withdrawal is a closed tombstone containing format, directory space, space ID, version, previous digest and `status: withdrawn`. A directory owner can sign it without cooperation from the target owner.

**Verification flow:**

1. Verify the platform space from its independently obtained genesis pin and accepted policy history.
2. Verify the directory signature and contiguous entry version/digest chain.
3. Obtain the target policy chain; verify it from the endorsed target genesis pin, including the pinned policy and target endorsement.
4. Check space ID, kind and ownership bindings.
5. Sync the target and evaluate its **current** policy, registered reader key and transport access before reading.

The trusted platform endorsement authenticates discovery of the target genesis. A self-signed advertisement alone does not bootstrap trust.

### 2. Why

D-018 and architecture §5.4 describe discovery. D-019 and `repo/docs/signing-policy.md` put access and record validity elsewhere.

The directory is authoritative for **the platform’s endorsed identity/project-to-location binding**. It is not authoritative for:

- Current access or successful transport.
- Record validity, decision currentness or revision authority.
- Identity delegation.
- Ownership transfer merely asserted by an entry.

The target policy remains the access authority; Git hosting enforces coarse repository access. The directory’s policy reference is a verification pin and discovery aid, not a capability.

### 3. Trade-offs and rejected alternatives

Two endorsements prevent an ordinary platform writer from redirecting an identity to a self-controlled repository. Platform owners still control onboarding; this is deliberate trust concentration, not federation or consensus.

A domain assertion would mix administrative discovery with evidence evaluation and still require separate trust bootstrap. A new kernel kind would violate the five-kind boundary without adding value.

V1 directory contents must be suitable for every reader of the platform repository. Git access exposes stored bytes; adapter filtering cannot provide confidential per-entry storage.

### 4. Changes needed

- **Package — v1:** no kernel semantic change. Document the directory boundary in the adapter contract.
- **Architecture — v1:** expand §5.4 with ownership, signature verification, bootstrap and withdrawal rules.
- **Decisions — v1:** close question 9. Preserve the existing one-owner-signature policy-transition rule; introduce no implicit quorum.
- **Implementation — v1:** closed directory schemas, signature purposes, replay verification, discovery/configuration commands and diagnostics.
- **Later:** delegated maintainers, registry-backed identity proofs and confidential directory partitions.

For stale entries, retain the last verified version as historical discovery data. A failed sync cannot establish current access. An old policy pin is acceptable as an ancestor, but never overrides newer target policy. Ownership or location changes require renewed endorsement.

A tombstone stops discovery; it does **not** revoke target access or delete existing clones. Actual revocation requires target policy and Git permission changes.

### 5. Tests and gate

**Stage 5:**

1. Owners A and B each operate their own trusted agent and space.
2. Each owner grants the other agent Git read access, registers its public key where named-reader authentication requires it, and grants the target reader role.
3. Both spaces receive verified directory entries.
4. Fresh agent homes discover, clone and read the other owner’s space through the directory.
5. Revoke one target reader while leaving the advertisement unchanged: the next verified read must fail.

This shares existing trusted owners’ spaces; it does not create memory for ephemeral external guests under D-021.

Negative cases: missing endorsement, wrong-purpose signature, forged ownership, wrong genesis, changed remote, entry rollback, target history rewrite, removed reader and unregistered reader key. None may silently replace an established trust pin.

Non-interference: hidden memory-record changes cannot alter directory lookup results or manufacture access information.

For promotion, exercise an agent promoting **its own** record. The current CLI reattributes promotion to the caller (`repo/docs/cli.md`, “Promote”); cross-issuer promotion must not be presented as preserving the original issuer without authenticated representation.

### 6. Risks and confidence

**Confidence: high.** Bootstrap compromise and stale discovery remain the principal risks. Revoking future access cannot recall Git objects already cloned.

---

## Q3 — Policy-directed resolution, delivered through the existing board

### 1. Recommendation

Use **board tasks for v1 escalation**. Keep routing separate from decision authority.

Extend the signed space-policy resolver entry:

```json
{
  "area": "home-retention",
  "selector": {
    "subject": "subject:home-policy",
    "schema": {"id": "schema:decision", "version": 1},
    "slot": "[]"
  },
  "identities": ["owner:a"],
  "route": {
    "kind": "board",
    "board": "board:architecture",
    "parent": "task:decision-resolution"
  }
}
```

Each selector field is exact or `null` for unrestricted. Fields combine by conjunction. No substring matching, identifier-prefix interpretation or model classification.

All matching entries contribute recipients; union and deduplicate them. Overlapping routes do not grant priority or create a voting rule. If none matches, notify **all current space owners**, using the caller’s established board workflow. Missing delivery configuration is a routing failure, not permission to continue.

The `area` string is a label, not authority. The route names a destination; it grants no board mutation or disclosure rights.

#### Authority

A nominated resolver can investigate and recommend. To record the resolution it still needs:

- Its registered signing key and an applicable writer grant.
- Required retention authority.
- Issuer identity or checked representation for revisions.
- A canonical deciding-authority receipt for a `decision_record`.

An owner title or resolver nomination alone grants none of these. The current CLI explicitly gives owners reader/writer grants separately.

**V1 should support resolutions signed by the deciding issuer itself.** A resolver lacking representation obtains that issuer’s decision instead of impersonating it. Registry-backed delegation follows D-010 later; the platform’s general `grant/1` architecture is not an implemented memory delegation API.

#### Close the receipt-integration gap

The current `agentprofile` supplies **no authority events or third-party representations** and cannot admit authoritative decisions (`repo/docs/cli.md`, “Provisional trusted profile”; `repo/go/agentprofile/profile.go`).

Add a narrow, owner-signed receipt-import binding to space policy for v1. Each binding must pin:

```text
receipt source ref
deciding issuer
canonical external object/revision/digest
assertion subject/schema/perspective/slot/body digest
predecessor receipt refs
```

The importer verifies the actual deciding issuer’s signed decision in the designated canonical decision register or board/domain record. Space-owner endorsement admits that source; it does not replace the deciding issuer’s signature. Only then does the trusted adapter supply the existing kernel `authority_events` facts.

Neither a memory record’s signature nor a task’s “done” status can manufacture these facts. This adds an adapter binding, not a new kernel authority.

For `ambiguous_current`, issue a receipt succeeding **every conflicting maximum in that issuer’s order**, then import the new canonical decision. Do not attempt CAS replacement of an ambiguous head: K-REV-1 correctly rejects it.

#### Across spaces and owners

Keep results qualified by space, issuer, perspective and exact version. The implemented reader returns separate views; K-DOM-3 does not infer incompatibility across spaces.

When one task depends on incompatible readable decisions from different spaces, the **consumer** identifies that dependency conflict and stops its step. It must not relabel it kernel `ambiguous_current`.

Route to each affected space’s resolvers and the deciding issuers. Different owners resolve their own sequences. They may issue compatible successor decisions, or the task’s authorized owner may change the task’s dependency. One owner cannot supersede another owner’s decision merely through a newer timestamp, platform-space placement or majority vote. D-009 remains intact.

### 2. Why and concrete escalation flow

D-020 already specifies the stop-and-escalate boundary. Architecture §10 and `repo/SKILL.md` put action with the agent/orchestrator.

`platform-book/13-doska.md` describes today’s board storage, CLI, roles and review machinery. Chapter 15 identifies that board as working. Chapter 6 explicitly says general grants lack their own implemented module. The supplied material does not establish an implemented Keeper escalation endpoint. Therefore v1 should use the existing board, not depend on a new Keeper protocol.

Flow:

1. The task identifies the decision its next step requires.
2. `recall --require-current` returns conflict data and exit **7**.
3. The agent stops that dependent step; unrelated work may continue.
4. The CLI formats a local escalation packet. The agent/orchestrator creates or updates the board task under its existing board authority.
5. Record the task revision and confirmed assignment/delivery. Failed delivery remains a blocker.
6. Resolvers reread under their own authority and record the canonical resolution.
7. Sync and reevaluate the dependency. Resume only after the required resolution is admitted and usable—not because the board task closed.

The packet should contain:

```text
format, data classification, reporting identity, idempotency key
task/step and explicit dependency request
conflict kind: ambiguous_current | evidence_conflict | cross_space_dependency
exact candidate refs, qualified by space
verified policy/rule/evidence-policy pins and protected view bindings
both evidence channels, qualifications and relevant disclosed sources
matched areas, resolver identities and board destinations
requested decision and required supersession/receipt relationships
```

Sign the full report with the reporter’s registered key under a separate escalation-report purpose. This proves attribution, not decision authority.

**The full local packet is not automatically a board attachment.** The current profile has unknown lineage and no forward grants. V1 sends task-owned dependency/routing information and a resolution request; resolvers obtain memory evidence through their own reads. Include exact references or evidence on the board only with separately established metadata-disclosure/forwarding authority for that audience. Excerpts should not be copied by default.

### 3. Trade-offs and rejected alternatives

Board routing uses an existing durable workflow, but adds a board dependency to this consumer’s escalation path. Memory itself remains independent.

Reject:

- Keeper-first implementation without a supplied callable contract.
- A new `resolve` kernel privilege.
- Resolver nomination as blanket revision authority.
- Cross-owner last-writer-wins.
- Withdrawing somebody else’s opposing assessment to “clear” conflict.

A successor decision establishes what was decided next. Historical disagreement and its evidence remain.

### 4. Changes needed

- **Package — v1:** preserve K-REV-1/3/4 and issuer-local order. Update the adapter’s receipt-verification contract; add semantic regression vectors for resolution of multiple maxima. Any changed kernel result requires the package release.
- **Architecture — v1:** specify selectors, fallback, board routing, receipt admission and resumption.
- **Decisions — v1:** close question 8 within D-020. No cross-authority ordering extension is proposed.
- **Implementation — v1:** versioned policy schemas, routing validation, packet formatter, skill/board integration and authenticated receipt import. Historical policies retain their original interpretation.
- **Later:** Keeper obligations, retries/deadlines, role resolution and registry-backed representation. These must not become prerequisites for stopping a dependent step.

### 5. Tests and gate

- Selector match, overlap union and owner fallback; no heuristic area matching.
- Resolver without writer/representation authority cannot revise another issuer; a properly authorized issuer succeeds.
- Forked canonical receipts remain ambiguous; a genuine same-issuer successor of both resolves currentness. Preserve S34–S42’s foreign-event invariance.
- Forged, mismatched, prior or incomparable receipts cannot resolve the conflict.
- Evidence conflict preserves both channels; `version_conflict` remains a write refusal.
- Two-space disagreement reaches both resolver sets without inventing a global order.
- Hidden-only conflicts cause no new visible blocker, packet, recipient count or task. Recheck disclosure before sending.
- Repeated escalation reuses one incident; policy changes trigger fresh routing verification.

**Stage 6 gate:** exercise the installed agent/skill against conflicting decisions backed by genuinely verified signed receipts. Observe exit 7, prove the dependent action did not run, and verify a real board task reached the configured resolvers. Then admit their valid successor and demonstrate continuation. A synthetic kernel snapshot or successful packet formatting alone does not pass this gate.

### 6. Risks and confidence

**Confidence: medium-high.** Routing is straightforward; authenticating canonical receipts is the substantial missing integration. The main failure risks are false authority, unauthorized evidence forwarding and treating task closure as resolution.

## For the owner

Two concrete inputs remain human-owned:

- **Name the actual directory stewards, trusted genesis anchors and resolver/board destinations.** The design can define verification and defaults, but cannot assign accountability or trust to real identities.
- **Where work requires agreement between independent owners, identify any mutually accepted deciding authority—or require compatible decisions from both.** Software cannot choose that authority without changing ownership semantics.