# astra-03 evidence and research worklog

Lens: semantics and formal core. Research only; no implementation, builds, source modifications or task-board writes. Mission-specific tracking lives here and in the verdict.

## Source snapshots, 2026-10-14

- Research clone synchronized with `git pull --rebase` before reading the mission and sketch.
- `wiki`: `94aebceca3af6a904b73644fb973e201762af8e2`.
- `swarm-platform-architecture`: `567b07701bdf32cdebc516e38e6f0321fc5253a0`.
- `curator-spec`: `eb1f08c6c66cedc52d9e09553fb791367f334704`.
- `swarma-session-host`: `255523d43129538b7e7064a0dbfc0b06713bb7e2`.
- Source clones are read-only and were not pulled.

## Platform evidence

1. Base: `memory/inputs/SKETCH.ru.md`, part 1 §§3–5 and §10; part 2 §§3–8. Correctly separates epistemic, verification and decision status; scopes guaranteed invalidation to registered dependencies; explicitly permits erasure; explicitly defers full ATMS in its platform-specific staging. Criticisms must not erase these concessions.
2. `wiki/book/ru/09-pamyat.md`: process memory belongs to the board; personal memory, persona and procedural skills differ; provenance-bearing memory ladders and immutable session snapshots are proposed; external facts are quarantined; notes grant no rights. Git-backed files are the earlier proposed default, not a currently enforced safe shared store.
3. `wiki/book/ru/10-sny.md`: dreams are explicitly simulated rehearsals, not just consolidation. Dream outcomes cannot qualify real checks; dream memory is quarantined. Runtime/evidence context therefore needs an explicit real versus simulated discriminator. Summarization may not launder it away.
4. `wiki/book/keeper/ru/09-zhurnal-i-vosstanovlenie.md`: journal writer is deterministic; fold order is `seq`, not wall time; invalid transitions are rejected; duplicate events are idempotent; recovery reconciles effects before new work. This is an existing authority, not material for a memory-owned replacement.
5. `swarm-platform-architecture/vision/contracts/handoff-package.md` §§1–6: audience-bound projection at committed watermark; per-item provenance; exact pins; protected-source references; reauthorization; redacted derivatives have new identities; partial seed is not a restore. Memory views should reuse these principles without becoming handoff authority.
6. `wiki/book/swarma/ru/16-postskriptum.md`: attestation binds contract version, candidate, policy version and environment; verdict has pass/fail/undetermined; reviews cannot be transferred across candidates. Memory must preserve these exact scopes.
7. `curator-spec/conformance/README.md` §§1,3,5–6 and `GOVERNANCE.md`: normative prose, schemas and vectors jointly define conformance; implementation behavior is not normative; schema validity is not qualification; exact suite/implementation/platform evidence matters. This is the right governance precedent for a memory semantic profile.
8. `curator-spec/cips/CIP-0013-machine-base-context.md`: machine base is explicitly configured and approved; suggestions are not consent; source trust checks persist. Memory cannot enter that path as an instruction merely because recall ranked it highly.
9. `skill-project-management/pkg/board/query/activity_ledger.go`: mirrored activity rows are derived; underlying ledgers remain authoritative. `activity_correction.go`: correction/supersession is privileged append-only evidence referencing an earlier event, not editing it. Memory revision must similarly avoid rewriting source decisions.
10. `waggle/spec/waggle.md` §§5,7: communication classes and author authority differ; reports are quoted data; permission gates remain outside the model. Memory content can inform, not act as `cmd`, approval, or authority.

## Primary prior art (accessed 2026-10-14)

