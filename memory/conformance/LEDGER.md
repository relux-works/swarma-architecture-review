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
| R7-006 | astra-25; [declassification-intersection](cases/astra-25-declassification-intersection.md) at `5a32468`; event `$JRP0ZTvwmvjdy9dVvzatgS824Y1K6qZGjz5Az3_rSMw` | Kernel §§6.4, 7.1–7.2, 9.3 | spec-bug | astra-21 | fixed@cde5754 | Verified 0.2.0 K-DISC-2, closed decision/owner grammar and extended P05. Judge rerun of astra-23 at 1439219 passes missing-owner atomic refusal, joint release, and current-owner revocation; retained snapshot bytes stay unchanged. Controls independently pass. |
| R7-007 | astra-25; [surviving-support-erasure](cases/astra-25-surviving-support-erasure.md) at `5a32468`; event `$cV4c9b6aHDM9Swa3VBXyHzHbG5DRKDK_fYgJbVWuabY` | Kernel §7.1/P08; companion §6/S12/S20 | rejected | None; astra-25 may retain regression | rejected | `0ef608a` K-ERASE-1 traverses lineage/custody independently of logical edges; K-ERASE-2 makes an unreachable controlled sink incomplete/purge_pending. Runtime custody encodes controlled/reachable/present; K-TIME-1 and K-PUB-1 prohibit erased historical payload delivery. Real deployment remains unqualified. |
| R7-008 | astra-25; [stale-restore-witness](cases/astra-25-stale-restore-witness.md) at `5a32468`; event `$7ed7G5T6VBlEQ1c53ObNr7Ab6sPC9h1GnaD2x8nQ7Nc` | Companion §6/S25; design retention contract | spec-bug | astra-21 | fixed@cde5754 | K-ERASE-3 now defines true as current complete outside-domain verification, and stale/incomplete evidence as false. Judge synthetic B10 comparison passes stale refusal, continued fencing and current reconciliation. Deployment stays unsupported; this closes the meaning gap, not real restore qualification. |
| R7-009 | astra-27 release inspection; convener event `$byrILfhj-Gjsp7famnjMP2EvJbP8t9WBhwRblTS_pGk`; package `0ef608a` | Mission editor scope; kernel v0.2 sections 1, 5.4, 6.4, 7.1, 9.3, P12–P15 | spec-bug | astra-21 | fixed@cde5754 | Reviewed normalized tuple, three conflict outcomes, immutable snapshots/current delivery checks, integration-supplied complete/unknown lineage, per-owner release and versioned projection exclusion. Judge reproduces P12-P15 and extended P05 with negative controls. Distinct B01 authoring omission and P15 attribution defect remain separately tracked as R7-021/022. |
| R7-010 | astra-26; [representative-public-alias](cases/astra-26-representative-public-alias.md) at `d9336fd`; event `$taT2lxQpJoTnfA07PMaF9vPsNbJGZk6O0xGQRWsW400`; decision `$4rnofaDXvrTjC2UMAgpxxn5o_DuPCzwbPN31zATQ3qE` | K-DISC-4; kernel §§2, 9.4 | spec-bug | astra-21 | fixed@cde5754 | K-DISC-4 explicitly applies policy.handles to each disclosed principal, refuses absent aliases and forbids merged mappings. Judge executes both migrated representative-alias fixtures against astra-23 at 1439219: exact pass for distinct alias and missing-alias refusal; schema/checker alias-collision plant also passes. |
| R7-011 | astra-22; [ASTRA22-01](impl-astra-22/DIVERGENCES.md) and [first report](impl-astra-22/runs/0.1.0-first.md) at `0216fbb`; event `$q2rmdjcgGsAbigvatBoz_JwexvdtkYlhoOGn0ROjGrg` | S12/B13; K-EVAL-2/5; companion §§4–6 | impl-bug | astra-22 | fixed@fb7df98 | Judge rerun against pinned 0.1.0: S12/B13 pass with incomplete/source_unavailable, and all 61 statuses/input hashes/actual outputs match the corrected committed report. Source controls cover current/retained/independent requirements, availability variants and hidden-source filtering. |
| R7-012 | astra-22; [ASTRA22-02](impl-astra-22/DIVERGENCES.md) and [first report](impl-astra-22/runs/0.1.0-first.md) at `0216fbb`; event `$0_1Sh7RGoPBXu7yojA34jiGypyl0onIm7AhyodbKP2s` | S12/B13/S32; kernel §6.1/S32; K-EVAL-5 | impl-bug | astra-22 | fixed@fb7df98 | Judge rerun passes S12/B13/S32 with exact empty-channel source associations; no fabricated witness or root. Source controls preserve vacuous no-source behavior, both polarities and hidden-source equivalence. |
| R7-013 | astra-22; [ASTRA22-03](impl-astra-22/DIVERGENCES.md) and [first report](impl-astra-22/runs/0.1.0-first.md) at `0216fbb`; event `$Px1j1aY5wn91auk3ubM-DXFIve6l_dMd2oBDI03YRGY` | S23/B03/S28/S29; K-REC-1/2, K-REV-3, K-EVAL-5/9 | impl-bug | astra-22 | fixed@fb7df98 | Judge rerun passes S23/B03/S28/S29 and the derived-premise source references in ASTRA24-03. Exact assessment provenance avoids unrelated same-origin copies; source and adapter controls verify documentary attribution, hidden filtering and no extra semantic root. |
| R7-014 | astra-24; [mixed-source-state](cases/astra-24-mixed-source-state.md) at `a46eb98`; event `$eIoHp2A9lGbaJ4DePaJMhcl2b_p-wP8voqMVOsjN3bw` | K-EVAL-5, K-RULE-2, K-REC-2/3; kernel §6.1; companion §6 | spec-bug | astra-21 | fixed@f31d58f | 0.2.1 K-EVAL-5 explicitly separates weakest necessary AND from strongest complete OR. Extended S32 direct, mixed and stronger-path controls pass exactly in judge-reproduced astra-23 f5fdd8b; source mixed regression was independently corrected under R7-015. |
| R7-015 | astra-22; [ASTRA22-04](impl-astra-22/DIVERGENCES.md), [case-first report](impl-astra-22/runs/case-first.json) at `b3c7ac9`; event `$OvHSZtZ_OnDnssWZ_HeCEWgQ2WUGsdZya6Wu9jd6qOY` | ASTRA24-03; same clauses as R7-014 | impl-bug | astra-22 | fixed@fb7df98 | Judge supplemental run passes ASTRA24-03 and both stronger-alternative/rule controls. Source controls cover all nine AND source-state pairs plus a stronger complete OR path. Canonical 0.1.0 report is 24 pass / 0 fail / 29 unsupported; unsupported remains explicit. |
| R7-016 | astra-26; [location-slots](cases/astra-26-location-slots.md) at `0c278b5`; event `$eQoI5RcBquCz3xymwrB0I0rS_ybnvNc9tOzeNAXrPuU` | Kernel §§4, 11.2; K-DOM-2/3; location schema | rejected | None; retained regression | rejected | The package explicitly keys single location sequences and incompatibilities by kind/slot. Residence and current location coexist; the flat reading contradicts the declared grammar. Source evaluator reports unsupported, not pass; the scenario remains useful additional coverage. |
| R7-017 | astra-26; [relationship-introductions](cases/astra-26-relationship-introductions.md) at `0c278b5`; event `$ZgkB3vgHDwZo1pwpJZPrV4Wk0IM6-5vDaRslUDCSnaw` | Kernel §11.2; K-SCOPE-1; profiles domain requirements | rejected | None; retained regression | rejected | Existing distinct schemas and no_derived_consent forbid deriving openness from relationship status or granting action from an enabled flag. Explicit enabled=true/adult_opt_in=false remains storable attributed data with no contact effects. No new spec defect; source adapter reports admit unsupported. |
| R7-018 | astra-25; [hidden-dirty-invalidation](cases/astra-25-hidden-dirty-invalidation.md) at `3045117`; event `$Y8BhmZnTDuBgOd71Z8nUDZn7rESyagj1V-VPqysc-h4` | K-EVAL-8 versus K-AUTH-1/K-NI-1; kernel §7.3, companion §4/S24 | spec-bug | astra-21 | fixed@f31d58f | 0.2.1 retains protected unresolved dirty causes and filters revision/target/path eligibility before visible effects. Judge reproduces S24/B07 and migrated hidden/visible adversarial controls with f5fdd8b; global dirty persists while public output stays unchanged and private control remains incomplete/review-required. Unrelated history defect is separately fixed as R7-024. |
| R7-019 | astra-23; [first run](impl-astra-23/FIRST-RUN.md) at `0008dc3`; event `$mGGmzxiZYa6di3hh8P1sCmVbUCjZVm_yc3jKRUsc05k` | B03/S23; K-ENV-3, K-REC-1, K-PUB-2 | spec-bug | astra-21 (clause); astra-23 (alignment) | fixed@f31d58f | 0.2.1 K-PUB-2 keys currentness to authorized publication-source associations. Judge reproduces B03/S23 mirror currentness and unchecked genuine-publication contrast with f5fdd8b; attribution remains noncanonical and no external event is certified. |
| R7-020 | astra-23; [first run](impl-astra-23/FIRST-RUN.md) at `0008dc3`; event `$I0tMpcP1ctw6Uco1iMi0_ElgUiDZ09Y86eiYgF7W0Gk` | S30; K-EVAL-3; closed view corpus_coverage shape | impl-bug | astra-23 | fixed@1439219 | Judge reproduces the complete 0.2.0 report and S30 now passes. Product control verifies exact declared ref and unknown coverage; replacing ref with declaration triggers both the exact-field comparison and closed-view-schema rejection. FIRST-RUN artifacts unchanged. |

