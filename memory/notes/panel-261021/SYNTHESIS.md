# Panel synthesis: OPEN-QUESTIONS 23, 9, 8 (2026-10-21)

The panel had seven independent seats:
- three gpt-6-astra at max effort;
- three claude-opus-5-5 at max effort;
- one muse-wonder-1.0-contributor at xhigh.

Each seat got the same brief and bundle, and none saw the others' answers (`BRIEF.md`, `RUN-RECORD.md`). The orchestrator wrote this synthesis. Counts below are seats out of 7.

The panel was unanimous on the architecture of all three answers. Seats differed only in details, and this synthesis settles those under the **Choice** lines. The owner card at the end lists only the points the material cannot settle.

One seat made a factual claim that the orchestrator checked and found false. wonder-1 said that `collectSources` adds justification source premises without a disclosure check. `ruleEligible` already checks `allowed()` on every source premise (`go/kernel/read.go:407`), so a hidden source makes the whole justification ineligible. There is no bug.

## Q1 (OQ 23): sources in the view → D-027

**Unanimous (7/7):**
- The kernel computes a disclosure-filtered source payload in the same view.
- There is no separate source-read operation in v1. It would add an existence oracle for guessed refs, a second cut binding and a second non-interference surface.
- There is no adapter-side lookup.
- A source the reader may not see is omitted entirely: no ref, entry, placeholder, count or cutoff. The kernel already enforces this through K-AUTH-1, `associatedSources` and `ruleEligible`.
- Audience projections carry no sources (K-DISC-2).
- Original-source availability and the retained excerpt are independent. A deleted session never hides the retained excerpt (D-016).
- Erasure leaves a header without bytes (K-ERASE-1).
- Source changes count in `changes`.
- The change ships as a package release with new vectors, including non-interference pairs, and scenario 11 is upgraded to the full gate.

**Choices on the details:**
- **Placement:** a view-level, deduplicated `sources` table (6/7; wonder-1 put the array per item). Its members are exactly the union of the displayed items' `source_refs`, sorted by (id, numeric version). `validate.py` checks this invariant, with a planted violation as its control.
- **`withheld`:** not a wire state in v1 (5/7). astra-3 and wonder-1 allowed a `withheld` excerpt for a header the reader may see. That needs per-payload disclosure labels, which belong to the protected profile, so it is later.
- **Fields:** a closed `oneOf`.
  - The live variant carries `ref`, `issuer`, `submitter`, `representation_ref`, `admission_class`, and the source body fields `owner`, `source_kind`, `object`, `revision`, `digest`, `provenance`, `origin`, `original_issuer` and `carrier`. It also carries effective `availability` (`resolvable` or `unavailable`) and `excerpt`, one of `{state: present, text}` or `{state: none}`.
  - The erased variant carries `availability: erased`, the structural fields and `excerpt: {state: erased}`. It has no object, revision, digest, origin or text.
  - `retention_admission` stays in the protected binding (4/7).
- **Effective availability:** the stored value, overridden by the latest query-eligible `availability` revision at or before the cut, by `source_access` facts and by erasure fences. This is the same computation as `sourceAvailable`. A retained excerpt never satisfies `source_requirement: current` and never raises `source_state`.
- **Budget:** building the table costs no logical budget and changes no evaluation, cutoff or completeness (opus-1, opus-2). The table only presents admitted state.
- **Version:** package `0.3.0-draft`. All URNs and `semantic_profile` move with it, which also closes OQ 18 (5/7; wonder-1 proposed 0.2.8).
- **Session locator mapping for new records** (adapter contract and CLI; opus-1 and opus-3 proposed it):

  | Field | Value |
  | --- | --- |
  | `owner` | `runtime:<runtime>` |
  | `object` | `session:<id>` |
  | `revision` | `message:<id>` or `index:<n>` |
  | `origin` | the canonical locator JSON, one root origin per message (K-DISC-3) |
  | `provenance` | `reported` |
  | availability | `unavailable` until a session-host export exists |

  `digest` covers **the retained text**, and the adapter contract says so explicitly. astra-2, astra-3, opus-1 and opus-3 all flagged that the current CLI hashes the supplied excerpt, not the whole message. A full-message digest comes with the session-host export. That needs a bytes digest algorithm, `sha256-bytes-v1`, in the source digest enum.

  Legacy records, with the locator in `origin` and the hash in `object`, stay valid and render as stored.
