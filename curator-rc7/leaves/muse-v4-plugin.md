# M3 — Audit released Muse v4 plugin and close the qualification seam

- **Owner repository:** skill-agents-management.
- **Normative clauses:** environments §§7.9, 10.2; CIP-0017 implementation
  leaves 2–3 and compatibility items 2–5.
- **Attack surface:** typed manager policy becoming argv and sealed identity.
- **Size:** S for qualification-table uptake; M only if replay reveals gaps.

## Acceptance

Fresh read-only v0.5.66 source is `acae871c0d53cd580cfef1863a75c58e59b59690`.
It carries typed root/store facts and removes the inspector. Its qualification
map still admits only 1.4.7-R6101.1 and checks the attested build at seal time.
This is a qualification follow-up, not a request to reimplement completed work.

Transport validated root/store policy through every real public build and
seal entrypoint. Required root yields exact exec exclusion or interactive
`-c`, `context.foreign_personal_skills=false`; dry-run uses the same builder.
No file stat/read/header or symlink test decides policy. The exact qualified
1.4.8 build from M2 must be admitted; a 1.4.7-only check cannot silently drop
required policy. Serve/unqualified form/build refuses before agent exec.
Network relocation preserves root via admitted materialization or refuses.
Seal/provenance includes the fact and backend; later changes invalidate reuse.

## Paired tests

- Qualified exec/interactive with root fact succeeds with exact argv; absent
  fact emits neither exclusion. Wrong build and serve with fact refuse.
- A linked, regular, absent, or inaccessible fake on-disk AGENTS.md cannot
  alter argv for identical validated facts. Plant a legacy inspector call;
  a bounded no-inspection test must catch it.
- Fragment file beats ambient backend; explicit contradictory backend
  refuses. Later environment merge cannot restore the conflicting value.
- Split/joined/aliased native configuration that can re-enable foreign
  skills refuses; unrelated admitted native options remain usable.
- Managed v3 refuses with upgrade guidance even when root fact is absent;
  valid v4 with no root succeeds. No downgrade/retry/inference path.
- Root/backend identity tampering refuses replay/seal reuse; unchanged
  identity succeeds. Both permission modes preserve required exclusion.

## Dependencies and paths

Depends on M2 for release qualification; consumes frozen v4, not the pending
Codex successor. No dependency on token refresh. Publish a new module only if
required gaps exist, then provide its immutable identity to M4/M5.

Paths, confirmed in v0.5.66: `pkg/agentic/curator_context.go`,
its identity/validation tests, `pkg/agentic/systems/muse/{personal_context,
args,seal,env}.go`, and `pkg/vendorplugin/vendors/local-models/curator.go`.
Rebase path ownership onto the implementation candidate first. Serialize shared
context/identity files with the Codex typed-plugin leaf.
