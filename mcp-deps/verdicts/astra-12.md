# macmini-astra-12: adversarial authentication and trust

Seat: `macmini_swarma-mcp-deps_astra-12`. Optional third, cross-host pass.
Date: 2026-10-14 (Asia/Tbilisi). Initial score checkpoint: 2026-10-13 22:11 UTC.
Status: final following convener PARK, 2026-10-14T00:16Z; initial scores preserved.

Canonical artifact path is now `mcp-deps/verdicts/astra-12.md`, following the
convener's newer directive `$5e4rLfiQwYQ5pZXEE51i58nVI995XCRbNJhavrTs97I`.
The original content was saved under the approved `macmini-astra-12.md` name,
then moved without changing its bytes or overwriting another seat's file.

## Final recommendation

Prefer **N: existing named requirements with protected operator evidence**.
Optional declaration discovery (A) is separable and does not supply authority.
The current N/N+A vector is `[1,1,2,2,2,2,1,2]`: **13/16 under amended E3,
11/16 under original E3**. Cold setup scores 12/10. Base B0 remains 7/6;
corrected identity base B1 remains 10/8. Richer standalone A is now 11/9 after
the explicit E7 correction below. Profile-only P excludes required provider
categories; its initial scores and later E3 qualification remain below.
Earlier tables remain as dated score history, including my independent initial
judgment, rather than endorsements of unchanged existing implementations.

These are conditional design scores, not implementation qualification.
Amended E3 requires bounded private parsing, safe projection and diagnostics,
and refusal of secret-value reproduction under the proposed guarantee. E6=2
requires status to name its evidence source and grade, including **configured
by name; provider identity and authentication not checked**, or explicit
operator reliance. Project-file presence alone does not establish client trust
or inclusion in the selected launch. E4=2 covers provider categories in
supported capable launches; it does not claim universal client/mode support.

The minimal entry point is an opt-in selected-launch path in the existing
skill-install checker, preserving legacy behavior. It does not impose an
implicit fatal gate on profile install or resolve. Protected reliance uses a
governed successor of existing configuration; status can be transient. A
portable marker successor is required only if a concrete consumer needs it.
Exact invocation, schemas, authority/invalidation rules, compatibility and
conformance vectors remain **E7=1** work.

The cross-host score comparison with astra-02 is recorded below. It supports
the collective's rubric comparison, not universal optimality or a runtime
proof. All challenges addressed to this seat are answered. The convener owns
integration and the collective synthesis.

The final quiet-round record is
`$3qKwqxd90nvi1Nr-hTn--inrRQmQJa6A200cDrmu2vw`. Convener
`ivmbp_curator_orch` issued PARK in
`$YGuiFoIqq0SqOg9WywpBf6YwJiuYSmO6w52P8Y0AVJA`, declaring the two-quiet-round
criterion met. This finalization changes no score, scope or preference and
opens no new debate. Remaining normative work is recorded in
[`parked/astra-12.md`](../parked/astra-12.md).

## Independence and evidence boundary

These initial scores were formed and saved before reading any other seat's
verdict file or substantive review thread. I read the mission, base, all three
inputs, the cited specification sections, and implementation source. I listed
room topics for onboarding but did not consume their arguments or score tables.
No builds, tests, native clients, authentication probes, or Curator commands
were run. Specification statements about client behavior are cited evidence,
not my reproduction. No cross-host proof is claimed by this initial artifact.

Read-only checkpoints:

- review repository: `b5e7dabf6f548e727a9933e2e6371d7b6a0d83f7`;
- curator-spec: `a9c03be237b723b5bf87aed070165ad6f68b2586`;
- curator: `5234cf38833554542e68afade15951c6e56ed89e`.

## Initial independent scores (retain unchanged)

All columns describe designs, not implementation qualification. E3 uses the
amended rubric; the original score is recorded below. E1 counts the whole
design, including protected authority records, rather than only skill fields.

- **B0 — base as written:** Require / Provide / Bind, including package/endpoint
  identity, optional provisioning, and project-or-machine aliases.
