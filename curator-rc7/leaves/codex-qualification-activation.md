# C7 — Record joint Codex qualification and activate the published revision

- **Owner repository:** curator-spec.
- **Normative clauses:** CIP-0018 implementation leaf 7;
  profile-codex-settings §§5–7; environments §§7.9,10.2.
- **Attack surface:** publication that overstates producer/consumer readiness.
- **Size:** S; evidence and normative activation, not the curator release tag.

## Acceptance

Record the jointly reviewed qualification matrix for C0–C6: exact carrier
identities, producer and consumer commits/tags, vendor binary/build/platform,
production entrypoint, positive and intended negative results, control plant,
and sanitized immutable evidence reference. Mark missing rows unverified;
do not infer behavior from a schema, metadata presence, fake exec or another
route's success. Native/empty compatibility and old-reader rejection remain
explicit. Record unresolved refresh and source/backend limitations accurately.

Enable the producer revision only under the adopted rollout contract once
strict consumers and required supported tuples exist. Every advertised route
must pass its own row. An unavailable host/relay route stays explicitly refused
and unadvertised; a scoped local-only activation is permissible only if the
published rollout contract admits it. If §7's full consumer gate still applies,
absence of a remote consumer is not a waiver: keep activation pending or first
publish a reviewed scoped rollout amendment. Never fabricate passing evidence.

R0 in curator consumes this record for tag/capability claims. It does not
replace this curator-spec ownership. Conversely a spec record alone does not
prove the actual distributed binaries carry the qualified implementation.

## Negative/control pairs

- Missing required consumer, unsupported mode, unobserved refresh or stale
  evidence refuses activation; a complete same-identity matrix is accepted.
- Changing producer/carrier/build after qualification invalidates the affected
  row; unchanged exact identities retain their established narrow result.
- An old-token/new-member sample and stripped-required-payload sample still
  refuse under the real consumer; valid adjacent old/native/new cases succeed.
- A deliberately omitted hosted or relay row must be caught by the activation
  checklist/checker whenever that route is required; a declared unavailable
  row is not presented as passing. Record the intended failure, not a tool error.

## Dependencies and paths

C0 publication, C1 producer, C2 plugin, C3 launcher, C4 vendor qualification,
C5 hosted settings and C6 relay as required by the adopted route matrix.
No new package setting vocabulary or credential-source authority.

Paths: `protocol/profile-codex-settings.md` qualification/rollout section,
`protocol/environments.md` version/transport references,
`conformance/profile-codex-settings-v1/README.md` and the newly published
successor-carrier evidence inventory. Preserve frozen historical cases/schema
bytes. Serialize these shared spec files with C0 and L15-0 publication.
