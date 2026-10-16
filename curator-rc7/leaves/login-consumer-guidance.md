# L15-5 — Consume sanitized readiness and preparation guidance

- Owner repository: **skill-project-management**.
- Normative clauses: CIP-0015 implementation leaf 7; login-readiness §§1–1.2,
  3–4, 6–7; D1/D7/D8.
- Attack surface: consumer diagnostics becoming a second readiness reader or
  an implicit login/repair authority.
- Size: 2. Neighbour follow-on after the released Curator status/prepare
  contracts; separate from M5's Muse module pin and from broker adoption.

## Acceptance

Use the published complete Curator status carrier to display current and
present/absent/unknown separately, preserving source, store/backend, reason
and caller-session scope. Strictly decode the supported revision; an old,
missing, malformed or unreadable response is unavailable, never an empty
successful readiness table. Do not inspect home paths, credential files,
Keychain, vendor auth-status or source nodes to fill a missing row.

Offer the existing explicit `curator profile prepare <installed-name>` or
source-specific guidance. Only supported isolated home-owned absence suggests
`curator env login <env-id> --profile <name>`; unknown requests resolution of
its stated uncertainty, shared mode points to native login, and external
sources point to their admitted enrollment path. Preserve Claude same-session
guidance and OpenCode's strict-aggregate limitation. Guidance is not authority
to run a command. Background/headless display starts no install, repair,
login, browser, enrollment or profile activation, and captures no vendor I/O.

Presence remains metadata, not a new launch authorization gate or a promise
about destination authentication, refresh or inference. Do not persist a
readiness row in a plan as authority, or reuse a caller observation as daemon
or remote readiness. Existing launch admission and doctor compatibility
verdicts retain their own meanings. Render only admitted sanitized fields,
not raw child stderr, account identities, source references or token values.

## Paired tests and controls

- Complete current/present fixture displays its caller-scoped result;
  current/unknown, absent and non-current/present remain distinct. A missing
  participant or unsupported carrier cannot turn into green readiness.
- Valid isolated absence gives exact login guidance; node/broker/shared or
  unknown rows never suggest home login. Valid preparation guidance preserves
  the installed selection without inventing flags or a source URL.
- Real diagnostic/UI entrypoints consume the supported response with zero
  home/credential reads and zero mutation/provider calls. Plant an unknown
  to absent conversion and an automatic repair/login call separately; both
  must fail their intended assertions beside the valid display control.
- Raw synthetic secret-bearing error and unexpected fields cannot reach board
  resources/logs; ordinary safe diagnostic fields remain visible. Schema
  fixtures prove consumer behavior only, not platform-reader qualification.

## Dependencies and paths

L15-0/2/3/4 published and released, plus the existing compatible Curator entry
path. Source baseline `ab63db823`: `tools/board-cli/internal/spawn/
curator_doctor.go` currently classifies plain resolve compatibility;
`curator_repair_gate.go` retains its 0.14-only automatic-repair boundary.
Do not conflate either with the new readiness API. Add the bounded status
consumer/guidance at the actual doctor/spawn/hosted presentation call sites,
sanitized outcome types, tests and operator docs. Serialize shared diagnostic
and module/pin files with M5 and source consumer work; no token custody or
broker client belongs in the board runner or session host.
