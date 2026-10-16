# Curator rc.7 implementation plan

Owner: astra-01. Working draft, round 1, 2026-10-16. This is a delivery proposal, not evidence that the implementation or runtime qualification exists. Seat leaf files supply detailed acceptance contracts; this document owns ordering, shared paths and the release cut.

## 1. Fixed scope and evidence baseline

Implement the curator sides of accepted CIP-0014/15/17/18, supply the Curator prerequisites for CIP-0016, and design/adopt the same-user Claude setup-token slice without a broker. D1–D14 remain binding. Consumers apply Curator-owned facts; they never reconstruct home content or credential policy. A live session never uses a mutable managed home.

Read-only evidence pins observed for this review:

| Repository | Observed local commit | Evidence limit |
|---|---|---|
| curator-spec | `55094992185521dba470d80e1745d60af7bf496c` | Accepted normative wave; pending carrier/activation gates remain explicit |
| curator | `0d00a109ad1da77a5506747c89f24af9442eb341` | Current local code still emits v2/v3; `beginOperationValidated` recovers transactions |
| curator-agent-launcher | `9ad2f0160a1995af94b5069e4e85638140cb2712` | Local parser supports v1–v3; hosted activation is not proved |
| skill-agents-management | `a2a6e9f377f62a5872d99ecdfff0d1690e385f2a` | Stale local checkout; mission reports released v0.5.66 v4 support, not independently re-read here |
| skill-project-management | `ad68902f74ae55b1cd0445fef58390b42feea3dc` | Stale local board-cli module pin v0.5.41-0.maint.1; no pull allowed |
| swarma-credential-broker | `ec7fb3d0670449b074521d51f3e03b59f0142a69` | Read-only boundary evidence; no broker work belongs to the local token slice |

The provided login facts are versioned observations, not fresh qualification. No builds, model calls, credential reads or source-checkout writes are performed by this collective.

## 2. Immediate publication and integration gates

- **G0a/G0b:** [publish missing complete carriers](leaves/rc7-carrier-publication.md). Login/config containing revisions and the CIP-0018 carrier allocation are unresolved, despite frozen member schemas. Do not widen old envelopes or implement a second competing store transport.
- **Q-Muse:** exact Muse 1.4.8 build, P1–P4 on both forms, root present/absent, foreign rules/skills, link/regular snapshot and workspace residual. Environments §7.9 makes replay a release gate. Loader observations and model-visible behavior remain distinct; quota prevents unsupported model evidence before 2026-10-19.
- **Q-Codex:** profile-codex-settings §5 requires real scalar precedence and login/app-server/refresh behavior before nonempty producer enablement, with strict consumers. An accepted schema cannot satisfy this gate.
- **G-Snapshot:** runtime bootstrap, protected-input verification API/receipt and credential strategy must be specified before a hosted consumer depends on them. `--manifest-only` is not an attestation API. Runtime B still requires the confirmation stated in managed-home-snapshots §6.
- **G-Hosted:** local-hosted-launches §§1,8 requires joint successor plan/control/preparation/capability/config publication, Codex policy qualification and all three runtime rows. Do not treat proposed plan `2.0.0` or protocol 10 as allocated.
- **G-Token:** the local source needs adopted normative text and a protected final-executor lookup/injection contract. A design or metadata row alone cannot advertise spawned-agent authentication.

## 3. Bounded work packages to synthesize from seat leaves

Each numbered row is a separate review/change, not a multi-repository mega-PR. The implementation owner maps these to its existing board before coding. The individual leaf files will replace these provisional names as seats publish them.

