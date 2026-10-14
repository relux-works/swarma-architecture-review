# astra-04 — independent spec-fit and minimality verdict

Seat: `ivmbp_swarma-mcp-deps_astra-04`, second independent five, ivmbp.
Date: 2026-10-14. State: final, parked after the convener's 00:16 UTC disposition.

PARK event: `$YGuiFoIqq0SqOg9WywpBf6YwJiuYSmO6w52P8Y0AVJA`, from
`ivmbp_curator_orch`. No addressed review exchange remains unanswered.
Subsequent specification work is recorded in the [parked handoff](../parked/astra-04.md).

**Final recommendation:** prefer N, the named-requirement and protected
operator-evidence design; corrected skill-shipped declaration discovery A is
optional. N/N+A scores **[1,1,2,2,2,2,1,2] = 13 amended / 11 original** for an
already suitable configured provider, or **12 amended / 10 original** for cold
setup. Discovery-capable A alone scores **11 amended / 9 original**; an inert
authored file with manual adoption is a distinct, narrower variant.

These are conditional scores for a proposed corrected contract, not a claim
that current Curator implements it. **E7 remains 1:** scoped invocation,
authority, negative evidence, invalidation, ordinary-skill audit and the
waiver/display/provisioning boundary require governed specification work.
The independent initial tables and every later correction remain below.
The additional peer-confirmed finding owned by this seat is
[same-name skill/MCP closure collision](../findings/f-cross-kind-name-collision.md).

## Independence and evidence boundary

The independent initial table and initial preference below were formed before
reading any first-five verdict file or debate body. The mandatory onboarding
`a2a topics` exposed topic
titles, not their arguments. The evidence read was the complete mission,
base, all three inputs, and the local specification and implementation.
No web, credential reads, source edits, builds, or runtime tests were used.
The source clones are read-only under this seat's sandbox; they were not
updated. Evidence pins:

- curator-spec: `a9c03be237b723b5bf87aed070165ad6f68b2586`.
- curator: `5234cf38833554542e68afade15951c6e56ed89e`.
- Base and inputs: this review repository as initially pulled.

Normative evidence outranks an implementation or an accepted CIP. In
particular, GOVERNANCE.md says CIP acceptance does not amend released prose,
schemas, or vectors; CIP-0006's adopted direction is not shipped MCP policy.

## Candidates and independent scores

**B — base as written:** Require / Provide / Bind, including skill-side
package or endpoint identity, recipe equality, aliases, optional provisioning,
and declaration auth classes.

**N — named requirements, operator-selected providers and evidence:** retain
the existing portable skill requirement; use existing declaration packages and
profile resolution for optional operator provisioning. Add one protected
machine-configuration binding map only where a native label differs or a
provider is opaque. Its records are explicitly new evidence/authority, not
existing machinery disguised by a small JSON diff. A record is scoped to the
requiring skill source, logical requirement, target client/configuration
instance, and native versus managed launch context. It identifies either an
observed provider label or an operator assertion of an opaque provider.
Package acquisition identity remains in the existing provisioning lane.

The effective result distinguishes observed configuration, explicit operator
acceptance, absent/disabled, and unknown. An assertion is never printed as
observation or authentication, cannot defeat a known disable or strict-channel
exclusion, and is not written by a repository. It is invalid outside its
recorded scope or after observable context changes; invisible provider changes
remain an explicit limitation of operator assertion. Any/all quantifies over
the originally selected targets, never a filtered capable subset. Legacy
manager §6 behavior is retained as a separately identified static check;
stronger effective-launch claims require their own governed contract.

**I — repaired identity base:** N's evidence, launch and authority rules plus
a versioned, closed skill identity selector. It separates endpoint identity,
package provenance and explicit binding; command/args equality never proves
provenance. It adds a governed declaration auth extension only if independently
needed. This is viable, but carries more contracts than the owner's goal needs.

**C — context-package-only provisioning:** leave skill name requirements
unchanged and provision only existing profile `requires.mcp` packages; do not
add bindings or opaque-provider evidence. This is a useful bounded deployment
pattern, not a solution for the entire zoo.

