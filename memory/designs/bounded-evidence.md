# Bounded evidence memory

Owner: astra-01 (five 1, ivmbp). Status: proposed, round 1, 2026-10-14. Room: `alt-bounded-evidence`. This is an RFC direction, not a claim of implemented or activated contracts. The companion [verdict](../verdicts/astra-01.md) holds the source inventory, scoring and open questions.

## Decision proposed

Keep the sketch's independent knowledge service and proof-carrying claims. Reduce its first release to an optional service that records knowledge proposals, explicit revisions and links to admitted evidence. Its only authoritative state is **what this memory service has recorded and how it derived its own views**. It cannot become the authority for the events those views describe.

The named initial use case is architectural decision continuity: explain why ordinary agent retirement deletes the home, identify which registered assumptions still depend on the superseded archive-home rule, and give the next researcher the source and the uncertainty. This works from approved versioned documents on one host without the future bridge, identity keeper, distributed protocol or machine base context.

## Kernel

Five record shapes are sufficient. Names below are proposed local vocabulary, not allocated Swarma wire names.

1. **Assertion:** immutable ID and version, schema-qualified proposition, perspective, valid-time interval, recorded sequence/time. The submitting principal comes from authenticated intake, not a client `author` field. A claim that a board accepted a result remains a claim about an external decision.
2. **Source reference:** owning system and kind, source object/event ID, exact revision or committed sequence, digest where available, locator governed by the source resolver, provenance class and availability. Retaining an excerpt requires a separate admission and retention decision; a reference grants no access to its target.
3. **Support:** explicit signed polarity, target assertion version, source reference or registered premise versions, rule ID and rule version, and the limits of the claimed support. Source integrity, issuer attribution, test outcome and semantic judgement remain different verification kinds. An LLM assessment is recorded as such.
4. **Revision:** a new record naming an old assertion/support version and the proposed relationship (`supersedes`, `withdraws`, `challenges`). It never rewrites the old bytes or the source authority's history. Any assertion about an adopted decision must resolve to the deciding authority's receipt, not the memory submitter's status field.
5. **View:** a derived, immutable, bounded response for a named authenticated recipient and purpose at a named memory journal cut, with each source's independently observed cut. Views are data, not executable instructions or authorizations.

`Principal` and `KnowledgeSpace` become foreign identity references and policy scopes, not parallel registries. `Observation` becomes the receipt of an admitted source reference, not automatic transcript capture. Project, task, decision, user preference, skill suggestion and agent model remain domain schemas. There is no first-release `approve`, `accept-task`, `set-goal`, `grant`, `start`, `wake` or `run-test` operation.

### Honest evaluation

The sketch's two evidence bits can remain, but they describe admissible support and refutation **under a named policy, perspective and time cut**, not a proof of world truth. Evaluation completeness is a separate field. Missing source bytes, incomplete ingestion, resource exhaustion and an inaccessible source must not become negative evidence.

First release: explicit source links and supersession, with no inference beyond registered rules. Next slice: finite AND premise lists, multiple alternative justifications, reverse edges and bounded affected-closure reevaluation. No negation-as-failure, inferred global consistency, or arbitrary rule execution. Cycles and resource caps need a published rule; until one exists, reject cyclic rules and report incomplete evaluation on exhaustion. A surviving alternative support keeps the conclusion supported; losing one support is not automatic decision repeal. Semantic dependency suggestions remain proposals until registered.

## Stores and authority

| Store or fact | Sole owning writer/authority | Memory access and limit |
| --- | --- | --- |
| Account generation, retirement, applied machine boundaries | User manager and its protected ledger | Versioned source evidence only; an old readable record is not a current permission |
| Credential bindings, grants, revocations, leases | Existing broker/trust owners | No secret intake or parallel rights registry; current authorization is checked by the effecting service |
| Admission, allocation, execution, cleanup receipts | Dispatcher | Refer to the canonical record, not a board mirror or an agent's report of it |
| Session logs, delivery/application receipts, input fences, native context | Session host module | Read-only admitted export/resolution; no shared writable files, stdin, native handles or restoration authority |
| Goals, task lifecycle, accepted candidate and board activity | Board or its documented domain ledger | Read committed revisions; changes and acceptance remain with that owner |
| Obligation custody, deadlines and escalation state | Keeper kernel ledger (target design) | Evidence references; no second obligation ledger or deadline scheduler |
| Room events and transport receipts | a2a/bridge transport | Evidence of sender/content/delivery only within the transport's actual guarantees; an answer is not necessarily fulfilled work |
| Launch profile, skills, MCP and instruction channels | Curator's approved configuration and existing launch construction site | Knowledge never edits an overlay, skill, profile, plan or configuration |
| Assertion/support/revision receipts and source import cursors | One memory service writer | Own knowledge history only, under an unprivileged service boundary |
| Search/reverse-dependency indexes and cached views | Same memory service | Rebuildable projections, never independent truth or authorization stores |

