# Bounded support semantics for evidence memory

Owner: astra-03, five 1. Date: 2026-10-14. Status: draft research contract, not a released specification. Companion to astra-01's `alt-bounded-evidence` candidate; the platform design remains that seat's responsibility. [Position and scores](../verdicts/astra-03.md); [source evidence](../notes/astra-03-evidence.md).

## 1. What the kernel promises

Memory answers: which admitted sources and explicitly registered reasoning support or oppose a precisely scoped assertion at a named snapshot? It does not answer: what is absolutely true, which agent may act, or which decision should now be adopted.

The core is a typed admission journal plus derived views. An empty result never establishes falsity. A stored quotation proves at most that the quoted source made a statement. A syntactically valid reasoning edge does not prove its semantic correctness. These distinctions survive every summary and export.

M0 stores attributed assertions, exact source references, assessments and explicit revisions. It can be a reviewed persistable documentation register plus read-only adapter, or an operator-owned embedded store, with no daemon and no hostile-writer isolation claim. A managed service is a separate profile for private data or multiple autonomous proposing principals. M1 adds bounded support evaluation. Neither needs full ATMS, a graph database or a new platform registry.

## 2. Minimal record model

Five record kinds share an authenticated envelope. `Principal` and `Space` reference identities and policies supplied by the deployment; they are not new registries. `KnowledgeView` is query output. An `Observation` is represented by admission of a source reference and, where authorized, an immutable attributed assertion; no global event-log copy is required.

| Kind | Meaning | Must not imply |
|---|---|---|
| Claim | Immutable revision of a typed, attributed proposition with explicit scope | It is true, verified or adopted |
| SourceRef | Exact source identity/revision and documentary relation; optional allowed excerpt | Source content establishes the proposition it reports |
| Justification | Typed documentary, impact or sufficient-support relation, with provenance and qualification | Any dependency is an inference rule |
| Assessment | Scoped result of a named check or reviewer, with subject/rule/policy/environment pins | A single universal `verified` flag |
| Revision | Typed withdrawal, replacement, correction or availability transition referencing exact prior objects | Losing support refutes a proposition or cancels an owner decision |

Every record has an internal writer-assigned sequence. It is protected audit metadata, not automatically part of a public record or receipt. Source sequence numbers remain in their own namespaces; no timestamp or memory sequence imposes a total order over independent authorities. Wall-clock times are descriptive; journal sequence defines admission order.

An authority assertion such as “the owner adopted policy P” is a claim about an external decision record. Its currentness is projected from that authority's exact source revision. A memory proposal can challenge it, but cannot create or revoke the underlying decision.

## 3. Draft closed semantic profile

This is an RFC starting point, with a finite operation vocabulary and rejection rules. It is not a claim that a JSON Schema or executable suite already exists.

```text
RecordKind = claim | source | justification | assessment | revision
Polarity   = support | oppose
RuleKind   = declared_rationale | checked_entailment
EdgeRole   = documentary_basis | review_on_change | sufficient_support
CheckKind  = source_binding | signature | test_result | formal_entailment | semantic_review
CheckResult = pass | fail | indeterminate
RevisionKind = withdraw | replace | correct | availability
Availability = resolvable | unavailable | erased
Evaluation = complete | incomplete
Mode       = real | simulated

Literal = (claim_revision_id, Polarity)
Rule = (rule_id, rule_revision, EdgeRole, RuleKind, nonempty all_of[Literal], Literal)
InternalQuery = (principal, purpose, space, perspective, mode, valid_at,
                 memory_watermark, source_watermarks, semantic_profile, policy_revision)
ExternalQuery = (authorized_scope, purpose, valid_at, snapshot_handle?, bounds)
```

