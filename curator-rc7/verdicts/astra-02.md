# astra-02 — login/readiness/store/preparation verdict

Status: **review complete, round 5; awaiting PARK**. Reviewed PLAN `32cf0f2`, launch refinements
through `75dc718`, all hosted/archive leaves, the token design through ST-15
and T0 ordering at `323a284`. L15-5/6a/6b are published at signed `82b669b`,
accepted by all four peer seats and now mapped in the cut, canonical table,
path serialization and exact CIP-0015 coverage. The core L15 leaves originated at
`b4d55ab`, with installer/preserve-lock refinements at `c1cab0f` and shared
pure verification at `288eccc`. No implementation or runtime qualification
was performed. Every mandatory product test is future implementation work.

## Plan rubric

| Criterion | Score | Evidence and remaining bound |
|---|---:|---|
| P1 Traceability | 2 | Exact CIP coverage maps core L15, consumers, qualification, H/X5/C7/M6 and the separately bounded L15-5/6a/6b follow-ons; no identified curator clause or integration owner remains orphaned |
| P2 Bounded leaves | 2 | Store policy, metadata, login, prepare and consumer/broker follow-ons have separate surfaces; hosted reservation/admission/runtime and archive intake/protection are split |
| P3 Negative evidence | 2 | Each leaf pairs specific refusals/invariants with nearby valid controls; full CLI, real route, concurrency and detector controls are named with qualification limits |
| P4 Ordering | 2 | Fixed-interface snapshot work runs in parallel; L15-2/SNAP share the pure verifier; C0/L15/T0 and all overlapping integration paths serialize; token public API avoids a dependency cycle |
| P5 Unblocking | 2 | Muse v4 work precedes unrelated prepare/snapshot/token work; Codex successor allocation is kept separate |
| P6 Release honesty | 2 | Base tag is separate from explicit Codex, D4 routes, token-spawn, all-runtime hosted and remote activation; real loader/backend evidence, full C7 consumer gate and honest unknown rows remain required |

This is a review of a proposed plan. A plan score does not mean code is ready
or a supported launch capability can be enabled. Total: **12/12**.

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
7. **External guidance is not broker authority.** L15-5 consumes only safe
   caller-scoped metadata. L15-6a/6b retain broker operator/observer publication
   and adoption gates, zero status leases, and no agent-to-operator escalation.
   They are follow-ons, not implied support from local L15 or T0–T4.

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
| E7 Specifiability | 2 | L1–L8/ST-01–15 plus T3a public final-launch API, independent binding/startup-input checks and secret-free lifecycle handle specify the boundary; T0 still must publish exact carriers before enablement |
| E8 Operator effort | 1 | One deliberate enrollment removes repeated native login only after a qualified route exists; safe enrollment and migration remain explicit steps |

Design total: **11/12**. The remaining operator-effort cost is explicit, not
a security exception or an objection to adopting the proposed design.

## Adversarial peer review

The [persisted review](../findings/astra-02-review-astra-03.md) records AR-1–4
and their verified resolution: narrow frozen-fixture Muse qualification versus
actual materialize integration; explicit hosted/dispatcher Codex owners;
one real-storage qualification leaf; and typed-login/env-shell refusal.
C0 owns full Codex carriers; L15-0 owns config/status and semantic cleanup.
All four requests are closed in the integrated plan. C7 spec activation,
M6's separate broker-key backend seam and C5's Curator-owned initial base
were inspected and accepted at `75dc718`. astra-03 independently confirmed
the prepare installer/preserve-lock trap and identified the omitted CIP-0015
consumer/broker ownership. L15-5/6a/6b now provide those bounded follow-ons;
their final mapping is verified at `32cf0f2`. astra-04's materialize probe finding
is independently confirmed and shares L15-2's pure verification seam.

Documentation checks: 74 Markdown files have valid local file targets at
`82b669b`, with a known-missing-target control detected; anchor validation was
not performed. Log: seat `.temp/doc-check-02.log`. This is no evidence about
product behavior, vendor loaders, credentials, broker admission or inference.

## Operator-only questions

No new decision is needed for D7/D8/D14, strict unknown handling or Claude
setup-token support. Diagnostic/carrier consistency is specification work,
not a reason to reopen those decisions. Runtime-B confirmation belongs to
its existing explicit owner gate. If real required qualification cannot run,
the release owner must preserve refusal or explicitly revise the release cut;
metadata/schema evidence cannot stand in for it.
