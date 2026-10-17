# R7 divergence ledger

Sole writer: astra-27 (judge). Contract: `memory/MISSION-R7.md`.
Initial review baseline: `95f974b41667e25d4a3a7630055ef1c20690fb7d`.
Final status: **PARKED**, 2026-10-17 19:12Z.
Final score: **2/2**, with dual 66/66 canonical semantic coverage on 0.2.6.
59 items: 48 fixed, 10 rejected, one ambiguity resolved by D-009 (R7-055).
No open specification/implementation finding or owner question remains.

## Review contract

Apply source precedence in `memory/designs/kernel.md`: owner decisions D-001–D-009,
kernel v0.3, normative companion, then bounded-evidence design. Do not reopen
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
| R7-025 | astra-27 static source probe; event `$NFG9lnMN_Ql0SjgWplmeYuSgEls8vZ1lCHuf8uJ-9YA` | Explicit-target history; K-EVAL-9, K-REV-1 | impl-bug | astra-22 | fixed@26d8cc6 | Judge independently reruns the exact static fixture with 26d8cc6: unrelated explicit target excludes other history, unfiltered selection preserves it, explicit old target is not duplicated, and hidden-old control is excluded. Three adapter controls pass; canonical report matches all 65 rows. Owned fixture and red/green reports are retained under impl-astra-22/fixtures and runs. |
| R7-026 | astra-22; ASTRA22-05 first 0.2.1 transaction run; event `$PG171V9oI4Um_5wsJuSNRTlfqsd3ZQUSf1kWxDG5Ku4` | P02; K-ENV-1 subject_principals | impl-bug | astra-22 | fixed@26d8cc6 | Judge reproduces df499a1 P02 forbidden admission and all 15 difference paths, then exact 26d8cc6 canonical pass with identical refusal state and valid distinct/delegated controls. Seven transaction controls pass, including wrong subject, equal spelling without binding and non-own perspective rejection. First failure report is preserved. |

| R7-027 | astra-25 [quality-budget-isolation](cases/astra-25-quality-budget-isolation.md) at `2a6d294`; astra-24 [polarity-budget](cases/astra-24-polarity-budget.md); events `$M-2IsLpo2I6lijkllP1qvqkD95XnpbXccbAHHCtSt64`, `$Dp4_riQyF6haSd2qyOmKMURbHNt2rkZrFJBDw9-Ctlw` | ASTRA25-06, ASTRA25-01 visible control, ASTRA24-05; K-EVAL-2/4 | impl-bug | astra-22 | fixed@4e647ea | Independent judge rerun passes all three regressions, exact canonical report (43 pass / 0 fail / 14 unsupported semantic) and 44 source/adapter/transaction/harness controls. Fresh per-channel and quality walks preserve local memoization, numeric reference ordering and genuine zero/insufficient limits. The distinct missing source bound persists as R7-028; hidden equality alone was never treated as proof of this fix. |
| R7-028 | astra-24 [source-resolution-budget](cases/astra-24-source-resolution-budget.md) at `67b1e06`; decision `$_nHN4l4lurg4x7z88Ie7my2bKrY65tHxu33Tb4NG5j8` | ASTRA24-06; K-EVAL-1/2/3/5 | impl-bug | astra-22 | fixed@c923ebd | Judge reproduces exact zero/one/provenance passes and all canonical rows/hashes. Distinct current-required source members are charged per independent walk with min(query, policy), repeated-source memoization and retained/independent exemptions. 48 controls pass at this fix; current supplemental inventory is 14 pass / 0 fail / 8 unsupported semantic. Original eight-field/three-forbidden failure remains preserved. |
| R7-029 | astra-22 [vacuous first probe](impl-astra-22/fixtures/independent-vacuous-source-first.json) at `f2d233a`; independent judge [nonempty pair](impl-astra-22/fixtures/independent-resolvable-judge-first.json); decision `$R6pEZvOBTW2UVbOfj04NRa4KfMIWwHX2EYq2GMksDS4` | ASTRA22-07; S32 neighbors; K-EVAL-5 | impl-bug | astra-22 | fixed@512d006 | Judge reproduces only the intended support.source_state change for empty/resolvable sources, with unavailable control, evidence kind and input state unchanged. All canonical/supplemental rows and hashes match; 50 source controls pass. Package implementation remains green with its independently authored 12-subcase control, 14 total controls. The source-resolution limit and retained/current neighbors remain enforced. |


| R7-030 | Judge [snapshot-idempotency probe](impl-astra-22/fixtures/persisted-idempotency-judge-first.json), first reproduction `f2c1570`; decision `$hbbJ9rJ7PJw8UKe81INSkYADsT_zK_WLJPPHBW3fgtQ` | S14 neighbor; K-API-1/2; companion §7 | impl-bug | astra-22 | fixed@1f3180d | Judge reproduces exact original receipt/handle replay across intake timestamps and changed-intent conflict, with full state unchanged. Authoritative runtime.idempotency now supplies initial and newly committed entries. Eleven transaction controls cover reconstruction, original time, actor/space/key isolation and current authorization; canonical report matches exactly. Original failure retained. |
| R7-031 | astra-25 [erasure-receipt-metadata](cases/astra-25-erasure-receipt-metadata.md) at `77ea085`; initial decision `$JPPhod2ZE3Dm7yPZZY1gOh8KGSHsO6j0Fi33ewipx7o` | ASTRA25-07; K-API-1 versus K-ERASE-2; companion §§4/6 | spec-bug | astra-21 | fixed@7e71765 | 0.2.2 supplies actor-bound explicit receipt_context, pre-fence metadata filtering and current-authorized exact replay without reducing protected closure. Judge verifies runtime a016781: canonical 57/57, all 18 controls, exact primary/authorized/other-purpose cases and state-preserving revoked replay. First 0ca2d27 red run retained. |
| R7-032 | astra-26 [checked-import-expiry](cases/astra-26-checked-import-expiry.md) at `837591e`; decision `$d-fCrpCafaGdZmlnjrNnqpKXqFOs7Um-npNJhPU8IJ8` | ASTRA26-07; K-PUB-2, K-EVAL-6; kernel §9.2 | impl-bug | astra-22 | fixed@1f35727 | Judge exactly reproduces all 65 canonical rows/hashes on 0.2.2: 45/0/12 semantic; S23 and unchanged semantic expiry case pass. Eight adapter controls preserve before/at/after, missing/unverified/replaced distinctions, ordinary source currentness, origin identity and immutable capture. First failure remains f2c1570; deployment remains unsupported. |
| R7-033 | astra-26 [checked-import-expiry](cases/astra-26-checked-import-expiry.md) at `837591e`; same initial decision as R7-032 | ASTRA26-07; same clauses as R7-032 | impl-bug | astra-23 | fixed@f10c7ba | Judge reproduces exact case pass and canonical 57/57 with every report row/hash matching after declared normalization. Before/at/after, missing-check, replacement, ordinary-document, unchanged evidence and immutable capture controls pass. First failure preserved at f83268d; source counterpart R7-032 remains independently tracked. |
| R7-034 | astra-26 [excluded-forward-right](cases/astra-26-excluded-forward-right.md) at `837591e`; decision `$4Zjns7pfNlPx6xuWQDRPHjvue4q-WXj_leO7bI0HshY` | ASTRA26-08; K-PUB-1, K-SNAP-1, K-PROJ-2 | impl-bug | astra-23 | fixed@f10c7ba | Judge reproduces both unchanged fixtures after exact selected-binding iteration. Selected read/use/forward removal, erasure fence, stale horizon and later revocation still refuse with unchanged state. Twelve product plus four checker controls pass; first incorrect refusal remains preserved at f83268d. Source operation is still unsupported at this reviewed baseline. |
| R7-035 | astra-24 [cartesian-proofs](cases/astra-24-cartesian-proofs.md) at `4e5d063`; decision `$UZdvnT7Rr6M6qyXZtyxf8uTE5OE3ivlwsPrlANzmCnw` | ASTRA24-07; K-EVAL-2/3/7 | rejected | None; retained regression | rejected | No defect was alleged or observed. Exact proof-reference sets and independent-origin sets are already explicitly different objects. Judge validates/reproduces four Cartesian proofs, exact cap-three truncation and two independent roots with unchanged complete evidence in package evaluator. Original source at 512d006 reported unsupported; judge verifies exact source pass at 4960d24 with four proof controls and canonical S07 pass. |


| R7-036 | astra-25 [retention-authority](cases/astra-25-retention-authority.md) at `2de226c`; decision `$pnqSyjGB7fzLv1dlK42vnCpvbXn2OS6hR2BAL5a-818` | ASTRA25-08; K-AUTH-1, K-DISC-1, K-API-1; companion §6 | impl-bug | astra-22 | fixed@d077064 | Round22 independent 0.2.3 canonical49/0/8 and supplemental37/0/9 match every committed input, normalized output and source hash. All89 source/product/harness controls pass, including eight new scoped-retention groups and all four original/transitive-unknown fixtures. Denial preserves records/runtime/policy and original receipt; metadata=false, exact input spaces, same-batch order, unknown lower bounds and current replay are covered. Unsupported source declassification remains a separate coverage gap. Decision $3mZqw6AM65j28W9NIr5SMhxgW6mF7IP2ykjcDuASILs. |
| R7-037 | astra-25 [retention-authority](cases/astra-25-retention-authority.md) at `2de226c`; same decision as R7-036 | ASTRA25-08; same clauses as R7-036 | impl-bug | astra-23 | fixed@4af0360 | Round22 independent 0.2.3 canonical57/57 and supplemental46/46 match all module/input hashes and expected outputs. Twenty-two product plus four harness controls pass; all four write APIs have atomic scoped denial, same-key recovery, exact original receipt and revoked replay checks. Future inputs, transitive unknown lower bounds and empty-label storage pass. First5416283/6861fec failures remain. Abbreviated producer package SHA resolves to the exact full release SHA. Decision $R1C7Xuq-cq3qtF4fctBsxmVdWtwwHIprLaYgX5e8HVI. |
| R7-038 | astra-25 [unknown-lineage-erasure](cases/astra-25-unknown-lineage-erasure.md) at `5d686fd`; decision `$Gfb8hRoyoU6bjoszyLeRlFn2ss9BBGiDTXjcxGzfih8` | ASTRA25-09; K-DISC-1, K-ERASE-1/3; kernel §7.1 | rejected | None; retained regression | rejected | No defect established: unknown lineage already retains known integration lower bounds for closure and late-write fencing. Judge validates/reproduces exact package passes for erased-input refusal and independently sourced private-unknown admission, with full original closure/purge. Source erase remains explicitly unsupported; retain pair for expanded source verification. |

| R7-039 | astra-22/23 scoped-retention requests; [package implementation analysis](impl-astra-23/DIVERGENCES.md) at `1828356`; editor concurrence; decision `$DgdmzXqH-rajfv36DacN6RQfHAQ3H45tTew6Xha8Qls` | K-AUTH-1/K-DISC-1/K-API-1; source explicit retention purpose | spec-bug | astra-21 | fixed@23290b3 | Judge round21 verifies explicit actor-bound retention_context for all four write variants, exact output/transitive known-input retain scope, independent onward labels, retain revocation and current-authorized replay. All94 artifacts regenerate exactly; 32 checker plants pass; onlyP11/P13 expected reports change beyond profile stamps. Isolated authorized traces match every field. Full runtime red results stay under R7-036/037. Decision $rWp5wPxg_ZSHpHlPAYbWHZgUK-mIqtBiiAYXTLlsLm8. |

| R7-040 | astra-24 [ambiguous-cas](cases/astra-24-ambiguous-cas.md) at `09f2d4d`; judge remaining-head probe | ASTRA24-08 family; K-REV-1/3/4 | impl-bug | astra-22 | fixed@99b5a85 | Round21 independently verifies all five unchanged CAS fixtures, including NEXT, against exact0.2.2/7e71765; 14 transaction controls pass with ordinary-record tokens and exact-replay precedence preserved. Canonical49/0/8 and every module hash match the pinned report. Original failures e38c37c/5d079be/bd75f4f and invalid judge setup remain preserved. Decision $tmfi_3vaCFABPnbEDIekguKbs5okvS5uAK-igNNYZng. |
| R7-041 | astra-24 [ambiguous-cas](cases/astra-24-ambiguous-cas.md); first `e525612`, closure `$wmXkAgaK-ZXUKfAoCetFXutHCU3khC2bHB5CGXyzF0Q` | ASTRA24-08 family; K-REV-1/3/4 | impl-bug | astra-23 | fixed@53266dd | Judge verifies all four unchanged cases, native atomic state/dirty checks, exact replay, changed intent, arrival-order independence and remaining-head withdrawal, including separate validated d3-then-d2 probe. Canonical 57/57 exactly matches all rows/hashes; 19 controls pass. Source counterpart remains independently open. |

| R7-042 | astra-25 [future-lineage-input](cases/astra-25-future-lineage-input.md) at `cacd82c`; decision `$GMbY9p6_pemnZ4YJ4kSkLz6M9eJTAjloeXsRPKzFrmA` | ASTRA25-10; K-DISC-1, K-API-1/2, K-VEC-1 | spec-bug | astra-21 | fixed@23290b3 | Round21 independently accepts migrated ASTRA25-10 and existing-A control, while admitted complete/unknown B missingA, accepted B without earlier A, duplicate future inputs and direct-nonempty facts still fail for their intended reasons. Same-batch later-input P13 passes. All32 checker plants and exact regeneration pass. Original0.2.2 false positive remains. Decision $VnpOe2mi3GgXbmhsUHB1BX-Eu0mxKhwbHU7aOMnsqIk. |

| R7-043 | Judge S17-derived rule/certificate withdrawal probes; source impact implementation `e38c37c`; decision `$lXcUN46jxrVt_c0amm5LNbwyvqnzNvPyTOc6omMPOmk` | K-EVAL-8, K-API-1; companion §5 | impl-bug | astra-22 | fixed@3722327 | Round21 reproduces correction with byte-identical impact code at99b5a85 on frozen0.2.2. All three original judge input hashes match and all exact vectors pass; nine impact controls cover hidden/challenge, transitive/history/recompute and zero-budget neighbors. First failure4744e62 remains immutable. Decision $7SPv0fhusw6LBCA4fpiCUg1pBXhDn87JlV2hcPupTDw. |

