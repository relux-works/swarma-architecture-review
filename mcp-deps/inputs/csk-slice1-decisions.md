# MCP slice 1: owner decisions and frozen contract (2026-10-13)

Base design: board resource `TASK-261013-cnfbiu_design.md` on TASK-261013-cnfbiu (proposal-v1, called "the design"
below). This file records the owner's decisions and the orchestrator's amendments. **Where this file and the design
differ, this file wins.** Leaves must not re-decide anything stated here; a leaf that finds a contradiction stops and
reports it in its results instead of choosing.

## Owner decisions (Ivan, 2026-10-13)

- **D1 Consent by authority.** Operator consent is required before csk publishes a declaration that:
  - executes code: `transport: stdio`; or
  - routes a secret: the declaration references any environment variable (stdio `env_names`, or an http `headers`
    entry with `env`).

  A remote `http` declaration with no environment reference (`auth.kind` `none` or `oauth`) installs without consent.
  Every declaration is still printed in the plan before publication.
  Why the second clause: an http entry whose header references `$GITHUB_TOKEN` makes the client send that token to a
  repository-chosen URL. That is credential routing and needs the operator, exactly like code execution.
- **D2** Project **Skillfile schema 3** carries `mcp_servers`. Skill manifests stay at versions 1–8. The global
  Skillfile keeps rejecting schema 3 until slice 3.
- **D3 Git policy.** Slice 1 implements `local` only:
  - a native file csk creates gets an exact-path ignore entry;
  - a tracked native file is patched in place and the change stays visible to git;
  - `git_policy: "shared"` is recognized and refused with `mcp_capability_unsupported`. It needs `adopt`, which is
    slice 2+.
- **D4 Windows.** HTTP entries and stdio entries whose command resolves to a native executable are supported. A
  command that resolves to a batch launcher (`.cmd`/`.bat`), or a known batch-only launcher (`npx`, `npm`, `pnpm`,
  `yarn`), is refused on Windows with `mcp_windows_batch_unsupported`. There is no `cmd /c` rewrite.
- **D5** Slice 1 writes Claude Code, Codex CLI and Cursor only. Gemini, OpenCode, Windsurf and Devin are later, as
  distinct versioned profiles. Naming any other agent in `agents` refuses with `mcp_capability_unsupported`.
- **D6** No `adopt` and no takeover in slice 1. A foreign same-name entry is a conflict, even when its bytes are equal.
- **D7** Only inline `server` declarations. A `reference` (git, file or url) is recognized and refused with
  `mcp_capability_unsupported`. git/file references come in slice 2, url in slice 5.
- **D8** The residual is documented: native clients may pass a server more environment than `env_names` lists.
  csk does not claim confinement.

## Orchestrator amendments (binding)

- **A1 No new runtime dependency.** `pyproject.toml` has `dependencies = []` and keeps it.
  - Native edits are span edits over the existing bytes, followed by a full strict re-parse.
  - The re-parse must equal the expected document: the old document with exactly the intended single-entry change.
  - Bytes outside the edited span stay identical by construction.
  - Parsers: TOML via stdlib `tomllib`; JSON via `protocol_json.loads`, which is strict and rejects duplicate keys.
- **A2 Strict JSON surfaces.** `.mcp.json` and `.cursor/mcp.json` are edited as strict JSON (RFC 8259, UTF-8, no
  BOM).
  - Comments, trailing commas, a BOM, duplicate keys or invalid UTF-8 refuse with
    `mcp_native_config_unsupported_syntax` before any write.
  - csk never strips or rewrites what it cannot preserve.
  - A file over 4 MiB refuses with `mcp_native_config_too_large`.
- **A3 TOML surface** (`.codex/config.toml`).
  - csk writes only the standard table form:
    ```toml
    [mcp_servers.NAME]
    command = "npx"
    ```
    plus `[mcp_servers.NAME.env_http_headers]` when needed.
  - Foreign entries in any form (inline table, dotted keys, quoted keys) are only *read*, through `tomllib`, to detect
    presence.
  - An owned entry is edited only when its span is exactly a standard-form table group that csk can locate. Otherwise
    the edit refuses with `mcp_native_config_unsupported_syntax`.
  - **A comment line is never deleted.** Removing an entry removes its header and key/value lines; comments inside
    the span stay in place.
  - When the last entry is removed, an empty `mcp_servers` table is semantically equal to an absent one.
