# Source baselines and claim limits

Author: astra-03. Round 1, 2026-10-16. All source repositories were inspected
read-only; none was fetched, pulled, built, installed, or executed as a product.

| Source | Inspected identity | Bound |
|---|---|---|
| curator-spec | `55094992185521dba470d80e1745d60af7bf496c` | Matches mission normative baseline |
| curator | `0d00a109ad1da77a5506747c89f24af9442eb341` | Newer than input pack's historical `205272e7`; producer still v2/v3 |
| skill-agents-management working tree | `a2a6e9f377f62a5872d99ecdfff0d1690e385f2a` | Stale; not evidence about v0.5.66 |
| skill-agents-management local historical tag | `v0.5.65`, `a8fff59` lineage | `git show` confirms old path/header inspector and 1.4.7 qualification; v0.5.66 object unavailable at first inspection |
| curator-agent-launcher | `9ad2f0160a1995af94b5069e4e85638140cb2712` | Strict parser accepts v1-v3; module pin v0.5.62 |
| skill-project-management | `ad68902f74ae55b1cd0445fef58390b42feea3dc` | Historical board-cli pin v0.5.41-0.maint.1; do not substitute for current deployment |

The convener subsequently supplied fresh read-only source copies. Inspection
now confirms agents-management `acae871c0d53cd580cfef1863a75c58e59b59690`
(v0.5.66), project-management `ab63db82365cdf9229ad60f72cc82997cbbe5043`
(agents-management pin v0.5.65), and the same launcher `9ad2f016`.
These supersede the stale sources for current consumer evidence.

At acae871, `pkg/agentic/curator_context.go:680–725` validates v4 agreement
and explicitly refuses applying non-native Codex storage.
`pkg/agentic/systems/muse/personal_context.go:20` qualifies only
1.4.7-R6101.1; `seal.go:217` also checks the actual attested build.
`context.go` refuses managed-network relocation instead of erasing the fact.
`env.go:130` overlays the backend after parent filtering. This confirms
released v4 policy support, not 1.4.8 exclusion qualification.

The same release has a concrete offline probe candidate: README:968 and
`systems/muse/args.go:117,159` map pseudo-model `echo` to `--provider echo`
for both forms, with no Meta model/effort flags. Tests prove argv construction,
not actual 1.4.8 loader execution. M2 preserves that distinction.

## Confirmed seams

- Curator `internal/envfragment/envfragment.go:54` has no root/store fields;
  `:66` emits v3 for Muse. `:163` returns after the four HomeVariables, so a
  backend addition to JSON alone would disappear from env/shell. `:347`
  treats every env value as a path: the file literal needs a single exact
  registry exception, not a general non-path escape.
- Curator `internal/envprofile/managed.go:2413` builds from a verification
  result. `:2564` calls it on current verified homes and otherwise follows
  refusal/repair paths. Root derivation belongs here, using the actual
  verified root surface, not a proposed write or launcher path inspection.
- Curator `internal/envprofile/muse.go:52` already preserves missing versus
  unreadable versus conflicting links and checks target liveness. Reuse these
  guarantees; D10 is not permission to relink a forked credential.
- Launcher `internal/plan/context.go:18` currently drops every adapter except
  Claude/Codex, and creates a v1 context. Updating only its fragment parser
  cannot transport Muse root policy. Its `internal/execution/execution.go:47`
  serializes environment literals and fragment digest into tracked requests;
  the new literal and typed identity must survive that path too.
- Spec `protocol/profile-codex-settings.md` §§3,7 requires a typed
  `codex_settings` payload and strict successor envelopes. Published v4
  instead has `credential_store.config_overrides`, and forbids unknown
  top-level `codex_settings`. This is a normative publication dependency,
  not an implementation naming choice.

These are source-inspection findings. No runtime or vendor qualification was
performed by this collective seat. Private input-pack observations must be
sanitized before reuse in a public implementation repository.