| R7-044 | astra-26 [import-check-coverage](cases/astra-26-import-check-coverage.md) at `03a0f85`; package first `08c4b9a`; decision `$Y8OHdh7iDMe_LPy7R9JzU80dB6gLZcU1j9HGQrDTFcg` | ASTRA26-09; K-PUB-2, K-DISC-3 | impl-bug | astra-23 | fixed@f6c339d | Round21 independently reproduces all three unchanged exact-publication-check fixtures, canonical57/57 with identical full module hashes, and18 product plus4 harness controls. Every missing exact check, hidden source and explicit-unverified/current neighbor is covered. First08c4b9a remains. Decision $G--edKuqkU1ptO6Zc7tC1mISY_NZF-JzmmRuXO1ky_k. |
| R7-045 | astra-24 [transitive-review](cases/astra-24-transitive-review.md) at `783b83a`; package first `08c4b9a`; decision `$w6ki9VdtqJ2t1FPa6C95Bnv2-P6BadtH6uI0_zpHFhY` | ASTRA24-09; K-EVAL-8, K-RULE-2 | impl-bug | astra-23 | fixed@f6c339d | Round21 independently passes unchanged ASTRA24-09 and transitive/cyclic/mixed review, hidden-path and no-review controls. Finite eligible closure preserves a review obligation along paths containing a review edge; sufficient/documentary-only paths do not invent it. Canonical57/57 and22 controls pass; first08c4b9a retained. Decision $FUaN_53BaXJmAS0URtEd8DTcbnlzmmLxJ_z4s3DG0yk. |
| R7-046 | astra-26 [delivery-actor-binding](cases/astra-26-delivery-actor-binding.md) at `3c69193`; decision `$g9ovpw6DYL8Zlps7PFLbTJ48DFO_AnuBgVT9hrvJ5tA` | ASTRA26-10; K-AUTH-1, K-API-2, K-PUB-1, K-SNAP-1 | impl-bug | astra-23 | fixed@3ce8ee3 | Round22 exact original 0.2.2 actor trace and native actor/audience/purpose/index controls pass against archived3ce8ee3. Migrated0.2.3 trace and complete current suite pass at4af0360. Wrong binding preserves state/captures/protected bindings/dirty-since, while rightful delivery and selected-right revocation stay exact. First5416283 retained. Decision $yjV0b8Np4X4WOpR5twcN5bIDbTo9nRpBvX9zWG8QBkg. |
| R7-047 | astra-24; [authority-succession](cases/astra-24-authority-succession.md), inputs/first report at `1a09fb6`; request `$Vq3tZEgKESq_rlmd6oQINVGbpMm2zJmMZdUCiANtpek` | Kernel §5.3; K-REV-3; B01 neighbor | impl-bug | astra-22 | fixed@4772258 | Judge independently reproduces canonical 0.2.3 50/0/7 and original 54-case supplement 44/2/8. Three strict-succession negatives now refuse exactly; direct positive passes. Four native groups verify replace/correct atomicity, direct/transitive writes, plain incomparable import, replay and separate CAS; 14 old transaction controls pass. On 0.2.4 every B01 operation/postcondition matches; final projection remains separate R7-051. First 64ef86e preserved. |
| R7-048 | Same ASTRA24-10; package first `47c0205` | K-REV-3; K-API-1; B01 neighbor | impl-bug | astra-23 | fixed@942bdee | Judge reproduces full 0.2.4 canonical 57/57 and all 54 migrated supplemental semantic cases, matching committed hashes and all exact outputs after declared normalization. All 28 product/checker groups pass; eight replace/correct-by-receipt-class negatives preserve state and allow same-key valid retry. Direct/transitive/plain-import positives, original replay after later head and distinct CAS remain exact. First 47c0205/0641033/e689cf2 preserved. |
| R7-049 | Same ASTRA24-10 refusal-mapping review; judge source/package inspection | K-REV-3 versus K-REF-1 | spec-bug | astra-21 | fixed@ef02647 | Judge verifies 0.2.4 K-REV-3/K-REF-1 exact non-retryable authority_receipt_required mapping, explicit strict ancestry and unchanged CAS/replay/plain-import distinctions. All 94 JSON files regenerate identically; 33 checker plants detect intended violations. Only B01 differs beyond profile stamps; other 64 vectors and pilot bytes unchanged. Source reproduces every B01 write/postcondition; remaining projection and package admission failures stay separate R7-051/048. |
| R7-050 | astra-22; first declassification expansion `36983de`; request `$vyyT5G253v4564j43WBy6W1q1-UlEKCXnkjBmP_jTcg` | K-JSON-2; K-DISC-2; P05 and ASTRA25-02 | impl-bug | astra-22 | fixed@8a42945 | Round24 independently reproduces canonical50/0/7 and every prior supplemental row; all98 source/product/harness controls pass, including nine release groups. Four separately validated ASCII/non-ASCII framed/raw probes now give the required verdicts with atomic raw rejection. Exact ASTRA25-02 and new DIGEST vector pass. First36983de/e1ba8db retained; corrected private-projection setup is explicitly excluded from product failures. Decision `$eKvZRGBlqzKr6xMsLkCJYW-knzBYjX56FZRIIFPlYHY`. |
| R7-051 | astra-24; ASTRA24-10-TRANSITIVE at `72a8f86`; event `$YqrXyQgyL7sx2kB1egs8lyBfJ3Rifkvz6LdkSQ-INbs`; judge read-only isolation | K-REV-3; kernel §5.3 | impl-bug | astra-22 | fixed@427fed5 | Judge reproduces exact full 0.2.4 source canonical 50/0/7 and migrated supplemental 46/0/8, including B01, ASTRA24-10-TRANSITIVE and ASTRA24-11 read-only pair. Receipt ancestry is closed per issuer before mapping exact sequence/space candidates. All 106 source controls pass, including four ancestry groups for longer chains, event permutations, eligible/private/historical candidates, genuine incomparable branches and unchanged read state. First d5f07be/64ef86e and judge read-only failures preserved. |

Rows classify received cases against their cited package release; queued intake
is explicitly recorded in the worklog. Rejection
means the proposed bad reading already contradicts explicit package clauses; it
does not discard useful implementation regression fixtures. Both independent
first reports are committed and reproduced. Fix closures below reference exact
commits and relevant controls; a candidate release alone is insufficient.

| R7-052 | astra-25 [retention-deadline](cases/astra-25-retention-deadline.md), first `604af18`; request `$XkFYu2DEMaA0d8d3wUeCqkwMVrlPAqRQAg0B_ViVOAg` | ASTRA25-11 native probes; K-DISC-1, K-AUTH-1, K-API-1/2 | impl-bug | astra-22 | fixed@4a14a56 | Judge exactly reproduces all 65 canonical 0.2.5 rows at 50/0/7 with correction module hashes and all 112 controls green. All seven migrated expiry vectors pass; independent three-positive/seven-negative operation checks now pass, with exact refusals and complete state preservation. Six native groups cover admit/raw/revise/declassify, every output, transitive/incomplete-known/batch deadlines, original live/expired replay, null/unrelated limits and authorization-before-duplicate priority. First c9e1faf and full old-runtime 0.2.5 failure remain immutable. |
| R7-053 | Same ASTRA25-11 submission and independently repeated inputs as R7-052 | Same deadline and authorized-replay clauses | impl-bug | astra-23 | fixed@23b4d74 | Judge independently reproduces 57/57 canonical and 61/61 current supplemental at 0.2.5 with exact reports/input/module hashes, 31 product/comparer controls and ten original isolated deadline operation checks. All four write APIs, every proposed output/known closure and current original-receipt replay use strict context.at expiry before idempotency. Equal/later fresh/replay refusals preserve full state and original receipts; live/null controls and same-key recovery pass. First failures remain unchanged. |
| R7-054 | Judge review of ASTRA25-11; editor recommendation `$rhmPEMI5yxqbjQprbScOEovbpGlhuBzhcvFNwa--FmA` | K-DISC-1, K-AUTH-1, K-API-1/2, K-REF-1 | spec-bug | astra-21 | fixed@6a04e8c | Judge verifies 0.2.5 explicit strict context.at expiry, not_authorized,false before idempotency, original-output/known-closure replay and no purge. All 94 JSON artifacts regenerate exactly; 34 intended checker plants pass. Only P11 changes beyond version; its first 16 operations/results and other 64 vectors/pilot are preserved. Isolated unchanged-runtime probes give five forbidden writes, two expired success replays and one wrong conflict priority; a separate 20-operation positive trace matches every expected field. Runtime fixes stay R7-052/053. |
| R7-055 | astra-24 [authority-issuer](cases/astra-24-authority-issuer.md), original input/first `4424598`; D-009 at `2c3100d` | D-009; kernel v0.3 §5.3; K-REV-3; S34–S42 | ambiguity | Ivan (decision); astra-21/22/23 (mapping and evaluation); astra-27 (verification) | resolved by D-009 | Judge independently verifies release `77b951e`, source runtime `946cbd8` with report/harness `c7e86d5`, and package correction `5897520`: both 66/66 canonical semantic, including all nine new vectors. Original mixed chain remains ambiguous d1/d3; assertion-free all-H and mixed/direct paths select d3; exact foreign-only pairs preserve order. Replace/correct share the relation and existing refusal codes, with full atomicity and replay/CAS controls. Separate unchanged 0.2.5 historical regression is 68/68 both. Original witness/firsts and package first `1be6026` remain immutable. See [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md). |
| R7-056 | astra-22 ASTRA22-08, signed native first `dbf4892`, [first evidence](impl-astra-22/runs/availability-recovery-first.json); request `$fDDTeYrjnc9MYUG4MHM6u2sw7BII51TC8fX0w9jadOU` | K-NI-3; S27 authorized public availability | impl-bug | astra-22 | fixed@87beb46 | Judge independently reproduces 57/57 canonical, 61/61 supplemental and all 125 native/comparer controls at the signed correction. The unchanged original native witness and four-transition matrix now pass, as do two exact atomic authorization negatives. Only current public/runtime availability facts change; policy pins, grants, records, receipts, cuts and captures remain preserved. Original single-case and expanded-matrix red evidence stays immutable; no deployment claim. |

| R7-057 | astra-22 ASTRA22-09, signed native first `0529814`, [first evidence](impl-astra-22/runs/erase-changed-context-first.json); request `$Jls_nbueo2sF-siMYb-5Xqb_iijrTcnTQ4UT_NDB2gU` | K-API-1/2; K-ERASE-2 | impl-bug | astra-22 | fixed@946cbd8 | Judge independently reproduces all 65 canonical/64 supplemental committed rows: 57/57 and 63/63 semantic, unchanged inputs; 128 source controls pass. Both unchanged 66233ab exact regressions and six original/native neighboring probes now pass with full refusal state and original receipts preserved. Current erase authority precedes changed-intent conflict; stored-ref metadata gates exact replay only. Read/use/metadata loss and immutable empty receipts remain covered. Original 0529814 native and five expanded wrong-code failures are retained. Package 23b4d74 remains conforming. |

| R7-058 | astra-25 [restore-current-obligations](cases/astra-25-restore-current-obligations.md), native first `644c793`, late-writer first `1138c5d`, exact fixtures `1cefcf9`; request `$kmeFdI3d8N1_BZoCMnBcpmZE-Lju4yXDpDMw7N1Zu7k` | K-ERASE-1/2/3; companion §6; bounded-evidence protected-service restore | impl-bug | astra-23 | fixed@104fbe8 | Judge independently reproduces all 57 canonical and 68 supplemental semantic passes plus 34 package controls. Current supplied closure is reconciled with retained erasure coverage, unreachable affected custody refuses atomically, and newly learned obligations update fences/erased/generation before reopening. Original four native traces and three late-writer controls pass; known/empty/repeated recovery and independent content/writes remain valid. Seven intended failures reproduce on the old runtime with the new tests. All original firsts and exact input bytes remain unchanged; only three previously failing exact actuals change. Source 946cbd8 remains conforming with 129 control coverage. |


| R7-059 | astra-22 [0.2.6 first controls](impl-astra-22/runs/d009-0.2.6-controls-first.json), signed `31d77d2`; request `$9UYjA1VRtJOzftlEfi0HtNQXugp52DZ63eOxpSbzQ4I` | Release 0.2.6 version-only migration; ASTRA26-08 pair; boundary_checks | impl-bug | astra-22 (control harness only) | fixed@c7e86d5 | Judge reruns 134/134 source controls and 66/66 canonical semantics. Both explicit copies change exactly two expected semantic_profile labels; original/copy hashes and recursive guards match the committed audit. An illicit query-actor change causes two intended guard failures, no errors. All other 22 modules and source runtime remain unchanged; no behavioral oracle or author fixture changed. First `31d77d2` and every canonical first row remain preserved. |

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

### Round 12 — source identity/history closed; independent quality budgets

Independently reproduced the committed source `df499a1` 0.2.1 transaction first
run: 42 pass / 1 fail / 14 unsupported semantic. P02 has the same 15 difference
paths and forbidden extra write. All 65 statuses and input hashes match. Two
literal report values differ: the wrongly returned random receipt handle and
its recorded diff value. That unexpected handle is outside declared normalization;
it is not silently normalized or described as literal equality. Every other
stored actual field matches. Existing five transaction controls pass.
Evidence: `.temp/astra22-judge-021-first.md` / `.json`,
`.temp/astra22-judge-021-first-comparison-01.json` (literal comparison false),
`.temp/astra22-judge-021-first-comparison-02.json` (exact mismatch paths and limit),
`.temp/transaction_checks-judge-021-first-01.log`.

Reviewed source fix `26d8cc6` and independently reran the canonical package:
43 pass / 0 fail / 14 unsupported semantic; 8 unsupported deployment. All 65
rows, package/core hashes, normalized reports and totals exactly match committed
RESULTS. Source controls 25, adapter controls 3, transaction controls 7 and
harness controls 5 pass. Closed R7-025/026. Evidence:
`.temp/astra22-judge-021-fixed.md` / `.json`,
`.temp/astra22-judge-021-fixed-comparison-01.json`,
`.temp/source_checks-judge-021-fixed-01.log`,
`.temp/adapter_checks-judge-021-fixed-01.log`,
`.temp/transaction_checks-judge-021-fixed-01.log`.

Reviewed new ASTRA25-06 in full and K-EVAL-2/4 against the source core. Its one
global budget spans both polarities and quality roots, directly contradicting
the already explicit independent-walk rule. Independently reproduced current
source supplemental inventory: 10 pass / 2 fail / 8 unsupported semantic; one
deployment unsupported. Both failures are one R7-027 property: ASTRA25-06 and
the visible-opposition final control of ASTRA25-01. The hidden pair stays equal.
The package evaluator passes all 20 current semantic cases; one deployment case
remains unsupported. Evidence:
`.temp/astra22-judge-021-supplemental-budget.md` / `.json`,
`.temp/astra23-judge-021-supplemental-budget.md` / `.json`.
These exact reports remain separate from the 57 canonical vectors. New cases
are useful precisely because canonical green alone does not prove the contract.

Ledger: 27 items, eight rejected, eighteen fixed, one open implementation bug,
no open specification bugs or owner questions. Score remains 1/2 for R7-027.


### Round 13 — root/quality isolation closed; source accounting and priority

Reviewed `4e647ea` core/adapter correction and regression controls. Independent
canonical rerun exactly matches all 65 committed rows, package/core hashes and
totals: 43 pass / 0 fail / 14 unsupported semantic, eight deployment unsupported.
All three budget-family regressions pass: ASTRA25-06, ASTRA25-01 visible control,
and ASTRA24-05 direct opposite polarity. Source controls 29, adapter controls 3,
transaction controls 7 and harness controls 5 pass. Closed R7-027. Evidence:
`.temp/astra22-judge-r7027.md` / `.json`,
`.temp/astra22-judge-r7027-comparison-01.json`, and
`.temp/astra22-r7027-{canonical,source,adapter,transactions}-01.log`.
The pre-fix direct-polarity witness remains in
`.temp/astra22-judge-polarity-budget-01.json`.

Reviewed ASTRA24-06 and independently reproduced its eight final field errors
plus three intended forbidden failures on the corrected root/quality core.
The omitted source-resolution limit is R7-028, separate from R7-027. Current
supplemental inventory is 22 semantic cases: source 13 pass / 1 fail / 8
unsupported; package 22 pass / 0 fail / 0 unsupported. Both retain one unsupported
deployment case. The earlier source corrected report's 21 cases predates this
new case; its 13/0/8 totals do not contradict the new inventory. Evidence:
`.temp/astra22-judge-r7027-supplemental.md` / `.json`,
`.temp/astra23-judge-source-budget.md` / `.json`, and corresponding
`.temp/astra22-r7027-supplemental-01.log`,
`.temp/astra23-judge-source-budget-01.log`.

Independent source adapter review found R7-029: a nonempty currently resolvable
source on an admitted independent assessment incorrectly retains the weaker
independent_attestation state. S32-derived unavailable/resolvable inputs pass
closed state, reference and query checks; the unavailable positive control stays
independent, while the resolvable variant must be resolvable_now under explicit
K-EVAL-5. Astra-22 independently supplied its empty-source variant at `f2d233a`;
judge also validates and reproduces it. Neither changes the assessment's evidence
kind. Exact inputs and outputs are in
`.temp/astra22-resolvable-independent-probe-01.json` and
`.temp/astra22-vacuous-independent-probe-01.json`. An initial validation invocation
used a nonexistent schema fragment and failed setup; the corrected invocation
checks fixture.properties.initial_state plus check_state. No successful-check
claim is based on the failed invocation. These targeted probes are separate from
the 22-case supplemental count. The fix owner has both witnesses and requested
neighbor controls; no package change or owner decision is needed.

