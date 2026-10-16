# L15-6b — Preserve broker authority across dispatcher readiness handoff

- Owner repository: **swarma-dispatcher**.
- Normative clauses: CIP-0015 implementation leaf 8, Design §5;
  login-readiness §§1.1, 3, 7; CIP-0011; broker spec §§3.1, 4.1–4.2, 7–8,
  13.2, 14 and §18.15 at `ec7fb3d`.
- Attack surface: dispatch readiness/guidance being promoted to enrollment,
  binding or credential authority.
- Size: 1 for the integration seam after its authority contracts exist.
  Broker follow-on only; M6's minted-key backend handling is a different leaf.

## Acceptance

Consume only the adopted sanitized source/readiness or enrollment-required
outcome through the existing admitted dispatcher request boundary. Preserve
caller/session limits and unknown observations. No dispatcher home inventory,
native-login attempt or new token field/channel is introduced. Enrollment is
the separately authenticated human operator act, never a dispatcher act on
behalf of an agent. An agent/observer cannot widen authority by asking the
dispatcher to route an enrollment command or by presenting an operator name.

No status/guidance request creates or renews a lease, changes a binding,
spawns a helper/operator shell or copies a credential. A later real dispatch
still performs every current caller, principal/generation, grant, revocation,
admission-class and binding check at its owning boundary. Cached presence or
a previous allowed result cannot replace them. Lease material stays between
broker and the independently qualified final executor; the board runner,
session host and dispatcher do not become its transport.

## Paired tests and controls

- An authorized metadata-only/guidance request returns the sanctioned safe
  outcome; unknown/unavailable remains unknown, with zero bind/lease/enroll or
  provider effects. A valid separately admitted dispatch still reaches its
  existing execution path after all normal checks.
- Wrong principal/generation, forged operator claim, agent enrollment request,
  stale observation or broadened account/profile refuses at the intended
  boundary without any privileged helper or material access. Do not use an
  unrelated setup failure as rejection evidence.
- Synthetic secret/account details in a bridged outcome cannot reach generic
  plans, resources, journals or logs; the permitted closed metadata survives.
  Plant one status-to-lease call or trusted-cached-presence bypass and prove
  the real request-path detector catches it beside a valid metadata control.

## Dependencies and paths

[L15-6a](login-broker-curator.md), adopted source metadata and operator/observer
publication, and the dispatcher's existing authority transport. No dispatcher
checkout was supplied; its owner must pin the actual admission, typed outcome,
retry/journal and guidance paths before implementation. The known contract
boundary is `spec/dispatcher.md` referenced by the broker. Serialize shared
request/outcome types with C6/X2/M6, without requiring their unrelated archive
or key-delivery activation. This leaf grants no broker support to the local
setup-token API and invents no enrollment RPC or wire revision.
