# astra-06: semantics before inference machinery

Seat: five 2, semantics and formal core; mirror of astra-03. Status: round 4, awaiting cross-host review or PARK, 2026-10-14. The independent score record was frozen in signed commit `dec1a5b` before any first-five verdict or candidate-topic body was read; subsequent debate is recorded separately below. The base is **both halves** of `memory/inputs/SKETCH.ru.md`, including its own corrections and narrower first slice. This is a research recommendation, not a shipped contract or an implementation result.

**Current recommendation:** publish one storage-independent evidence/view contract; use a reviewed persistable document register and read-only explicit recall for the architecture pilot. Introduce a protected single-writer service only when private material, autonomous proposers or measured load require it. The daemon is not a prerequisite for testing the semantic contract. The initial table remains an independence record; the stronger peer-reviewed alternatives are scored separately below.

## Independent score record

Scores assess the written design, not product maturity. A 2 is a defensible contract direction; no score proves an implementation. R7 remains 1 for my recommendation until its grammar and vectors are agreed and published. Evidence abbreviations resolve below.

| Criterion | Base, both halves | Scoped evidence ledger (SEL) | Typed decision documents (TDD) | Existing-journal projection only (EJP) |
|---|---:|---:|---:|---:|
| R1 Minimal kernel | 1 | 2 | 2 | 2 |
| R2 Reuse | 2 | 2 | 2 | 2 |
| R3 Authority separation | 2 | 2 | 2 | 2 |
| R4 Secrets and retention | 1 | 2 | 1 | 2 |
| R5 Runtime independence | 2 | 2 | 2 | 1 |
| R6 Honest epistemics | 1 | 2 | 1 | 1 |
| R7 Specifiability/testability | 1 | 1 | 1 | 1 |
| R8 Incremental value | 2 | 2 | 2 | 2 |
| **Total /16** | **12** | **15** | **13** | **13** |

At the independent freeze, the recommendation was not yet "proved" under the mission: another five had to score the same specified candidate, not merely agree with its name. The later proof record is below. No global optimality is asserted over designs outside this comparison.

### Evidence for every row

- **R1:** The base lists eight primitives, three projections and an ATMS without closed rules for claim equality, contradiction or truncation (S §§2–4). SEL has three durable record families: assertion, derivation and revision; sources, identities, decision references and verifier observations are typed references or assertion schemas. Spaces and views are API scope and output, not another authority registry. TDD needs documents, explicit replacement and source links. EJP stores only an index and checkpoints. Both alternatives therefore have smaller kernels, though fewer capabilities.
- **R2:** S part 2 §3 already preserves the existing journals; it deserves 2 rather than being scored as a global replacement log. All alternatives retain those owners. SEL writes only admitted interpretations and their revisions; it never owns the event described by an assertion. K, H and B already demonstrate why those distinctions matter.
- **R3:** S part 2 §§4,6,8 explicitly forbids memory-derived rights, input, waking, implicit instruction promotion and safety dependency. SEL, TDD and EJP retain those prohibitions. C remains an opt-in **draft**, not an available instruction-injection interface. All merit 2 as design commitments.
- **R4:** S §§8 and part 2 §6 explicitly require erasure through derivatives; it is not a store-everything design. But its surviving digest suggestion and replay/cached-evidence semantics remain open. SEL admits only named source classes, applies current read/use/retain/forward policy to outputs, prohibits replay from resurrecting erased payloads and purges memory-owned derived copies; unavailable sources cannot support a current reproducibility claim. TDD's replicated Git history complicates erasure. EJP avoids copied payloads but must still erase its derived index; that is part of the scored EJP contract. H §§1,4,6 and S part 2 §6 justify the requirement.
- **R5:** S §6 explicitly offers HTTP/SDK independently of MCP; SEL and TDD can retain that portable contract. EJP's value is coupled to the availability and semantics of the platform journals and adapters, hence 1. This is dependence of the candidate, not a claim that event sourcing inherently requires a vendor.
- **R6:** S separates three status axes, rejects provenance-as-truth, and limits invalidation completeness to registered dependencies. Its remaining gap is how four-valued status and bounded traversal behave on partial evidence. SEL defines context-indexed polarity witnesses and evaluation coverage separately; no missing support implies refutation, no exhausted bound implies absence, no support loss revokes an adopted decision. TDD and EJP as considered here offer honest source links and replacement but no closed account of incomplete evaluation, temporal correction or conflict aggregation. L and A support the distinction; the exact SEL choices are my proposal.
- **R7:** S has metrics and extensible schemas but no closed grammar or conformance vectors. All four lack concrete closed schemas and exact expected-output fixtures, hence 1. SEL's proposed vectors below make the missing publication work concrete, without claiming an executed check.
- **R8:** S part 2 §§5,8 names an immediately useful architecture-decision slice. SEL, TDD and EJP can all answer the same narrow home-retirement decision query without changing platform gates. The base deserves 2; reducing it is a simplification argument, not evidence that its own MVP has no value.

