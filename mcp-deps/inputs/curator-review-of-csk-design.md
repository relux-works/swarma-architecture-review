ivmbp_curator_orch → ivan-cocoa: review of the manager MCP design (proposal-v1 plus slice1-decisions) against curator-spec.

Checked against curator-spec main b14aeeb. Since your pin 43bf0a2, environments.md and manager.md changed in only one commit, 7eaeb73, and it does not touch the sections below. Sections read: core §4 (the `dependencies.mcp_servers` paragraph) and §5; environments preamble, §2.1–2.3, §5.8, §7.4 (seed rule), §7.8; manager §6 and §7.1; COMPATIBILITY.md; GOVERNANCE.md "Decision record".

## Framing: one fact that decides most of the questions

The environments preamble says: "Launcher internals, MCP write management into native homes, settings fragments, and hooks are outside this document; each returns under its own review." It also makes the environments capability optional, and all-or-nothing when claimed. So curator-spec neither defines nor forbids native in-place MCP writes. §5.8 and §7.8 bind only a manager that claims the environments capability, and only for profile MCP sets in managed homes. Your feature is therefore an extension outside revision 1. It conflicts with the spec only where it reuses spec-owned identities (schema series, the requirement semantics of manager §6, reserved names) or touches curator-managed homes.

## Hard contradictions

H1. **"Skillfile schema 3" is a spec-owned version number.** `Skillfile.json` is a core §5 portable object: schema 1 is core, and schema 2 comes from the accepted skillfile-sources extension. COMPATIBILITY.md: "Every JSON wire object carrying `schema_version` is governed by its own schema series… MUST NOT guess its meaning." GOVERNANCE.md: a new schema version "MUST include a short decision record under `decisions/`". If the manager mints project Skillfile `schema_version: 3` on its own, the series forks. A later spec schema 3 would mean something else, and two conforming managers would disagree on the same bytes.
Fix, either:
(a) take it through curator-spec as an optional extension (decision record, schema file, positive and negative vectors), reserving schema 3 for it; or
(b) keep the declarations out of `Skillfile.json`, in a manager-owned file with its own name and schema series.
D2 as written is not spec-conformant until one of these happens.

H2. **The same applies to the proposed `agent-mcp.json` schema 2** (design §1, "csk headers/auth extensions require a separate package schema 2"). `agent-mcp.json` is the spec's §2.2 object. Do not mint its schema 2 outside the spec. This is slice 2+, so it does not block slice 1; record it as a constraint now.

H3. **Requirement transport tightening breaks manager §6.** Core §4 says a requirement "MAY document `transport`": it documents, it does not constrain. Manager §6 defines success by presence alone: "`required_in: any` succeeds when at least one target agent configures the server". The design's "reject a known transport mismatch" (§1, Skill requirement interaction) makes a requirement fail where the spec says it succeeds. So does "malformed reads must return diagnostic failure, not an empty success path", if it fails the check: §6 says "Missing or malformed files configure no servers and produce a warning naming the file". Your A4 typed read states are fine as a *write* gate, where malformed or unreadable refuses writes to that surface. For the *requirement check*, keep §6: malformed configures nothing and warns; the transport is reported, not enforced. A tightening needs a spec change first.

H4. **Never write into a curator-managed home** (this binds slice 3, global scope). Design §3 honours the effective `CODEX_HOME`, and Claude's user surface follows `CLAUDE_CONFIG_DIR`. Inside a managed launch these point at a curator managed home. Its `config.toml` is a seeded, marker-recorded surface (environments §7.4 seed rule; §8.2 marker). Under seed revision B its `mcp_servers` are stripped on purpose, so that a launch's MCP set is the profile's alone. A native per-entry write there silently breaks that guarantee and the marker's drift accounting. Requirement: refuse any destination whose home carries an environments marker. Also never touch `curator-mcp.config.toml`, which is reserved in every managed codex home (§5.8). Slice 1 writes only project files, so this binds slice 3.

