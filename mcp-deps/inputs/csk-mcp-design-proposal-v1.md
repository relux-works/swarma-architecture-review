# Skillfile MCP declarations and native agent config materialization

Task: TASK-261013-cnfbiu — design-mcp-servers-in-skillfile  
Parent: STORY-261013-1azqs0  
Date: 2026-10-13, Asia/Tbilisi  
State: proposal-v1, ready for review; implementation is not claimed.

## Decision and recommended boundary

Add an operator-selected `mcp_servers` map to **Skillfile schema 3**. Compile its inert declarations into native agent configuration entries during install; reconcile only entries whose ownership was recorded by csk. A project invocation writes project surfaces; `csk global install` writes user surfaces. Never upgrade a project request into a user write when an agent lacks project support.

Installation is config materialization, not server execution, package-manager execution, connectivity testing, or authentication. It never requests, resolves, expands, prints, or stores new authentication values. Mixed native files may already contain foreign credential literals: the writer handles their existing bytes privately, without extracting or reporting them; this is not a guarantee that native files are secret-free. Authentication remains a separate human-operated native client flow or trusted environment setup. A future keychain broker is outside this design.

The first production slice is inline HTTP/stdio for project Claude Code, Codex CLI, and Cursor, including operator consent, protected ownership, merge, removal, dry-run, and drift. Later slices add reference acquisition, global scope and additional clients. This is one bounded design prerequisite, not a chain of research prerequisites.

| Research contract | Bound |
| --- | --- |
| Decision to unblock | Owner brief questions 1–9: declaration grammar and safe native config installation |
| Frozen precondition | proposal-v1 accepted subset and JSON vectors below; reviewer/owner acceptance freezes them for implementation |
| Worker-time budget | 60 minutes, including source verification and packaging |
| Artifact budget | Design under 100 KiB plus logbook under 10 KiB; no archives |
| Serial prerequisite budget | One research leaf; budget exhaustion or a proposed second prerequisite triggers re-scope toward implementation |
| Exit criteria | Nine questions walked; recommendations, source evidence, capability bounds, phases and owner questions recorded |
| Consuming slice | Real `csk install` → parser/planner → three native writers → ledger/removal; negative entry-point tests |

Artifact placement resolves two conflicting brief instructions: the run write boundary forbids direct writes outside its worktree. Scratch is authored under `.temp/TASK-261013-cnfbiu/`; `task-board resource add` alone writes the externally stored outcome. No product, README, real config, or control-root file is edited.

## Verified baseline and sources

Local csk evidence is at commit `0da153a54e7f8b446e63a6a177a9b5392e30da11`, the assigned Story checkout. This is a recorded checkpoint, not a claim that remote main was freshly synchronized. Curator was read using `git show origin/main:<path>`, without changing it: curator-spec `43bf0a2506d5c354a73bbc3ea4623d4653db10c7`; curator `876127f7c714e01092f43c8950dc879421c52461`. Vendor documentation was consulted on 2026-10-13; its tables are documentation evidence, not six-client runtime certification.

Current facts:

- Skill manifests support versions 1–8, with MCP requirements introduced at v5. Entries are keyed by name; `hint` is mandatory, `transport` optionally `stdio`/`http`, and `required_in` defaults to `any`, accepting `all`. Unknown requirement fields are rejected. [C1]
- `configured_servers` unions project/home names; the checker does not validate endpoint identity or requirement transport. `_check_mcp_servers` uses `any`/`all`, raises on missing requirements, and warns on unresolved stdio commands and project-only entries. Its call precedes the audit gate in the inspected install path. [C2, C3]
- Native paths are known for six agents; Windsurf has no project surface in the registry. OpenCode `enabled:false` and Claude `disabledMcpjsonServers` are filtered. Missing **and unreadable/malformed** configs both become an empty result. OpenCode `.jsonc` is parsed with `json.loads`, so comments/trailing commas do not work in that reader. These are observations, not proposed writer semantics. [C2]
- Skill mirroring uses `.csk-managed.json`, rejects unmanaged targets, and removes managed names absent from the desired set. Its ledger parser distinguishes absence from read failure but documents that an exact foreign ledger is indistinguishable from one csk wrote. A repository-supplied MCP ledger must therefore never authorize writes to native settings. [C4]
- Generated skill paths are gitignored individually. Project `remove` edits Skillfile and tells the operator to install; install cleans removed skill directories. GC collects runtime/cache references conservatively. These are the removal/reconciliation model to extend, rather than an existing MCP uninstall API. [C5]
- Skillfile schema is separate from skill-manifest schema: project versions 1/2 currently reject a top-level `mcp_servers`. Version 2 accepts legacy skill entries as well as selectors. Global loader explicitly rejects version 2 and requires version 1. New global schema support cannot be assumed. [C6]
- The project is Python >=3.11 and declares macOS, Linux and Windows support. An existing recoverable transaction engine exists; config inputs already participate in a filesystem-generation probe. Reuse needs a native-file target/CAS review, not a promise that dispatch's proposed writer has landed. [C7]

### Local code reference index

All paths below are relative to the recorded csk checkpoint unless qualified:

- **C1:** `src/csk/skillspec.py:25–26, 793–802, 856–888`; `docs/skill-authoring.md:188–213`.
- **C2:** `src/csk/mcp_configs.py:9–44, 51–62, 65–95, 98–176`.
- **C3:** `src/csk/installer.py:874–881, 3911–3967`.
- **C4:** `src/csk/adapters.py:38–39, 137–165, 425–445, 520–536`.
- **C5:** `src/csk/adapters.py:60–66`; `src/csk/cli.py:986–1003, 1008–1023`; `src/csk/installer.py:4602–4618`; `src/csk/gc.py:66–97, 124–179`.
- **C6:** `src/csk/manifest.py:19–21, 227–255, 289–351`; `src/csk/global_install.py:59–68, 306–318`; `src/csk/cli.py:817–827`.
- **C7:** `pyproject.toml:10–40`; `src/csk/transactions.py:181, 406–427, 512–631, 2023–2045`; `src/csk/installer.py:2460–2491`.
- **C8:** `src/csk/identifiers.py:10–25, 33–53`.

## 1. Declaration schema, references and requirement satisfaction

### Options

| Option | Benefits | Costs | Recommendation |
| --- | --- | --- | --- |
| Pass through per-client native JSON/TOML | Fast, unrestricted fields | Six divergent formats; credentials and auto-approval can enter through arbitrary fields | Reject |
| Closed, client-neutral declaration | Reviewable execution/endpoint intent; deterministic adapters | Deliberate unsupported capability errors | Adopt |
| Only references to definition packages | Reuse, Curator alignment | Acquisition and pinning required for the simplest case | Add after inline vertical slice |