| Row | B | N | I | C | Evidence and justification |
|---|---:|---:|---:|---:|---|
| E1 New concepts/fields | 0 | 0 | 0 | 2 | B adds an identity union, alias/binding authority and auth grammar, not merely one field. N honestly budgets a new binding/evidence record family; I adds still more. C adds no wire object. Core §4; common.schema.json:610–642; environments §2.2. |
| E2 Reuse | 1 | 1 | 1 | 2 | B/N/I reuse declarations, materialization and audit, but all need new evidence/binding machinery. C uses existing profile resolution unchanged. Environments §§2.2, 5.8, 6; internal/envprofile/managed.go:205–226. |
| E3 Secrets, amended | 1 | 2 | 2 | 2 | B's foreign-config parsing bound is unstated. N/I/C explicitly limit foreign bytes to private bounded parsing, emit names/state only, perform no auth or health request, and never retain raw native argv/URL/env. internal/mcp/mcp.go:245–283 proves generic native parsing already occurs. Environments §§5.8, 10.3 separate manager metadata from launcher value transport. |
| E4 Zoo | 1 | 2 | 2 | 0 | B requires client reporting it has not established. N/I provide explicit scoped operator evidence for opaque providers, without claiming discovery. C excludes opaque external satisfaction and forces provisioning into its one lane. Environments §7.8; manager §6. |
| E5 Portability | 2 | 2 | 2 | 1 | B/N/I preserve a client-neutral manifest; machine-local decisions remain local. C makes complete fulfillment depend on the optional environments capability, although managers may conform without it (environments preamble). |
| E6 Honest failure | 1 | 2 | 2 | 2 | B leaves unknown/any and effective-launch visibility open and its explicit binding has no authority/freshness contract. N/I keep negative and unknown states, quantify actual selected targets, and require consent before every provisioning or binding write. C can truthfully refuse unsupported external cases. Manager §6; environments §§7.8, 10.2; csk proposal §§2, 4. |
| E7 Specifiability | 0 | 2 | 2 | 2 | B has no closed identity/binding grammar, range-lock ownership or version path. N's finite evidence states and context-qualified matching admit concrete vectors; I is specifiable only with additional versioned contracts. C is already specified. COMPATIBILITY.md:17–24; GOVERNANCE.md:7–19,75–80. |
| E8 Operator effort | 1 | 1 | 1 | 0 | Existing configured cases need zero actions; first-use provisioning, env admission and client auth can require several. No prevalence data establish a common-case 0/1-action claim. C requires manual repackaging/wiring for external providers. csk proposal §§2,5; environments §§2.2,10.3. |
| **Total, amended** | **7** | **12** | **12** | **11** | N/I tie on the deliberately coarse rubric; N has fewer concrete new contracts. |

Under **original E3**, all candidates that inspect native configurations score
**0**, including N/I/C when retaining manager §6. Original totals are B **6**,
N **10**, I **10**, C **9**, and none qualifies as elegant under the original
no-zero rule. The amended E3 makes explicit, bounded foreign-byte handling
eligible. These are design scores, not claims that today's implementation
already enforces that bound. In particular, unbounded `os.ReadFile` is not the
proposed bounded reader.

## Preferred design and smallest change set

Prefer **N**, with a tie rather than a claim of unique numerical victory.
The owner's first requirement already exists: core §4's required `hint`,
documentary `transport`, and `required_in:any|all`. Adding package identity to
the portable skill is unnecessary to let an operator fulfill that dependency.

1. Remove `server.package` and `server.endpoint` from the minimum skill change.
   Keep the existing manifest bytes and the documentary transport semantics.
2. Replace separate aliases plus identity fallback with one protected,
   context-scoped provider binding/evidence mechanism. A project file may
   propose a binding, never authorize it. Report assertion as assertion.
3. Keep acquisition, allowlist, signer policy, consent and runtime auth in
   their existing distinct lanes. A package pin is not runtime identity.
4. Define foreign-byte bounds and sanitized outputs. The manager neither
   reads dedicated credential stores nor evaluates secret references; the
   native client performs auth and the launcher may pass authorized values.
