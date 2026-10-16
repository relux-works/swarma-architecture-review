# C5 — Preserve Codex settings through hosted start, client and resume

- **Owner repository:** skill-project-management.
- **Normative clauses:** profile-codex-settings §§3–4,6–7; CIP-0018 leaf 5;
  local-hosted-launches §§3–5 for prepared home/policy identity.
- **Attack surface:** a host or reconnecting client changing accepted backend
  ownership while reusing an existing app-server/session.
- **Size:** M. Settings delivery only; general hosted activation is separate.

## Acceptance

Carry the published typed settings block and accepted profile/fragment/plan
identity through app-server composition, attached client, host reuse and cold
resume. C2 owns scalar serialization; the host owns private tools/trust/MCP
policy. Keep those channels disjoint. Do not serialize profile settings into
native, seed, snapshot or private session `config.toml`.

Fresh host start applies the accepted exact `-c` block. Reuse/resume must match
that identity or require the normal explicit new-session/restart transition;
later machine policy cannot relabel the existing host. Raw argv, native
profiles, equivalent client/RPC config and aliases that could replace storage
refuse, including equal duplicates. Reject unsupported delivery before any
provider start rather than allowing a client-side default.

Codex exclusive MCP policy must use an exclusive base document; merging
`-c mcp_servers={}` is not proof inherited servers were cleared. Preserve the
existing seed-revision residuals and the required policy on start and resume.
Curator's protected runtime preparation/verification is a dependency when
using the new hosted route; this leaf creates no receiver-owned home inventory.

## Paired negative tests and controls

- Same accepted settings succeed at start/reuse/resume; changed or missing
  required settings refuse or take an explicit new-session transition before
  reuse. Assert old host policy/state remains unchanged on refusal.
- Hosted app-server sees the exact typed override; a valid direct launch
  cannot mask dropping it only on the host path. Plant that omission and
  require the actual hosted-entry test to detect wrong effective policy.
- Raw split/joined config, profile, dotted/quoted/table or RPC competitors
  refuse even when equal; unrelated host policy remains functional.
- Seed/native/private config stays unchanged as regards profile settings;
  valid host-owned policy stays in its independently admitted channel.
- A conflicting inherited MCP server remains demonstrable under the unsafe
  empty-table control; the exclusive host base excludes it on both start and
  resume. Schema/argv-only fake success is not vendor loader qualification.
- Unsupported successor/revision or unavailable materialization/runtime
  contract refuses without provider execution; published supported tuple
  succeeds using its real production path and protected identity.

## Dependencies and paths

Depends on carrier publication, C2/C3, C4 exact supported-version evidence,
and the applicable host home/plan contracts. Can land dormant before the
complete local-hosted three-runtime activation. A capability matrix must not
claim hosted Codex settings until this leaf's route passes.

Confirmed at fresh `ab63db823`: `tools/board-cli/internal/sessionmanager/
codex_host.go` consumes ManagedHost.Argv, owns reuse/remote resume and performs
thread/resume; `curator_identity.go` owns provenance matching. Integrate with
`internal/spawn/curator_fragment.go`, `internal/spawnruntime/runtime.go`,
host plan composition and their tests; update the actual module pin/vendor.
Serialize these files with M5 and the general hosted/runtime owners. Add a
distinct acceptance row to their release matrix rather than hiding this work
inside common Curator runtime bootstrap.
