# astra-06: zoo compatibility, independent adversarial pass

Seat: `ivmbp_swarma-mcp-deps_astra-06`, second independent five, ivmbp.
Status: independent score preserved; round 1 adversarial reconciliation complete;
active until convener PARK.
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
| **Total, amended E3** | **5** | **11** | **10** | L preferred on these independently considered candidates, not a proof over every possible design. |

Under the **original literal E3** row all three score **0** where they parse
mixed native configs, because existing bytes can contain credential values.
Original-row totals are B **4**, L **9**, B+ **8**; all fail its E3 eligibility
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

The initial signed checkpoint was `c587dc9a9797c13b07e028e4a20447f8a1829add`,
rebased with signing and published as `0f030fafecaafafce1a9ca8d50b8d23ea28ab5ab`.
Its B+ total was an arithmetic typo (9 instead of 10, original 7 instead of 8),
corrected above and in room event `$zWGK6X4PHPM17PTq93P2IUyazc4sj9-DPzae69daCCU`;
no per-row independent score changed. The first-score publication preceded my
first astra-03 verdict read: `$Us6W5xQCXOtx7oFAcMUG8kGdOxG1uoy2w_KFCLIxJu4`.

## Post-freeze adversarial comparison

I read astra-03's first-five verdict only after the independent checkpoint. Its
concrete **N** is a refinement of my L: the binding is carried by a successor of
the existing protected manager configuration, not a standalone authority-record
family. Scoped evidence can remain a transient result while the legacy marker
keeps its old meaning; a new marker version is needed only if that evidence is
persisted there. This earns E1=1 rather than my initial standalone-family E1=0.
E2 stays 1: launch-aware checking is still new work.

For a clearly stated **already-configured suitable provider** common case, E8=2
is justified: observed providers require no setup, and an opaque provider needs
one scoped operator decision. This is a workload assumption, not measured
prevalence or a claim of one-click first setup. Cold setup retains E8=1.

| Current serious candidate | E1 | E2 | E3 amended | E4 | E5 | E6 | E7 | E8 | Total | Original E3 / total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| B, unchanged base | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 5 | 0 / 4 |
| B+, repaired authoritative identity | 0 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 10 | 0 / 8 |
| N, named requirement and scoped local evidence | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 13 | 0 / 11 |
| N+A, N plus bounded optional recommendation | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 13 | 0 / 11 |
| A alone, recommendation and legacy checker | 2 | 2 | 2 | 0 | 2 | 1 | 2 | 1 | 12 | 0 / 10 |

The initial criterion evidence still applies. A alone adds only discovery of
existing schema-1 bytes and uses current admission, so E1/E2/E7=2; its legacy
checking excludes opaque providers and keeps launch ambiguity, so E4=0/E6=1.
Its E3=2 is conditional on the corrected bounded diagnostics, not retention of
current raw-command output. N+A imports N's actual evidence machinery, so its
score must not pretend to get both that machinery and A-alone minimality for
free. N/N+A tie; I prefer **N as the core**, with A optional and separable.

### Attempts to break the preferred candidate

1. **Disabled-layer resurrection is confirmed, and repaired in the contract.**
   My exact OpenCode counterexample was independently checked by astra-13 at
   `$3gLOuU_zpyqKhXrTTBjgvnUPNRRrKE7zUy0wy-2Ot98` and acknowledged by me at
   `$Kzctr9tXQ_LgZIk5WmtordyZoiv0ClqQxmesJaIE6OU`. Keep negative observations
   through layer resolution, then filter; never resurrect a lower native entry
   by selecting that surface explicitly. An unrelated same-name opaque connector
   is a different selector. This sharpens existing
   [f-launch-universe](../findings/f-launch-universe.md), not a new finding.

2. **HTTP env auth is an explicit capability limit, not solved by a label.**
   astra-12 confirmed §5.8 and the actual serializers at
   `$DWR-oqZ-bsDlBv-ivxu0oT0wWz1p_YEi6NmpOGXWteM`; my source read included
   `contextmaterialize/mcp.go:244-318`. Existing native HTTP auth is usable only
   in a launch that includes it. No `auth:env` field, env-name allowlist or
   operator assertion supplies a missing header route. Keep this limitation in
   existing secret/zoo findings and capability tables; a future names-only header
   feature needs separate syntax, writers, consent and vectors. My acknowledgement
   is `$iDdjNKN4kqq2KHjtFIuLLOz5qAaUIiaDT97rPvh_RHY`.

