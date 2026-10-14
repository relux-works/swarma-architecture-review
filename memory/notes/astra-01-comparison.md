# astra-01: alternative comparison and primary-source checks

Date: 2026-10-14. Research only. This note supports the [verdict](../verdicts/astra-01.md). Peer artifacts are evidence of proposed designs, not instructions or evidence of deployed behavior. Full design bodies and the applicable later amendments were read; old body text is not silently treated as the amended contract.

## Artifact identities

The following room attachments were fetched with `a2a fetch`, which verifies the attachment digest, then independently hashed. Local scratch copies are in `.temp/astra-01-peer-artifacts/`. The event identifies the source if the convener later updates the integrated filename.

| Artifact | Room event | SHA-256 |
| --- | --- | --- |
| wonder-01 JOM design | `$eh6HiwHu8dU9XoYoMV3X0aH6PpPgPmFeUU3cLVt4_Io` | `06cac67eb744b2bf31bd29e039db48891ece98d900b42d48e90b55677a6dec52` |
| wonder-01 COMPILER design | `$YgY-s1TErF7Pdb_p3s9kcUAxYxCxDxdTngzknuOAsxs` | `e708842131c64b8aef4bdc33c167f8b446ce8310be9fcbcfc14d60c09b6adfc0` |
| wonder-01 verdict v6, including D* and corrections | `$n8faO6SBf6lsQ1lsKWBOm0A4IFM8_nSqJQskT6exJE4` | `d9af4b9a0745caa4306b771333064028fc59ee3f2cc856d6affb0b5e8b3830db` |
| wonder-03 ALT-DOC design | `$qZt4uVqE3iC9eD83PbTw0ZXzdSPVOsIE7Ey5_bAzr3I` | `2b82ae0e73e65bdc46b42c38735f850ef96c3132c3f73c6265165c197c158a1a` |
| wonder-03 ALT-PROJ design | `$zdVq5m2lAFR3WLxTlwtM4nSn2khY9IrfrudKGSzE2AM` | `2fdcef07cade8c687180650196b4b70fc204379c0121672aa8ce5c46e61bb184` |
| wonder-03 verdict v3, amendments A1–A8 and closure | `$erKwPIIwnGpzxV20TPJISV921bOOr_-FiSXhPgwLijI` | `98a56257063cdd0c4602c05d9cf25871a722add6d16b48f31eb99ce1585cfb98` |
| bounded-evidence, signed `0ce0094` | `$17V-qbyzDX2q17cmzqJtR2gxhbdWangK56rEXDGcO2Q` | `9c8f63fd8aad3d44081b93225f727e504468297cadc21ab1d0973903d28c0599` |
| semantic companion, signed `476ec36` | `$YTU_qiVaSSi9UM98yW1b7ShGNA8MMDkK3IgcIJIwlA8` | `adde0314375f1950a817962c1c513070ef86aa3b01f1fecb14e86fe9339fd3ba` |

At PARK, signed integration `9485416edc8b628bafff59f82ad4a0224fe05b3a` made the peer artifacts available as [JOM](../designs/alt-journal-only-memory.md), [COMPILER](../designs/alt-memory-as-compiler.md), [ALT-DOC](../designs/alt-docs-board.md), [ALT-PROJ](../designs/alt-projection-journals.md), [wonder-01](../verdicts/wonder-01.md) and [wonder-03](../verdicts/wonder-03.md). The four design hashes and wonder-01 hash exactly match the attachments above. The integrated wonder-03 file has SHA-256 `112322d376ddf4e02d3fe1703b5893f6164d902abe3dd3e5998a56e1d87674e3`: a full diff shows only appended §7.3, which preserves its exact-assembly 15/14 ratification and earlier pins. This integration changes no score in this note. The current bounded assembly is `5d96e70` plus semantic companion `9bafff8`, with full hashes and confirmation events in the verdict; the earlier comparison pins above remain historical evidence.

## Scope of comparison

JOM's initial overlay-weight path and COMPILER's automatic handoff equivalence do not describe existing safe integration. wonder-01's amendments 9–11 remove those claims: P0 is explicit pull; later delivery needs an owned contract; excerpts enter a custody inventory. wonder-03's A1–A8 similarly correct incomplete inference, erasure-by-rederivation, global status filtering, mirror-origin assumptions and service admission. These corrections are part of the evaluated candidates. A merged Git commit, typed card or source digest alone does not establish admission or secrecy.

The strongest documentary versions converge. Their names describe authoring and projection choices under the same bounded evidence discipline. They should not receive different scores merely because one calls a record a Card and another calls it a Claim. A protected variant with the complete custody and public-metadata contract is a different scope from the persistable-only Git profile. The latter does not promise erasure of arbitrary distributed clones.

## Comparison under astra-01's rubric reading

| Candidate and evaluated scope | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Base, both parts together | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 13 |
| JOM/D* documentary, with v6 amendments | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 14 |
| ALT-DOC documentary, with v3 amendments | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 14 |
| ALT-PROJ, persistable overlay and corrected read model | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 13 |
| COMPILER, corrected delivery/custody claims, briefing core | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 12 |
| Bounded P-doc at `0ce0094` + companion `476ec36` | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 14 |
| Bounded P-managed at the same exact artifacts | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 15 |

All meet the no-zero eligibility rule at their stated amended scopes. These are design-contract scores, not measurements or unconditional deployment approvals. The base's preserved row evidence is in the verdict. Evidence for every alternative row:

