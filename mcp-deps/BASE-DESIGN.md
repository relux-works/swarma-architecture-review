# Base design: MCP servers as skill dependencies (Require / Provide / Bind)

Author: ivmbp_curator_orch (curator lane orchestrator), 2026-10-14. This is the **starting proposal** for the collective, not a decision. Attack it.

## The owner's goal (verbatim, 2026-10-14)

«у меня есть простая цель - нужно что бы скиллы могли добавлять к себе в зависимость mcp сервера, так что бы это просто требование элегатно сочеталось с тем зоопарком подходов к работе с mcp что я сейчас вижу, особенно - что бы элегантно решался вопрос аутентификации (что бы куратор не брал на себя слишком много)»

The goal in English:
- skills can declare MCP servers as dependencies;
- the requirement combines elegantly with the existing zoo of MCP approaches;
- authentication is solved elegantly, and the manager (Curator) does not take on too much.

## The zoo today (what any design must coexist with)

| Source of an MCP server | Who writes the config | Where | Auth handled by |
|---|---|---|---|
| Hand-written native config | the operator | `.mcp.json`, `~/.claude.json`, `.codex/config.toml`, `.cursor/mcp.json`, `opencode.json`, `~/.gemini/settings.json` (manager §6 table) | the client: OAuth flows, env refs |
| Client plugins / extensions bundling MCP | the plugin installer | client-owned plugin dirs | the client |
| Cloud connectors (provider-hosted remote MCP) | the provider account | not on disk | the provider and the client |
| Curator environment profiles | the manager, as `requires.mcp` → `agent-mcp.json` packages | managed homes only, launched through `--mcp-config` / `-p curator-mcp` / `OPENCODE_CONFIG` (environments §§2.2, 5.8, 7.8) | env **names** only (`env_names`, `passable_env_names`); values come from the operator |
| cocoaskills (csk) Skillfile proposal | csk `install` | native in-place configs, with per-entry ownership | env references in the native client syntax; OAuth by the native client |

What already exists for skills: core §4, `dependencies.mcp_servers` (manifest v5+): `{<name>: {hint, transport?: stdio|http, required_in?: any|all}}`. Manager §6 verifies it **read-only** against the native surfaces: presence by name, disabled entries do not count, a missing command warns, and project-only configuration warns.

## Design: three layers, with the manager thin in each

### 1. Require (the skill)

The skill keeps `dependencies.mcp_servers`, extended by **one optional field**, `server`, which states the server's identity:
- `{"package": {"git": "…", "range": "^1"}}`: an `agent-mcp.json` declaration package (environments §2.2), **or**
- `{"endpoint": "https://…"}`: the identity of a remote server (an HTTPS origin plus path).

A skill **never installs anything** and never carries config, credentials or approval state. A requirement without `server` keeps today's meaning: name only.

### 2. Provide (anyone)

A requirement is **satisfied** when, for the target agent(s) per `required_in`:
- some configured, enabled server has the required name (or the name the Bind layer maps it to), **and**
- if `server` is given, the configured entry's identity matches: the same declaration digest or command/args for a package, the same origin+path for an endpoint, or an explicit operator binding.

**Where the server came from does not matter:** hand-written, a plugin, a cloud connector the client reports, a Curator profile, or csk. The manager checks read-only, as manager §6 does today, and never claims "connected" or "authenticated".

### 3. Bind (the machine / operator)

- **Aliases.** Machine or project configuration may map `required name → configured name` (for example `figma → figma-dev`). Names are local labels; skills cannot rename the operator's servers.
- **Optional provisioning.** When a requirement is unsatisfied and carries `server.package`, the manager MAY offer to provision it from that declaration package:
  - into managed homes through the existing environments §5.8 channel, **or**
  - for a manager that implements native writes (the csk feature), into a native config.

  Either way, provisioning happens only with **explicit operator consent** and under the existing package allowlist, audit and signer policy. Endpoint-only requirements are never auto-provisioned.

### Authentication: entirely the client's job

- Declarations carry only an **auth class**: `none`, `oauth`, or `env` with variable **names**. They never carry values, tokens, client secrets or header literals.
- `oauth`: the native client performs the flow (`/mcp` in Claude Code, `codex mcp login`, and so on). The manager prints what to do and never executes it.
- `env`: values come from the operator's environment; in managed launches the existing `passable_env_names` allowlist bounds them. The manager never reads, stores or forwards values.
- Status reports "configured / auth not checked". The manager runs **no health checks**, because a health check can itself send a credential.

### Why this is meant to be elegant

1. **One new optional field** (`server`) on an existing object. Everything else reuses existing machinery: the v5 requirement, the §2.2 declaration package, §5.8 materialization, the allowlist, audit and consent.
2. **Requirements are separated from provisioning**, so the zoo stays as it is, and every member of the zoo can satisfy a requirement.
3. **No secrets in the manager, ever.**
4. **Curator and csk share one declaration format and one requirement semantics**, and differ only in *where* they may write.

## Known open points (start here)

- **Identity matching** for servers that the manager cannot see: plugins and cloud connectors. Is "unknown" acceptable for `required_in: any`?
- **Transport mismatch:** should `server` make transport checking normative, given that today `transport` is documentary?
- **The schema home:** does a skill-manifest field belong to manifest schema 9 (draft) or to a v5+ optional extension? Note the governance rules in COMPATIBILITY.md and GOVERNANCE.md.
- **Native writes vs managed homes:** both stay legal (environments preamble), but what rule keeps them from colliding (environments §7.8 residuals, curator-spec#141)?
- **Is the alias map one concept too many?** Could the `server` identity replace aliasing entirely?