| ID | Owner | Single surface and exact normative scope | Dependency | Release intent |
|---|---|---|---|---|
| G0a | curator-spec | Config/status complete carriers; login-readiness §§1,2,7 | Accepted modules | rc.7 prerequisite |
| G0b | curator-spec | Settings complete carriers and one delivery authority; profile-codex-settings §§1–3,7; environments §10.2 | D14, reader coordination | Before corresponding producer |
| F1 | curator | v4 value model/validation/renderers; environments §10.2 | Published v4 | Early curator lane |
| F2 | curator | Muse verified root fact and effective file admission; environments §§7.4,7.9,10.2 | F1, shared policy projection | rc.7; release after Q-Muse |
| Q1 | curator qualification owner | Exact Muse P1–P4 evidence; environments §7.9, CIP-0017 leaf 2 | Disposable probe prerequisites | Before consumer release |
| A1 | agents-management | Released v4 request/argv/sealer support; environments §10.2 | F1 fixtures, Q1 release gate | Verify supplied v0.5.66 evidence; do not reimplement blindly |
| L1 | curator-agent-launcher | v4 parsing, composition, plan binding; environments §10.2 | A1 | Unblock public v4 launches |
| P1 | project-management | Compatible module pin and real hosted/spawn v4 context path; CIP-0017 leaf 6 | Usable curator release + A1 + Q1 | First neighbour handoff |
| C1 | curator | Machine-only store selector and eligibility; login-readiness §2, profile-codex-settings §5 | G0a; single shared projection | rc.7 |
| C2 | curator | Empty settings contributions/lock/marker identity; profile-codex-settings §§1–2 | G0b | rc.7 machinery; no package keys |
| C3 | agents-management / launcher, separate PRs | Typed Codex argv and collision rejection; profile-codex-settings §§3–4 | G0b, C1, Q-Codex | Before explicit Codex activation |
| R1 | curator | Metadata-only presence readers; login-readiness §§1,1.1,5 | C1; source contract where applicable | rc.7; unqualified probes return unknown |
| R2 | curator | Status rows and strict aggregation; login-readiness §§1.2,6 | G0a, R1 | rc.7 |
| R3 | curator | Direct interactive login ceremony; login-readiness §3 | C1, R1; qualified vendor mapping | rc.7 |
| R4 | curator | Prepare orchestration/report-only behavior; login-readiness §4 | R2,R3 | rc.7 |
| S1 | curator | Snapshot closure/relocation/identity; snapshots §§3–4,6 | Current verified resolver, F1/F2 inputs | rc.7 |
| S2 | curator | Non-recovering consistent capture; snapshots §§1,5 | S1, read-only resolver interface | rc.7 |
| S3 | curator | Handle-safe destination/publication; snapshots §2 | S2 | rc.7 |
| S4 | curator | Public materialize and verifier boundary; snapshots §§1,4–6; hosted §3 | S1–S3, G-Snapshot for verifier extension | rc.7 prerequisites; no hosting claim |
| D4-N | curator-agent-launcher | Native interactive/exec snapshot composition; snapshots §§1,6; environments §10.5 | S4, published runtime/credential projection | Separate activation; no live-home fallback |
| D4-S | project-management | Per-run task-board spawn snapshot and restart identity; snapshots §§1,4,6; hosted §1 spawn separation | S4, qualified executor/runtime projection | Separate from primary hosted matrix |
| T1+ | curator-spec, curator, final executor | Local setup-token contract, custody, readiness and injection | G-Token; seat-05 design | Owner-requested capability; enable only complete path |
| H1+ | launcher, agents-management, project-management | Local hosted preparation/admission/runtime matrix | G-Hosted, S4, policy/source delivery | Follow-on activation; never partial Codex omission |
| X1+ | spec, dispatcher, launcher, curator | Canonical archive, transfer and cross-account exec | Snapshot producer; separate archive/binding publication | Follow-on, no local-success equivalence |
| R0 | curator | [Exact release evidence and capability claims](leaves/rc7-release-evidence.md) | Every advertised row | Signed rc.7 cut |

Mandatory negative cases and controls are specified in each detailed leaf. Every case must assert the intended refusal plus post-failure state; rejecting everything is not a pass. The table will be replaced with the seats' bounded leaf specifications before a final 2/2 traceability score is justified.

## 4. Ordering and path serialization

The high-priority chain is `F1 + C1 Muse projection -> F2`, with Q1 in parallel, then compatible v4 release/pin handoff. C2, readiness, snapshots and token design do not belong in Q1's path. Release feasibility and qualification must be exposed early rather than discovered after implementation.

