# Curator rc.7 implementation plan

Owner: astra-01. Round 2 synthesis, 2026-10-16. This is an implementation and delivery plan, not shipped-code or runtime-qualification evidence. The linked leaves define clauses, acceptance, negative tests with positive controls, dependencies, paths and estimates. Each repository maps its own leaves into its existing board before implementation; a coordinated handoff is never a multi-repository mega-PR.

## 1. Fixed scope and inspected baseline

Implement the curator sides of accepted CIP-0014/15/17/18, identify the Curator prerequisites and bounded follow-ons for CIP-0016, and deliver the design/normative proposal for the same-user Claude setup-token slice without a broker. D1–D14 are binding. Curator owns homes and their verification; consumers apply its facts and separately admitted policy. A live session needs its own snapshot. Export availability alone does not migrate any launch route.

| Repository | Inspected commit | Bound on the evidence |
|---|---|---|
| curator-spec | `55094992185521dba470d80e1745d60af7bf496c` | Accepted normative modules; containing-carrier and activation questions remain open |
| curator | `0d00a109ad1da77a5506747c89f24af9442eb341` | v2/v3 producer; mutation-oriented transaction entry recovers; install can activate even with `Use=false` |
| curator-agent-launcher | `9ad2f0160a1995af94b5069e4e85638140cb2712` | v1–v3 parser; internal plan context omits Muse; tracked execution serializes env literals before starting ax |
| skill-agents-management | `acae871c0d53cd580cfef1863a75c58e59b59690`, v0.5.66 | Strict v4 exists; explicit Codex stores remain unsupported; Muse qualification map names only 1.4.7-R6101.1 |
| skill-project-management | `ab63db82365cdf9229ad60f72cc82997cbbe5043` | board-cli pins v0.5.65; real headless spawn executes plan binary/argv/env; no snapshot capability is implied |
| swarma-credential-broker | `ec7fb3d0670449b074521d51f3e03b59f0142a69` | Boundary evidence only; no broker implementation belongs to this local slice |

Updated neighbour clones were supplied under `curator-rc7-collective/sources/`; original stale checkouts were not pulled. Landing notices are not substituted for inspection. The input login pack is versioned measured evidence, not qualification of later binaries or different routes. This collective did not build, execute providers, read credentials, or modify source repositories.

## 2. Release cut and explicit gates

| Cut | Required work | What the cut may claim |
|---|---|---|
| **Curator v0.15.0-rc.7 base** | L15-0..4; M1 with M2 evidence and compatible M3/M4 handoff; SNAP-ID/LOCK/CLOSURE/PUBLISH/CLI; C0/C1 empty-vocabulary machinery; R0 | Qualified Muse v4 emission, machine store policy with honest unsupported rows, metadata-only readiness, interactive login, preparation, pure materialize and its actual-tree verifier |
| **Explicit Codex override activation** | C0..4, each advertised route's C5/C6 evidence, and the spec-owned activation record | Only exact qualified release/platform/mode tuples. Dormant code or valid enums are not backend support. Package vocabulary stays absent or `{}` |
| **Native and headless snapshot uptake** | HOST-HOME-SPEC/CODE plus D4-N/D4-S and each destination authentication/runtime row | D4 only on the named migrated route. No mutable live-home fallback or current-profile recapture on resume |
| **Owner-requested Claude node-source outcome** | T0..T4, including both T3a/T3b, plus private-home and real headless-spawn qualification | Same-user `task-board spawn -> curator-run final-exec -> Claude` only. Direct-only injection does not close spawned-agent support |
| **First public local hosted activation** | All hosted leaves, common runtime contract/code, three-runtime operation matrix and applicable C5 | Claude, Codex and Muse together. No partial two-runtime launch flag; materialize or a registered factory is insufficient |
| **Cross-account archive activation** | X0..X4, separately admitted credential channel and destination runtime qualification | Only measured archive/relay/executor/platform tuples; local success does not prove D6 |

The rc.7 tag must not wait for full hosted or archive implementation. Conversely, it must not be described as completing D4 on existing consumers, the owner-requested token-spawn outcome, or all five CIPs. HOST-HOME is the remaining Curator prerequisite for those route activations, not part of pure materialize. If a mandatory rc.7 row remains unqualified, R0 records the exact blocker; it cannot quietly drop that row or label refusal-only code as supported.