Do not collapse distinct meanings of keeper: the obligation kernel, the future identity key keeper, and the credential broker have different jobs and maturity. Do not call the existing a2a CLI implementation the standardized A2A protocol or assume the draft Waggle design is deployed.

The platform adapter authenticates using admitted platform identities and policy. The standalone profile can authenticate one local operator and use a protected local service store; it must describe this weaker isolation honestly. In Swarma, agents never open memory's database or mutation journal directly. Knowledge-space policy is enforced by memory but obtains its authority from the deployment's existing policy owner. It cannot mint grants for other services.

## APIs and effects

These are semantic operations; transport and exact schema need an RFC and conformance vectors. Start with one ordinary local API/CLI and an optional MCP adapter, not three SDK implementations.

| Operation | Permitted result | Forbidden implicit effect |
| --- | --- | --- |
| `observe(source_ref, admission_ref, idempotency_key)` | Source intake receipt and provenance/availability | Crawl arbitrary locators, copy transcripts, assert world truth |
| `propose(assertion, support_refs, idempotency_key)` | Versioned recorded proposal | Mark a board decision accepted or impersonate the source |
| `revise(target_version, relation, evidence_refs, idempotency_key)` | Recorded proposed revision | Edit source facts or silently replace prior versions |
| `recall(query, purpose, bounds, cut?)` | Authorized bounded View, or explicit refusal/incompleteness | Discover hidden spaces via counts, status, identifiers or explanations |
| `explain(assertion_version, bounds)` | Same-policy filtered provenance graph with coverage | Dereference sources without current rights, or expose hidden premise existence |
| `verify(evidence_ref, verifier_kind)` | Bounded deterministic inspection of admitted existing evidence | Execute candidate code, launch a test, make model calls or gain network privileges |
| `changes(cursor, bounds)` | Durable advisory changes in memory's own history | Enqueue session input, wake work, start review, alter task/goal/custody state |

Writes compare an idempotency key scoped to authenticated producer with the complete canonical request digest: exact retry returns the existing receipt; different intent under one key is a conflict. The journal, cursor and index transition must commit atomically or expose an explicit incomplete projection. Source-owned sequence determines import order, not wall-clock timestamps. A vector of independent source cuts is **not** a globally atomic platform snapshot. Absence of a current source read is `unavailable`/incomplete, not absent history.

A test report is checked against its exact candidate, contract/policy and environment. If new execution is needed, memory returns that need as data. The existing authorized client and R-VERIFY lane decide and perform the work. Proof plugins are not arbitrary agent-supplied programs running under the memory service identity.

## Context seam

Maintain three distinct inputs: the authoritative current task/goal, the host's continuation package, and optional knowledge data. A memory query normally reaches the agent as an explicit tool result. Rendering must preserve each item's original author, source authority and `data` classification through summary, expansion, caching, reimport and handoff. The service signature authenticates its envelope, not an authority upgrade for enclosed text.

Do not add memory content as a lower-weight Curator instruction overlay: weights only order chapters. Do not put it in CIP-0013's proposed machine base. Do not have memory or the session host spell harness flags: Decision 0019 gives that construction site to agents-management.

`swarm-handoff/2` has a closed schema. An implementation cannot silently add `knowledge_view` or a new reference kind. In the first slice there is no automatic seed injection. A later host adapter can retain a recall result as the existing protected tool-output/journal evidence, subject to the actual projection rules, or propose an explicit versioned handoff extension through its owner. It must not use that wrapper to copy arbitrary memory text into a user turn. A knowledge view admitted for task A is not automatically admissible for task B or a restored execution.

