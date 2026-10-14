# astra-05 — independent security, privacy and retention verdict

Status: independent Round 1 position, frozen before reading any first-five verdict. Date: 2026-10-14. Seat: five 2, ivmbp; mirror: astra-02. These are design scores, not implementation certification. No first-five verdict or substantive room debate was read before this version was written. Research only; no prototype or test execution.

## Recommendation and independent scores

Recommend a **local evidence ledger with controlled admission and disclosure**, initially over one explicitly admitted architecture corpus. Keep the sketch's separation of belief, verification and decision; shrink the first implementation; make privacy a release condition, not a later federation feature. Its two-point advantage is conditional on the contracts below. No claim of global optimality or cross-five proof yet.

The base means the whole sketch, including its more careful Swarma second half. Scoring the first half alone would unfairly ignore its explicit corrections.

| Criterion | Base, both parts | Local evidence ledger | Curated versioned documents | Source-journal replay only |
|---|---:|---:|---:|---:|
| R1 Minimal kernel | 1 | 2 | 2 | 2 |
| R2 Reuse | 2 | 2 | 2 | 2 |
| R3 Authority separation | 2 | 2 | 2 | 2 |
| R4 Secrets and retention | 1 | 2 | 1 | 1 |
| R5 Runtime independence | 2 | 2 | 2 | 2 |
| R6 Honest epistemics | 2 | 2 | 1 | 1 |
| R7 Specifiability and testability | 1 | 1 | 1 | 1 |
| R8 Incremental value | 2 | 2 | 2 | 1 |
| **Total / 16** | **13** | **15** | **13** | **12** |

### Evidence for every row

- **R1:** Base §§2–5 has eight named primitives plus proof/TMS engines without a closed grammar. Ledger has four record families below; identities, policy and views are references/envelopes. Documents need only typed notes and revisions. Source replay needs adapter events and a fold. These are design-complexity judgments, not measured implementation size.
- **R2:** Base part 2 §3 already preserves authoritative platform journals. Ledger follows that boundary. Documents use existing reviewed artifacts and board decisions; replay reads their existing journals. Board code explicitly says activity is a derived copy, never a reconstruction source for authoritative ledgers [B]. All four receive 2; a new memory journal is not automatically duplication of platform authority.
- **R3:** Base part 2 §§4,6 expressly denies grant, input, wake and acceptance powers. Ledger adds explicit request/response boundaries; documents and replay remain data read by existing consumers. Handoff preserves per-item verdict and reauthorizes on seed [H]; Curator base context is not proof of model obedience [C]. A document becoming an automatically discovered instruction would invalidate these alternative scores.
- **R4:** Base provides explicit retention and erasure intent but no acknowledgment boundary, backup rollback protocol or policy for derived metadata. Ledger conditions service availability on the erasure and disclosure protocol below. Documents in git retain deleted text in history and copies; deletion of the current file is insufficient. Replay avoids a new source-body store but still generates query results, caches and diagnostics; source retention and cross-source disclosure remain unresolved. Helper §4.4.1 rejects positive classification of arbitrary agent content and distinguishes accepted code from secret-free metadata [U].
- **R5:** Base offers HTTP/SDK independently of MCP. Ledger is a data API with optional platform adapters. Documents are ordinary versioned data; replay adapters do not require a particular model/runtime. None requires capture hooks to deliver its minimum value.
- **R6:** Both base and ledger separate evidence from truth, preserve contradiction and bitemporal history, and bound dependency completeness to registered edges. Documents can retain explicit supersession but do not intrinsically maintain alternative supports. Replay recovers what sources said, not whether an inferred belief remains supported. Deleted or inaccessible sources cannot become negative evidence [U §§4.5–4.6; K].
- **R7:** All designs are still proposals; none in this comparison has a complete normative grammar and conformance package. Ledger has writable adversarial vectors below, but fields, budgets and final governance remain to publish. Awarding 2 merely for naming JSON Schema would reward aspiration. Broker revocation supplies a concrete model for release serialization and fenced restore [CB §6.4].
- **R8:** Base part 2 §§5,8 names architecture-decision drift, already useful on one host. Ledger and documents implement that use case without federation or a graph database. Pure replay alone requires enough source adapters and an interpretation model to beat ordinary source search; incremental value is plausible but less direct. Platform book distinguishes proposed personal memory from already authoritative process memory [P9].