Publication gates are concrete work: L15-0 allocates complete config/status carriers and resolves Muse/status seams; C0 allocates complete Codex carriers without widening v4; HOST-HOME-SPEC freezes runtime initialization and protected-input verification; T0 freezes the local source and executor API; hosted publication freezes its joint wire; X0 freezes archive bytes/caps. Runtime B still needs the operator confirmation expressly retained in snapshots §6. A reviewable mechanism and its protection evidence must precede that decision; chmod in an agent-owned tree is insufficient.

## 3. Canonical bounded leaves

### 3.1 Login, store and early Muse unblock

| ID / detailed contract | Owner | Scope and predecessor |
|---|---|---|
| [L15-0](leaves/login-store-contract-publication.md) | curator-spec | Complete config/status contracts; Muse native/file, ambient and diagnostic reconciliation; status executes no vendor binary. No runtime predecessor |
| [L15-1](leaves/credential-store-policy.md) | curator | One machine-owned source/store/isolation projection and explicit migration boundary; after L15-0 |
| [M1](leaves/muse-v4-producer.md) | curator | Verified root fact, v4 structured/plain renderers, four XDG roots plus mandatory file backend; share L15-1 policy, no new Muse marker member |
| [M2](leaves/muse-148-exclusion-replay.md) | curator qualification owner | Exact 1.4.8 P1–P4 real-loader replay; starts alongside M1, using frozen conforming regular-file fixture and real Curator link |
| [M3](leaves/muse-v4-plugin.md) | agents-management | Qualify/map the exact new build after M2; reuse shipped v0.5.66 reader rather than reimplement it |
| [M4](leaves/muse-v4-launcher.md) | curator-agent-launcher | Full strict v4 parsing and internal request/composition path; fixtures parallel to M1/M2, release after qualified M3 |
| [M5](leaves/muse-v4-consumer-pin.md) | project-management | Actual module/pin/vendor uptake after usable Curator release and M3; pin is not D4 migration |
| [L15-2](leaves/login-readiness.md) | curator | Caller-session metadata probes and full status/strict aggregate; after common policy, never `--version` or auth-status execution |
| [L15-3](leaves/env-login.md) | curator | Trusted direct vendor login, both TTYs, admitted isolated home, exact failure/cancellation semantics; after policy/readiness and qualified delivery |
| [L15-4](leaves/profile-prepare.md) | curator | Every participant, explicit install/resolve/login orchestration, headless report-only, no activation and no implicit lock migration; after L15-2/3 |

L15-4 must not reuse ordinary installation with only `Use=false`: current `envprofile.go:911–919` still activates the first profile. Add an explicit no-activation seam; pointer restoration after native writes is too late. Preserve ordinary first-install activation as the positive control. Use the existing selected-lock preservation contract rather than unconstrained repair.

M2 qualifies the real loader on both representations; it does **not** prove materialize capture, publication or provenance. SNAP-CLI separately runs actual `env materialize -> Muse loader` with the frozen expected bytes. This removes a false early-release dependency without deleting the product integration gate. Offline echo is only a candidate observation lane until exact-loader equivalence is proved. Quota/auth failure, argv-only success and a fake binary cannot pass P1–P4. Model-visible residuals and refresh remain separate measured or unknown rows.

### 3.2 Codex typed policy

| ID / detailed contract | Owner | Scope and predecessor |
|---|---|---|
| [C0](leaves/rc7-carrier-publication.md) | curator-spec | Full manifest/lock/marker/fragment successors, one typed authority and compatibility vectors; coordinate L15-0 under one schema owner |
| [C1](leaves/codex-settings-producer.md) | curator | Validate every empty contribution, canonical lock/marker identity, machine-only projection; after C0/L15-1; code may land dormant |
| [C2](leaves/codex-typed-plugin.md) | agents-management | Canonical typed scalar argv, all raw/profile collision refusals and sealed identity; after C0 fixtures, serialized with M3 |
| [C3](leaves/codex-typed-launcher.md) | curator-agent-launcher | Structured direct/tracked delivery and digest coverage; after C2/C0, serialized after M4 |
| [C4](leaves/codex-storage-qualification.md) | curator qualification owner | Real no-model precedence/login/app-server/legitimate refresh matrix; probes parallel, production-entry completion joins C1–3 |
| [C5](leaves/codex-hosted-settings.md) | project-management | App-server/client/reuse/cold-resume typed payload and private MCP/policy ownership; after applicable host contracts and C2–4 |
| [C6](leaves/codex-dispatch-settings.md) | swarma-dispatcher | Covered payload survives relay and destination admission; after published dispatch route, unavailable until independently qualified |

