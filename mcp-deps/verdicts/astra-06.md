# astra-06: zoo compatibility, independent adversarial pass

Seat: `ivmbp_swarma-mcp-deps_astra-06`, second independent five, ivmbp.
Status: final after verified convener PARK
`$YGuiFoIqq0SqOg9WywpBf6YwJiuYSmO6w52P8Y0AVJA`; independent score history and
first/second-five agreement preserved.
Date: 2026-10-14.

Final recommendation: **N as the core**, with **A optional and separable**.
For the stated already-configured-provider case, N/N+A scores **13/16 under
amended E3**, **11/16 under original E3**; cold setup scores **12/16** and
**10/16**, respectively. Original E3 remains 0 and fails its eligibility gate.
These are conditional design
scores: the corrected checking and optional provisioning boundaries are required,
and **E7=1** records unfinished normative work. A-discovery alone scores
**11/16 amended**, **9/16 original**.
The tables below preserve the independent baseline and explain every later
qualification. The [PARK record](../parked/astra-06.md) lists the remaining
specification work; no review challenge addressed to this seat remains open.

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
| A alone, recommendation discovery and legacy checker | 2 | 2 | 2 | 0 | 2 | 1 | 1 | 1 | 11 | 0 / 9 |

The initial criterion evidence still applies. A alone adds only discovery of
existing schema-1 bytes and uses current admission, so E1/E2=2; its legacy
checking excludes opaque providers and keeps launch ambiguity, so E4=0/E6=1.
E7=1 for recommendation discovery: syntax reuse alone does not close its ordinary
skill-lane audit scope, severity and waiver rules (late qualification below).
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
   is a different selector. First-pass astra-03 also confirmed this exact case at
   `$-WPmMsTwqDITDwlLnchhPOzpeZDwUvCNbfeRCtPGOkU`. This sharpens existing
   [f-launch-universe](../findings/f-launch-universe.md), not a new finding.

2. **HTTP env auth is an explicit capability limit, not solved by a label.**
   astra-12 confirmed §5.8 and the actual serializers at
   `$DWR-oqZ-bsDlBv-ivxu0oT0wWz1p_YEi6NmpOGXWteM`; my source read included
   `contextmaterialize/mcp.go:244-318`. Existing native HTTP auth is usable only
   in a launch that includes it. No `auth:env` field, env-name allowlist or
   operator assertion supplies a missing header route. Keep this limitation in
   existing secret/zoo findings and capability tables; a future names-only header
   feature needs separate syntax, writers, consent and vectors. My acknowledgement
   is `$iDdjNKN4kqq2KHjtFIuLLOz5qAaUIiaDT97rPvh_RHY`. First-pass confirmations:
   astra-03 `$pqoN-QjlkB5g7Xqw7eRpNAuBDF9cKqvDLNccUSxqOoE` and astra-02
   `$SDG3Hg98YjUa8EGwWXliAclPj-Z5in5qhpPTgYrT1I4`.

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
   collision. No automatic rename/alias or resolver redesign is part of N. The
   owned confirmed finding is
   [f-cross-kind-name-collision](../findings/f-cross-kind-name-collision.md).
   This is a current implementation reuse limit, not a lock-schema prohibition:
   the lock format can distinguish `(kind, name)` even though this resolver
   selects one kind for a name.

For bounded A, the same git snapshot may carry an inert schema-1 recommendation;
show safe candidate metadata only, select its exact commit through an
operator-owned context `requires.mcp`, preserving canonical source, exact
revision, package directory (root shown explicitly) and declaration name, and
independently apply MCP source, signer, allowlist and audit policy.
A path/local skill does not acquire the
git-only declaration identity by co-location. Root schema 1 recommends at most
one declaration; multiple servers use existing companion context packages.
This is optional setup assistance, never authority and never cloud discovery.
Path-source discovery is informational only and emits no executable profile
adoption recipe. A recommendation-discovery feature must explicitly govern
`agent-mcp.json` args/URL secret-scan scope in the ordinary skill lane, including
severity, waiver and admission behavior; the always-strict profile rules cannot
be imported silently. Pre-admission output stays metadata-only and diagnostics
value-free regardless of the scan. Later MCP adoption independently passes its
strict admission rules. Malformed optional metadata is not, by itself, a new
skill-install failure.
The recommendation bytes are pinned by the skill snapshot; adoption makes a
separate operator pin. A later skill update does not update the provider or make
its selected pin stale merely because the name is the same. No ongoing
author/provider coupling or mandatory update-notice mechanism is implied.

Late A-only score qualification, after direct re-reading at spec `a9c03be`:
manager §7:1111-1171 leaves ordinary audit under machine policy and makes
`context-secret-material` mandatory specifically for profile snapshots;
environments §9.1:2302-2319 scopes that mandatory class to context/MCP snapshots.
This does not yet close the ordinary skill-root sidecar contract. I therefore
correct my earlier A-discovery E7=2 to 1 (12/10 becomes 11/9), agreeing with
astra-03's source-checked qualification
`$731Jpduhgk_b3gengesp8z1BBFy-K3u39HvzRMg6qgA`. An inert authored file with no
discovery feature may retain E7=2, but cannot borrow discovery behavior for free.
N and N+A remain 13/11, E7=1; the preferred design and independent proof pair are
unchanged. This is a qualification of the alternative, not a new finding.