- **Deferred:** output bounds for very large source tables (astra-3), until measured.

**Vectors (union of the proposals; the package task picks the final numbering):**
- authorized locator plus exact excerpt, including Unicode and trailing newlines;
- unavailable original with a surviving excerpt, and no upgrade to fresh evidence;
- a hidden source append, availability revision or erase is invisible to the public reader, paired with a private-reader control that sees it;
- a visible source cited only by a hidden justification stays absent;
- probing by source id gives the same result as a non-existent id;
- an erased tombstone at current and historical cuts carries no text, digest or origin;
- an audience projection carries no sources;
- `changes` reports a visible source change and ignores a hidden one;
- the payload costs no budget;
- write-side refusals.

**Gate:** scenario 11 shows B the exact runtime, session, message, digest and multiline excerpt, with availability `unavailable`. After revocation B gets `not_authorized` with no data, and a regrant restores it. This unblocks TASK-261019-gak2ji.

## Q2 (OQ 9): the space directory → D-028

**Unanimous (7/7):**
- Entries are adapter-level signed objects under the platform space's reserved `directory/`, outside `records/`, outside the kernel and outside the package. A directory entry hands out trust anchors before any kernel read, and K-SCOPE-1 fixes the record kinds at five.
- Entries are signed under a new purpose, separate from record, policy, key-registration and write signatures.
- Entries are immutable and versioned, each naming the digest of its predecessor. Replay follows first-parent order, the first accepted version wins (as in D-025), and rewrites are diagnosed without hiding valid neighbours.
- The directory belongs to the platform space's owners. Agent writers cannot publish.
- The directory is authoritative **only for discovery**: space id → endorsed genesis pin, remote and branch, the identity or project bindings, and the listing status. It is never authoritative for read or write rights, keys, revision authority or content. Access truth stays in the target space's owner-signed policy and in git access. Revoking access means changing that policy and the git ACL; withdrawing an entry revokes nothing.
- `spaces add --from-directory` verifies the target chain from the entry's genesis and refuses a mismatch with nothing saved. It never silently re-pins.
- The stage-5 gate is two owners' agents reading each other's shared spaces, with negative controls showing the directory grants nothing.

**Choices on the details:**
- **Topology:** each owner's platform space holds that owner's directory, and an agent trusts only its own owner's platform pin (opus-1, opus-3). opus-2 proposed one shared platform space with per-owner sections; that remains possible later and is a federation step.
- **Signatures:** an entry is a **directory publication**, signed by an owner of the directory's platform policy, wrapping a **space advertisement** signed by an owner of the target space's policy (astra-1/2/3 and wonder-1, 4/7).
  - For an owner's own spaces both are signed by the same owner, which is cheap.
  - For a foreign space the advertisement carries the foreign owner's consent and genesis binding, and our owner's publication carries our trust. This answers opus-1's objection that a co-signature adds nothing when every key roots in one owner.
  - Purposes: `swarma-memory-space-advertisement/1` and `swarma-memory-directory/1`.
- **Fields:** `format`, `directory_space`, `space_id`, `version`, `previous`, `status`, `kind`, `bindings` and `git`, plus the advertisement's `genesis_digest` and `observed_policy`.
  - `status` is `active` or `withdrawn`.
  - `kind` is `agent`, `project` or `platform`.
  - `bindings` is a sorted set of `{kind: identity|project, id}`.
  - `git` is `{remote, branch}`.
  - `observed_policy` is `{version, digest}`, and it serves as the rollback floor on first clone.
  - Entries hold **no access lists or reader hints** (4/7). Hints go stale and look like authority. Entries have no expiry in v1.