- Johan de Kleer, *An assumption-based TMS* (1986), author-hosted paper: https://dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf ; publisher identity https://doi.org/10.1016/0004-3702(86)90080-9 . ATMS keeps assumption environments as well as justifications. Ordinary labels exclude inconsistent environments; applications must specify what contradictions mean. Our bounded DAG proposal deliberately does not claim full ATMS semantics.
- de Kleer, *Extending the ATMS* (1986), author-hosted paper: https://dekleer.org/Publications/AIJ%20Version%20Light%20Copy.pdf . Follow-up for default reasoning and arbitrary propositional expressions; not an MVP requirement.
- Bourgaux, Bourhis, Peterfreund, Thomazo, *Revisiting Semiring Provenance for Datalog* (KR 2022), https://arxiv.org/abs/2202.10766v2 . Recursive provenance has multiple nonequivalent semantics, and unrestricted derivations may be infinite. A named engine alone does not define a memory contract.
- Přenosil, *Four-Valued Logics of Truth, Nonfalsity, Exact Truth, and Material Equivalence* (2020), https://doi.org/10.1215/00294527-2020-0025 . The same four-value carrier supports different consequence relations. A four-label status table is not a complete inference language.

All derived counterexamples and recommendations below are this seat's analysis, not claims that prior work evaluated Swarma.

## Research state

- Mission and all 778 sketch lines read.
- Onboarded as `ivmbp_swarma-memory_astra-03`, joined room, inspected topics and convener opening.
- Candidate `f-bounded-inference`: `$OBDtFuUr2q0hTYIsRiTtWssnyOD-dUIel-auBGhnyYU`.
- Candidate `f-conflict-semantics`: `$S11M0JLIejp2VDPHjWALSFSFEJXh6sGbPwOxpC91fzo`.
- Findings remain candidates until a different seat confirms them; no finding file yet.
- Tool readiness: `.temp/astra-03/tool-readiness-01.log`, `a2a-help-01.log`, and `a2a-skill.md`. One read-only discovery command used a nonexistent CIP glob and failed with zsh `no matches found`; replaced with `rg --files` and exact path. No workflow relied on that failed query.
- Next: publish draft design/verdict, seek cross-five challenges and scores, then iterate through mission rounds until PARK.

## Round 2 evidence and corrections

- Signed and verified publication: `877cfdf1568bcafce0ecd063f88f2d8e99910e63` (signed rebase of `d49eddb`). Five files, two peer-confirmed findings. Source-boundary confirmations and 23 draft vectors recorded there.
- Directly inspected user-manager `spec/helper.md` §§2,4.4.1: `not_recorded` requires complete authoritative evidence; `unavailable` is never absence. Directly inspected dispatcher `spec/dispatcher.md` effect/reconciliation contract: a journaled result is not fresh admission authority, and receiver-owned observation does not mutate. Directly inspected broker `spec/broker.md` §6.4: a valid old snapshot cannot witness its own rollback; outside-domain evidence is required. These reinforce coverage and retention semantics without making memory a control-plane participant.
- Verified source mirror gap directly in board `pkg/board/query/activity_ledger.go` lines 53–85; posted confirmation `$xzDm_O3PeUE8MD5xDjVIfjyrUtbwb5KtSExaKegqSm8`.
- Opened the FLAIRS-31 primary paper https://cdn.aaai.org/ocs/17599/17599-77711-1-PB.pdf (2026-10-14); its abstract/§2 explicitly distinguish the four-valued carrier from a conditional satisfying modus ponens.
- Astra-06 independently confirms both findings in `$6jxHbLsDl-Lkefu_yhwLyBeLhFIr4aFr8vtcXgP56qg` and `$9Og11QdbR3N1C-_IDJ_7DOz5rCLDQFEO0JmC0FlyiBM`; wonder-01 and wonder-02 separately confirmed both in-room. Record files now exist.
- Revised recommendation R7 from initial 2 to 1 before first publication: draft vectors and a profile sketch are not full closed record schemas. No prototype or conformance execution occurred.
- Accepted astra-04/01 challenge: document-only M0 does not require a daemon. Separate the semantic contract from reviewed-register and managed-service deployment profiles.
- Adopted astra-02/05 erasure closure and view inference findings; directly checked their cited broker restore doctrine. Add durable erasure fence, outside-domain witness, explicit custody/rights boundary. Telemetry is inventoried as a sink; specific evolving OTel convention details are not relied on here without independent web verification.
- Astra-02 `$mBVrz35sCx2C_g0mVVVpJB0440Y4AoASEcsfFJza8DM` and astra-06 `$CX7dxB6U3_Gt7xaJ6irKNkIFR_eWBh0dPjOEyQgH3TM` identified a real contradiction in my original S13: exposed global sequence reveals hidden activity. Accepted in `$aj-ZpyPOcKqLo4UAkX9Vp7UD-DoPLNhsnAo_Yv6SMfY`; protected internal cuts and hidden-activity-independent external handle semantics now specified, with S24–S26.
- A patch attempt failed to match one whole paragraph and applied no changes; replaced by asserted exact text substitutions. This was an editing failure, not a research/tool assumption.
- Round protocol used `a2a wait --room swarma-memory --timeout 20m` as a persistent exec session (no short process timeout), followed by `a2a inbox`. Subsequent rounds continue the same contract until PARK.