| R7-021 | astra-23; [B01 divergence](impl-astra-23/DIVERGENCES.md) at `1439219`; event `$ej8DWxYS8jYpwc8WvM3_qATyIHrZ9DtPhPRSMP_rSmI` | B01; K-DISC-1 | spec-bug | astra-21 | fixed@f31d58f | 0.2.1 supplies B01 exact revision integration fact without changing semantic expected output. Judge rerun passes B01; omission control still returns invalid_reference with unchanged state, positive control succeeds, and package checker detects the original omission for its intended reason. |
| R7-022 | astra-26; [foreign-self-declaration](cases/astra-26-foreign-self-declaration.md) at `4b5d034`; event `$LFCNfaFCUty4LXmmxpSWyukWTQC8nhjAmkocbEFA9Hw` | P15; K-ENV-1/3, K-REC-1; kernel §§2, 4, 8, 11.2 | spec-bug | astra-21 | fixed@f31d58f | 0.2.1 explicit subject_principals plus own perspective govern self attribution; P15 is correctly typed as organisation facts. Judge f5fdd8b run passes P02 wrong-subject/valid distinct-binding, P10 delegated admission, P15 unchanged exclusion and ASTRA26-06. Initial-state and equal-spelling-without-binding controls reject. Newly mapped source admission defect is separately R7-026. |

