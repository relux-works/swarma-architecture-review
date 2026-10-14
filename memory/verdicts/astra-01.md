# astra-01 verdict: platform fit and authority boundaries

Seat: astra-01, five 1, ivmbp. Status: round-3 comparison and exact-revision agreement, 2026-10-14. No peer verdict was used to form the preserved initial scores. Work is research-only; no source repositories, board state, runtime configuration or platform contracts were modified. Recommended candidate: [bounded evidence memory](../designs/bounded-evidence.md), room `alt-bounded-evidence`.

## Position

The base sketch is directionally compatible with Swarma, **especially its second half**, which already rejects a global source-of-truth log, secret hoarding, automatic instruction promotion and hidden orchestration. Those are strengths, not findings against it. Its weakness is an unclosed integration contract: a generic `KnowledgeView`, `verify` and `Notify` do not yet tell a consumer how to preserve authority, authorization, source cuts and execution boundaries.

I recommend the smallest version of the base that has independent value: a reviewed documentary register first, with exact references to existing domain records, explicit supersession, bounded registered dependencies and data-only pull results. No named documentary-P0 requirement needs a new daemon. An isolated single-writer service is the target for protected private/multi-proposer operation, not a prerequisite for the experiment. Neither profile owns grants, launches, goals, acceptance, custody deadlines, configuration or session input. The full recommendation, stores, APIs, context seam and acceptance vectors are in the linked design.

## Independent round-1 rubric (preserved)

Scores assess documented designs, not measured implementations. A 2 means the criterion is explicitly met at the evaluated design level; no score is a product qualification. Every column must also satisfy no 0 in R3/R4/R6. Initial alternatives are mine; named peers may supersede them with stronger designs.

| Criterion | Base, both halves | Bounded evidence service | Typed documents + existing decisions | Pure source-journal query, no knowledge log |
| --- | ---: | ---: | ---: | ---: |
| R1 Minimal kernel | 1 | 2 | 2 | 2 |
| R2 Reuse | 2 | 2 | 2 | 2 |
| R3 Authority separation | 2 | 2 | 2 | 2 |
| R4 Secrets and retention | 1 | 1 | 1 | 1 |
| R5 Runtime independence | 2 | 2 | 2 | 2 |
| R6 Honest epistemics | 2 | 2 | 1 | 1 |
| R7 Specifiability/testability | 1 | 1 | 1 | 1 |
| R8 Incremental value | 2 | 2 | 2 | 1 |
| **Total /16** | **13** | **14** | **13** | **12** |

### Evidence for each row

- **R1:** Base part 1 §§2–5 introduces eight primitives, full ATMS ambitions and multiple verifier families without a closed kernel. The bounded design reduces identities/scopes to external references and has five finite record shapes, with graph engines optional. Documents and source-query alternatives have smaller kernels still; their limitation appears in R6/R8 rather than an invented complexity penalty.
- **R2:** Base part 2 §3 explicitly keeps a knowledge journal plus source references. All serious alternatives retain source ownership. The source table below shows why a global journal would be a regression: SH §1/§3.2, DP §1.1, board activity §Derived Control-Plane Ledger Mirror and keeper book ch.11 assign different authorities.
- **R3:** The base explicitly prohibits memory grants, wake/input, automatic acceptance and instruction promotion in part 2 §§4,6. Its omissions are a contract-closing need, not evidence it intentionally grants those powers. Every scored alternative retains this prohibition. Bounded memory additionally binds actual consumers, operations and forbidden effects to Handoff §§1–5, Curator D0019 and SH §§3.4–3.8.
- **R4:** Base part 2 §6 correctly demands admitted sources and derived deletion, but the first-half P0–P3 plan postpones access control and has no erase/restore completion contract. Bounded memory improves admission and lineage, but remains 1 until security peers close erasure, authorized explanations and restore. Git history makes erasure difficult for the document baseline; source-only query avoids copies but still needs policy for responses, caches, logs and disclosures. No design gets a free 2 from saying "references only".
- **R5:** Base MCP plus HTTP/SDK are adapters. The bounded core, plain documents and source query can be consumed independently of a harness. None requires Curator or host hooks for its first use.
- **R6:** Base expressly distinguishes integrity, epistemics and decisions, bitemporal history, alternatives and registered dependencies (part 1 §§3–5; part 2 §§4–5). Bounded memory adds observed-source cuts, evaluation completeness and source-authority classification. Bare document/query alternatives have provenance but need a closed conflict/revision convention before matching those guarantees.
- **R7:** Base names metrics but supplies no closed grammar, replay/erasure vectors or governance for adapters. Bounded memory has concrete negative vectors and owners, but exact schema, policy vocabularies and evaluator semantics are not frozen; it earns 1, not a claim of conformance. The alternate document/query formats are similarly only design sketches here.
- **R8:** Base's part 2 decision-drift use case is already useful, as is bounded evidence memory or typed documents. Pure query over source journals cannot by itself retain a new cross-source interpretation, a challenge or a registered dependency unless it stores those somewhere else; it gives retrieval value but misses the named continuity loop.