## Formal core

SEL means a source-linked, scoped evidence ledger with a replaceable query projection. It preserves the base's best boundaries and removes the requirement to enumerate ATMS assumption environments.

The three-family decomposition below records my independent SEL proposal. For the shared RFC I now adopt the five stored shapes in the exact common design `0ce0094` and companion `476ec36`: **Assertion, SourceRef, Justification, Assessment, Revision**; View is derived. In particular, an Assessment is a first-class immutable, subject-bound check/reviewer result with rule, policy and environment pins. This makes verification distinct from the rule it evaluates rather than leaving that distinction to an assertion schema. It does not change the signed-rule calculus or confer authority on an assessment.

1. **Assertion:** immutable identified proposition version, with schema version, explicit subject/predicate/typed object, polarity, perspective, source reference and valid-time interval. Free prose is documentary data until an admitted mapping names the precise proposition it supports. `A said p` and `p` are distinct assertions. Identities and decision acceptance are references to their owners' records.
2. **Derivation:** a versioned rule application, named conclusion polarity and ordered/set-defined premise references; it states whether the relation is `sufficient_support`, `documentary_basis` or `review_on_change`. Those relations never silently substitute for one another. Finite, grounded, acyclic sufficient-support rules with explicit signed literals are enough for the first inference slice. Multiple rules are alternatives; every premise in one rule is required. No negation as failure, probabilistic confidence, automatic contraposition or inference from a prose similarity score.
3. **Revision:** an authorized append identifying the replaced assertion/rule version and its effective interval. Proposed corrections do not silently change the accepted view. Retraction removes an admitted assertion from current support; it does not assert its negation. Erasure is a separate retention transition whose restricted audit residue cannot reconstruct deleted content.

The journal is ordered by monotonically increasing committed sequence, not wall-clock order. Valid time says when the proposition applies; knowledge time is the committed sequence at which this service learned the admissible record. Source event time and ingest time are different metadata. A late correction changes a present query about the past but not an "as known at sequence H" query, subject always to **current** disclosure/erasure rules. Historical reconstruction never restores yesterday's access rights.

Every query is evaluated at a context tuple containing knowledge space, perspective, current audience/purpose policy, valid-at, committed memory watermark, source-version frontier and rule-set revision. A vector of journal frontiers is not an atomic platform-wide snapshot. Missing source frontiers make coverage limited; unavailable source history is not evidence that no event occurred. Internal global cuts stay protected: public frontiers, cursor changes, view digests and dirty-state metadata must depend only on authorized information unless the owner explicitly declassifies global activity. An opaque token is insufficient if its equality or issuance cadence still reveals hidden writes. Compare permitted response semantics/distributions with independently generated request metadata appropriately normalized; do not promise byte identity of random view IDs or universal timing noninterference.

### Four values are evidence summaries, not permission or a completeness claim

For a fixed context, maintain independent positive and negative witness sets. Completed evaluation gives `(0,0)` unknown, `(1,0)` supported, `(0,1)` refuted, `(1,1)` conflicted. The bits describe **admitted evidence in that view**, not objective truth, confidence, universal consensus or an action authorization.

A resource-limited evaluation must return discovered witnesses **plus** per-polarity completeness. A missing negative witness under truncation cannot justify the categorical claim "supported and unopposed". Both witnessed polarities remain a demonstrated conflict even if additional search is incomplete. Exhausted evaluation and a complete unknown result are different outputs. Do not invent a fifth truth value for transport failure: keep operational status orthogonal.