| R7-023 | astra-24 [derived-source-refs](cases/astra-24-derived-source-refs.md) at `fb00b35`, astra-23 supplemental report; events `$7UDumulp6n1Yh6BKA4PimUs-cFL2shg1GIRRBmlSoDw`, `$JC4s7_UyfP-jBJGDKUt2Wh2NG8ZUYvSeVZbP7ASaF9k` | ASTRA24-03/04; K-EVAL-1/3/5; companion §§4, 7 | impl-bug | astra-23 | fixed@7c765fe | Judge reproduces exact ASTRA24-03/04 passes with implementation 7c765fe and pinned 0.2.0 grammar; all 65 canonical rows match the committed report. Ten checker/product controls pass, including direct/derived source refs, hidden source, unfound path and unrelated same-origin copy. Audience redaction remains after provenance collection; frozen red evidence is preserved. |

| R7-024 | astra-23; [0.2.1 first report](impl-astra-23/RELEASE-0.2.1-FIRST.md) at `bc342e1`; event `$Fey2TsAQS9NPAEPYE4vPLTQTOluGysxk-1N5UIpjk7E` | B07/S24; K-EVAL-9, K-REV-1 | impl-bug | astra-23 | fixed@f5fdd8b | Explicit rec:a target collected unrelated multi-sequence rec:hidden/1 history. Judge independently reproduces 55/57 pre-fix and 57/57 corrected reports, matching all 65 rows and implementation hashes. Exact sequence filtering preserves unfiltered history, explicitly displayed historical targets and hidden-reference exclusion; 13 checker/product controls pass. |
| R7-025 | astra-27 static source probe; event `$NFG9lnMN_Ql0SjgWplmeYuSgEls8vZ1lCHuf8uJ-9YA` | Explicit-target history; K-EVAL-9, K-REV-1 | impl-bug | astra-22 | open | Judge reproduces on 8b97e1e using a valid static multi-sequence state, without dirty/runtime operations: target rec:a wrongly lists other-sequence/1. Unfiltered positive control lists it correctly; an explicit old target does not duplicate its displayed ref. Exact source/queries/outputs and intended lists are in seat .temp/astra22-selected-history-probe-02.json; closed state shape and references pass. |
| R7-026 | astra-22; ASTRA22-05 first 0.2.1 transaction run; event `$PG171V9oI4Um_5wsJuSNRTlfqsd3ZQUSf1kWxDG5Ku4` | P02; K-ENV-1 subject_principals | impl-bug | astra-22 | open | New transaction mapping reports acceptance of wrong-subject self-declaration instead of invalid_domain_value, with extra committed state affecting the valid control cut. Explicit released identity requirement determines classification; committed report reproduction is pending. Require atomic wrong-subject/equal-spelling-without-binding rejection, valid distinct binding and valid represented-self controls. |