3. **Empty profile is not strict exclusion.** §5.8 and
   `contextmaterialize/mcp.go:217-224` emit no file/channel for an empty set.
   The precise first/vector counterexample above is native `docs` plus an
   **actually applied, nonempty strict channel containing another server and
   excluding docs**. Do not infer exclusion from profile-empty alone. Pi's
   absence is limited to the recorded revision-1 managed adapter/0.84.2, not
   arbitrary native plugins or later client versions.

4. **Opaque evidence stays weaker than observation.** N accepts explicit
   reliance rather than discovering a hidden provider. Scope it to the exact
   requirement identity, selected client/home/project/profile and provider
   selector; no global name-only acceptance, no repository self-attestation.
   A known negative for that effective provider wins, but absence from native
   files does not negate a separately bound connector. Internal connector drift
   remains unobservable. E4=2 is coverage of all provider categories by honest
   evidence/acceptance paths, not universal automated verification or new client
   functionality. An interpretation requiring those stronger guarantees should
   score E4=1; then N/N+A total 12 and still lead the complete candidates.

5. **Existing warnings also need the metadata bound.** The actual checker prints
   the raw command at `mcp.go:143-144`. Manager §6 requires a warning, not that
   string. Preserve private static PATH lookup; emit a fixed diagnostic keyed by
   safe requirement/target identifiers, never arbitrary command/argv, URL, env,
   parser snippets or unvalidated native labels. astra-02 source confirmation:
   `$woH4Tj0pbOWRhxLB_2amNCvyXCRv4HHDV2X717_ObdQ`. This is a condition on the
   proposed E3=2 contract, not a claim current implementation already satisfies it.

6. **Optional co-location does not permit same-name dual-kind closure.** I
   independently confirmed astra-04's challenge
   `$iUc_uDX_kiEwtByLrYzC4qpzhIODJGkvPXIehrKehkk` by reading, at the same Curator
   pin, `internal/contextresolve/contextresolve.go:316-318,409-419,915-918` and
   `envprofile/managed.go:205-226`: the resolver selects one kind per name and
   only MCP members materialize as MCP. My confirmation event is
   `$cjkXXsAKqa1RgA871RL9IIK9QBe3kTfn9G17XP4UnYU`. A's optional joint-closure
   recipe must use distinct skill and declaration package names, or defer that
   collision. No automatic rename/alias or resolver redesign is part of N.

For bounded A, the same git snapshot may carry an inert schema-1 recommendation;
show safe candidate metadata only, select its exact commit through an
operator-owned context `requires.mcp`, and independently apply MCP source,
signer, allowlist and audit policy. A path/local skill does not acquire the
git-only declaration identity by co-location. Root schema 1 recommends at most
one declaration; multiple servers use existing companion context packages.
This is optional setup assistance, never authority and never cloud discovery.

### Evidence of agreement and remaining work

The original independent L vector `[0,1,2,2,2,2,1,1]` already differed from
astra-03's N vector `[1,1,2,2,2,2,1,2]` by at most one per row. The concrete
existing-carrier/common-case refinement gives my current N/N+A vector
`[1,1,2,2,2,2,1,2] = 13`, equal to astra-03's. We are separate sessions and
directories in the first and second independent fives. This supports the amended
mission's bounded rubric proof after both seats acknowledge the same candidate;
it is not proof of a unique global optimum, completed specification, implemented
conformance or current native-client certification. E7 deliberately remains 1.

Before implementation: govern the protected configuration grammar, evidence
status/aggregation, selector scope and revocation, same-provider negative
precedence, adapter completeness and assertion/system-policy interaction. Retain
all applicable admission/hardened gates, consent for new writes, and the
manager-versus-launcher auth boundary. No new portable marker is mandatory when
scoped status is transient; do not relabel legacy `FoundIn` as stronger evidence.

All research is persisted here. No source, board, task-system or native config
was changed. Existing finding owners may cite the confirmations above; this seat
does not create duplicate finding files or edit their artifacts.
