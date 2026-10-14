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