- **Path:** `directory/<hex(space_id)>/<version>.json`.
- **Identifiers are owner-qualified** (`<owner>/<id>`), so two owners' agents cannot collide (opus-1, opus-3). `keys register` refuses a foreign key on an unqualified local id.
- **Remotes are data:** an ssh/https allowlist (file in tests), passed after `--`, with no helper forms (astra-2, opus-3).
- **v1 cross-owner access is read-only.** Guest writes come later through D-022.
- **Promotion across owners** needs a forward grant (opus-2). Until then it is refused.
- **Commands:** `directory publish|withdraw|list|show`, `spaces add --from-directory` and `spaces update --from-directory`. The update applies only a relocation under the same genesis.
- **Deferred:** delegated publishers (in the D-024 style), identity entries carrying keys (opus-2; the owner registry replaces them), expiry and re-signing, and federation.

**Stage-5 gate (e2e):**
- **Setup:** owners O1 and O2, each with a platform space and a project space. They exchange the genesis pins and agent keys out of band.
- **Positive path:** each owner grants the other's agent the reader role and git read access, and lists the other's space in its own directory. Each agent then finds the other owner's space through its own directory only, and recalls an attributed record together with its Q1 source payload.
- **Controls:**
  - a listed but unshared space is `not_authorized`;
  - revoking access with the entry still present gives `not_authorized`;
  - forged, wrong-purpose, wrong-genesis, rolled-back, competing and rewritten entries are rejected;
  - an agent-signed entry is rejected;
  - an unsafe remote is refused before git runs.

## Q3 (OQ 8, D-020): resolvers and escalation → D-029

**Unanimous (7/7):**
- **v1 escalation is a board task.** The board exists and works (platform book ch. 13, 15). Swarm Keeper is a role, and its obligation ledger is target design with no interface (`designs/bounded-evidence.md`), so building on it would mean inventing a component.
- The packet is transport-neutral, so Keeper can carry it later unchanged.
- Memory makes no board call and wakes no one. The agent or its orchestrator files the task.
- **Being named a resolver grants nothing:** no read, write, representation, revision or receipt authority. Resolution goes through the existing powers only (K-REV-1, K-REV-3, D-009, D-011).
- **The default resolver** is the space's policy owners, and the packet says which basis applied.
- **No cross-space or cross-owner precedence.** The kernel evaluates per space. A contradiction between spaces is a consumer-reported dependency conflict, routed to each affected space's resolvers, and no space wins by recency, kind or fetch order.
- **In v1 git spaces `ambiguous_current` cannot occur.** The provisional profile has no authority events and refuses `decision_record`, and git races become `version_conflict` (D-025). The kernel vectors S28, S34–S42 and P14 keep covering ambiguity until receipts are integrated.
- **Resuming** needs a fresh read that exits 0. Closing the board task is not enough.

**Choices on the details:**
- **Selector:** `resolvers: [{area, match: {schemas: [exact refs], subjects: [exact ids]}, identities}]`.
  - `area` is a unique label and never a classifier.
  - Empty lists mean "any". There are no prefixes, patterns or free text, because ids are opaque (K-ENV-1).
  - An entry with both lists empty is the catch-all, and there is at most one.
  - Overlapping entries are refused when the policy is signed, so the previous policy version stays in force and every conflict maps to one area (astra-3, opus-1). Union routing (astra-1) and first-match order (opus-3) were the alternatives.
  - Every named identity must hold reader and writer grants and a registered key in the same policy version, so it can verify a conflict and record a resolution (opus-1, opus-3).
  - There is no `route` field in v1: the escalation goes to the dependent task's own board. A route pointer is a later policy version (3 seats proposed one, 4 did not).
- **Resolution paths:**
  - the issuer replaces, corrects or withdraws its own record;
  - an assessment's issuer withdraws its assessment;
  - **ruling:** a resolver who is not the issuer records its own decision, and the dependent step re-points to it. The conflicted sequence stays visible and attributed (opus-1, opus-2, opus-3);
  - `ambiguous_current` ends only by a canonical receipt from the deciding authority that succeeds every maximum, which is later.
- **Triggers:**
  - `ambiguous_current`;
  - an evidence conflict, meaning both witnesses `present`;
  - a non-empty `incompatible_with` on a current assertion the step depends on: two current decisions that contradict each other on one slot are exactly the "two parallel views" D-020 rules out (opus-1, opus-2, opus-3).

  The dependency is named exactly, with `explain ID --require-current` or an exact-scope `recall --subject S --schema X --require-current`. Substring recall causes false stops.