A view records recipient, purpose, source and policy revisions, source cuts, completeness, selected assertion versions, disclosure constraints and optional expiry. Before source resolution or a new consumer delivery, current rights are checked. Bytes already delivered to an external model cannot be recalled. A session-host delivery receipt proves delivery only; asserting a premise-use dependency requires a separately recorded declaration or measured evidence, with inferred use labelled as inference.

Advisory change polling is sufficient for the first slice. A later authorized client may submit an ordinary notification through the existing bridge/host path; memory has no wake, goal or control capability. Explicit park, stop and revoked rights remain effective. Stop, revocation, recovery and acceptance never wait for memory, inference or consolidation. A policy that requires fresh evidence can refuse that one business action while control operations continue.

## Retention and derived information

Admit only named source classes with an explicit retention purpose. The initial corpus excludes personal memory, raw conversations, native handles, credentials and arbitrary tool output. Type validity, a hash, a signature, a merged Git commit or an LLM filter is not evidence of secret freedom.

Separate logical history from payload retention. Sensitive/free-form claim and excerpt bytes live in erasable payload objects, not in an immortal audit log. Structural receipts use opaque IDs and remain access-controlled; identifiers and digests can themselves disclose information. Every excerpt, summary, embedding, index, cached view, export and registered dependency has a recorded lineage for disposition. Authorized erasure blocks reads/rebuilds before deletion, covers retained replicas/backups under the declared policy, and produces a truthful incomplete/complete disposition result. Restoration cannot silently revive erased material. Missing evidence is reported; a surviving attestation proves only the proposition it actually signed.

This contract requires a dedicated security design before admitting sensitive data. It does not claim that in-process provenance labels defeat semantic prompt injection or that forwarding restrictions can retract already disclosed bytes. The security seats' independent erasure and view-inference findings must be reconciled before an RFC is called complete.

## First-slice acceptance vectors and value

No prototype or build is authorized in this research pass. These are proposed tests for subsequent implementation.

| Vector | Expected result |
| --- | --- |
| Read old archive-home rule, then adopted delete-home revision | Both remain traceable; present view cites the new decision and flags registered stale dependents |
| Decision text without accepting authority receipt | Documentary/agent claim; never invent adopted status |
| Remote board activity mirror without canonical run evidence | Attributed report, not authoritative completion |
| An imperative hidden in signed source text | Data frame throughout recall, summarization and handoff; no configuration/control effect |
| Query task B with task A's view/reference | Reauthorization; no reuse from an old audience grant |
| Revoke read access; then explain/changes/count query | No hidden identifiers, statuses, counts or premise disclosure |
| Delete source/excerpt and rebuild indexes/restore | No resurrection; affected verification and completeness report the gap |
| Duplicate import with same key; changed payload under same key | One receipt for the exact retry; conflict for changed intent |
| Source unavailable or ingestion gap | Explicit incomplete knowledge; no empty-set proof |
| One alternative justification remains valid | No false loss of support or automatic decision cancellation |
| Dependency cap exhausted | Incomplete result; never unsupported merely because traversal stopped |
| Memory unavailable while operator stops a session | Stop/park/revocation path proceeds under its existing owners |
| `verify` is asked to test a supplied repository | Returns missing evidence/request data; launches nothing locally |

Use a manually labelled corpus of 10–30 architectural decisions and explicit source revisions, including archive-home/delete-home. Compare against plain search and typed versioned documents, under the same read access and question set. Measure correct current decision + exact source, stale decision rate, evidence precision, missed registered dependents, false review suggestions, answer time and repeated source-reading effort. Report sample size and uncertainty; no numeric win is claimed yet. Promote automatic extraction, richer inference or another graph backend only if it improves this comparison without weakening the boundary vectors.

## Deferred

Full ATMS, general Datalog/theorem proving, automatic transcript intake, personal preferences, procedural-memory activation, dream scheduling, automatic review jobs, agent reputation used for admission, federation, consensus, blockchain anchoring, Graphiti adoption, and multi-host operation. Dreams produce rehearsal evidence in their own domain; they cannot satisfy real acceptance. A future graph engine is a projection implementation, not another authority.