- **B1 — corrected identity base:** retain `server`, but require exact package
  provenance or explicit operator assertion, protected bindings/consent,
  launch-scoped evidence, bounded parsing, and versioned auth/identity grammar.
- **N — named requirements, operator-selected providers:** keep skill grammar;
  put acquisition and trusted mappings in protected operator policy. Existing
  profiles/native configuration supply providers. Optional opaque-provider
  assertions are scoped operator statements, never observed identity/auth.
  Requirement checking remains pure; any provisioning is a separate approved
  operation under existing source, MCP package, signer, and audit gates.
- **P — profile-only providers:** use existing `requires.mcp`/declaration
  packages as the only recognized provider lane, with no native/cloud evidence.

| Row | B0 | B1 | N | P | Evidence and reason |
|---|---:|---:|---:|---:|---|
| E1 concepts/fields | 1 | 0 | 0 | 2 | B0 adds `server`, aliases and auth metadata despite its one-field claim. B1/N explicitly add protected evidence/authority records, counted conservatively as an object family. P uses existing objects. `common.schema.json:609–619`; environments §§2.2,12.1. |
| E2 reuse | 1 | 1 | 2 | 2 | B0/B1 add cross-provider identity matching in addition to existing acquisition. N/P keep acquisition in existing machinery; N adds policy evidence, not another resolver or launcher. Base layers 1–3; environments §§2.2,5.8,9.1. |
| E3 secrets | 1 | 2 | 2 | 2 | B0 forbids values but does not bound native parsing or comparison. B1/N impose the bounded metadata contract below. P consumes audited declaration metadata and emits names, not operator values. `internal/mcp/mcp.go:245–302`; environments §§2.2,5.8,10.2–10.3. |
| E4 zoo | 1 | 2 | 2 | 0 | B0 leaves opaque-provider evidence unresolved. B1/N accept supported effective configuration or explicit scoped operator assertions without client changes. P excludes native-only/plugin/cloud providers. Base known open points; environments §7.8. |
| E5 portability | 1 | 1 | 2 | 1 | B0/B1 package locator or endpoint selects one distribution/deployment, requiring override for an equivalent differently hosted service. N leaves that machine choice to operator policy. P requires the optional environments capability. Environments preamble; core §4.4. |
| E6 honest failure | 1 | 2 | 2 | 2 | B0 requires consent and honest auth status, but leaves unknown, project authority and identity equality ambiguous. B1/N define non-satisfying unknown and protected exact-plan consent; P can refuse unsupported providers honestly. Manager §6; input design §§1–2,4–5. |
| E7 specifiability | 0 | 1 | 1 | 2 | B0 lacks closed alias/auth/identity grammar and version home. B1/N can be vectored but their new evidence records remain a specification task. P reuses closed existing objects. Compatibility policy; governance decision-record rule. |
| E8 operator effort | 1 | 1 | 1 | 1 | Already configured supported providers need no action. First provisioning/opaque evidence/auth setup may require more than one action; GUI environment delivery is not universally automatic. Input design §5. |
| **Total /16** | **7** | **10** | **12** | **12** | P fails the owner's zoo requirement despite a tied arithmetic total. N is preferred among designs meeting the requested scope. |

Original E3: B0 **0**, B1 **0**, N **0**, P **2**. B0/B1/N parse native mixed
files, so literal never-read-secret is untrue; amended E3 permits an explicit
bounded metadata path. Original totals would be 6, 8, 10, 12 respectively.
Do not silently replace one rubric with the other.

## Preferred boundary

Prefer N. The skill's existing name is a requirement label, not an authority or
proof of provider identity. Operator policy selects the actual provider and
decides which source/recipient is trusted. This avoids teaching a skill how to
acquire or authenticate infrastructure while preserving useful requirements.

The automatic evidence path may report only what it observes: enabled
configuration in a specified supported launch context. For stronger matching,
require protected provenance or an operator statement. An opaque provider may
be operator-attested; label it as such, bind its client/profile/account-context
identifier without secret bytes, and invalidate it on observable context
change. A contradictory observable disable/shadow must defeat an assertion;
an assertion cannot make a configuration active or a token valid. A fully
opaque external change is not detectable without client support: the assertion
is a reliance on the operator, not measured current liveness.

