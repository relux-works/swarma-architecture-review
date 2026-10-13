# astra-06: zoo compatibility, independent adversarial pass

Seat: `ivmbp_swarma-mcp-deps_astra-06`, second independent five, ivmbp.
Status: independent score frozen before first-five verdict access; debate pending.
Date: 2026-10-14.

## Independence and evidence boundary

This initial position was formed from MISSION-MCP.md, BASE-DESIGN.md, all three
inputs, and the local specification and implementation. No first-five verdict
file or topic body was read before this score was written. `a2a topics` titles
were listed as required for onboarding; their arguments and scores were not read.

Source pins:

- review repository: `b5e7dabf6f548e727a9933e2e6371d7b6a0d83f7`;
- curator-spec: `a9c03be237b723b5bf87aed070165ad6f68b2586`;
- curator: `5234cf38833554542e68afade15951c6e56ed89e`.

The required initial `git pull --rebase` failed with an SSH connection reset on
port 22. Source clones were read without updating, because writes outside the
seat directory are forbidden. No builds, client invocations, authentication,
network probes of MCP servers, or credential files were used. Tool readiness and
failed pull evidence are in the seat's `.temp/astra-06/`. One source read used
the implementation cwd for a spec-relative path and returned file-not-found; the
correct spec path was subsequently read. These are static conclusions, not new
runtime certification. Mission artifacts are the task/documentation flow.

## Independently considered designs and scores

- **B: base as written.** Require / Provide / Bind, including the skill-level
  `server` union, declaration auth class, local aliases, and optional provisioning.
- **L: named requirement, local provision choice, scoped evidence.** Keep the
  existing portable skill requirement. Operator configuration chooses existing
  declarations or external providers. Check evidence for the selected launch,
  preserving native/profile precedence. Opaque providers may use an explicit,
  protected, scoped operator assertion, reported as asserted rather than observed.
  No assertion overrides a known disabled/excluded provider. Provisioning remains
  a separate consented operation using the existing profile or native writer.
- **B+: repaired identity-bearing base.** Keep skill `server` but close its
  identity/equivalence and versioning contracts; add the same evidence and trust
  boundaries as L. This is viable but makes declaration acquisition identity a
  portable requirement concern, with more cross-client exceptions.

| Criterion | B | L | B+ | Evidence and reason |
| --- | ---: | ---: | ---: | --- |
| E1 new concepts/fields | 0 | 0 | 0 | B adds a nested identity union, alias/binding semantics and declaration auth metadata, not merely one field's syntax. L still needs a new local evidence/binding object contract; it is not free just because the skill schema is unchanged. B+ retains both costs. |
| E2 reuse | 1 | 1 | 1 | All reuse requirements and optional profile/native provisioning, but none can derive opaque evidence or effective launch checking from today's native-file name union. `internal/mcp/mcp.go:22-62,89-136`. |
| E3 amended secrets | 1 | 2 | 2 | B states absolute no-read/no-forward but does not bound foreign config parsing or recipe comparison. L/B+ require bounded transient parsing and metadata-only outputs, no value expansion, no health/auth operations. Inputs proposal §§4-5 supply a workable preservation boundary. |
| E4 zoo | 0 | 2 | 2 | B's configured-name prerequisite has no route for opaque providers; an identity override alone does not establish enabled presence. L/B+ admit existing client metadata or explicit scoped operator evidence, without requiring a client API change. This is acceptance of evidence, never proof of availability/authentication. |
| E5 portability | 1 | 2 | 1 | Names remain the shared skill requirement in L; local recipes and cloud/plugin bindings vary. B/B+ tie stronger requirements to one package recipe or endpoint unless local equivalence policy rescues them. |
| E6 honest failure | 1 | 2 | 2 | B has consent and auth-not-checked, but leaves unknown and launch scope unresolved. L/B+ require typed unknown, known negative precedence, explicit assertion provenance and consent before every new write. |
| E7 specifiability | 0 | 1 | 1 | B leaves identity comparison, binding grammar and version gate open. L/B+ have writable counterexample vectors below but still need a closed adopted schema/profile. Core §4, common.schema.json `$defs.mcpRequirement`, COMPATIBILITY stability and GOVERNANCE Changes/Decision record. |
| E8 operator effort | 1 | 1 | 1 | Existing visible provider costs zero; opaque provider one local assertion. Fresh env setup, client login, package allowlist and provisioning can be multiple independent actions. No universal one-action claim is evidenced. |
| **Total, amended E3** | **5** | **11** | **9** | L preferred on these independently considered candidates, not a proof over every possible design. |

Under the **original literal E3** row all three score **0** where they parse
mixed native configs, because existing bytes can contain credential values.
Original-row totals are B **4**, L **9**, B+ **7**; all fail its E3 eligibility
gate. The amended row is the proof row. The manager/launcher ownership distinction
must also be explicit: environments §§7.8/10.3 delegates operator-value
passthrough to the launcher; the requirement verifier must not resolve values.