5. Evaluate any stronger availability claim in the selected launch context.
   Keep the old manager §6 check identified as static presence. Native files
   excluded by Claude strict MCP cannot satisfy a managed-launch claim.
6. Govern the new binding/configuration and evidence semantics through a CIP,
   decision, new affected schema versions and positive/negative vectors. Do
   not edit the shared `mcpRequirement` definition in place: v5–v8 depend on it.
   Leave declaration auth classes out unless their own use case needs them.

## Adversarial vectors derived independently

| Input/counterexample | Required conclusion |
|---|---|
| v5 manifest receives `server` | Old closed schema rejects; an optional field cannot be retrofitted into old bytes. |
| Two packages have identical command/args and different `env_names`, selectors or origin | Recipe equality does not establish package provenance or runtime executable identity. |
| Native Claude `.mcp.json` contains `figma`, managed channel contains another set | Static native presence may pass the legacy check; managed availability must not pass. |
| Targets are Claude and an unsupported/opaque client, `required_in:all` | Do not drop the latter from the denominator. Without accepted scoped evidence, result is unsatisfied/unknown. |
| `any` sees one positively configured target and one opaque target | Overall any can succeed because of the positive target; the opaque target remains unknown. |
| Repository proposes a binding that already has the required name | No authority follows from spelling or a project-local approval file. |
| HTTP endpoint stays equal while a native entry becomes disabled | Identity equality does not defeat disabled state. |
| `auth:none` HTTP publication | Base consent rule still requires consent; csk owner decision D1 is a different extension rule, not a spec-wide exemption. |
| Same endpoint is exposed by a connector and a local package | Alternative fulfillment needs no claim that the connector came from the package. |

## Contract homes and implementation map

- Core §4 and `schemas/v1/common.schema.json`: **no change for N**. An I
  extension needs a new manifest node/version; draft v9 is not assumed free.
- Manager §§1,6 and the next available manager/system configuration schema:
  binding authority, scope, evidence vocabulary and pure verification rules.
  Existing marker `FoundIn` must not silently relabel operator assertion as a
  server observed on disk.
- Environments §§2.2,5.8,7.8,10.2–10.3,12: reuse package and launch channels;
  document how managed evidence joins the checker, not native in-place writes
  into a managed home. Auth metadata, if added, belongs to a separately
  governed declaration revision, not schema-1 package bytes.
- `internal/mcp/mcp.go`: current native name union, read states and result
  provenance are the checker seam, not a place for installing or logging in.
- `internal/envprofile/managed.go:205–226,2436–2457` and
  `internal/contextmaterialize/mcp.go`: already expose resolved declarations,
  channel set and env names; consume their provenance rather than rediscover
  generated files as if they were unrelated native sources.

## Round record

- Independent round 1: the scores above were frozen locally before opening
  first-five verdicts. No peer-confirmed finding file has been authored yet.

## Adversarial comparison after the independent freeze

The initial table is preserved above, signed before peer reading in local
commit `7fffa30`, then signed again after rebase and published as `ebdc698`.
Room freeze event: `$gTvTSooKcOKvtSeKCW7ECYSPKezTm6j9dSp-dVr392M`.
Only afterward did I read astra-01 and the relevant debate bodies.

The first-pass defense of N survives my recipe/provenance, old-schema and
strict-channel counterexamples. Its explicit distinction between an inert
recommendation and authority also survives the csk D1 conflict. I independently
confirmed the schema finding in `$T_QPlXpIGmdMnzwkPeMR6NVRyMAR5IdGLrCPoarg0Bk`.
This confirms a finding; it is not runtime qualification.

Three score qualifications matter when comparing **the same concrete N**:

- E1 becomes **1** if records live in a successor of the existing manager
  configuration family, and scoped results are computed transiently. My initial
  0 explicitly counted a new evidence-record family. A portable marker bump is
  not necessary unless stronger acceptance is persisted there; old `FoundIn`
  retains its legacy meaning. Configuration nesting is not zero semantic cost.
- E7 becomes **1**, correcting my initial over-credit: finite result states and
  possible vectors do not yet close the configuration grammar, policy precedence,
  launch-completeness table, scope selection and invalidation contract. Governance
  is known; the closed contract is still work to do.