Explicitly choose a rule semantics rather than saying "Belnap-like". My initial choice is positive support propagation over signed atoms: `+p` and `-p` are separate premises, so a conflict does not entail an arbitrary `q`. A conflict-bearing premise can supply its named polarity under this semantics, and the explanation retains the contrary witness. A later policy may require unopposed premises, but that is a different versioned rule policy and its completeness requirements must be explicit. Ordinary policy/decision authority never follows from this calculus.

Do not infer logical negation from a failed test, withdrawn source, superseded decision or incompatible prose. `usesStorage(SQLite)` and `usesStorage(Postgres)` conflict only under an explicit schema cardinality/exclusivity rule at overlapping validity and matching scope. Evidence about distinct commits, environments, perspectives or valid-time intervals must not be collapsed into one contradiction.

### Bounded maintenance, with no full ATMS requirement

Evaluate the finite signed-rule graph for the selected context without enumerating all minimal assumption environments. Return a bounded explanation witness; large explanation **display** can be truncated independently of complete support evaluation. Traversal/evaluation exhaustion is instead `incomplete`, never a fabricated final value. Acyclic version references make replay and removal tractable; an unsupported positive cycle cannot bootstrap evidence. Abstract ontology graphs may still contain cycles.

For the two one-way rules `(A and B) -> C` and `(D and E) -> C`, withdrawing B while D and E remain admitted leaves positive support for C. The sketch's equation is interpreted as alternative sufficient grounds, **not** a biconditional definition of C: negative A and negative D do not derive negative C. Any resulting review notification means a named basis changed, not that the decision was annulled. Reverse dependency traversal guarantees only the explicitly registered graph. An LLM-discovered possible dependency remains a candidate, including the claim that a delivered KnowledgeView was actually used.

## Stores, APIs and platform seams

- In the protected service profile, the memory service is the only writer of its admitted semantic journal and derived SQLite indexes. An extractor is an unprivileged proposal client. In the documentary pilot, the existing reviewed repository integration owner writes persistable typed records, and the recall adapter is read-only. That register is a durable semantic history even when Git supplies the machinery; claiming "no new log" must not hide ownership of its facts. Source owners retain their existing journals, source resolution and acceptance authority. No new source-of-truth board, grant registry, keeper ledger or session log is introduced.
- Minimal API: `propose`, `record_revision`, `recall`, `explain`, `changes`; read-only source resolution remains with the owning service. Request retries have stable idempotency identities; immutable receipts name committed sequence and schema. A verifier produces a typed report naming exact subject bytes, environment, verifier/rule version and limits. A generic `verify=true` field is forbidden.
- `recall` yields data framed for an audience and a purpose, plus pins, coverage, evidence availability and explicit source status. Session-host alone delivers it; Curator alone supplies approved executable/instruction context. A changes cursor is a notification stream, never a wake or new-goal capability. Board/keeper processes decide what follow-up exists.
- Simulation/dream evidence carries its world/run scope through every derivation; it may support a claim **about rehearsal** but cannot satisfy a real-world acceptance gate. Apiary chapter 10 explicitly makes that distinction.
- Retention operates on payloads, assertion text, snippets, embeddings, indexes, cached views and exports inside memory's custody. A restricted audit marker records what can legally remain. Source-owned stores and already-disclosed external recipients have separate obligations; do not promise remote recall. A globally queryable content hash may itself disclose information and is not an automatic safe erasure residue.

## Smallest change from the base

Keep its standalone optional runtime, provenance, own semantic journal, source references, alternative justifications, three status axes, bitemporal intent and advisory review. Specify equality, literal polarity, support admission, temporal intervals, source frontiers, current-access checks and partial-evaluation outputs. Replace mandatory ATMS labels with a bounded signed-rule DAG; postpone logic plugins and federation. Distinguish documentary basis/review edges from sound sufficient-support rules. Close the erasure/replay contract and bind each verifier report to its exact subject. Nothing here requires moving authority between existing modules.

## First slice and measurable acceptance

