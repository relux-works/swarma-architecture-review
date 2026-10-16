# T1 — Implement protected node enrollment and revocation

- **Owner repository:** curator.
- **Normative clauses:** T0 L2/L8; CIP-0010 C1, C3.5, C4 and Security/Revocation; CIP-0003 protected read order retained by C6.
- **Attack surface:** local secret object lifecycle, including partial publication and races.
- **Size:** M, independent protected-store module plus narrow CLI wiring.

## Acceptance

1. Implement Claude-only `env credential enrol ... --token-stdin`, metadata `status` and local `revoke` with the exact T0 command/input grammar. No vendor invocation, native credential import, environment/argv token ingress, arbitrary source paths or broker operations.
2. Store secret only in the approved per-user 0600 object under protected 0700 ancestry. Validate ACL/ownership/type/mode and descriptor identity; reject symlinks/hard links/substitution. No permission-repair shortcut, generic journal, backup copy or shell command handling the material.
3. Serialize replacement/revoke/final-read operations. A crash never activates mismatched metadata/material generations. Preserve the prior coherent enrollment or expose a recoverable unavailable state. Re-enrollment rotates opaque reference/generation so old plans do not bind a replacement by label.
4. Report lifecycle metadata only, never material, hash, prefix or raw input errors. Unknown issuance/expiry stays unknown. Revocation means future local delivery disabled; it never claims vendor revocation or recall from running sessions.

## Mandatory negatives and positive controls

- ST-02: empty/multiline/oversized/control-containing/terminal input and invalid date refuse with no echo or old-source mutation; bounded synthetic token and optional stated date succeed.
- ST-03: protected-path attacks, open/reopen races, wrong user/modes/ACL and unexpected hard links refuse without writing attacker targets; safe regular source control enrolls/reads metadata/revokes.
- ST-04/11: inject interruption at every publication boundary; interleave enroll/revoke/release and stale-reference replay. Assert no mixed usable generation or post-revoke release. Serial completed actions remain usable.
- Secret leak detector gets a planted sentinel in a disposable diagnostic fixture and must fail for that reason. Scan actual success/refusal/recovery output and store metadata; exclude the deliberately approved secret object, not arbitrary directories.

## Dependencies and paths

T0 complete contract; new protected store can develop separately from readiness. Proposed new `internal/envcredential/` (name finalized by implementation owner), `cmd/curator/envcredential.go`, CLI dispatch/help/docs. Shared `cmd/curator/env.go` wiring is serialized with login/materialize leaves. Reuse existing no-follow/atomic primitives only after confirming they do not log/journal secret values. No credentials are placed under `internal/envprofile` content hashes or snapshot pipelines.