| Shared files / package | Serialization rule | Safe parallel work |
|---|---|---|
| curator `internal/envfragment/envfragment.go`, `internal/envprofile/managed.go` | F1 then C1/F2 integration, then C2 projection, then snapshot resolver integration; one owner at a time | Pure new snapshot identity code, metadata readers and vendor qualification with no edits to these paths |
| curator `internal/config/{config,environments}.go`, `cmd/curator/envconfig.go` | G0a consumer/C1 before token source config; batch one schema transition | New read-only probe implementations and snapshot publication module |
| curator `internal/envprofile/lock.go`, managerlock/transaction seams | S2 capture lock work separately reviewed; no opportunistic mutation-recovery refactor | S1 deterministic closure/manifest helpers and S3 destination helpers against fixed interfaces |
| curator `cmd/curator/env.go`, `envstatus.go`, `profile.go` | R2, R3, R4 and S4 CLI wiring sequential; pure packages may precede wiring | Test fixtures, documentation drafts, isolated platform qualification |
| curator context package/lock/marker models | C2 after G0b; source migration hooks after C2 if same carrier | Snapshot destination safety and readiness collectors |
| launcher fragment/composition/hosted/main | L1 before settings delivery, then token injection integration, then hosted orchestration | Hosted receiver and Curator export work in other repositories |
| project-management sessionmanager Codex/Claude/Muse paths | Pin first; preparation/admission before runtime adapters; Codex lifecycle work serial with settings/resume identity | Snapshot/producer work elsewhere and separate runtime-specific test fixtures |
| shared spec protocol sections and conformance inventories | One landing owner per shared file; publish G0a/G0b before consumers; hosted/archive publication separate | Draft distinct schema families in separate files, then serialize inventory updates |

Dependencies are semantic and path-based. A separate worktree does not make concurrent changes to the same path safe. Rebase/review the actual integrated head and validate that head, rather than trusting a stale worktree's suite.

## 5. Proposed release cut

**Curator v0.15.0-rc.7:** usable v4 production/consumer agreement, D14 store policy, metadata readiness/status, `env login`, `profile prepare`, credential-free `env materialize`, exact verification boundary needed by its first consumer, and the bounded CIP-0018 machinery once full carriers are published. Require the corresponding qualification before advertising a nonempty Codex override. The same-user setup-token path is an explicit owner-requested workstream: normative adoption/custody alone is not support; it ships only with the qualified final-executor path.

**May follow the curator tag:** complete local hosted runtime activation; task-board replacement of the interim copy after materialize/verification and runtime projection qualification; cross-account archive/dispatcher execution; broker source adoption; token refresh qualification, unqualified platform backends, new Codex package-setting vocabulary and OpenCode snapshot support. Do not defer only Codex from the first hosted release, and do not defer credential safety to a later release.

**D4 coverage is route-specific:** additive materialize does not make native `curator-run`, headless exec, task-board spawn or primary hosted sessions snapshot-backed. D4-N and D4-S must remain separately tracked alongside H1+, with real launch/repair/resume evidence for each route. Until a route is migrated and qualified, the release cannot describe D4 as delivered there or use that route to claim the new lifetime guarantee. Its migration must never substitute a consumer-maintained copy list or live-home fallback.

There are two different gates: the curator capability tag and the multi-repository first hosted release. Publication of materialize can unblock hosted implementation without claiming that hosting works. Similarly, source metadata may report present without proving inference or refresh. If a mandatory rc.7 gate remains unmet, name the blocked capability and revise the cut explicitly with the convener; do not silently weaken the contract.

## 6. Adversarial questions for astra-04

1. What exact callable verifier/receipt lets admission and restart verify protected inputs without the host maintaining an inventory? Manifest-only and whole-home hashing are insufficient.
2. Where is the separate Curator runtime-bootstrap contract when snapshots exclude config seeds but hosted Codex demands a fully prepared initial home? No receiver-written config exception may appear implicitly.
3. Which runtime-B protection mechanism and owner confirmation support activation? Chmod in an agent-owned ancestry is not immutable protection.
4. Does a minimal rc.7 materialize leaf preserve read-only behavior in the presence of a pending journal, and avoid calling `beginOperationValidated` (which invokes recovery at current curator `internal/envprofile/lock.go`)?
5. Is the complete three-runtime hosted matrix after the curator tag, with preparer/admission/runtime/wire leaves explicit, rather than a single unreviewable hosted leaf?

## 7. Pending synthesis

Seat-owned detailed leaves and adversarial responses are pending. No final rubric score or owner decision is implied by this draft. Only genuine new operator choices belong in the final questions list; already-decided D1–D14 are not reopened.
