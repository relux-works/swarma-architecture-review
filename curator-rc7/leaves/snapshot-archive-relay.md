# X2 — Relay and journal the plan-covered archive unchanged

- Owner repository: **swarma-dispatcher**.
- Normative clauses: managed-home-snapshots §7; CIP-0014 implementation leaf 6 relay portion; CIP-0016 leaf 9 transport boundary; X0 and published R-TRANSFER.
- Attack surface: authorized opaque resource admission, relay and retry identity.
- Size: 3; follow-on, not inferred from local hosted success.

## Acceptance and paired tests

Authenticate/admit through the existing dispatcher boundary, verify published length/digest/caps and journal the actual relayed archive/manifest identity. Relay opaque bytes without profile resolution, home inspection, policy recomposition or credential access. Preserve exact identity through retries; corruption/loss cannot trigger remote resolve. Cleanup is scoped to the admitted allocation/generation and existing retention rules.

An admitted valid resource is relayed byte-for-byte and retries preserve its identity. Unauthorized caller, wrong adapter/profile, missing/read-failed resource, substitution after admission, declared/actual digest mismatch or stale generation refuses without dispatching child execution. A same-bytes self-minted plan still lacks authority. Plant a declared-digest-only journal implementation and require the real prepare/start relay checker to catch swapped bytes beside a valid control.

## Dependencies and paths

X0; X1 provides product integration evidence but relay implementation can use frozen canonical fixtures. Preserve typed settings via the separate C6 payload leaf, not by putting them into the snapshot. Paths are the dispatcher protected resource intake, transfer/journal/retry modules and R-TRANSFER conformance; exact implementation paths must be confirmed in its owner checkout before coding (not supplied to this collective). Serialize common plan/capability fields with C6 and the later hosted-to-dispatcher allocation transition. No local capability is advertised as cross-account qualification.
