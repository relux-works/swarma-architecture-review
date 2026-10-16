# C0 — Publish complete Codex successor carriers and one settings authority

- Owner repository: **curator-spec**; launcher and receiver owners review their imported contracts.
- Normative clauses: profile-codex-settings §§1–7; CIP-0018 implementation leaf 1; environments §§1.3, 2, 6, 8.2, 10.2–10.3; D14.
- Attack surface: closed serialization and ownership of typed policy, not runtime credential custody.
- Size: 3. This replaces draft G0b; draft G0a is superseded by [L15-0](login-store-contract-publication.md). Do not create duplicate config/status tasks.

## Acceptance

1. Allocate complete manifest, lock, marker and fragment successors with exact discriminants, required members, whole-object schemas, canonical bytes and old/new compatibility vectors. A schema-module suffix is not a containing wire allocation. Existing closed envelopes remain unchanged.
2. Publish one coherent delivery rule. Recommended successor: `credential_store.selection` remains agreement metadata; `codex_settings` is the sole typed argv payload; legacy `config_overrides` is forbidden under that successor. This recommendation requires adoption before code relies on it. Published Muse v4 remains usable unchanged; never append a new member to v4.
3. Preserve the closed package vocabulary: only absent or `{}` is admitted. Record empty contributions/provenance and effective `{}` in the allocated lock/marker contracts. Machine selector/projection never becomes package provenance or lockable state.
4. Publish the compatibility/capability rules for every producer and consumer, including env/shell projection. Proposed successor rule: nonempty Codex settings requested through env/shell refuse with `codex_settings_unsupported` and no partial output; native/empty projections remain usable. A usable full-launch artifact cannot silently omit required typed settings. Direct structured login applies the common policy; shell evaluation is not an alternate settings transport. Muse's specified five-value projections retain their limited meaning.
5. Separate grammar publication from runtime enablement. Explicit Codex projection remains unavailable until qualified store behavior, strict consumers and covered route delivery pass the applicable gates. Snapshot descriptors stay in their separate closed namespace and never acquire credential policy.

## Paired contract tests

| Positive control | Forbidden outcome / intended refusal |
|---|---|
| Complete new envelopes validate; old envelopes retain their previous meaning | New fields under old tokens, duplicate/unknown members, missing required payload or invented revision refuse |
| Valid absent/empty contributions produce canonical empty settings identity | Nonempty package key, including a losing dependency or package-selected store, refuses before replacing installed state |
| One typed payload agrees with machine selection | Competing legacy payload, selection mismatch, dropped required transport or conflicting policy owners refuse |
| Native omits the override; qualified file/keyring uses its exact published transport | Env/shell output masquerading as a complete launch, unsupported consumer or implicit seed rewrite cannot satisfy delivery |

Plant a bounded invalid containing carrier and require the intended validator failure beside its valid control. Module-schema checks alone cannot authorize full-envelope emission or vendor execution.

## Dependencies and paths

Accepted CIP-0018 and D14. Coordinate L15-0's store/precedence reconciliation under one schema-allocation owner; serialize shared `protocol/environments.md`, schema/conformance indexes and release metadata. Own `protocol/profile-codex-settings.md`, complete successor schemas, canonical/compatibility vectors and their references. C1/C2/C3 and downstream typed consumers may develop against frozen published fixtures; activation remains a separate evidence join. C0 does not wait on snapshot, hosted or archive implementation and does not hold already specified Muse v4 behind future package vocabulary.