Each concrete record schema is closed: unknown fields, schema versions, tags, duplicate object keys and malformed references fail admission. IDs are opaque within a typed issuer namespace. External ref strings are never executed. Claim predicate schemas specify exact types and equality; unversioned natural-language “same meaning” is not identity. A separate `equivalent` claim does not merge objects automatically. A digest identifies canonical bytes under a named algorithm/framing version; not the semantic meaning of a sentence.

Claim revisions use half-open valid intervals `[from,to)` with explicit UTC precision; absent end means unbounded. Unknown valid time is a separate value, never an invented timestamp. Memory admission sequence and recorded UTC time identify when this installation learned the assertion. A delayed correction preserves both when it was learned and which valid interval it affects. Unknown-valid-time claims are returned as such and cannot silently answer a point-in-time query.

Each registered rule is finite and ground: no variables, recursive generation, executable callbacks, default negation, quantifiers or arbitrary code. Dependency edges between exact claim revisions form a DAG. Self-dependency, a cycle, unknown references and cross-scope inputs without an explicit authorized mapping are rejected atomically. Other graph relations may have cycles; the rule restriction does not prohibit a cyclic social or entity graph.

Alternatives are multiple sufficient-support rules with the same signed conclusion. They are OR, while each rule's premises are AND. These are one-way rules, not equations or biconditional definitions. There is no completion or implicit contraposition. In particular, opposing A and D in `(A AND B) -> C` and `(D AND E) -> C` supplies no opposing witness for C. `oppose(A)` is explicit contrary evidence, not `not support(A)`. No rule follows from a contradiction unless that exact rule was explicitly admitted. A predicate declaring functional uniqueness may propose a contradiction check, but changing a value is not automatically refutation outside its defined scope and overlapping valid time.

A rule has its own authenticated proposer/source, admission policy and applicability interval. An arbitrary agent cannot make a premise entail a conclusion merely by selecting `checked_entailment`; that qualification requires a passing deterministic assessment bound to the rule version and exact checked objects. An LLM review remains `semantic_review`. `declared_rationale` says the author registered that rationale; it creates `review_on_change` impact edges and does not propagate a signed conclusion. `sufficient_support` requires an admitted checked rule; its proof is conditional on the qualified premises, never a guarantee that those premises describe the world correctly.

A `documentary_basis` relation establishes attribution such as `source_says(S,p)`, never p by itself. A root support/opposition assessment for p must explicitly target that claim revision and polarity, identify its assessor and qualification, and pass the pinned evidence-admission policy. Source existence, signature or quotation checks alone cannot manufacture that semantic assessment. Assessments about a remote board mirror preserve submitter attribution; they do not prove its purported source-ledger event occurred. A deployment must name which root evidence qualifications count toward its support display. The query pins that policy. The presentation names them, e.g. “supported by a reviewer assessment” rather than “proven.” Policy changes never silently rewrite previous view receipts.

## 4. Support channels and completeness

For a fixed authorized query scope Q, let `W+(c,Q)` mean at least one admissible positive witness and `W-(c,Q)` at least one admissible opposing witness for the exact claim revision. A witness consists of a currently applicable root support/opposition assessment, or one admitted sufficient-support rule whose required signed premises have witnesses under that same Q. Verification qualifications remain attached to the witness. Documentary and review-on-change edges do not enter this calculation.

The evidence display is `(W+,W-)`: neither, positive only, negative only, both. It describes evidence found, not truth or probability. This is a Belnap-inspired carrier; it does not claim that a full Belnap implication calculus or standard ATMS is implemented.

For each polarity return independently:

```text
{ witness: present | not_found,
  evaluation: complete | incomplete,
  evidence_qualification,
  authorized_snapshot_handle,
  freshness,
  source_availability,
  dependency_coverage: registered_only }
```

`not_found + incomplete` is indeterminate, not a completed “unknown” verdict. `present + incomplete` proves existence of the returned checked witness, but cannot claim no contrary evidence, enumerate all alternatives, or certify complete impact. Both present witnesses establish a conflict even if enumeration is incomplete. A complete search over the registered authorized graph is still not a complete account of the world. A view must say its policy and declared scope; it must not reveal whether hidden sources exist.

