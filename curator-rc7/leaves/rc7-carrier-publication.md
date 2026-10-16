# G0 — Publish the missing rc.7 carriers before enabling their producers

- Owner repository: `curator-spec` (launcher/receiver owners co-review only the carriers they consume).
- Author: astra-01. Status: proposed; split into independently reviewed G0a/G0b below.
- Normative clauses: `protocol/login-readiness.md` §§1, 2, 2.1, 7; `protocol/profile-codex-settings.md` §§1–3, 7; `protocol/environments.md` §10.2 v4; owner D14.
- Attack surface: versioned serialization, not runtime credential custody.
- Estimate: G0a 2 points, G0b 3 points. They are separate bounded leaves; no hosted or archive wire is bundled here.

## G0a — Containing login/config carriers

Publish the containing manager-config and status wire revisions, importing the already frozen credential-store subtree and standalone login-row schema. State old/new read and write behavior and the explicit configuration upgrade path. Retain every prior boundary and diagnostic. The selector is user-owned, not lockable, and cannot originate in packages, overlays or repositories.

Acceptance: exact complete schemas and carrier examples are published, with explicit version discriminants and compatibility table. Plain status and `--check` semantics are distinguished. Unsupported adapters and caller-session scope remain observable. Old envelope bytes remain unchanged.

Negative tests paired with positives: a valid new containing envelope accepts its frozen subtree/row; the same addition under each old closed envelope refuses. Unknown fields/versions, package-selected store and a system lock attempting to select a store refuse. Missing/unknown login never passes `--check`; current+present does. These are structural/contract tests, not qualification of metadata readers.

Dependencies: accepted CIP-0015 modules at spec `5509499`; no snapshot, hosted receiver or broker dependency. Paths: `protocol/login-readiness.md`, `protocol/environments.md` configuration/status references, new full carrier schemas and conformance cases, compatibility/release metadata. Serialize edits to shared protocol and schema inventories with G0b.

## G0b — One Codex settings delivery allocation

Resolve the existing v4 `credential_store.config_overrides` carrier versus CIP-0018's proposed successor `codex_settings` transport. Publish one coherent authoritative delivery rule and exact complete manifest/lock/marker/fragment successors where required. Do not independently widen v4, invent a v5 number, emit both as competing owners, or infer a carrier from a schema-module `v1` suffix. A deliberately retained agreement-only field must have equality rules and one application owner.

D14 is fixed: package `codex_settings` is absent or `{}`; no nonempty package key is admitted. The machinery records empty package selection/provenance and the machine store projection remains outside package locks and markers. Future vocabulary is not an rc.7 feature.

Acceptance: every enabled producer has a published full envelope, exact corresponding consumer validator and old/new compatibility vectors. Missing required transport and disagreement are refusals. The Muse v4 five-variable/root-context contract remains usable independently; this allocation does not hold it behind speculative package vocabulary.

Negative tests paired with positives: valid empty package settings and valid machine file projection pass; forbidden package store keys, invalid losing contributions, duplicate keys, invalid UTF-8 and all nonempty package settings fail without replacing lock/home. Typed Codex `file`/`keyring` passes only its declared carrier; duplicate or conflicting ownership, dropped required payload and old-token/new-field fail. Native selection emits no store override. Verify that no test gains success by inventing an allowed package key.

Dependencies: accepted CIP-0017/CIP-0018/D14; coordinate with agents-management's released v4 reader before enabling nonempty Codex emission. Paths: `protocol/profile-codex-settings.md`, `protocol/environments.md` §10.2, `schemas/profile-codex-settings-v1/`, newly allocated complete envelopes, conformance vectors and compatibility metadata. Snapshot descriptor remains its separate closed namespace; no credential policy is inserted there.

## Required review evidence

Each leaf publishes immutable before/after carrier references and a clause-to-vector map. A bounded known-invalid carrier must fail the intended validator, alongside the nearby positive control. Passing module-schema checks alone cannot authorize full-carrier emission or vendor execution. No runtime qualification is claimed by these specification leaves.
