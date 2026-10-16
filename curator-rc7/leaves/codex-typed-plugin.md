# C2 — Apply typed Codex overrides in the agent plugin

- **Owner repository:** skill-agents-management.
- **Normative clauses:** profile-codex-settings §§3–6; CIP-0018 leaf 3;
  the successor allocation in [C0](rc7-carrier-publication.md), coordinated
  with L15-0.
- **Attack surface:** typed launch policy to exact argv and sealed identity.
- **Size:** M; the mission states v0.5.66 explicitly refuses this capability.

## Acceptance

Extend the typed context and provenance identity, validate the exact closed
enum again at every public plan entry, and emit each admitted key once in
ASCII order as two argv elements. `file` becomes `-c` then
`cli_auth_credentials_store="file"`; qualified keychain maps to `"keyring"`.
Use a canonical TOML scalar serializer. Insert before prompt/`--` boundaries;
never a shell string or seed write. Empty/native preserves existing behavior.

Reject competing raw `-c`/`--config`, dotted/table/quoted aliases, native
profile selection or equivalent request fields that could replace the
backend. Equal duplicate values still have two owners and refuse. Other
provider/host-owned blocks keep their ordering and ownership. Cover typed
policy in sealing and reuse; missing required payload is not native silence.

## Mandatory paired tests

- Real BuildPlan/Args paths for interactive and exec produce exact pairs;
  absent payload preserves prior argv. Unknown key, mistyped enum and
  contradictory selection/payload refuse with no usable plan or config write.
- Split `-c`, joined `-c...`, split/joined `--config`, quoted/dotted/table
  aliases, native profile and equal duplicates refuse where the vendor parser
  would compete. Allowed unrelated native flags remain functional.
- Payload after positional prompt/`--`, double emission, string corruption,
  or mutation after sealing is caught by production capture/reuse tests;
  exact unchanged policy succeeds.
- Unsupported mode/release refuses before execution. A fake binary proves
  argv plumbing only; real no-model loader/login/app-server probes establish
  backend effect before capability is declared supported.
- A bounded omission on exec while interactive works must fail the test suite.

## Dependencies and paths

Depends on coordinated carrier allocation and the real supported-version
qualification matrix from the store owner. May develop against immutable
fixtures while C1 is dormant. All externally advertised consumers must be
available before producer activation; no temporary raw-argv workaround.

Paths: `pkg/agentic/curator_context.go`, identity/provenance validation;
`pkg/agentic/systems/codex/{args,composition,seal}.go` and real plan tests;
`pkg/vendorplugin/vendors/local-models/curator.go`. Confirm paths on the actual
current source. Serialize shared context files and tag publication with M3.
