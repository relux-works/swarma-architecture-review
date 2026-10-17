# R7 divergence ledger

Sole writer: astra-27 (judge). Contract: `memory/MISSION-R7.md`.
Initial review baseline: `95f974b41667e25d4a3a7630055ef1c20690fb7d`.

## Review contract

Apply source precedence in `memory/designs/kernel.md`: owner decisions D-001–D-008,
kernel v0.2, normative companion, then bounded-evidence design. Do not reopen
settled design. The package supplies concrete grammar and normalization choices
within that contract; it cannot silently change source semantics. A package-only
implementer must be able to reproduce each exact expected semantic output.

Each submitted divergence or adversarial case receives its own row, with a
minimal witness and the relevant source/package clause. Classifications are
`spec-bug`, `impl-bug`, `ambiguity`, or `rejected`. A correction is closed only
against a committed fix and relevant rerun/control evidence. A source-level
choice the contract does not decide becomes an owner question; the judge does
not choose new architecture on the owner's behalf. Rejected cases retain their
reason. Mixed findings are split so a fixed package cannot hide an unfixed
evaluator, or vice versa.

## Items

| ID | Source (seat, file, event) | Vector or clause | Classification | Fix owner | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| R7-001 | astra-24; [premise-quality-alternatives](cases/astra-24-premise-quality-alternatives.md) at `9ecd449`; event `$G4OHTOUl4Wqb3NVg7LDKrGvEjh9H_w7noy_5kFAQBR0` | Kernel §6.1; companion §§4–5; S03/S31 neighbors | rejected | None; astra-24 may retain regression | rejected | `0ef608a` K-EVAL-4 explicitly makes any demonstrated clean path win, independently of explanation enumeration (K-EVAL-7). Proposed bad reading contradicts the package. No evaluator result yet; a later failing fixture receives its own implementation finding. |
| R7-002 | astra-24; [rule-applicability](cases/astra-24-rule-applicability.md) at `9ecd449`; event `$oVPSMnZ16rOhG4J9bIPYpl0Gz8ahzkjS7HRmnYKAc2c` | Companion §§3–4; kernel §§2, 6; S10 neighbor | rejected | None; astra-24 may retain regression | rejected | `0ef608a` K-RULE-2 includes rule validity/context/active revision/policy; K-TIME-1 defines half-open endpoints; the required justification envelope carries validity. No missing interval representation or competing normative reading. |
| R7-003 | astra-26; [import-attribution](cases/astra-26-import-attribution.md) at `93455d8`; event `$_hBE9WQEffLFwyKMHmaG3P-pHANdFygcHEddq8zxP6A` | Kernel §§2, 6.1, 8, 9.1; companion §3 | rejected | None; astra-26 may retain regression | rejected | `0ef608a` K-ENV-1/2, K-REC-1 and K-DISC-3 distinguish the importer-issued report from its original issuer. Source fields include original_issuer, carrier and origin; K-ENV-3 preserves input classes. Explicit issuer-A impersonation still refuses. |
| R7-004 | astra-26; [publication-currentness](cases/astra-26-publication-currentness.md) at `93455d8`; event `$yfHdYWubs0jO06LmD0GiV5hRlAfmwZCeuruA1gvERi8` | Kernel §§1, 6.3–6.4, 9.2 | rejected | None; astra-26 may retain regression | rejected | `0ef608a` K-PUB-2 requires an admitted current-version check, otherwise last_received; K-EVAL-6/9 separates freshness and currentness. policy.imports represents current/replaced/unverified and checked_at. No source ambiguity for the stated unavailable-check case. |
| R7-005 | astra-25; [hidden-premise-quality](cases/astra-25-hidden-premise-quality.md) at `5a32468`; event `$D58DR3_cFp-0TYJp-WFZHS95MPjO_CdsU00kf3SSL0w` | Kernel §§6.1, 7.3; S13/S24/S27 | rejected | None; astra-25 may retain regression | rejected | `0ef608a` K-AUTH-1 filters individual records by audience/purpose before accounting; K-EVAL-4 and K-NI-1 explicitly preserve quality under hidden-only changes. Same-space narrower grants are representable. Adversary independently concurs in event $MiH7YQ55_M6fGk-VY8Qf1LUHtcNM4Ffs5URYTzKDA8E. |
| R7-006 | astra-25; [declassification-intersection](cases/astra-25-declassification-intersection.md) at `5a32468`; event `$JRP0ZTvwmvjdy9dVvzatgS824Y1K6qZGjz5Az3_rSMw` | Kernel §§6.4, 7.1–7.2, 9.3 | spec-bug | astra-21 | open | `0ef608a` K-DISC-2 uses one policy owner and retained assessment; disclosure has one assessment ref, with no input-owner decision intersection/current applicability facts. Kernel v0.2 section 7.2 requires every constrained owner's exact current decision before new disclosure. Retain revoked-OB and valid two-owner controls. |
| R7-007 | astra-25; [surviving-support-erasure](cases/astra-25-surviving-support-erasure.md) at `5a32468`; event `$cV4c9b6aHDM9Swa3VBXyHzHbG5DRKDK_fYgJbVWuabY` | Kernel §7.1/P08; companion §6/S12/S20 | rejected | None; astra-25 may retain regression | rejected | `0ef608a` K-ERASE-1 traverses lineage/custody independently of logical edges; K-ERASE-2 makes an unreachable controlled sink incomplete/purge_pending. Runtime custody encodes controlled/reachable/present; K-TIME-1 and K-PUB-1 prohibit erased historical payload delivery. Real deployment remains unqualified. |
| R7-008 | astra-25; [stale-restore-witness](cases/astra-25-stale-restore-witness.md) at `5a32468`; event `$7ed7G5T6VBlEQ1c53ObNr7Ab6sPC9h1GnaD2x8nQ7Nc` | Companion §6/S25; design retention contract | spec-bug | astra-21 | open | `0ef608a` K-ERASE-3 requires current completeness but restore/reconcile_restore expose external_witness:boolean without defining its trusted prevalidation predicate. Clarify true means current COMPLETE outside-domain evidence for all obligations, not location/existence/signature alone; add stale-witness refusal plus current-complete control. No new recovery protocol is required. Corroborated by astra-25 event $fMIluMf1cdLWFgQgV0CDLBqth9WrfbTbmxanjHDANe4. |
| R7-009 | astra-27 release inspection; convener event `$byrILfhj-Gjsp7famnjMP2EvJbP8t9WBhwRblTS_pGk`; package `0ef608a` | Mission editor scope; kernel v0.2 sections 1, 5.4, 6.4, 7.1, 9.3, P12–P15 | spec-bug | astra-21 | open | Landed 0.1.0-draft intentionally targets kernel v0.1. Lineage is only a ref array, projection rules lack exclusion, and P12–P15 are absent. Release the assigned v0.2 uplift with distinct outcomes, snapshot applicability, integrated/unknown lineage and normalized tuple. Declassification is tracked separately as R7-006. |
| R7-010 | astra-26; [representative-public-alias](cases/astra-26-representative-public-alias.md) at `d9336fd`; event `$taT2lxQpJoTnfA07PMaF9vPsNbJGZk6O0xGQRWsW400`; decision `$4rnofaDXvrTjC2UMAgpxxn5o_DuPCzwbPN31zATQ3qE` | K-DISC-4; kernel §§2, 9.4 | spec-bug | astra-21 | open | Public aliases for distinct disclosed principals are required but their lookup through the closed policy.handles mapping is unspecified. Define lookup for every disclosed principal by principal-as-subject, exact space and audience. Existing success/missing-row fixtures distinguish aliasing from refusal; no new primitive or authority is needed. |
| R7-011 | astra-22; [ASTRA22-01](impl-astra-22/DIVERGENCES.md) and [first report](impl-astra-22/runs/0.1.0-first.md) at `0216fbb`; event `$q2rmdjcgGsAbigvatBoz_JwexvdtkYlhoOGn0ROjGrg` | S12/B13; K-EVAL-2/5; companion §§4–6 | impl-bug | astra-22 | open | Current-required unavailable/erased root produces complete support search and no cutoff, rather than incomplete + source_unavailable. Judge reproduced exact differences at `bbc1b50`; core simply continues on unavailable non-retained sources. Fix must preserve resolvable/retained/independent controls and hidden-source filtering before budget/cutoffs. |
| R7-012 | astra-22; [ASTRA22-02](impl-astra-22/DIVERGENCES.md) and [first report](impl-astra-22/runs/0.1.0-first.md) at `0216fbb`; event `$0_1Sh7RGoPBXu7yojA34jiGypyl0onIm7AhyodbKP2s` | S12/B13/S32; kernel §6.1/S32; K-EVAL-5 | impl-bug | astra-22 | open | No-witness channels lose authorized unavailable-source associations and report resolvable_now instead of prior_assessment_only, including S32 opposite controls and its forbidden predicate. Judge reproduction agrees. Preserve the vacuous no-source state and never convert signature/documentary association into a signed root or hidden-source leak. |
| R7-013 | astra-22; [ASTRA22-03](impl-astra-22/DIVERGENCES.md) and [first report](impl-astra-22/runs/0.1.0-first.md) at `0216fbb`; event `$Px1j1aY5wn91auk3ubM-DXFIve6l_dMd2oBDI03YRGY` | S23/B03/S28/S29; K-REC-1/2, K-REV-3, K-EVAL-5/9 | impl-bug | astra-22 | open | source_refs omits the exact source for subject-pinned non-root assessments and the authority receipt; polarity/currentness otherwise agree. Judge reproduced each missing list entry. Extend adapter association mapping with visibility intact; mirror attribution must remain noncanonical and no extra semantic root may be minted. |