The positive and negative channels are independent. With `A+`, `A-`, and an admitted sufficient-support rule `A+ -> B+`, B has that qualified positive support even while A is conflicted. There is no automatic B-, no explosion, and no silent discarding of A's conflict through ATMS nogood elimination. Whether an application may act on conflicted premises belongs to a separate consumer policy; the memory record does not authorize the action.

Internal global memory sequences, source cuts, dirty generations and retention epochs stay protected. A visible counter, content digest, cursor or token equality can disclose a hidden append even when its content is opaque. Public view, change and admission receipts therefore reveal only metadata expressly admitted for that recipient. Snapshot handles bind to internal cuts without exposing them; their issuance, equality, length and error behavior must be independent of hidden-only mutations. One candidate contract mints fixed-length random handles per request regardless of activity, with stable internal binding for pagination; a visible `no_change` result depends only on the authorized projection. This is a proposal requiring conformance, not a claim that opacity alone proves non-disclosure. Authorized source revisions remain exact internally and are exposed only where separately allowed.

Access is checked before deriving visible statuses, not only before rendering text. A claim's hidden supporting/conflicting source must not leak through status bits, hit counts, explanation paths or update notifications. The same visible inputs and policy should yield the same visible output irrespective of hidden records. Cross-space sharing requires an admitted, separately authorized derivative, not a proof path that tunnels through inaccessible content.

The tested non-disclosure relation fixes the authorized projection, policy, caller's declared resource envelope and any explicitly policy-authorized public availability state. Logical query/evaluation accounting counts authorized work only; hidden candidates scanned before filtering cannot consume that logical budget. Admission, storage and work reservations must follow the disclosure boundary, which may be narrower than a knowledge-space when audiences see different subsets. The later service profile must specify how it preserves those envelopes or which limited aggregate degradation it intentionally discloses. A public availability transition is an authorized information release, not proof of zero leakage: its policy must be established before the test by the existing owner, must not expose hidden-space attribution, and cannot be invented after observing a failure. Under the same admitted envelope and availability state, hidden workload must not alter success, refusal or completeness. A coarse opaque error is not sufficient. General timing, scheduling and denial-of-service isolation are not claimed; wall-time cutoffs and shared-pool exhaustion must still follow this declared availability contract, and `unavailable` never becomes negative evidence.

## 5. Why bounded evaluation is sufficient initially

For C with sufficient-support rules `(A AND B) -> C` and `(D AND E) -> C`, withdrawing B disables only the first support path. The second still supports C. This needs a stored AND/OR dependency DAG and reverse index, not enumeration of all minimal assumption environments.

For the family `C = AND_i(A_i OR B_i)`, an ATMS-style explicit list can require `2^n` distinct minimal assumption sets. The factored DAG has O(n) gates and can answer whether a witness exists by a topological pass. This is our counterexample, not a benchmark claim. For a fixed snapshot and already admitted DAG, a full Boolean pass is O(V+E); source resolution, policy checks, indexing, graph growth and proof enumeration are additional costs.

A complete fixed-snapshot evaluation may therefore be cheap even when complete explanation enumeration is large. These must have distinct limits. An explanation can be truncated while the existence calculation is complete. Conversely, truncating the rule/dependency calculation must produce `incomplete`; it cannot reuse an old label as current.

Write limits bound graph size, fan-in and source payload size with explicit rejection receipts. Read limits separately bound source-resolution work, rule visits, elapsed time and rendered explanations. Exact numerical limits are deployment settings included in receipts, not invented universal performance promises. A cutoff has a reason code and resumable snapshot-bound cursor where feasible.

