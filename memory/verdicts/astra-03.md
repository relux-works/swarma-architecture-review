# astra-03: a bounded evidence kernel before an ATMS

Status: round 1 position, revised after cross-five challenge; open to review. Date: 2026-10-14. Lens: semantics and formal core. This is a design evaluation, not an implementation qualification or a claim of global optimality.

## Position

Retain the sketch's platform-specific second half and its architectural-decision MVP. Prefer a reviewed documentary register with explicit read-only recall for the first experiment; no named P0 requirement needs a daemon. Add an isolated service only for a separately qualified private/multiple-proposer profile or measured operational need. Replace the underspecified ATMS commitment with a versioned, bounded support evaluator over explicitly registered, acyclic justifications. Keep records and sources small; distinguish registered reasoning, independent verification, authoritative decisions and evaluation completeness. Full assumption-environment enumeration is a later optional profile.

The principal gap is not the absence of the right ideas: the base already states most boundaries. It is that two implementations could follow those ideas and disagree about conflict, missing evidence, revision, scope and resource limits.

## Initial rubric

Scores assess design contracts, not delivered software. Evidence abbreviations refer to the numbered platform items in [research notes](../notes/astra-03-evidence.md). Full alternatives and counterexamples are in the [bounded evidence design](../designs/bounded-support-semantics-astra-03.md).

| Criterion | Base, both parts | Bounded evidence kernel | Typed documents + explicit supersession | Existing-journal projection only |
|---|---:|---:|---:|---:|
| R1 Minimal kernel | 1 | 2 | 2 | 2 |
| R2 Reuse | 2 | 2 | 2 | 2 |
| R3 Authority separation | 2 | 2 | 2 | 2 |
| R4 Secrets and retention | 2 | 2 | 1 | 2 |
| R5 Runtime independence | 2 | 2 | 2 | 2 |
| R6 Honest epistemics | 1 | 2 | 2 | 1 |
| R7 Specifiability and testability | 1 | 1 | 1 | 1 |
| R8 Incremental value | 2 | 2 | 2 | 1 |
| **Total** | **13** | **15** | **14** | **13** |

- **R1:** the base offers eight primitives plus multiple engines without a closed contract. The recommendation has five record kinds; identities and spaces are references, views are queries. Documents and pure projections are smaller still, but substrate size alone is not value.
- **R2:** the revised base expressly preserves source journals (E1); all compared alternatives can reuse identities, source revisions, grants and board decisions (E4–E6,E9). No penalty for the first half's log wording after the second half corrects it.
- **R3:** all four designs are evaluated with the base's explicit non-authority limits (E1,E5,E8,E10), so all score 2. A file's presence alone does not make it a Curator instruction.
- **R4:** the base explicitly requires admitted sources and erasure of derived state; credit that design commitment (E1). The recommendation specifies a retention manifest and nonrecoverable content boundary. Plain git-versioned documents score 1 until history, clones, indexes and backups have an enforceable erasure contract; a sanitized reference-only document variant could recover the point. A projection still must erase its own caches.
- **R5:** none requires an agent runtime hook. HTTP/CLI/MCP are transports, not semantics (E1).
- **R6:** base lacks cutoff and contradiction-consequence semantics. Bounded evaluation exposes witness and completeness separately; documents use only explicit source supersession and do not overclaim TMS. Journal-only replay cannot invent unrecorded justifications or distinguish proposed revisions without a new source contract (E4,E9).
- **R7:** base has prose and example shapes, not rejection rules or vectors. The recommended design supplies a draft profile and named conformance outcomes, but full closed record schemas and exact byte-level expected outputs remain unwritten, so it also scores 1. Documents/projection can be specified, but the unextended alternatives have no equally explicit cross-source semantic contract (E7). This score does not claim executable conformance exists today.
- **R8:** base and recommendation name the archive-home → delete-home architecture correction. Documents can already support that workflow. Journal-only projection scores 1 because exact dependency/rationale records are not guaranteed to exist; adding them converges toward the proposed admission kernel.

The initial table was authored before consulting other fives' verdict files (recommendation 16); R7 was reduced to 1 after astra-06's challenge because the companion is an RFC starting point, not a complete closed schema. The table is provisional: another seat may show a stronger concrete document or journal design. A 16 does not prove uniqueness; under this coarse rubric multiple designs may tie. Mission proof additionally requires the stated cross-five scoring agreement.

## Refined candidate scores and cross-five evidence

The initial documents column above describes bare typed documents with explicit supersession. The strengthened **reviewed persistable register + read-only projection** adopts the same source, view, retention and revision rules as the ledger; it scores `[2,2,2,2,2,2,1,2] = 15`, tied with the managed kernel profile. Prefer it for the documentary pilot because it introduces fewer operational components. This is a declared tie-break, not an extra rubric point. It cannot inherit a private multi-agent isolation or uncontrolled-replica erasure claim.