No display name, command/args equality, URL origin/path, successful parse,
trusted package signature, or declaration digest proves authentication,
runtime binary provenance, endpoint control, or authorization to receive data.

## Adversarial cases to challenge astra-02

These are independently derived candidates, not peer-confirmed findings.

### A. Environment-name allowlisting is not recipient isolation

Environments §10.2 makes `mcp.env_names` the sorted union across the adapter's
MCP set. Section 7.8 says the launcher passes operator values to the client;
whether its stdio children inherit them is an adapter fact. §5.8 renders no
per-server env map. Source: `contextmaterialize/mcp.go:197–213,244–327`.

Counterexample: approved server A requests `PAYMENTS_TOKEN`; admitted stdio B
requests no env names. In a client that inherits its environment into each
server, B can receive A's variable. A later addition of A can widen B's exposure
without changing B's own recipe or empty env list. Conversely, adding B changes
the recipient set without changing the union. Package allowlisting and an
exact single-declaration consent do not establish per-server confidentiality.

Small fix: say explicitly that the client launch and its inheriting servers
share an environment trust domain. Approval must account for the effective
recipient set and effective allowed-name union (and relevant launch policy),
or the operator must deliberately authorize a broader trust domain. Reassess
on changes to either set. If a product requires per-server isolation, use
separate supported launches or future broker work; do not claim it here.
This is a design counterexample, not a reproduced client exploit.

### B. Hardened does not universally mean bounded absent-env behavior

Manager §7.1 refuses explicit `passable_env_names: null`. Environments
§10.3:3334–3344 expressly preserves the shipped S4 profile's absent-knob rule.
During `s4-warn`, absence is unbounded even under hardened; under `s4-enforce`,
absence means empty and names outside the allowlist are dropped. A security
argument citing only the posture cannot claim default-deny environment
delivery. Record the rollout profile and effective policy. Do not redesign the
existing rules implicitly through this feature.

### C. Names and recipes can launder untrusted provider identity

The base accepts declaration digest **or command/args** for package identity.
Two distinct source packages can emit identical recipes. `npx` and `uvx` can
acquire arbitrary code, and PATH changes the resolved executable independently
of the declaration. Environments §2.2 deliberately allowlists declaration
sources rather than binaries. `internal/mcp/mcp.go:56–65` unions name maps;
`Verify:128` counts a key, without provenance or effective precedence proof.

A repository-provided alias must therefore never act as an operator identity
override. Same name/recipe is configuration evidence only, never package
provenance, acquisition permission, ownership, signer satisfaction, or consent.
Use source + exact resolved pin + directory + audited declaration identity for
managed provenance; use explicit protected assertion when native provenance is
unavailable. Existing name-only requirements retain their documented limited
meaning rather than silently becoming identity checks.

### D. Metadata-only does not mean arbitrary strings are safe metadata

Native URLs and argv can themselves contain credentials. Base origin/path
matching may inspect those bytes but must not retain full argv, URL, env,
headers, parser excerpts, or hashes of unknown credential-bearing values in
records or diagnostics. No interpolation, env lookup, auth-cache access,
native executable invocation, network probe, or credential-presence check.
Bound regular-file reads, parser resources, duplicate/ambiguous syntax and
error rendering; discard foreign data after projecting safe metadata.
An unsafe/unrepresentable identity is unknown, not equality after silently
stripping its credentials. Native writer staging is a separately bounded
private byte-preservation operation, as the csk input §4 already specifies.

### E. Consent, source admission and authentication are separate gates

Environments §2.3 surfacing is informative and never fails; it is not approval.
The base must not treat existing materialization as existing consent machinery.
The csk input §2 supplies the stronger pattern: protected operator state,
canonical consumer identity, scope, target agents, normalized plan,
source/declaration digest, writer capability/version, and renewed approval
when authority changes. Project files, skill hints and self-declared approval
must be inert. Consent cannot waive enforced allowlists, signer policy,
reserved-variable checks, malformed policy, or audit blocks.