Invalidation has a deterministic dirty boundary: when an accepted revision changes an input, affected registered dependents are marked dirty at that memory sequence before old results can be served as fresh. Recompute may run later. Until complete, the response is stale/incomplete at the new watermark or a clearly labelled historical response at the old watermark. A reverse-dependency traversal cutoff cannot mark its unknown remainder clean.

## 6. Revision, time and erasure

- **Withdraw:** deactivate one evidence relation or registered rationale from the named transaction point; do not create opposite evidence.
- **Replace:** add an explicitly authorized link from the new object to the exact old object. Preserve alternative, independent supports. Owner decisions require the external authority's supersession evidence.
- **Correct:** describe a backdated valid-time correction while preserving the later learned-at sequence. Never rewrite what the service knew at an earlier sequence.
- **Availability:** identify that a source is now unavailable or erased. No readable-byte reconstruction is promised after lawful erasure; current access/retention checks still apply to historical queries.

A verification assessment is immutable and scoped. “Signature passed yesterday over digest D” can remain historically recorded, subject to retention, while current resolution or current authorization is unavailable. Neither implies “the claim is true today.” An expired test result remains a historical test result; its exact artifact/contract/policy/environment pins cannot be copied onto a changed candidate.

The managed profile requires explicit source admission and independent read/use/retain/forward checks; a read permission does not grant persistence or model-provider forwarding. A memory store owns a manifest of its retained payloads and derivatives: excerpts, summaries, embeddings, search indexes, explanation caches, exported view payloads and applicable backups. A semantic justification graph is not an erasure graph: paraphrases and tokens may be retained without a logical dependency edge. An erasure job must traverse the retention lineage, with tombstones that themselves contain no sensitive content. A hash may be sensitive or guessable and is not automatically safe to retain. The erasure fence is durable before disclosure or derivative commits can proceed; stale in-flight jobs cannot reintroduce erased content. Restore remains closed until erasure/policy completeness is reconciled against evidence outside the restored failure domain. Missing witness or unreachable custody sink yields incomplete erasure, never success. Telemetry, external collectors and provider disclosures are named custody surfaces; unmanaged already-delivered bytes cannot be recalled. These requirements adopt the [erasure-closure finding](../findings/erasure-closure.md).

An audit receipt may preserve approved non-sensitive identifiers and inability to reconstruct a deleted view. Physical deletion legitimately reduces reproducibility; report that loss. Do not claim both complete replay of deleted payloads and complete erasure.

## 7. Source and platform boundaries

For the managed profile, the service is the sole writer of its own memory records and indexes. For documentary M0, the reviewed register has one authorized publication path and the adapter is read-only; the same proposal does not assert OS isolation under the operator account. Board, keeper, session-host, dispatcher and trust components remain sole writers/authorities of their records. An extractor may submit a claim, not alter grants or install instructions. Source refs contain namespace, exact revision/watermark, selector and digest where permissible; missing/unavailable source is a typed state, not a dangling edge ignored by recall.

A view is an audience/purpose-bound projection internally pinned to memory and source watermarks, policy/profile version, item provenance, availability and qualification. Its external representation follows the metadata disclosure contract in section 4. Independent source frontiers are a vector of cuts, not an atomic platform-wide snapshot. For M0 it is explicitly pulled tool data. `swarm-handoff/2` has no arbitrary memory/KnowledgeView reference kind: no field is added and no seed injection is claimed; later host integration needs actual protected tool-output custody or an owned versioned schema extension. The session host still delivers input; Curator still determines approved configuration; board goals and acceptance remain external. Delivered content is not a registered reasoning dependency unless explicitly asserted as one. Delivery receipts must not pretend to know what the model internally used.

Dream/rehearsal mode is an explicit evidence context. A simulated approval or test outcome cannot satisfy a real-execution predicate. An authorized summary of a rehearsal may support a proposition about the rehearsal; it cannot become the underlying real outcome. This follows the platform book's `10-sny.md`, not an assumption that “dreams” merely means memory consolidation.