Every received case is classified against the first landed package. Rejection
means the proposed bad reading already contradicts explicit package clauses; it
does not discard useful implementation regression fixtures. Both independent
full evaluator reports remain pending.

## Judge worklog

### Round 0 — intake and source review

- Completed the required initial pull and identity onboarding as
  `ivmbp_swarma-memory_astra-27`; subscribed to room events for case intake.
- Read the entire R7 mission, decisions, kernel v0.2, companion, and design.
  No project-local skills were present. The CLI's printed a2a skill supplies
  coordination guidance; the mission's narrower ownership, no-spawn, no-board,
  and signed direct-main rules govern this collective.
- `memory/spec/` is absent at the baseline; no `PACKAGE LANDED` marker was
  present in rounds. Source implementer astra-22 has committed its source-only
  reading boundary and work plan at `95f974b`.
- Next: validate the landed release, inventory semantic versus deployment
  vectors, inspect both independent committed runs, classify all received
  items, and track fixes to evidence. Preserve the package implementer's blind
  first-run boundary when addressing it.
- Final gate: finalize the score and verdict, write the park note, push signed
  artifacts and acknowledge only after the convener's PARK marker.

This initial change records process and evidence only; it changes no executable
contract. Its relevant checks are ownership/diff review and signature
verification. Product negative tests wait for the concrete cases and runners;
no passing behavior is claimed from this documentation-only initialization.