At this freeze the mission's proof of optimality was not met. The bounded service led my limited comparison by one point. A well-specified document design could tie or win; the post-freeze reassessment below records that challenge without rewriting the independent evidence.

## Round-2 reassessment and honest product boundary

astra-04's independently frozen verdict and its question `$CxWQDD5684oRqeMZqeg0LwNNMnIq1wGZ9OLGQMfuPKA` improve the typed-document candidate: it has a closed assertion/amendment convention, current authorization, explicit source cuts and the same data-only contract. My original R6=1 described a bare document convention, not this stronger design. wonder-01's `$dq4OKFcMgkU6jF7cGJ8fjiVxlRs_ojdlEhhcCOLuPPE` correctly challenges a daemon as an unearned first-slice prerequisite. I accept both; the full design now separates the documentary experiment from protected service operation.

astra-02/05's erasure and view-inference analysis supplies the missing service contract: independent read/use/retain/forward predicates; view-relative status; separate byte/custody lineage; publication fencing; per-boundary purge receipts; restore coverage outside the restored failure domain. These are now explicit in the design, so its service-profile R4 rises at the **design-contract** level. Actual qualification remains unperformed. The Git documentary profile stays R4=1 for general memory: its allowed corpus and retention promise are narrower, and arbitrary clones are not controlled erasure stores.

| Criterion | Base, unchanged | Bounded service, revised | Governed typed register, revised | Source-only query, unchanged |
| --- | ---: | ---: | ---: | ---: |
| R1 | 1 | 2 | 2 | 2 |
| R2 | 2 | 2 | 2 | 2 |
| R3 | 2 | 2 | 2 | 2 |
| R4 | 1 | 2 | 1 | 1 |
| R5 | 2 | 2 | 2 | 2 |
| R6 | 2 | 2 | 2 | 1 |
| R7 | 1 | 1 | 1 | 1 |
| R8 | 2 | 2 | 2 | 1 |
| **Total /16** | **13** | **15** | **14** | **12** |

Unchanged scores retain their row evidence above. R6 for the revised register follows astra-04's exact-source/assertion/amendment rules and data-only/current-access semantics, not any intrinsic power of Git. R4 for the service is conditional on the published retention/disclosure protocol; R7 remains 1 until a closed profile and conformance package is published. The service is the highest-scoring general-memory target among these candidates. The lower-surface document experiment is still the recommended first step because its narrow admitted use case requires neither sensitive storage nor autonomous mutation. This is a stated scope/cost tie-break, not a claim Git provides the service's security boundary.

The `56d18ee` service score of 15 was premature: astra-05 identified an unresolved public-watermark ambiguity, and astra-04/03 subsequently accepted the stricter artifact reading of 14. I accept that correction. The assembled design at signed `0ce009435206f31f387efd207dc3f2662e66e4d9` removes the ambiguity, adopts semantic companion `476ec36`, and adds the protected-service admission gate. Its SHA-256 is `9c8f63fd8aad3d44081b93225f727e504468297cadc21ab1d0973903d28c0599`; the companion is `adde0314375f1950a817962c1c513070ef86aa3b01f1fecb14e86fe9339fd3ba`.

After reading those exact artifacts, astra-04 (five 2) confirmed 15/14 in `$ZHOqMsgPsMRvYmQ7oOiijzHHx4oGmE-89-RrG36iArE`; astra-05 independently confirmed them in `$W6Z420vc49y3Eflx2Xn5ti_MQNDmd58lKsVT549kVVA`; wonder-03 confirmed them from the attachment in `$ZeuRdPyKP2twOa9nqwmn_a9KVVn1losLGgFDyxoYeMg`. astra-03 (five 1) confirmed the same exact vectors in `$p6gek454MWjxXasqM_alguzPwr9bffWW2c8AiyLIgC8`. Every row matches mine. The mission's two-seat/two-five proof criterion is met for the corrected contract. A cross-host proof is not yet claimed. Neither this agreement nor 26 proposed vectors establishes executed qualification, an empirical winner or a unique global optimum.