Bump **Skillfile**, not `agent-skill.json`, to schema 3. Schema 1/2 keep their current meanings; no automatic migration on install. Project schema 3 inherits schema-2 `project`, `agents`, `locale`, `sources` and `skills` semantics, plus `mcp_servers`; MCP acquisition references are distinct from skill source selectors. Global schema 3 initially allows the existing legacy `skills` list, `agents`, `locale` and MCP declarations, but rejects `project`, nonempty `sources`, and `from` selectors until global selector support is deliberately implemented. This makes global MCP possible without silently broadening the separate source-selector feature. The global loader must explicitly accept this subset. [Baseline: C6]

Example (synthetic endpoint/package; illustrative versions, not a recommendation to install):

```json
{
  "schema_version": 3,
  "agents": ["claude_code", "codex_cli", "cursor"],
  "skills": [],
  "mcp_servers": {
    "docs": {
      "scope": "project",
      "server": {
        "transport": "http",
        "url": "https://mcp.example.invalid/mcp",
        "headers": {"Authorization": {"env": "DOCS_TOKEN", "prefix": "bearer"}}
      },
      "auth": {"kind": "env", "help_url": "https://example.invalid/account/tokens"}
    },
    "tools": {
      "agents": ["claude_code", "cursor"],
      "server": {
        "transport": "stdio",
        "command": "npx",
        "args": ["-y", "@example/mcp-tools@1.2.3"],
        "env_names": ["TOOLS_TOKEN"]
      },
      "auth": {"kind": "env"}
    }
  }
}
```

### Accepted grammar (proposal-v1)

Strict JSON: reject duplicate keys, unknown fields, booleans where integers are required, invalid Unicode/control characters, and non-string names. Names use the **intersection** of csk's portable identifier rule and clients' server identifiers: `[A-Za-z0-9][A-Za-z0-9_-]{0,127}`, excluding Windows reserved components and client-reserved names. csk currently allows dots, while Claude docs restrict server names to letters/digits/hyphens/underscores; a narrower new declaration grammar avoids inventing aliases or changing old requirements. [C8; A1, “Add a server from an mcpServers JSON block”]

| Field | Contract |
| --- | --- |
| `mcp_servers` | Optional object keyed by canonical server name; empty means desired managed set is empty |
| Declaration | Exactly one of `server` or `reference`; optional `agents`, `scope`, `auth`, `git_policy`; no native config escape hatch |
| `agents` | Omitted = resolved install target agents; nonempty unique explicit list must be a subset of those targets; unknown agent refused |
| `scope` | Optional assertion `project` or `user`, default from invocation; mismatch refused; project cannot assert user |
| `server.transport` | Exactly `stdio`, `http` (Streamable HTTP), or `sse`; first slice admits only stdio/http |
| stdio | Required bare `command`, optional `args` string array default `[]`, `env_names` unique names default `[]`; no `url`/headers |
| http/sse | Required literal HTTPS `url`; no userinfo, query, fragment, interpolation or command fields; optional `headers` |
| `headers` | Header-name map to `{ "env": "NAME", "prefix": "none" or "bearer" }`; prefix defaults none; bearer allowed only for Authorization. No literal header values |
| `auth` | Required `{kind: none|env|oauth, help_url?: HTTPS URL}`. No executable instructions or credentials. `env` requires at least one env reference; `none`/`oauth` require no env reference; oauth remote-only in proposal-v1 |
| `git_policy` | `local` default or `shared`; per-file policy must agree among all declarations targeting that file |
| env name | `[A-Za-z_][A-Za-z0-9_]*`, unique; exclude loader/interpreter/manager-control names and families (`PATH`, `HOME`, `LD_*`, `DYLD_*`, `NODE_*`, `NPM_CONFIG_*`, `PYTHON*`, `CSK_*`, agent config/trust override names) |

No raw `env` values, cwd, envFile, header helper, native `trust`, tool allowlist or approval-mode fields. Arguments are data, but can encode programs/secrets: reject token-like material through the source-audit gate, keep outputs sanitized, and show execution intent before writing. A secret detector is best effort, not a proof that arbitrary argument strings are secret-free. First slice denies explicit shell launchers (`sh`, `bash`, `zsh`, `cmd`, PowerShell) and dynamic evaluator recipes; it does not claim that any other approved binary is safe. Operator consent still covers arbitrary stdio execution at client startup.

### Inline vs reference

References resolve to **one normalized declaration**, never a native client config or another reference chain. Proposed package shape: strict `agent-mcp.json` schema 1, `name`, `version`, `server`; Curator-compatible base fields are `transport`, `command`, `args`, `env_names`, `environments`. csk headers/auth extensions require a separate package schema 2, not reinterpretation of Curator schema 1. Skillfile retains final `agents`, `scope`, `auth`, `git_policy`; no arbitrary overrides to the imported command/url. For schema-1 packages, `environments` must cover all selected agents or installation refuses.

```json
{
  "mcp_servers": {
    "docs": {
      "reference": {
        "kind": "git",
        "git": "https://github.com/example/mcp-definitions.git",
        "revision": "1111111111111111111111111111111111111111",
        "file": "servers/docs/agent-mcp.json",
        "sha256": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "auth": {"kind": "none"}
    }
  }
}
```

The synthetic digest intentionally is not a valid pin for an existing artifact. Reference variants:

- `git`: exact full commit OID, portable repository-relative regular `file`, SHA-256 of raw committed file bytes. No branches/ranges/tags in install declarations. Acquire raw objects without executing filters/hooks; reuse csk's established admitted source path. Package name must equal map key.
- `file`: portable relative file under the operator project/global specification root, mandatory raw-byte SHA-256, refuse symlinks/reparse points and escapes. Edited bytes require digest update and fresh consent. This is an intentional deviation from Curator's git-only declaration packages.
- `url`: HTTPS config-document URL plus mandatory SHA-256; HTTPS endpoint URL and declaration-document URL are different types. Bound at 1 MiB/one request/30s, no redirects, credentials, cookies or ambient proxy credentials; refuse private/loopback/link-local destinations including DNS rebinding. No auth-required downloads in this phase. Prefer immutable publisher URLs; even a mutable URL is admitted only if pinned bytes match.