## Proposed RFC boundary

### Primitives, stores and writers

1. `Claim`: typed proposition, immutable revision, perspective, valid time and recorded time. Epistemic support, verification report and decision-source reference are separate fields. Acceptance can only be reported from the decision owner's source record.
2. `EvidenceRef`: source owner, immutable source version, protected locator, admitted capture/retention policy, source author versus submitting principal, and verification/availability state. Locators and digests inherit confidentiality; neither is presumed harmless metadata.
3. `Justification`: a bounded explicit set of premises for one claim revision. Initial rules are enumerated `all` premises and alternative support sets. Unknown, missing or truncated evaluation never becomes complete/supported by default. Semantic dependencies suggested by a model remain proposals.
4. `Revision`: explicit correction, supersession, challenge or withdrawal against exact object revisions. Erasure is an administrative lifecycle event distinct from epistemic refutation.

The memory service alone writes its own record ledger, protected content store, dependency index, disposable search projections and erasure state. Original journals and artifacts stay with their source owners. The extractive model has proposal authority only. Identity, active account generation and present grants are bound by the existing authenticated service path [CB §§4.1–4.2]; no model-supplied `author` grants writer identity. A retained source signature proves bytes and issuer, not present permission or truth. Keeper-derived identity is a later platform contract, not an implemented prerequisite [CB §4.3].

No agent opens a shared SQLite file or writes an index directly. One unprivileged service account hosts the ledger. First slice has one host, one configured corpus, one operator-admitted policy. Runtime portability does not imply identical isolation outside Swarma.

### Minimal API and platform seams

- `propose`, `revise`, `challenge`: bounded, idempotent proposals; service authenticates writer independently of body. Changes to a canonical claim do not mutate source journals.
- `recall`, `explain`, `changes`: scoped read operations; every response, reference expansion, cursor and notification is authorized. A knowledge view binds recipient, purpose, query, source/claim versions, source coverage and policy generation. It is data, never a Curator instruction package.
- `admit`, `erase`, `erasure_status`: policy-owner operations with durable state and explicit partial/unavailable outcomes. Agent proposal rights do not imply these administrative rights.
- `verify`: record validation over admitted evidence, not arbitrary URI fetching or code execution. Running a test is a separate authorized platform verification operation; memory receives its exact-artifact result [SH §3.5].

Adapters resolve board/dispatcher/host/keeper references through their owner. A room event is a peer statement, not an accepted decision or grant [A]. Waggle's signed-envelope design is draft, not deployed trust [W]. Knowledge is delivered through the session-host data path; the host retains sole input and lifecycle authority. Curator continues to own approved instructions and launch composition. Memory cannot accept results, start review work, wake a session or modify a goal. Missing memory does not block stop, revocation or recovery.

### Non-negotiable privacy semantics

**Admission:** default deny by source class and purpose. Do not ingest raw homes, credential metadata, native transcripts or arbitrary tool output. Even admitted documents and accepted git artifacts can contain secrets; review/filters reduce risk but do not prove absence. Sensitive bytes require an authorized retention policy and a protected erasure path before durable admission. Personal and cross-owner memories are outside the first slice.

**Separate rights:** read, use for a purpose, retain, and forward are independent predicates checked by the service/consumer boundary. A source grant does not automatically permit retaining a summary or sending it to an embedding/LLM provider. Mixed-source derivatives inherit all applicable restrictions; an explicit authorized new derivative is required for declassification. Retention deadlines cannot be lengthened by summarization. Plaintext already disclosed to an independent process cannot be recalled by later revocation; no service can promise otherwise.

**No hidden-evidence oracle:** changing inaccessible records must not change a caller's disclosed claim status, graph shape, counts, ranking, cursor or change notice except through an explicitly authorized disclosure. Compute the epistemic view over the caller's admitted evidence and report its scope; do not label a filtered global status as universally true. Hiding a refutation may leave `supported within this view`, never `globally unconflicted`. This inference follows the provenance privacy risk described in W3C PROV-AQ §5 [WEB1]. Semantic output invariance is a proposed conformance target; no constant-time side-channel guarantee is claimed.