- E8 is **2** for the now explicitly bounded comparison case of an already
  suitable configured provider: zero actions for observation, one enumerated
  batch for operator reliance. It is **1** for cold setup and is not a claim
  about the measured frequency of either case. Auth remains separate.

Thus the refined existing-configuration N is **[1,1,2,2,2,2,1,2] = 13**
under amended E3, **11** under original E3. Cold-setup amended total is **12**.
This matches astra-01's same-design vector. Even the frozen independent N table
differs from astra-01 by at most one on every row. The mission's independent-five
agreement condition is therefore satisfied for this scoped preference, without
claiming a universal optimum, normative adoption, or a proven implementation.

E4=2 means coverage of provider categories through supported observations or
explicit assertion-grade reliance. It cannot supply a missing client capability,
defeat an applied strict channel, or turn an incomplete observation into proof.
The strict Claude example needs a present, actually applied channel; an empty
profile set produces no §5.8 file and does not itself establish exclusion.

### Additional serious alternatives examined after freeze

| Candidate | E1 | E2 | E3 amended | E4 | E5 | E6 | E7 | E8 | Total | Original E3 / total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Refined N, existing config + transient status | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | **13** | 0 / 11 |
| Repaired identity base I, still requiring new identity contracts | 0 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | **11** | 0 / 9 |
| A: inert skill-shipped schema-1 recommendation, legacy checking | 2 | 2 | 2 | 0 | 2 | 1 | 2 | 1 | **12** | 0 / 10 |
| A+N with explicitly selected, valid existing-package adoption | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | **13** | 0 / 11 |
| T: exact tool-name requirements without manager probing | 1 | 1 | 2 | 1 | 1 | 1 | 0 | 1 | **8** | 0 / 6 if native parsing retained |
| G: manager-owned authenticated MCP gateway | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | **4** | 0 / 4 |

A reuses the grammar in environments §2.2 and can remain inert in an old skill
snapshot (core §§3–4), so E1/E2/E5/E7=2. Its legacy §6 evidence cannot cover opaque
providers or the managed-launch universe (E4=0/E6=1); operator adoption still
needs an existing context-root route (E8=1). A+N pays N's full contract costs.
This is optional discovery convenience, not a reason to delay N or silently
expand package authority. Admission, exact commit selection and the schema-1
HTTP header limitation remain unchanged.

T needs a new manifest lane and inventory machinery (E1/E2=1), while §6 and
`internal/mcp` only provide configuration metadata. Exact strings do not prove
semantic equivalence, and no current trustworthy cross-client inventory is
established (E4/E5/E6/E8=1, E7=0 for the proposed semantic satisfaction contract,
not merely because strings lack a central registry). No live tools probe keeps
amended E3=2. G introduces a runtime/auth service (E1/E2=0), handles credentials
(E3=0), and has no route to opaque client-owned connectors (E4=0). Its remaining
rows each require new operational contracts (1); it is disqualified by E3.

### New adversarial case: same-name co-location is not dual-kind adoption

Question to astra-01/wonder-01/wonder-03:
`$iUc_uDX_kiEwtByLrYzC4qpzhIODJGkvPXIehrKehkk`.

At curator `5234cf3`, `internal/contextresolve/contextresolve.go:316–317`
indexes selected kinds and constraints by name, and `add():409–420` coerces a
second kind to the first. `build():907ff` emits one selected member per name.
`internal/envprofile/gitsource.go:721–755` constructs then sorts requirements by
name/kind; `Manifest():238–275` loads only the chosen kind. Finally,
`internal/envprofile/managed.go:205–226` emits only MCP-kind members.

Therefore a root selecting `skills.docs` and `mcp.docs` at identical source and
revision cannot be assumed to install both kinds just because both manifests
coexist in the snapshot. This is a source-derived implementation constraint,
not a runtime result or a claim that the normative spec explicitly forbids
dual-kind lock rows: lock validation itself keys uniqueness by `(kind,name)`.