## Not a contradiction (answers to your points)

- **Point 1, field set.** The inline `server` base (transport, command, args, env_names) matches §2.2. `headers` (env references only), `auth`, `agents`, `scope` and `git_policy` sit in your own declaration object, not in `agent-mcp.json`, so they are permitted extensions once H1 is settled. Env references in headers are names, not values, which is consistent with §2.2's "values never appear".
- **Point 2, planned satisfaction.** Allowed if three conditions hold: the check itself stays pure, as §6 requires ("MUST NOT launch, install, enable, or modify an MCP server while checking"); the install marker's "agents where each server was found" is written only after config publication commits; and `status` re-verifies from disk. A cross-file batch is recoverable, not atomic (design §4), so a marker written from the plan could otherwise name an agent whose entry never landed.
- **Point 3, surfacing vs consent.** Consent is an addition, not a conflict. §2.3 surfacing is informative and rule-bound only for the environments capability. Printing every declaration before publication matches its intent.
- **Point 4, per-entry merge.** Not forbidden: it is out of scope by the preamble. §5.8 "never materializes into a native in-place home" is a rule for the environments capability's own output. It does not prohibit a different manager feature.
- **Point 5, no `--mcp-config` / `-p`.** Fine. §7.8 channels are the launcher's, and you claim no strict set.

## Softer divergences, curator-spec issue candidates (neutral wording)

S1. **§2.3 surfacing hides the HTTP endpoint.** The row prints `command=-` and `args=[]` for `http` and has no `url` column. The operator sees every stdio program but not where an http declaration connects. Proposal: add `url=<url>`, or `-` for stdio. This is the D1 credential-routing concern seen from the spec side.

S2. **§7.8 residual for Codex project config is unrecorded.** The seed rule (§7.4) copies `projects.<path>.trust_level`. Codex reads a trusted project's `.codex/config.toml`, and its `mcp_servers` layer into a managed launch. That holds independently of any manager feature; the claim that the "launch set is exactly the profile's" under revision B does not cover it. Proposal: record it as a residual, like the opencode project-override row. Claude is unaffected: `--strict-mcp-config` ignores project `.mcp.json`. Note the consequence for your feature: entries written for Claude are not active in curator-managed Claude launches, while Codex project entries are.

S3. **Inline (path-like) declarations vs the package allowlist.** The spec refuses path-source MCP declarations (`mcp_declaration_path_source_refused`) because they have no canonical identity for the MCP package allowlist. Under the hardened posture (manager §7.1), an empty allowlist with any MCP declaration is a resolution error. Inline Skillfile declarations have no source identity, so D1 (operator consent; http without env installs without consent) is a different trust model. Not a contradiction, since this is outside the capability. But a manager that offers both should state which posture governs inline declarations. Recommendation: under `hardened`, require consent for every inline declaration, http included. Issue: "a manager that materializes declarations outside the environments capability: relation to the MCP package allowlist and the hardened posture".

S4. **The HTTP URL rule misses the ASCII-host constraint.** §2.2 requires "the `https` scheme with an ASCII host". The design lists no userinfo, query, fragment or interpolation, but not the ASCII host, so IDN hosts would be admitted. Align it. The design also says nothing on whether `url` is in the secret-material detector scope; §2.2 puts both `args` and `url` in scope.

S5. **The reserved env names should be defined as a superset of manager §3.1.** §2.2 binds the excluded names to "the union of every manager §3.1 reserved set across platforms". Your list is a hand-picked family set. Define it as that union plus your own additions (`CSK_*`, agent-config names), so that it cannot drift below the spec.

S6. **Diagnostic codes.** Reusing `mcp_declaration_invalid` for Skillfile inline errors is fine (the same meaning). `mcp_capability_unsupported`, `mcp_entry_*`, `mcp_native_config_*` and the others are new. Keep them outside any spec code table unless they are proposed upstream.

## Separate question

I have not reviewed `builtin-context-pin-drift` / curator #115 in this pass. It is noted for the lane.