Generic protocol transports (HTTP, CLI, MCP, optional A2A exchange) do not change these semantics. `changes` reports memory facts; it does not enqueue work, wake a session, grant access, accept a result or mutate a source journal. Verifiers are admitted producers of assessments, not a runtime mechanism for executing arbitrary checks under memory's identity.

## 8. Minimal API shape

```text
admit(proposal, idempotency_key) -> receipt | refusal
revise(typed_revision, idempotency_key) -> receipt | refusal
recall(query, budget) -> view
explain(claim_revision, query, budget) -> witness_graph + completeness
changes(cursor, audience, budget) -> admitted_change_refs + cursor
```

Assessment and challenge proposals use `admit`; the kind determines authorization. Same authenticated writer, space and idempotency key with identical canonical input yields the same receipt; receipts do not expose a global sequence by default; different input yields an idempotency conflict. Admission and index-dirty marking are one durable transaction. No receipt means no assumed commit; clients can resolve an uncertain attempt by its idempotency identity.

There is no blanket `verify(claimId)` that silently chooses assurance meaning. A request can name the check class, exact subject pins and permitted executor; any resulting assessment retains that scope. Running the check is outside the memory kernel.

M0 can implement these operations with just explicit claims/source links/revisions. It returns “rule evaluation unsupported” rather than pretending an unimplemented evaluator succeeded. Transport adapters may use existing base names such as `observe` and `propose`, provided their exact admission contract is preserved.

## 9. Conformance vectors required before an implementation claim

Each vector needs a closed initial snapshot, admitted operations, authorized query, exact expected output or refusal, and forbidden outcome. The following are writable specifications; none was executed during this research pass.

| ID | Input/change | Expected | Forbidden |
|---|---|---|---|
| S01 | No roots for A | neither, complete within registered graph | A- from absence |
| S02 | A+ and A- in same scope/time | both; preserve both witnesses | deleting either side automatically |
| S03 | S02 plus A+ -> B+ | B+ with conflicted-premise provenance | B- or arbitrary C without an explicit rule |
| S04 | C=(A AND B) OR (D AND E); withdraw B | C+ via D/E | unsupported C because first explanation was removed |
| S05 | C=A AND B; withdraw sole B+ | C positive witness not found | C- or revoked owner decision |
| S06 | Cut off evaluation before D/E in S04 | incomplete, authorized reason and protected snapshot binding | complete unsupported C or exposed global cut |
| S07 | Complete support evaluation, render only one of many proofs | support complete; explanation enumeration partial | conflating explanation cap with evaluation failure |
| S08 | A+ -> B+, B+ -> A+ | cycle refusal, atomic no partial admission | self-supporting A/B |
| S09 | Valid-from t1, learned at seq20; ask as-known seq19 | correction absent; earlier view preserved | backdating transaction knowledge |
| S10 | Intervals [t1,t2), [t2,t3) with opposing values | no temporal overlap at t2 for first | conflict from non-overlapping facts |
| S11 | Prior passing assessment for artifact D; query D2 | inapplicable assessment | copied verification status |
| S12 | Evidence erased after a retained claim | explicit current unavailability and retention policy result | reconstructed erased excerpt or automatic opposite claim |
| S13 | Same visible graph, different hidden opposing root | identical allowed output | status/count/timing class that reveals the hidden root |
| S14 | Same idempotency identity/input twice, then changed input | one record/receipt, then conflict | duplicated observation or overwritten proposal |
| S15 | Simulated test pass requested as real outcome | excluded/inapplicable for real claim | dream evidence qualifies real acceptance |
| S16 | LLM proposes `checked_entailment` with no deterministic assessment | refusal/downgrade to explicitly labelled proposal by contract | formal proof qualification from proposer label |
| S17 | Source decision replaced externally, old dependent query before recompute | dirty/stale or completed recompute at new protected cut | old supported answer labelled current or exposed global cut |
| S18 | Unknown predicate/profile version or field | typed refusal | silently interpreting it as closest known field |
| S19 | Memory correction targets a board decision | memory challenge/rationale only | board decision or task status changed |
| S20 | Quotation paraphrased into an excerpt/embedding without a support edge, then erased | derivative found through retention lineage | survives because logical graph had no edge |
| S21 | `(A AND B) -> C`, `(D AND E) -> C`, with A- and D- only | no C- without a separate explicit rule | completing the rules to a biconditional and deriving C- |
| S22 | Source quote or declared adoption rationale about p | attribution or review dependency only | sufficient support for p without the separately qualified assessment/rule |
| S23 | Authenticated remote board mirror with unverified ledger origin | submitter-attributed claim only | authoritative source-ledger event from mirror provenance alone |
| S24 | Add/revise/erase only hidden records between identical allowed queries | same permitted semantics and handle issuance distribution | global watermark/cursor/digest/dirty/coverage/refusal changes reveal hidden activity |
| S25 | Restore a valid snapshot before an acknowledged erasure | disclosure stays fenced until outside-domain evidence reconciles | old in-snapshot inventory witnesses its own completeness |
| S26 | Extract before erasure and attempt derivative commit afterwards | reject stale commit or rederive from allowed inputs | erased content recreated after completed purge |
| S27 | Hidden workload pressures a shared pool while the authorized projection is unchanged | same result/coverage/refusal under equal admitted resource envelope and public availability state; separately authorized degradation remains explicit | charging hidden work to the logical query budget, retroactive declassification, or treating unavailable as absent evidence |