Local tool readiness evidence: seat work directory
`.temp/tool-readiness-01.log` (git, Python, rg, a2a). Initial git pull completed
successfully from `6d14828` to `95f974b`; working tree was clean before this work.

### Round 1 — source cases queued for package inspection

Reviewed ASTRA24-01 and ASTRA24-02 in full at `9ecd449`. Both source-level
requirements are supported by the cited contract. Neither is an observed
implementation divergence, and an unreleased/absent package cannot yet decide
whether there is an additional specification bug. Accepted both for release
inspection and package-format fixtures; no owner decision is needed on these
requirements at present. Their negative controls protect against explanation
order altering semantic quality and historical rule qualification overriding
current applicability; neighboring valid paths prevent reject-all behavior.

### Round 2 — publication and attribution source cases

Reviewed ASTRA26-01/02 at `93455d8`. Kernel §9.1 expressly permits source import;
companion §3 separates an attributed report from the reported proposition. An
explicit importer-issued source report therefore needs no invented grant from
its subject, while an actual issuer/submitter mismatch remains governed by §2.
This is a distinction between two submitted record meanings, not permission to
downgrade an unauthorized issuer-A request into an issuer-B observation.

Kernel §9.2 separately requires issuer-version evidence and says that without
it the importer knows only the last state received. §6.3's consumer freshness
horizon cannot supply that missing knowledge. These source-level requirements
need no owner decision; classification of the concrete encoding and output
awaits the package. Both cases include valid controls and forbidden authority
or currentness upgrades. Source evaluator freeze reported at `4d4ef45`, with
20 source-derived controls; no package-vector result exists yet.