Every received case is classified against its cited package release. Rejection
means the proposed bad reading already contradicts explicit package clauses; it
does not discard useful implementation regression fixtures. Both independent
first reports are committed and reproduced. Fix closures below reference exact
commits and relevant controls; a candidate release alone is insufficient.

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

### Round 6 — mixed witness qualification and remaining profile scenarios

Reviewed ASTRA24-03 and ASTRA22-04 together. The source contract requires scoped
attestation and every AND premise; a witness for A cannot remove C's necessary
dependence on retained-only B. K-EVAL-5's preference between alternative complete
paths must not be applied to a flattened union of their individual premises.
R7-014 closes that package algorithm; R7-015 tracks the observed implementation
upgrade. An authorized source-state summary may be conservative, but cannot
advertise a sufficient independent/current path that does not exist. No owner
architecture decision is required for this qualification boundary.

At `a17c231`, judge execution of the proposed ASTRA24-03 fixture reproduced all
five reported differences: two existing R7-012 fields, a derived source_refs
omission extending R7-013, and the incorrect C source state plus its forbidden
predicate (R7-015). Local output is seat
`.temp/mixed-source-state-probe-01.json`; the proposed fixture was not silently
treated as an already-released canonical vector. R7-013's fix also covers
authorized provenance from found premise paths, without exposing hidden inputs.

Read both newly submitted profile regressions at `0c278b5`. R7-016/017 reject
their bad readings as already forbidden; their scenario coverage is retained.
All source fixes preserve the immutable first-run report. Editor acknowledgments
confirm R7-006/008/010 are being addressed in the next release.

### Round 7 — package-only first run and hidden invalidation

