# T0 — Publish the local setup-token source contract

- **Owner repository:** curator-spec; coordinate launcher SPEC as a separately reviewed companion change.
- **Normative clauses:** proposed [design §7 L1–L8](../designs/setup-token-local-source.md#7-proposed-normative-text); CIP-0010 C1–C4/C6 and narrow C7 amendment; retained CIP-0003 launch-selection/protected-read/migration gates; login-readiness §§1–4; environments §§7.4,10.2,10.3,12.1–12.2; Decision 0013 required extensions.
- **Attack surface:** interpreting source metadata as secret-delivery authority or silently widening old contracts.
- **Size:** M; publication only, no implementation or qualification claim.

## Acceptance

1. Adopt the same-UID/same-host Claude node slice explicitly without adopting broker authority. Keep per-home default and existing native login behavior; record C7's narrow sequencing carve-out.
2. Publish complete closed manager/source/marker and local binding shapes, the required-understanding node source carrier and exact typed refusals. Coordinate config/status with L15-0 and full fragment/marker successors with C0; v4 remains closed. Specify which CLI/final-execution route consumes the carrier. Do not claim that a standalone member schema freezes its enclosing transport.
3. Bind local executing UID/profile/harness/source reference+generation/channel/approved endpoint/executable digest/policy generation. Reference reuse, stale generations and missing binding have explicit refusal outcomes. No broker peer/generation fiction or local `lease_*` codes.
4. Define `login-row-v1` node/native/file/caller mapping without widening its enums; separate registration lifecycle and executor capability from candidate presence.
5. Freeze protected store/input bounds, atomic publication/revoke behavior and inspect → plan → apply preservation. Tokens and their digests never enter public metadata; snapshot descriptor/manifest/archive excludes source metadata as well.
6. Publish the proposed same-user headless chain `task-board spawn → approved curator-run local final-exec → Claude noninteractive process`, including its entry point and required plan carrier. It is independent of the full CIP-0016 primary hosted matrix. Direct-only and interactive hosted PTY have different qualification rows. `tb-sessiond` node lookup/restart remains refused: local-hosted-launches §§4/6 currently preserve the exact provider process and prohibit daemon lookup of fresh restart secrets. A later hosted token route needs an explicit amendment, never an internal injection callback or hidden wrapper.
7. Freeze the Curator-owned public in-process `pkg/localcredential` facade: metadata describe plus typed authorize-and-start at the final boundary, with a secret-free process handle result. It resolves protected authority itself and offers no token getter, environment-map return, CLI stdout/IPC or caller-asserted authorization. Curator's internal store implementation stays private; launcher pins/imports the public API. Preserve existing launch signal/terminal/cancellation semantics.

## Mandatory negatives and positive controls

- ST-01/06: package or lock authority, conflicting explicit isolation, node+file/keychain store and silent native migration refuse; user-owned linkless node control admits.
- ST-07/09/13: old carrier, unknown required member, arbitrary secret path, token literal/env-name fallback, source in snapshot, wrong UID or stale reference refuse; closed supported metadata-only carrier control validates.
- Conformance checker control: plant one forbidden secret-bearing field and one unknown required source branch in disposable fixtures; require the intended validation error, then the valid sibling passes.
- Each refusal maps to a specific command diagnostic; readiness reasons remain the existing closed row vocabulary. Semantic fixtures alone do not qualify vendor execution.

## Dependencies and paths

After the accepted rc.7 base; serialized with [L15-0](login-store-contract-publication.md) on config/status and [C0](rc7-carrier-publication.md) on full fragment/marker inventories, under one allocation owner. Before T1–T4 enablement (including T3a/T3b). New dedicated `protocol/local-setup-token-source.md`, schema/conformance family; shared `protocol/environments.md`, `protocol/login-readiness.md`, `cips/CIP-0010-credentials-setup-token-and-inherited-auth.md`, Decision 0013, schema index and coordinated successor schemas. Launcher SPEC carrier/entry-point companion lands before producer emission. This is not a prerequisite for unrelated existing v4 Muse delivery.