### Round 3 — disclosure and erasure source cases

Reviewed ASTRA25-01–04 at `5a32468`. All four recommended constraints follow
explicit normative boundaries: authorized-graph computation, current per-owner
release decisions, content/custody lineage independent of support, and current
restore reconciliation against outside-domain evidence. No source ambiguity
is established by these pairs. The release inspection must distinguish missing
grammar/prose from an actual evaluator defect and from a properly declared
unsupported deployment claim. Synthetic state transitions alone do not prove
real sink deletion, rollback resistance or isolation. The adjacent positive
controls in each case prevent a deny-all implementation from qualifying.

### Round 4 — first package inspection

Acknowledged the convener's PACKAGE LANDED marker and pulled `0ef608a`, package
`0.1.0-draft`. Read all normative semantics and the draft-choice register, plus
domain descriptions and relevant schema/fixture definitions. Ran
`python3 -B memory/spec/checks/validate.py`: exit 0, 90 JSON files, 14 closed
schemas, 14 domain documents, one pilot fixture, 61 vectors (53 semantic / 8
deployment), 49 clauses, and 13 intended checker violations detected. Local
evidence: seat `.temp/package-validate-01.log`. This is structural validation,
not an evidence-evaluator run or deployment qualification.

R7-001–005 and R7-007 are rejected as package defect allegations because explicit
clauses already exclude the bad readings. Keep their implementation regression
value; a subsequent concrete divergence receives its own row. R7-006 is an
actual source/package gap within the editor's assigned v0.2 update. R7-009
records the remaining assigned uplift. R7-008 needs a narrow fixture-boundary
clarification and stale/current controls, not a new restore architecture: the
boolean may stand for an admitted current-completeness fact, but merely being
external or signed cannot establish that fact. All three spec fixes are owned
by astra-21. No source-level ambiguity requiring an owner decision is established.

### Round 5 — first independent run and public-alias clarification

Round-4 publication raced twice with other seats. The required signed bundle
handoff was posted to rounds with SHA-256
`92ecb066d9a43fe2861401581f24aaadd60d89c5f1c4581277e2e66f06e865ca`.
After the convener confirmed retry, a signed rebase landed the same reviewed
scope as `bbc1b50` (signature G); the bundle head is superseded. No force push,
other seat edit, or unsigned commit was used.

Read ASTRA26-03 and its package clauses at `d9336fd`; R7-010 is a narrow grammar
interpretation fix, already sent to the editor. Accepted concrete regressions
for the rejected-as-defect cases are committed by their owners at `ab75dd1`,
`d9336fd`, and `dfc2894`; structural validation is not a behavioral pass.

Read astra-22's first immutable report, divergence notes, runner, and relevant
core/adapter paths at `0216fbb`. At judge checkout `bbc1b50`, independently ran:
`python3 -B memory/conformance/impl-astra-22/run_vectors.py --out ../.temp/astra22-judge-first.md`.
Exit 1 reproduces the seven semantic failures, not a setup error. Semantic
totals: 17 pass / 7 fail / 29 unsupported; deployment: 0 / 0 / 8. A subsequent
comparison verified all 61 statuses, input hashes, exact normalized reports,
field-level differences, totals, and the unchanged frozen-core SHA-256 against
`runs/0.1.0-first.json`. Local evidence: seat `.temp/astra22-judge-first-01.log`,
`.temp/astra22-judge-first.json`, and
`.temp/astra22-judge-first-comparison-01.log`. The runner's five controls passed.

All observed failed fields map to R7-011–013. These are implementation fixes;
the package's expected outputs remain unchanged. Unsupported operations remain
explicit and are not scored as passes, disagreements, or proven package defects.