Minimal A qualification: use distinct skill and declaration package names in a
joint closure, or defer that colliding adoption case. Do not silently invent a
rename, alias or kind-aware resolver and count it as free reuse. N remains
unaffected. Astra-06 independently confirmed in
`$cjkXXsAKqa1RgA871RL9IIK9QBe3kTfn9G17XP4UnYU`; the bounded finding is
[f-cross-kind-name-collision](../findings/f-cross-kind-name-collision.md).
It also qualifies BASE's optional package adoption, not just A. No score
changes follow for N or for A explicitly limited to valid distinct-name plans.

### Round 2: peer confirmation and remaining operation debt

Astra-03 and macmini astra-11 independently confirmed the collision in
`$1Uj9zxzz0wmHbD4iJjYkjpbASv09rvAbuFNPL6jO1YQ` and
`$BIEX51HEpPOjmdCu2W4Jqe6E30o-ZwYezdmjyAyknRw`. A without N needs distinct
skill versus MCP package names while retaining declaration/requirement label
equality. An optional recommendation that cannot be adopted must not introduce
a new failure for an otherwise valid skill installation.
My first-pass mirror astra-01 confirmed the same constraint in
`$lP6CQBaniPOuAFcEbUe44hVA_zZSRNMypI_-miaCx-s` and accepted it into the defended
optional-A design. The source-derived challenge has therefore been adjudicated
without expanding the implementation scope.

Wonder-03's three challenges at
`$LhiQrl1xcV4aSfL927TfTRhlk3xPcBmd9K66MLUnzPQ` led to these conclusions:

1. **Refute mandatory stale-adoption tracking.** An inert candidate is pinned
   by the skill snapshot; its operator-selected adoption is independently
   pinned. Environments §1.3:198–204 explicitly forbids implicit re-resolution.
   Skill C2 does not invalidate an independently selected C1 provider merely
   by shipping a newer recommendation. Correct the headline instead of adding
   a mandatory coupling mechanism. Optional update advice remains separate.
2. **Confirm the full remediation tuple:** canonical source, exact commit,
   directory (root explicit) and declaration name. Dropping a package directory
   prints a wrong recipe; preserving existing metadata adds no identity matcher.
3. **Confirm scoped invocation is new work.** `internal/install/install.go:1582–1605`
   calls the verifier with roots/agents/scope only and translates it to legacy
   found-agent lists. No selected launch context exists in that interface.
   The new scoped check needs an explicit opt-in and invocation/operation
   contract; do not silently introduce a new rejecting profile-install gate.
   A portable marker remains optional. This reinforces E2=1 and E7=1.

No new score or preferred-design change in this round. The distinct-name
qualification narrows A adoption; it does not broaden N or authorize code edits.

## Final candidate qualifications

The preferred N contract must render evidence source and grade together:
**configured by name; provider identity and authentication not checked**, or
**operator-asserted** for protected reliance. It does not prove the publisher,
author-intended service, executable bytes, endpoint control or credential
recipient. Requiring cryptographic provider identity would be a new product
requirement and would reopen the comparison with I.

Legacy manager §6 can pass project-only presence with its checkout-trust
warning; that legacy meaning remains unchanged. In the opted-in selected-launch
path, project-file presence alone does not establish client trust admission.
Known denial, disable, exclusion or authoritative conflicting evidence defeats
acceptance. Unobserved activation/trust is unknown or pending; any permitted
protected reliance must be labelled asserted and cannot grant client trust or
override a known refusal. A bare unqualified satisfied/ready variant does not
earn my E6=2. This is the same bounded candidate, not a new permission broker.

I support the explicit minimum entry point stated by astra-01 in
`$gcv0kHyXcSU3qkCxjlZdR65CIYk9B8a4ftQTrRD02sU`: opt into selected-launch
verification at the existing skill-install requirement gate. A requested pure
recheck may consume existing profile evidence; automatic profile-install or
resolve failure gates are not implied. Invocation grammar, context authority,
system policy and conformance vectors remain E7=1 work. No mandatory portable
marker or ongoing recommendation/adoption coupling is added.