CIP-0018 implementation leaf 7 remains spec-owned: record jointly passing evidence and explicitly authorize producer revision activation. R0 consumes that record; Curator cannot self-allocate or self-enable the spec revision. Nonempty env/shell Codex projection must refuse with no partial launch output under the proposed C0 rule; typed login consumes structured policy directly. Snapshot identity neither transports nor authorizes settings. C5/C6 are their own owners, never work hidden in HOST-HOME bootstrap.

### 3.3 Snapshot producer and common runtime seam

| ID / detailed contract | Owner | Scope and predecessor |
|---|---|---|
| [SNAP-ID](leaves/snapshot-identity-verifier.md) | curator | Closed manifest/descriptor identity and complete actual-tree verification; frozen normative vectors |
| [SNAP-LOCK](leaves/snapshot-nonrecovering-capture.md) | curator | Non-recovering, non-provisioning consistent capture and ABA defenses; interface agreed with ID/CLOSURE |
| [SNAP-CLOSURE](leaves/snapshot-content-relocation.md) | curator | Verified allowlisted content and relocation, including supports/skills; root fact from M1; no credentials, seeds or source metadata |
| [SNAP-PUBLISH](leaves/snapshot-destination-publication.md) | curator | Retained-handle all-ancestor destination admission, no-replace publication and verified idempotence; independent of capture implementation |
| [SNAP-CLI](leaves/snapshot-cli-integration.md) | curator | Public materialize, manifest-only parity, no hidden effects and real producer-to-loader row; joins the four mechanisms |
| [HOST-HOME-SPEC](leaves/hosted-home-contract.md) | curator-spec | Runtime initialization, separate credential strategy, protected-input receipt and fresh/resume API; common native/spawn/hosted contract |
| [HOST-HOME-CODE](leaves/hosted-home-runtime.md) | curator | Common implementation of that published bootstrap/verifier only; after SNAP-CLI and SPEC; provider lifecycle proof belongs to each route |
| [D4-N](leaves/native-snapshot-consumer.md) | curator-agent-launcher | Native interactive/exec private snapshot composition and original resume baseline; after M4 and common runtime seam |
| [D4-S](leaves/spawn-snapshot-consumer.md) | project-management | Per-run headless snapshot/provenance, cancellation/retry identity and no duplicate start; after published executor/runtime seam |

SNAP-ID, SNAP-LOCK and SNAP-PUBLISH develop in parallel in disjoint files against fixed interfaces. CLOSURE joins verified resolver inputs; CLI integration follows all four. Do not serialize publication helpers behind completed capture. `beginOperationValidated`, provisioning manager locks and current partial no-follow helpers are not reused as evidence for stronger snapshot guarantees. `--manifest-only` is not actual-tree attestation.

### 3.4 Local Claude setup-token source

The [design](designs/setup-token-local-source.md) supplies the normative proposal and ST conformance pairs. These are conditional implementation leaves after adoption, not claims that the current binaries support the source.

| ID / detailed contract | Owner | Scope and predecessor |
|---|---|---|
| [T0](leaves/setup-token-contract.md) | curator-spec; launcher companion | Same-user closed source/binding/carrier and final-entry/public API contract; coordinate C0/L15-0, no broker |
| [T1](leaves/setup-token-custody.md) | curator | Protected bounded stdin enrollment, atomic custody/generation/revoke and metadata facade; after T0 |
| [T2](leaves/setup-token-policy-readiness.md) | curator | Source-first policy, explicit migration and existing readiness mapping; after T1/common L15 policy |
| [T3a](leaves/setup-token-executor-api.md) | curator | Public in-process protected authorize-and-start API with secret-free lifecycle handle; after T2 |
| [T3b](leaves/setup-token-final-executor.md) | curator-agent-launcher | Actual final-hop API integration and real Claude child/source/reload qualification; after T3a and the private runtime seam |
| [T4](leaves/setup-token-spawn-consumer.md) | project-management | Actual headless task-board -> curator-run -> Claude uptake and qualification; joins T3b with D4-S |

