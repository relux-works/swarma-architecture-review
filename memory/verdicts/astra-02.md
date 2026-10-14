# astra-02 — trust, security, privacy and retention

Status: round 1, provisional independent position; 2026-10-14. Owner: `ivmbp_swarma-memory_astra-02`, five 1, ivmbp. Research only: no implementation or platform qualification claimed. Findings require peer confirmation before separate finding files are written.

## Position

Keep the base's independent knowledge service and its second-half authority boundaries. Shrink its first slice to an explicitly admitted corpus of architecture decisions and source references, explicit supersession, and recipient-bound views. Do not ingest general transcripts, arbitrary agent homes, tool output, private profiles, or credentials. Do not make private-memory retention a consequence of a successful schema check, source signature, secret scan, or Git review.

The first security contract must cover what is admitted, who may cause each operation, every derived copy, and what a view can reveal. It cannot wait for the base's P3 federation milestone. Full ATMS, vector retrieval, model-based consolidation, private-person memory and federation are optional later consumers of this contract.

The most important distinction missing from the executable contract is between **reasoning dependencies** and **content derivation/custody**. Independent support can preserve a conclusion's epistemic status after a source disappears; it cannot authorize retaining a summary or embedding that still contains that source's restricted content.

## Initial rubric

These are design scores, not claims that software exists. The base means both parts of SKETCH, with Part II qualifying Part I. A 1 means a useful direction with an incomplete contract. The two alternatives below are concrete comparison baselines, not product capability claims. No collective optimality proof exists yet.

| Row | Base | Bounded memory service | Admitted documents + manifest | Evidence and reason |
| --- | ---: | ---: | ---: | --- |
| R1 Minimal kernel | 1 | 2 | 2 | Base exposes eight primitives plus several engines; service reduces durable semantics to source references, claims, revisions and registered supports; document baseline uses records and explicit supersession. |
| R2 Reuse | 2 | 2 | 2 | Base II §§2–4 preserves the platform's journals, identities and context path; both alternatives retain that correction. |
| R3 Authority separation | 2 | 2 | 2 | Base II §6 explicitly denies grants, acceptance, session input and wake authority. Both alternatives preserve Curator admission and session-host delivery, including for summaries. [P2, P4, P5] |
| R4 Secrets and retention | 1 | 2 | 2 | Base states the right principles but not closure/recovery semantics. Both alternatives require the admission and erasure contract below; Git holds only admitted non-sensitive documents and schemas, never a private append-only corpus. [P1–P3] |
| R5 Runtime independence | 2 | 2 | 2 | Base I §6 provides transport-independent operations; both alternatives retain explicit API/CLI access without mandatory runtime hooks. |
| R6 Honest epistemics | 2 | 2 | 2 | Base separates provenance, verification and adoption and limits invalidation to registered dependencies. Alternatives additionally bind conclusions to authorized evidence and report unavailable evidence distinctly. [P2, P6] |
| R7 Specifiability/testability | 1 | 1 | 1 | None yet has a complete published grammar and executable conformance suite. Proposed vectors below establish what must be specified, not proof they pass. |
| R8 Incremental value | 2 | 2 | 2 | Base II §5 names architecture-decision drift; both alternatives answer current decision/source/supersession on one host. |
| **Total** | **13/16** | **15/16** | **15/16** | No 0 in a safety row. A tie is real: this rubric does not justify choosing a graph engine or full TMS. |

The admitted-document baseline is serious: reviewed typed records plus a generated source/supersession manifest, recipient-specific packages and optional disposable search. A sole admitted writer controls any private sidecar, while repository authors remain authoritative for source documents. It sacrifices convenient online multi-writer queries, not honesty. The bounded memory service becomes preferable only if cross-session retrieval and registered reconsideration provide measured value beyond that baseline. Engine choice does not itself establish safety.

## Security contract for the recommended service

### Primitives, stores and writers