## Zoo counterexamples and evidence

1. **Native configuration is not the selected launch set.** Environments §7.8
   says managed Claude's strict channel ignores other MCP configuration. A
   csk-written `.mcp.json` therefore cannot satisfy that selected managed launch
   just because `internal/mcp` sees its name. Conversely §5.8 puts the profile's
   file under `.agent-context/mcp/`, which `internal/mcp` does not read. Both a
   false positive and a false negative follow from reusing that checker alone.

2. **Dropping disabled entries before composition loses negative intent.**
   `internal/mcp/mcp.go:54-61,254-270` removes a disabled project OpenCode entry
   and then unions home entries. Environments §7.8 says project overrides
   `OPENCODE_CONFIG` and global state. With home `docs` enabled and project
   `docs.enabled=false`, simple positive-name union resurrects the home name.
   Effective precedence must retain the negative entry until after composition.
   This is a static code/spec counterexample, not an executed client test.

3. **Managed HTTP env authentication lacks a routing representation.**
   Environments §2.2 has `url` and `env_names`; §5.8 emits only type/url (or just
   url for Codex). `internal/contextmaterialize/mcp.go`'s MCPServer has no header
   binding. By contrast the csk input §3 requires Codex `bearer_token_env_var`
   or `env_http_headers`, and other clients' header interpolation. Naming an
   environment variable for the client does not tell a remote HTTP client which
   header receives it. Base `auth: env` alone cannot claim that recipe is
   provisionable across the zoo. Keep externally configured auth valid; either
   refuse this managed provisioning capability explicitly or separately govern
   names-only header bindings. This does not justify reading a secret value.

4. **An opaque provider cannot be discovered from absence.** Manager §6 and
   `internal/mcp` enumerate native files, not cloud-account connectors or all
   plugin inventories. Two clients with identical inspected files may differ in
   a cloud connector. Any algorithm limited to those files must give the same
   result for both. It needs existing client metadata or new operator evidence,
   otherwise unknown is the only honest result. A name alias is not evidence.

5. **A declared package is not an effective endpoint or executable.**
   Environments §2.2 permits HTTP declaration packages, so the base's package
   comparison via command/args is not even total. The same stdio recipe can
   select a different PATH binary or transitive runtime package; csk input §7
   explicitly distinguishes definition pinning from runtime identity. Package
   provenance, normalized static configuration, and service equivalence must
   not be one predicate.

6. **No MCP channel is a capability boundary.** Environments §5.8/§7.8 gives
   Pi no MCP output/channel. Do not let `all` silently shrink to clients that
   happen to be inspectable or supported. Existing names remain portable syntax,
   not a promise that every client can implement MCP. A known unsupported target
   is unsatisfied; a binding cannot manufacture client functionality.

The csk owner decisions override proposal-v1 where they differ. In particular
D1 permits HTTP without env references to install without consent; that is a
recorded native-writer policy, not evidence that the mission base's stricter
consent-before-write promise is implemented. D5/D7 restrict the actual first
slice to three clients and inline definitions. Its future package support must
not be counted as existing machinery.

## Smallest change set and proposed conformance examples

Prefer L. Remove skill `server` for the first increment; preserve v5-v8 grammar
and treat package choice as operator provisioning policy. Add one explicitly
versioned manager contract for launch-scoped, metadata-only requirement evidence
and local assertion/binding authority. Existing requirement semantics must not
silently be tightened in their old profile; governance must name the new check
and compatibility treatment. Reuse declaration admission and writers only where
they actually express the desired configuration.

Required outcomes for the new contract:

| Input | Expected outcome |
| --- | --- |
| Native Claude project `docs`; strict managed profile without `docs` | unsatisfied for that launch |
| Managed profile `docs`, valid applied channel; no native `docs` | observed in managed launch |
| OpenCode home enabled `docs`; higher project disabled `docs` | unsatisfied, known-disabled |
| Opaque cloud connector, no metadata or operator assertion | unknown, never silently satisfied |
| Same opaque connector with protected assertion for this client/home/project/profile | accepted-as-asserted, auth not checked |
| Assertion reused with a different launch scope or known disabled entry | stale/invalid or unsatisfied; no positive fallback |
| `any`: one observed target, one unknown | satisfied with per-target unknown retained |
| `all`: one observed target, one unknown/unsupported | not satisfied; target denominator unchanged |
| HTTP package requiring env token but no supported header route | provisioning unsupported; external configured provider still eligible |
| Project approval/alias file attempts to attest for itself | untrusted evidence; no authority, no writes |

Next: publish this frozen independent score, then read astra-03's position and
the room, confirm/refute with cited evidence, and update only the debate section.
Do not write a finding file without high confidence and another seat's event-id
confirmation. Stay active through rounds until the convener's PARK.
