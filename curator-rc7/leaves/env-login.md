# L15-3 — Execute a bounded vendor login in a trusted isolated home

- Owner repository: **curator**.
- Normative clauses: login-readiness §§2–3, 5–6; environments §§7.4, 10.1;
  profile-codex-settings §§3–6; D8, D14.
- Attack surface: authority and I/O at the vendor-login process boundary.
- Size: 3. Baseline curator `0d00a109`, spec `5509499`.

## Exact surface and acceptance

```text
curator env login <env-id> [--profile <name>]
```

Canonical lookup/CLI environment aliases match `env resolve`. Require an
installed profile, trusted current home, supported adapter and **isolated,
home-owned source**, even if already present. No install, repair, migration,
activation, source replacement, arbitrary vendor arguments, shell command or
stdin-key mode. Shared refuses before exec with native-login guidance; stale
home reports existing resolve/repair guidance. External sources give their
own enrollment guidance, not local login. This command never collects a
Claude setup-token.

Require both terminal stdin and stdout and no detected headless/CI marker.
Use the trusted machine executable outside profile-owned bins, a neutral cwd
and direct argv: `claude auth login`, `codex login` plus its single validated
typed store block, or `muse login` with all managed XDG paths and file literal.
No project MCP/tool/prompt channels. Explicit source and store conflicts
refuse before exec; do not strip a selected credential source to manufacture
home readiness. Resolve once through L15-1, with input revalidation before
exec and before final reporting. Release mutation locks before browser wait.

The child owns terminal/browser I/O. Curator never captures, parses, persists
or logs credential-bearing child output, callbacks, stdin or env values.
Disable transcript capture at this process boundary; emit only sanitized
post-exit metadata. Do not use `exec.Command(...).Output()` or a tee here.

| Outcome | Exit / required behavior |
|---|---|
| Child 0 and recomputed home presence | 0 |
| Curator policy/resolve refusal; child 0 plus absent/unknown post-read | 1; distinguish refusal from vendor failure |
| Invalid usage or noninteractive input/output/CI | 2, no child |
| Nonzero child or signal | Preserve child code or ordinary platform signal convention; identify origin despite overlapping numeric codes |

Failure/cancellation leaves vendor-owned writes intact; no logout, credential
deletion or store copying. Claude repeats same-session guidance and the
explicit setup-token alternative for inference; forcing a file store is not
a repair for an OS user without a login Keychain.

## Negative tests and positive controls

| Negative / forbidden effects | Positive control |
|---|---|
| Shared home (including present) executes or mutates native credential | Trusted current isolated absent/present home permits the deliberate command |
| Redirected stdout, missing stdin TTY, CI or invalid flags starts ceremony | Both TTYs and interactive context attach directly |
| Repository/profile PATH executable, cwd config, stale/untrusted home, unsupported adapter/mapping executes | Trusted executable runs from neutral cwd with exact argv/env |
| Environment token/source conflict stripped or counted as successful home login | Home-only source with no conflict; external source gets enrollment guidance and no exec |
| Child 0 overrides unknown post-read; child 2 mislabeled solely as Curator usage | Child 0+present; nonzero/signaled child retained with sanitized origin |
| Child sentinel output captured in logs/receipt/summary; native config rewritten | Terminal-only synthetic sentinel; sanitized result and unchanged native config |
| Selector/source/home changes between check, exec and post-read redirect login | Stable revalidated tuple proceeds; changed tuple stops affected operation |

Use a disposable synthetic child and terminal fixture, not real credentials.
Pair tripwires with a child that records only nonsecret argv/cwd/env-name
metadata. A bounded mutant enabling shared exec or redirecting stdout must
produce the intended test failure. Test the real CLI entry and composition.

## Dependencies, paths, release cut

L15-1 policy and L15-2 metadata; qualified Codex/Muse delivery paths before
their respective ceremonies are enabled. Likely paths: new
`cmd/curator/envlogin.go`, `cmd/curator/env.go` dispatcher,
`internal/envprofile` login projection, terminal/process adapter and tests,
help/docs. Serialize `env.go` changes with status/materialize integration.
Required in rc.7; no live login is executed by this planning collective.