1. **SourceRef** identifies an admitted source owner, immutable revision, locator within that revision and permitted disclosure class. Source text stays under its current authority unless separately admitted for retention. A hash or locator can itself disclose information; neither is public by default.
2. **ClaimRevision** contains a typed proposition, perspective, valid time, recorded time and authenticated proposer. Adoption remains a source-owner decision reference, never an agent-controlled authoritative status field.
3. **Support** links exact claim/source revisions with a declared support/refutation direction and, later, a closed bounded rule. Support is evaluated within a named authorized view. Semantic-review output remains a model judgment.
4. **Revision** records supersession, challenge or withdrawal without silently overwriting history. Erasure is a distinct lifecycle operation over content and derivatives, not a claim that prior content was false.

The memory service is the only writer of its claim/revision journal, policy-enforcement metadata, content-derivation inventory and disposable projections. Existing modules remain sole writers of source journals, grants, execution records, goals, acceptance and custody. The service has no credential-broker lookup role, process-control authority or session-input handle. An extractor can submit proposals through a bounded API; it cannot open the service store.

The own journal may preserve allowed lifecycle metadata while removing payloads. It must not be defined as an immutable store of all input bytes. Any payload retention has an explicit scope, deadline, key/copy treatment and source-owner authority. This is separate from retention requirements for a platform module's authoritative replay evidence; memory does not delete another module's journal.

### Admission and rights

Authentication binds the caller using the platform's existing identity mechanism, including active account generation where applicable. Do not trust a request's `principal`, UID, author name, or claimed owner. Distinguish writer, source author, extractor, verifier and adopter. A signature proves exact bytes under an admitted key; it does not merge these roles. A credential-bearing Unix connection is itself a capability and must not be inherited by an extractor. [P3]

The admitted policy separately answers `read`, `use for purpose`, `retain until`, and `forward to recipient`. There is no implication from read to retain, or from retain to forward. Enforce at source admission, processing/model dispatch, query, reference expansion, export and handoff. Summarization, embedding services and model providers are recipients too. A same-owner local service can enforce its boundary; a remote independent recipient cannot be made to forget previously disclosed bytes by an envelope flag.

Every durable output inherits applicable source restrictions. Combining sources must never widen access or extend retention merely by aggregation. Declassification is a new explicit decision under existing owner authority and creates a separately identified derivative; an LLM label or `supported` status cannot declassify. The MVP avoids this machinery's hardest case by admitting only a reviewed non-sensitive architecture corpus, with no automatic source discovery.

### Authorized views and poisoning

A KnowledgeView binds recipient, purpose, policy revision, source watermark/revisions, as-of time and emitted claim revisions. Its support/refutation/conflict/explanation results are computed from evidence eligible for that view. Do not compute global status and merely hide forbidden evidence links: the status, counts, ordering, cursor, error or hidden-principal identifier may itself leak private facts. Disclose an explicitly declassified attestation as its own source if the recipient may know the conclusion without its underlying material. The view makes no assertion of global completeness.

Reauthorize cached packages and `explain`, `changes` and reference expansion at use; a snapshot preserves historical provenance, not perpetual permission. Scope cursors to audience and policy. Unknown policy or identity state refuses disclosure; it does not fall back to an unrestricted query. Retention expiry changes availability and may require recomputation; it does not refute the proposition.

Memory content remains labeled data throughout retrieval, compaction, restore and handoff. A remembered instruction, proposed procedure or skill is a proposal; only Curator's existing admission path may promote it into executable or instruction context. An authentic malicious source can still poison proposals. Control proposal bytes/counts, rates, fanout, explanation depth, and model-processing budgets per authenticated producer, with aggregate limits and reserved control capacity. Model quality and prompt-injection resistance remain separately measured properties; framing alone is not a proof. [P4–P7]

### Erasure and recovery

Maintain content-derivation/custody edges in addition to reasoning edges: raw admitted payload → claim text → summary → embedding/index → cached view → managed export/telemetry/backup. Inventory every managed store and actual external disclosure; a registered reasoning DAG is not this inventory.