Ledger: 29 items, eight rejected, nineteen fixed, two open implementation bugs
(R7-028/029), no open specification bugs or owner questions. Score remains 1/2.


### Round 14 — all classified defects closed; score 2/2

Reviewed source correction `c923ebd`: the adapter clamps the source bound, passes
original source identities through synthetic availability groups, and the core
charges distinct current-required visits within each independent walk. Eligibility
and hidden-input filtering precede accounting; retained/independent checks do not
consume current-required visits. Judge canonical and current supplemental runs
exactly match the committed reports. Canonical: 43 pass / 0 fail / 14 unsupported
semantic; supplemental: 14 pass / 0 fail / 8 unsupported semantic. All 48 controls
pass, including source groups, repeats, distinct sources, policy clamping,
independent polarities/quality, true exhaustion and found-path-only provenance.
R7-028 is fixed@c923ebd. Evidence: `.temp/astra22-judge-r7028*.json` and
`.temp/astra22-r7028-{canonical,supplemental,source,adapter,transactions}-01.log`.

Reviewed `512d006` source priority correction and its neighboring controls. The
judge reran both independently authored nonempty states and the committed empty
state. After normalization at exactly the top-level and two channel snapshot
handle paths, the only changes are support.source_state for the empty and
resolvable variants; the unavailable control is identical. Evidence qualification
remains semantic_review, and input state is preserved. Canonical and supplemental
reports exactly match all rows, package/core hashes and totals; 33 source, 5
adapter, 7 transaction and 5 harness controls pass (50 total). R7-029 is
fixed@512d006. Exact evidence:
`.temp/astra22-judge-r7029-probes-01.json`,
`.temp/astra22-judge-r7029-comparison-01.json`,
`.temp/astra22-judge-r7029-supplemental-comparison-01.json`,
`.temp/astra22-judge-r7029.md` / `.json`,
`.temp/astra22-judge-r7029-supplemental.md` / `.json`, and
`.temp/astra22-r7029-checks-01.json` with every command, exit code and log.

Reviewed astra-23's independently package-derived K-EVAL-5 control at `8b9baf3`:
twelve current/retained/independent cases cover resolved, denied, lost and empty
sources plus true zero-budget exhaustion; qualification and state preservation
are asserted. The evaluator code remains `f5fdd8b`. Reran its canonical and
supplemental reports and compared every row, input/implementation hash and actual
field using only the vector-declared normalization. Exact equality: 57/0/0
canonical semantic and 22/0/0 supplemental semantic. Four checker and ten product
controls pass (14 total). Evidence:
`.temp/astra23-judge-r7029-comparison-01.json`,
`.temp/astra23-judge-r7029.md` / `.json`,
`.temp/astra23-judge-r7029-supplemental.md` / `.json`, and
`.temp/astra23-r7029-checks-01.json` with commands, exit codes and logs.

Ledger: 29 items, eight rejected, twenty-one fixed, no open specification or
implementation bugs, no source ambiguities or owner questions established.
Package remains `f31d58f`, with prior structural validation and every semantic
vector executable. Both evaluators pass every supported semantic vector. The R7
rubric therefore scores **2/2**, with source unsupported coverage explicit and
all eight canonical plus one supplemental deployment vectors still unqualified.
The collective remains active; no park note or final completion is issued before
the convener's PARK marker.


### Round 15 — phase 2 coverage gate; collective remains active

