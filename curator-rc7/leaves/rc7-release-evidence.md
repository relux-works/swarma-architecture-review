# R0 — Cut rc.7 from exact producer/consumer and refusal evidence

- Owner repository: `curator`; each neighbour retains its own release ownership.
- Author: astra-01. Status: proposed.
- Normative clauses: environments §§7.9, 10.2, 10.5, 13; login-readiness §§1.2, 5–7; profile-codex-settings §§3, 5, 7; managed-home-snapshots §§6–7; local-hosted-launches §§1, 7–8; D1–D14.
- Attack surface: capability activation and release claims.
- Estimate: 2 points; no implementation is folded into the release leaf.
- Paths: curator release/version metadata, `README.md`, `docs/environment-config.md`, `docs/agent-logins.md`, pinned conformance provenance and task evidence. Consumer pin/lock/vendor changes remain separate neighbour leaves.

## Acceptance

1. Record exact spec commit, producer commit/release, consumer commits/tags, supported provider builds, platform/session scope, commands, exit codes and artifact references for each advertised capability. A green helper or schema suite is not production-entry qualification.
2. Publish separate capability rows for Muse v4 emission, login metadata, interactive login, preparation, materialize, verification, local token injection, local hosted runtime operations, and cross-account transport. No umbrella claim of all five CIPs being implemented.
3. Muse's required M2 P1–P4 replay precedes the coordinated producer/consumer release. Its frozen conforming regular-file fixture qualifies the actual loader representation only; SNAP-CLI independently requires real `env materialize -> Muse loader` integration. Preserve both evidence rows. Loader evidence and model-visible evidence have separate statuses. Subscription exhaustion is a blocked observation, not a pass; D10 file admission does not await refresh qualification.
4. A nonempty Codex override remains disabled/refused until C0 complete carrier publication, machine eligibility, strict consumers and C4 login/app-server/refresh qualification are all evidenced, with the spec-owned C7 activation record. C5/C6 have their own route evidence; a missing required route is not a scoped-rollout waiver without prior spec adoption. The empty package vocabulary is explicit; no env/shell output can silently omit required typed policy.
5. A first public local hosted capability requires every Claude/Codex/Muse operation row. Curator materialize availability alone never advertises hosting or D4 on native/spawn consumers. HOST-HOME-SPEC/CODE, D4-N and D4-S retain distinct evidence. Token support needs T3a/T3b and the actual T4 spawned path; direct-only injection is insufficient. Archive format, cross-account execution, runtime protection and broker remain separately gated.
6. Describe strict `--check` migration, caller-only presence semantics, unsupported platform rows, OpenCode aggregate limitation, Muse refresh residual and Claude Remote Control limitation. Preserve old readers' rejection and publish minimum usable consumer versions.

## Negative evidence and positive controls

- A compatible exact producer/consumer pair succeeds through the real public entrypoint; old consumer or missing required policy refuses without downgrade/fallback.
- An unqualified provider/build row remains unavailable while a qualified row is advertised. A known-missing receipt or capability is planted in an isolated fixture and must block release/admission for the intended reason.
- Snapshot bytes survive profile repair; a drifted snapshot refuses verification/attach instead of rebasing its baseline. No credential enters snapshot/plan/log fixtures; use synthetic canaries only.
- A partial hosted matrix does not advertise `--hosted`; all required cells with production evidence do. Native selection still performs zero receiver contact.
- Audit every mandatory leaf against its actual landed reviewed head; pending code, review, CI or publication is not completion.

## Dependencies and release ordering

All advertised rc.7 leaves and their specific gates, not every future neighbour feature. Prioritize v4 producer/consumer interoperability and publish its evidence to unblock the project-management pin. Run snapshot and login implementation lanes concurrently where paths are disjoint. Do not make the curator tag depend on full CIP-0016 or dispatcher activation. If a required rc.7 capability cannot be qualified, report the exact missing gate; do not relabel a refusal-only implementation as working support.