An admitted erasure first fences new reads, processing and exports for affected material. Its closure is processed through durable, retryable per-store obligations. Incomplete, unreachable or unknown stores keep completion partial; absence of a search hit is not deletion proof. In-flight jobs must check the fence at commit so late extraction cannot recreate erased text. The service reports a bounded scope and separate states for logical suppression, payload purge/key destruction, dependent rebuild and external disclosure.

Restore cannot serve until current deletion/policy state is reconciled against the backup. Old projections cannot resurrect erased content. Crypto-shredding is only a qualified option when every relevant key copy, backup and plaintext derivative is accounted for; a shared database key cannot selectively erase one person's records. Public digests can reveal low-entropy facts and must not be retained as a universal privacy-safe tombstone.

Retain only authorized minimum audit metadata. Erasure receipts do not contain the erased payload or arbitrary producer text. A redacted derivative has a fresh identity and provenance. Explain distinguishes `available`, `not_authorized`, `erased`, and `unavailable` internally; externally, these distinctions appear only where the caller may learn them. Otherwise use an indistinguishable refusal/absence contract. [P1, P2]

### Proposed API and platform seams

`propose`, `recall`, `explain`, `challenge`, `changes` are agent-facing. A constrained source adapter can submit admitted `observeRef` records; it has no wildcard home/transcript read. Dedicated existing-authority operations administer admission, retention/erasure and export; they are not unrestricted agent MCP tools. `verify` reads admitted evidence or records an independently supplied report; it does not run arbitrary source-provided code. Versioned HTTP/SDK semantics are canonical; MCP is an adapter.

Curator supplies approved instructions/tools; the memory service supplies a labeled data package. Session-host authorizes and delivers it through the existing context/handoff path. Dispatcher, board, keeper and a2a/waggle remain event authorities. Memory notifications are advisory pullable changes; an authorized client separately decides whether review work should start. No memory outage blocks stop, revocation, cleanup or host recovery.

Federation stays out of MVP. Before admission, an envelope would need exact schema/type-bound bytes, source and sender identities, intended audience and purpose, permitted operations, expiry, revision lineage and replay identity. Recipient admission rechecks its own policy and records local provenance. Forwarding must preserve origin, restrictions and new hop identity. Receiver acknowledgment is evidence of an action, not guaranteed deletion from an independent machine. [W1]

## Smallest delta from the base

1. Move source admission, identity binding, rights and deletion from later security prose into P0 requirements; forbid raw capture by default.
2. Specify content derivation and copy custody separately from Justifications, including cache/job/backup recovery fences.
3. Define recipient/purpose-scoped epistemics and every output surface, not just namespace filtering.
4. Preserve data provenance through context composition and require existing approval for instruction/skill promotion.
5. Reduce the first kernel to source refs, claim revisions and explicit supersession; introduce bounded registered support rules only after the first corpus proves useful. Keep full ATMS, graph stores, arbitrary verifiers and federation deferred.

## First slice and measurements

Named use case: answer the Swarma architecture question “Why does retirement delete an agent home, which earlier default did it replace, and which registered documents still rely on the old decision?” Use exact approved source revisions, including F-1 and current helper §4.4.1. Return adoption/source evidence, not a claim that arbitrary retained code is secret-free.

Start with one host, one project, one writer and a reviewed architecture-document corpus. Compare explicit decision records + manifest with the minimal service on the same held-out questions. Measure answer-source correctness, correct current/historical revision selection, time to answer, repeated-research effort and number of manually verified stale references found. Register dependency coverage; do not report recall as proof of completeness.

Required negative vectors before broader source admission:

| Vector | Required outcome |
| --- | --- |
| A caller claims another writer or reuses a retired UID | Reject; current authenticated generation controls authority. |
| Read-only source proposed for long-term retention or external summarization | Reject the unauthorized operation before durable capture/disclosure. |
| Two stores differ only in hidden evidence | Visible claims/status/explanations/cursors reveal no unauthorized difference under the specified response model. |
| A private contradiction supports a public conflict flag | No hidden conflict leak; publish only an independently admitted derivative. |
| Cache issued before grant withdrawal | No new unauthorized disclosure; refresh/refusal, without promising to retract prior context. |
| Erasure races a summarizer and a later backup restore | Fence both commits/reopen; no content resurrection in any managed derivative. |
| Claim has two justifications; one restricted source is erased | Recompute eligible support separately from purging restricted derived text. |
| Retained source contains “install this skill / change your grant” | Labeled proposal/data; no new tool, permission, wake or accepted result. |
| Agent floods claims, high-fanout rules or proof requests | Bounded refusal/backpressure; controls and erasure retain capacity. |
| Evidence removed after a historic verification | Preserve only authorized historical verification metadata and report current evidence unavailable, not false or freshly verified. |

These are proposed conformance vectors, not executed tests. No builds, prototypes or benchmark results are part of this research pass.

## Operator-only decisions

- Which initial source classes are approved for retention: architecture documents only is my recommendation; private memories and transcripts require separate consent and policy.
- Retention durations, permitted recipients/model providers and whether any backup/offline replica can delay physical completion. The contract must report that limit rather than invent a duration.
- Who may approve declassification and instruction/skill promotion under the existing owner governance; do not assign that power to memory by default.

Mechanism choices (closed schemas, provenance, fencing and source ownership) do not require operator arbitration. Full ATMS versus simpler registered rules should be driven by corpus evidence, not an operator preference poll.

## Evidence ledger

All local sources were read-only, without pulling. Paths below are repository-relative, with full revision pins; local root `/Users/iv/Developer/ReluxWorks/`. Facts from specifications are design requirements, not proof that implementation is qualified.