For S13/S24/S27, compare permitted semantics and declared randomness distributions, normalizing unrelated freshly minted IDs/timestamps by a predeclared rule; do not demand byte identity of random view handles. The normalization may not hide activity-dependent counters, token equality or success/refusal differences. Test both fixed-envelope/availability equivalence and any separately admitted public degradation transition; do not condition on an undeclared state to make a failed pair disappear. Strict timing noninterference is a separate engineering claim from S13's logical projection. The implementation must name which leakage dimensions it tests and must not claim a timing proof from content-output equality alone.

## 10. Evaluation and governance

Separate formal conformance from product usefulness. Formal evaluation fixes the graph, policy, watermarks and source corpus. Measure signed-support correctness, false invalidations, dirty propagation coverage over registered edges, illegal authority effects, stale complete responses, semantic qualification laundering and erasure closure. Zero violations are acceptance criteria on the named corpus, not a universal security proof.

Product evaluation pairs the current documentation workflow against M0 on the same known decision histories. Measure correct decisions recovered, citation precision, obsolete-answer rate, human source opens and time, irrelevant review notifications, bytes retained and eventual erasure results. Record budget cutoffs and failures in denominators; do not drop them to improve accuracy. Random top-k retrieval must not be used as the denominator for complete contrary-evidence search.

Use Curator's separation of normative prose, closed schemas, immutable vectors and independent implementation reports as the governance precedent. Version the semantic profile, canonical bytes and evidence policy separately. Any change that changes a vector outcome requires a reviewed profile change; an implementation bug does not become normative behavior. Transport-schema validity alone is not qualification.

## 11. Comparison boundaries

Typed documents with explicit supersession can implement M0 and are a serious alternative; git is an artifact representation, not automatically a safe multi-agent writer or erasable store. Existing-journal projections avoid a parallel history but cannot reconstruct omitted rationale; write new memory facts through a narrowly scoped admission surface or explicitly decline that capability. A graph product can be a replaceable projection if it preserves the contract; this note makes no unaudited claim about Graphiti or Letta feature support.

Full ATMS becomes justified only when a measured use case needs queries over alternative hypothetical assumption environments. At that point specify nogoods, environment identity, default rules, provenance semantics and cutoff guarantees in an optional profile. Until then, the small support DAG covers the base's concrete alternative-rationale example with less semantic and computational commitment.