Independence boundary: astra-23 committed its complete first run and evaluator at
`0008dc3` before reading design/companion/notes/inputs, other implementation,
ledger or divergence threads, as stated in its worklog/verdict. Its 0.1.0 run
has 50/53 semantic passes, three failures, zero semantic unsupported; all eight
deployment cases are unsupported. The judge reconstructed the exact old package
from `git archive 0ef608a memory/spec` into its own scratch directory, then ran:
`python3 -B memory/conformance/impl-astra-23/run_vectors.py --spec-root ../.temp/package-0.1.0/memory/spec --package-commit 0ef608ae279a9bc209ad78ffdc72dbbbdc828f8f --output ../.temp/astra23-judge-first.md`.
Exit 1 reproduces the reported semantic failures. All 61 statuses, vector and
implementation hashes, exact differences/check failures and complete actual
reports match after only declared fresh-handle normalization. Evidence: seat
`.temp/astra23-judge-first-01.log`, `.temp/astra23-judge-first.json`, and
`.temp/astra23-judge-first-comparison-01.log`. B03/S23 expose the package's
publication-class applicability gap (R7-019); S30 is a closed-field implementation
error (R7-020). Neither justifies changing expected answers to match a runner.

Reviewed ASTRA25-05 in full. Source non-interference takes precedence over the
package's global dirty shortcut; invalidation is not an authorized disclosure
of a hidden revision. Both hidden and visible control vectors passed the judge's
independent shape/reference/normalization checks; replacing the hidden result
with the visible dirty result was rejected specifically for unequal normalized
outputs. Evidence: seat `.temp/hidden-dirty-case-review-01.log`. R7-018 is a
spec contradiction, not a measured evaluator failure or timing claim.

Package `0.2.0-draft` landed at `cde5754`: structural validator exit 0, 94 JSON
files, 65 vectors (57 semantic / 8 deployment), 52 clauses and 16 intended
checker controls. Log: seat `.temp/package-validate-02.log`. The editor reports
candidate fixes for R7-006/008/009/010; behavioral verification and exact delta
review remain pending, so these rows are not yet marked fixed. R7-014 is accepted
for the next release. The original 0.1.0 reports do not claim a 0.2.0 run.

### Round 8 — verified corrections and new v0.2 fixture defects

Reviewed source correction `fb7df98` without changing the immutable first report.
At judge checkout `119b25f`, ran the corrected adapter against all 61 vectors of
an exact `git archive 0ef608a memory/spec` copy. All statuses, input hashes,
normalized actual reports and differences match committed RESULTS.json: semantic
24 pass / 0 fail / 29 unsupported, deployment 8 unsupported. Supplemental inventory
at that checkout: 3 pass / 0 fail / 13 unsupported, separately from canonical
counts. Its three supported cases are ASTRA24-03 (mixed AND/stronger OR), ASTRA24-02
(rule expiry), and ASTRA26-02-CONTROL (checked publication currentness). Source controls: 24 passed; adapter visibility
control: 1 passed; harness controls: 5 passed. Closed R7-011/012/013/015.
Evidence in seat scratch: `.temp/astra22-judge-fixed-canonical-01.json`,
`.temp/astra22-judge-fixed-adversarial-01.json`,
`.temp/astra22-judge-fixed-comparison-01.log`,
`.temp/source_checks-judge-fixed-01.log`, and
`.temp/adapter_checks-judge-fixed-01.log`. The direct Python driver imports the
same Adapter/compare functions, passes only state/operations/query to execution,
and keeps the pinned external package outside other seats' owned directories.

At checkout `1439219`, independently ran the package evaluator against canonical
`0.2.0-draft` (`cde5754`): 54 pass / 3 fail / 0 unsupported semantic, 8 unsupported
deployment. All 65 report rows, vector hashes, implementation hashes and complete
actual outputs match committed RESULTS after only declared fresh-handle
normalization. Four checker and five product controls pass. Closed R7-020.
Evidence: `.temp/astra23-judge-020.md` / `.json`,
`.temp/astra23-judge-020-01.log`, `.temp/astra23-judge-020-comparison-01.log`,
`.temp/test_controls-judge-020-01.log`, `.temp/test_semantics-judge-020-01.log`.

