> Final on convener PARK, 2026-10-14T00:16Z: prefer N-C (named requirements plus protected, selected-launch evidence), optionally with corrected inert recommendations. Score **12/16 amended, 10/16 original**; E4=1, E7=1. A alone is **11/16 amended, 9/16 original**, after correcting its E7 over-credit. Cross-host comparison with astra-03 meets the one-point-per-row tolerance, with the E4 interpretation difference retained. This is a bounded design assessment, not runtime or universal compatibility proof. The independently frozen initial record follows unchanged; later refinements and final disposition are appended.

# macmini-astra-13 — adversarial zoo compatibility

Status: independent initial verdict, frozen 2026-10-13T22:12:01Z (2026-10-14 local). Third, optional cross-host pass. Seat identity: `macmini_swarma-mcp-deps_astra-13`. Lens: challenge astra-03 on native configuration, plugins, cloud connectors, managed launches and csk.

## Independence and evidence boundary

This initial section was formed and saved before reading any other seat's verdict file or substantive room discussion. Only topic titles were listed for onboarding. Mission, base and all three supplied inputs were read. No implementation, client, build or test was run; source and specification statements below are static evidence. No live native configuration or credential store was inspected. This is not yet a cross-host agreement or implementation proof.

Pins: review repository `b5e7dabf6f548e727a9933e2e6371d7b6a0d83f7`; curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`; curator `5234cf38833554542e68afade15951c6e56ed89e`.

## Independently considered designs

- **B — base Require / Provide / Bind**, as written, including its open points.
- **R — repaired Require / Provide / Bind**: retain the optional skill identity, but define a protected binding/evidence record, selected-launch scope, conservative unknowns, distinct package provenance and operator-equivalence assertions, bounded metadata projection, and a governed version transition. No speculative client introspection is presumed.
- **N — named requirement plus operator evidence**: leave the released skill requirement unchanged. The operator selects provisioning through existing profiles or csk; a new protected local record maps a requirement to evidence for an exact client/home/project/launch mode. Observable configuration and explicit operator attestation are different result types. The skill gains no recipe, endpoint or authority. A name remains a logical dependency label, not a claim of cryptographic service identity.

N is my provisional preference. It pays explicitly for the local evidence mechanism while avoiding package acquisition identity in portable skills. R is a serious alternative if publishers need stronger optional identity constraints.

## Initial scores — immutable baseline

Intermediate score 1 means partial coverage or an unresolved contract. Scores judge designs, not shipped implementations. E3 uses the amended mission row; original-row differences follow the table.

| Criterion | B | R | N | Evidence and reasoning |
|---|---:|---:|---:|---|
| E1 New concepts/fields | 1 | 0 | 0 | B adds aliases and auth semantics beyond one skill field. R/N explicitly introduce a protected evidence-record family; it is not free because it lives locally. Existing `mcpRequirement` is closed (`common.schema.json:609–619`), as is manager configuration (manager §1). |
| E2 Reuse | 1 | 1 | 1 | All retain existing declarations, allowlist and materialization. Neither plugin/cloud evidence nor effective-launch reconciliation exists in `internal/mcp/mcp.go:22–62,89–165`; R/N add that machinery. |
| E3 Secret boundary, amended | 1 | 2 | 2 | B states no secret handling but gives no bound for foreign config identity comparisons. R/N require private bounded parsing, metadata-only output, no raw argv/URL/env retention, no credential lookup, expansion, auth or endpoint probe. csk proposal §§4–5 supplies the applicable boundary. |
| E4 Zoo | 0 | 1 | 1 | B assumes observable enabled providers and leaves opaque providers open. R/N give every source category a conditional path through observation or explicit attestation, but cannot guarantee actual availability in unsupported or suppressing launch modes. Literal universal automatic verification remains impossible; see cases below. |
| E5 Portability | 1 | 2 | 2 | B conflates recipe/package identity with service equivalence and leaves fallback underspecified. R makes equivalence explicit; N leaves machine choices entirely outside the skill. Core §4.4 already supplies named requirements. |
| E6 Honest failure | 1 | 2 | 2 | B promises consent/auth-unchecked but does not close unknown, stale binding, target-set or precedence rules. R/N never turn unknown into observed configuration; known disable/deny/suppression defeats positive evidence. Existing any/all targets stay fixed. |
| E7 Specifiability | 0 | 1 | 1 | B's digest-or-command equality and alias/binding semantics lack a closed contract. R/N have writable discriminating cases but still need normative grammar, carrier/version and vectors through GOVERNANCE.md; a sketch is not a completed protocol. |
| E8 Operator effort | 1 | 1 | 2 | B/R add identity reconciliation even for equivalent differently packaged servers. N retains zero-action observable same-name configuration and one explicit local attestation for a compatible opaque provider. Authentication setup remains a separate native-client operation; neither design promises universal zero-setup auth. |
| **Total / 16** | **6** | **10** | **11** | Conditional design assessment, not universal optimality proof. |

Under **original E3**, B/R/N each score **0**, rather than 1/2/2: supporting native mixed files entails reading bytes which may contain credentials. Original totals are 5/8/9 and all fail the original E3 admissibility gate. The amended interpretation is the mission's proof basis. B's amended score is capped at 1 by its missing explicit parser bound; the absence of such a bound is not evidence that the implementation intentionally uses credentials.

E4 clarification: 1 for R/N is partial, conditional coverage, not a claim that all source/client/mode combinations work. Under a strict reading that any excluded combination forces zero, both become E4=0 and totals 9/10. A collective must state its supported universe before granting E4=2.

## Discriminating zoo cases

1. **Opaque account connector, no metadata API.** Two account states (enabled and absent/disabled) can expose identical filesystem inputs. A file-only checker must return the same result for both. Thus it cannot truthfully observe satisfaction for one and rejection for the other. An existing metadata-only client report, an explicit weaker operator attestation, or a client capability change is required. BASE-DESIGN's phrase “a cloud connector the client reports” is a precondition, not evidence that every client reports it. Native reader tables provide no plugin/cloud surface (manager §6; `mcp.go:22–40`). No particular vendor's undocumented API absence is asserted here.

2. **csk project server suppressed in managed Claude.** `.mcp.json` can contain enabled `docs`, satisfying today's native-name check. Managed Claude with `--strict-mcp-config` ignores that file; if the profile does not contain `docs`, it is not in that launch. Re-running csk or accepting an alias cannot change this. Choose a compatible native launch or explicitly add an admissible declaration to the profile. A provider that cannot be expressed/exported into the channel cannot satisfy that managed launch merely through attestation. Evidence: environments §5.8 `1112–1125`, §7.8 `1837,1847`; csk review H4/S2. This is a manager/launch-policy boundary, not necessarily a client-code change.

3. **Plugin descriptor is not enabled runtime registration.** Finding a package or bundled manifest does not establish that its MCP feature is enabled for this workspace/client/account. Resolve the configured instance in the selected launch, including native disable and trust state. An opaque instance may be operator-attested; it must never be reported as machine-observed.

4. **Managed HTTP with env-header authentication.** csk has an explicit `headers.Authorization={env:...,prefix:bearer}` representation and native writers (proposal `171–180`). Current `agent-mcp.json` and §5.8 HTTP output carry URL only; an `env_names` list in the client's process is not a rule mapping a variable into an outgoing header (`contextmaterialize/mcp.go:41–53`; environments `1123–1130`). Therefore “same declaration format” does not yet cover this working native recipe in managed output. This requires a governed declaration/serializer capability or choosing an already-capable native route, not manager credential handling. Merely adding `auth: env` is insufficient. This is a manager-format gap, not proof a client must change.

5. **OpenCode override, Codex seed versus project.** A profile entry can lose to a same-name project entry in OpenCode (environments `1839,1849`). Codex revision-B seed stripping concerns the base; the supplied curator review S2 records a trusted-project residual. A union of discovered names cannot establish effective identity. `ConfiguredServers` actually inserts project entries then home entries (`mcp.go:54–62`), which is not an adapter-specific launch resolver. Preserve the review's evidence level; no native runtime was reproduced here.

6. **Unsupported MCP channel.** Revision-1 managed `pi` explicitly has no MCP file or launch channel (`environments:1840,1850`; `SupportsMCPFile`, `contextmaterialize/mcp.go:69–77`). A requirement over targets `{claude_code,pi}` with `all` must not drop pi to manufacture success. `any` may succeed through Claude. There is no documented manager-only route that makes pi's missing channel appear; any new extension/client capability must be separately established. This bounds the zoo claim without assuming all zoo/client cross-products were intended.

7. **Native support is not writer support.** csk slice-1 D5/D7 limits writers to three clients and inline declarations; Windows batch recipes refuse under D4. An already configured external entry may still satisfy a named requirement without csk ownership. Treating native-write support as a prerequisite for satisfaction would unnecessarily exclude working zoo members. csk proposal `209–216,270–272` and owner decisions D4–D7.

## Smallest change set and initial round position

1. Keep v5–v8 name-only requirements byte- and semantics-compatible; explicitly version any stronger verification lane. Transport remains documentary for legacy requirements (core §4.4; supplied curator review H3).
2. Define the verification universe first: actual target set, client/version, native versus managed mode, project/home and active channel. Separate legacy configured presence from effective-launch evidence.
3. Specify protected local binding/evidence with `observed`, `operator-attested`, `unknown`, and known-negative outcomes. Bind assertions to their scope and inspected/provider revision where available, invalidate on relevant scope changes, prohibit repository self-approval, and never let a positive assertion override known disable/deny/suppression. No auth or connectivity claim follows.
4. Reuse profile provisioning with explicit consent and existing package/source/signer policy. Keep csk's native entry ownership and managed-home exclusion. A requirement alone cannot install, authenticate or confer ownership.
5. State native-byte bounds and versioned adapter capability limits. Extend headers/auth grammar only by a separate governed declaration change when needed; do not pretend schema 1 already supports it.
6. Write conformance cases for opaque providers, stale/wrong-scope assertions, suppressed entries, same-name override, missing channel, HTTP env-header materialization, and any/all with unsupported targets. No such tests were run in this review.

No finding file is created yet: mission requires peer confirmation. Debate updates will be appended without rewriting this independent baseline.

## Round 1 reconciliation after the independent freeze

The convener's direct naming directive `$5e4rLfiQwYQ5pZXEE51i58nVI995XCRbNJhavrTs97I` superseded the prefixed path. This seat moved its own file to `mcp-deps/verdicts/astra-13.md`; the frozen initial bytes retain SHA-256 `6e8ceb9b5669aa4ce620fe96d5e5841296bf3d307b9d83e2dab066cecf701f66` in signed, signature-verified local commit `e948938`. No shared-main push occurred.

Only after that initial save, I read astra-03's verdict and the existing `f-launch-universe`, `f-opaque-provider`, `alt-names-local-evidence` and `alt-skill-ships-declaration` discussion. The two zoo findings were independently reproduced by my initial cases. I confirmed launch scoping at `$Ik6SFKGm-9ekiZyHUaGRomeGLoHoWzQQZcIZiEa-QDU` and opaque evidence at `$wLoUfoiOHgAPNZNmoxN_csBRJZY6WzWiKvsgMOyx22k`. Their owners/convener may integrate those confirmations; I will not duplicate or edit their findings.

My initial R/N defined a separate authority-record family, hence E1=0. The collective **N-C** specifies successors of existing protected manager configuration and result carriers instead. That is a smaller concrete variant, deserving E1=1. This is a disclosed design refinement, not retroactive editing of independent scores. Whether a portable marker successor is necessary, or a local result can preserve the old marker's meaning, remains a governance choice; no marker may silently conflate asserted with observed.

I now also consider **A alone** serious: optional discovery of existing same-snapshot `agent-mcp.json` as an inert recommendation, safe metadata only before independent MCP admission, existing operator-selected provisioning, legacy checker unchanged. It does not inherit N-C's checker/evidence machinery. **N-C+A** is a convenience composition, not a second identity mechanism.

| Current candidate | E1 | E2 | E3 amended | E4 | E5 | E6 | E7 | E8 | Total | Original E3 / total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| N-C, existing config/result families | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | **12** | 0 / 10 |
| N-C+A, optional recommendation | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | **12** | 0 / 10 |
| A alone, legacy checker only | 2 | 2 | 2 | 0 | 2 | 1 | 2 | 1 | **12** | 0 / 10 |

N-C E2/E3/E5/E6/E7/E8 retain my initial N reasoning. E1 changes for the concrete existing-carrier choice. E4 remains 1 because assertion-grade source-category coverage is weaker than universally observed effective availability. A alone earns E1/E2=2 by reusing the released requirement/declaration and provisioning machinery; E3=2 assumes bounded native inspection and no pre-admission raw candidate disclosure; E4=0 because its unchanged checker cannot admit an opaque provider; E5=2 because old managers ignore the inert file; E6=1 retains the legacy checker's limits; E7=2 relies on existing closed declaration grammar plus a bounded recommendation convention; E8=1 reflects cold-setup guidance without solving opaque reliance. These are design scores, not claims a governed implementation exists.

N-C/N-C+A is preferred despite the numerical tie with A alone: it addresses the actual opaque-provider goal, whereas a recommendation alone cannot. Under E4's strict exclusion anchor applied to *every client/mode combination*, N-C/N-C+A score 11; neither the tie nor the scoped preference proves universal optimality. Common-case E8 assumes a suitable provider already exists; cold setup and client authentication can take multiple actions.

The concrete limitations adopted from peer clarification are:

- Strict Claude exclusion requires an **actually applied** strict channel over a **nonempty** set, for example managed Y versus required native X. An empty profile alone emits no channel and proves no exclusion (environments §5.8).
- A negative must concern the **same bound provider and launch**. A native-file miss is not authoritative absence for an opaque connector, and an unrelated disabled same-name entry cannot invalidate its separate selector.
- Origin is independent of acceptance: a locked/audited package can still be suppressed, shadowed or missing. A lock is not execution authority or effective-availability proof.
- Assertion never bypasses applicable source, signer, audit, hardened or explicit disable/deny/exclusion gates. Internal opaque-provider drift remains unverified; context change, revocation and authoritative contrary evidence bound reliance. No credential-store inspection is used to close this gap.
- Current managed HTTP output lacks header routing. A compatible native HTTP entry remains useful only in a launch that includes it. Adding an auth label or process env name is not an HTTP serializer capability.
- Native MCP support, manager observation support, and declaration writer support are three different capabilities. Missing writer support alone must not exclude an already usable external provider.

Comparison with astra-03's recorded N vector `[1,1,2,2,2,2,1,2]` is within one point on every row, with E4 the sole retained difference for N-C. I have requested explicit confirmation that its E4=2 claim has the same source-category and launch bounds. The frozen initial N vector also differs by at most one point per row, but its authority carrier was less concrete. This is cross-host evidence available to the convener, not a claim of unconditional zoo verification or implementation conformance.

## Round 2 — scope confirmed across hosts

astra-03 explicitly confirmed the same candidate and boundary at `$kOe1Skk9G9JhTmiB5NR6WNRulSzfx2mVaTf8I6-jbGQ`: source-category coexistence through observed evidence or accepted, labeled reliance in a supported selected launch; no universal effective availability, machine verification, authentication or new client capability. It accepted my stricter E4=1 as a one-point interpretation difference. Its launch-finding acknowledgement is `$8dnCyQGZfFjV7O0beaipNMjxKjWhDqE9CeEZDCVvXWw`.

Thus an actual cross-host pair now exists: this independently initialized Mac mini seat's N-C vector `[1,1,2,1,2,2,1,2] = 12`, and ivmbp astra-03's `[1,1,2,2,2,2,1,2] = 13`, differing only by one point at E4. My published vector is `$RKJQQ3pw4wfBtrQGoZPE2MqssfXEMEstE_v5cTmrbAU`. This meets the mission's row-tolerance condition for the bounded preferred design. It does not prove universal optimality, universal zoo/client/mode availability, closed conformance, or a deployed implementation. The convener owns the collective proof summary and integration.

No new mechanism, confirmed finding or score change resulted in this round. N-C/N-C+A remains preferred; E7 remains 1; the frozen initial scores remain intact. No finding file is needed because both reproduced findings already belong to astra-03. Awaiting convener PARK.

## Round 3 — preserve negative layers and bound diagnostic output

astra-06 independently supplied the OpenCode negative-layer counterexample at `$eYBcS-nMESRK1ys0xtnRMblxOfqF9wHgoV_kDzj7P50`. I inspected the pinned reader and confirmed it at `$3gLOuU_zpyqKhXrTTBjgvnUPNRRrKE7zUy0wy-2Ot98`; astra-06 accepted that cross-host confirmation at `$Kzctr9tXQ_LgZIk5WmtordyZoiv0ClqQxmesJaIE6OU`.

Synthetic case: global native `docs` is enabled; project `docs` has `enabled:false`. `entriesInFile` (`mcp.go:259–269`) discards the project entry before composition; `ConfiguredServers` (`54–62`) then counts the enabled home entry. Under the recorded OpenCode precedence (`environments:1839,1849`), the higher project disable applies to that native provider. **Preserve negative observations until effective precedence is resolved, then determine satisfaction.** Merely reversing positive-map union order cannot restore a discarded negative. A selector naming the lower native surface cannot evade the higher disable; an independently bound opaque connector remains a different provider. This is a discriminating case for the existing launch finding, not a separate finding or runtime reproduction.

I also adopt the no-raw-command clarification supported by manager §6 `1107–1108`, the current leaking warning at `mcp.go:140–145`, and peer confirmations `$BMMBx08uFxUycmtcAf1ZQilO1FY6gBTsU-EVAk8I0y8`, `$5ZtvB0DDPL6HL0hbH3s1KpuNwzFzbZlzTDvQxwBL-F0`, and `$woH4Tj0pbOWRhxLB_2amNCvyXCRv4HHDV2X717_ObdQ`. A static PATH warning is required; echoing native command bytes is not. Amended E3=2 requires fixed diagnostics with validated requirement/target identifiers, no arbitrary command/argv[0], raw foreign label, parser snippet, argv, URL, header or env value. A bare executable string has no automatic secret-free guarantee. The private PATH lookup need not execute the server. A alone's unchanged legacy checker means unchanged satisfaction semantics, not preservation of unsafe diagnostic rendering.

The existing-carrier variant does not mandate a portable marker bump: fresh scoped status can remain local while old `FoundIn` keeps its old meaning. If stronger evidence is later persisted into portable markers, use a governed successor. These sharpenings leave all current scores and preferences unchanged. No new finding file, client probe, build or test was produced.

astra-03 subsequently accepted the OpenCode case for its owned finding at `$-WPmMsTwqDITDwlLnchhPOzpeZDwUvCNbfeRCtPGOkU`.

### Optional recommendation: joint-closure name guard

After astra-04/06's challenge, I independently read `internal/contextresolve/contextresolve.go:313–319,409–419,909–918` at the same curator pin: selection is keyed by name, a later different kind is coerced to the earlier kind, and output has one selected member per name. `internal/contextlock/contextlock.go:245–249` checks duplicates by `(kind,name)` instead. Therefore this is a concrete resolver reuse limitation, not a newly established normative ban on multi-kind lock members. Peer confirmations: `$cjkXXsAKqa1RgA871RL9IIK9QBe3kTfn9G17XP4UnYU`, `$DXLx6b3LVuLDCnJ_1jDtgxYMXNQ3NEp521MCqE3HO2k`, `$1Uj9zxzz0wmHbD4iJjYkjpbASv09rvAbuFNPL6jO1YQ`.

A/N-C+A's current scores assume the corrected recommendation path: use authored distinct package names when skill and MCP both enter one closure, or report/defer the colliding adoption plan. For example, skill `docs-skill` requires MCP `docs-mcp`, and its co-located declaration is named `docs-mcp`. A alone still needs declaration/configured name equal to the requirement label; it cannot borrow N-C's alias mechanism. No automatic rename, resolver rewrite or extra install authority follows. Existing external fulfillment remains available even when this recommendation cannot be adopted. N-C itself is unaffected; optional A is bounded convenience rather than a universal provisioning mechanism.

## Round 4 — explicit trust grade; no score change

astra-03's `$1OwD97M9qTzcB8uGSBb7Jmc1QNktZ0ZFkRVr0wLiBE4` states the same honest-failure premise I use for E6=2: a project entry proves configured presence, not admission through a native trust gate. Keep legacy §6 and its checkout-trust warning unchanged. In the opted-in selected-launch lane, known denial/exclusion is negative; unobserved trust is unknown/pending unless policy admits explicit scoped operator reliance, which remains asserted and never grants native approval. Render evidence source and grade, plus **configured by name / provider identity and authentication not checked**. No bare ready/satisfied rendering, new trust probe or automatic fatal profile gate is implied. The concrete invocation and aggregation grammar remain E7=1 work.

The optional recommendation's remediation must identify canonical source, exact revision, normalized directory, declaration name and compatible destination. Adoption is an independently selected and pinned provider; a later skill recommendation change is not automatic provider drift or an obligation to update it. These are bounds on A's existing provisioning reuse, not extra monitoring or authority.

No new finding, score or preferred-design change in this round. My attribution query `$ml-ERI9H_OqLk860PphjXSBnqGMukDSs27fBQHpLxcs` was resolved by wonder-12's correction `$gaPvBPCZ2BHxf2bbhCCyOzC6ytV98oYNuY57v6HSdU4`, acknowledged at `$_kHe3kSZc1hjABrfm1sG9_48mllCW7NCn80Uek3ux2k`; the corrected-away marker is not evidence for this verdict. No unanswered peer request remains for this seat.

## Rounds 5–6 — quiet preferred design; correct A-alone E7

Round 5 was quiet (`$ReZHauUSHqHbCirrxpVfPjBmD_FdljlPpi2cGB4dy5w`). The subsequent optional-A clarification at `$hKtj6U7xrnori2tj3Kux8CPOM6OoWY1HhVtumWKoax4`, acknowledged by wonder-11 at `$wrTpvGC3T5YkfUOfMFRe7JOjlBYkPwTgVBOmzNcyPZM`, made one remaining contract gap explicit. I independently re-read manager §7 `1113–1130,1167–1171` and environments §9.1 `2301–2325`: the mandatory `context-secret-material` addition and unconditional strict mode are specified for profile context/MCP snapshots, not explicitly for an ordinary skill-root recommendation read. Corrected A needs an explicit skill-lane declaration audit scope, severity/waiver/admission rule, and value-free diagnostics. It must not silently import always-strict profile behavior or make malformed optional metadata a new install failure. Pre-admission output remains safe metadata regardless of scan results; later adoption independently passes the MCP gates.

Path-sourced skill declarations remain informational only: environments §2.2 `551–559` forbids path-kind MCP members, so do not print a supposedly executable existing-profile adoption recipe for them. A separate native/manual extension must identify itself as such.

I therefore correct my **A-alone E7 from 2 to 1**: an existing declaration grammar alone does not close the new discovery/audit contract. The round-1 comparison table is retained as history, not silently rewritten. Current A-alone vector is **`[2,2,2,0,2,1,1,1] = 11` amended, 9 original**. This is an alternative-score change, not a new finding or preferred-design change. N-C and N-C+A already had E7=1 and remain **12 amended / 10 original**. Optional A is not necessary for N-C's dependency/evidence mechanism.

### E3 scope at the legacy provisioning boundary

The profile waiver at environments §9.1 `2305–2319` changes admission, not the admitted bytes. The §2.3 row (`562–591`) and `contextmaterialize.FormatDeclarationRows` (`152–175`) still serialize stdio args, and §5.8 materialization copies args/URL. These previously inspected clauses support the subsequently confirmed counterexample: a waived credential literal is not sanitized by strict admission. The current HTTP surfacing row has no URL column, so this is not an allegation that it currently prints URL. Confirmations include `$AM4igYxULdLF11cnYRkV8pM2jgUsLQRZfcqMly7lufI` and `$7xAqOx7_rd6ZhqDV7GluuciCFXbjrKXgKHwWdGcHgeQ`.

My amended E3=2 applies to the **proposed bounded dependency path**, not all existing profile installation or launcher behavior. Keep recommendation/evidence output metadata-only independently of admission, withhold sensitive display details, and refuse credential-bearing materialization/forwarding under this feature's no-use/no-store/no-forward promise. A waiver is neither disclosure authority nor a bypass of that boundary. If withholding prevents meaningful exact-plan review, the proposed write remains unapproved. A clean detector result is not a proof of secret-free arbitrary strings. An explicit handoff to legacy provisioning must state its narrower guarantee rather than inherit the feature's end-to-end E3 score.

Changed §2.3 display or §5.8/§9.1 admission/materialization behavior requires governed compatibility and vectors. This sharpens existing E7=1 work; no new auth field, broker, finding file or score change follows. Existing native configurations remain eligible for bounded read-only evidence in a launch that actually includes them; foreign values are never reproduced by the dependency checker.

## Final disposition on PARK

The convener `ivmbp_curator_orch` issued PARK at `$YGuiFoIqq0SqOg9WywpBf6YwJiuYSmO6w52P8Y0AVJA` (2026-10-14T00:16Z), after two quiet rounds. This closes the review and the pending coordination request. No new debate or score change follows that marker.

| Final candidate | E1 | E2 | E3 amended | E4 | E5 | E6 | E7 | E8 | Amended total | Original total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N-C, preferred | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | **12/16** | **10/16** |
| N-C+A, optional convenience | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | **12/16** | **10/16** |
| A alone, corrected | 2 | 2 | 2 | 0 | 2 | 1 | 1 | 1 | **11/16** | **9/16** |

The frozen B/R/N baseline and the disclosed design refinements remain above. Original E3 is 0 for these native-reading candidates. Amended E3=2 is conditional on the bounded dependency path, including its diagnostic, display and provisioning limits; it is not an inherited guarantee of general legacy profile behavior.

The last pre-PARK astra-03 publication, `61fbd1336feb253b1199aa21235b58008c44efdc`, and quiet-round confirmation `$zHbfi6FJfgmvNGh__PQR4-AvimDgtu7sJlLGNZD6Bk4` retain N/N+A13 amended/11 original, A-alone11/9 and E7=1. Our preferred-design vectors still differ only at E4. The explicit cross-host confirmation recorded in round 2 therefore remains valid for the bounded candidate; it does not prove every provider/client/launch combination works.

The decisive zoo limits remain: opaque providers cannot yield machine-observed presence without an available client metadata surface; a missing or excluding launch channel cannot be repaired by an assertion; native presence must preserve precedence, negative layers and trust grade; and managed HTTP header routing requires a real declaration/serializer capability. Some cases permit a compatible native route or a manager change. They do not establish that every zoo member can satisfy every selected launch without a client capability change.

No addressed design exchange remains open. Confirmations stay with the existing finding owners; this seat created no duplicate finding file. Open governance and implementation work is listed in `mcp-deps/parked/astra-13.md`. Final artifacts are submitted to the convener for signed integration under the mini-seat attachment route; this seat does not push shared main.