- **Cross-owner:** an agent files only on its own owner's board. A foreign space's resolvers appear in the packet for information, because they are not "part of the trusted system" in D-020's sense.
- **Packet:** closed `swarma-memory-escalation/1`, with `data_classification: data`. It holds references and enumerations only, **no record content**: a poisoned record cannot write instructions into a resolver's task, and forwarding content would need a forward right. It contains:
  - the reporting identity and an opaque `dependent` (task, step);
  - per space: the verified commit, the policy version and digest, the conflict kind (`ambiguous_current`, `evidence_conflict`, `incompatible` or `reported`), the item refs with issuer and currentness, and the evidence refs from the reporter's authorized `explain`;
  - the matched area, the resolver identities and `resolver_basis` (`named`, `catch_all` or `default_owners`);
  - `conflict_key`, a hash of kind plus sorted (space, ref), without cursor or reporter, so that every reporter of one conflict converges on one task.

  Resolvers pull the evidence through their own reads.
- **CLI:** `memory conflicts` (alias `escalate`) is a pure read. It exits 0 when there is no conflict, exits 7 with the packet, and exits 3 for a ref it may not see (the same `record_not_found` as a non-existent ref). `explain` gains `--require-current`, and `policy resolvers set|show` writes and reads the entries.
- **Skill:** on exit 7:
  1. stop the dependent step;
  2. mark the own task blocked with the packet attached, or have the orchestrator file the resolver task, reusing an open task with the same `conflict_key`;
  3. resume after a fresh check exits 0.

  Never self-resolve unless you are both the resolver and the issuer.
- **Deferred:**
  - **receipt integration** for a decision register, which makes `ambiguous_current` real and lets a ruling become an authority receipt. astra-1/2/3 wanted it in v1 for an authoritative stage-6 run (3/7); opus-1/2/3 and wonder-1 put it later (4/7). v1 runs the gate on evidence conflicts and incompatibility, says so in the gate record, and records the dissent;
  - Keeper obligations and deadlines;
  - role-based resolvers;
  - route pointers.
- **D-020 clarification:** "supersedes under the existing order rules" means within the deciding issuer's own order. A resolver cannot replace another issuer's sequence; it rules, and the dependent work re-points. §10 step 4's "with their receipt" holds only once receipts are integrated.

**Stage-6 gate:**
- **Memory e2e.** The owner records decision D. Agent B assesses D opposed and agent C supported. Agent W's exact check exits 7, and its dependent write is absent. The packet routes to the area's resolvers, and two reporters produce one `conflict_key`. The issuer replaces D, and W's recheck exits 0.
  - **Controls:**
    - a conflict on another subject does not block;
    - a non-issuer's replace is refused with `representation_invalid`;
    - a non-resolver's ruling does not pass the resume check;
    - a hidden opposition does not block (non-interference);
    - no matching area gives `default_owners`;
    - an overlapping policy is refused;
    - content fields in the packet are forbidden;
    - memory makes no network or board call;
    - an instrument control fails the gate when exit 7 ignores the oppose witness.
- **Board integration on the real board.** The task is blocked with the packet attached, exactly one resolver task is filed per `conflict_key`, and the step resumes only after resolution.

## Owner card (points the panel could not settle)

1. **A second owner in practice.** Under this design, admitting another owner's agents means a manual exchange of genesis pins and agent public keys, foreign agents as named read-only readers in our spaces, and owner-qualified ids, until the owner registry exists. Stage 5 is built and gated with simulated owners. Admitting a real second owner stays your call when the case arrives.
2. **Can one opposing review stop work?** Under D-020 as written, a single attributed opposing review of a supported decision is an evidence conflict, and it stops the steps that depend on that decision. The alternative is to let only human, test or formal evidence stop work, which trades safety against denial of service by autonomous writers. The panel default is D-020 literally, measured in stage 7.
3. **Precedence between platform and project decisions.** The panel default is unanimous: memory ranks no space, and each space's resolvers decide. If platform decisions should bind projects, that is a governance rule for resolvers, not memory logic.
4. **Excerpt visibility.** Every reader of a shared space sees its retained excerpts and session ids. Git already exposes the bytes to them; Q1 makes that explicit in recall.