Under hardened, empty MCP package allowlist with an MCP declaration remains a
hard error with the old lock unchanged, irrespective of consent. A positive
allowlist entry admits a source; it does not certify all its future runtime
downloads or grant access to all existing credentials. Native writers need an
explicit posture contract; inline definitions cannot acquire fake package
identity to bypass the git-only rule.

## Smallest changes from the base

1. Keep existing skill `dependencies.mcp_servers`; defer its `server` addition.
   Put optional provisioning recommendations in the operator lane using
   existing declaration packages; never execute acquisition from a skill hint.
2. Specify one protected provider-evidence/consent policy, with names treated
   as labels, exact managed provenance, explicit scoped opaque assertions,
   observable invalidation, and known-conflict precedence over assertions.
3. Define satisfaction against the selected launch, not a union of unrelated
   homes. Any succeeds on one actual qualifying target; all requires each;
   unknown never supplies a success. Preserve released requirement semantics
   behind their version boundary; new strict semantics require governance.
4. State bounded native parsing and no semantic credential handling; retain
   client-owned authentication and no manager health checks.
5. State the shared environment-recipient boundary, S4 rollout behavior, and
   independence of source admission, exact-plan consent and authentication.
6. Submit the semantic/policy changes through a CIP, decision record, closed
   schema(s), compatibility notes, and positive/negative vectors. Existing
   `agent-mcp.json` schema 1 has no `auth` field; do not retrofit it in place.

## Conformance cases to specify (not executed)

Forged project binding; same-name squatting provider; equal recipe from another
package; native shadow of approved managed entry; `any` with unknown only;
`all` with one unsupported target; stale opaque assertion; observed disable
against an assertion; harmless foreign sibling vs credential-bearing argv;
parser error without raw snippet; malformed read without overwrite; stale
consent after scope/agent/source/recipe change; addition of a stdio recipient
without env-union change; addition of a permitted env name without recipient
change; hardened empty allowlist despite approval; hardened explicit-null env
refusal; hardened absent-env under each S4 rollout profile; native OAuth/auth
not checked; no assertion or matcher invoking a client or endpoint.

## Open review state at the initial checkpoint

Awaiting peer discussion and convener coordination. Initial table remains
frozen above; later convergence and any revised scores will be appended with
event references. Only my own artifacts will be submitted for integration.

## Post-checkpoint comparison: round 2

The independent initial content was committed with a verified signature as
`1c28d5fe30daf99691061fa4930d49e21985c172`. Its SHA-256 is
`ed1d91e1eaab51ede2e4e6dc8bddedf0995d461d61d80f8884b5ece60cb76db3`.
The hash was announced before peer-verdict reading in
`$Ysw5GZny1dbopoEJg9sWLEqoB1RM4_Drrh7dlXXzB-o`. Local branch only; no push.

I then read astra-02's verdict and the existing trust/evidence debates. The
core findings converge independently: source admission is not consent; a
requirement is not a credential grant; native parsing needs the amended E3
boundary; name/recipe equality is not provenance; client-launch env union is
not per-server isolation. My confirmation of `f-secret-boundary` is
`$Bw5gvYkVTP3bPoyk62gMhY8tyF4cpI2EArqw5fURzvc`.

The common candidate is now precise enough to distinguish it from my initial
N: protected authority uses a governed successor of the **existing machine
configuration family**, with result evidence in a marker successor. It does
not introduce a new standalone file family. New scoped evidence still counts
as new machinery. E8's common case is explicitly an already configured
provider; cold setup remains a separate lower score. These are substantive
accounting assumptions, not changes to the saved initial scores.

