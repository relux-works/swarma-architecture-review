# T3 — Qualify and implement the same-user final token executor

- **Owner repository:** curator-agent-launcher.
- **Normative clauses:** T0 L5–L8; CIP-0010 C3.2–C3.6/C6; retained CIP-0003 final-executor item 5; launcher SPEC §10.3's binding/conflict/child guarantees, with explicitly published local scope; Decision 0021 entry-point ownership.
- **Attack surface:** material release into the real Claude process after admission/serialization.
- **Size:** M for one published route; add each different final route as an independently reviewed consumer, not a flag that disables checks.

## Acceptance

1. Implement the published local final-execution entry point using Curator-owned source/home admission and protected node access. Required-understanding metadata survives to that point; unknown source/capability and different UID/host refuse before lookup.
2. Re-resolve binding to current profile, source generation, channel, executable digest, endpoint and policy. Check inherited/settings/helper/provider/argv conflicts before secret read and recheck changed identities before launch. Do not derive source authority from a plan digest or caller readiness.
3. Inject only into the actual Claude child environment. No mutation of global parent env, composition `EnvLiterals`, `env_names`, tracked ax request, hosted payload, logs or argv. No intermediate executor receives the token and no credential FD survives into the child.
4. Pin capability to exact executable/platform/mode/child-policy qualification. Prove selected-source/no-native-read behavior and uncontrolled child exclusion under real harness execution; include MCP interpolation and settings reload. A known-leaking control verifies the detector. No current-host live qualification is implied by the collective review.
5. Known expiry/revoke/source replacement refuses without fallback. Bounded sanitized auth failure retains uncertainty; resume with replacement token is separately measured. `--bare` and unqualified interactive routes refuse.
6. Preserve current tracked/hosted refusal until their **actual** final route implements the contract. Direct execution alone does not close the owner-requested spawned-agent workstream.

## Mandatory negatives and positive controls

ST-07–11/13/14 in [design §8](../designs/setup-token-local-source.md#8-required-conformance-pairs), each against the real public entry point as well as narrow unit seams. Wrong binding/executable/endpoint, stale generation, unknown carrier/capability, native auth conflict, token literal and remote UID refuse before lookup/exec; same exact tuple with valid binding passes. Child/script/MCP probe controls must distinguish real leakage from setup failure. Direct synthetic exec tests cannot establish Claude native-read or child-scrub behavior.

## Dependencies and paths

T0 finalized carrier/route; T1 protected API; T2 source projection; qualified Curator runtime preparation where D4 requires a private home. Land after v4 consumer changes on launcher `internal/fragment`, `internal/composition`, `internal/execution`, `cmd/curator-run/main.go` and their conformance fixtures. Local final-intake implementation may use new files/package with an explicit published entry point; do not silently implement pending cross-user §10 grammar. Actual current risk: `internal/execution/execution.go:83` serializes literals, `:143` starts ax rather than Claude.