The convener explicitly withheld PARK in rounds event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc` (2026-10-17 04:28:09Z).
Phase 2 expands the completion gate to full dual-implementation canonical
semantic coverage, plus one full round without a new open item, or the existing
13:00Z hard cap. The earlier supported-vector rubric result at `b1ae299` is
preserved as historical evidence; it does not establish the expanded gate.

Audited the current source report against the canonical inventory. Dual coverage
is **43/57**, not 57/57. The exact fourteen remaining source-unsupported semantic
vectors are B01, B07, P05, P06, P08, P12, S07, S17, S20, S23, S24, S25, S26 and
S27. The clauses and explicit runner reasons are persisted in seat-local
`.temp/phase2-dual-coverage-baseline-01.json`. They cover dirty closure, exact proof
enumeration, imported-publication currentness, current disclosure/revocation,
immutable delivery, erasure/restore and logical non-interference under load.
None is silently counted as a pass or fabricated implementation bug.

Source seat astra-22 will extend its own implementation; adversaries focus on
these clauses and the v0.2 delta. Judge intake will preserve immutable initial
failures, classify every observed disagreement before correction, and rerun the
exact committed expanded reports and relevant controls. Source/package intake
history must remain explicit: astra-22's original core was source-derived before
package landing, and later adapter/corrections followed authorized package
intake. No claim of a second package-blind implementation is made for the new
phase. No package release is needed merely to improve implementation coverage.

Current phase-2 score is **1/2** for incomplete dual coverage. Historical original
mission supported-vector score remains 2/2 at `b1ae299`. Ledger disposition is
unchanged: 29 items, 8 rejected, 21 fixed, no open bugs or owner questions. This
coverage gap is a completion requirement, not a source architecture ambiguity.
No final verdict or park note is issued; the collective remains active.


### Round 16 — phase 2 first counterexamples

An independent judge reconstruction probe found R7-030. Start from S14, perform
its valid first admission, then supply a new complete snapshot containing that
record and an explicit runtime.idempotency entry authored from the canonical
request and original receipt. Full closed-state and reference checks pass.
Source `512d006` ignores the entry: exact retry, later intake stamp and changed
intent all return duplicate_record. K-API-1/2 instead require exact receipt,
exact receipt and idempotency_conflict. The same writer's retry passes, as does
package `f5fdd8b` on the identical reconstructed state; both leave state unchanged.
Source stores successful receipts only in a private map, omitting the declared
runtime store. Exact witness and controls are persisted in
`.temp/astra22-restored-idempotency-probe-01.json` and
`.temp/astra23-restored-idempotency-probe-01.json`. This is a semantic supplied-state
contract, not a live restart or deployment test. Source owner acknowledged and
will preserve the first evidence before repair.

Reviewed ASTRA25-07 and its authorized metadata control. The source already
requires approved receipt metadata; conflicting package K-API-1/K-ERASE-2 and
missing explicit receipt scope are R7-031, not a new erasure architecture.
Judge validates both cases and reproduces precisely the two extra-ref fields
and forbidden hidden ID in package runtime `f5fdd8b`. Full protected erased_refs,
custody dispositions and result remain correct. The implementation's immutable
first report is `127bc0b` PHASE2-ERASURE-FIRST; resolution requires a released
explicit operation-bound receipt context and independent evaluator verification.
Evidence: `.temp/astra25-erasure-receipt-judge-validation-01.json`,
`.temp/astra23-judge-erasure-receipt.md` / `.json`,
`.temp/astra23-erasure-receipt-01.log`.

Reviewed ASTRA26-07/08 and ASTRA24-07 completely. Validated their closed grammar,
state references, normalization and expected forbidden guards. Both evaluators
incorrectly call an expired checked publication current; this is two independently
owned implementation bugs (R7-032/033) under explicit K-PUB-2. last_received
preserves bounded knowledge; historical would invent a replacement. The exact
fresh capture and evidence remain unchanged. Package-only R7-034 wrongly checks
forwarding on an excluded unrelated assertion; its extra-grant positive control
and actual selected-right revocation negative control both pass. R7-035 retains
the explicitly correct Cartesian-proof/origin distinction as regression coverage,
with exact package pass and source unsupported at the tested baseline.

Current 28-case supplemental semantic inventory at source `512d006` / package
runtime `f5fdd8b`: source 14 pass / 1 fail / 13 unsupported; package 25 pass / 3
fail / 0 unsupported. One supplemental deployment vector stays unsupported in
both. These are separate from canonical counts and the R7-030 targeted probe.
Exact inputs/results/hashes and validation are persisted in
`.temp/phase2-initial-new-cases-validation-01.json`,
`.temp/astra22-judge-phase2-initial-cases.md` / `.json`,
`.temp/astra23-judge-phase2-initial-cases.md` / `.json`, and
`.temp/astra{22,23}-phase2-initial-cases-01.log`.

Ledger: 35 items, 9 rejected, 21 fixed, 1 open spec bug and 4 open implementation
bugs; no owner question. Phase-2 score remains 1/2. Verified dual canonical
coverage remains 43/57; source's new exact-proof head `4960d24` reports 44/57 and
is queued for independent judge review. A new retention-authority case has also
arrived for the next intake unit. No pending result is treated as verified or
silently merged into the earlier inventory.


### Round 17 — proof coverage and three corrections verified; retention findings

Reviewed source exact-proof implementation `4960d24` including its finite set-family
union/join/prefix representation, local witness provenance, independent origin
sets and adapter ordering. Canonical report exactly matches all 65 rows, package
and core hashes and totals: 44 pass / 0 fail / 13 unsupported semantic. S07 and
both unchanged ASTRA24-01/07 regressions pass. Four proof controls use independent
small finite-set oracles, exact numeric/JSON ordering, hidden/quality exclusions
and a shared 2**40-family prefix. They do not establish a universal resource bound;
worst-case representation growth remains explicitly documented. 33 source, 5
adapter, 7 transaction and 5 harness controls also pass (54 total at this head).
Verified dual canonical coverage is now **44/57** on package `f31d58f`.
Evidence: `.temp/astra22-judge-phase2-proofs.md` / `.json`,
`.temp/astra22-judge-phase2-proofs-comparison-01.json`,
`.temp/astra22-phase2-proof-code-hashes-01.json`,
`.temp/astra22-phase2-proofs-{canonical,proof,source,adapter,transaction}-01.log`.

Reviewed and validated ASTRA25-08's missing-retain and retain-authorized fixtures.
The independent retention requirement is explicit; both implementations store an
unauthorized derivative. Classified R7-036/037 by owner, with atomic not_authorized
and scoped neighboring controls required. The original input remains legal; the
new derivative creates the forbidden persistence. Historical final queries avoid
confusing invalid future-cut rejection with correct authorization. Evidence:
`.temp/retention-authority-judge-validation-01.json`,
`.temp/astra22-judge-phase2-proofs-retain.md` / `.json`,
`.temp/astra23-judge-phase2-retain.md` / `.json`, and corresponding logs. On the
then-current 30-case semantic inventory source is 17/2/11 and package 26/4/0
(pass/fail/unsupported); the original retention failure is preserved by each owner.

Reviewed source R7-030 correction `1f3180d`. Runtime idempotency is now the sole
store; the lookup is derived from it. Judge exact original snapshot probe passes
both literal original-receipt replays and intended changed-intent conflict, with
records/policy/runtime unchanged. All 11 transaction controls pass, adding four
meaningful controls to the seven unchanged ones; canonical 44/0/13 report remains
an exact match. Reused unchanged source/adapter/proof/harness evidence yields 58
passing controls across this head. Closed R7-030. Evidence:
`.temp/astra22-judge-r7030-probe-01.json`,
`.temp/astra22-judge-r7030-comparison-01.json`,
`.temp/astra22-judge-r7030.md` / `.json`, and
`.temp/astra22-r7030-checks-01.json` with commands, exit codes and logs.

Reviewed package correction `f10c7ba` and the two new regression groups. R7-033
now observes the exclusive import horizon without changing evidence, origin,
ordinary-document currentness or earlier captured bytes. R7-034 checks only the
exact selected binding for forwarding; selected read/use/forward denial, fence,
expiry and later revocation remain effective. All 16 product/checker controls
pass; canonical 57/57 exactly matches every row and implementation/input hash
with only declared normalization. Closed R7-033/034. Evidence:
`.temp/astra23-judge-r7033-34.md` / `.json`,
`.temp/astra23-judge-r7033-34-comparison-01.json`, and
`.temp/astra23-r7033-34-checks-01.json`.

New ASTRA25-09 is retained as R7-038 regression, not a new defect. Both exact
unknown-lineage/known-input erasure traces validate and pass package execution;
the independent-input positive control prevents reject-all unknown-lineage
behavior. Source erase is still unsupported. The resulting current inventory is
32 semantic cases: source 17 pass / 2 fail / 13 unsupported; package 30 pass / 2
fail / 0 unsupported. Both leave one supplemental deployment case unsupported.
The committed package supplemental report predates these two cases; comparison
by ID matches all 31 common rows except the known unexpected R7-037 random
receipt and its diff value, outside declared normalization. Literal equality is
not claimed. Evidence: `.temp/unknown-lineage-erasure-judge-validation-01.json`,
`.temp/astra22-judge-r7030-supplemental.md` / `.json`,
`.temp/astra23-judge-r7033-34-supplemental.md` / `.json`, and
`.temp/astra23-judge-r7033-34-supplemental-comparison-02.json`.

Ledger: 38 items, 10 rejected, 24 fixed, one open spec bug (R7-031) and three open
implementation bugs (R7-032/036/037), no owner questions. Phase-2 score stays 1/2.
New package 0.2.2 `7e71765` and source import candidate `1f35727` arrived after
these pinned checks and are the next review unit; neither is silently included
in the validated 0.2.1 coverage or closures above.


### Round 18 — explicit retention scope, ambiguous CAS and 0.2.2 review

Classified R7-039 spec-bug after verifying both implementers' separating scope
neighbor and all four closed operation contexts. The source design requires an
explicit retention purpose, but the package cannot bind exact audience/purpose
grants to one write intent. Disclosure label sets do not select existential or
all-label retention authority, and empty disclosure intersections remain
non-disclosable records. Requested an explicit actor-bound retention scope with
per-output/transitive-known-input authority, current revocations, same-batch and
unknown-lineage handling, canonical replay and atomic refusal. This implements
existing source requirements; it is not an owner architecture choice. Definite
no-retain implementation findings R7-036/037 remain separate. Evidence:
`.temp/retention-scope-judge-01.md`,
`.temp/retention-scope-contexts-01.json`, and decision
`$DgdmzXqH-rajfv36DacN6RQfHAQ3H45tTew6Xha8Qls`.

Validated ASTRA24-08 and its unique-head control against 0.2.2 closed grammar,
references, normalization and expected forbidden predicates. Both evaluators
accept the forbidden ambiguous-head withdrawal and persist a seventh record;
both pass the unique-head control. Source has ten field/shape differences plus
two forbidden matches; package has eleven plus two forbidden matches. K-REV-1
already names ambiguous-head conflict and K-REV-3 defines authority ordering.
Classified R7-040/041 implementation bugs by owner; required atomic no-write,
current authority, challenge and exact replay neighbors. Historical view equality
alone cannot prove refusal. Evidence:
`.temp/ambiguous-cas-judge-validation-01.json`,
`.temp/astra22-judge-r7032-supplemental.md` / `.json`,
`.temp/astra23-judge-cas-supplemental.md` / `.json`, decision
`$jWF7PS9bJWLBKtoGF2OqBiJIlvcfYJB7WzuI6j5fxPw`.

Reviewed 0.2.2 `7e71765` erasure-receipt grammar, normative clauses, exact P08
oracle and checker changes. Independent validation passes 94 JSON files,
14 schemas, 14 domain documents, 65 vectors, 52 clauses and 23 intended violation
controls. Exact regeneration in an isolated copied package passes. Only P08's
expected report changes after explicit profile-version comparison; all 13 erase
operations supply explicit receipt context. The unchanged package runtime
reproduces the intended sole canonical failure, P08: 56 pass / 1 fail / 0
unsupported semantic, eight deployment unsupported. This is a detection control,
not corrected conformance; R7-031 remains open until behavior is verified.
Evidence: `.temp/package-validate-04.log`,
`.temp/package022-release-review-01.json`,
`.temp/package022-regeneration-01/spec/`,
`.temp/astra23-judge-package022-first.md` / `.json`, and
`.temp/astra23-package022-first-01.log`.

Reviewed source R7-032 correction `1f35727` and all three new control groups.
All eight adapter controls pass. Canonical 0.2.2 result exactly reproduces the
committed report's 65 rows, input/core hashes, package pins and totals: 45 pass /
0 fail / 12 unsupported semantic. S23 is newly supported; ASTRA26-07 passes
unchanged apart from its owner's explicit profile migration. Closed R7-032.
Verified dual canonical coverage is **45/57**. Previous unchanged control groups
plus these eight adapter controls total 61 (33 source, 8 adapter, 11 transaction,
4 proof, 5 harness); reused evidence is not represented as a fresh full-suite run.
Evidence: `.temp/astra22-judge-r7032.md` / `.json`,
`.temp/astra22-judge-r7032-comparison-01.json`,
`.temp/astra22-r7032-code-hashes-01.json`,
`.temp/judge-round18-execution-01.json` with commands/exits/logs,
`.temp/package022-dual-coverage-01.json`, and closure decision
`$t62IzV7AQgzvkNmi_vyikVHDeAPF9N8MjuqfCuupUxk`.

The supplemental inventory is mid-migration: 20 semantic fixtures validate
against 0.2.2, giving source 17/1/2 and package 19/1/0. Fourteen semantic fixtures
and one deployment fixture still use old grammar/profile at this pinned
checkout. Package marks these unsupported; source reports four cases with old-profile
mismatches (including the already known R7-036 failure) and unsupported operations.
These do not establish additional semantic defects.
Do not merge these raw runs into a common valid corpus or silently migrate
another seat's fixtures. Inventory and exact statuses:
`.temp/package022-supplemental-migration-inventory-01.json`. Earlier full 0.2.1
supplemental results remain pinned in round 17. Initial local schema probes used
a Path where parse expects text and included prohibited envelope.context
placeholders in a recursive count; corrected targeted probes pass, and no
classification relies on those setup failures.

Ledger: 41 items, 25 fixed, 10 rejected, two open specification bugs
(R7-031/039) and four open implementation bugs (R7-036/037/040/041). No owner
questions. Phase-2 score stays 1/2. No PARK has been announced.


### Round 19 — erasure closure verified, 47/57 coverage, two new defects

Closed R7-031 at package `7e71765` after reviewing and independently executing
runtime correction `a016781`. Shared exact grants preserve the prior read
predicate. Receipt metadata is filtered before the new fence; full erasure
closure, custody and generation are unchanged. Authorized replay preserves exact
stored refs/handle, including across later intake timestamps or newly broader
rights; changed context conflicts, while current read/use/metadata loss or expiry
refuses without altering any state or stored receipt. All 65 canonical rows and
code/input/package hashes match after only declared handle normalization: 57/57
semantic, eight deployment unsupported. Four checker and fourteen product tests
pass. Migrated ASTRA25-07 primary, authorized and unrelated-purpose fixtures
validate and pass exactly. First 0.2.2 red evidence `0ca2d27` stays immutable.
Evidence: `.temp/astra23-judge-r7031.md` / `.json`,
`.temp/astra23-judge-r7031-comparison-01.json`,
`.temp/astra23-judge-r7031-cases.md` / `.json`,
`.temp/astra23-r7031-{canonical,harness,semantics,cases}-01.log`, and closure
`$31IyK5gwGSJaMRrozQ-A02a1oUfrXbHkp9e1ZaOGWjI`.

Reviewed source dirty-impact implementation `e38c37c`. Canonical report exactly
matches 65 rows and pinned hashes: 47 pass / 0 fail / 10 unsupported semantic;
B01 and S17 are newly supported. ASTRA25-05 hidden/visible pair passes. All six
impact controls pass, including pre-cause/recomputed state, hidden cause/path/
premise/certificate, hidden AND sibling/context, later path retirement and
cross-schema review. Fresh reruns of 33 source, eight adapter, eleven transaction
and four proof controls pass, with five harness controls invoked by each vector
run: 67 total. Verified dual canonical coverage is **47/57**. This does not
claim complete invalidation correctness; R7-043 below is an independent failure.
Evidence: `.temp/astra22-judge-phase2-dirty.md` / `.json`,
`.temp/astra22-judge-phase2-dirty-comparison-01.json`,
`.temp/astra22-judge-phase2-dirty-cases.md` / `.json`,
`.temp/astra22-phase2-dirty-checks-01.json`,
`.temp/astra22-phase2-dirty-impact-01.log`,
`.temp/astra{22,23}-round19-code-hashes-01.json`, and
`.temp/judge-round19-execution-01.json` with commands/exits/logs.

Validated and reproduced both additional CAS neighbors at `f13a3e6`: the
historical candidate incorrectly commits in both implementations, while challenge
correctly ignores the stale CAS token without manufacturing opposition or dirty
state. These extend R7-040/041 rather than duplicate defect counts. Source
first report `e38c37c` and package first report `e525612` preserve the failures.
The primary and unique-head fixtures remain unchanged. Decision
`$ouwGQLkAq_ICQJkSwSucRdoGhIuhQShrtac9FEp3j4A`.

Classified ASTRA25-10 as checker spec-bug R7-042. The initial state has no records
but contains protected facts for future A and B, where B will consume A. The
checker rejects A's absence before any operation, contrary to K-DISC-1's future
fact contract. Both evaluators correctly refuse premature B, admit A, then accept
identical B retry. Closed shape, normalization and accepted-fact checks pass.
Judge independently verifies the admitted-A positive and truly dangling admitted
complete/unknown-B negative controls. Required correction defers existence only
for unadmitted outputs, retaining fact integrity and operation-time checks.
Evidence: `.temp/future-lineage-input-judge-validation-01.json`, case evidence
`cases/astra-25-evaluator-results.json`, and decision
`$GMbY9p6_pemnZ4YJ4kSkLz6M9eJTAjloeXsRPKzFrmA`.

Judge code review found R7-043: source impact edges include literal premises but
omit the changed justification and its check certificate. Three independent
S17-derived closed vectors were written before execution. Set relation to withdraw,
target and expected_version to rec:j/1 or cert:j/1, both replacement fields null,
query cut 101, expected receipt refs rec:r/1 and inventory without rec:a/2; retain
S17's required dirty-B result. Source returns no dirty cause/marker, complete
channels, no review and no dirty cutoff: six differences plus forbidden-complete
for each. Premise-withdrawal control passes, as do all three package traces.
Thus agreement on canonical B01/S17 is insufficient. Exact fixture inputs,
original actual/runtime/hashes and rationale are preserved at
`.temp/dirty-edge-judge-vectors-01/`,
`.temp/astra22-dirty-edge-judge-first.json`,
`.temp/astra23-dirty-edge-judge-first.md` / `.json`,
`.temp/dirty-edge-judge-review-01.md`. Source CLI's initial outside-repo path error
is recorded as setup failure; successful execution uses the existing Adapter and
comparator directly, passing no expected data to the evaluator. No same-source
output generated the oracle. Owner astra-22 must preserve the probes in its
tracked fixtures before correcting. Decision `$lXcUN46jxrVt_c0amm5LNbwyvqnzNvPyTOc6omMPOmk`.

All 39 supplemental fixtures now have the 0.2.2 closed shape; 38 are semantic and
one is deployment. Their initial-state checks pass except the explicit R7-042
false positive. Full execution is source 24/3/11 and package 35/3/0; the three
failures are missing retention plus two CAS cases. Judge's three additional
invalidation probes are separate: source 1/2/0 and package 3/0/0. Inventory
validation: `.temp/round19-supplemental-validation-01.json`. No silent case
migration or invalid-state success is claimed.

Ledger: 43 items, 26 fixed, 10 rejected, two open specification bugs (R7-039/042)
and five open implementation bugs (R7-036/037/040/041/043). No owner questions;
phase-2 score 1/2. Package 0.2.3 scope has been described by the editor but is not
released or verified in this pinned round. Continue until PARK.


### Round 20 — 49/57 coverage, package CAS closed, source neighbor still fails

Validated and independently reproduced three new package implementation defects:
R7-044 missing one exact publication check (two currentness fields and two
forbidden matches), R7-045 missing transitive review dependent (length/ref and
forbidden-size), and R7-046 ungranted delivery actor (nine fields and forbidden
receipt). Source passes all five new fixtures, including explicit-unverified and
all-checked import controls. Hidden review-path and rightful/revoked delivery
controls pass. Their existing clauses determine the outcomes; no owner or package
architecture decision is needed. Evidence: `.temp/round20-new-cases-validation-01.json`,
`.temp/astra{22,23}-judge-round20-cases.md` / `.json` and row-linked decisions.
Package first import/review report remains `08c4b9a`; delivery owner must preserve
its new first report before correction.

Reviewed source delivery expansion `5d079be` and eight boundary controls. Saved
captures bind exact selected refs and immutable values. Current selected
read/use/forward, horizon, erasure/restore, actor/audience/purpose/index binding,
owner-only revoke and unrelated-scope revocation controls pass. P06/P12 and both
unchanged ASTRA26-08 traces now pass. At reviewed source `68152c5`, canonical
49/0/8 exactly matches all 65 committed rows, input/core hashes and package pins;
verified dual coverage is **49/57**. No external send occurred. Evidence:
`.temp/astra22-judge-r7040.md` / `.json`,
`.temp/astra22-judge-r7040-comparison-01.json`,
`.temp/astra22-phase2-boundary-01.log`, and coverage decision
`$jk002-IEoShLg1iYvSrLfgoWeqaRf4LN1XZIbrPw8Yk`.

Reviewed both CAS corrections in full. Package `53266dd` shares receipt-order
selection with its projection; all four original cases, full-state/dirty atomicity,
challenge exemption, later unique ordering, reversed storage, exact later-stamp
replay, changed intent and remaining-head withdrawal pass. All 65 canonical rows
and code/input/package pins match after declared normalization; 57/57 semantic,
19 product/checker controls. Closed R7-041. Source `68152c5` passes the same four
original cases and 13 transaction controls, but not the additional valid
remaining-head probe, so R7-040 remains open rather than being prematurely closed.
Evidence: `.temp/astra23-judge-r7041.md` / `.json`,
`.temp/astra23-judge-r7041-comparison-01.json`,
`.temp/astra23-r7041-{canonical,semantics,harness}-01.log`,
`.temp/astra22-r7040-transactions-01.log`,
`.temp/astra{22,23}-round20-code-hashes-01.json`, and
`.temp/judge-round20-execution-01.json` with all commands/exits/logs.

Remaining-head witness: start the unique-head fixture, withdraw d3, then submit
reviewed direct-lineage withdraw-next against d2 with expected_version=d2 and a
fresh key. The intermediate source projection already reports d2 current, yet
source head() retains withdrawn d3 and falsely returns version_conflict; state
is unchanged on that false refusal. Package accepts both withdrawals. This is
the same R7-040 head-selection failure class, not a duplicate item. The first
helper omitted the review allowance's required reviewer; a shell sequencing
mistake sent the validation statement before the failure was observed. That
statement was corrected explicitly in event `$1bUzACRYK88lMyGybBGEdvztQMQ5oCG_18CW_c-Qxk8`.
After adding only the authenticated reviewer, closed state/operations/query and
references pass; both runtimes were rerun and the exact intended divergence
persists. Invalid setup files are preserved but excluded from semantic evidence.
Valid inputs and evidence: `.temp/authority-next-head-judge-probe-01.json`,
`.temp/astra22-authority-next-head-judge-first.json`,
`.temp/astra23-authority-next-head-judge-control.json`.

Current 43-case semantic supplemental execution: source 33/1/9, package 39/4/0;
one deployment case unsupported. These do not include the separate judge
rule/certificate probes or remaining-head probe. Source established controls
total 77 (33 source, 8 adapter, 13 transaction, 4 proof, 6 impact, 8 boundary,
5 harness), with unchanged groups reused; passing suites do not cover the two
open judge failure classes. Package has 19 passing controls.

Ledger: 46 items, 27 fixed, 10 rejected, two open specification bugs (R7-039/042)
and seven open implementation bugs (R7-036/037/040/043/044/045/046). No owner
questions. Phase-2 score remains 1/2; pending 0.2.3 is not counted as released.


## Round 21 — six closures and the explicit 0.2.3 baseline

Reviewed source `99b5a85` and package runtime `f6c339d` in a scratch tree with exact
0.2.2 package `7e71765` and unchanged case tree `3f06da5`. Archive checksums and every
source module hash are recorded. R7-040/043/044/045 close only on this pinned
behavioral evidence. Source canonical 49/0/8 exactly matches its committed report;
package canonical 57/0/0 exactly matches its committed report after only declared
handle normalization. Source 14 transaction and 9 impact controls, plus the three
original judge invalidation vectors, pass. Unchanged established groups are
reused explicitly: source 81 total controls, package 22 rerun controls.

The complete frozen 44-semantic-case corpus gives source 34/1/9 and package 42/2/0.
Both retain failures and the package delivery-actor failure remain real. The
source pinned supplemental report and the package overlapping 42-case report
agree everywhere except the fresh handle inside the forbidden retention-success
receipt. That handle has no declared normalization path because the operation
must refuse; the reports are not falsely described as byte-identical. NEXT and
actor binding are the two additional package rows. Deployment remains 8 canonical
plus 1 supplemental unsupported on both evaluators.

Package 0.2.3 / `23290b3` closes R7-039 and R7-042. Read the actual prose, schemas,
generator and checker changes: authenticated actor and explicit audience/purpose
bind retention of each output and every transitive known content input; current
revocations and exact replay use the same scope. Onward labels grant no storage
right, and empty labels do not prevent authorized storage. The deferred-fact
checker preserves admitted-input integrity and accepted whole-batch resolution.
Independent positive/negative controls establish future-fact acceptance without
allowing missing admitted complete/unknown inputs, duplicate/direct corruption,
or acceptance of B without A. No owner architecture choice is needed.

All 94 JSON artifacts regenerate byte-for-byte;14 schemas, 14 domain documents,
65 vectors, 52 clauses and 32 intended checker violations pass. Only P11/P13 expected
reports change after profile-only normalization. Their isolated prescribed
positive traces match every expected field, including same-batch inputs and
empty-label non-disclosure. This does not assert the skipped retention refusals
are implemented. An initial judge regeneration-driver syntax error occurred
before execution, was preserved, and contributes no semantic evidence.

Current 0.2.3 full canonical reruns at checkout `9799025` are source 47/2/8 and package
55/2/0. Only P11/P13 fail in each; current exact dual passes are 47/57, with 49 source
vectors implemented. Historical 0.2.2 dual 49/57 remains separate. R7-036/037 stay
open for behavioral retention and atomic/replay correction. The new adversary
transitive-unknown retention pair extends these same items; its current-release
review is queued. Incoming actor fix `3ce8ee3` and later fixture migrations are also
queued for the next round, not included in this verification baseline.

Evidence in judge seat `.temp/`: `judge-round21-frozen022/archive-evidence.json`,
`astra22-judge-round21-pinned-{canonical,cases,dirty}.json`,
`astra22-round21-controls-01.json`,
`astra23-judge-round21-pinned-{canonical,cases}.json`,
`astra23-round21-execution-01.json`, `judge-round21-pinned-comparison-01.json`,
`package023-regeneration-review-01.json`, `package023-future-input-review-01.json`,
`package023-authorized-traces-review-01.json`,
`judge-round21-current023-execution-01.json` and
`judge-round21-current023-provenance-01.json`. Original reports and inputs remain
in committed producer/adversary paths; judge scripts do not alter any of them.

Ledger: 46 items, 33 fixed, 10 rejected, three open implementation bugs
(R7-036/037/046), no open specification bugs, no owner questions. Current score 1/2.
Full dual 57/57 plus the convener's quiet-round condition remains unmet. No PARK.


## Round 22 — retention and actor fixes verified; succession separated

Package 0.2.3 remains `23290b3`. Source `d077064` independently reproduces every
canonical row (49/0/8) and every current supplemental row (37/0/9). All 89 controls
pass: 33 source, eight adapter, 14 transaction, four proof, nine impact, eight
boundary, eight retention and five harness controls. Every current Python module
matches the signed correction commit. R7-036 closes for the implemented write
paths; unsupported declassification/erasure/restore coverage is not implied.

Package `4af0360` independently reproduces 57/57 canonical and 46/46 supplemental
semantic cases, plus 22 product and four harness controls. R7-037 closes on scoped
per-record authority over outputs and transitive known inputs, including unknown
lower bounds. Missing authority and revoked exact replay preserve full state and
the old receipt; restored authority permits same-key recovery. All four write
APIs, metadata-independent retention, input spaces, batch order and empty labels
have positive/negative controls. Producer package labels are abbreviated; an
initial literal comparison exposed that difference, and Git resolves them to the
same full release SHA. All actual rows and module/input hashes match; no mismatch
is hidden by changing a conformance input or expected output.

R7-046 closes at `3ce8ee3`: original 0.2.2 vector and native binding controls were
rerun against an exact archive, then the explicit 0.2.3 migration was verified in
the current full corpus. Wrong actor/audience/purpose/index leaves state, captures,
protected view bindings and dirty-since unchanged. Rightful delivery and later
selected-right revocation preserve their exact outcomes. All 47 current
supplemental artifacts (46 semantic, one deployment) pass closed shape, state,
normalization, accepted-fact and forbidden-oracle checks. Eight canonical and one
supplemental deployment cases remain unsupported, separately from semantic passes.

ASTRA24-10 is independently confirmed beyond that vector denominator. All three
unchanged input triples validate. Both implementations accept the ordered positive
and incorrectly accept incomparable and identical authority receipts. Each
negative adds two records, advances cut 100→102, dirties the registered dependent
and stores one idempotency entry. This is a runtime failure with observable writes,
not a parser failure or an inferred consequence of another implementation.
The bundle hash is `5dcc51600aaed1a2253c9c8ebbde951556521ccea982a55fa3f60d055965ecd4`.

R7-047/048 track the separate source/package implementation defects. R7-049 tracks
the missing exact closed-code mapping. K-REV-3 already requires a strictly
succeeding receipt, and kernel §5.3 forbids memory-side order from manufacturing
authority adoption. Use `authority_receipt_required`, retryable=false, for missing
qualifying successor evidence and publish that concrete mapping; preserve
`version_conflict` for CAS mismatch. Incomparable plain imports, direct/transitive
valid successor replacement and exact accepted replay remain positive neighbors.
Earlier CAS closures concern a different invariant and are not silently reopened.
No settled architecture or owner question is introduced.

Evidence in judge seat `.temp/`: `astra22-round22-execution-01.json`,
`astra23-round22-execution-01.json`, `astra{22,23}-judge-round22-{canonical,cases}.json`,
`judge-round22-report-comparisons-01.json`, `judge-round22-case-validation-01.json`,
`astra23-judge-round22-actor022.json`, `judge-round22-authority-input-validation-01.json`,
`astra{22,23}-judge-round22-authority-first.json` and
`judge-round22-authority-decision-01.json`. Original producer/adversary first
failures remain committed. These native succession probes are not fabricated
exact-vector passes and do not inflate the 46-case semantic corpus.

Ledger: 49 items, 36 fixed, 10 rejected, two open implementation bugs (R7-047/048)
and one open specification bug (R7-049). Current exact dual canonical passes are
49/57, with eight source gaps. Score remains 1/2; no PARK or deployment claim.


## Round 23 — source declassification digest mapped incorrectly

Source first expansion `36983de` attempts P05 and ASTRA25-02, which were previously
unsupported. Independent full runs exactly reproduce its committed canonical
49/1/7 and supplemental 37/1/8, including every input hash and normalized output.
The sole new failure in each corpus is the valid joint-owner release. This is
R7-050, a source implementation defect; earlier R7-006 fixed the specification.

K-JSON-2 already requires SHA-256 over `bounded-evidence:cjson-v1`, a single NUL,
and canonical UTF-8 assertion-body JSON. The source code hashes only the final
body. The existing canonical P05 pin equals the independently calculated framed
digest. Separate judge controls keep trusted owner decisions and their assessment
pins consistent for both ASCII and non-ASCII bodies. All four initial states and
operations pass closed grammar and state checks. Source refuses both framed
positives and admits both raw negatives, with forbidden record mutations. Package
`4af0360` accepts the two positives and refuses both raw negatives with unchanged
complete state. The claim is grounded in the explicit canonical-byte contract;
evaluator agreement is only an independent control, not the oracle.

The source correction may change framing only as needed for K-JSON-2, retaining
first reports and negative witnesses. Exact P05/ASTRA25-02 and owner/pin/revocation
atomicity controls remain required before closure. No package or owner decision
is needed for this defect. Authority-succession R7-047/048 and code-mapping R7-049
remain separately open; no late candidate has been silently accepted.

Evidence in judge seat `.temp/`: `judge-round23-first-execution-01.json`,
`judge-round23-first-comparison-01.json`,
`astra22-judge-round23-first-{canonical,cases}.json`,
`judge-round23-release-digest-probe.py`,
`astra{22,23}-judge-round23-release-digest-first.json` and
`judge-round23-digest-input-validation-01.json`. Original inputs and producer
reports remain unchanged. Native digest controls stay outside vector totals.

Ledger: 50 items, 36 fixed, 10 rejected, three open implementation bugs
(R7-047/048/050) and one specification bug (R7-049). Exact dual canonical passes
remain 49/57; P05 now fails on the source's first expansion and seven canonical
vectors remain unsupported. Package canonical 57/57 and supplemental 46/46 at
`4af0360` remain the independently verified baseline. Score 1/2; no PARK.


## Round 24 — declassification verified; receipt-only ancestry isolated

R7-050 closes at `8a42945`. Independent full canonical 0.2.3 execution is
50/0/7, matching every committed row and input/core hash. Every source module
matches the correction commit; all 46 prior supplemental semantic rows match
its committed report. All 98 controls were rerun: the previous 89 plus nine
release groups. Exact joint-owner P05 and ASTRA25-02 pass. The four independent
ASCII/non-ASCII framed/raw controls now satisfy both acceptance and atomic
rejection, without changing their inputs or expected invariants. Producer first
implementation `36983de` and control failures `e1ba8db` remain immutable. The
producer's newly reached unregistered-projection test setup was fixed explicitly;
it is not relabelled a product regression. This verifies P05 as new source coverage
and brings exact dual canonical passes to 50/57 on package `23290b3`.

The current supplemental inventory adds five adjudicated authority vectors and
one raw-digest vector: 52 semantic and one deployment. All 53 pass independent
closed shape, initial-state/reference, admission-fact, normalization and
forbidden-oracle checks. Source results are 40/4/8; package runtime `4af0360`
gives 49/3/0. Both fail the three forbidden succession writes already tracked as
R7-047/048. Direct successor and raw-digest cases pass both. The source alone
fails the full transitive-successor projection, now separately tracked R7-051.
The code-mapping release R7-049 remains pending; these supplemental expectations
use the judge's explicit adjudicated mapping, not a claim that 0.2.3 prose had
already stated that exact code.

For R7-051, source admission of the valid transitive successor succeeds. The
adapter maps only direct predecessor receipts that have assertion candidates,
so a path through an admitted receipt-only intermediate event disappears. A
fresh source evaluator over the actual post-write snapshot, with no operations,
returns ambiguous_current and the old/new candidates. The complete snapshot
passes closed state/reference checks and the read changes no records/runtime/
policy. Its exact direct-edge neighbor passes. Package reads of the identical
two snapshots both match the expected result. This isolates projection from
replacement validation and grounds the required order in K-REV-3/kernel §5.3.

The initial judge isolation helper incorrectly selected a leading capture as a
revision and failed with KeyError before producing evidence. That setup failure
is preserved and excluded. The corrected helper executes the original operation
sequence before creating a fresh read-only snapshot; it reproduces nine exact
comparison/forbidden differences only in the transitive case. No evaluator or
author-owned input was modified to obtain the result.

Evidence in judge seat `.temp/`: `astra22-round24-execution-01.json`,
`astra22-judge-round24-{canonical,cases}.json`, `astra23-judge-round24-cases.json`,
`judge-round24-release-comparison-01.json`,
`astra22-judge-round24-release-digest-corrected.json`,
`judge-round24-case-validation-01.json`,
`judge-round24-readonly-authority-probes.json`,
`astra23-judge-round24-readonly-authority-control.json` and
`judge-round24-readonly-setup-01.log`.

Ledger: 51 items, 37 fixed, 10 rejected, three open implementation bugs
(R7-047/048/051) and one specification bug (R7-049). No owner question. Seven
canonical source vectors remain unsupported: B07, P08, S20, S24, S25, S26, S27.
Deployment stays eight canonical plus one supplemental unsupported on both.
Score 1/2; no PARK. Incoming release/correction candidates require separate review.

## Round 25 — strict succession verified; expired retention adjudicated

R7-047 closes at signed `4772258`; R7-049 closes at signed package 0.2.4
`ef02647`. Source native controls pass all three forbidden receipt orders for
replace and correct with complete unchanged state, direct and transitive positive
writes, event-array reversal, ordinary incomparable import, exact replay before
CAS and stale-head conflict. Four new groups and fourteen existing transaction
groups pass. The separate receipt-only projection controls reproduce three
intended failures; their incomparable control passes. They are R7-051 evidence,
not green controls or a reopened write finding.

An exact archive combines package `23290b3`, source `4772258` and original cases
`2c2dc53`, preserving the producer's 0.2.3 inputs. Canonical results exactly match
all 65 committed rows: 50/0/7 semantic. The original 54-case semantic supplement
is 44/2/8, with only ASTRA24-10-TRANSITIVE and ASTRA24-11 failing projection.
All 55 supplemental artifacts validate. Every case status, hash and comparison
error matches the producer. Two failing actual reports differ only in fresh
handles on their forbidden extra second items; those undeclared paths are kept
raw, not normalized into a false byte-equality claim. The initial blanket report
comparison therefore failed as intended and was refined into this explicit
account. Package `4af0360` on these same unchanged original cases gives 51/3/0;
its three successor-admission failures remain R7-048.

Independent 0.2.4 execution gives source 49/1/7 and package 56/1/0. Only B01
fails in either executable canonical subset. Source matches every operation,
receipt, replay, refusal and postcondition; its seven final-view differences are
R7-051. Package still admits a prior receipt, causing the expected downstream
cascade. Exact dual canonical coverage is therefore 49/57 on this expanded
release, not the historical 50/57 on 0.2.3. No new source coverage regression is
inferred merely from the stronger B01 oracle.

Package review confirms the source-derived strict-succession rule and exact
closed refusal mapping. All 94 JSON artifacts regenerate byte-identically in an
isolated release archive, and all 33 structural checker plants detect the intended
violation. Only B01 changes after profile-version normalization; the other 64
vectors and original pilot fixture are unchanged. Module hashes confirm the
source runtime at 4772258 and package runtime at 4af0360; the only later source
Python addition is the explicitly red projection control file. All reviewed
commits have verified human signatures. Supplemental author migration remains
explicit; the retained 0.2.3 inventory is not silently rewritten for 0.2.4.

ASTRA25-11 at `604af18` establishes R7-052 (source implementation), R7-053
(package implementation) and R7-054 (exact package mapping), decision
`$JPRw0HAxhQiEJ-rN4erBtnvRBnBXixLi2Rap_jcFAN0`. Independent native replay of
all five original probes validates every state and operation. Both runtimes
accept the before-deadline positive and incorrectly commit a new output at the
input deadline, after it, and at the output's own deadline: records 1→2, cut
100→101 and a new replay receipt. The late exact-replay probe returns its stored
success receipt with state unchanged, although current retention has expired.
These are native observations outside the vector denominator.

Kernel §7.1 and the design Context seam prohibit extending inherited retention;
K-DISC-1 ends retention at the earliest non-null deadline, K-AUTH-1 keeps deadlines
independent of grants, and K-API-1 subjects replay to current retention authority.
The concrete mapping is `not_authorized`, retryable=false, at/after any applicable
deadline under trusted `context.at`, in the existing current-retention authorization
class before idempotency. Apply the same test to original outputs and known input
closure on replay. Denial preserves the original receipt and full state; it does
not erase data or launch a purge. Null adds no bound. Complete and incomplete-known
lineage, transitive inputs and whole-batch resolution retain their existing rules.
No owner architecture choice is needed. Exact author vectors and a normal package
release must preserve the first observations and before/unbounded positive controls.

ASTRA24-11 is accepted as a second independent read-only witness for existing
R7-051, not another defect; decision `$mIllJVB-2Xb74ZRgxK-batWe57ATb2lDU-isgksI2_E`.
Its complete-assertion control passes and receipt-only intermediate case fails
only source. The source projection correction remains a separate pending unit.

Evidence in judge seat `.temp/`: `judge-round25-execution-01.json`,
`astra{22,23}-judge-round25-canonical.json`,
`astra{22,23}-judge-round25-pinned-cases.json`,
`astra22-judge-round25-pinned-canonical.json`,
`judge-round25-succession-report-comparison-01.json`,
`judge-round25-pinned-case-validation-01.json`,
`judge-round25-package-review-01.json`,
`judge-round25-signatures-modules-01.json`,
`astra{22,23}-judge-round25-deadline-first.json` and
`judge-round25-deadline-decision-01.json`. First failures remain committed unchanged.

Ledger: 54 items, 39 fixed, 10 rejected, four open implementation bugs
(R7-048/051/052/053) and one specification bug (R7-054). No owner question.
Seven canonical source gaps and all eight canonical plus one supplemental
deployment cases remain unsupported. Current score 1/2; no PARK.

## Round 26 — both authority-order corrections verified

R7-048 closes at signed `942bdee`, and R7-051 closes at signed `427fed5`.
Both independent full runs use the verified 0.2.4 release `ef02647`. Source
canonical is 50/0/7; package is 57/0/0. Exact dual canonical passes return to
50/57 on the stronger release. The current 54-case semantic supplement is source
46/0/8 and package 54/0/0. Every committed canonical/supplemental input hash and
exact actual output matches after only the declared handle normalization. All
runtime module hashes match their correction commits. No unsupported case is
promoted to a pass, and no implementation is used as the other's oracle.

Package strict succession uses canonical receipt traversal for head selection
and the authoritative replace/correct gate. Twenty-eight product/checker groups
pass, including eight relation-by-receipt-class atomic negatives with a valid
same-key retry, direct/transitive successor writes, exact original receipt replay
after the later head, separate stale-CAS refusal and plain incomparable import.
The original native, exact supplemental and 0.2.4 first failures remain immutable.

Source projection closes the issuer's canonical receipt graph before mapping
ancestors onto exact assertion sequences/spaces. It therefore preserves paths
through receipt-only events. Expanded B01, ASTRA24-10-TRANSITIVE and the complete
read-only ASTRA24-11 pair now pass exactly. All 106 source controls were rerun,
including the four ancestry groups that previously showed three intended failures.
Longer paths and event permutations preserve ordering; eligible/private/historical
candidate controls and a genuinely incomparable branch preserve their distinct
results. Reads leave semantic state unchanged. These controls do not claim
universal hidden-receipt non-interference or arbitrary-graph qualification.

All 55 current supplemental artifacts validate, including state references,
admission facts, normalization and forbidden-oracle checks. Each author-owned
migration round-trips to the preserved 0.2.3 artifact by changing only its profile
stamp. No expected semantic value was relaxed. Reviewed test maintenance is
explicit: the B01 impact/lineage controls now select the released direct-successor
positive instead of the new refused first operation, exact fixtures use the
current profile, and an unreached invalid hypothetical context was corrected to
the admitted simulated variant. The genuine original projection witnesses never
depended on that invalid setup branch.

Evidence in judge seat `.temp/`: `astra{22,23}-round26-execution-01.json`,
`astra{22,23}-judge-round26-{canonical,cases}.json`,
`judge-round26-report-comparison-01.json`,
`judge-round26-case-migration-validation-01.json` and
`judge-round26-signature-{source,package}-01.log`.

Ledger: 54 items, 41 fixed, 10 rejected. Retention-deadline implementation
R7-052/053 and exact package mapping R7-054 remain open; native first evidence
and adjudication are unchanged. No owner question. Source canonical gaps remain
B07, P08, S20, S24, S25, S26 and S27; deployment remains eight canonical plus one
supplemental unsupported on both. Score 1/2, phase 2 active; no PARK.

## Round 27 — exact expiry regression vectors admitted

The seven author-owned ASTRA25-11 vectors at signed `4c7ee50` make the prior
native expiry finding executable under the judge's explicit mapping, while the
0.2.5 clarification remains pending. They add five negative and two positive
vectors without adding a new defect. All 62 current artifacts validate; the
semantic supplemental inventory is now 61. Original seven vector hashes match
the frozen first-input bundle, and native `604af18` evidence is byte-identical.

Independent full supplemental runs at source `427fed5` and package `942bdee`
give 48/5/8 and 56/5/0. Every prior row, input hash and exact output is unchanged
after declared normalization. Only ASTRA25-11, OWN, REPLAY, UNKNOWN and BATCH
fail. BEFORE and BATCH-CONTROL pass, as does the existing null-deadline control.
These are R7-052/053 regression witnesses, not unrelated new findings.

Separate native per-operation checks isolate each expected refusal from any
prior forbidden write. Both runtimes pass three positive admission checks and
fail all seven negative attempts: at/after inherited expiry, own expiry, a
transitive known ancestor through unknown lineage, both same-batch proposal
orders, and expired exact replay. Every fresh negative wrongly admits records;
late replay returns the original success with unchanged state, which still fails
the required refusal. Full before/after semantic state is retained, including
replay storage, captures and package bindings. The script does not count a crash,
arbitrary error or state equality alone as correct expiry rejection.

Evidence in judge seat `.temp/`: `astra{22,23}-judge-round27-cases.json`,
`judge-round27-corpus-comparison-01.json`, `judge-round27-case-validation-01.json`,
`judge-round27-deadline-atomic.py`,
`astra{22,23}-judge-round27-deadline-atomic-first.json`,
`judge-round27-atomic-summary-01.json` and `judge-round27-first-integrity-01.json`.

Ledger remains 54 items: 41 fixed, 10 rejected, R7-052/053 implementation and
R7-054 mapping open. Canonical release/runtime bytes are unchanged; round-26
50/57 dual coverage and 106/28 established controls remain the verified baseline,
not a claim that the new expiry controls pass. No owner question, no deployment
qualification, score 1/2; continue until PARK.

## Round 28 — expiry package clarification verified

R7-054 closes at signed release 0.2.5 `6a04e8c`. K-AUTH-1, K-API-1/2 and
K-REF-1 now explicitly require live retention at the trusted current intake time,
strictly before each applicable non-null deadline, for all admission APIs and
original outputs/known-input closure on replay. Expiry returns not_authorized,
retryable=false before idempotency, including changed-intent conflict. Refusal
preserves original receipts and state without a purge side effect. This matches
the existing source requirements and judge ruling; no new owner choice is made.

Independent regeneration of all 94 JSON artifacts is byte-identical; all 34
checker controls detect the intended violation, including a planted expired
successful replay. Only P11 changes beyond release identifiers. Its first sixteen
operations and their exact expected results are preserved, as are all other 64
vectors and the reusable decision fixture. New private-purpose grants are
unrevoked, so the deadline negatives do not merely repeat earlier grant revocation.

The unchanged source `427fed5` gives 49/1/7 and unchanged package `942bdee` gives
56/1/0 on the full 0.2.5 corpus. P11 is the only semantic failure. Exact dual
canonical passes are therefore 49/57 on the expanded release. Runtime hashes
match these pins; the later source deadline-control file is a test-only addition.
No expiry implementation correction is claimed by accepting the specification.

Eight isolated package probes execute from the same valid prescribed prefix:
five expired fresh writes commit, two expired exact retries return the original
success without mutation, and one expired changed-context request returns
idempotency_conflict instead of the prior not_authorized. Full before/after state
and actual replies are preserved. A separate positive-trace fixture omits those
eight expired operations entirely, remaps only operation-result indices and their
declared normalization/predicates, and exactly passes all twenty remaining
operations, final view and postconditions. It proves the original controls,
before-deadline admission/replay and later unlimited same-key recovery oracle;
it is not a passing full P11 run or a waiver of the omitted negatives.

Canonical P11 exercises admit and admit_raw. Runtime closure must additionally
cover revise and declassify, transitive/incomplete-known inputs, both batch orders,
null/unrelated deadlines, current replay and complete refusal state. The seven
independent typed witnesses and earlier native first inputs remain unchanged.
Supplemental migrations to 0.2.5 remain explicit author work, not an implicit
conversion by the judge.

Evidence in judge seat `.temp/`: `judge-round28-package-review-01.json`,
`package025-*-01.log`, `judge-round28-package-signature-01.log`,
`astra{22,23}-judge-round28-release-first.json`,
`judge-round28-release-first-summary-01.json`, `judge-round28-p11-probes.py` and
`judge-round28-p11-probes-first.json`.

Ledger: 54 items, 42 fixed, 10 rejected, R7-052 and R7-053 implementation open.
No owner question. Seven source canonical gaps and eight canonical plus one
supplemental deployment case remain unsupported. Score 1/2, no PARK.

## Round 29 — source deadline correction verified

R7-052 closes at signed `4a14a56`. Independent full canonical 0.2.5 execution
reproduces all 65 committed rows and input/module hashes: 50/0/7 semantic.
Expanded P11 passes. Every established source control and six new deadline
groups pass, for 112 total including the five comparison-harness controls.

The native groups cover admit, admit_raw, revise and declassify, checking each
proposed output independently. A still-live exact retry preserves its original
receipt; equality/after expiry refuses without writes or purge, including a fresh
key. Transitive complete and incomplete-known closure, both batch orders, null
and unrelated deadlines, and repeated-proposal authorization precedence retain
valid positive controls. The shared traversal checks each proposed envelope
before deduplicating recursive input work; a later duplicate cannot hide an
expired output. The correction preserves the grant/scope and erasure contracts.

All seven unchanged migrated expiry vectors pass. Independent judge probes
reuse the original semantic operations and now pass all ten checks: three
positive admissions and seven exact non-retryable not_authorized refusals with
complete before/after state equality. Expired replay retains its original stored
receipt. First native and typed failures remain unchanged; no oracle is relaxed.

At this verification checkout the supplemental corpus intentionally has two
explicit profiles. Forty-one semantic cases from seats 25/26 use 0.2.5 and give
33/0/8; twenty seat-24 cases still use 0.2.4. Each of those twenty passes exactly
when explicitly executed with its original profile. Running them as 0.2.5 produces
only semantic_profile field mismatches, independently enumerated in the evidence;
these are not twenty implementation defects. No input is silently rewritten and
no unified 0.2.5 supplemental pass total is claimed before author migration.
All 62 artifacts validate against their own declared profile, and profile-only
migration round-trips to the preserved original corpus.

Evidence in judge seat `.temp/`: `astra22-round29-execution-01.json`,
`astra22-judge-round29-canonical.json`, `astra22-judge-round29-mixed-cases.json`,
`astra22-judge-round29-pending024-cases.json`,
`astra22-judge-round29-deadline-atomic-corrected.json`,
`judge-round29-profile-validation-01.json`, `judge-round29-source-comparison-01.json`
and `judge-round29-source-signature-01.log`.

Ledger: 54 items, 43 fixed, 10 rejected. Only R7-053 package expiry remains open.
Package `942bdee` still has its verified 56/1/0 first 0.2.5 result, so dual exact
canonical coverage remains 49/57 despite source P11 recovery. Seven source
canonical gaps and eight canonical plus one supplemental deployment case remain
unsupported. No owner question; score 1/2, no PARK.


## Round 30 — cross-issuer receipt order needs an owner decision

R7-055 classifies ASTRA24-12 as ambiguity, not an evaluator bug. The original
signed `4424598` native pair validates against the closed state/query grammar.
Independent isolated reader processes reproduce every actual field: both select
current d3 for the all-H1 path; changing the intermediate event/source attribution
to H2 produces ambiguous d1/d3 in source `4a14a56` and current d3 in package
`942bdee`. Durable records, runtime and policy remain unchanged. The original
representation-invalid preparation is excluded from semantic evidence.

Kernel §5.3's own ordered record and D-004/D-008 do not define the endorsement
meaning of an H1 edge pointing to an H2 canonical predecessor. Both endpoint
decisions remain H1, so foreign sequence ownership alone does not settle the
case. Bounded independent editor and attribution reviews explicitly distinguish
an issuer-local recommendation from a logically required reading. The package's
A07 supplies the graph representation without resolving that intermediate scope.

[OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) records the exact input hash, outputs,
source limits and viable owner choices. Issuer-local paths can ignore valid
foreign edges while retaining any all-H1 bypass; global endorsement can accept
the foreign chain. Declaring mixed edges invalid would be a separate admitted-
state/refusal decision. No exact oracle, transfer mechanism, package change or
new implementation verdict follows until an attributed owner decision. Prior
same-issuer R7-048/R7-051 closures remain supported.

Owner topic `q-authority-issuer` was created at
`$xI3um-5-5mtAfRLub6enUIlkEPrUbVS41wk0hCp6-4Y`, with owner-needed event
`$Ju7IuqWDcWw6JB87jbG-0K3yC4TWQ2WszJTNwNLZQHs` addressed to the convener for
routing. Other correction and coverage work is independent of this decision.
Judge evidence in seat `.temp/`: `judge-round30-issuer-probe.py`,
`astra{22,23}-judge-round30-issuer-first.json`,
`judge-round30-issuer-analysis.md` and `judge-round30-issuer-signature-01.log`.

Ledger: 55 items, 43 fixed, 10 rejected, one open implementation bug R7-053 and
one owner question R7-055. Latest verified canonical results remain source
50/0/7 and package 56/1/0, giving 49/57 dual exact passes. The native pair does not
enter vector denominators. Seven source canonical gaps and eight canonical plus
one supplemental deployment case remain unsupported. Score 1/2; no PARK.

## Round 31 — full semantic inventory passes; native recovery defect remains

R7-053 closes at signed `23b4d74`. Independent full package execution reproduces
all 65 canonical and 62 supplemental rows, input/module hashes and complete
actuals after only declared fresh-handle normalization. Canonical semantics are
57/57 and all 61 current supplemental semantics pass. All 27 product controls
and four comparer controls pass. Ten judge operation checks reuse the unchanged
seven deadline vectors: three positive admissions and seven exact atomic
not_authorized,false refusals, retaining original receipts on denied replay.
The shared traversal checks strict context.at expiry before node deduplication
and idempotency, across all four write APIs and current original-input/output
closure. Live admission/replay, null deadlines and same-key recovery remain
positive. Preserved first failures are not replaced by corrected results.

Signed source coverage `dbf4892` independently reproduces 57/57 canonical and
61/61 current supplemental semantics as well. All seven formerly unsupported
canonical paths now execute: B07, P08, S20, S24, S25, S26 and S27. Eight new native
erasure groups cover receipt replay/current authority, metadata-versus-purge
scope, invalid/unauthorized atomicity, partial/unreachable/independent custody,
unknown-lineage lower bounds, late writers, restore fencing and current external
witness reconciliation. Four availability/control groups pass alongside prior
controls. These are synthetic state transitions, with no deployment qualification.

The newly added 125th source control fails for the intended recovery assertion;
124 controls pass, including the five comparison-harness controls. R7-056 is an
implementation bug, independently reproduced from the unchanged validated first
artifact. An initially degraded public state with runtime memory already available
accepts the owner's set_availability available operation but remains unavailable
on the same query. A four-transition public-state matrix isolates only degraded
to available as failing. Foreign actor and undeclared coarse policy instead return
exact not_authorized,false with complete state unchanged. Successful recovery must
update current public availability while preserving policy pins, records, grants
and unrelated state; it grants no power to recover real infrastructure. Judge
classification event `$JwiSCClsftcbsOR8UrOJoe2h7NZWY12YYcjSgWm4S6c` authorizes the
source correction. Its original native first stays immutable.

All twenty seat-24 fixtures migrated explicitly at signed `27303e4`; reverse byte
substitution of the view-profile stamp restores the previous files exactly.
All 62 supplemental artifacts now validate at 0.2.5. Canonical input hashes are
unchanged from the prior source first run. Both independently reproduced report
sets match their committed rows; no expected answer or forbidden predicate is
relaxed to obtain the full semantic totals.

The convener holds R7-055 for Ivan in event
`$wrLtxOryOvNuOttDN4ofHbvs0INg6jS0hLEpgMJ58wk`. Both issuer-path readings and the
native separating pair remain recorded without an oracle or denominator entry.
This hold is not an attributed owner decision.

Evidence in judge seat `.temp/`: `astra{22,23}-round31-execution-01.json`,
`astra{22,23}-judge-round31-{canonical,cases}.json`,
`astra23-judge-round31-deadline-atomic-corrected.json`,
`judge-round31-report-comparison-01.json`, `judge-round31-availability-first.json`,
`judge-round31-availability-analysis.md` and `judge-round31-signature-*-01.log`.

Ledger: 56 items, 44 fixed, 10 rejected, R7-056 implementation open and R7-055
owner-question. Dual canonical semantics 57/57; supplemental semantics 61/61
in both readers. Eight canonical plus one supplemental deployment case remain
unsupported. Score remains 1/2 because the native recovery bug is open. No PARK.

## Round 32 — recovery closes; erase retry priority is a separate source defect

R7-056 closes at signed `87beb46`. Independent current source execution reproduces
all 65 canonical and 62 supplemental committed rows exactly, with unchanged input
hashes and the correction's module bytes. The 57/57 canonical and 61/61 supplemental
semantic totals are preserved. All 120 native tests and five comparer controls
pass. The original native recovery witness and judge four-transition matrix now
produce the required views/refusals; foreign actor and undeclared coarse admission
remain exact atomic not_authorized,false refusals. The expanded product matrix
also verifies that only public/runtime availability facts change. Original first
failure and expanded-matrix failure evidence remain immutable.

R7-057 classifies ASTRA22-09 as a source implementation bug. The original signed
`0529814` admitted initial state and operations validate. Independent isolated
reader runs reproduce changed ungranted receipt purpose and changed audience:
source `87beb46` returns not_authorized,false, while package `23b4d74` returns
idempotency_conflict,false. A fresh-key request with the changed context succeeds
in both readers, purges the same protected closure and discloses no refs.

K-API-1 explicitly treats a changed erase receipt_context as a different canonical
intent. K-ERASE-2 permits an authorized erase with an empty metadata-authorized ref
subset. Current erase operation authority still comes first; the stored-receipt
metadata check applies to exact replay, which actually returns those refs. A
changed canonical request returns a conflict without disclosing or changing the
stored receipt. Broad authorization priority cannot make its undisclosable refs
an operation-wide erase denial. This follows the existing explicit distinction,
not reader agreement or a new owner choice.

Both readers preserve the neighboring guarantees in independent six-case probes:
exact live retry returns the identical original receipt; exact retry after current
metadata revocation refuses not_authorized; changed intent after erase-authority
revocation also refuses before conflict; fresh changed-context intent succeeds
with empty refs. Every refused attempt preserves complete state and the original
receipt. The author's first native Refusal records only a code; judge wire
responses explicitly record retryable=false. Classification/correction event
`$eZJtQ5NtpfBEb7qFsk54ePTdCFPWyGbT_S4eBcV9FM8` preserves these boundaries and
requests supplemental encoding by its authorized case owner. No canonical oracle
or package change is required by this verdict.

Evidence in judge seat `.temp/`: `astra22-round32-execution-01.json`,
`astra22-judge-round32-{canonical,cases}.json`,
`judge-round32-availability-corrected.json`, `judge-round32-source-comparison-01.json`,
`astra{22,23}-judge-round32-erase-context-first.json`,
`judge-round32-erase-context-analysis.md` and both round-32 signature logs.

Ledger: 57 items, 45 fixed, 10 rejected, R7-057 implementation open and R7-055
owner-question held for Ivan. Dual canonical 57/57 and supplemental 61/61 semantic
passes remain valid; the native erase-context failure still blocks score 2.
Score 1/2; deployment 8+1 unsupported; no PARK.

## Round 33 — exact erase-context regressions accepted

Signed `66233ab` contributes two exact semantic fixtures for R7-057, preserving
the original `0529814` initial state: changed receipt purpose and changed audience.
Each trace includes complete erase, identical later retry with the original
receipt handle, the adjudicated changed-intent conflict, and fresh-key erase with
empty disclosed refs. Protected closure/custody postconditions, exact replay
identity, fresh-handle separation and forbidden success checks remain explicit.
These encode the already classified defect and introduce no new ledger item.

Independent full supplemental runs at the unchanged runtime pins reproduce
source `87beb46` 61/2/0 and package `23b4d74` 63/0/0 semantic results. Each new
source failure is exactly operation_results[2].code: not_authorized instead of
idempotency_conflict. Every older source row, actual and input hash is unchanged;
all older package cases remain exact passes. All 64 supplemental artifacts pass
closed shape, state/reference, integration-fact and normalization/forbidden
checks. Original native firsts remain distinct from these exact typed witnesses.
Canonical 57/57 dual evidence is unchanged; no new canonical execution or runtime
correction is claimed by accepting the supplemental pair.

A bounded restore follow-up rechecked K-ERASE-3's admitted external_witness fact.
True explicitly means current complete outside-domain verification; a stale or
incomplete inventory must receive false. Supplying incomplete verification while
retaining true would violate that fact, so it establishes no new semantic defect.
No such probe or owner choice was introduced. Deployment verification remains
unsupported. Analysis is persisted in `judge-round33-restore-scope-review.md`.

Other evidence in judge seat `.temp/`: `astra{22,23}-judge-round33-cases-first.json`,
`astra{22,23}-round33-cases-first-01.log`, `judge-round33-case-review-01.json` and
`judge-round33-case-signature-01.log`. The expected source runner exit is 1 for
exactly the two intended field differences; package runner exit is 0.

Ledger remains 57 items: 45 fixed, 10 rejected, R7-057 implementation open and
R7-055 owner-question. Supplemental inventory is now 63 semantic plus one
unsupported deployment case. Score 1/2; no PARK.

## Round 34 — final open implementation correction verified

R7-057 closes at signed `946cbd8`. The correction preserves current erase
operation authority, then compares canonical intent before attempting exact
stored-receipt disclosure. It changes no admission retention priority. Independent
full source execution reproduces all 65 canonical and 64 supplemental committed
rows and exact input/module hashes: 57/57 and 63/63 semantic passes. Compared
with the preserved typed first, only the two adjudicated refusal codes change;
all older actuals remain exact. Neither author fixture nor any canonical oracle
is modified.

All 123 source native tests and five comparison controls pass. Three new erasure
groups cover changed audience/purpose, revoked erase authority, exact replay after
read/use/metadata loss, fresh-key empty-ref purge, and an originally empty receipt
remaining immutable after broader metadata grants. The expanded first records
five intended wrong-code failures against the old runtime; old/new module and
control hashes independently match the preserved artifacts, with no setup errors.

Six independent judge probes rerun the original native input and neighbors. Both
changed contexts now conflict atomically; exact live retry preserves the identical
receipt; current metadata loss and lost erase authority deny atomically; fresh-key
changed context purges with empty refs. Every refusal preserves complete state and
the original stored receipt. Original `0529814` bytes and both `66233ab` vectors
remain unchanged.

The package runtime and test modules remain byte-identical to `23b4d74`, so its
independent round-33 supplemental execution and earlier canonical/control runs
remain applicable. All 64 rows in its newly committed supplemental report at
`348ea38` reproduce the independent first after only declared handle normalization.
No redundant execution or source-code intake is claimed for the package reader.

Evidence in judge seat `.temp/`: `astra22-round34-execution-01.json`,
`astra22-judge-round34-{canonical,cases}.json`,
`astra22-judge-round34-erase-context-corrected.json`,
`judge-round34-closure-review-01.json` and both round-34 signature logs.

Ledger: 57 items, 46 fixed, 10 rejected, no open specification or implementation
bug. R7-055 remains a filed owner question, held for Ivan without an oracle.
Current R7 score is **2/2** under the stated rubric, with full dual canonical
57/57 and supplemental 63/63 coverage. The owner-question pair stays outside
those denominators; deployment 8+1 remains unsupported. No new ledger item this
round. Continue the convener's quiet-round/PARK protocol; no PARK has been posted.

## Round 35 — a current restore obligation exposes a package defect

R7-058 classifies ASTRA25-12 as a package implementation bug. Signed `644c793`
preserves four native traces. The judge independently validates all initial
states, operations, queries and returned response shapes, reproduces every
operation/final-query/postcondition field in both readers, and verifies all
seventeen content-addressed before/after snapshots. The original native bundle
SHA-256 is `4bf7bac62cce5959d0300c86c59747b07661675763851ef2dc16e10d9f41329a`.

The separating input uses the unchanged old S25 snapshot with A and controlled
payload/backup, but no local erased/fence entry. A current complete external
witness supplies obligation A during recovery. Package `23b4d74` claims
reconciled/purged-within-boundary while leaving both sinks present, A unfenced and
A readable. With an affected sink unreachable it also claims success and opens
the global fence. Source `946cbd8` respectively reconciles the current obligation
or refuses erasure_incomplete,true atomically while retaining the restore fence;
its restore behavior is unchanged from the author's `87beb46` pin.

Both readers agree on locally known obligations and genuinely empty current
obligations. Every false-witness reconcile refuses with exact erasure_incomplete,
retryable=true and complete state equality; every restore-fenced query refuses
with erasure_fenced,false. These are meaningful positive and negative controls,
not a blanket refusal oracle.

K-ERASE-1/2/3, companion §6 and the source protected-service contract explicitly
require current outside-domain obligations, including later erasures missing from
an old backup. The witness here truthfully supplies A and current-complete
verification; it is distinct from the round-33 hypothetical incomplete witness
mislabeled true. The correction must reconcile incoming and retained obligations
and full content/custody closure before reopening, preserve atomic fencing on an
unreachable sink, and maintain erasure/fence/generation state for newly learned
obligations. Known/empty obligations, false witnesses, independent unaffected
content and late writers remain required neighbors. No owner or specification
change is needed; the native first remains outside vector denominators until its
authorized case owner encodes exact fixtures.

Classification event `$M8NvqvBJqj0P6G_HX3wtl3-FVKIbSUxxSZFXB9YCyvE` authorizes
the package correction and exact supplemental mapping. The round-34 score 2/2
was the adjudicated state before this next inbox batch; R7-058 now returns the
current score to **1/2** and resets the no-new-open-item condition. R7-057 and
other established closures remain valid.

Judge seat evidence in `.temp/`: `astra{22,23}-judge-round35-restore-first.json`,
`astra{22,23}-round35-restore-first-01.log`, `judge-round35-native-validation-01.json`,
`judge-round35-restore-analysis.md` and `judge-round35-native-signature-01.log`.

Ledger: 58 items, 46 fixed, 10 rejected, R7-058 implementation open and R7-055
owner-question. Existing canonical 57/57 and supplemental 63/63 dual passes
remain pinned evidence, without waiving this native failure. Deployment 8+1
unsupported; no PARK.

## Round 36 — exact restore regressions preserve the original witness

Accepted five exact supplemental vectors in signed `1cefcf9` under R7-058;
acceptance event `$iMI3b6URDc8d-vwo1lbBpFhGHcCsTJ5Dg3guKuO3Sq0`. All 69
supplemental artifacts validate against 0.2.5 closed schemas, admitted references,
integration facts, normalization and forbidden assertions. Two bounded controls
prove the existing forbidden checker detects retained obligated custody and false
successful reconciliation of an unreachable sink, with valid controls accepted.

The four original variants preserve every initial state, non-capture operation
and final query from immutable native `644c793`. Their sole additional operation
explicitly captures the already-observed restore-fenced read. The fifth adds only
an independent direct B, its declared lineage fact and controlled sink. Its
expected readable B and retained B custody follow the unaffected-content contract;
it does not authorize a blanket empty-view implementation. Expected direct views
use the existing S01 oracle and receipts/refusals use K-ERASE/S20/S25. No expected
output is inferred merely from reader agreement.

Both readers execute the entire new supplemental corpus independently. Source
`946cbd8` passes 68/68 semantic cases; unchanged package `23b4d74` passes 65 and
fails exactly ASTRA25-12, ASTRA25-12-UNREACHABLE and ASTRA25-12-INDEPENDENT. Known
and genuinely empty obligations pass in both. Every one of the 64 older artifact
bytes and source report rows is unchanged; all older package rows reproduce after
only their declared handle normalization. Both module trees match the previously
verified runtime pins. Canonical 57/57 dual evidence and the existing 128/31 control
runs remain applicable; no code or canonical package change occurred this round.

R7-058 stays open pending correction plus protected erasure/fence/generation,
complete refusal atomicity and late-writer checks. Exact fixtures do not replace
that native state evidence. Original bundle SHA-256 remains
`4bf7bac62cce5959d0300c86c59747b07661675763851ef2dc16e10d9f41329a`.

Judge seat evidence: `.temp/judge-round36-case-review-01.json`,
`judge-round36-case-review.py`, `astra{22,23}-judge-round36-cases-first.{json,md}`,
`astra{22,23}-round36-cases-first-01.log` and
`judge-round36-case-signature-01.log`.

No new item: 58 total, 46 fixed, 10 rejected, R7-058 open and R7-055 owner-question.
Current score remains **1/2**. Deployment 8+1 unsupported; no PARK.

## Round 37 — current restore obligations and late writers close R7-058

Candidate `104fbe8dd5be973698e1b226fd9a52bcb79a1d2c` closes R7-058 after
independent judge review. Candidate request is
`$Gi1NESKNu9thWv6mMTBMiAEW9CRCKzyBdCIfCE9Y6l8`. The runtime delta selects the
current supplied obligation closure, retains the coverage guard for known local
erasures, checks every affected controlled sink before mutation, and records new
erasure/fence/generation state before purging and opening recovery. No package
clause, expected oracle or source runtime changed.

Before correction review the judge independently reproduced all three additional
native late-writer firsts from signed `1138c5d`. The old package admitted an old-
generation derivative with state mutation, then incorrectly refused both current-
generation variants because recovery retained generation zero. Source `946cbd8`
met all three K-ERASE-3 expectations. The valid independent proposal has its own
review and direct integration fact; the author's earlier missing-review scratch
attempt is explicitly excluded. All six content-addressed snapshots verify.
These are R7-058 neighbors, not new ledger items or vector denominators.

The corrected package independently passes all 65 canonical and 69 supplemental
report rows: 57/57 and 68/68 semantic, deployment 8+1 unsupported. Every committed
row, module hash and full actual reproduces after only declared handle
normalization. All fixture bytes are unchanged; only the three previously failing
restore actuals differ from the round-36 package first. The source's expanded
committed 68/68 report likewise matches the judge's independent round-36 output.

All 30 package product tests and four comparer controls pass. A clean isolated
candidate archive using the byte-exact old `23b4d74` engine reproduces all seven
intended failures of the three new groups, exit 1 with no setup errors. The same
candidate tests pass with the corrected engine; all nine constructed initial
states and every exercised operation/response additionally pass independent
closed-schema and admitted-reference validation. The tests cover full complete
and incomplete-known derived closure, unreachable affected custody, unaffected
content, uncontrolled recipients and repeated recovery.

The original four native recovery inputs now have the required complete outputs
and protected postconditions. False-witness and unreachable refusals preserve all
engine data state and keep disclosure fenced. Known/empty and repeated recovery
remain valid without a spurious generation increment. The unchanged three native
late-writer inputs now produce stale_generation,true; erasure_fenced,false; and
an admitted independent current-generation record, respectively. Both refusals
preserve full engine data state, and independent admission retains A's fence.
The original `644c793`, `1138c5d`, package `b805582` and exact `390b208` first
artifacts remain byte-identical.

Source runtime remains `946cbd8`; only its focused erasure tests changed at
`b8189ba`. The judge reran all 12 erasure groups, which pass, and verified all
other source module bytes against prior pins. Combined with 117 previously green
unchanged controls, current source coverage is 129. This is explicit evidence
reuse, not a claim that all 129 controls were re-executed in round 37.

Judge seat evidence in `.temp/`: `judge-round37-closure-review-01.json`,
`astra23-round37-execution-01.json`, `astra23-judge-round37-{canonical,cases}.json`,
`astra23-judge-round37-restore-corrected.json`,
`astra{22,23}-judge-round37-late-writer-first.json`,
`astra23-judge-round37-late-writer-corrected.json`,
`judge-round37-pre-fix-controls-01.json`,
`judge-round37-generated-input-validation-01.json`,
`astra22-round37-erasure-checks-01.log` and
`judge-round37-candidate-signature-01.log`.

Ledger: 58 items, 47 fixed, 10 rejected, R7-055 owner-question; no open spec-bug
or impl-bug. Current rubric score returns to **2/2** with full dual canonical
57/57 and supplemental 68/68 coverage. Owner 055 remains held without a chosen
oracle; deployment remains unqualified. No new item this round. Continue the
convener's full quiet-round/PARK protocol; no PARK has been posted.

## Round 38 — corroborating restore reviews, no new intake

The next inbox batch contains the already-answered R7-058 correction request and
independent corroboration from astra-26 `a7fa673`, astra-25 `b949afb` and editor
`21221cb`. The judge verifies all twelve author-corrected snapshot hashes and
matches every actual, protected recovery postcondition and late-writer outcome
against the independent round-37 evidence. Package and evaluator trees are
unchanged since candidate `104fbe8`; no test rerun is needed for these report-only
confirmations. Audit: seat `.temp/judge-round38-intake-review-01.json`.

No new case, divergence, owner decision or unanswered directed request appears
in this intake. Score remains 2/2; 58 items comprise 47 fixed, 10 rejected and
held owner question R7-055. This is the judge's quiet round, not an assertion that
every seat has completed the convener's collective gate. Continue waiting for
PARK; deployment remains unsupported.

## PARK — final judge handoff

Convener event `$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg` explicitly
parks the collective at 2026-10-17 06:33Z, after independently checking the gate at
`1f92e91`. Every seat reported a quiet post-closure round. Judge rounds 39–40 and
subsequent quiet intake added no finding, owner decision or unanswered request.
The gate request and all seven quiet event references are preserved in seat
`.temp/judge-park-gate-review-01.json`; the actual PARK message is in
`.temp/judge-park-inbox-01.log`.

Final score is 2/2: package 0.2.5-draft `6a04e8c` validates; both evaluators pass
57/57 canonical and 68/68 supplemental semantic vectors. Final module hashes,
package bytes and all exact fixture bytes still match the independently reviewed
pins. Native first failures remain retained. All 58 items are classified: 47
fixed, 10 rejected, R7-055 owner-question. No open spec-bug or impl-bug remains.

R7-055 is held for Ivan without a chosen oracle or authority change. Eight
canonical plus one supplemental deployment vector remain unsupported; no real
custody, witness, authorization or erasure qualification is claimed. Final
[score](R7-SCORE.md), [verdict](verdicts/astra-27.md),
[owner question](OWNER-QUESTIONS.md) and [park note](parked/astra-27.md) are the
handoff. No further judge implementation/review task is pending.


## Reopened round 1 — D-009 received; verification gate recorded

Convener event `$7qVXDb4qnZcORPIQr_qJeUzKFAj9Md3ZRI_VLpdOSKk` reopens
only R7-055 for seats 21, 22, 23 and 27; seats 24–26 remain parked. The owner
approved D-009 on 2026-10-17. Judge pulled signed main to `2c3100d`, read the
mission, decision, kernel v0.3 §5.3 and full Russian review, and completed the
required identity/join/topics onboarding. The former PARK remains historical.

D-009 removes the source ambiguity. The selected relation is the nonempty
transitive closure of predecessor edges whose two endpoint events belong to
H under protected policy authority-event attribution. Filtering precedes
reachability; assertion-free intermediate events participate. An all-H path
wins even beside a foreign branch, and foreign-only changes cannot affect it.
Currentness and strict replacement succession share this relation. Missing
order does not reject a mixed graph or add a refusal code.

The bounded review task is to inspect the editor's 0.2.6 clause and exact
vectors, independently reproduce both evaluators' new-vector and complete
regression reports, preserve first disagreements, then close R7-055 and publish
dual coverage. Until that evidence exists, the owner decision is received but
conformance closure is pending; current score is provisionally 1/2. The prior
0.2.5 result remains 57/57 canonical and 68/68 supplemental semantic for both,
with 8+1 deployment cases unsupported. No old finding is retroactively relabeled
as an implementation bug merely because the owner has now selected a rule.

Reopening evidence: seat `.temp/judge-r055-readiness-01.json`,
`.temp/judge-r055-topics-01.log` and `.temp/judge-r055-round01-inbox-01.log`.
The next gate is 0.2.6 publication followed by independent dual verification.
Continue the required wait/inbox protocol through one quiet round and the new
convener PARK, or the 2026-10-17 22:30Z hard cap. Only the new PARK authorizes
finalization of this reopened turn.


## Reopened round 2 — supplemental regression version boundary

Astra-23 asks how to run the 68 semantic supplemental cases, whose immutable
expected views pin 0.2.5, while their authors remain parked (event
`$JKnjj1hDMNWG-LvRIQ5MB29ajPHRkFL0OhRTrG96vVc`). Judge directs both evaluators
to use their existing package-root options with frozen 0.2.5 package `6a04e8c`
and unchanged case bytes. Report current-runtime historical regression coverage
separately from canonical 0.2.6 coverage. No scratch oracle migration, author-file
edit or package-blind claim is needed. A separately observed wrong-profile result
against 0.2.6 is unsupported metadata, not a semantic failure or current pass.

All three active peers acknowledge their permitted roles. The editor prepares
the release; the source evaluator derives D-009 from source; the package evaluator
awaits publication and will preserve an unchanged-runtime first run before any
correction. No new finding or verification result is claimed in this intake.
Evidence: seat `.temp/judge-r055-round02-inbox-01.log`.


## Reopened round 3 — source-derived D-009 controls independently verified

Source first evidence `abc8511` predates 0.2.6 intake. Judge independently reruns
all 129 native source controls and five comparer controls: 134/134 pass. Module
hashes exactly match the producer report; existing runtime remains `946cbd8`.
The five new D-009 groups cover the original pair, assertion-free middles,
no contraction, an all-H bypass beside a foreign path, foreign-part invariance,
all 256 four-event DAG/issuer variants, and actual replace/correct operations.
Currentness, CAS head and strict succession agree with the independently defined
Boolean-matrix closure. Rejected foreign-only writes return the existing
`authority_receipt_required,false` and preserve complete adapter state; nearby
own-path writes succeed.

Judge additionally applies full package schema and consistency validation to all
282 constructed state instances (275 unique) while rerunning the five groups:
all pass. Policy event issuer is deliberately independent of source-carrier
issuer in those controls. A bounded in-memory global-order plant reproduces
exactly the intended foreign-middle currentness assertion failure, with no setup
error and the all-H positive passing. No runtime or fixture is changed.

Local evidence: `.temp/judge-r055-round03-source-controls-01.json`,
`.temp/judge-r055-round03-source-input-validation-01.json`, and the individual
`judge-r055-round03-source-*-01.log` files in the astra-27 seat. This verifies
source-derived controls only. Canonical 0.2.6 and both complete vector reports
remain pending; R7-055 stays verification-pending and the current score is 1/2.


## Reopened round 4 — unchanged source historical regression verified

Astra-22's signed `0bf20dc` reports 68/68 semantic and one unsupported deployment
case against the unchanged 0.2.5 corpus. Judge independently reruns all 69 rows:
input hashes, exact normalized outputs and statuses match the committed report.
The entire checkout package tree equals `6a04e8c`, avoiding the source runner's
documented limitation that `--package` alone does not relocate transaction
Shapes. Any later historical run with a changed runtime must keep both grammar
paths pinned in an isolated checkout. No input or expected output is migrated.

Evidence: seat `.temp/astra22-judge-r055-round04-cases-0.2.5.{md,json}` and
`.temp/judge-r055-round04-source-historical-review-01.json`; producer
`impl-astra-22/runs/d009-0.2.5-regression-first.json` and its provenance companion.
Runtime remains `946cbd8`. Current canonical 0.2.6 coverage remains pending;
this historical regression is not included in its denominator. No new finding.


## Reopened round 5 — 0.2.6 accepted; package first mismatch preserved

Release `77b951eb86d5ba9198921d058930884918a39942` maps D-009 exactly in
K-REV-3. Judge independently regenerates all 103 JSON artifacts byte-identically;
14 schemas, 14 domains, one fixture, 74 vectors (66 semantic/eight deployment),
52 clauses and 38 intended checker plants pass validation. Every prior JSON
artifact (94) retains its complete structure/content except declared version
values. S34/S35 initial state, operations and query exactly equal the unchanged
original foreign/same-issuer probes. The original bundle SHA-256 remains
`8224829a810a97c79fef81cb18f0d650b59ffc84a3262bdef09b1ea900c521b3`.

Independent induced-subgraph closure agrees with each new oracle: S34/S37 are
ambiguous; S35/S36/S38/S42 select d3; S39 refuses replace/correct with the existing
code, permits ordinary import, keeps candidates ambiguous and distinguishes CAS;
S40/S41 accept succession, preserve replay and refuse stale CAS. S34/S37 and
S36/S38 change only the foreign predecessor list, retaining identical complete
expected reports. S42 independently checks the protected event-issuer axis.
No behavioral oracle correction or new refusal code is indicated.

Judge first runs: source runtime `946cbd8` passes 66/66; unchanged package
runtime `104fbe8` gives 64 pass / two fail / zero unsupported semantic. Both
leave eight deployment vectors unsupported. Package first `1be6026`, reported
before its correction, preserves the same S34/S39 failures: forbidden global
order and a forbidden replacement with cut/dirty/idempotency consequences.
Every input/module hash and status matches. Seventy-three complete rows match
under declared normalization; S39 has the same difference paths, with only four
fresh nonce fields differing in forbidden unexpected receipt/view outputs.
Those extra handles remain failures, not an expanded normalization allowance.

The convener's PACKAGE LANDED event is
`$WTb-jdx1xZXxlfS2LIDbJgLJbttB8s-9sxOtjCz9uKY`; the source seat preserved
its independent controls and historical report before new-package intake.
Judge evidence: seat `.temp/judge-r055-round05-package-review-01.json`,
`.temp/judge-r055-round05-package/` (isolated regeneration), and
`.temp/astra{22,23}-judge-r055-round05-canonical-first.{md,json}`. A first
comparison-script optional-field KeyError is recorded and corrected in the audit;
it was not an evaluator error. R7-055 remains verification-pending for the
required package alignment; the earlier ambiguity is not retroactively a bug.
Current score 1/2. No new ledger ID or owner question is needed.


## Reopened round 6 — source canonical first matches; harness version defect

Source signed first `31d77d2` reproduces all 74 canonical rows exactly, including
input hashes, normalized outputs and statuses: 66 semantic pass, zero fail or
unsupported; eight deployment unsupported. Its runtime and all 23 Python modules
remain at the pre-package `abc8511` freeze. The complete control rerun has 133
passes and one failure in `test_excluded_record_has_no_forwarding_effect`.

R7-059 classifies that failure as an implementation control-harness profile bug.
The test feeds historical 0.2.5 expectations to a live 0.2.6 adapter. Judge
reproduces the exact two semantic_profile differences and independently executes
the second pair member that the first failing assertion prevents the test from
reaching. Both variants have only those two metadata differences; explicit
copied expectations with only the declared labels advanced compare cleanly.
This does not mask another behavioral mismatch or authorize original fixture
changes. The owned harness must declare and audit its version-only copies,
retain negative/positive assertions and rerun complete controls/canonical checks.
No source runtime correction is indicated. Decision event:
`$uu1YAT4x6_6pzGAo0MiCwVPWZMPoXTpBNGZi3c1Nc3Q`.

Evidence: seat `.temp/judge-r055-round06-boundary-review-01.json` and
`.temp/judge-r055-round06-boundary-copies/` with original/copy hashes and exact
changed paths; first control evidence remains at `31d77d2`. This bounded harness
alignment was triggered by the D-009 release, without reopening earlier semantics.
Score remains 1/2; package alignment and R7-059 correction are pending.


## Reopened round 7 — D-009 conformance closure and score 2/2

Verified at 2026-10-17 19:07Z. R7-055 is **resolved by D-009** and R7-059 is
**fixed at c7e86d5**. Both evaluators independently and exactly pass all 66
canonical semantic vectors of 0.2.6 `77b951e`, including S34–S42; neither has a
semantic failure or unsupported case. Both also pass all 68 unchanged historical
semantic cases under exact 0.2.5 `6a04e8c` grammar. The latter remains a separate
regression denominator. Deployment is explicitly unsupported: eight canonical
and one historical case in both readers.

Package candidate `5897520b6ca9fb4772d728fecf4a33a392b1905d` adds only the
protected-issuer restriction before the shared receipt reachability traversal.
The existing caller checks, same relation for projection/CAS/succession,
assertion-free events and ordinary mixed import remain intact. Judge reproduces
all 74 canonical and 69 historical report rows, module/input hashes and exact
normalized outputs. All 38 controls pass: four new current-profile groups, 30
legacy groups with frozen 0.2.5 grammar and four comparer groups. The legacy
`--spec-root` option makes that historical boundary explicit without fixture
migration. The old runtime produces exactly eight intended new-control failures
and zero errors; all-H/direct positive subcases remain valid.

The independent package native audit checks full state and response grammar on
125 state instances (74 unique), 25 writes and 11 exact atomic refusals. All
engine data except the immutable grammar object is preserved on each refusal.
The 64 bounded three-event DAG/attribution/list-order variants, two exact
invariance pairs, both revision relations, same-key recovery, ordinary import,
ambiguous CAS and authorized replay pass. This is bounded conformance evidence,
not a proof over arbitrary deployments or graph sizes.

Source candidate `c7e86d5ea9794577b200b033649bfac0cf197ac0` changes only the
profile-binding test; product runtime remains `946cbd8`, and its other 22 modules
match `abc8511`. Judge reruns all 129 native plus five comparer controls and
canonical 66/66. Two copied fixture audits match every hash and exact metadata
delta; both recursive guards detect a planted non-version actor change before
execution. All 74 canonical rows still equal immutable first `31d77d2`.

Original `4424598` native input/first outputs, package first `1be6026`, source
first `31d77d2`, all historical case bytes and all 103 reviewed package artifacts
remain unchanged. Current dual normalized outputs match each other and the
independently reviewed expectations. Local evidence in the astra-27 seat:
`.temp/judge-r055-round07-closure-review-01.json`,
`.temp/judge-r055-round07-{source,package}-execution-01.json`,
`.temp/judge-r055-round07-package-native-audit-01.json`,
`.temp/judge-r055-round07-package-old-controls-01.json`,
`.temp/astra{22,23}-judge-r055-round07-canonical.{md,json}`, and
`.temp/astra23-judge-r055-round07-historical.{md,json}`. The source historical
report remains the unchanged round-4 run. Earlier package/source controls and
original input validation are indexed in reopened rounds 3–6.

Ledger: 59 items, 48 fixed, 10 rejected and one resolved owner ambiguity.
No open spec-bug, impl-bug, owner question or unclassified submission remains.
Current R7 score is **2/2**. The judge now reports closure and waits through the
required quiet round for the new convener PARK; this commit does not itself park
the collective or qualify any protected deployment.


## Reopened round 8 — quiet judge round after closure

The editor's independent review `1e222f6` accepts package candidate `5897520`:
66/66 canonical, complete normalized report reproduction, four native groups,
11 atomic full-state refusals and eight intended old-runtime failures. The
prior audit-format question was answered by metadata-only `fddb403`, describing
typed-map hash serialization and run-local post-write nonce hashes. Every prior
audit field, runtime/test module, vector and package artifact remains unchanged.
Judge's own native audit already uses literal state equality within each trace;
no cross-run nonce equality or extra conformance normalization is claimed.

This post-closure intake adds no case, divergence, package change, owner question
or unanswered judge request. Module/package/case hashes match the complete
round-7 review; no new test run is warranted. Evidence: seat
`.temp/judge-r055-round08-inbox-01.log` and
`.temp/judge-r055-round08-quiet-review-01.json`. Four judge-generated migration
scratch files were moved from the otherwise empty repository `.temp/` into seat
`.temp/judge-r055-round07-source-migration-copies/`; exact hashes and paths are
preserved in `judge-r055-round07-scratch-moves-01.json`. Checkout is clean.

Score remains 2/2; all 59 ledger items are closed (48 fixed, ten rejected,
R7-055 resolved by D-009). This records the judge's quiet round only. Continue
the required wait/inbox protocol until the convener confirms the collective gate
and explicitly posts the new PARK.


## PARK — D-009 bounded-round final handoff

Convener event `$wTjjxPAdO1lPYyIX7BgMky5ptiS0vPzX6HGGgE99C0U` explicitly parks the
reopened round at 2026-10-17 19:12Z after checking the gate at `715d7a7`.
All four active seats recorded a post-closure quiet round; seats 24–26 remained
parked. The complete quiet-event set and unchanged evidence pins are preserved
in seat `.temp/judge-r055-park-gate-review-01.json`; gate request is
`$qt1Mrqziy6K4bZdyih74rXWgKmaGcyZFgsHLCc66qW0`, and the actual instruction is
`.temp/judge-r055-park-inbox-01.log`.

Final score **2/2**. R7-055 is closed by D-009, implemented in package `77b951e`
and verified against source runtime `946cbd8` / harness-report `c7e86d5` and
package runtime `5897520`. Both pass 66/66 current canonical semantic vectors,
including all nine D-009 vectors, and separately 68/68 unchanged historical
0.2.5 semantic cases. R7-059 is fixed. Ledger: 59 items, 48 fixed, ten rejected,
one resolved owner ambiguity; no open finding, owner question or pending intake.

All original first failures, input bytes and reviewed runtime/package hashes
remain preserved. Eight canonical and one historical deployment vector remain
unsupported. The final [score](R7-SCORE.md), [verdict](verdicts/astra-27.md),
[owner-question closure](OWNER-QUESTIONS.md) and [park note](parked/astra-27.md)
record the completed scope and limits. No further judge correction or directed
review remains. Finalization ends the seat's wait loop; no background service
was started.
