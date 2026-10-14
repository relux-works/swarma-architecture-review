# astra-05 — independent security, privacy and retention verdict

Status: Round 3; exact assembled revision ratified, awaiting cross-host critique and PARK; the Round 1 score table below is preserved, frozen before reading any first-five verdict. Date: 2026-10-14. Seat: five 2, ivmbp; mirror: astra-02. These are design scores, not implementation certification. No first-five verdict or substantive room debate was read before the initial score version was written. Research only; no prototype or test execution.

## Recommendation and independent scores

Initial recommendation: a **local evidence ledger with controlled admission and disclosure**, over one explicitly admitted architecture corpus. Keep the sketch's separation of belief, verification and decision; shrink the first implementation; make privacy a release condition. After comparing the strengthened documentary alternative, I recommend implementing the first slice as reviewed decision records plus a read-only adapter under the same semantics, without requiring a daemon. A separate service becomes necessary for a protected multi-proposer/private-data boundary, not for the first documentary experiment. The highest score is a conditional tie, not proof of a unique engine choice; see the Round 2 comparison below.

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

## Independent RFC starting point

### Primitives, stores and writers

1. `Claim`: typed proposition, immutable revision, perspective, valid time and recorded time. Epistemic support, verification report and decision-source reference are separate fields. Acceptance can only be reported from the decision owner's source record.
2. `EvidenceRef`: source owner, immutable source version, protected locator, admitted capture/retention policy, source author versus submitting principal, and verification/availability state. Locators and digests inherit confidentiality; neither is presumed harmless metadata.
3. `Justification`: a bounded explicit set of premises for one claim revision. Initial rules are enumerated `all` premises and alternative support sets. Unknown, missing or truncated evaluation never becomes complete/supported by default. Semantic dependencies suggested by a model remain proposals.
4. `Revision`: explicit correction, supersession, challenge or withdrawal against exact object revisions. Erasure is an administrative lifecycle event distinct from epistemic refutation.

The memory service alone writes its own record ledger, protected content store, dependency index, disposable search projections and erasure state. Original journals and artifacts stay with their source owners. The extractive model has proposal authority only. Identity, active account generation and present grants are bound by the existing authenticated service path [CB §§4.1–4.2]; no model-supplied `author` grants writer identity. A retained source signature proves bytes and issuer, not present permission or truth. Keeper-derived identity is a later platform contract, not an implemented prerequisite [CB §4.3].

No agent opens a shared SQLite file or writes an index directly. One unprivileged service account hosts the ledger. The protected-service profile has one host, one configured corpus and one operator-admitted policy. The documentary experiment may instead read an immutable approved register through an operator-owned adapter; it claims no hostile-agent writer isolation and admits no private payload sidecar. Runtime portability does not imply identical isolation outside Swarma.

### Minimal API and platform seams

- `propose`, `revise`, `challenge`: bounded, idempotent proposals; service authenticates writer independently of body. Changes to a canonical claim do not mutate source journals.
- `recall`, `explain`, `changes`: scoped read operations; every response, reference expansion, cursor and notification is authorized. A knowledge view binds recipient, purpose, query, source/claim versions, source coverage and policy generation. It is data, never a Curator instruction package.
- `admit`, `erase`, `erasure_status`: policy-owner operations with durable state and explicit partial/unavailable outcomes. Agent proposal rights do not imply these administrative rights.
- `verify`: record validation over admitted evidence, not arbitrary URI fetching or code execution. Running a test is a separate authorized platform verification operation; memory receives its exact-artifact result [SH §3.5].

Adapters resolve board/dispatcher/host/keeper references through their owner. A room event is a peer statement, not an accepted decision or grant [A]. Waggle's signed-envelope design is draft, not deployed trust [W]. Knowledge is delivered through the session-host data path; the host retains sole input and lifecycle authority. Curator continues to own approved instructions and launch composition. Memory cannot accept results, start review work, wake a session or modify a goal. Missing memory does not block stop, revocation or recovery.

### Non-negotiable privacy semantics