Use case: answer **why home retirement changed from archive-by-default to deletion, when the decision became effective, and which explicitly registered architecture notes need review**. Admit selected architecture documents and accepted decision records only. Start with assertion/revision/source references, documentary basis and explicit review dependencies. No autonomous extraction from homes, transcripts or arbitrary web pages. The first slice is useful without an inference engine; its wire vocabulary reserves the later sufficient-support relation without pretending prose is proof.

Measure the same fixed, human-labelled case corpus with plain document search and SEL: correct source/version retrieval; historical/current distinction; unsupported "current" answers; precision of proposed review targets; registered dependency coverage; operator time to resolve a question; p50/p95 recall latency; bytes retained and purged. Report denominators and source-corpus/annotation revisions. Do not equate dependency coverage with the recall of unregistered semantic consequences. No claimed improvement until measured.

Proposed conformance vectors (paper specification, **not executed tests**):

| Vector | Input or transition | Required result | Forbidden result |
|---|---|---|---|
| V1 Statement vs fact | Signed source says p | source attribution passes; p still needs support admission | signature makes p true |
| V2 Conflict | admitted +p and -p, complete view | conflicted; unrelated q remains unknown | explosion or last-write-wins |
| V3 Alternative support | retract B from `(A and B) or (D and E)` | C retains support through D,E | blanket descendant invalidation |
| V4 No remaining support | remove every sufficient derivation | unknown unless explicit -C exists | refuted merely from removal |
| V5 Bounded work | +p found, -p traversal unfinished | positive witness with negative coverage incomplete | "no opposing evidence" |
| V6 Unsupported cycle | A relies on B, B on A, no ground witness | rejected sufficient-rule cycle in v1 | self-support |
| V7 Late correction | record at seq 20 changes validity from t=5 | distinct answers at H=19 and H=20 | rewrite what was known at H=19 |
| V8 Erasure | source erased, rebuild index from history | no resurrected payload; current verification unavailable | stale cached reproducibility |
| V9 Visibility | contrary evidence is outside audience | output describes only authorized scope, no hidden-edge leak | global "unopposed" or leaked hidden count |
| V10 Schema scope | SQLite and Postgres assertions at disjoint intervals | no conflict without applicable exclusivity | text-based automatic negation |
| V11 Real vs dream | test succeeds only in rehearsal | rehearsal claim only | real acceptance witness |
| V12 Decision survives | one adopted decision basis withdrawn | preserved acceptance record plus review rationale | memory rescinds owner decision |
| V13 Source gap | missing journal range or restored source | coverage gap, explicit uncertainty | infer event never occurred |
| V14 Sufficient, not necessary | rules A,B -> C and D,E -> C; only -A,-D witnessed | no positive C witness; no negative C witness | completing sufficient rules into a definition and deriving -C |
| V15 Attributed remote mirror | authenticated remote writer submits a board ledger-mirror row | attributed report; asserted ledger origin remains unchecked | treat writer attribution as proof that ledger event occurred |
| V16 Hidden metadata mutation | public graph fixed; hidden append/erase/revision advances internal cut | authorized view/cursor semantics disclose no hidden delta | leaking global sequence, cache digest or dirty-generation changes |

## Operator-only questions

1. Which selected architecture sources and audiences are admitted for the pilot, and who owns retention/declassification? This chooses product scope, not a new authority model.
2. What labelled pilot benefit and cost threshold is enough to fund a service beyond document tooling? Proposed measurements above; no invented success numbers.
3. Whether personal memory belongs in a later product. It should not enter the architecture-decision pilot by accidental ingestion.

Choice of rule notation, schema syntax and interval convention should be resolved by maintainers/researchers, not escalated as an operator product choice.

## Evidence and source state

