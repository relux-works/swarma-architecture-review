# astra-03: zoo compatibility verdict

Status: first-five review converged; cross-host row agreement recorded; second-five adversarial comparison active. Seat: ivmbp astra-03. No implementation or native-runtime certification is claimed.

**Prefer named skill requirements with scoped operator evidence (N), plus an optional skill-shipped declaration recommendation (A).** Keep the current skill-manifest grammar; put deployment choice and explicit reliance on opaque providers in protected operator policy. Use existing operator-selected profile/native provisioning and native authentication. The base's three-way separation is useful, but authoritative package/endpoint identity in the requirement adds complexity without covering opaque providers or distinguishing native and managed launches correctly.

N and N+A tie at **13/16** under the amended rubric. A is a separable convenience for first setup, not a required second mechanism. The base as written is not proved elegant. Independent Mac mini evidence now corroborates the bounded design within one point per row; the retained E4 qualification and amended independent-five proof rule are recorded below.

## Evidence and limits

Sources were read from clean local snapshots. Outside clones were not pulled because the sandbox is read-only there. No web, builds, tests, native-client probes, real configuration reads or credential-store reads were performed.

- **S:** curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`: core §§3–4; manager §§1,6; environments preamble, §§1.3,2.2,2.3,5.8,7.8,10.3; `schemas/v1/common.schema.json` `$defs.mcpRequirement`; `agent-mcp-v1.schema.json`; COMPATIBILITY.md and GOVERNANCE.md.
- **I:** curator `5234cf38833554542e68afade15951c6e56ed89e`: `internal/mcp/mcp.go:24-61,245-287`; `internal/contextmaterialize/mcp.go:31-107`; `internal/envprofile/managed.go:205-229,298-364`; `internal/envprofile/surfacing.go`; `internal/install/install.go:1582-1605`; `internal/marker/marker.go:253`.
- **C:** supplied csk proposal §§1–5; slice-1 decisions D1/D5/D6/D7 and A4/A6; curator review H1–H4 and S2/S3. These are proposal/review evidence, not implementation certification.
- **F1:** [selected-launch evidence finding](../findings/f-launch-universe.md). **F2:** [opaque-provider evidence finding](../findings/f-opaque-provider.md). Both are proposed, with independent same-host confirmations and event ids recorded in the files.

Claude strict-channel behavior is verified only as recorded by S for its pinned release. OpenCode precedence remains S's docs-confidence fact. The Codex trusted-project residual is supplied review evidence, not independently reproduced by this seat.

## Rubric and scores

Primary E3 is the explicit **MISSION-MCP.md amendment at `534e384`**, announced at `$ropOGjw3dqPFz1fjx0hkU8dYrqD4iOS6X3jfs7L5y9o`: bounded foreign-byte handling is allowed; credential-value use, auth execution and raw foreign argv/URL/env persistence, logging or surfacing are not. Original literal E3 scores remain separate below. Primary E8 uses the rubric seat's stated common case: a suitable provider is already configured. Cold setup is reported separately.

B is BASE as written. B+ retains authoritative package/endpoint requirements but repairs consent/evidence/schema boundaries. N retains named requirements and adds scoped local binding/evidence. N+A adds the optional shipped recommendation. A alone is **legacy-checker-only**: ship, display safe candidate metadata, then operator-selected existing provisioning; it borrows none of N's new checker/assertion machinery. S-only forbids arbitrary native reads/writes in the dependency operation. K requires tool capabilities without live manager probes. G is the manager-owned authenticated gateway.

| Design | E1 | E2 | E3 amended | E4 | E5 | E6 | E7 | E8 | Total | Original E3 / total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| B: base as written | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 5 | 0 / 4 |
| B+: repaired authoritative identity | 0 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 10 | 0 / 8 |
| N: named requirements + local evidence | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 13 | 0 / 11 |
| N+A: N + shipped recommendation | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 13 | 0 / 11 |
| A alone: recommendation + legacy checker | 2 | 2 | 2 | 0 | 2 | 1 | 2 | 1 | 12 | 0 / 10 |
| S-only: restricted metadata-only branch | 1 | 1 | 2* | 2 | 2 | 2 | 1 | 1 | 12* | 2* / 12* |
| K: tool-capability requirements | 0 | 0 | 2 | 1 | 1 | 1 | 0 | 1 | 6 | 0 / 4 |
| G: manager-owned authenticated gateway | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 2 | 5 | 0 / 5 |

S-only's conditional 2 is limited to that restricted dependency operation, not existing Curator launch/provision functionality; it needs a governed capability boundary rather than silently claiming unchanged §6 scanning. G is ineligible through E3=0. All native-inspecting candidates fail the original literal E3 gate.

This seat applies E4's explicit exclusion anchor: opaque providers remaining unsatisfiable make A's E4=0. Wonder seats interpolate partial coverage as 1; that raises A to 13 but does not change the preference among complete zoo candidates. N/N+A's E4=2 is common to both readings. Under cold first setup, N/N+A's E8=1 and totals=12: selection/consent and native authentication remain distinct actions. No universal one-click setup is claimed.

### Evidence for each criterion

- **E1:** S closes the requirement, declaration and manager configuration schemas. B/B+ need requirement identity, auth metadata and binding/state changes. N/N+A choose a successor of the **existing protected manager-config family** for structured scoped reliance, hence 1. Selected-launch status may remain transient; a marker successor is conditional on persisting stronger evidence, not required by minimal N. A standalone authority-record family would score 0 even if manager-private. A alone reuses existing declaration bytes; K/G introduce new contract/runtime families.
- **E2:** N/N+A reuse requirements, profile locks, materialization, allowlists and audit, but launch-aware evidence/assertions are genuinely new checker work. B+ also imports identity equivalence and package-lock ownership. A alone retains legacy checking and existing provisioning. S-only loses native scanning; K needs unavailable session inventory; G adds routing and lifecycle.
- **E3:** I reads/unmarshals mixed native files; C §§4–5 acknowledges foreign credential literals. Corrected candidates explicitly bound handling: no credential resolution, auth or probes; no raw foreign command/argv/URL/env/header output or persistence; metadata-only errors. Even a bare native command name is arbitrary foreign content: manager §6 requires an unresolved-command warning, not echoing that string. Field names alone do not establish secret-free contents. A shows metadata before MCP admission, never raw recommendation argv/URL. B's new matcher has not fully stated the bound. G forwards backend credential values by construction.
- **E4:** F1/F2 refute B's unqualified zoo claim. N/N+A cover provider-source categories through actual selected-launch evidence or explicitly accepted, labeled reliance where observation is unavailable. This is conditional on an already capable selected launch and assertion-accepting policy, not universal effective availability, machine verification or authentication. They do not add a channel to the current managed pi adapter or make strict Claude read excluded native settings. This says nothing about arbitrary native/plugin integrations or later releases. K lacks universal safe tool inventory; a cloud connector need not expose a backend G can route. Mac mini astra-13 assigns 1 to this same bounded coverage, making N/N+A 12; I retain 2 under the source-category interpretation. The one-point difference is explicit in the proof.
- **E5:** N/N+A preserve existing skill bytes and leave deployment local. S COMPATIBILITY lets older partial clients reject new unsupported schemas, a concrete cost for B/B+. K adds provider-specific tool contracts; G requires a gateway environment. A's inert extra file does not require a manifest-version upgrade.
- **E6:** B leaves opaque presence, alias authority and effective precedence unresolved. N/N+A separate observation, assertion, unknown and authoritative negatives per target; protect consent; preserve legacy marker meaning; and never auto-provision a duplicate to hide uncertainty. A alone retains legacy checking limitations. K's install-time claim remains underdefined. A gateway can report its own configuration honestly, but does not thereby establish every backend, hence G=1 here rather than assuming it must always lie.
- **E7:** S supplies governance, but B does not close identity/binding/lock semantics. N/N+A/B+ have concrete sketches and writable cases, but config and scoped-verification semantics, adapter completeness, and assertion/system-policy interaction remain to be governed; 1 is not an implementation claim. Persisted stronger markers would additionally need their own versioned contract. A's bounded recommendation convention uses an existing closed grammar. K lacks a settled capability meaning; exact tool names alone do not prove equivalent semantics. G is specifiable but substantially larger.
- **E8:** N/N+A need zero extra actions for a suitable observable provider, or one decision covering an enumerated opaque-reliance set. A improves discovery for cold setup without adding a point above the common-case ceiling. B/B+ may need identity/alias resolution; S-only needs assertions even for normally readable native state. G offers one configured entry, but fails the auth boundary. These scores never count authentication as already completed.

## The smallest coherent contract

A requirement name is an author-chosen label explained by the skill's hint/documentation, not a global capability identity. Retain `hint`, documentary `transport`, and `required_in` in existing schemas. Names alone never grant write authority or config ownership.

Protected local bindings may batch an **enumerated set of exact skill requirement identities** in one decision. Each acceptance is scoped to requirement identity, consumer project/profile, target agent and selected launch descriptor. Added requirers or changed scope do not inherit a wildcard assertion. Provider selectors are matching identities, not recipe fingerprints:

| Provider | Selector | Evidence limit |
| --- | --- | --- |
| Native entry | Agent, config surface, configured name | Static configuration under known precedence; no auth or executable identity claim |
| Managed declaration | Profile and lock member, in selected channel context | Recorded origin alone does not establish effective availability |
| Opaque plugin/connector | Agent, launch, operator-assigned handle | Explicit reliance; configuration/auth/internal drift remain unverified |

Acceptance is observed or asserted; origin is orthogonal annotation in existing profile/audit/ledger evidence. A locked declaration can still be missing, disabled or shadowed in the effective launch. No stale origin record outranks current negative evidence. Environments §1.3 expressly forbids using a lock as an authorization token or provenance proof; signature admission and operator consent remain separate.

`any` needs one accepted target; `all` needs every target. Retain per-target unknowns when `any` succeeds elsewhere. Contrary evidence must be authoritative for the **same selector and launch**. Absence from the six native files does not prove an opaque connector absent. An unrelated disabled same-name native entry does not defeat a separately bound connector. Opaque internal drift has no claimed durable detection; revocation, context change and authoritative contrary observation bound reliance validity.

Evidence belongs to every requirement/target/launch tuple: one provider may be observed for Claude and asserted for Codex. The minimal lane computes this status afresh and keeps protected reliance in the existing configuration family's governed successor. Old `FoundIn` markers establish legacy native presence only; no automatic upgrade or assertion is written there. A marker successor is needed only if a consumer requires persisted stronger evidence. The opted-in scoped-verification contract and old-reader behavior still need specification. Neither this checker nor its reliance record enforces per-skill runtime access to tools.

### Launch completeness and native writers

| Selected context | Honest boundary |
| --- | --- |
| Claude with an actually applied strict channel over a non-empty set | Other native MCP configuration is excluded; a channel containing Y cannot be satisfied for X by native X |
| Claude with no MCP channel | An empty profile set is not proof of exclusion; §5.8 emits no channel for an empty set |
| Managed Codex | Seed revision and effective project residual matter; supplied trusted-project behavior is not runtime-certified here |
| Managed OpenCode | Project entries can add/override the channel set; lock/marker alone is incomplete |
| Native launch | File absence is incomplete for plugins/connectors; inspect relevant known disabled/precedence state |
| Current managed pi adapter (recorded 0.84.2) | No revision-1 MCP channel for that managed launch; no claim about arbitrary native/plugin integration or later versions |

A native writer must not mutate marker-owned managed homes or reserved channel files. csk foreign equal entries may satisfy a requirement without granting ownership; provision can still conflict under D6. An alias/assertion cannot override a known launch exclusion, enabled-state failure or applicable source/audit/signer/hardened refusal. Whether system policy additionally forbids assertion-grade reliance is an explicit remaining governance choice.

### Optional shipped recommendation and authentication

A git-backed skill may offer existing root `agent-mcp.json` bytes from its exact resolved commit. The skill lane shows only safe candidate metadata and the real remediation route: add it as `requires.mcp` to an operator-selected context package. The declaration source must independently pass MCP allowlist, signer and strict audit gates; skill admission does not prove MCP admission. Full declaration plan display occurs at its existing audited admission point, with HTTP endpoint review addressed explicitly because §2.3 currently omits that column.

The snapshot fixes bytes, not authority. Use its exact commit rather than assuming the skill's version tag matches the declaration version. A path/local skill gains no canonical git identity merely by containing the file; §2.2 git-only admission still applies. Root schema 1 offers one server; multi-server setup can use an existing companion context package. Malformed recommendation parsing warns safely and creates no new skill-install failure; credential/audit failures retain their normal blocking policy. No directory-discovery format or naked-declaration install command is smuggled into this proposal.

Native clients own OAuth and secret handling. Schema-1 declarations have no auth class or HTTP header binding; §5.8 emits argv or URL, and `env_names` requests launch passthrough rather than specifying an Authorization header. A native HTTP env-header entry can serve an effective native launch, but cannot serve strict managed Claude when excluded. Unsupported managed materialization remains explicit, or names-only routing is governed separately. No health check, manager proxy or credential broker is required.

Provider-write consent renews for changes to admitted declaration/execution, credential routing, agents, destination or scope. The list of requiring skills is display attribution, not a new per-skill use-permission system. A newly installed skill using an unchanged observed provider is not a provider mutation. Reliance scoping and write-consent lifecycle are distinct.

Environment names are a launch-wide union (§§5.8,10.2), not a per-server credential-isolation mechanism. Consent must expose and reassess the effective recipient set and admitted-name union when composition changes. The manager still handles names only. Under §10.3, hardened posture rejects explicit `passable_env_names: null`, while an absent knob retains the active S4 profile's behavior: `s4-warn` is unbounded with warnings; `s4-enforce` drops unlisted names. No stronger sandbox or rollout guarantee is claimed.

## Minimum delta from BASE

1. Remove authoritative `server.package`/`server.endpoint` and auth-class wire additions from this slice; retain current named requirements.
2. Keep provisioning explicitly operator-selected through existing profile/declaration channels or independently reviewed native writers.
3. Govern scoped reliance in the existing protected config family and compute per-target status transiently; version a stronger marker only if persistence is required. Do not hide a new authority-record family.
4. Specify selected-launch evidence, aggregation, selectors, assertion validity and authoritative negatives without changing old §6/marker meanings silently.
5. State amended E3's bounded native handling explicitly and keep authentication with clients.
6. Optionally add metadata-only discovery of an existing same-snapshot declaration, without bypassing its independent admission or consent.
7. Freeze the configuration and scoped-verification grammar, completeness cases and system-policy choice with positive/negative vectors before claiming E7=2; govern any optional stronger persisted marker separately.

## Agreement and proof status

The same-host N/N+A vector converged to **[1,1,2,2,2,2,1,2] = 13**, original E3=0 and total=11. Relevant independent events include astra-01 `$jNFV-zBNiS3FKni1yne77cS0_Y-b38h4OEqSLseNKEs`, astra-02 `$CSGD0bKQZ4cX9rCtVuSn-Ed_d0kdAOoRM-eZdJyVc_o`, and rubric-seat clarification `$cCNG9kO0TxjYdp7ig8nqRCDeij6qGhpceigw3Q9UlZM`. Wonder-02's earlier N+A=14 was an arithmetic error corrected at `$biOtkvfKBYfAg78ALG0Qkbz0DpsF-rAKHaxk3E4VC1E`; it is not current evidence.

Mission amendment `b5e7dab`, announced at `$16H5I0yTqnEJxkLpw6pt1gM406Uxyf0Hm5b4KZAid3g`, changes the required proof pair to two independently formed fives; Mac mini is an additional cross-host pass. New seats freeze independent scores before reading first-five verdicts. Second-five astra-04 has posted an independently frozen N12 vector at `$gTvTSooKcOKvtSeKCW7ECYSPKezTm6j9dSp-dVr392M`; its adversarial comparison remains active.

Mac mini astra-13 froze its own initial artifact before reading peer verdicts (SHA-256 `6e8ceb9b5669aa4ce620fe96d5e5841296bf3d307b9d83e2dab066cecf701f66`, signed local checkpoint `e948938`). I fetched and read that artifact. It independently reproduces both zoo findings and the URL-only managed-header limitation at the same source pins. Launch confirmation: `$Ik6SFKGm-9ekiZyHUaGRomeGLoHoWzQQZcIZiEa-QDU`; opaque confirmation/challenge: `$wLoUfoiOHgAPNZNmoxN_csBRJZY6WzWiKvsgMOyx22k`.

After resolving its initial standalone-record assumption to the concrete existing-family variant, astra-13 records **[1,1,2,1,2,2,1,2] = 12** (original 10) at `$RKJQQ3pw4wfBtrQGoZPE2MqssfXEMEstE_v5cTmrbAU`. Every row agrees with this seat within one point; E4 is the sole retained difference. My response `$kOe1Skk9G9JhTmiB5NR6WNRulSzfx2mVaTf8I6-jbGQ` accepts the exact scope boundary rather than claiming universal availability. This is actual two-host rubric corroboration for bounded N, not client/runtime certification. Mac mini astra-12 independently reconciles to the same N13 vector at `$eGPXQxniiaik52_BvU6lKGlHLY13Lv3lZH7V3NEou54`.

Mac mini astra-11's minimality challenge `$KoKVkUqcYkat6O2_XqNcx5zDxclzgzMVkvWTDXBoTpM` removes a mandatory marker bump: stronger persistence is optional, as accepted by astra-01 and this seat. Its command-output challenge `$PQDzCQTVLt5VerUZ46IwDPyeXJfaJTYBGdBFsudcu1s` is also supported by my independent read of manager §6 and I's raw-command warning. Neither clarification changes my scores. Environment union/S4 boundaries are independently checked against S §§10.2–10.3 after astra-12's trust review.

N/N+A remains preferred among the compared candidates, with E7=1 and the stated E4 scope. The collective must preserve independent initial scores, the original/amended E3 distinction, the E4 interpretation difference, and the common-case/cold-setup E8 distinction. Universal optimality and full conformance are not claimed.
