# L15-4 — Prepare every participant without activation or hidden login

- Owner repository: **curator**.
- Normative clauses: login-readiness §§1.2, 3–6; environments §§9, 10.1,
  12; D8. Source/store rules from L15-1 remain prerequisites.
- Attack surface: orchestration across install, resolve, login and partial failure.
- Size: 5. Baseline curator `0d00a109`, spec `5509499`.

## Exact surface and acceptance

```text
curator profile prepare <source-or-name> [--non-interactive]
```

An installed name uses its existing lock/snapshots. Otherwise accept the same
explicit source operand forms and default naming as `profile install`;
ambiguous bare names refuse, never become guessed URLs. Do not silently
inherit install's `--use`, `--takeover` or update authority. Existing trust,
audit and install admission gates apply. If a source needs additional
explicit installation options, guide the operator to `profile install`,
then prepare the installed name; do not invent undocumented flags.

Interactive operation installs only when absent and preserves machine-current
and **all** scoped-current selections. Enumerate every participant from the
selected lock and effective machine policy. Reuse resolve/repair without
bypassing trust, isolation, migration or credential conflicts; an existing
lock cannot be silently updated as a side effect of preparation.

Only supported, isolated, home-owned **absent** login may enter L15-3. Present
does not relogin; unknown never prompts; shared/native absence gives native
guidance; external sources give enrollment guidance. Recompute all rows and
report environment, currency, login, source, store/backend, caller scope and
next action. Keep independent errors; cancellation starts no further login
ceremonies. Completed transactions and vendor writes remain after partial
failure. Release mutation locks before browser interaction and revalidate
home/source/selector before execution and reporting.

Explicit **or detected** noninteractive mode is report-only: no fetch,
install, repair, activation, browser or login. Read-only resolution of
installed participants must not call mutation/recovery code. Missing profile
means installation required and participation unknown, never success from
an empty table. An installed/current/present repeat performs zero writes.

Exit 0 requires every participant current/present and no failed operation.
Missing/unknown readiness, unresolved participant, failure or cancellation
gives aggregate 1; invalid arguments 2. Do not return the last vendor child's
exit. Participating OpenCode currently forces unknown/1; document it, never
filter that row. Source metadata presence does not promise inference.

## Negative tests and positive controls

| Negative / forbidden effects | Positive control |
|---|---|
| Reinstall/update existing lock, activate profile, mutate any scoped-current marker | Missing explicit source installs once without activation; installed name retains bytes |
| Only current environment or convenient adapters appear | Multi-participant lock emits all rows, including failures and OpenCode |
| Headless absent profile fetches; stale home repairs; empty invented matrix passes | Existing current/present profile reports 0 with no writes; missing profile reports 1 |
| Unknown/conflicting/shared/external source invokes home login; present is repeated | Supported isolated absence starts exactly one admitted ceremony |
| One failure rolls back successful independent work or hides later rows | Partial failure retains prior successes and emits complete sanitized table |
| Cancellation starts a second ceremony or deletes vendor state | Cancelled row recorded, later ceremonies skipped; retry only remaining needs |
| Browser wait holds mutation lock or concurrent selector/home change redirects login | Stable tuple proceeds after lock release; revalidation detects changed tuple |
| `--non-interactive` absent but CI/non-TTY still mutates | Explicit and detected report-only modes are equivalent |

Drive production `profile prepare` with synthetic install/resolve and vendor
boundaries, verifying observable transactions and untouched selections.
Retain regression witnesses for dropped participants and unknown→login.
Control plants must show that a single hidden repair or repeated login is
detected, not just compare formatted rows. No builds/tests are run here.

## Dependencies, paths, release cut

L15-0–L15-3, existing installer and resolver. Likely paths: new
`cmd/curator/profileprepare.go`, `cmd/curator/profile.go`, a focused
`internal/envprofile` coordinator, help, tests and
`docs/environment-config.md`. Serialize profile.go/status/managed integration
with other producer leaves; a coordinator module can be developed separately.
Required in rc.7 after the early v4 unblock, not before it. Consumer guidance
in skill-project-management follows the released command/status contract and
must not inspect home files or credentials itself.