Lock acquisition identity and normalized definition digest with source/file/revision, record integrity algorithm/version, and distinguish network/read/parse failure from absence. Offline install reuses only verified pinned cached bytes; missing cache fails. Install never refreshes references; explicit update changes a pin and requires new consent. SHA-256 provides byte integrity, not publisher identity or authorization. Optional source-signature verification uses the manager's existing operator policy. Recommendation: inline first, git/file second, URL last because it adds a separate network threat surface.

### Skill requirement interaction

Keep requirements independent from provisioning. Skills can require a server and supply a hint without defining it. Do not auto-install a definition simply because a requirement has that name.

`csk install` resolves/audits definitions, constructs an **effective post-write config view**, then runs the pure requirement verifier on that view before any write. A newly planned entry can satisfy a requirement; a declaration merely present in Skillfile cannot. Scope/agent filters, enabled/rejected state, conflicts and write feasibility participate in the result. Then publish config and skills in one recoverable transaction. On failure, neither is reported installed.

Maintain `required_in:any/all` over the skill's actual resolved target agents. Unselected/unsupported clients remain missing for `all`; `any` still needs one target. Do not change the historical meaning into “authenticated/connected.” Report separate dimensions: configured, approval unknown/pending/rejected, executable resolvable/unresolved, authentication not checked. Never infer connected from a successful write. For new typed verification, reject a known transport mismatch; `http` requirements may accept Streamable HTTP and legacy SSE remote entries, while unrecognized shapes are unknown, not satisfied. Preserve v1–v8 requirement grammar and explicitly document this checker tightening. Existing external entries remain usable without csk ownership, but malformed reads must return diagnostic failure, not an empty success path. [Current semantics: C1–C3]

## 2. Who can declare and authorize

| Option | Tradeoff | Decision |
| --- | --- | --- |
| Only root operator Skillfile | Simple trust and explicit intent; repetitive definitions | First slice |
| Skill-shipped recommendations, explicit root reference | Reusable but adds pin/source review | Later; import only the explicitly named pinned file |
| Transitive auto-provision | Convenience grants execution authority to dependency closure | Reject |

A repository file is attacker-controlled until the operator chooses to trust its MCP plan. Writing a native entry can trigger an already-running client, so **consent comes before config publication**, not just before the next launch. Store consent in protected manager-home state outside any checkout, bound to canonical project identity, scope, server name, selected agents, normalized argv/url/env names, reference digest and writer capability/version. New bytes, wider agent set, changed scope or changed native interpretation require renewed consent.

Recommended non-programmer path: first interactive `csk install` presents a concise plan and obtains operator selection in that same command; subsequent installs of an unchanged plan need no prompt. Headless/agent install accepts only a preapproved plan from operator-owned policy; an unapproved plan returns a precise refusal and human instructions. A Skillfile boolean, committed approval file, `--yes`, or project-local ledger cannot approve itself. This trust step is separate from authentication and client workspace approval. The runtime cannot distinguish a malicious same-user process from the operator; that is outside the declared threat model, not solved by a magic “human-only” CLI flag.

## 3. Per-agent writers and evidence

Every shape below is an **entry under the named key**, not a replacement for the whole config. `T` denotes an env-variable name, never its value. Static hints and native permission state stay outside generated entries. Where documentation lacks a guarantee, the table states the bound; no general claim that all clients hold project servers pending is made.

| Agent | Project / user file and key | Exact generated entry shapes | Trust/approval and evidence |
| --- | --- | --- | --- |
| Claude Code | `.mcp.json` / `~/.claude.json`; `mcpServers.NAME` | stdio: `{"type":"stdio","command":"npx","args":["-y","@example/tools@1.2.3"],"env":{"T":"${T}"}}`; HTTP: `{"type":"http","url":"https://example.invalid/mcp","headers":{"Authorization":"Bearer ${T}"}}`; SSE changes type to `sse` | Project workspace/server approvals remain native; never write `enableAllProjectMcpServers`, enabled lists or permission rules. User entry merges at top-level, never into `projects`. A1: scopes, JSON configuration, variable expansion, project approvals. |
| Codex CLI | `.codex/config.toml` / `~/.codex/config.toml` (effective CODEX_HOME honored only from operator context); `mcp_servers.NAME` | stdio TOML: `command="npx"`, `args=["-y","@example/tools@1.2.3"]`, `env_vars=["T"]`; HTTP: `url="https://example.invalid/mcp"`, `bearer_token_env_var="T"`; custom raw header: `[mcp_servers.NAME.env_http_headers]` with `X-Key="T"` | Project config trusted-project-only; no trust or approval edits. Direct SSE not documented, refuse. A2: Configure with config.toml. Native parser/list verified locally on 0.162.1; not server launch or env delivery. |
| Cursor | `.cursor/mcp.json` / `~/.cursor/mcp.json`; `mcpServers.NAME` | stdio: `{"type":"stdio","command":"npx","args":["-y","@example/tools@1.2.3"],"env":{"T":"${env:T}"}}`; HTTP/SSE: `{"url":"https://example.invalid/mcp","headers":{"Authorization":"Bearer ${env:T}"}}` | Native URL entry covers both remote transports; exact forced-transport selection not documented. csk SSE writer remains unsupported until tested. Tool calls prompt by default, modified by Run Mode/admin policy; that is not a proven server-start gate. Never alter permission/auto-run config. A3. |
| Gemini CLI | `.gemini/settings.json` / `~/.gemini/settings.json`; `mcpServers.NAME` | stdio: `{"command":"uvx","args":["example-tools==1.2.3"],"env":{"T":"${T}"},"trust":false}`; HTTP: `{"httpUrl":"https://example.invalid/mcp","headers":{"Authorization":"Bearer ${T}"},"trust":false}`; SSE uses `url` | Untrusted safe mode ignores workspace settings and does not connect MCP; `trust:true` bypasses tool confirmation, so never emit it. A4: properties; A5: Settings files/global string expansion; A6: untrusted workspace. |
| OpenCode | `opencode.json` or `.jsonc` / `~/.config/opencode/opencode.json` or `.jsonc`; `mcp.NAME` | stdio: `{"type":"local","command":["uvx","example-tools==1.2.3"],"environment":{"T":"{env:T}"}}`; HTTP: `{"type":"remote","url":"https://example.invalid/mcp","headers":{"Authorization":"Bearer {env:T}"},"oauth":false}` for env auth; omit oauth for native OAuth | No workspace/server-start approval guarantee established; most tool permissions default allow. Do not add permission allow rules. Native transport is remote; force-SSE mapping unverified. Existing `enabled:false` counts disabled and must not be silently reversed. A7–A9. |
| Windsurf/Cascade compatibility | csk reader: user `~/.codeium/windsurf/mcp_config.json`, no project; current redirected vendor docs: macOS/Linux `$XDG_CONFIG_HOME/devin/mcp_config.json` or `~/.config/devin/mcp_config.json`; Windows `%APPDATA%/devin/mcp_config.json`; `mcpServers.NAME` | Current documented stdio: `{"command":"npx","args":["-y","@example/tools@1.2.3"],"env":{"T":"${env:T}"}}`; HTTP: `{"serverUrl":"https://example.invalid/mcp","headers":{"Authorization":"Bearer ${env:T}"}}` | Legacy path is verified only as csk's reader path, **not** a current vendor/runtime guarantee. Current docs cover Devin, toggles and admin allowlists, not a project approval gate. No local Windsurf installation found in `/Applications`. Keep legacy writer disabled until release/profile verified; add separate Devin profile rather than silently migrate. A10; C2. |