Successful strict admission is also **not a secret-free presentation or
provisioning proof**.
The same direct source read establishes that §9.1:2302-2319 permits a scoped
waiver to clear a secret finding, while schema-1 args are arbitrary bounded
strings and HTTPS paths can carry sensitive data. `contextpkg.ParseMCP:497-518`
preserves them, and §2.3 / `FormatDeclarationRows:150-175` serializes raw args.
The current HTTP row has no URL column; this is not a claim of an existing
HTTP-row URL leak. A separate direct read of §5.8's serializers at
`contextmaterialize/mcp.go:244-327` confirms they copy args/URL into generated
files. A waived credential literal therefore reaches persistence/forwarding as
well as potential display. JSON/TOML escaping and a waiver do not sanitize it.
Thus a waived finding cannot authorize disclosure or value-bearing provisioning
under the dependency feature's stronger no-use/no-store/no-forward promise.
Presentation remains
independently bounded after admission: withhold known/waived sensitive details
or refuse detailed surfacing; a detector miss is not a proof of safe bytes.
If withholding prevents meaningful exact-plan review, keep the new mutation
unapproved. N's checking/assertion path needs no such reproduction. Optional
provisioning must refuse/defer credential-bearing cases under this feature's
claim; a legacy operation delegated unchanged stays outside that stronger claim.
A governed reconciliation is needed wherever current mandatory raw surfacing,
materialization or general waiver compatibility conflicts with the corrected E3
contract. This does not remove the general waiver mechanism or introduce a
credential classifier. It qualifies existing reuse; it is not a new credential
mechanism or a claim that current Curator already conforms. N/N+A E3=2 stays
conditional on this corrected bounded path, with E7=1 reserving the normative
work. My display confirmation is `$woL6DCgGyMNdEsCeou1DBjqFEDSqzQwGXbfNjecvjUY`;
the serializer follow-up is astra-12's
`$lUSbVgBMWBhdEhk31UaFQqExiNO7W6fGl3S57ebwsqE`, accepted by the existing
secret-boundary finding owner astra-02 at
`$uLalPw5QAdJUb8kQmXrn0yOqqe5Xhe7TBeS74X9cLcI`.

### Evidence of agreement and remaining work

The original independent L vector `[0,1,2,2,2,2,1,1]` already differed from
astra-03's N vector `[1,1,2,2,2,2,1,2]` by at most one per row. The concrete
existing-carrier/common-case refinement gives my current N/N+A vector
`[1,1,2,2,2,2,1,2] = 13`, equal to astra-03's. We are separate sessions and
directories in the first and second independent fives. **astra-03 explicitly
acknowledged the same candidate and read my complete frozen baseline at
`$7Q7hZ8vwgM3_PzWDcavW9tlMilzWWm5fNVzC2NEMX2c`.** This supplies the amended
mission's bounded rubric proof, using the independent baseline as well as the
separately recorded post-debate clarification. It is not proof of a unique global
optimum, completed specification, implemented
conformance or current native-client certification. E7 deliberately remains 1.

Before implementation: govern the protected configuration grammar, evidence
status/aggregation, selector scope and revocation, same-provider negative
precedence, adapter completeness and assertion/system-policy interaction. Retain
all applicable admission/hardened gates, consent for new writes, and the
manager-versus-launcher auth boundary. No new portable marker is mandatory when
scoped status is transient; do not relabel legacy `FoundIn` as stronger evidence.
The scoped check must be explicitly requested at a governed skill-check entry
point with selected-launch inputs. Availability of profile-lock evidence does
not mean profile install already runs such a gate, and this proposal must not
silently add a fatal environment-lifecycle check. Invocation, compatibility and
failure rules remain part of E7's unfinished normative work.

The E6=2 condition is explicit: render evidence source and grade together as
`configured by name / provider identity and authentication not checked`, or
`operator-asserted`. In the opted-in selected-launch check, a project-file entry
alone never establishes observed-effective inclusion. Known rejection, ignoring,
disabling or exclusion defeats acceptance; unobserved client activation/trust
stays unknown/pending unless the governed protected-reliance path is permitted,
in which case it stays asserted. Such reliance neither grants native workspace
trust nor overrides a known denial. Legacy §6 presence plus warning retains its
legacy meaning. I stated this at `$B5QnpvuW_xpWXR3HqRomKjb3kUX8KUBoYel8PUX7P0g`;
wonder-12 accepted the bounded E6=2 condition at
`$EPII6SRyCz1HAGKpUMXptv-sC3S42daQGPYtw346D_o`, acknowledged by me at
`$M2t2Oy8eMX5ZGicYLMCnutYhkD5v13OxWIYwKI4cyw0`. A variant reporting bare
satisfaction from project-name presence deserves E6=1; that dissent remains a
condition on the design, not a claim of completed normative precision.

All research is persisted here. No source, board, task-system or native config
was changed. Existing finding owners may cite the confirmations above; this seat
does not create duplicate finding files or edit their artifacts.
