# M4 — Preserve Muse v4 through curator-run

- **Owner repository:** curator-agent-launcher.
- **Normative clauses:** environments §§7.9, 10.1–10.3; CIP-0017 leaf 4;
  login-readiness §2.1 as specifically amended by Muse v4.
- **Attack surface:** fragment decode, launch composition and covered request.
- **Size:** M.

## Acceptance

Update the strict reader and SPEC together. Parse complete v4 with duplicate
rejection, validate cross-field agreement and common-XDG-parent constraints,
then transport Muse's actual revision, root fact and backend to the plugin.
The inspected `internal/plan/context.go:18` currently excludes Muse and
constructs v1: parser-only work is insufficient.

Preserve typed identity and file backend through direct, dry-run and tracked
execution, canonical fragment digest and plan serialization. Ambient backend
is replaced by fragment file; explicit incompatible plan selection refuses.
Apply no extra root-layout checks. Follow M3's qualification result. Network
relocation uses the admitted snapshot contract or refuses without deleting
the root fact. Managed v3 refuses with upgrade guidance and no retry.

## Paired tests

| Refusal / forbidden effect | Positive control |
|---|---|
| Duplicate JSON keys, unknown revision/member, root null/false/empty/extra or wrong adapter | Frozen valid v4 fixtures through the production decoder |
| Missing/wrong backend, store/env disagreement, sibling XDG parent, HOME, Muse system/MCP channel | Exact five-key Muse env, file selection and optional closed root |
| A dropped root/backend between parser, Context, plugin, sealer or tracked request must fail | Full end-to-end captured child argv/env and covered identity agree |
| Ambient or late merge replaces file, explicit conflicting override survives | Ambient contradiction is overridden, explicit contradiction refuses |
| Fact on serve/unqualified build proceeds; fact erased only for network launch | Qualified forms succeed, admitted relocation preserves root |
| Raw native option defeats exclusion; v3 triggers fallback | Nonconflicting options and fact-free valid v4 succeed |

Observe no child exec and no usable plan on rejection. Retain old non-Muse
revision acceptance and permission/source semantics. Plant a Context mapping
that drops Muse: the real launch-path test must fail, not just a JSON test.

## Dependencies and overlap

Consumes M3's immutable module tag and M2 evidence. Can implement strict
reading against existing v4 fixtures in parallel with M1/M2; release follows
the coordinated producer/consumer gate. Explicit Codex file/keychain remains
unsupported until C1–C3 and platform qualification; schema validity grants no
backend capability.

Paths: `SPEC.md`, `internal/fragment/{fragment,json,resolve}.go`,
`internal/plan/context.go`, `internal/composition/`, `internal/execution/`,
`go.mod`, `go.sum`, production-entry fixtures. Serialize those shared files
with the Codex launcher and snapshot/hosted launch owner.