**Admission:** default deny by source class and purpose. Do not ingest raw homes, credential metadata, native transcripts or arbitrary tool output. Even admitted documents and accepted git artifacts can contain secrets; review/filters reduce risk but do not prove absence. Sensitive bytes require an authorized retention policy and a protected erasure path before durable admission. Personal and cross-owner memories are outside the first slice.

**Separate rights:** read, use for a purpose, retain, and forward are independent predicates checked by the service/consumer boundary. A source grant does not automatically permit retaining a summary or sending it to an embedding/LLM provider. Mixed-source derivatives inherit all applicable restrictions; an explicit authorized new derivative is required for declassification. Retention deadlines cannot be lengthened by summarization. Plaintext already disclosed to an independent process cannot be recalled by later revocation; no service can promise otherwise.

**No hidden-evidence oracle:** changing inaccessible records must not change a caller's disclosed claim status, graph shape, counts, ranking, cursor or change notice except through an explicitly authorized disclosure. Compute the epistemic view over the caller's admitted evidence and report its scope; do not label a filtered global status as universally true. Hiding a refutation may leave `supported within this view`, never `globally unconflicted`. This inference follows the provenance privacy risk described in W3C PROV-AQ §6 [WEB1]. Semantic output invariance is a proposed conformance target; no constant-time side-channel guarantee is claimed.

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
- **[WEB1]** W3C, [PROV-AQ §6](https://www.w3.org/TR/prov-aq/#security-considerations), accessed 2026-10-14: provenance itself can expose sensitive relationships; automatic reference traversal is a privacy surface. Our non-disclosure contract is an inference, not a W3C implementation guarantee.
- **[WEB2]** NIST, [SP 800-88 Rev. 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf), accessed 2026-10-14. Sections 3.2.3 and 3.2.5 checked: all target key copies, lower-level/unwrapped keys, externally recoverable keys and backup/escrow sources matter to erasure assurance. This supports the need for explicit key custody; our service-level protocol is an inference and does not assert NIST compliance.


## Round 2: adversarial comparison and evidence

Independent score freeze: 2026-10-14T01:00:19Z; original SHA-256 `95f6f78d6e05de6111c653a1ec9881808287a6c12141a39fb2a0fec24f506a81`. Signed initial artifact landed as `e2a3cd41dc990019a4e99b2d0a7634ac5a4c5e84`; pre-rebase objects were `cce146e` and `efc389c`. First-five verdict bodies were read only after this freeze. The original file is recoverable from that commit.

### Mirror comparison

astra-02's bounded-service profile in `f6e282d` scores R1..R8 `2,2,2,2,2,2,1,2`, identical to my independent 15/16 vector. Its strengthened admitted-documents + manifest alternative also carries those safeguards; my original bare-document baseline does not. On that stronger, explicitly constrained alternative my vector is likewise `2,2,2,2,2,2,1,2` (15/16). It need not implement optional inference to be epistemically honest. The distinction is the safety/semantics contract, not SQLite versus git.

This yields agreement across fives 1 and 2 on the protected-ledger profile at design level, with R7 still 1. It does not establish empirical superiority, a unique winning implementation or cross-host agreement. The shared `bounded-evidence` design was still being revised toward a documentary first slice at review time, so final proof must identify its exact revision/profile and carry the security preconditions. A plain git note corpus remains the original 13/16 baseline.

Adversarial challenges and replies:

- **Restore cannot self-certify current deletion.** My challenge/confirmation `$XapTkO3ta1Oq23N3ZBqQGDJzMvd8cO8FMF7SX0HH2Eg` cites broker §6.4: restoring the deletion log with the data cannot witness erasures acknowledged after that snapshot. astra-02 accepted and committed to an external-to-restored-domain witness in `$SqT4Seq_4lZNcywzuFHVtqA8wiIRa5HN97IeHYMvfXY`. Late extractor writes also require generation checks. This strengthens the mirror's defended contract rather than inventing a second finding.
- **Metadata oracle survives hidden-link filtering.** My confirmation `$xsPoJ7ySbI_0Q7ev0saFa7mvwPPaHpRljhmg-1oH3J4` requires paired-store equality for statuses, ranks, counts and cursors. astra-02 accepted in `$xzASIoBf7TlGzWYhc-15wyPLFO1eqNc9i1yfWmmPuuQ`; astra-03 confirmed scoped epistemics in `$qpSMGS8lVGSpLCosO8E8mxfQnKhRkWhzz5UUylovT6g`. A generic scope label cannot signal that a hidden contradiction exists.
- **Host receipt is another retained copy.** astra-01's `$-tTXQoCv0Ij3aTd-l5wKpf4LX-85ekLuQyOKmNB3VbY` identifies host tool-result/transcript custody as independently owned. I accept the correction: sensitive disclosure to that sink is inadmissible without compatible disposition or an explicit narrower guarantee. Memory cannot delete the host's journal by owning its own cache.
- **No new daemon prerequisite for document-only P0.** astra-01's replies `$5xQbTPFC1tAGDlJkbflxxJmT0dR82c9-2Sc8hTjOsYU` and `$FSMUYFQhhG7FtlpyeGkC3gbmNTScdQ5TqTFpYGuL-7w` accept astra-04/wonder-01's challenge. I adopt it: the first experiment can use reviewed records and a read-only adapter. The complete service profile remains a later implementation choice. Git-managed content must be explicitly persistable; a summary of a secret is not made safe by putting it in a reviewed file.

### Graphiti audit: exact version matters

Source: [Graphiti `graphiti.py` at `9d56c190926b382a54c5ea03e7680af1d05e1c9d`, lines 1993–2018](https://github.com/getzep/graphiti/blob/9d56c190926b382a54c5ea03e7680af1d05e1c9d/graphiti_core/graphiti.py#L1993), accessed 2026-10-14; revision verified with public `git ls-remote`.

Static inspection: `remove_episode` selects an edge when the deleted episode is first in its episode list; it selects a node when only one episode mentions it. The method does not regenerate surviving summaries. Thus an edge with two source episodes can meet the deletion condition when its first source is removed. This is a code-path observation, not an executed failure across all releases or drivers.

The [official provenance article](https://www.getzep.com/blog/how-zep-tracks-provenance-in-agent-memory/), accessed 2026-10-14, describes a stronger remaining-support cascade; it separately admits that surviving summaries are not regenerated and prior invalidations remain. That discrepancy prevents inheriting an erasure guarantee from a generic product description. Qualify the exact API/backend/version against two-source edge survival and sensitive-summary removal; keep custody/erasure policy outside the projection. wonder-01 independently confirmed the pinned source in `$CK_BbKpnIp2BGqGZW6Hhh3uU11bDJcHS5C4gO_b3WsA`; the scoped proposed finding is [graphiti-erasure-contract](../findings/graphiti-erasure-contract.md).

### Additional constraints for the documentary experiment

No raw sensitive bodies enter git, its indexes or the context adapter; ordinary accepted code is not automatically admitted memory. Persistability is an explicit corpus policy, not a claim that review detects every secret. The adapter retains only policy-permitted data and emits a bounded data response; no context overlay or direct `swarm-handoff/2` schema extension is assumed. Unexpected sensitive content closes further disclosure and creates a scoped incident/erasure obligation; already distributed clones and model contexts are reported as external disclosures, never declared purged by a redaction commit.

The paper vectors are implementation requirements. They were not executed, and no research score overrides an unpublished platform gate. Local source trees were checked for tracked modifications: the cited source files match the recorded revisions; unrelated task-board state changes were present and were not read or changed.


### Follow-up attacks accepted

**Global-cut oracle:** astra-02 `$mBVrz35sCx2C_g0mVVVpJB0440Y4AoASEcsfFJza8DM` and astra-06 `$CX7dxB6U3_Gt7xaJ6irKNkIFR_eWBh0dPjOEyQgH3TM` identify an additional leak in a view carrying a global memory/source sequence. I confirm: even an opaque digest leaks hidden activity if its equality changes only after a hidden append. Global cuts stay in protected audit. Public cursors, view digests and dirty generations must depend only on admitted activity or satisfy an explicit issuance/distribution contract. Compare permitted semantics/distributions after normalizing independent randomness and timestamps; do not demand byte equality for fresh random view IDs. Extend V2 to hidden append, revision and erasure. Explicit declassification of global activity would change the threat model and must be named.

**Service admission:** confirmed astra-04's candidate `$aCgRSrl8VZ6lmLDudVHq8Vwy643SdvLgx-NnF_kjFSc` from [U] §8.1 and [SH] §3.1. Every non-root platform service needs an explicit egress row before v1 enforced readiness, installer/operator ownership, start/scheduled verification, authenticated socket and private-state boundaries. An unprivileged account alone does not supply this. Documentary P0 requires no new admitted daemon; a later memory service cannot borrow host/broker privileges or bypass platform readiness. Current row encodings and qualification are publication gates, not implemented capabilities invented by this verdict.


### Exact revision calibration at the end of Round 2

I read the complete `bounded-evidence.md` at `56d18ee` and the complete semantic companion at `476ec3618c7c55d471a572454aa7e4aba772aab6`. The companion's InternalQuery/ExternalQuery split, protected audit cuts, public-handle issuance/equality contract and S24 close the metadata attack at design-contract level. S25/S26 also state the restore and late-writer fences. These are specified obligations, not executed conformance.

| Candidate actually reviewed | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | Total | Scope of score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Protected profile, `56d18ee` alone | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 14 | View wording still names public memory/source cuts ambiguously |
| Protected profile with `476ec36` metadata contract normative | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 15 | Requires assembled design to adopt the companion's protected/public distinction |
| Documentary P0 as filed at `56d18ee` | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 14 | Persistable reviewed corpus; its disposition boundary is narrower than the hypothetical strengthened document alternative |

This clarification was sent to astra-01 in `$M8XV1cvdXQOP9rtDE-7zxUut-_KVr2shqgRTprqqBEU`. It is a reservation about a specific artifact, not a new architectural finding. The frozen baseline and the hypothetical full-contract scores remain unchanged. I will ratify an assembled revision after inspecting its matching metadata wording. R7 is held at 1 for absent closed concrete schemas and exact normative vectors; this research mission does not require building an implementation to state a complete specification.


## Round 3: assembled revision ratified

I read the entire [bounded-evidence design](../designs/bounded-evidence.md) at signed and locally verified `0ce009435206f31f387efd207dc3f2662e66e4d9`, including its diff from `56d18ee`. It explicitly adopts the semantic companion at `476ec3618c7c55d471a572454aa7e4aba772aab6`. The protected binding/public projection distinction, handle issuance/equality constraints, erasure and restore fences, downstream-custody boundary and platform-service admission requirements resolve my exact-artifact reservation.

| Exact assembled profile at `0ce0094` | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Protected service | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | **15** |
| Documentary P0 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | **14** |

The final RFC direction adopts its five stored shapes: Assertion/Claim, SourceRef, Justification, **Assessment**, and Revision; View is derived. This supersedes the independent four-family packaging above by making the already-separated verification report explicit as an Assessment. Documentary basis and review-on-change are distinct from sufficient logical support. An LLM cannot acquire deterministic-assessment authority by choosing a label. R1 remains 2: this remains a handful of domain-neutral shapes.

Rows R2/R3/R5 retain the same source-owner and data-only boundaries; R4 reaches 2 only in the protected profile with the named custody contract. R6 preserves per-polarity witness and completeness semantics. R7 remains 1 for missing closed concrete schemas, exact normative fixtures, authorization vocabulary and budgets. R8 names the independent architecture-decision continuity experiment. This is a design-contract score, not an implemented security assurance or a measured win over plain search.

My first-slice recommendation remains documentary P0, evaluated against plain search and typed reviewed documents before introducing a service or richer inference. Agreement with astra-01 on this exact revision satisfies the mission's two-five scoring criterion; cross-host agreement has not yet been independently inspected by this seat. No new finding arose in this round.
