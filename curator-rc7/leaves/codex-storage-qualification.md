# C4 — Qualify Codex storage delivery without model calls

- **Owner repository:** curator (qualification matrix and enablement evidence).
- **Normative clauses:** profile-codex-settings §5 and §7; CIP-0018 Test plan
  `SettingsCredentialNativeMatrix`, `SettingsLaunchAllModes`,
  `SettingsSeedUntouched`; login-readiness §2; environments §7.4.
- **Attack surface:** unproven vendor backend behavior being advertised as
  an implemented machine selector.
- **Size:** M, bounded to exact supported release/platform/entrypoint tuples.

## Required matrix and evidence

Use disposable homes and dedicated test accounts, never active native login
state. Record binary version/build/digest, OS/session, native selector,
managed seed identity, isolation, effective selector, actual entrypoint,
exact sanitized command, exit and metadata observations. No credential values,
digests, account identity or vendor output transcript is retained.

The input pack's native storage facts do not qualify CLI precedence over a
conflicting seed, `codex login`, app-server or refresh. A fake executable
qualifies wiring only. Exercise the real supported binary without inference:

1. Establish effective configuration on interactive/exec preparation and
   app-server startup with a deliberately conflicting seed. Verify the typed
   CLI value wins using an available nonsecret effective-config observation
   or actual backend metadata effects. Parse acceptance alone is insufficient.
2. Perform dedicated no-inference login preparation and inspect destination
   metadata. Explicit isolated/file must create/use only its private file even
   with verified native keyring/auto. Native and shared-compatible rows retain
   their existing contract; never use a stale unrelated file as proof.
3. Observe legitimate refresh on the same backend through a supported
   authentication operation that does not request a model turn. If no such
   trigger/observation is available, record refresh unverified and retain the
   §5 producer-enable gate. Do not force expiry by editing a real credential.
   API-key storage cannot stand in for OAuth refresh evidence.
4. Cover app-server, direct login and each advertised launch mode, including
   their load/override order. Seed/native/snapshot config bytes remain intact.
   A mode that starts but has not exercised the selected storage is not a
   qualified success. Required host/resume policy enforcement is a separate
   consumer integration gate, not established by vendor storage probes.

Qualify file paths on every advertised platform and macOS with/without
credential-store access. Explicit keychain is enabled only for a qualified
macOS backend; isolated/keyring remains refused absent the independent scope
evidence required by the spec. Do not add Windows/Linux keychain capability
because its enum is schema-valid. Unknown matrix cells remain unsupported,
with exact limitations reported rather than replaced by mock evidence.

## Paired negatives and controls

| Forbidden result | Positive control |
|---|---|
| Explicit file ignored under conflicting native/seed keyring/auto | Same real binary and entrypoint with admitted file produces observed private-file backend |
| Shared keyring/auto plus explicit file resurrects old auth.json | Shared compatible file uses the expected verified link |
| Native read/parse failure becomes absent-key/file, or unknown enum is accepted | Successfully read config with absent key uses native file |
| Explicit isolated keyring succeeds or guessed per-home keyring scope is claimed | Qualified shared keyring row or separately prepared isolated file |
| Login passes but app-server/refresh silently use another store | Every required same-tuple entrypoint independently observes the selected store |
| Backend selector rewrites config or copies a native credential | Valid preparation preserves config/native bytes and uses vendor-owned writes only |
| Mock, quota error, skipped refresh or unrelated failure is labeled qualified | Completed actual observation with exact expected outcome and control |

Use a bounded control omitting only the override against the conflicting
fixture: the detector must observe the wrong backend/effective setting, not
merely fail authentication. This proves the observation distinguishes the
property being qualified. Preserve real product negative tests separately.

## Dependencies and paths

Begin fixture/probe design alongside L15-1 and C2. Final Curator/launcher
production-entry runs require their landed implementations; vendor-only
evidence can precede them. This breaks no dependency cycle: code may land
dormant, while activation requires the completed matrix and strict consumers.

Store sanitized results in curator's native task evidence/docs and reference
the exact supported tuples from registry/capability/status owners. Coordinate
those shared code edits through L15-1/C1; this evidence leaf does not create
another store resolver. Release gate for every advertised explicit Codex
store path; it does not block the independent Muse v4 path.