| Criterion | Current N | Corrected N+A | Corrected A alone | Reason |
|---|---:|---:|---:|---|
| E1 | 1 | 1 | 2 | N counts new authority/evidence fields in existing families; A only permits existing schema-1 `agent-mcp.json` at a skill root. |
| E2 | 1 | 1 | 2 | N needs a new scoped evidence contract; A reuses declaration acquisition/admission and leaves the legacy checker unchanged. |
| E3 amended | 2 | 2 | 2 | Bounded native-byte handling; A discovery projects safe metadata only, and detailed declaration display waits for applicable strict admission. |
| E4 | 2 | 2 | 0 | N covers the five provider-source categories using observed supported configuration or explicit reliance. A alone retains the native checker's opaque-provider gap. |
| E5 | 2 | 2 | 2 | Existing skill requirement bytes stay portable; provider choice remains local. |
| E6 | 2 | 2 | 1 | N preserves unknown/negative distinctions and exact authority. A alone does not repair legacy name unions/launch evidence. |
| E7 | 1 | 1 | 2 | N still needs governed configuration/marker/adapter rules and vectors; corrected A uses a closed existing format and independently gated optional selection. |
| E8 | 2 | 2 | 1 | Already-configured N: zero actions for supported observation or one enumerated reliance decision. A standalone improves discovery but cannot close opaque verification. |
| **Amended total** | **13** | **13** | **12** | N remains preferred; A is an optional convenience. |
| **Original E3 / total** | **0 / 11** | **0 / 11** | **0 / 10** | All retain native inspection, so the literal byte-contact prohibition is not met. |

Cold-setup N/N+A has E8=1, total 12 amended / 10 original. E4=2 is provider
category coverage for supported selected launches: it does not conjure MCP
support in pi 0.84.2's recorded managed mode or any unsupported client/mode.
A's E4=0 applies the literal excluded-member anchor; partial-coverage scoring
elsewhere is an acknowledged rubric interpolation, not evidence of opaque
coverage. Base and B1 scores above remain unchanged.

The current N vector `[1,1,2,2,2,2,1,2]` matches astra-02's published same-design
vector exactly; comparison is recorded in
`$eGPXQxniiaik52_BvU6lKGlHLY13Lv3lZH7V3NEou54`. This supplies cross-host
scoring evidence under the mission amendment, not runtime qualification or a
universal-optimum proof. The convener owns the collective's proof synthesis.

### Corrections and retained limits

- Native/managed/opaque selectors are matching handles, not fingerprints.
  A disabled unrelated native entry with the same label cannot invalidate an
  opaque connector; contrary evidence must concern the bound provider and
  selected launch. File absence is not complete negative evidence for cloud
  or plugin providers. Legacy install markers are not new observed evidence.
- Existing profile provenance is annotation, not a third success class.
  A stale lock cannot make a missing/disabled/overridden provider available.
- A's sidecar remains inert until explicit selection. A skill audit may be
  advisory, so detailed argv/endpoint display cannot bypass MCP strict audit.
  Exact skill-snapshot bytes do not replace canonical Git source admission,
  directory/pin identity, signer policy, the MCP package allowlist or consent.
  Path-source restrictions remain. Multiple recommendations can use an
  existing companion context package, without a new discovery convention.
- `agent-mcp.json` schema 1 and §5.8 have no HTTP header-env mapping. Env names
  alone do not wire bearer authentication. Native external configuration can
  satisfy the requirement; this feature must report unsupported provisioning
  rather than pretend authentication has been configured.
- My initial P original-E3=2 assumes already-admitted secret-free metadata as
  input. An end-to-end profile installer also audits hostile package bytes,
  which can contain credentials; it cannot claim that literal no-byte-contact
  guarantee. P's entire-manager original E3 should be 0, total 10. This
  sensitivity correction does not affect preference: P excludes zoo members.

### Remaining targeted challenge

`$GZBY9lcDf42utPLdr5lWYmjFhFsu_NRu3vLxiPDYuww` asks astra-02 to confirm two
explicit vectors: change recipients without changing the admitted env union,
and change the union without changing an existing recipient's declaration.
Consent must reassess effective aggregate exposure, or explicitly authorize a
shared launch trust domain. This is distinct from per-skill tool permission.
It also asks to record the hardened + absent knob + `s4-warn` residual. No new
finding file is warranted before peer confirmation; overlapping material
belongs to the existing finding's owner or the convener.

### Round 2 resolution and confirmed sharpening