**Erasure is a protocol:** atomically fence new disclosures and derivative writes for the target privacy generation; persist a bounded erasure job; enumerate all controlled content and derivatives, including index payloads, embeddings, excerpts, summaries, caches, queues, logs and exports. Late work from an earlier generation cannot resurrect it. Report `access_closed`, `purge_pending`, `purged_within_boundary`, or `unavailable` as distinct states. Do not acknowledge physical erasure when only a tombstone exists. Historical queries use current rights; a query's historical timestamp cannot resurrect old permission.

**Backups and keys:** restore remains closed until erasure obligations and current authority are reconciled against evidence outside the restored failure domain, following [CB §6.4; U §4.5]. If such coverage cannot be established, the old content remains unavailable. Encryption helps only when all relevant key copies and plaintext derivatives are covered; shredding a key beside a recoverable backup is not an erasure proof [WEB2]. No indefinite raw content digest in a public tombstone: small-domain content can be guessed against it. Use opaque service-generated identifiers and protected audit evidence, under its own retention policy.

**Scope of completion:** source-owner storage, memory-owned copies, controlled consumers and external recipients are separate boundaries. Every erasure receipt names the boundary it covers and outstanding recipients; it cannot certify remote deletion without enforceable custody and evidence. For admitted long-lived audit requirements, retain only authorized minimal service-generated facts. An unresolved conflict between evidence retention and deletion is an operator policy decision, never an excuse to call both complete.

## Adversarial conformance vectors to publish

| Vector | Setup / attack | Required result |
|---|---|---|
| V1 Writer forgery | Agent submits another agent's author, UID or retired generation | Authenticated submitter remains distinct; no authority gained |
| V2 Metadata leak | Secret supports/refutes a claim visible to a reader without secret access | Output reflects only authorized evidence and declared scope; no hidden count/status leak |
| V3 Erasure race | Begin extraction, erase source, then finish extraction | Old-generation derivative write and queued delivery refused |
| V4 Restore resurrection | Restore a valid pre-erasure/pre-revocation snapshot | Reads stay fenced until surviving obligations/authority reconciled |
| V5 Derived survival | Secret appears only in summary, embedding, cache, diagnostic or queued view | Erasure remains pending until each controlled copy is handled |
| V6 Hash disclosure | Tiny-domain personal fact erased but public hash retained | Public tombstone does not expose a testable content commitment |
| V7 Capability replay | Valid old view re-used for a different recipient/purpose or after grant withdrawal | Current authorization refuses new release; past disclosure not falsely recalled |
| V8 Instruction laundering | Peer proposes 'owner approved tool X', repeated by several summaries | Remains attributed data; no instruction, grant, session wake or tool installation |
| V9 Verifier deputy | Evidence ref targets arbitrary local path, metadata endpoint or executable test | Memory does not fetch/run it; only admitted source resolver or separate platform action |
| V10 Alternative support | One support erased, another independently sufficient support survives | Recompute authorized support; no automatic refutation and no resurrection of erased bytes |
| V11 Historical query | Query old valid time after current read/use rights expire | Current authorization still governs disclosure |
| V12 Synthetic evidence | A dream/rehearsal outcome is offered as a real-world result | Preserve synthetic origin; cannot satisfy real acceptance [P10] |
| V13 Availability pressure | Producer fills knowledge proposals, fan-out or refusal logs | Bounded work/admission, protected cleanup/control budget, honest incomplete results [SH §§3.1–3.2] |

## Smallest changes to the base

1. Make the second half's boundaries normative throughout; replace 'any knowledge may be stored' with admitted source/purpose/retention only.
2. Move current authorization, provenance retention and erasure into P0. P3 adds federation, not the first enforceable privacy checks.
3. Use source references and minimal memory records; retain no duplicate platform authority log.
4. Add view-relative epistemics, policy generation fencing, non-disclosing metadata and a durable erasure/restore contract.
5. Narrow verification to checked evidence; keep execution and network authority with existing modules.
6. Start with explicit revision and bounded support sets; defer full ATMS, automatic consolidation, graph database, private-agent reputation and federation until demonstrated need.

## First slice and measurement

