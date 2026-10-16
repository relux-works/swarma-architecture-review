# C1 — Adopt closed Codex carriers and project only machine-owned storage

- **Owner repository:** curator.
- **Normative clauses:** profile-codex-settings §§1–7; CIP-0018 leaf 2;
  login-readiness §2; D14; environments §§1.3, 2, 6, 8.2, 10.2–10.3.
- **Attack surface:** package/machine ownership separation and launch identity.
- **Size:** M. No nonempty package key exists in this revision.

## Prerequisite, not an implementation choice

[C0](rc7-carrier-publication.md) must first allocate complete strict
manifest/lock/marker/fragment carriers, coordinated with L15-0 config/status
and cross-document reconciliation. The published v4 permits
`credential_store.config_overrides`; it does not permit top-level
`codex_settings`. Do not silently extend it or use projection schemas as full
validators. Recommended successor: selection remains agreement metadata,
`codex_settings` is the sole typed argv payload, and the legacy override
payload is disallowed under that successor. The spec owner must adopt this
exact reconciliation before code depends on it.

## Acceptance

Validate every context-package contribution, including losing dependencies
and overlays, before precedence. Only absence or `{}` is valid. Skill/MCP
packages cannot become another settings source. Preserve previous installed
lock/materialized state on invalid input. Successor locks record effective
`{}`, empty contributions and existing precedence; successor markers record
`{}` and bind the lock. Machine store values never enter package provenance,
locks or markers as package settings. Their effective launch value is bound
in the fragment/accepted plan identity and covered digest.

Project the common store-policy result to file/keyring typed launch values
only after eligibility and supported-runtime qualification. Native omits the
override. Unavailable required transport refuses before login or agent exec.
Use the same projection at login and launch; never rewrite native, seed or
snapshot `config.toml`. Changing policy cannot relabel a running session or
implicitly migrate credentials.

Proposed C0 renderer rule: requested env/shell output with nonempty Codex
settings refuses `codex_settings_unsupported` with no partial output, because
those formats cannot encode the required typed policy. Native/empty Codex
projections remain usable; Muse retains its expressly defined five-value
projection. `env login` consumes the typed result directly and never obtains
it by evaluating shell output. Publish this rule in C0 before implementation
rather than treating an environment-only result as a settings-bearing launch.

The future inheritance algorithm remains specified, but no synthetic
nonempty package vocabulary may be enabled merely to demonstrate ties. With
the current closed vocabulary, correct resolution yields `{}` everywhere.
Future-key winner/tie tests belong to the future reviewed extension.

## Mandatory paired tests

- Empty/absent declarations across root, requirement and overlay succeed;
  any nonempty declaration, including a lower-ranked package-selected store,
  unknown/dotted/quoted key, invalid UTF-8 or duplicate key refuses with
  `context_manifest_invalid`, preserving old state and producing no fragment.
- Valid successor carrier identities recompute; modified settings,
  contribution/member mismatch or hash/marker mismatch refuses. Old envelopes
  reject additions; no repair silently upgrades them.
- Native produces no override; admitted explicit file produces exactly file.
  Unknown native selector/read failure, incompatible shared native/effective
  storage, or isolated keyring refuses before link/login/launch. Pair with
  valid shared file and separately prepared isolated file.
- Changing the machine selector alters covered launch policy but cannot
  insert file/keyring into package lock/marker settings. Config bytes are
  unchanged after resolve, repair, skill sync and login preparation.
- Missing/unsupported payload refuses with the specified delivery diagnostic;
  qualified supported delivery succeeds. A consumer that rejects all rows
  cannot pass qualification.
- Explicit file plus requested env/shell refuses with no output under C0;
  native/empty projection succeeds. The adjacent typed JSON/login path applies
  the override; a login changed to shell-eval must fail the test.

## Dependencies, serialization and paths

Depends on published successor carriers and astra-02's store/migration policy.
Producer enablement additionally waits for C2/C3, hosted and relay support on
every advertised route, and no-model Codex backend qualification (§5).
Code can land dormant before the release gate; do not advertise support.

Paths: `internal/contextpkg/`, `internal/contextresolve/`,
`internal/contextlock/`, `internal/envmarker/`, `internal/envfragment/`,
`internal/envprofile/{managed,status,overlays}.go`, fixtures and docs. Serialize
shared identity edits with base-context/snapshot work; shared managed/status
edits with M1 and astra-02. Reuse existing strict parsing and hash machinery.