The later shared-budget counterexample from astra-05 (`$o7sd2ib0EzNRlJeGf19MijoAiudZdGw678GfcHmG_u4`) refines the tested scope. Companion `9bafff829e9233b5510ef827ca79a6707d69ae64`, SHA-256 `62ae18cbec7c4be25764f8da0e8084d3b434ac224cc121f09b2304f97ce7aafd`, adds S27 and authorization-relative logical accounting. I read its full delta, verified its signature and incorporated the same scope into the assembled design: pair tests fix the admitted resource envelope and previously authorized availability state; hidden work cannot be charged to the logical query; coarse public degradation requires the existing owner's advance policy and cannot be invented after failure. This is not automatic declassification, a denial-of-service guarantee or a P0 dependency. The old exact proof pins remain historical evidence; confirmation of this assembled refinement is tracked separately. My profile scores remain 15/14.

## Full alternative-artifact comparison

The [comparison note](../notes/astra-01-comparison.md) records attachment hashes, per-row evidence, primary-source checks and the existing platform-memory disposition. These scores include the authors' explicit delivery, custody and semantic amendments; the obsolete body text is not silently endorsed.

| Serious alternative and evaluated profile | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| JOM/D* documentary, wonder-01 v6 amendments | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 14 |
| ALT-DOC documentary, wonder-03 v3 amendments | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 14 |
| ALT-PROJ, persistable overlay and corrected read model | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 13 |
| COMPILER, corrected delivery/custody claims, briefing core | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 12 |

The strongest document variants tie P-doc: they are authoring/projection choices within one semantic family. PROJ's one-point portability judgement can move without changing the first-slice choice. COMPILER contributes a useful promotion/delivery discipline, but cannot alone preserve the declared dependency history required by the named use case. I do not penalize documents for lacking a daemon or give a backend an authority guarantee from its name. Graphiti remains a replaceable projection candidate, supported by the scoped pinned-code audit; native MemFS auto-activation is incompatible with the data-only boundary, while its document shape can be reused under different governance. No whole product is declared universally unsuitable from those limited observations.

## Source evidence and maturity

Read-only clone revisions observed 2026-10-14; files below were read from these local clones. Section references are stable within the listed revisions. A book paraphrase never upgrades a proposed mechanism into shipping behavior. The mission's source preference is module specs over book text when they differ.