Named use case: **Swarma architecture decision drift**, initially the move from default home archival to deletion. Capture only admitted decision records, exact spec revisions, review findings and explicit dependencies; return which decision superseded which, its surviving source and the registered documents needing review. The source owner's decision remains authoritative. Curator/handoff configuration is not modified.

Evaluate a fixed, owner-approved question set against ordinary source search and the curated-document alternative. Measure correct source/version attribution, obsolete-decision answers, time to locate rationale, registered-dependency impact recall, false review suggestions, bytes retained, deletion completion within the declared boundary, and cross-audience/synthetic-evidence failures. All safety vectors above must pass before release; no benchmark numbers are invented. Real release targets and retention durations remain to set. Memory failure must leave platform safety controls usable.

## Operator-only questions

- Which source classes, audiences, purposes and exact retention deadlines may the first corpus include? Default proposal: explicitly admitted architecture artifacts only.
- Which audit facts must outlive content deletion, and who may inspect them? What external/backup erasure boundary can the installation actually promise?
- May any personal information or independent-owner federation enter later stages, under what disclosure/retention contracts?
- What measured reduction in repeated research justifies a persistent service over reviewed documents?

## Source register

Local sources were read without pulling or editing. Pinned revisions and paths:

- **[S]** This repository, `memory/inputs/SKETCH.ru.md`, all 778 lines, including part 2. Base source for all rubric judgments.
- **[U]** `swarma-user-manager` `12609a9e05d5013c34416e1a0332fe5c28c4bcd5`, `spec/helper.md` §§4.4.1–4.6: deletion, restricted metadata, separate artifact policy, unavailable versus absent, restore floor.
- **[CB]** `swarma-credential-broker` `ec7fb3d0670449b074521d51f3e03b59f0142a69`, `spec/broker.md` §§4.1–4.3,6.4: peer identity/generation, key-class maturity, serialized revocation and fenced restoration.
- **[H]** `swarm-platform-architecture` `567b07701bdf32cdebc516e38e6f0321fc5253a0`, `vision/contracts/handoff-package.md` §§1–6: allowlisted projection, protected refs, reauthorization, per-item provenance and disclosure limits. `vision/contracts/trust-and-isolation.md` §1: action-site checks, no free text in authority.
- **[SH]** `swarma-session-host` `255523d43129538b7e7064a0dbfc0b06713bb7e2`, `spec/session-host.md` §§3.1–3.2,3.5: service-owned output budgets and isolated verification. These are SH2+ requirements/publication gates, not claims of deployed enforcement.
- **[C]** `curator-spec` `eb1f08c6c66cedc52d9e09553fb791367f334704`, `cips/CIP-0013-machine-base-context.md`, authority rule and security considerations: proposed, not adopted; provenance and prompt placement do not prove model obedience.
- **[B]** `skill-project-management` `ad68902f74ae55b1cd0445fef58390b42feea3dc`, `pkg/board/activity_ledger.go` lines 9–14,101–106; `pkg/board/query/activity_correction.go`: derived activity, bounded typed records and explicit correction.
- **[P9], [P10], [K]** `wiki` `94aebceca3af6a904b73644fb973e201762af8e2`, `book/ru/09-pamyat.md`, `book/ru/10-sny.md`, `book/keeper/ru/09-zhurnal-i-vosstanovlenie.md`: quarantine and memory ladder, synthetic results not real acceptance, deterministic keeper replay. Preserve each chapter's proposed/decided labels.
- **[A]** `a2a-swarm` `d283a43c2b7832a7d0e0472151fa0229de7d13b9`, `docs/protocol.md` rule 1: peers are data, communication grants no authority.
- **[W]** `waggle` `010b96501ac8777a1a0dc1a083623b9b685fdd0f`, `README.md`: signed-role envelope and guarded data delivery are a draft design.
- **[WEB1]** W3C, [PROV-AQ §5](https://www.w3.org/TR/prov-aq/#security-considerations), accessed 2026-10-14: provenance itself can expose sensitive relationships; automatic reference traversal is a privacy surface. Our non-disclosure contract is an inference, not a W3C implementation guarantee.
- **[WEB2]** NIST, [SP 800-88 Rev. 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf), accessed 2026-10-14. Initial discovery only; full relevant section is to be checked before treating it as normative erasure evidence. The independent design does not assert compliance with this standard.