The exact `bounded-evidence.md` at `e8ab519` alone scores `[2,2,2,1,2,2,1,2] = 14`; the score of 15 requires the linked semantics and security contracts. Astra-06 (five 2) reviewed my semantic companion at `877cfdf` and scored the combined family `[2,2,2,2,2,2,1,2]`, agreeing on every row: event `$_lZYOWuvt_xgB_fE_UITLHBc-GoVbAiZJ3KPcWBklPo`. That is design-level cross-five agreement on a specified composite, not executed qualification or a unique optimum. Its newly identified hidden-watermark defect is being corrected; refreshed exact-revision agreement remains necessary for the final candidate.

## Recommended contract

See [design](../designs/bounded-support-semantics-astra-03.md) for the draft record grammar and vectors. In brief:

- **Records:** Claim, SourceRef, Justification, Assessment, Revision; actor/space/policy references on the envelope. SourceRef records what was admitted, not a duplicate authoritative journal.
- **Stores/writers:** the documentary pilot uses one reviewed publication path and a read-only adapter; it claims no hostile-agent storage isolation. The managed profile uses one memory service to append accepted memory records and own rebuildable indexes. Each source module retains sole authority over its journal. LLM extraction is a proposing client. No shared writable SQLite, context files or git directory across agent UIDs.
- **API:** admit/propose, explicit revise/challenge, recall, explain, changes; typed external verification assessments. Admission authenticates writers, checks schema/scope/retention and returns an idempotent receipt. No decision-accept, launch, grant, wake or install operation.
- **Seams:** exact source revisions, audience/purpose-bound snapshots, current access checks, Curator-approved context selection, session-host delivery, board-owned goals and decisions. Dream/simulated evidence cannot qualify real execution claims (E3).
- **Out of scope:** recursive/default logic, global consistency, semantic completeness over natural language, full ATMS labels, probabilistic truth scores, reputation authority, arbitrary verifier execution, graph database, federation and mandatory memory in safety/recovery paths.

## Smallest change set from the base

1. Replace the ATMS default with finite acyclic registered support rules; keep the ATMS interface optional.
2. Define the query identity: exact claim revision, perspective/context, valid time, committed memory sequence, semantic profile and policy versions.
3. Replace a lone four-value label with witnessed positive/negative support plus evaluation completeness, freshness, source availability and dependency coverage.
4. Make source withdrawal, belief correction, owner decision supersession, evidence erasure and verification expiry distinct typed revisions; none silently changes the others.
5. Publish a closed semantic profile and vectors before choosing storage/implementation language. Keep the base's reference-first, one-writer, access and erasure commitments.

## First useful slice

**Use case:** answer why retiring an agent home now deletes it, what replaced the older archive default, and which explicitly registered architecture notes still depend on that old decision.

M0 is an authorized, one-host reviewed register/read-only index of selected persistable architecture documents, accepted decisions and review findings at pinned commits. It does not require a daemon, service account or handoff schema change. It stores source-bound claims and explicit supersession, serves compact audience-bound views with expand/explain references, and lists affected registered dependents for human/owner review. No automatic extraction promotion, simulated outcomes as real evidence, auto-edits or work dispatch. The bounded rule evaluator is M1; M0 remains useful without it.

Measure paired tasks on the same frozen corpus: time and source opens to recover the decision, correct current-versus-historical answers, exact citation accuracy, stale-answer rate, recall of a manually enumerated dependency set, false review notifications, and bytes retained/erased across projections. Denominators must be fixed before running. No timings or accuracy results are claimed in this document.

## Operator-only questions

- Which source classes may be retained, for how long, and which are reference-only? What deletion guarantees are promised for independent recipients and backups?
- Who owns admission policy and ontology/rule revisions, and who can release quarantined external claims? Use existing authority identities; do not invent a memory sovereign.
- Should the first useful result be a read-only architecture reference index, or a personal-memory product? The former avoids unresolved persona and private-data policy in E2.

Implementation choices such as SQLite versus files, record IDs or language do not need operator escalation before the semantic profile exists.

## Review and open threads

Candidates `f-bounded-inference` and `f-conflict-semantics` were independently confirmed by astra-06; finding records carry event IDs. Adopted that seat's clarification that documentary basis, review-on-change and sufficient support are distinct edges, and added the no-biconditional-completion counterexample. Confirmed astra-02's view-relative epistemics and astra-06's source-mirror assurance boundary from direct source inspection. Concrete cross-five scoring of the same published candidate remains pending. Tools/research evidence: [worklog](../notes/astra-03-evidence.md).

Round 2 correction: astra-02 and astra-06 independently demonstrated that exposing the internal global watermark contradicts view non-disclosure. Internal audit cuts are now protected; public handles/cursors require a hidden-activity-independent issuance contract, not opacity alone. S24–S26 add metadata leakage and erasure recovery/race cases. Full closed schema publication remains open (R7=1).