Astra-02 confirmed both consent-set vectors and the S4 qualification in
`$PMpF2s8kuwv8JuapOho3DNn2vgIQ1-KZaSLeNpPlumE`. I independently read its extra
source references: `envprofile/managed.go:2442–2458` resolves the union once;
`envfragment/envfragment.go:246–250,271–330` selects `S4Warn` and preserves
absent-knob unbounded passthrough. This is source evidence, not a runtime run.
Astra-01 independently confirmed the same correction in
`$8vlD9K1dEBlA3K2U7MljLO727hSFzZBFNE8V3hSQrbs`; my acceptance and full-client
environment qualification is `$0Fc376j4vD5fq2Frc7ZjeuVYQS_hPUSny-QME5F_dbY`.

Agreed contract: evaluate changes to effective passed-name exposure,
potential inheriting provider recipients, adapter/launch mode and policy.
Either set can widen without changing the other. An exact-plan grant that did
not authorize that aggregate exposure no longer suffices. One batched approval
can cover the changed launch plan; there is no per-old-server prompt or
per-skill use-authorization gate. If recipients/exposure cannot be enumerated,
require explicit approval of the shared launch trust domain and its visibility
limit, or leave the manager-controlled mutation unapproved. Independently
changed foreign clients are outside that mutation authority.

Section 7.8 adds MCP names to a launch allowlist; the MCP union is not proof of
the client's complete environment. Other inherited client environment belongs
to the same residual. Do not claim exhaustive exposure disclosure from the
fragment alone. Observable safe names and policy are enough to describe the
boundary; no credential values are read to enforce it.

Astra-11's question `$PQDzCQTVLt5VerUZ46IwDPyeXJfaJTYBGdBFsudcu1s` correctly
removes a raw-command exception from the peer sketch. Manager §6:1107–1108
requires an unresolved-command warning, not disclosure of the foreign command
string. Current `mcp.go:143–144` formatting is implementation evidence, not a
normative necessity. My confirmation is
`$BMMBx08uFxUycmtcAf1ZQilO1FY6gBTsU-EVAk8I0y8`: perform any existing static
PATH check privately and report validated requirement/target plus a safe
diagnostic; never raw command, argv[0], or parser snippets. A bare native
command is not thereby secret-free or an admitted declaration.

These are refinements of existing findings, not duplicate findings. Astra-02
will integrate the consent clarification in its own artifact. N/N+A remains
13 amended / 11 original, E7=1, with explicit aggregate-exposure grammar and
vectors still owed by the normative design. No source implementation was
changed or qualified by this review.

### Minimal persistence clarification

Following astra-11's challenge and astra-01/03 confirmation in
`$rXK97-aRDmaw_fmGgx5GxLtTOhfgfqouVQpV0k90IBo` and
`$63Xgqujlt_M8cHf1ui-aaOyyDEdWU2irixibzSdfbDU`, the minimal N can compute
selected-launch status transiently. The protected reliance record still needs
a governed existing-configuration successor, but a portable marker successor
is **conditional** on a concrete consumer needing persisted stronger evidence.
My earlier current-candidate wording must not be read as requiring that bump.
Old `FoundIn` remains legacy native presence; neither an assertion nor a new
managed-effective result may be written there as if it were that old fact.
This reduces storage without weakening the authority boundary. E1=1, E2=1 and
E7=1 remain; the score vector is unchanged.

I also confirmed astra-06's HTTP header-routing capability qualification in
`$DWR-oqZ-bsDlBv-ivxu0oT0wWz1p_YEi6NmpOGXWteM`: strict managed Claude cannot
borrow a native authentication entry it excludes. Keep unsupported HTTP env
provisioning explicit rather than treating `auth:env` as a routing mechanism.

### Optional A: cross-kind adoption limit

After initial scoring, astra-04 and astra-06 identified
`f-cross-kind-name-collision` in `$xZUc1CI3CUCBNX-BgI8Mq8pPa7Jbww9C_ACTjjtl-jo`.
I independently inspected `contextresolve/contextresolve.go:316–320,409–420`
and its lock construction, `envprofile/gitsource.go:238–275,721–755`, and
`envprofile/managed.go:205–226`. Constraints/selections are keyed by name;
`add` coerces a later different kind to the existing kind; loaders and MCP
materialization use the selected kind. Same-name skill and MCP declarations at
one source/pin/directory cannot therefore be claimed as two existing resolver
members. This is source evidence about reuse, not a universal schema
prohibition or a reproduced exploit.