## Round 3 exact-artifact calibration

Read the full `bounded-evidence.md` at `56d18ee`, including its protected custody and erasure section. Exact scores: protected service `[2,2,2,2,2,2,1,2]=15`; documentary P0 `[2,2,2,1,2,2,1,2]=14`. This agrees with astra-01/04; my earlier hypothetical fully guarded register score of 15 is not substituted for the filed documentary artifact. Metadata correction published signed/verified as `476ec3618c7c55d471a572454aa7e4aba772aab6`; attached for peers at `$YTU_qiVaSSi9UM98yW1b7ShGNA8MMDkK3IgcIJIwlA8`. Owned Markdown links and `git diff --check` passed. Waiting for refreshed exact-text review; no new semantic finding.

## Round 4 assembled-artifact review

- Read `bounded-evidence.md` at `0ce0094` and its complete diff against `56d18ee`. Content SHA-256: `9c8f63fd8aad3d44081b93225f727e504468297cadc21ab1d0973903d28c0599`. The assembled file now incorporates companion `476ec36`, aligns all five record kinds, treats views as derived and closes global-cut/handle/admission-receipt metadata disclosure. Confirmed exact vectors: managed `[2,2,2,2,2,2,1,2]=15`, documentary `[2,2,2,1,2,2,1,2]=14`, event `$p6gek454MWjxXasqM_alguzPwr9bffWW2c8AiyLIgC8`.
- Accepted the stricter retrospective reading from astra-04/05/06: `56d18ee` alone is 14, since its raw-cut wording was ambiguous; the earlier 15 assumed the corrected companion. This supersedes only that exact-file attribution, not the original independent base scores or current composite score.
- Astra-06's exact review of `476ec36` confirmed S24 metadata and S25/S26 restore/late-writer changes at design level, event `$ZXyxc2K3znMXyC3wI7IiUxKX4XSOjjmCRfzeGdzgP-A`, unchanged 15-point vector. The refreshed companion review is complete.
- Read astra-04's `memory-service-admission.md`; independently inspected user-manager `spec/helper.md` §§8–8.1 and session-host `spec/session-host.md` §3.1 at the same pinned source heads. These support the new managed-profile admission gate, including installer/operator-owned service rows, current UID generation, authenticated server and declared socket/resolver boundary. They are specification gates, not evidence of deployed enforcement, and do not apply retroactively to documentary M0.
- Source snapshot audit `.temp/astra-03/source-snapshot-check-01.log`: every cited file matches its source clone HEAD. No source clone was pulled or modified. Published own round-3 calibration as signed/verified `b056c8329ff92fa00aa746d6fc7c0942a2239b3e`.
- No new semantic mechanism or finding. R7 remains 1; full schemas and precise conformance fixtures belong to the follow-on RFC.
- Exact assembled-file confirmation arrived from five 2: astra-04 `$ZHOqMsgPsMRvYmQ7oOiijzHHx4oGmE-89-RrG36iArE`, astra-05 `$W6Z420vc49y3Eflx2Xn5ti_MQNDmd58lKsVT549kVVA`, wonder-03 `$ZeuRdPyKP2twOa9nqwmn_a9KVVn1losLGgFDyxoYeMg`. Their full-read/diff/hash evidence matches this seat's own read; all rows match on managed 15/documentary 14. Mission two-five proof is satisfied at design level; no cross-host upgrade or executed qualification is inferred. Await cross-host challenge or PARK.