Reviewed 0.2.0 prose/schema/checker delta and reproduced P05/P12-P15. Both migrated
public-alias cases pass exact comparisons. B10 was separately exercised only as
a synthetic transition model: stale witness refusal and current reconciliation
match; no deployment pass is added. Evidence:
`.temp/astra23-judge-020-fix-controls-01.json`. These checks close
R7-006/008/009/010. The package evaluator's B01 failure exposes a missing mandatory
revision integration fact (R7-021); its isolated negative and positive control
both pass. ASTRA26-06 identifies incorrectly typed organisation attestations in
P15 (R7-022). These narrower remaining defects are not hidden by closing the
v0.2 uplift. Both are source-determined package corrections, not owner choices.

Five spec bugs remain open: R7-014/018/019/021/022. There are no open implementation
bugs or established owner questions at this round. Score stays 1/2 until package
corrections and both same-release runs satisfy the rubric. A failed initial file
search used a nonexistent profiles directory; the successful follow-up inspected
the actual profiles-synthetic path. No validation relied on that failed read.

### Round 9 — same-release baseline and derived provenance

At judge checkout `dcde639`, reviewed source evaluator extension `8b97e1e` and
reran canonical 0.2.0. The report matches committed package version/commit, core
hash, totals and every vector row exactly: semantic 29 pass / 0 fail / 28
unsupported; deployment 8 unsupported. Source controls 25, adapter controls 2,
and runner harness controls 5 pass. New supported read paths cover declared
incompatibility, audience aliases/redaction and versioned exclusion. Evidence:
`.temp/astra22-judge-020.md` / `.json`,
`.temp/astra22-judge-020-comparison-01.log`,
`.temp/run_vectors-judge-020-01.log`,
`.temp/source_checks-judge-020-01.log`, `.temp/adapter_checks-judge-020-01.log`.
Both independently verified current reports now target package `cde5754`.

Reviewed ASTRA24-04 and astra-23's same defect report. Executed current 0.2.0
cases with package implementation `1439219`: ASTRA24-04 has two exact source-ref
field differences and both intended paired/forbidden checks; ASTRA24-03 has four
source-ref differences while its source-state controls agree. Classified one
implementation defect R7-023; the first-run matched old-package evidence remains
historical evidence, not a claimed new-release run. Also reproduced ASTRA25-05's
14 hidden-dirty field differences, paired inequality and two forbidden checks;
the visible dirty control passes. This extends R7-018 evidence without charging
an implementation for following the package's contradictory global instruction.
The current ASTRA25-02 joint-release/wrong-owner-revoke/correct-owner-revoke fixture
passes exactly. Evidence: `.temp/astra23-judge-round9-cases-01.json`.

Five spec bugs and one implementation bug remain open. Editor acknowledgments
accept R7-021 and R7-022 for the next release. All directed findings have decisions
or closure replies. A source-closure reply initially used a nonexistent topic;
no message was delivered there, and the reply was sent to the actual
`div-astra22-current-source` topic after listing topics. No missing delivery is
assumed successful.

### Round 10 — 0.2.1 candidate review and derived-reference closure

Read the full normative/schema/checker delta of `0.2.1-draft` at `f31d58f` and
RELEASES.md. Independently validated 94 JSON artifacts, 14 closed schemas,
65 vectors (57 semantic / 8 deployment), 52 clauses and 20 intended checker
violations. Reviewed targeted expected traces for B01, S23/S24, B07, S32,
P02/P10/P15. The candidate corrections match R7-014/018/019/021/022: necessary
AND versus alternative OR source states, unresolved authorized dirty causes,
actual publication associations, B01's missing fact, and explicit self identity
with separately typed organisation assertions. Positive and negative controls
remain distinct. Evidence: `.temp/package-validate-03.log` and
`.temp/package-021-targeted-review-01.json`. These five rows stay open pending
exact-release independent behavioral evidence, not merely a green validator.