| ID | Repository revision | Paths/sections used | What it establishes |
| --- | --- | --- | --- |
| W | wiki `94aebceca3af6a904b73644fb973e201762af8e2` | `book/swarma/ru/02-sistema-celikom.md`; `07-put-soobscheniya.md`; `16-postskriptum.md` | One writer and typed APIs; bridge admission vs session effects; runtime/distributed protocol/substrate are different maturity levels |
| A | swarm-platform-architecture `567b07701bdf32cdebc516e38e6f0321fc5253a0` | `vision/contracts/handoff-package.md` §§1–5; `goals.md` §§1–4 | Recipient-specific high-watermark projection, closed allowlist, original item provenance, reauthorization, authoritative goal revisions; contract drafts, no activation claim |
| SH | swarma-session-host `255523d43129538b7e7064a0dbfc0b06713bb7e2` | `spec/session-host.md` §§1,2.2–2.3,3.1–3.8 | Host owns logs/receipts/input, dispatcher execution/cleanup; machine-local context policy is independent of board facts; explicit stops stay stopped; D-GOALS; SH1 vs gated SH2+; private state, socket/peer identity and service-egress qualification |
| DP | swarma-dispatcher `b719e2307f5f4d6284abbd1ba60c42330f2d6ae8` | `spec/dispatcher.md` §1 and §1.1; revisions R-TRANSFER/R-VERIFY | Dispatcher owns execution records, not plan composition or board acceptance; draft v0.14 explicitly says nothing implemented |
| UM | swarma-user-manager `12609a9e05d5013c34416e1a0332fe5c28c4bcd5` | `spec/helper.md` §§4.4.1,8.1 | Ordinary retirement deletes the home; only closed service-generated metadata survives under that lane; workspace-export custody is separately authorized; account removal is not identity revocation; other non-root services need installer/operator-owned rows before v1 enforced readiness |
| CB | swarma-credential-broker `ec7fb3d0670449b074521d51f3e03b59f0142a69` | `spec/broker.md` §§3,4.1–4.3,6.4 | Kernel peer identity plus generation, broker grant/lease authority; caller keys differ from future keeper identity keys; no memory-side identity shortcut; acknowledged revocation and restore completeness need evidence outside the restored failure domain |
| C | curator-spec `eb1f08c6c66cedc52d9e09553fb791367f334704` | `protocol/environments.md` §6; decisions `0019-fragment-consumers-and-one-construction-site.md` §§1–2; `0021-sessions-enter-through-curator-run.md`; `cips/CIP-0013-machine-base-context.md` status/current state; `cips/CIP-0002-project-context-in-managed-launches.md` trust principles | One channel-spelling site, composed plans at host, overlay weights order chapters; machine base proposal is Draft, not a shipped memory context path; untrusted candidate bytes must remain outside discovery roots and acceptance does not admit control context |
| B | skill-project-management `ad68902f74ae55b1cd0445fef58390b42feea3dc` | `docs/activity-mutation-coverage.md` operator guide, Derived Control-Plane Ledger Mirror, Authoring authority; `docs/context-payloads.md` Authorization before provider access | Immutable per-element sequence and correction; source-ledger-before-mirror; remote mirror authoring is only attribution, not prevention; current authorization before materialized context use |
| K | wiki revision W | `book/keeper/ru/09-zhurnal-i-vosstanovlenie.md`; `11-yadro-kipera-i-a2a.md`; `12-kiper-v-platforme.md` | Kernel journal owns obligation state, transport supplies evidence; response != fulfilment; several integration and signature questions remain open |
| P | wiki revision W | `book/ru/09-pamyat.md`; `10-sny.md` | Earlier hierarchical memory/overlay proposal; external facts quarantined; weights do not grant rights; dreams are rehearsal, not real acceptance, and sleep activation needs authority |
| R | a2a-swarm `d283a43c2b7832a7d0e0472151fa0229de7d13b9` | `internal/skill/files/a2a/SKILL.md`; `references/protocol-rules.md`; runtime `a2a --help` | Actual room/tool protocol, identity ownership, untrusted inbox frame and explicit addressed events; no inference that transport receipts authorize acts |
| G | waggle `010b96501ac8777a1a0dc1a083623b9b685fdd0f` | `README.md` Status and Design in brief | Draft signed communication/coordination design; signatures and claims are not deployed integration evidence |

The local source-head inventory and CLI readiness evidence are in `.temp/astra-01-onboarding/`. These contain no credentials. No source clone was pulled or modified. No credential directories were inspected.

## Candidate disposition

1. **Context data can be promoted by an unspecified consumer.** [Peer-confirmed finding](../findings/memory-data-channel.md), room `f-memory-data-channel`. astra-02 confirmed in `$XxrJ2a2afWS6E-CwUzsZUFHSCKohG2BivATAPsKPPB4`; astra-04 confirmed across fives in `$TorX3CcPnhLO7UDztCEB7ZL8CkxNEUHTxii8kc3qMTk`. The finding explicitly distinguishes unchanged external authority gates from model obedience, and preserves the closed handoff grammar.
2. **A source reference needs an authority class.** B says remote derived ledger mirrors can be hand-minted by the same token path and remain attributed. Memory must resolve canonical run evidence before reporting an authoritative outcome. I confirmed astra-06's `f-mirror-origin` in `$F5k5_K05289EcMGd0y6gEMbmwTJPKqn456SU5brFNd0`; the exact primary branch is `pkg/board/query/activity_ledger.go:53–85`, verified unchanged from B's pinned HEAD. astra-06 owns the finding; no duplicate file.
3. **`verify` cannot gain executor authority.** A test-verifier plugin may inspect reports, but fresh tests/candidate execution belong to R-VERIFY, with an authorized client choosing the action. Memory must not become a side door into arbitrary code execution or network fetch.
4. **Platform-wide snapshots need qualified completeness.** Existing stores own independent sequences. A memory watermark plus source cut vector can explain observed state; it cannot promise global serializability or conclude absence from an unavailable source.
5. **Erasure is not epistemic invalidation.** Confirmed astra-02's `f-erasure-closure` in `$-tTXQoCv0Ij3aTd-l5wKpf4LX-85ekLuQyOKmNB3VbY`. A still-supported proposition can retain restricted bytes. Host tool results/transcripts are a different custody boundary and require the owner's disposition evidence; memory cannot promise their erasure from its own receipt.
6. **Opaque metadata can still disclose hidden mutations.** Confirmed astra-02/06's existing `f-view-inference` finding in `$cwdpvj0aPRoiPn__nmDq3EouTlkQyhPGVQo3hE7ScPQ`. A token derived from a global cut leaks through equality even when undecodable. The design and companion now protect global cuts and include admitted-projection semantics, public issuance behavior and paired hidden append/revise/erase vectors.
7. **A service account is not platform admission.** Confirmed astra-04's `f-memory-service-admission` in `$FWnTAnj6ViVInNIOgT_uYGjcK3B3DEwL4_9dZKhH9bg`, from UM §8.1 and SH §3.1. Protected deployment needs its own qualified service row, authenticated socket and private single-writer state. No such new prerequisite is imposed on documentary P0 or an earlier platform slice.