- **A4 Typed read states.** Every native read returns exactly one of:
  - `absent`: no file and no dangling link;
  - `present(entries)`;
  - `unreadable(reason)`: permission, I/O, not a regular file, a link, or a reparse point;
  - `malformed(reason)`: syntax, duplicates, encoding or size.

  Only `absent` may create a file. `unreadable` and `malformed` refuse all writes to that surface.
- **A5 Consumer identity.** Computed from `locking.canonical_project_identity(project_root)` plus the scope. It is
  never a caller-supplied path string.
- **A6 Manager-home state layout.** Rooted at the csk home, the directory holding `config.json`:
  - `state/mcp/ledger/<consumer-id>.json`
  - `state/mcp/consent/<consumer-id>.json`

  Both are private, regular files reached without following links. A missing ledger means "owns nothing". An
  unreadable or invalid ledger means "ownership unknown": no write or removal is allowed on that consumer.
- **A7 Validation order** follows the design §9, with D1 consent:
  1. syntax, type and closed fields;
  2. scope, name, env, url and recipe rules;
  3. agent selection;
  4. capability (including D3, D5, D7);
  5. ownership and transaction feasibility;
  6. consent;
  7. pure requirement check;
  8. publication.
- **A8 Refusal codes.** These are stable strings and tests assert them:
  - from the design vectors: `mcp_declaration_invalid`, `mcp_scope_mismatch`, `mcp_agent_selection_invalid`,
    `mcp_env_name_reserved`, `mcp_command_invalid`, `mcp_url_invalid`, `mcp_capability_unsupported`,
    `mcp_runtime_pin_required`, `mcp_plan_unapproved`;
  - added here: `mcp_native_config_unsupported_syntax`, `mcp_native_config_too_large`,
    `mcp_native_config_unreadable`, `mcp_entry_conflict`, `mcp_entry_drift`, `mcp_ownership_unknown`,
    `mcp_windows_batch_unsupported`.
- **A9 Vectors.** Design vectors V01–V12 are frozen, with two adjustments:
  - V03 expects `mcp_plan_unapproved` only where D1 requires consent. V03 as written (http, `auth: none`, no env
    reference) must therefore **admit without consent** under D1.
  - Add V13: http with header `{"Authorization": {"env": "DOCS_TOKEN", "prefix": "bearer"}}` and policy unapproved
    expects `mcp_plan_unapproved`.
- **A10 Drift policy.** This deviates from design §4 rule 4, deliberately: it is non-destructive and keeps installs
  usable.

  | Case | Result |
  | --- | --- |
  | Owned entry that is still declared, modified by the user | **skipped**: no write, ledger entry kept, warning `mcp_entry_drift`; the install continues and `status --check` reports drift (exit 1) |
  | Owned entry that is still declared, deleted by the user (or its whole file deleted) | **restored**: re-added under the already-approved consent |
  | Owned entry no longer declared, modified by the user | **released**: ledger entry dropped, native entry untouched, warning |
  | Owned entry no longer declared, deleted by the user | ledger entry dropped silently |

  Why restore is acceptable: deleting an entry is not a client's disable mechanism. Clients have native disables, such
  as Claude `disabledMcpjsonServers` and Codex `enabled = false`, and the latter is an edit, so it is skipped as drift.
  The Skillfile stays the declared state. A user who wants a server gone removes it from the Skillfile.

  Refusals that block the whole install, before any write:
  - grammar and capability errors;
  - `mcp_entry_conflict`, a foreign same-name entry;
  - `mcp_native_config_unreadable` or `mcp_native_config_unsupported_syntax` on a surface that needs a write;
  - `mcp_ownership_unknown`;
  - `mcp_plan_unapproved`.

## Slice 1 leaves

| Leaf | Story | Depends on | Lands |
| --- | --- | --- | --- |
| M1 declaration contract (pure) | mcp-declaration-contract | none | internal module, no CLI wiring |
| M2 native config codecs (pure bytes) | mcp-native-config-codecs | none | internal module, no CLI wiring |
| M3a ownership, consent and reconcile planner | mcp-ownership-consent-planner | none (opaque inputs) | internal module + manager-home stores |
| M3b install integration, transaction, UX, docs | mcp-install-integration | M1, M2, M3a on main | user-visible feature, CHANGELOG |

M1, M2 and M3a must not change any user-visible behaviour, and must not edit `CHANGELOG.md`, `README.md` or
`docs/`. The Skillfile loader keeps refusing schema 3 until M3b wires it in.