Reviewed the three-line provenance correction in astra-23 `7c765fe` and its
regression controls. Constructed an isolated judge scratch copy of the exact
0.2.0 package at `cde5754`, and the implementation/cases at `7c765fe`, using
standard-library extraction of git archives. No other seat's files were edited.
Both ASTRA24-03 and ASTRA24-04 pass exact reports, forbidden and paired checks;
four checker and six product controls pass. All 65 canonical rows, hashes and
actuals match the committed report after declared fresh-handle normalization:
54 pass / 3 fail / 0 unsupported semantic, 8 unsupported deployment. Those three
old-release failures remain the already-classified package defects, not a
regression. Closed R7-023 fixed@7c765fe. Evidence:
`.temp/astra23-judge-r7023.md` / `.json`,
`.temp/astra23-judge-r7023-comparison-01.json`,
`.temp/astra23-judge-r7023-cases-01.json`,
`.temp/test_controls-judge-r7023-01.log`,
`.temp/test_semantics-judge-r7023-01.log`.

An attempted report read used an absent version-suffixed filename; the exact
report subsequently read and compared is SUPPLEMENTAL/RESULTS under the pinned
archive, not an assumed successful read. Current ledger: eight rejected,
ten fixed, five open spec bugs, no open implementation bugs or owner questions.

### Round 11 — package behavior verified; selected history and source identity

Read astra-23's complete 0.2.1 adaptation and selected-history correction. Using
an isolated git-archive copy of `bc342e1`, independently reproduced its immutable
first release report: 55 pass / 2 fail / 0 unsupported semantic. Both failures
are only the private capture historical list in B07/S24. K-EVAL-9 already limits
history to selection sequences; K-REV-1 distinguishes multi assertion IDs.
Classified R7-024 and reproduced corrected `f5fdd8b`: 57 pass / 0 fail / 0
unsupported semantic. All 65 rows, input and implementation hashes, differences,
checks and normalized actual reports match both committed reports. Four checker
and nine product controls pass. Deployment remains 8 unsupported. Evidence:
`.temp/astra23-judge-021-first.md` / `.json`,
`.temp/astra23-judge-021.md` / `.json`,
`.temp/astra23-judge-021-comparison-01.json`,
`.temp/test_controls-judge-021-01.log`, `.temp/test_semantics-judge-021-01.log`.

The current supplemental run has 15 semantic passes, no failures, four explicitly
unsupported old-grammar semantic cases, and one unsupported deployment case.
Migrated hidden-dirty, joint-release, foreign-self and alias controls all pass.
No implicit fixture conversion was used. Evidence:
`.temp/astra23-judge-021-supplemental.md` / `.json`. Closed the five package
corrections at `f31d58f` and R7-024 at `f5fdd8b`; no package bug remains open.

Source adapter inspection revealed the same selected-history omission. An initial
S09 probe was unsuitable: its query preceded correction and its domain was single,
so it established no defect. The successful independent probe starts from S24's
initial multi-domain state, adds a separate sequence's two versions and visible
replacement plus exact direct integration facts, and performs only reads at the
existing cut. Full closed-state and reference checks pass. Explicit rec:a
incorrectly includes the other sequence's old version; unfiltered and explicit-old
positive controls behave as specified. Persisted exact witness:
`.temp/astra22-selected-history-probe-02.json`. R7-025 is a separate fix owner
from R7-024; astra-22 received the full artifact path and controls.

Astra-22's expanded transaction first run reports a missing new identity check
in P02. R7-026 is an implementation mapping omission under explicit K-ENV-1,
not a reopening of source identity or a package defect. Its first report must be
committed before correction and independently reproduced. Current ledger has
26 items: eight rejected, sixteen fixed, two open implementation bugs. The score
remains 1/2 pending those source corrections and its exact 0.2.1 run.