This order avoids the custody/source-policy cycle and cross-module `internal` imports. The public facade is not a token getter, environment-map result or secret IPC. Snapshot composition and source-independent executor intake can develop before vendor authentication qualification; their final evidence joins at T3b/T4. Token bytes enter only the actual admitted Claude child. Injection before tracked ax serialization is forbidden. Current `tb-sessiond` restart lookup and hidden provider wrappers remain refused by local-hosted-launches §§4/6; the first node route is independent headless spawn, not full hosted activation.

## 4. Delivery lanes and serialization

1. **Start the scarce qualification work immediately:** M2's exact loader observation and C4's real backend observation design. In parallel, publish L15-0/C0; prepare HOST-HOME-SPEC/T0 on independent text, merging shared carrier edits sequentially. A missing vendor observation is exposed early, not after every implementation finishes.
2. **First implementation lane:** L15-1 common projection, then M1; M4 develops against published v4 fixtures. M2 -> qualified M3 -> integrated M4 and the usable Curator release -> M5 is the neighbour unblock chain. Do not put Codex future vocabulary, tokens, hosted or archive work before it.
3. **Independent Curator lanes:** snapshot identity/capture/publication mechanisms in disjoint files; readiness reader helpers and vendor evidence; empty Codex parsing/identity after C0. Shared integration paths still serialize. SNAP-CLI, L15-4 and C1 each get a focused integration review, not one aggregate PR.
4. **After the base cut:** common runtime preparation plus native/headless migration and T0..T4 are the priority route to the owner's spawned-Claude outcome. Hosted and archive contracts/fixtures progress independently; their public activation waits for their complete matrices.

| Shared path or state | Required serialization | Work that can proceed independently |
|---|---|---|
| spec `protocol/environments.md`, config/fragment/marker schemas and indexes | L15-0 + C0 allocation owner, then T0/hosted/transport companion amendments; no parallel numbering | Dedicated evidence, conformance drafts and independent protocol text |
| curator `internal/config/{config,environments}.go`, `cmd/curator/envconfig.go` | L15-1 before T2 source config; one containing-carrier transition | Pure metadata readers, custody file code, snapshot publication |
| curator `internal/envfragment`, `envprofile/managed.go`, registry/status integration | L15-1/M1 first; C1 settings and SNAP-CLOSURE integration next; source hooks thereafter | M2/C4 vendor evidence, immutable fixture readers, new modules |
| curator context manifest/resolve/lock/marker identity | C1 full-carrier work before consuming snapshot resolver integration; do not rewrite frozen old identities | Pure snapshot hashing/destination code; empty-vocabulary fixture design |
| curator managerlock/transaction/capture | SNAP-LOCK owns the new non-recovering seam; no opportunistic mutation-recovery rewrite | SNAP-ID and SNAP-PUBLISH through fixed interfaces |
| curator `envprofile.go`, CLI env/status/profile entry files | L15-2, L15-3, L15-4, SNAP-CLI wire-up sequential as paths overlap; preserve ordinary install and selected lock | Independent package implementations and qualification records |
| curator runtime/bootstrap, source admission, `pkg/localcredential` | SNAP-CLI -> HOST-HOME-CODE; T1 -> T2 -> T3a on their shared API; join only published seams | Source-independent D4 consumer fixtures and separate schema publication |
| agents-management shared Curator context/seal and module release | M3 first, then C2 and hosted process-form integration; one module tag/pin state at a time | Provider-specific fixture work with no shared file edits |
| launcher fragment/plan/context/composition/execution and SPEC | M4 first, C3 then D4-N/T3b as overlapping entrypoints require; archive intake after its contract | New parser/control fixtures and contract reviews outside shared files |
| project-management module/vendor, spawn, hosted identity/client/runtime | M5 first; D4-S before T4 integration; C5 serialized with Codex host work; reservation/admission own shared receiver state | Disjoint Claude/Muse runtime tests and non-mutating qualification |
| dispatcher covered plan/resource contract and relay journal | C6 settings and X0/X2 archive owners coordinate the same schema/relay boundary | Frozen canonical resource vectors; no invented implementation paths |