## Round 5 resource-envelope refinement

- Astra-05 proposed hidden workload exhausting a shared query/admission/storage pool while the visible graph stays identical: `$o7sd2ib0EzNRlJeGf19MijoAiudZdGw678GfcHmG_u4`. Its observable refusal/incompleteness is not removed by opaque errors or by excluding strict timing from the threat model.
- Independently confirmed the counterexample in `$WhvxJRzL5wS-wZsiFZblEa2XuvFCPKlLUYnPHYPDuxs`. Resource envelopes must track the disclosure boundary, which may be narrower than a knowledge-space. A policy-admitted aggregate availability release is intentional leakage, not an automatic exemption; the existing policy owner must define it before testing. Equal-envelope/equal-admitted-availability comparisons must still preserve success/refusal/completeness.
- Added S27 and explicit comparison conditions to the semantic companion. S06/S17 now explicitly call their cuts protected, avoiding ambiguous public-watermark shorthand. This is a refinement of the existing view-inference contract, not a new finding or infrastructure request. No score change, test execution or source modification. Exact proof history remains pinned to `0ce0094`/`476ec36` until the new text is independently ratified.

## Round 6 exact refinement closure

- Published the companion refinement signed/verified as `9bafff829e9233b5510ef827ca79a6707d69ae64`, SHA-256 `62ae18cbec7c4be25764f8da0e8084d3b434ac224cc121f09b2304f97ce7aafd`, attachment `$univofQFsdHL7qP5MnFgzNHrp6egmMD1-NpsRHvFECQ`.
- Exact independent review: astra-06 `$c1AGA1adC-yFt8xyemrZ0ILx04xmwOa1Q7S65uJWJ2U`; astra-05 `$kuyKKxWMU00hDn_Ou8Tl1WRVz02m1_XHGJeM-o8uRfA`; wonder-03 `$4dBbaVEN3sLeIYmqVuwZ_2D1IrKbtA60vc64nNnP4Ro`. All confirmed the specified comparison scope without a score change.
- Read the complete assembled `0ce0094` to `5d96e7020053370cb03ad4f243d07157d798d696` delta and resulting clauses; verified its signature and SHA-256 `50f77834992bcbe64358b7fea771f0ef3a8a94f524bcd3d22d8bf43377fd85dc`. It pins the new companion, states selection/accounting before logical budgets, adds fixed-envelope and pre-admitted-degradation vectors, and preserves historical review identities. Own exact confirmation `$wRsGJyOVsic3HCBkepD-f8F3m0VRv1xgRsVd2rPigvI`.
- Fresh exact assembled agreement from astra-06 `$PiCCXD-mxfgOPA49NQvnIXKBbl40CZXGqgZ8o1MtBF8` and astra-05 `$vFk2PtdiSVjBeEzpiQMAW3NfZzpGAqbOdtJWxhR8Gzk`, both five 2. Managed `[2,2,2,2,2,2,1,2]=15`, documentary `[2,2,2,1,2,2,1,2]=14`. This closes the current two-five proof; it is not a cross-host or empirical qualification.
- No new finding, score change, source mutation or implementation. No addressed semantic challenge remains unanswered. R7 schemas/fixtures, corpus policy, any public availability tradeoff and measured pilot value remain future work. Ready for PARK while retaining the mandated wait/inbox loop.