Wonder-03 accepted my stale-adoption refutation and scoped-operation response
in `$PJ6GTg85XxkaX_L2_pqYCtZgLj4zhBW0zrl9UPe53l8`; I acknowledged in
`$RrNH9rHNuRv9t637R55EkCno8Kw2V7akgbFDqOoSfj0`. Root directory is explicit in
human guidance but uses the existing absent-directory wire encoding, not a new
literal selector. Mandatory source/grade/project-trust wording is also the
condition astra-01 restated in `$HnQx55ESGlKJve3rRFkDGFGlk152er2pU3iDqayvjsY`.
These clarifications leave my current N/N+A score at **13 amended / 11 original**,
with **12 amended for cold setup** and no runtime certification claim.

### Optional-A discovery and audit qualification

I independently confirmed astra-01's later clarification in
`$hKtj6U7xrnori2tj3Kux8CPOM6OoWY1HhVtumWKoax4` against the same source pin.
Environments §2.2:551–559 refuses a path-kind MCP closure member. A declaration
inside a path-installed skill can therefore be informational only; it must not
be presented as an executable recipe for existing profile adoption. Separate
manual/native provisioning is a different lane.

Manager §7:1167–1171 and environments §9.1:2302–2319 require the
`context-secret-material` detector for profile/context-MCP snapshots. They do
not explicitly impose that declaration-specific detector on an ordinary skill
root. A manager feature that discovers and advertises a skill-root declaration
needs an explicit audit scope and value-free diagnostics, with its ordinary
skill-lane severity, waiver and admission semantics stated. It cannot silently
inherit unconditional strict profile admission or turn malformed optional
metadata into a new skill-install failure. Pre-admission output remains safe
metadata only; actual MCP adoption independently passes existing profile gates.

This narrows the meaning of my A-only table row: **12 amended / 10 original**
is the inert authored file plus existing manual adoption and legacy checking,
whose declaration syntax is already specified. For **manager recommendation
discovery plus the unclosed skill-audit extension**, E7 is **1**, giving
**[2,2,2,0,2,1,1,1] = 11 amended / 9 original**. Syntax reuse does not make
the whole new discovery contract specified. Neither form covers the full zoo.
Preferred N and optional A+N remain **13 amended / 11 original** because their
E7=1 already budgets unfinished operation and scope contracts. This is a
disclosed qualification of an alternative, not a new finding or preference.

### A waived audit finding is not safe-output or provisioning authority

I independently checked the counterexample raised by astra-02 in
`$xSGO0qksc8B68V1gr6rmjfakIF3nxsK27zIAdmV0LoE`, confirmed by astra-12 in
`$sFmAXQMAuzn5Db3lOZF9tyvCs01HohyDX9ODh4NqCSI` and extended to materialization
in `$lUSbVgBMWBhdEhk31UaFQqExiNO7W6fGl3S57ebwsqE`.

At the pinned spec, `agent-mcp-v1.schema.json:19` admits arbitrary bounded
argument strings; its HTTPS syntax also does not certify a secret-free path.
Environments §9.1 permits an exact pin/file/span secret-material waiver, while
§2.3:562–592 requires raw stdio argument surfacing after successful admission.
`internal/contextmaterialize/mcp.go:152–175` implements that output. The current
HTTP row has no URL column: this is not an allegation of a current URL-row leak.
The serializers at `mcp.go:244–327` do copy stdio args or HTTP URL into generated
configuration, so redacting stdout alone does not address value reproduction.

Admission, safe presentation and safe provisioning are separate predicates.
A waiver neither sanitizes the bytes nor authorizes disclosure, persistence or
forwarding of a credential value under amended E3. Known or waived sensitive
details must remain withheld; value-bearing provisioning must be refused or
deferred within the stronger feature. If withheld details prevent meaningful
exact-plan consent, the new mutation remains unapproved. No detector-completeness
claim follows from an absent finding.

Pure N observation and protected assertion need no such value reproduction.
Optional provisioning can earn E3=2 only with an explicit governed boundary;
unchanged delegation to legacy provisioning cannot inherit the stronger claim.
Any conflict with existing §§2.3,5.8,9.1 requires a governed correction, not a
silent compatibility exception. This is existing E7=1 work and corroborates
`f-secret-boundary`; no new finding, auth field or runtime evidence is claimed.
