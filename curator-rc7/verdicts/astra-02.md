# astra-02 — login/readiness/store/preparation verdict

Status: **provisional, round 2**. Reviewed PLAN as still present at `9d26855`,
peer launch refinements at `95ced00`, C0 at `b3d5e66`, and the token API split
at `7e93dd9`. The synthesis is still the round-1 draft at this freeze; leaf
improvements do not silently upgrade its score. No implementation or
qualification run is claimed. The five L15 leaves were initially published
at signed `b4d55ab`; this revision adds concrete installer/preserve-lock
controls and resolves publication ownership. Every test remains proposed
implementation work, not a passing report.

## Plan rubric

| Criterion | Score | Evidence and remaining bound |
|---|---:|---|
| P1 Traceability | 1 | L15-0..4 cite all login-readiness clauses and semantic rows; synthesis still has provisional C/R/H/X placeholders and awaits astra-03 integration |
| P2 Bounded leaves | 1 | Login policy, metadata, process ceremony and orchestration are separate; H1+/X1+ are not yet bounded delivery leaves |
| P3 Negative evidence | 1 | L15 and snapshot/token leaves pair refusals with valid controls and post-failure state; the full synthesized leaf set is not yet complete |
| P4 Ordering | 1 | Shared-path serialization is present, but round-1 PLAN still makes all snapshot publication wait on capture and retains retired duplicate G0 names; agreed C0/L15 and M2/SNAP-CLI splits await synthesis |
| P5 Unblocking | 2 | Muse v4 work precedes unrelated prepare/snapshot/token work; Codex successor allocation is kept separate |
| P6 Release honesty | 1 | Explicit publication/qualification and route-specific D4 gates are good; final feasibility under Muse quota and complete carrier/hosted split still need closure |

This is a review of a proposed plan. A plan score does not mean code is ready
or a supported launch capability can be enabled.

## Top risks and evidence

1. **Two Codex delivery authorities.** At spec `5509499`, v4 carries
   `credential_store.config_overrides` while CIP-0018 requires a successor
   `codex_settings` payload. L15-0 and astra-03 agree on a fresh successor,
   selection-only agreement metadata and one settings payload. Never widen v4.
2. **Status executes more than the credential helper.** Curator `0d00a109`
   `internal/envprofile/status.go:1140` and `managed.go:2386` invoke version
   probes, conflicting with login-readiness §1.1's no-agent-execution rule.
   The full CLI tripwire and spec reconciliation are mandatory.
3. **Managed Muse's configured native is effective file.** Environments §7.4
   overrides the generic native-preservation story. Separate configured and
   effective reporting; reconcile explicit-keychain diagnostic and ambient
   backend precedence before coding tests. Credential-source conflicts are
   not merely backend-variable precedence.
4. **Prepare can appear helpful while changing authority.** Current
   `Install(Use=false)` activates on an empty machine (`envprofile.go:911–919`),
   so L15-4 needs an installation-only seam, not pointer restoration. Reuse
   `managed.go:2599–2607` PreserveLock checks rather than ordinary migrating
   repair. Preserve every current marker; headless is entirely report-only;
   unknown never starts login. OpenCode unknown remains an aggregate failure.
   See [the source finding](../findings/prepare-install-activation.md).
5. **Source-home presence is not runtime-home authentication.** Claude's
   native identity depends on exact `CLAUDE_CONFIG_DIR`. L15 has no assumed
   snapshot login API; HOST-HOME and the protected final executor must define
   the destination route. Never copy a home credential to make relocation work.
6. **A released v4 reader is not Codex/Muse qualification.** Fresh read-only
   agents-management `acae871` (v0.5.66), `curator_context.go:715,725`, refuses
   explicit Codex stores, and Muse `personal_context.go` admits only the exact
   1.4.7-R6101.1 exclusion build. These are inspected code facts, not executed
   tests. The stale mission source checkout is not substituted for this pin.

## Setup-token design rubric

Scoring the proposed design in `designs/setup-token-local-source.md`, not
runtime support. Readiness/source mapping and no implicit home-login fallback
are confirmed; destination and actual spawn-route delivery remain gated.

| Criterion | Score | Evidence and limit |
|---|---:|---|
| E1 New concepts | 2 | Reuses CIP-0010 nodes/source refs/binding/capability; no new broker or generic secret transport |
| E2 Reuse | 2 | Uses D14 store policy, frozen login row and existing migration contract |
| E3 Secrets | 2 | Private file custody, generation-safe release, final-child injection, no plan/snapshot values; real child/reload qualification required |
| E6 Honest failure | 2 | Missing/unreadable/conflicting/expired/revoked and unsupported routes refuse without native fallback; local revoke does not recall delivered tokens |
| E7 Specifiability | 2 | L1–L8/ST-01–14 plus T3a public final-launch API, independent binding checks and secret-free lifecycle handle specify the cross-repository boundary; T0 still must publish exact carriers before enablement |
| E8 Operator effort | 1 | One deliberate enrollment removes repeated native login only after a qualified route exists; safe enrollment and migration remain explicit steps |

## Adversarial peer review

The [persisted review](../findings/astra-02-review-astra-03.md) records AR-1–4
and their verified resolution: narrow frozen-fixture Muse qualification versus
actual materialize integration; explicit hosted/dispatcher Codex owners;
one real-storage qualification leaf; and typed-login/env-shell refusal.
C0 owns full Codex carriers; L15-0 owns config/status and semantic cleanup.
All four requests are closed at leaf-design level, pending PLAN integration.
C7 spec activation and the Muse relay follow-on remain to inspect when
published. astra-03 independently confirmed the prepare installer trap and
the existing preserve-lock seam; astra-01 accepted their synthesis.

## Operator-only questions

No new decision is needed for D7/D8/D14, strict unknown handling or Claude
setup-token support. Diagnostic/carrier consistency is specification work,
not a reason to reopen those decisions. Runtime-B confirmation belongs to
its existing explicit owner gate. If real required qualification cannot run,
the release owner must preserve refusal or explicitly revise the release cut;
metadata/schema evidence cannot stand in for it.