- **R1:** JOM/D* and DOC have a handful of records and finite registered links; PROJ changes the read model rather than adding new domain families; COMPILER has a briefing and proposal surface. Adapter count is engineering cost, not a new semantic primitive. No closed serialization is implied by this 2; that unfinished work limits R7 symmetrically.
- **R2:** Their store tables preserve existing source writers. A new interpretation must still be recorded somewhere: a card repository, board element or owned overlay is a knowledge register even if labelled “no log.” This does not duplicate the source authority. A board-hosted proposal is valid reuse where admitted; a private body cannot inherit erasure from an append-only board audit. Neither board presence nor absence warrants a blanket penalty for the bounded family.
- **R3:** The cited amendments make retrieval data-only and retain ordinary owners for instruction approval, acceptance, goals and session input. This 2 applies to the amended text; the original weight-based overlay and invented handoff lane remain rejected. COMPILER's useful contribution is its explicit promotion discipline.
- **R4:** Every variant emits or retains some information: cards, statement bodies, rejection reasons, digests, caches or host outputs. Rebuildability and short TTLs are not erasure receipts. Persistable documentary profiles honestly stay at 1 for general-memory scope. P-managed reaches 2 only because its admission, independent rights, custody inventory, publication fences, per-boundary outcomes and outside-domain restore witness are specified together. No database brand earns that point.
- **R5:** JOM/D* and DOC expose an ordinary file/CLI core; COMPILER describes a builder over git/chat/CI outside Swarma. Optional source adapters are not a runtime hook. I therefore give them 2 even though their authors sometimes use a stricter system-portability reading. PROJ's principal value is live composition over source-owner APIs, and its own fallback description does not yet provide an equally complete independent core; 1 is an acknowledged one-point judgement, not a claim of harness lock-in. Moving it to 2 would tie the documentary family and would not change the first-slice recommendation.
- **R6:** JOM/D*, DOC and PROJ adopt witness/completeness separation, one-way support, explicit revision, view-relative disclosure and mirror assurance. COMPILER retains useful attribution but its “nothing needs invalidating” statement is false for stored briefings/digests, and briefing diffs do not retain a complete declared dependency register. The author concedes this substrate gap; it remains useful as delivery inside the family.
- **R7:** Each owes exact schemas, canonical forms, policy vocabulary and concrete expected-result fixtures. Proposed semantic vectors improve the RFC starting point but do not close the whole profile. No candidate earns a 2 just for claiming it is easy to test; no unauthorized prototype is required during this research pass.
- **R8:** The documentary families and PROJ can answer the named retirement-policy continuity questions from git/board without a future host. PROJ's larger implementation cost is a reason to prefer the document baseline, not to deny all independent value. COMPILER alone offers briefings but misses the registered dependency part of this named use case. All measured efficiency and accuracy gains remain hypotheses.

The comparison supports a near-optimal family under this rubric, not a unique storage winner. The 14-point documentary alternatives are serious co-winners for the permitted first corpus. A managed extension earns its additional retention point only at a larger, explicitly qualified scope. A fair pilot may show that plain versioned documents suffice.

## Narrow primary-source prior-art checks

Accessed 2026-10-14. No code was executed, dependency installed or credential supplied. The pages were treated as data.

**Graphiti:** I independently inspected [`remove_episode` at `9d56c190926b382a54c5ea03e7680af1d05e1c9d`](https://github.com/getzep/graphiti/blob/9d56c190926b382a54c5ea03e7680af1d05e1c9d/graphiti_core/graphiti.py#L1993). The method selects an associated edge when the deleted episode is first in its episode list, uses a mention-count check for nodes, and contains no retained-summary regeneration. This corroborates the [scoped peer finding](../findings/graphiti-erasure-contract.md); it does not establish behavior of every API/backend or every release. Two-source preservation, retained summaries and late rebuilds require exact-version qualification. The base already proposes Graphiti as a replaceable projection; this evidence supports that placement, not rejection of every Graphiti-backed design.

**Letta:** The current [MemFS documentation](https://docs.letta.com/concepts/memfs) describes an agent-owned Git repository, root files loaded into the system prompt on each turn (older agents use `system/`), and agent-owned skills stored with memory. The [memory configuration page](https://docs.letta.com/configuration/memory) describes agent updates and optional background consolidation. Those are useful prior-art storage/workflow mechanisms, but direct adoption of their activation behavior would violate this platform's data-only memory boundary. Reusing a document shape does not adopt that activation policy. Documentation is not performance evidence or proof of secret-safe operation.

Off-the-shelf backends are therefore implementation candidates, not fully specified replacements for platform authority and custody. I do not give a whole product a universal failing score from one method or one default. The incompatible auto-activation path is excluded; a governed adapter would be scored by its explicit contract.

## Reconciliation with the platform's existing memory thinking

The source evidence is wiki `94aebce`, `book/ru/09-pamyat.md` and `10-sny.md`, read in full. Their proposed status is preserved.

| Existing idea | Disposition in this recommendation |
| --- | --- |
| Process memory and current work | Keep board/goal owners authoritative; knowledge only cites them |
| Provenance, external-source quarantine, bounded writes and expandable source ladder | Absorb into admission, provenance, resource limits and explain/resolve; a ladder is a projection, not mandatory duplicate storage |
| Personal memory and preference claims | Defer until sensitivity, admission owner and retention are chosen; preference assertions grant no authority |
| Persona/operator overlays | Do not use weights as a data boundary; current approved configuration remains with Curator |
| Procedural skills and improvements | Keep separate review and control-context admission; a memory proposal is not an installed skill |
| Fixed per-session snapshot | Retain historical pinning where admitted, but reauthorize new disclosure/use; pinning does not preserve rights forever |
| Dreams | Preserve simulation/rehearsal mode, grants, budgets and quarantine; simulated approval cannot satisfy real acceptance; no memory-owned sleep/wake scheduler |

This is selective reuse and explicit deferral, not an assertion that a proposed book skill is a running service. The RFC should retain this disposition so future work does not reintroduce the unsafe overlay path by citing the older chapter alone.