For header `{env:T,prefix:none}`, all clients except Codex use their interpolation token without `Bearer `; Codex uses `env_http_headers`. Codex uses `bearer_token_env_var` only for Authorization/bearer. stdio `env_names` maps name-to-same-name references; Codex forwards names with `env_vars`. csk does not expand any token. Native inheritance can expose more environment than the declared list; this design does **not** promise Curator's process environment allowlist confinement. That would require a trusted launch broker, outside the native config writer slice.

### Official documentation index (section citations)

- **A1:** [Claude MCP](https://code.claude.com/docs/en/mcp): “Option 1: Add a remote HTTP server”, “Option 2: Add a remote SSE server”, “Option 3: Add a local stdio server”, “Add MCP servers from JSON configuration”, “MCP installation scopes”, “Environment variable expansion in .mcp.json”, “Project server approvals and workspace trust”, “Authenticate with remote MCP servers”.
- **A2:** [Codex MCP](https://developers.openai.com/codex/mcp) (redirects to ChatGPT Learn): “Supported MCP features”, “Connect Codex to an MCP server”, “Configure with config.toml”, “Other CLI commands”.
- **A3:** [Cursor MCP](https://cursor.com/docs/mcp): “Using mcp.json”, “STDIO server configuration”, “Configuration locations”, “Config interpolation”, “Authentication”, “Tool approval”, “Run Mode”, “MCP Allowlist”.
- **A4:** [Gemini MCP](https://geminicli.com/docs/tools/mcp-server/): “Configuration structure”, “Configuration properties”, “Environment variable expansion”, “Managing OAuth authentication”.
- **A5:** [Gemini configuration](https://geminicli.com/docs/reference/configuration/): “Settings files”, including “Note on environment variables in settings”.
- **A6:** [Gemini trusted folders](https://geminicli.com/docs/cli/trusted-folders/): “Why trust matters: The impact of an untrusted workspace”, “Headless and automated environments”.
- **A7:** [OpenCode MCP](https://opencode.ai/docs/mcp-servers/): “Local”, “Remote”, “OAuth”, “Authenticating”, “Disabling OAuth”.
- **A8:** [OpenCode config](https://opencode.ai/docs/config/): “Format”, “Precedence order”, “Global”, “Per project”, “Variables / Env vars”.
- **A9:** [OpenCode permissions](https://opencode.ai/docs/permissions/): “Actions”, “Defaults”.
- **A10:** [Windsurf MCP URL](https://docs.windsurf.com/windsurf/cascade/mcp), now [Devin Desktop/Cascade MCP](https://docs.devin.ai/desktop/cascade/mcp): “mcp_config.json”, “Remote HTTP MCPs”, “Config Interpolation”, “Admin Controls”, “Enabling/Disabling Tools”. This redirect/path discrepancy is a capability bound, not evidence that legacy Windsurf uses the new path.

### Format preservation and file selection

Writers use concrete syntax trees or lossless token/span edits for JSON/JSONC, and a TOML-preserving editor such as `tomlkit` after dependency review. `json.loads` + `json.dumps` and `tomllib` + reserialization are insufficient. Reject ambiguous duplicate keys/tables, malformed or undecodable bytes and unsupported syntax **before** touching disk. Preserve comments, sibling values, unknown native keys, key order, indentation, newline style and BOM if supported. An unsupported BOM/encoding is refused, not rewritten. Updating one owned server may rewrite that server's syntax span; bytes outside edited spans remain identical. Comments attached to removed entries are surfaced in dry-run; never remove a neighboring comment by heuristic.

OpenCode: choose the one existing valid supported file; if both JSON and JSONC exist, refuse ambiguous selection unless an operator-owned adapter profile explicitly selects one. Missing files create registry-default JSON. Never create a second config to bypass a failed read. JSON clients use strict JSON unless the native release is explicitly certified for JSONC; if comments exist on an uncertified surface, refuse rather than strip them. TOML quoted/dotted keys are resolved by AST paths, not regex. User home/config overrides are resolved from operator context once, displayed, and recorded; repository data cannot select arbitrary destination paths.

## 4. Ownership, merge, removal and atomicity

### Options and recommendation

Whole-file ownership is safe only for an isolated managed home (Curator's model). Native user files contain unrelated settings and often credential material; replacing or backing them up indiscriminately is unacceptable. Use **per-entry ownership** plus byte-preserving merge. Never treat `.csk-managed.json` beside a repository config as authority. [Baseline C4; comparison R2]

Authoritative ledger: `<csk-home>/state/mcp/<consumer-id>.json`, user-owned, private permissions/DACL, regular file, no symlink/reparse traversal, manager home outside any repository. Consumer id is csk-generated from canonical project identity and scope, not a caller path. Registry-selected destination paths only. Fields: schema version; consumer identity/scope; agent capability version; declaration/source digest; exact AST key; normalized last-written entry SHA-256; ownership state; transaction id; whether file/container was created; policy and approved-plan digest. No resolved secrets. A project witness, if emitted, is inert and must not authorize writes. Same-user ledger forgery remains outside the model.

Rules:

1. Absent target entry: add after complete preflight and consent.
2. Existing entry without authoritative ownership: conflict, even if bytes match. Do not “claim” a user's entry through equality. Requirements may still use it as external configuration when no provision request conflicts.
3. Owned entry equal to last-written normalized value: replace/reconcile; unrelated file edits are retained after fresh parse.
4. Owned entry changed, disabled, or deleted by the user: drift. `install` refuses destructive repair, reports the field path and offers explicit human resolution. No automatic re-enable or recreation of intentional deletion. First-slice repair is manual, followed by relinquishing ownership/re-adopting with reviewed policy.
5. Missing/unreadable/forged ledger: ownership unknown. Preserve config, refuse writes/removal; never reconstruct authority from project markers or config contents.
6. Conflicts at other discovered scopes/overrides: report effective-precedence/shadowing uncertainty; never claim success based solely on unioned names. A different same-name definition at a higher-precedence supported surface blocks managed satisfaction. Dynamic/admin/plugin surfaces not inspected are named as blind spots.

Recommendation: no generic `--takeover` in slice 1. A later operator-only `adopt` can bind an exact displayed entry digest and preserve an encrypted/private recovery record if needed. Replacement takeover broadens scope and is a separate decision; it must not let an agent steal ownership or erase disabled state.

Lifecycle:

- Removing a skill does not remove a root MCP declaration used by another skill or declared intentionally. Removing a declaration then installing removes its **unchanged owned** entries for previously selected agents, including agents removed from the selection. csk does not delete external same-name entries.
- Whole-consumer uninstall (new explicit API if added) reconciles owned entries to an empty set with the same drift guard. Currently the project uses remove + install, not a demonstrated MCP uninstall command. [C5]
- Remove an empty wrapper table/file only when csk created it and it contains no foreign fields/comments. Otherwise keep it. Never invoke native `mcp remove`: it may alter native OAuth state; removal owns configuration only.
- GC deletes unreferenced acquisition/cache/journal artifacts after the existing grace/uncertainty discipline; it does not scan arbitrary home files or treat an unreachable project as authorization to delete active user settings. Explicit consumer unregister/uninstall handles native entry cleanup. Uncertain registry/ledger retains state. [Pattern: C5]
- `status --check`: read-only comparison of desired definitions, protected ledger, native semantic entries, reference pins, supported capability versions and known disabled/rejected state. Exit 1 on missing/drift/unknown read/capability, 0 only for current static installation; auth/connectivity explicitly “not checked.” Formatting-only changes are not semantic drift; ownership paths and consent changes are.
- `install --dry-run`: all reads, schema/capability/conflict/audit checks and sanitized plan, no writes, no consent creation, no cache acquisition unless separately allowed as a read-only already-cached plan. Uncached references report “resolution required,” never a fake successful plan. First slice has no such network dependency.

### Transaction contract

Plan every agent config patch and skill publication before mutation; requirement checking consumes planned effective state. Acquire manager-home mutation lock plus ordered target locks, snapshot exact input digests/stat identity, stage patched bytes adjacent to each target, flush/fsync as supported, recheck CAS before rename, publish config targets and authoritative ledger through a recoverable journal. A single rename is atomic for one file; a cross-file batch is recoverable, **not** globally atomic to observing clients. Interrupted status is non-current until recovery completes; rollback refuses to overwrite a concurrent external edit.

Do not persist full unredacted user-config snapshots in logs or journals: `~/.claude.json` can contain other client state. Whole-file staging/backups needed for atomic replacement stay private adjacent to their target, mode/DACL preserved, never enter csk caches or board artifacts, and are removed after recoverable commit. Ledger/journal stores digests, paths and csk-generated entry data only. Never log diff bodies containing foreign data. File size limit 4 MiB and bounded read growth; outside-limit files refuse.

Reuse existing transaction target/CAS machinery after verifying these properties. If the dispatch atomic writer is integrated by implementation time, reuse its safe byte-writer primitive; do not make a second research task or imitate an unlanded interface. Acceptance includes process-kill recovery and client-write collision tests, not only tempfile happy paths. [Existing machinery: C7]

## 5. Secrets, authentication and non-programmer UX

| Declared auth class | What install writes | Next human action |
| --- | --- | --- |
| `none` | Endpoint/argv only | Review native workspace/server trust prompts if any |
| `env` | Variable names/references only | Use trusted personal environment/credential setup outside agent conversation; launch client with those variables |
| `oauth` | Remote endpoint and supported native OAuth metadata only; no client secret | Open native client and perform its OAuth flow personally |

Native guidance: Claude `/mcp` Authenticate; Codex `codex mcp login NAME`; Cursor native server authentication UI; Gemini `/mcp auth NAME`; OpenCode `opencode mcp auth NAME`; Windsurf/Devin native setup UI only after selecting a verified release profile. These are displayed instructions, never commands executed by csk or an agent. [A1–A4, A7, A10]

Install output lists each name, selected agents/scope, destination, transport, argv or endpoint origin, env names, auth class, ownership action and approval state. Source-supplied help URLs are escaped HTTPS links marked as publisher guidance; no executable hint text is trusted. The CLI never prints a token placeholder as a request to paste a value into the chat. It does not read `.env`, keychain, separate credential stores, browser state or OAuth caches, and does not evaluate token-bearing header references. Existing native config bytes may contain foreign credentials and are handled only through the private file-preservation path in §4; never return their contents to the agent or attach them as evidence. It does not test the endpoint: even “health check” can authenticate or send sensitive data.

Successful output should say: “Configuration installed. Authentication not checked. In your client, review the server and sign in.” GUI-launched clients may not inherit a terminal environment; env auth is therefore not universally zero-setup. Prefer OAuth for non-programmers where the native client/server pair supports it. A broker would improve env-token setup but is not smuggled into this feature. Missing required env variables are diagnosed by the client/trusted auth operation; installer does not evaluate secret values or infer token presence from the metadata-only Codex list result.

## 6. Git policy

| Policy | Source of truth | Generated surfaces | Tradeoff |
| --- | --- | --- | --- |
| `local` (default) | Committed Skillfile and pins | Newly created native files ignored with exact file patterns; protected ledger never committed | Portable specification, less team noise; native config not preinstalled for people who skip csk |
| `shared` (explicit) | Skillfile plus reproducible generated public entries | Team chooses to commit `.mcp.json` / `.cursor/mcp.json`; other mixed settings only after review | Native tooling works after clone; generated/server trust still required; dual-file drift must be visible |

Do not ignore whole `.claude`, `.codex`, `.cursor`, `.gemini`, or OpenCode files blindly; existing tracked configs remain tracked. For a tracked config, patch only owned entries and report the reviewable delta; `local` cannot make a tracked file private. If the requested policy conflicts with an existing tracked/shared file, refuse with the precise conflict rather than changing repository policy automatically. Gitignore changes use the established explicit repair lane; dry-run changes none. User-scope files are never repository artifacts. [Current skill-ignore pattern C5; Claude project sharing A1]

For `shared`, generated entries contain only public literals and env references, no absolute machine paths. The manager ledger is machine-local: another clone must perform its own exact-digest adoption/consent; committed native entries alone do not confer ownership. In slice 1, a fresh clone with preexisting shared entries therefore conflicts with a provision request; use those entries as external requirements or defer shared adoption to the later exact-digest adopt feature. This is an explicit sharing limitation. Recommendation: default local generation, allow explicit shared `.mcp.json` and Cursor config; mixed TOML/settings files require all declarations targeting the file to agree and byte-preserving edits. Do not auto-stage generated config changes.

## 7. Windows, paths and stdio resolution

Use the project's Python/pytest stack on its declared macOS/Linux/Windows platforms; no iOS build applies. [C7]

Canonical command is a bare executable name, argv is a string array, never a shell command string. No `~`, `$VAR`, `%VAR%`, relative checkout executable, `cwd`, or host-specific absolute paths in portable declarations. Later typed project-root argument placeholders need per-agent verified support; they are excluded from the first grammar. Config destinations use native Path/home handling selected by operator context. Static command resolution does not launch anything and is not proof of runtime identity: PATH changes between install and client launch can select a different binary.

`npx` recipes must name an exact package version (`@example/tools@1.2.3`), never unversioned/latest/range; `uvx` recipes must bind an exact distribution/version (`example-tools==1.2.3` or exact pinned `--from`). Arbitrary recipes not recognized by the closed parser are refused rather than guessed. Exact top-level package versions do **not** pin every transitive dependency or downloaded executable; an immutable server executable/container digest is stronger. Installation does not run npm/uv or download their execution dependencies; the agent may later do so when starting the server, covered by the reviewed execution plan.

Windows `.cmd`/`.bat` need a native client compatibility lane. Do not universally rewrite `npx` into `cmd /c`: shell interpretation changes security semantics. First slice supports HTTP and stdio resolving to native executable images on Windows, and refuses batch-launch requirements with `mcp_windows_batch_unsupported`. The next Windows lane may generate a registry-owned `cmd.exe /d /s /c` invocation only for a narrow pinned npx recipe, with fixed executable path, native quoting, rejection of shell metacharacters/expansions, and real client tests for spaces/quotes/Unicode and injection vectors. The generated wrapper participates in the approved digest. Prefer a native `uvx.exe`/binary where available. This is a declared support limit, not a claim that quoting has already been implemented or certified.

Missing command remains a warning for external checked requirements. For new materialization, show unresolved command and actionable installation guidance; do not install tooling or claim runnable. If runnable is a required operator policy, refuse statically before publication. Package pinning/integrity of the **definition** and pinning of server **runtime acquisition** are distinct.

## 8. Threat model and reference-manager alignment

### Threat model (dispatch style)

Model anchor: the csk dispatch threat model (local to the cocoaskills repository), “Threat model (binding for reviews from rev 5 on)”, read during this run.

**Attacker:** repository contents the operator registers/enters, including Skillfile, pinned reference definitions from hostile publishers, local config entries/markers and symlinks. The attacker cannot modify manager-home state or trusted tools outside the checkout. Network fetch peers are untrusted input providers.  
**Trusted:** operator account and explicit policy/consent, protected manager home and ancestors outside checkout, csk runtime, approved system tools and native client implementation.  
**Outside this model:** malicious same-user processes or races modifying protected manager-home ancestors/registry, compromised native client/toolchain, operator knowingly approving malicious execution. Status digest checks detect some drift but do not establish sandboxing.

Today csk's MCP path reads configuration and probes PATH, without provisioning/launching servers. The proposed path newly lets an approved declaration modify files that clients may consume immediately and start arbitrary stdio code or send data to a remote endpoint. This is the material authority increase; tool-call confirmation is not sufficient protection against process startup. [C2–C3]

| Attack | Required boundary | Refusal/negative evidence for implementation |
| --- | --- | --- |
| Skill dependency auto-installs malicious server | Root-only explicit declaration and consent | Requirement/recommended definition without root selection writes nothing |
| Repo claims its own approval/ownership | Protected operator state outside checkout | Forged project ledger/approval never permits write/removal |
| Project declaration writes global settings | Invocation-bound scope and registry destinations | `scope:user` from project refused before any target write |
| Existing symlink/reparse config redirects into home | No-follow path validation and admitted target roots | Final/parent link escape rejected; safe missing file remains distinct |
| Pinned config URL becomes attacker content | Raw-byte digest plus fixed acquisition policy | One-byte mismatch, redirect/private target/read error all fail closed |
| Header/env/argv exposes secret | Env-reference-only fields, audit, sanitized rendering | Literal secret/header, reserved env name, control chars rejected; no token read or output |
| Auto-approval through arbitrary native fields | Closed grammar and writer whitelist | `trust:true`, enabled approval lists, headers helpers refused |
| Same-name user entry overwritten | Per-entry protected ledger, exact previous digest | Identical foreign entry and drifted owned entry refused |
| Failed read treated as absent | Typed absent/read-failed/malformed states | Permission/parse failure never creates/replaces a config |
| Concurrent client write lost | Input CAS and recoverable journal | Change between plan and rename refuses; rollback preserves external edit |
| Shell/batch injection | Bare argv, closed recipe and Windows limit | `&`, `%`, newlines, quote/space boundary vectors in any future shell lane |
| False claim of confinement | Honest capability status | Tests/report never equate env names or written config with isolated runtime/auth readiness |

Protection ratio for this research: **12/12 threat rows specified, 0/12 production gates implemented or tested**. First slice owns rows relevant to inline materialization; URL and batch rows remain deferred refusals. This is design coverage, not measured implementation coverage.

### Curator comparison (read-only, pinned sources)

**R1:** curator-spec `protocol/environments.md:479–560` (§2.2), `562–597` (§2.3); `profiles/manager.md:1075–1099` (§6).  
**R2:** curator-spec `protocol/environments.md:1110–1141` (§5.8), `1826–1866` (§7.8).  
**R3:** curator `internal/mcp/mcp.go:1–42, 128–157, 245–283`; `internal/envprofile/envprofile.go:740–742, 875–891, 1797–1809`; `internal/envprofile/surfacing.go:24–53`.  
**R4:** curator `internal/contextpkg/contextpkg.go:434–539`; `internal/contextmaterialize/mcp.go:21–127, 152–177`; `internal/envprofile/managed.go:204–224, 300–355, 2881–2904`. Sources are the origin/main OIDs recorded above, not mutable working-tree files.

| Topic | Curator contract / observed implementation | csk alignment or deliberate deviation |
| --- | --- | --- |
| Requirements | §6 read-only checker; any/all; missing command and project-only warnings; `internal/mcp` implements it | Keep verification pure; provisioning separate. Tighten parse errors and typed/effective resolution for writer safety; do not copy blanket trust warning |
| Declaration | §2.2 `agent-mcp.json`, name/version, stdio/http, env names, environments; bare command, restricted HTTPS; git-only; source allowlist | Adopt base fields and inert definitions; explicit root selection stricter than transitive profile closure. Permit pinned operator-local file/URL later, with stated additional boundaries |
| Surfacing | §2.3 print every declaration before lock publication; envprofile emits after audit, before publishing | Adopt pre-write execution/endpoint/env-name visibility; add actual protected operator consent because native configs may auto-start |
| Secret values | §5.8 no env values in materialized file; launch fragment env-name union, bounded launch passthrough | Values still excluded; native client references instead of fragment delivery. csk does not claim Curator launcher env confinement |
| Ownership | §5.8 inert hashed marker-recorded files in managed homes only, never native in-place homes | Owner request deliberately needs native merge. Per-entry ledger/CAS replaces whole-file ownership; do not overwrite Curator channel files or seed homes |
| Claude launch | §7.8 `--mcp-config` + `--strict-mcp-config`, exact profile set | Native `.mcp.json` augments the user's environment; no strict-set guarantee or flags introduced |
| Codex launch | §7.8 `-p curator-mcp` layer, 0.153.2 evidence; missing layer ignored so launcher stats it | Native `.codex/config.toml`; no dependency on that custom profile channel; current local 0.162.1 probe covers entry parsing only |
| OpenCode launch | §7.8 `OPENCODE_CONFIG`, documented merge residual: project can override | Respect native merge and expose shadowing; no exclusive-profile claim |

Curator package parser and materialization were read in addition to the requested `internal/mcp`/`internal/envprofile`, because those implement requirements, admission and surfacing rather than all server serialization. No Curator runtime was rerun. Its “verified” launch facts are **accepted as recorded specification evidence**, not represented as this worker's executions. Sharing source-definition schema and refusal fixtures is useful; sharing byte writers blindly is not, because Curator owns isolated whole files and csk must preserve mixed native state.

## 9. Phased implementation slices and acceptance

| Slice | Scope | Acceptance criteria at real entry points |
| --- | --- | --- |
| 1 — inline project vertical | Skillfile v3 project subset; stdio/http; Claude/Codex/Cursor; static auth classes; consent, protected ledger, lossless merge, removal, dry-run/status | `csk install` writes native entries and skill requirement succeeds in planned view; repeat is idempotent; decl/agent removal deletes only unchanged owned entries; conflict/drift/malformed/CAS/link/forged consent fail with no target mutation; no server/auth launched; comment preservation and crash recovery; Windows HTTP/native-exe stdio accepted, batch refused |
| 2 — pinned definitions | git/file references and lock/cache; opt-in skill recommendations | Real install verifies committed raw bytes/name/digest before writer; digest mismatch/read failure/path escape/transitive-only recommendation fail; offline pinned reuse works; update reconsents; no new prerequisite research chain |
| 3 — global vertical | Global schema-3 bounded loader; same three user writers and ledger | `csk global install` writes only effective operator-selected user surfaces, preserving unrelated/private fields; project cannot reach them; user removal and drift guards; no global selector expansion by accident; no credentials in journals/logs |
| 4 — additional agents | Gemini, OpenCode; version-selected Windsurf/Devin after path verification; explicit SSE capability support | Native release probes in isolated homes on supported OS; JSONC comments/trailing commas preserved; disabled remains disabled; auth/trust settings untouched; unknown capability/version refuses; legacy/new Windsurf paths never guessed or auto-migrated |
| 5 — network and Windows extensions | HTTPS definition URL acquisition; narrowly certified batch recipe if needed | SSRF/redirect/digest/size/read-growth negatives; native Windows process/argv injection vectors and actual client startup with benign fixture server; no install-time auth/download execution; recipe/runtime pin limitations surfaced |

Slice 1 can start from this proposal without waiting for slices 2–5. Implementers keep deferred fields recognized only to return precise unsupported capability errors; they must not silently ignore them. Acceptance uses Python/pytest for host behavior and isolated benign native-client probes for adapter conformance. No tests mutate real user profiles.

### Frozen initial machine-readable vectors

These are valid JSON test inputs/expected outcomes for the slice-1 declaration admission contract, not a claim that production implements it. Tests consume `name`, `declaration`, install targets, invocation scope and policy state directly; unspecified policy is unapproved. Transport/audit/ownership negatives use named fixtures in the matrix after this block.

```json
{
  "contract": "csk-skillfile-mcp-proposal-v1",
  "invocation_scope": "project",
  "targets": ["claude_code", "codex_cli", "cursor"],
  "vectors": [
    {"id":"V01","name":"docs","declaration":{"server":{"transport":"http","url":"https://example.invalid/mcp"},"auth":{"kind":"none"}},"policy":"approved-exact-plan","expect":"admit"},
    {"id":"V02","name":"tools","declaration":{"server":{"transport":"stdio","command":"uvx","args":["example-tools==1.2.3"],"env_names":["TOOLS_TOKEN"]},"auth":{"kind":"env"}},"policy":"approved-exact-plan","expect":"admit"},
    {"id":"V03","name":"docs","declaration":{"server":{"transport":"http","url":"https://example.invalid/mcp"},"auth":{"kind":"none"}},"expect":"mcp_plan_unapproved"},
    {"id":"V04","name":"docs","declaration":{"scope":"user","server":{"transport":"http","url":"https://example.invalid/mcp"},"auth":{"kind":"none"}},"expect":"mcp_scope_mismatch"},
    {"id":"V05","name":"docs","declaration":{"agents":["windsurf"],"server":{"transport":"http","url":"https://example.invalid/mcp"},"auth":{"kind":"none"}},"expect":"mcp_agent_selection_invalid"},
    {"id":"V06","name":"docs","declaration":{"server":{"transport":"http","url":"https://example.invalid/mcp","headers":{"Authorization":"literal-token"}},"auth":{"kind":"env"}},"expect":"mcp_declaration_invalid"},
    {"id":"V07","name":"tools","declaration":{"server":{"transport":"stdio","command":"uvx","args":["example-tools==1.2.3"],"env_names":["PATH"]},"auth":{"kind":"env"}},"expect":"mcp_env_name_reserved"},
    {"id":"V08","name":"tools","declaration":{"server":{"transport":"stdio","command":"./tools/server","args":[]},"auth":{"kind":"none"}},"expect":"mcp_command_invalid"},
    {"id":"V09","name":"docs","declaration":{"server":{"transport":"http","url":"https://example.invalid/mcp","trust":true},"auth":{"kind":"none"}},"expect":"mcp_declaration_invalid"},
    {"id":"V10","name":"docs","declaration":{"server":{"transport":"http","url":"https://user:password@example.invalid/mcp"},"auth":{"kind":"none"}},"expect":"mcp_url_invalid"},
    {"id":"V11","name":"docs","declaration":{"server":{"transport":"sse","url":"https://example.invalid/sse"},"auth":{"kind":"none"}},"expect":"mcp_capability_unsupported"},
    {"id":"V12","name":"tools","declaration":{"server":{"transport":"stdio","command":"npx","args":["-y","@example/tools@latest"]},"auth":{"kind":"none"}},"expect":"mcp_runtime_pin_required"}
  ]
}
```

Validation order: syntax/type/closed fields → scope/name/env/url/recipe rules → agent selection → capability → source/audit → ownership/transaction feasibility → exact-plan consent → pure requirement check → publication. This fixes precedence when a vector could fail multiple gates.

Additional acceptance fixtures (implementation must report measured killed-mutant ratios, never just “covered”):

| Fixture family | Must distinguish | Narrowing mutation |
| --- | --- | --- |
| Requirements | any one target vs all targets; declaration vs planned valid entry; rejected vs pending; typed mismatch vs unknown | Only check selected capable clients for all, or count map key without successful plan |
| Ownership | foreign equal entry vs genuinely owned entry; project forged ledger vs protected ledger; edited disabled entry vs unchanged | Trust any parsed ledger or equality; ignore one edited native field |
| Read/format | absent vs inaccessible/malformed; JSONC comments vs string containing `//`; quoted TOML keys vs duplicate semantic tables | Convert one error class to absence; remove one duplicate check |
| Atomicity | unrelated edit preserved; input changed before rename; interruption before/after each journal step | CAS compares only owned subtree, allowing foreign edit loss |
| Secrets/auth | names vs values; literal header/control characters/reserved variables; guidance vs executing auth | Admit one header string or one reserved variable family; invoke health/auth command |
| Scope/trust | project vs user, narrower vs widened agent plan, changed digest vs stale consent | Omit one destination/agent/digest component of consent identity |

## Evidence and review walk

Run-owned checks:

| Command/check | Result | Limit |
| --- | --- | --- |
| `codex --version` | Exit 0; 0.162.1 | Readiness only |
| `CODEX_HOME="$PWD/codex-home" codex mcp list --json` in throwaway probe | Exit 0; two configured entries, env names and header-name map parsed | Native config grammar only; auth_status is metadata, no token present/used and no connectivity certification |
| Duplicate-table native Codex config: same isolated list command with `codex-invalid-home` | Exit **1**; expected failure, duplicate key rejected before config loading | Negative parser probe, not an implementation gate |
| Official documentation reads for six clients | Source sections A1–A10 inspected | Docs-confidence; legacy Windsurf path/runtime discrepancy retained |
| Pinned Curator `git show` reads | Exit 0 for requested spec and implementation files | No Curator launch-channel tests rerun |
| Artifact JSON/TOML/citation/section verification | Initial exit **1**, citation end line exceeded file by one; corrected to 4618; rerun exit **0** (design-verify-02.log) | Structural self-check, not product implementation tests |

No existing test suite is accepted as validation of this feature; it has not been implemented. No product build was needed for a read-only design. Source-discovery misses (`src/csk/skillfile.py`, `spec.py`, `global_scope.py` and absent local skill directories) were corrected to actual modules; these were failed discovery reads, not passing gates. Tool/version/probe logs and raw pinned reference extracts remain in task scratch; design cites OIDs and paths so it does not duplicate entire corpora.

| Numbered owner question | Walk state | Answer location / retained bound |
| --- | --- | --- |
| 1. Schema/references/requirements | Walked — done | §1, schema 3, explicit variants, effective view; new global subset stated |
| 2. Who declares | Walked — done | §2, root selection/consent; no transitive authority |
| 3. Six native writers | Walked — done | §3, shapes/scopes/env/trust/lossless edits; legacy Windsurf and forced SSE capability unknown, refused |
| 4. Ownership/lifecycle | Walked — done | §4, protected entry ledger/CAS/removal/GC/status/dry-run |
| 5. Secrets/auth | Walked — done | §5, no value processing/auth execution, native human flow |
| 6. Git policy | Walked — done | §6, local default/shared opt-in/tracked-config conflicts |
| 7. Windows/stdio | Walked — done | §7, native executable subset, batch deferred, pin limits |
| 8. Security | Walked — done | §8, attacker/trusted/outside model, 12 threat rows, reference alignment |
| 9. Phased slices | Walked — done | §9, entry-point acceptance and frozen vectors |

Walk ratio **9/9**. “Done” in this table means the question was walked, not that the board task has been accepted. No question was skipped after the first anomaly.

## Open questions for the owner

These are product choices for acceptance, not another prerequisite research chain. Recommended defaults let slice 1 start.

1. Accept the same-command interactive **first-install trust selection**, with protected exact-plan preapproval for agent/headless installs? Recommended yes; root Skillfile alone is not execution authorization under the hostile-repository model.
2. Accept **Skillfile schema 3** and the bounded global subset (legacy skills only initially), leaving skill manifests at versions 1–8? Recommended yes; do not retrofit privileged writes into existing schemas.
3. Should shared `.mcp.json`/Cursor generation be opt-in or default? Recommended local default, explicit shared policy; no automatic takeover of tracked files.
4. Is first-slice Windows native-executable/HTTP support sufficient, with npm batch recipes refused until a certified lane? Recommended yes; avoid an untested generic `cmd /c` rewrite.
5. Should the legacy Windsurf profile be preserved as a separate versioned adapter, or should csk add a new Devin adapter? Recommended distinct profiles; verify the owner's target release before enabling either user writer, never migrate based on a documentation redirect.
6. Is future `adopt` needed for preexisting identical native entries, or should users keep them external and remove the provision request? Recommended no takeover in slice 1; add exact-digest adoption only with a separate reviewed recovery policy.
7. Are pinned HTTPS **definition-document** downloads worth the added network surface, or are inline/git/file definitions sufficient initially? Recommended defer URL support until slice 5; design does not conflate definition acquisition with MCP endpoint access.
8. Accept the explicit residual that native clients may inherit broader environments than `env_names`? Recommended document it now; a confined launch broker is a separate architecture, not a claim this writer can fulfill.