## Smallest change set from the base

1. Keep part 2's module split; replace Principal/Space ownership with platform references and an enforced adapter policy.
2. Make all source intake explicit; retain source-owned records and exact revisions rather than a second platform log. Distinguish transport, derived mirror, source-owned receipt and interpretation.
3. Close the KnowledgeView consumer contract: audience/purpose, source cuts, original provenance, coverage, data-only presentation and current authorization. No memory overlay or new launch composer.
4. Move access, retention, leakage and resource bounds into P0. Keep security-control availability independent of memory. Add a non-model administration path for source admission and erasure.
5. Start with supersession and bounded registered rules; defer full ATMS. Keep incomplete evaluation distinct from unsupported status.
6. Limit `verify` to checking admitted evidence. Changes are advisory data; existing effect owners decide whether to act.
7. Make the decision-drift corpus the first acceptance gate and compare typed documents before choosing Rust, a daemon, Graphiti or a graph database.

## First slice and operator decisions

First slice and measurement are specified in the linked design. Success means the next researcher can answer the current retirement policy, its historical basis and the registered work that needs reconsideration, without rereading whole sessions or inventing present authority. A one-host explicit query suffices; no platform gate waits for it.

Only the operator can choose the first admitted corpus/data sensitivity, the owner of source-admission and erasure policy, the acceptable retention period, and whether the useful measured product should remain a local tool or be operated as a dedicated platform service. A later protected deployment must also choose whether any coarse availability disclosure is permitted, or require stronger resource isolation; researchers do not approve that disclosure. Recommend approved architecture documents only, personal/dream/agent-reputation memory deferred, no automatic promotion to procedural instructions. Exact schema and conformance engineering are technical work, not operator decisions by default.

## Round log

- Round 1: mission and entire base read; identity ensured and room joined; current local sources checked; independent scoring recorded; context-seam candidate and bounded evidence alternative opened. Initial design/verdict signed, signature verified and published as `e8ab519`.
- First adversarial replies: confirmed erasure closure and mirror-origin against primary sources; obtained cross-five context finding confirmation; accepted closed-handoff and documentary-first challenges. Initial score table preserved; revised comparison and design explicitly separate documentary and protected-service profiles. All publication uses signed commits and ordinary non-forced main pushes as the mission directs.
- Round 2 refinement: exact `56d18ee` received cross-five score agreement and a precise residual watermark objection. Accepted the objection, aligned the five stored primitives with astra-03's `476ec36` companion (View is derived; Assessment is explicit), and added the independently confirmed platform-service gate. No new candidate topic or implementation was needed.
- Round 3: signed `0ce0094` and companion `476ec36` received exact-artifact agreement from both fives. Fetched and read both alternative hunters' full designs and applicable amendments; added the comparative evidence note, independently checked the narrow Graphiti deletion method and MemFS activation documentation, and explicitly reconciled platform-book memory/dream ideas. No new architecture finding was needed. R7 remains an RFC/schema/fixture gap, not a request to build during this mission.
- Round 3 scope refinement: accepted astra-05's shared-budget counterexample and astra-03's `9bafff8` companion/S27. Logical budget isolation and explicit availability disclosure scope are now stated without promising physical isolation or changing scores. This refines the existing view-inference finding rather than increasing the finding count.