Freeze small interfaces before parallel work; a task claims an exact path set before edits. A leaf exceeding its single attack surface splits before coding. Size estimates are relative, not delivery dates. Existing scoped tests may be reused only at the reviewed commit and with their demonstrated limits.

## 5. Bounded follow-on hosted and archive ownership

The hosted owner is publishing detailed leaves for the remaining CIP-0016 implementation rows: joint carrier/capability/config publication; agents-management process forms; project-management reservation and admission; distinct Claude/Muse runtime operations; Codex app-server/policy/resume; launcher selection/preparation/handoff; and all-runtime activation/migration. These are post-base route work, not a hidden rc.7 mega-leaf. Their canonical links replace this coordination paragraph before the plan is final.

| Archive leaf | Owner | Dependency and activation boundary |
|---|---|---|
| [X0](leaves/snapshot-archive-contract.md) | curator-spec + matching launcher/dispatcher publications | Exact bytes/caps and protected plan/resource contract; no code chooses the pending wire |
| [X1](leaves/snapshot-archive-caller.md) | curator | SNAP-CLI + X0; actual-tree verified canonical resource |
| [X2](leaves/snapshot-archive-relay.md) | dispatcher | X0; opaque verified relay/journal/retry; X1 integration and C6 settings join |
| [X3](leaves/snapshot-archive-executor.md) | launcher | X0 + qualified runtime seam; whole-manifest install and protected expected admission; X1/X2 integration joins |
| [X4](leaves/snapshot-consumer-migration.md) | project-management / agents-management, separate releases | Retire fallback per qualified route; local migration need not await remote implementation |

X1/X2/X3 can implement against shared immutable vectors in parallel after X0. Actual end-to-end activation is a join. Runtime projection protection, credentials and cross-account authority remain independent gates; a valid archive hash is never admission. Dispatcher source was not supplied: its owner must pin actual code paths before implementation, rather than treating contract references as code evidence.

## 6. Normative coverage and release evidence

| Accepted work | Accountable leaves |
|---|---|
| CIP-0014 leaf 2 / snapshots §§1–5 | SNAP-ID/LOCK/CLOSURE/PUBLISH/CLI; separate schema identity and real filesystem controls |
| CIP-0014 leaves 3–4 / snapshots §6 | HOST-HOME-SPEC/CODE, D4-N/D4-S and hosted route leaves; all adapter/runtime policy and credential boundaries retained |
| CIP-0014 leaves 5–7 / snapshots §7 | X0..X4 and C6 where settings cross dispatch |
| CIP-0015 / login-readiness §§1–7 | L15-0..4, C4 for Codex qualification; T2 only after its source extension is adopted |
| CIP-0016 curator leaf 2 | Snapshot producer plus explicit common runtime initialization/verifier seam; receipt is not authentication or provider qualification |
| CIP-0016 remaining leaves | Hosted follow-on owners above; C5 owns typed Codex policy, X0..X3 the later transport boundary |
| CIP-0017 leaves 2–6 / environments §§7.9,10.2 | M1..M5, with SNAP-CLI's independent real producer/loader row |
| CIP-0018 leaves 1–7 | C0..C6 plus spec activation record; R0 records the corresponding released pair |

[R0](leaves/rc7-release-evidence.md) owns the Curator release evidence and capability claims. For each advertised row retain exact spec/producer/consumer/provider/OS/session pins, commands, exit codes, fixture/control identity and normal task evidence links. Require intended negative outcomes and unchanged forbidden state, beside valid controls; unrelated failure and universal rejection are not passes. Metadata/schema controls do not qualify syscalls, vendor loaders, child-secret containment or authentication. Retain skipped/unknown rows explicitly.

Full status must execute zero vendor binaries, not merely avoid auth-status. OpenCode's unknown login row remains visible in strict all-participant checks, and materialize refuses its unqualified skills target. Muse D10 file admission is not held for refresh; refresh limits remain reported. Claude node source is inference-only and never claims Remote Control. No release removes these bounds to make a matrix green.

Final review must close the hosted-link integration and spec activation ownership above, validate all relative links/IDs, and obtain peer confirmation of the dependency/release cut. This plan remains a working synthesis until those review actions finish; runtime gates are intentionally future work, not collective validation results.
