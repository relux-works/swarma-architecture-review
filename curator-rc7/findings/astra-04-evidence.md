# astra-04 evidence ledger

Method: read-only normative/source inspection on 2026-10-16. No source checkout was pulled or modified, no build/provider probe was run, and no credential store was accessed. Every test name in the proposed leaves is a future acceptance requirement, not passing evidence.

| Source | Inspected identity | Use / limit |
| --- | --- | --- |
| curator-spec | `55094992185521dba470d80e1745d60af7bf496c` | Full CIP-0014/CIP-0016, both normative protocols, snapshot schema/corpus READMEs; accepted contracts and retained gates |
| curator | `0d00a109ad1da77a5506747c89f24af9442eb341` | env command dispatch, managed resolve/render seams, lock/recovery, existing no-follow/source snapshot/buildcache helpers |
| curator-agent-launcher | `9ad2f0160a1995af94b5069e4e85638140cb2712` | SPEC and hosted/fragment code inventory; production hosted route remains dormant in this baseline |
| skill-project-management checkout | `ad68902f74ae55b1cd0445fef58390b42feea3dc` | Old/dirty read-only tree; not current release evidence. Hosted route still unconditionally refuses, protocol 9 capabilities empty |
| skill-project-management local object | `b057ef468` | `git show` confirms already-registered musepty factory and child fragment resolver cited by CIP-0016; no checkout/pull required |
| skill-agents-management checkout | `a2a6e9f377f62a5872d99ecdfff0d1690e385f2a` | Stale source; mission's v0.5.66 statement is supplied release evidence, not verified from HEAD |
| mission input pack | review repository `curator-rc7/inputs/` | D1–D14, measured Claude/Muse/Codex facts and Muse quota bound; not measurements repeated here |

Do not conclude a missing Muse factory from the stale project-management working tree: it exists in the already-local CIP baseline object. Conversely, factory registration does not activate the hosted admission path or prove exact environment, goals or resume behavior.

No vendor web research was needed to establish these normative ownership and implementation seams. Claims about future provider behavior remain explicitly qualification-dependent.

Round 2 source refresh supplied by the convener (read-only, no pull by this seat):

- `sources/skill-project-management` at `ab63db82365cdf9229ad60f72cc82997cbbe5043`: `hosted_control.go:5–32` still unconditionally refuses the exact hosted plan; actual daemon construction registers musepty. `claude_host.go:486–531` takes `provenance.ManagedHome`, validates it against the fragment and applies it as `CLAUDE_CONFIG_DIR`; this is managed-home provenance, not immutable snapshot evidence. `codex_host.go:1703–1751` retains receiver-side config rendering and auth linkage on the legacy route. No new snapshot capability is inferred from these legacy improvements.
- `sources/skill-agents-management` at `acae871c0d53cd580cfef1863a75c58e59b59690` (v0.5.66): `pkg/agentic/curator_context.go:725` explicitly keeps Codex credential-store application false; `systems/muse/personal_context.go:20` qualifies only `1.4.7-R6101.1`, with the actual build rechecked by `systems/muse/seal.go:218`. v4 shape support is verified; Muse 1.4.8 and explicit Codex store execution are still separate gates.

These replace the stale HEADs as neighbour implementation evidence; older source entries above remain labeled historical. New moving-head news in the room is not silently substituted for these pins.

Artifacts: SNAP-ID, SNAP-LOCK, SNAP-CLOSURE, SNAP-PUBLISH, SNAP-CLI; HOST-HOME-SPEC, HOST-HOME-CODE; findings `snapshot-helper-boundaries.md` and `hosted-home-seam.md`. PLAN synthesis remains astra-01-owned.