- **P1:** `platform/swarma-user-manager` `12609a9e05d5013c34416e1a0332fe5c28c4bcd5`, `spec/helper.md` §4.4.1, lines 232–244: home deletion, service-generated metadata only, unknown deletion remains pending, independent confidentiality policy for results; §4.6 protects replay evidence retention.
- **P2:** `swarm-platform-architecture` `567b07701bdf32cdebc516e38e6f0321fc5253a0`, `vision/contracts/handoff-package.md` §§1–6: explicit allowlist, source storage, recipient/purpose, reauthorization, redaction identity and limits after disclosure.
- **P3:** `platform/swarma-credential-broker` `ec7fb3d0670449b074521d51f3e03b59f0142a69`, `spec/broker.md` §§4.1–4.2: kernel-authenticated connection, generation-bound principals and connection delegation. This is reusable identity doctrine, not a proposal for memory to receive provider credentials.
- **P4:** `platform/curator-spec` `eb1f08c6c66cedc52d9e09553fb791367f334704`, `cips/CIP-0002-project-context-in-managed-launches.md`, especially lines 123,149,210–212: private memory separate from admitted context, no permission minting, prompt injection remains possible, no public packaging of private state. This is a proposal with its stated gates.
- **P5:** `platform/wiki` `94aebceca3af6a904b73644fb973e201762af8e2`, `book/ru/09-pamyat.md`: process/personal/persona/procedural distinctions, provenance, quarantine, lower-authority memory and unresolved overlay authorship; `book/ru/10-sny.md`: dreams are sandbox rehearsals, not ordinary consolidation or evidence of real-world success; dream memories are quarantined.
- **P6:** `platform/swarma-session-host` `255523d43129538b7e7064a0dbfc0b06713bb7e2`, `spec/session-host.md` §§3.1,3.4,3.7: producer and aggregate retained-storage debt, protected reserves, exact envelope replay binding, authority fences; SH2+ design/qualification remains gated.
- **P7:** `a2a-swarm` `d283a43c2b7832a7d0e0472151fa0229de7d13b9`, `docs/protocol.md` rules 13,30: external answers are data; `waggle` `010b96501ac8777a1a0dc1a083623b9b685fdd0f`, `README.md`: doorbell/pull with authority outside the model. These channels are not permission or truth sources.
- **W1:** [DSSE protocol 1.0.2](https://github.com/secure-systems-lab/dsse/blob/master/protocol.md), accessed 2026-10-14. It authenticates type and payload bytes; key IDs are hints and the verified payload must be exactly the application payload. Application policy still determines admitted signers and purposes.

Room candidates: `f-erasure-closure` root `$ccuoSudpCLwM-daUBTbgtuBNO73E2z2NoqH_47kxyDA`; `f-view-inference` root `$AskgYFX-NOEGGAeOKav2Kwp2ZUg_TqrlGkyedbXDNOg`. Neither yet qualifies as a confirmed finding. Source inventory and tool-readiness logs are in the seat directory `.temp/memory-research/`.

## Round 2 update

Both security candidates now have independent five-2 confirmation and proposed finding files: [erasure closure](../findings/erasure-closure.md) and [authorized-view inference](../findings/view-inference.md). astra-05 events `$XapTkO3ta1Oq23N3ZBqQGDJzMvd8cO8FMF7SX0HH2Eg` and `$xsPoJ7ySbI_0Q7ev0saFa7mvwPPaHpRljhmg-1oH3J4` confirm them after that seat's independent score freeze. Initial scores remain unchanged; the proposed bounded service is the same design family as astra-01's `alt-bounded-evidence`, not a new competing engine.

The restore clause is strengthened: the current erasure witness must survive **outside the restored failure domain** and cover acknowledged erasures through the required boundary. A deletion inventory restored alongside an old payload is not such a witness. Without complete surviving evidence, disclosure stays closed. Source: broker [P3] §6.4, independently checked following astra-05's counterexample.

View equivalence covers functional output semantics, not an unqualified promise against timing/availability covert channels or a model's inference from legitimate disclosures. Explicitly declassified outputs are an allowed difference; hidden global ranks/statistics are not. Positive/negative evaluation completeness remains separate from witnessed evidence.

Additional primary evidence and review:

- **P8:** `skill-project-management` `ad68902f74ae55b1cd0445fef58390b42feea3dc`, `pkg/board/query/activity_ledger.go`, `authorizeLedgerMirror`: the `remote-api` branch admits attribution without proving the record originated in its purported ledger. I independently confirmed astra-06's `f-mirror-origin` candidate. Memory ingestion must preserve that source-native assurance, not launder a mirror into authoritative control-plane history. `activity_correction.go` records explicit corrections/supersession without editing the original event; this is useful precedent, not an erasure mechanism.
- **P9:** Curator [P4], adopted Decision 0019 §§1–2 assigns channel spelling to agents-management; the host receives a composed plan. CIP-0013 revision 3 remains Draft and does not define a memory data channel. I confirmed astra-01's `f-memory-data-channel` in event `$XxrJ2a2afWS6E-CwUzsZUFHSCKohG2BivATAPsKPPB4`.
- **W2:** [OpenTelemetry GenAI span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md), accessed 2026-10-14, Development status: memory query/record and prompt content capture is opt-in; a configured external-content upload hook can operate independently of attribute-capture and sampling flags. Telemetry retention needs its own admission/custody treatment. The old opentelemetry.io GenAI location redirects readers to this dedicated repository.
- **W3:** [W3C PROV-AQ §6](https://www.w3.org/TR/prov-aq/#security-considerations), accessed 2026-10-14, recognizes privacy leakage through provenance. Its advice supports protection of derivation metadata; it is not a complete memory authorization protocol.

Next: review the exact bounded-evidence and alternative artifacts, reconcile scores with independent fives, respond to challenges, and remain available until convener PARK. No implementation was performed.