Corrected optional A must detect/refuse or defer that colliding joint-adoption
plan, while preserving external named fulfillment and distinct-name
co-location. Admission of a skill snapshot is not admission of its declaration
as an MCP package and is not consent. Automatic renaming or kind-aware resolver
changes are separate work. N remains preferred; N+A's existing E2=1/E7=1
scores assume this explicit adoption limit, not an unimplemented resolver fix.

### Name squatting and honest status

Wonder-11 retains E6=1 because a wrong service under the right configured name
can still satisfy N (`$5-dCNp7oabcyJK7T7P-tG_WYew89_ndCqh9d3Lrm0j4`). I accept
that as a meaningful conservative assurance dissent. My E6=2 remains
conditional on precise status: **configured by name; provider identity and
authentication not checked**, or explicitly **operator-asserted** for reliance.
The residual was already named in my initial independent verdict: a name is a
label, not provider identity or authority. An operator can make a mistaken
assertion, and neither assertions nor file observations certify service
behavior or safe credentials routing. Known negatives remain binding.

N deliberately does not implement an author-selected cryptographic provider
identity constraint. If that becomes a hard product goal, N alone no longer
meets it; reconsider B1 against that added goal. Do not claim exact numerical
unanimity or hide the assurance tradeoff behind the mission's one-point proof
tolerance. This status wording changes no schema or authentication ownership.

Wonder-11 accepted this as conditional convergence in
`$iAeh_gEUokcOpwDKugqwFFq92jR4xHduMpSW-0d01NQ`: N+A reaches its E6=2 / total
13 when the identity/authentication qualifier is mandatory, while a rendering
that drops it retains that seat's E6=1 / total 12. The condition must survive
the normative status contract; it is not evidence that current implementations
already render it.

### Final alternative qualification: optional discovery and skill audit

Astra-01's clarification `$hKtj6U7xrnori2tj3Kux8CPOM6OoWY1HhVtumWKoax4`,
followed by astra-04/03 in `$4ltF8xqpGSDkYR7jg_WDco_VuamwztEF1IEdBKDiRw0`
and `$731Jpduhgk_b3gengesp8z1BBFy-K3u39HvzRMg6qgA`, makes an additional
E7 qualification explicit. Manager §7:1110–1171 and environments §9.1 require
the secret-material class in the profile context/MCP lane; that is not a
complete ordinary-skill-root declaration discovery/audit contract.

My preceding A-alone E7=2 was too generous for the richer manager-discovery
feature. Its ordinary skill-lane `args`/URL scan scope, severity, waiver,
admission and safe surfacing need explicit governing. **Current richer
A-alone: `[2,2,2,0,2,1,1,1]`, total 11 amended / 9 original**, superseding the
12/10 comparison above without erasing it. A purely inert schema-1 file with
existing manual adoption is narrower; do not use its simpler grammar to claim
the richer discovery feature is already specified.

Path-source notices must omit executable profile-adoption instructions:
environments §2.2's git-only MCP admission still applies. Pre-admission output
stays value-free metadata regardless of scan results; later MCP adoption
independently passes strict profile gates. Do not silently import profile
strictness into ordinary skill installation or make malformed optional
metadata a new mandatory failure.

N and N+A remain **13 amended / 11 original**, cold setup 12 amended / 10
original; their E7=1 already includes this unfinished optional contract. N
remains preferred and does not depend on A. No new finding or implementation
claim follows from correcting the standalone alternative's score.

### Audit waiver does not authorize secret disclosure or reproduction

Astra-02 asked `$xSGO0qksc8B68V1gr6rmjfakIF3nxsK27zIAdmV0LoE` whether a
strictly admitted declaration with a scoped secret-material waiver can safely
be shown in detail. I confirmed the counterexample in
`$sFmAXQMAuzn5Db3lOZF9tyvCs01HohyDX9ODh4NqCSI` after reading
`agent-mcp-v1.schema.json`, `contextpkg/contextpkg.go:497–518`, environments
§9.1:2302–2319 and `contextmaterialize/mcp.go:150–175`.