Local sources were read only, without pulls or builds. Source revisions observed on 2026-10-14: wiki `94aebceca3af6a904b73644fb973e201762af8e2`; architecture `567b07701bdf32cdebc516e38e6f0321fc5253a0`; dispatcher `b719e2307f5f4d6284abbd1ba60c42330f2d6ae8`; session-host `255523d43129538b7e7064a0dbfc0b06713bb7e2`; user-manager `12609a9e05d5013c34416e1a0332fe5c28c4bcd5`; broker `ec7fb3d0670449b074521d51f3e03b59f0142a69`; curator-spec `eb1f08c6c66cedc52d9e09553fb791367f334704`; board `ad68902f74ae55b1cd0445fef58390b42feea3dc`; a2a `d283a43c2b7832a7d0e0472151fa0229de7d13b9`; waggle `010b96501ac8777a1a0dc1a083623b9b685fdd0f`. The initial mission/sketch clone was `ec0d6fe44d2596da57d619c9f91f1c0fa5fae130`.

- **S:** [Base sketch](../inputs/SKETCH.ru.md), especially lines 54–203, 219–276, 337–379, 521–591 and 628–760.
- **H:** `swarm-platform-architecture/vision/contracts/handoff-package.md` §§1–6: committed watermark, recipient projection, protected sources, provenance and current authorization at seed time.
- **B:** `wiki/book/ru/09-pamyat.md`: four memory roles, source-linked ladder, explicit command boundary, quarantine and no authority; `10-sny.md`: rehearsal evidence never satisfies real acceptance and dream insights remain quarantined.
- **K:** `wiki/book/keeper/ru/09-zhurnal-i-vosstanovlenie.md`: journal ordering by sequence, atomic transitions, duplicate-input handling and recovery. These are proposed contracts, not claimed deployed capabilities.
- **C:** `curator-spec/cips/CIP-0013-machine-base-context.md` revision 3, lines 9–24, 85–95, 184–225: draft status, consent, pinned updates, no authority from package content and read failure distinct from absence.
- **U:** `swarma-user-manager/spec/helper.md`, effect observation result table: `not_recorded` requires complete authoritative evidence, unlike missing history. `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, lines 101–118: home deletion decision and metadata-only exports.
- **W:** `waggle/spec/waggle.md` §§4.3–4.4, §8: signed provenance and policy remain separate; transport is untrusted. Draft status is explicit.
- **A:** de Kleer, [An assumption-based TMS](https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf), 1986, DOI 10.1016/0004-3702(86)90080-9; author's [publication list](https://www.dekleer.org/bib.htm). Accessed 2026-10-14. Section 4.3 (pp. 144–145) defines sound, consistent, complete and minimal labels; §4.5 gives up to 2^n contexts for n assumptions. The propagation discussion (p. 152) explicitly limits consistency/completeness before termination. Choosing simpler selected-context evaluation is my design choice, not a claim ATMS cannot work. An original worst-case construction is AND over n independent pairs of alternative assumptions: it has 2^n minimal sufficient environments even though the signed support graph is linear-sized.
- **L:** Sutcliffe, Pelletier and Hazen, [Making Belnap's Useful Four-Valued Logic Useful](https://cdn.aaai.org/ocs/17599/17599-77711-1-PB.pdf), FLAIRS-31/AAAI, 2018, pp. 116–117. Accessed 2026-10-14. The paper discusses FDE's lack of a conditional connective and failure of modus ponens for a material-implication encoding. Thus four-value rendering does not pick an executable inference calculus. Source admission, access policy and incomplete evaluation remain our own explicit contract obligations.
- **J:** `skill-project-management/pkg/board/query/activity_ledger.go`, `authorizeLedgerMirror` and its `STATED BOUND` comment at `ad68902`: remote-api mirrors preserve authenticated attribution but cannot prove they were emitted by the ledger mirror sink. `activity_correction.go` separately implements append-only `corrects`/`supersedes` records through an activity transaction. Inspected as code, without running it.

## Post-freeze adversarial round 1

The frozen SEL is a formal specialization of astra-01's `alt-bounded-evidence`, not a competing service or new alternative topic. astra-03 is writing that family's formal companion. I confirmed its two independently reached issues in events `$6jxHbLsDl-Lkefu_yhwLyBeLhFIr4aFr8vtcXgP56qg` (cutoff) and `$9Og11QdbR3N1C-_IDJ_7DOz5rCLDQFEO0JmC0FlyiBM` (conflict rules). This is confirmation of counterexamples, not yet a same-version score proof.

New attack V14 was addressed to astra-03 in `$xo9GjCq6DOlYLcCGOM8NsGmf8ax8frBJtWAL_Iq2YmE`: a support equation must not become a definition whose failed sufficient grounds refute the conclusion. Candidate V15 is in topic `f-mirror-origin`, opener `$39Rvtun7xhHKMjnF4wic_w4CfVDkxx8uoc2U9EELVEM`, with confirmation requested from astra-01/03 in `$aNOKbN84ZuzEm-w97aYUEY-Ft2FPCxP-5obUMxfvaoc`. No finding file exists yet because independent confirmation is pending.

The MCP date-specific statement in S line 52 was checked against [official specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28), accessed 2026-10-14: its Base Protocol section does describe stateless self-contained requests and per-request negotiation. This corroborates that transport state is not durable knowledge; it does not validate the knowledge semantics.

## Post-freeze adversarial round 2

The [mirror-origin finding](../findings/mirror-origin-astra-06.md) is now published in signed `71d9066`, with direct-read confirmations from astra-03 (`$xzDm_O3PeUE8MD5xDjVIfjyrUtbwb5KtSExaKegqSm8`) and astra-01 (`$F5k5_K05289EcMGd0y6gEMbmwTJPKqn456SU5brFNd0`), both five 1. More seats independently confirmed later. No source code change is proposed. Finding attachment `$7O5dlQVM-0TlUQEXrjD4poG7S9FPSx8ioC6GoUqx9-s` has SHA-256 `86ff1dbe51a000d7ff05b5d67deae2050b58e9321fe97562b1a36346efda1706`.

astra-03 explicitly accepted V14 and the edge-role split in `$Wn4qxVWxqyUWx27i2Mf6KkDW5KjKhEmULrFXAuAT2IU`. I read the complete [formal companion](../designs/bounded-support-semantics-astra-03.md) at `877cfdf1568bcafce0ecd063f88f2d8e99910e63`, including its 23 vectors, and the complete [bounded-evidence design](../designs/bounded-evidence.md) at `e8ab519c71c7ad4df483f32cdc77a139b859e6a3`. Those files resolve the original inference/source attacks. I also read [astra-02's security profile](astra-02.md) and its erasure/view findings at `a121605080aee5b4a2aa787979b2d8bde13fa3f3`: current-access rechecks, separate retention lineage, late-writer fencing and an erasure witness outside the restored failure domain are required parts of the scored managed profile.

New V16 challenges a concrete tension between that companion's S13 noninterference and its globally named watermark. I posted `$CX7dxB6U3_Gt7xaJ6irKNkIFR_eWBh0dPjOEyQgH3TM`; astra-02 independently posted the same counterexample eight seconds earlier in `$mBVrz35sCx2C_g0mVVVpJB0440Y4AoASEcsfFJza8DM`. This strengthens the existing [view-inference finding](../findings/view-inference.md); it is not a duplicate finding. The proposed resolution is already incorporated into my query contract above; common-artifact closure remains to be checked.

### Concrete candidate scoring after peer review

| R1–R8 vector | Total | Candidate and evidence boundary |
|---|---:|---|
| 2,2,2,1,2,2,1,2 | 14 | Bounded-evidence **file alone** at e8ab519: the author explicitly leaves the dedicated security/evaluator contracts incomplete. Matches astra-01 and astra-04 on this exact file. |
| 2,2,2,2,2,2,1,2 | 15 | Bounded evidence **with** astra-03 semantic and astra-02 security profiles, including current-access/erasure and authorized-metadata commitments. No executed conformance. |
| 2,2,2,2,2,2,1,2 | 15 | Strengthened documentary register with the **same** admitted-source, view, supersession and managed-derivative contract, limited to explicitly persistable documentation. Git is not a private payload store; controlled private sidecars, if any, must satisfy the service profile. |
| 2,2,1,1,2,1,1,2 | 12 | Original wonder-01 JOM attachment `06cac67e…`: useful card/CLI/kernel, but its low-weight Curator overlay is not a data boundary (R3); Git erasure is admitted incomplete (R4); its initial read-time evidence/AND-OR semantics are open (R6/R7). Later room corrections materially strengthen this candidate. |
| 2,2,2,1,2,1,1,1 | 12 | Original wonder-01 compiler attachment `e7088421…`: narrow builder and normal approval boundaries, but its no-derived-storage premise contradicts retained briefing bytes, ladder summaries, rejection log and TTL caches (R4); recomputed explanations lack a complete reproducibility contract (R6/R7); first worker-briefing slice depends on an unclosed host package lane (R8). Explicit-pull documentary compilation could improve that last score. |

The strengthened document score is not a revision of the frozen TDD score by wishful thinking: it adds the very semantics, controlled output/retention and source typing the thin baseline lacked. R1–R3 and R5 reuse the common small, non-authoritative, runtime-independent contract. R4 is conditional on the named document-only admission and managed derivative scope, not the extension `.md` or a promise that review detects all secrets. R6 follows the same source/partial-evaluation/revision contract. R7 stays 1; R8 uses the same archive-home decision corpus with explicit pull and fewer initial moving parts. Broad Git private-memory ingestion would lose the R4 point again.

I fetched and read the original JOM and compiler files from room attachments `$eh6HiwHu8dU9XoYoMV3X0aH6PpPgPmFeUU3cLVt4_Io` and `$YgY-s1TErF7Pdb_p3s9kcUAxYxCxDxdTngzknuOAsxs`, respectively, rather than treating later discussion as the original design. Exact hashes: `06cac67eb744b2bf31bd29e039db48891ece98d900b42d48e90b55677a6dec52` and `e708842131c64b8aef4bdc33c167f8b446ce8310be9fcbcfc14d60c09b6adfc0`. Local read copies are `.temp/astra-06/alt-journal-only-memory.md` and `.temp/astra-06/alt-memory-as-compiler.md` in the seat directory. The compiler retention/replay challenge is `$EqNSU-JhqIsQ3UtPC_l6udEy1AkoRgToPvCq4XnESDw`; I do not claim these original files contain subsequent repairs.

**Recommendation narrowing:** astra-04's review of the P0 surface was persuasive, and astra-01 accepted it in `$5xQbTPFC1tAGDlJkbflxxJmT0dR82c9-2Sc8hTjOsYU` / `$FSMUYFQhhG7FtlpyeGkC3gbmNTScdQ5TqTFpYGuL-7w`. Documentary M0 has no requirement that forces a daemon. It also must not silently allocate a `knowledge_view` reference in the closed `swarm-handoff/2` grammar; explicit pull avoids that unpublished integration. Service isolation is justified by a later protected multi-proposer profile, not by calling a journal universal.

**Round-2 proof status:** my full-profile vector was posted in `$_lZYOWuvt_xgB_fE_UITLHBc-GoVbAiZJ3KPcWBklPo` and matched astra-03 on every row. At that point the V16 metadata clarification still needed an assembled artifact. The hypothetical strengthened document and managed profiles tie, so that comparison does not select a unique storage engine. The exact subsequently filed profiles and proof record follow below.

## Exact assembled review, round 4

I read the complete `56d18ee` to `0ce009435206f31f387efd207dc3f2662e66e4d9` delta and resulting [bounded-evidence design](../designs/bounded-evidence.md), verified that commit's signature, and checked its SHA-256: `9c8f63fd8aad3d44081b93225f727e504468297cadc21ab1d0973903d28c0599`. Its explicitly adopted [semantic companion](../designs/bounded-support-semantics-astra-03.md) at `476ec3618c7c55d471a572454aa7e4aba772aab6` has SHA-256 `adde0314375f1950a817962c1c513070ef86aa3b01f1fecb14e86fe9339fd3ba`. I previously read the companion and its complete corrective delta; confirmation event `$ZXyxc2K3znMXyC3wI7IiUxKX4XSOjjmCRfzeGdzgP-A` records that review.

The assembled text closes V16 at contract level: protected internal cuts are distinct from disclosed metadata; hidden writes cannot change public handle equality, issuance, length, cursor, digest, receipt, coverage or error behavior. Normalization cannot conceal a hidden-dependent counter. S24 compares authorized projections across hidden append/revise/erase; S25/S26 cover an old restore and a late derivative writer. This is a semantic/metadata requirement, not a universal timing or traffic-analysis proof. The original source-origin and one-way-support challenges also remain resolved. No new finding is created for these refinements.

| Exact profile at `0ce0094` with companion `476ec36` | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Protected service, P-managed | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | **15** |
| Filed documentary pilot, P-doc | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | **14** |

R1 follows the five explicit shapes with a derived View; R2 preserves existing owners and journals; R3 retains data-only explicit pull and no new handoff wire member. R4=2 belongs to the specified managed custody, current-rights, erasure, restore and metadata contract; it is a design score, not a passed security qualification. The filed documentary profile explicitly avoids private Git payloads but does not inherit that full managed custody guarantee, hence R4=1. This exact P-doc is **not** the hypothetical strengthened document profile scored 15 in round 2. R5 follows the runtime-independent API and optional platform adapters. R6 follows typed attribution/assessment, one-way signed support, separate completeness and proposed revisions. R7 stays 1 because concrete closed schemas and exact input/output fixtures remain unpublished; executing a prototype is neither allowed by this mission nor required merely to score a sufficiently specified research design. R8 retains the independently useful explicit-pull archive-home/delete-home pilot.

The added [service-admission finding](../findings/memory-service-admission.md) is consistent with direct inspection of user-manager `spec/helper.md` §§8–8.1 and session-host `spec/session-host.md` §3.1 at the source pins above: a later service needs its own owned, qualified socket/generation/egress boundary. Documentary M0 does not need that daemon, and the later gate does not disable earlier software-root work. This is a deployment constraint, not a reason to enlarge memory's authority.

**Proof boundary:** astra-03 (five 1) directly read and scored this exact assembled artifact in `$p6gek454MWjxXasqM_alguzPwr9bffWW2c8AiyLIgC8`; my matching rows supply the independent five-2 side. Astra-04 and astra-05 also directly ratified it in `$ZHOqMsgPsMRvYmQ7oOiijzHHx4oGmE-89-RrG36iArE` and `$W6Z420vc49y3Eflx2Xn5ti_MQNDmd58lKsVT549kVVA`. This meets the mission's two-five agreement rule for the highest-scoring assessed contract, with no R3/R4/R6 zero. It does not establish global optimality, measured product superiority, a unique storage choice or two-host proof. Documentary P-doc is the recommended first experiment despite its narrower R4 guarantee; managed P-managed is a later qualification target, not a reason to deploy a service before measuring value.

One intentional alternative-score difference remains: I retain original COMPILER R5=2 for its explicit non-runtime-specific `build_view` adapter, while its author uses R5=1 for stronger system-portability expectations. That is a stated one-point rubric interpretation, not an unrecorded convergence. Original COMPILER R4/R6/R8 limitations and original artifact hash remain as scored above; later amendments must not be projected backward onto it.

## Work log

- Read the mission fully; pulled the research clone with `git pull --rebase` (already current); read both sketch halves. Tool readiness recorded in the seat directory `.temp/astra-06/tool-readiness-01.log`.
- Onboarded only the assigned a2a identity; joined `swarma-memory`; initial topic list contained `rounds` only. Followed the a2a skill printed by `a2a skill print`; source is `a2a-swarm/internal/skill/files/a2a/SKILL.md`. No other source repositories, board state or code were modified.
- Froze and published the independent score record before reading five 1's verdicts, then read astra-03, challenged the formal and disclosure boundaries, obtained peer confirmation and compared exact candidate versions. Only the confirmed mirror-origin issue became this seat's finding; later refinements stayed with existing finding owners.
- Signed and verified `dec1a5b`, pushed directly to main under the mission-specific publication rule; the source corpus remained unchanged. First-five topic bodies were read only after that commit.
- CLI documentation mismatch: `a2a post --non-blocking` was refused (`flag provided but not defined`); `--reply-by 30m` was refused (RFC3339 required). Retried with non-blocking intent in the message body and exact `2026-10-14T01:45:00Z`; both questions posted successfully. No shared tooling fix was attempted because this mission forbids source/tool changes. `a2a post --help` also only reports `help requested`; evidence is in `.temp/astra-06/a2a-post-help-02.log` in the seat directory.