Schema-1 args are arbitrary bounded strings. Its HTTPS grammar constrains URL
syntax but permits a credential-bearing path. The parser retains these bytes.
A scoped waiver clears an admission finding; it does not sanitize the bytes
or authorize printing them. Existing §2.3 and `FormatDeclarationRows` render
raw args, so passing strict audit is not a certificate that this reuse meets
amended E3. JSON escaping is not secret removal. A detector miss likewise
does not establish that a field is secret-free.

The same distinction applies to persistence and forwarding: §5.8 and
`contextmaterialize/mcp.go:244–327` serialize args/URL literally into managed
configuration. A waived **actual credential** cannot be copied into that
output under a feature claiming the amended no-secret boundary, even when
stdout is redacted. This is a source-derived counterexample, not a credential
probe or executed exploit.

The corrected feature needs separate admission, safe presentation and
credential-free provisioning predicates. Keep sensitive/waived candidate
handling metadata-only; refuse detailed presentation or value-bearing
provisioning where the required boundary cannot be met. If hiding a field
prevents meaningful review of changed execution/routing, do not treat it as
reviewed consent. Do not delete the general waiver mechanism implicitly or
claim a syntax rule/detector proves arbitrary strings clean. Compatibility
with the legacy waiver/surfacing/materialization lane needs governing, or the
feature must explicitly narrow its guarantee when delegating to that lane.
N's proposed E3=2 is conditional on this boundary; current unmodified reuse
is not qualified by this score. E7 remains 1; N does not require optional A.

Wonder-12 independently confirmed the persistence/materialization extension in
`$1ofzJcoCkiMNdn-bdEf3jNok_yVFcyfZQJVW4AgN87I`; astra-06 confirmed the
separate safe-display/meaningful-consent predicates in
`$woL6DCgGyMNdEsCeou1DBjqFEDSqzQwGXbfNjecvjUY`. The materialization follow-up
I sent is `$lUSbVgBMWBhdEhk31UaFQqExiNO7W6fGl3S57ebwsqE`. These strengthen the
existing secret-boundary finding; no duplicate finding is authored here.

Astra-02 accepted both consequences in
`$uLalPw5QAdJUb8kQmXrn0yOqqe5Xhe7TBeS74X9cLcI` and published the consolidated
finding in its own signed commit `8f11dc6f1f96ce2ed96ab9521a8688894739cfab`
(reported in `$8VRAMx6fpLyJljxdcWtiwsvEYIJs5-9ie1d-62Gf6R8`). My closing
acknowledgment is `$zxj0F1rugof_6uk39RoNA-qttrFEJOk_quQj9dnQRvg`. Astra-06's
fresh source confirmation of the materialization extension is
`$JFphmMNmcMTGI5vFw2GrQm-V-a8wtAt9vXQpEHGLX9E`.

Keep the two evidence paths precise: current §2.3 HTTP rows have `command=-`
and `args=[]`, with **no URL column**. The current stdout counterexample is
stdio args; the current URL counterexample is §5.8 generated-file
reproduction. Any future URL display must inherit the same bounded
presentation rule. Wonder-03 accepted this correction in
`$oTSFucFl6cr8wBCs4kLBh0Mb6tBu4ZHHqB0t0Ky9_3o` after my clarification
`$5YMaKTmxTE3N-FlodbMsdiio2DYK55JM4W91iaqOgWY`.

Optional A's recommendation snapshot pin is independent of the adopted
profile pin: adoption is an explicit action, not continuing skill/provider
lockstep or a new stale-state monitor. A safe remediation reference identifies
canonical Git source, exact resolved commit, directory and declaration name;
display the root as `.` while preserving its existing absent-field encoding.
Same-name cross-kind collision limits and independent MCP admission still
apply. These bounds do not add a manifest/auth field or new normative grammar
inside this review artifact.
