# astra-03: zoo compatibility verdict

Status: round-2 position; cross-host scoring remains open. Seat: ivmbp astra-03. No implementation or runtime certification is claimed.

The base has the right separation between requirements, provision and native authentication, but its claimed zoo coverage is not established. A native entry is not necessarily effective in a managed launch, and an opaque connector supplies no observable configured/enabled premise. My preferred core is **named skill requirements with scoped operator evidence**, `alt-names-local-evidence` (N). `alt-skill-ships-declaration` (A) is a useful optional provisioning complement: a git-backed skill can offer existing `agent-mcp.json` bytes from its pinned snapshot without adding a skill-manifest field. It conveys neither import authority nor verified source provenance.

This verdict uses the **amended E3 in MISSION-MCP.md at `534e384`**, announced by the convener at `$ropOGjw3dqPFz1fjx0hkU8dYrqD4iOS6X3jfs7L5y9o`. The original literal byte-contact scores remain visible. The amendment is explicit; no conclusion below depends on calling a native read credential-free.

## Evidence basis

- **S**: curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`, clean local checkout: core §§3–4; manager §§1,6; environments preamble, §§1.3,2.2,2.3,5.8,7.8,10.3; `schemas/v1/common.schema.json` `$defs.mcpRequirement`; `agent-mcp-v1.schema.json`; COMPATIBILITY.md; GOVERNANCE.md.
- **I**: curator `5234cf38833554542e68afade15951c6e56ed89e`, clean local checkout: `internal/mcp/mcp.go:24-61,245-287`; `internal/contextmaterialize/mcp.go:31-107`; `internal/envprofile/managed.go:205-229,298-364`; `internal/envprofile/surfacing.go`; `internal/install/install.go:1582-1605`; `internal/marker/marker.go:253`.
- **C**: supplied csk proposal §§1–5, slice-1 decisions D1/D5/D6/D7 and A4/A6, curator review H1–H4 and S2/S3. These are proposal/review evidence, not implemented-client certification.
- **F1**: [launch universe finding](../findings/f-launch-universe.md); **F2**: [opaque provider finding](../findings/f-opaque-provider.md). Each records independent confirmations; cross-host challenge remains pending.

External clones were not pulled because the sandbox makes them read-only. No web, builds, tests or actual credential/config-store reads were performed. Source-recorded native facts keep their original verified/docs-confidence labels.

## Rubric table

B is BASE as written. B+ retains its authoritative package/endpoint requirement but adds scoped evidence, protected assertions/consent, honest static-versus-recorded-origin labels and governed schema changes. N retains named requirements and existing operator-selected provisioning, with scoped local binding/evidence. N+A adds the optional shipped declaration. S-only restricts the dependency operation to secret-free managed metadata and assertions, foregoing arbitrary native reads/writes. K is the tool-capability alternative without manager live probes. G is the manager-owned authenticated gateway.

| Design | E1 | E2 | E3 amended | E4 | E5 | E6 | E7 | E8 | Total | Original E3 / total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| B: base as written | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 5 | 0 / 4 |
| B+: repaired authoritative identity | 0 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 10 | 0 / 8 |
| N: named requirements + local evidence | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 13 | 0 / 11 |
| N+A: N + shipped declaration recommendation | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 13 | 0 / 11 |
| S-only: restricted metadata-only branch | 1 | 1 | 2* | 2 | 2 | 2 | 1 | 1 | 12* | 2* / 12* |
| K: tool-capability requirements | 0 | 0 | 2 | 1 | 1 | 1 | 0 | 1 | 6 | 0 / 4 |
| G: manager-owned authenticated gateway | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 2 | 5 | 0 / 5 |

S-only's conditional E3=2 concerns the expressly restricted dependency operation; it cannot be generalized to existing Curator launch/provision functionality. It needs a governed capability boundary and cannot silently claim unchanged manager §6 scanning. G is ineligible through E3=0. All native-inspecting candidates fail the original literal E3 gate; the amended gate is the one used for this comparison.

### Evidence for every row

- **E1:** S's requirement, declaration and manager configuration schemas are closed. B/B+ need manifest identity, declaration auth and local binding/state changes. N/N+A drop the first two but still need binding/status representation; zero new skill fields is not zero total schema work. The recommendation half A reuses schema 1, including its one-server limit. K introduces a new tool-contract format/namespace; G adds a runtime object family.
- **E2:** N reuses requirements, profile locks, materialization and policy, but scoped assertions and launch-aware evidence are new checker work. I changed round-1 N from 2 to 1 after astra-01's challenge (`$FhazSElgCy2Xe8UMZTxFMwc1V0y5fj9P-yJmdqqkeYs`). B+ also imports identity equivalence and lock ownership. S-only drops native scanning. K needs session tool inventory absent from S §6/I; G adds routing, lifecycle and backend ownership.
- **E3:** I reads/unmarshals mixed native files; C §§4–5 admits foreign credential literals. Amended 2 requires explicit bounded processing, no credential-value use/auth flows, and no raw argv/URL/env logging, surfacing or persistence. Metadata-only errors remain metadata-only even on malformed input. A whitelist of field names is insufficient because arbitrary argv/URL can contain credentials. These bounds are part of N/N+A/B+/K as scored; B has not stated them completely. G forwards backend credential values by construction.
- **E4:** F1/F2 refute B's universal claim. Corrected candidates support provider sources through effective target evidence or explicitly labeled reliance, not new client APIs. This is coverage for a client/launch that can expose the provider, not a promise that pi gains MCP or strict Claude begins reading excluded native files. Unsupported/excluded combinations remain unsatisfied. K's tool inventory is not universally visible. A cloud connector need not expose a backend endpoint that G can route.
- **E5:** N/N+A preserve current portable skill bytes; deployments/provisioning remain local. Existing partial-client baselines reject new unknown manifest schemas (S COMPATIBILITY), a real cost for B/B+. K adds a tool-contract lane with provider-specific names/semantics. G requires the gateway environment. S-only uses the same named manifest but a narrower optional evidence lane.
- **E6:** B leaves unknown, alias authority and effective precedence unresolved. Corrected candidates label observed/asserted/unknown/known-negative separately, retain per-target results, protect consent and refuse contrary authoritative evidence. K remains underdefined at install time. A gateway can truthfully report only gateway configuration, but does not establish every backend; I score 1 rather than assuming every possible gateway must lie. C D1's consent-free HTTP rule is not proof of the base's consent-before-write promise.
- **E7:** S COMPATIBILITY/GOVERNANCE provide the path, but B supplies no closed identity/equivalence/binding grammar. N/N+A/B+ have bounded shapes and writable cases, but a complete binding/status grammar, marker migration and vectors are not frozen. K lacks a closed capability meaning; exact tool names do not establish equivalent semantics. G is describable but much larger. No forecast is scored as an implemented conformance result.
- **E8:** Following rubric seat `$mTl0E_Eso4-XNeWtQR8osepFdQ7_K2nPIEFeKZsH2u4`, the common case is an already suitable configured provider: N/N+A need zero actions when observable, one scoped reliance decision when opaque. S-only requires assertions for otherwise readable native providers. B/B+ may require extra identity/alias resolution. G offers one client entry. For a new provider, N can require manual package/policy wiring; A reduces discovery work but cannot bypass source admission, consent, native authentication or unsupported auth mapping. No universal one-click first setup is claimed.

N and N+A tie under this coarse rubric. I prefer N as the required core and A as a separable convenience, not an extra obligation in the minimal contract. The comparison does not prove that optional A is always needed.

## Zoo and evidence contract

| Provider source | Evidence that can count | Limit / operator action |
| --- | --- | --- |
| Hand-written native config | Bounded static projection in the selected native context | Does not prove auth, connection or executable identity; native mixed-byte handling disclosed |
| Client plugin | Existing safe report/metadata when available | Otherwise scoped reliance; no plugin install or client API change implied |
| Cloud connector | Existing safe client report when available | Otherwise asserted reliance with configuration/auth unknown; never silently provision a duplicate |
| Curator profile | Existing lock, adapter selector, marker and channel evidence | Claude strict exclusion and OpenCode override residual still apply; profile membership alone does not establish every launch's effective set |
| csk entry | Same static evidence as a hand-written entry when effective | Requirement use conveys no ownership; foreign equality can satisfy a check while a provision request conflicts (D6) |

`any` needs one accepted target; `all` needs every target. Unknown targets remain visible when `any` succeeds elsewhere. Assertions must identify the requiring skill/requirement and actual target, so two unrelated skills using `docs` do not inherit one global assertion silently. A name is an author-chosen label explained by its hint/documentation, not a globally governed capability identifier.

Contrary evidence must concern the same bound provider and selected launch. Absence in the six native files alone is not proof of absence of an opaque connector. Only authoritative complete evidence, or a channel's explicit exclusion, can establish that negative. Known disabled/mismatched/excluded providers cannot be waved through by assertion. Assertion state must never be written into legacy `FoundIn` as if observed; marker/status representation requires governance. Existing §6 semantics and documentary transport remain unchanged in their old lane.

## Authentication, acquisition and ownership

Native clients retain OAuth and secret handling. Schema-1 `agent-mcp.json` has no auth field or HTTP header binding. Section 5.8 emits argv or URL, while `env_names` only requests launch passthrough: it does not tell the client which HTTP header uses a token. Native operator configuration can satisfy a native launch; it cannot satisfy strict managed Claude when that configuration is excluded. Unsupported managed materialization remains explicit, or a names-only routing extension is governed separately.

The optional shipped declaration is inert advice, imported only by an operator-selected plan through existing package policy. Section 2.2 remains git-only: a path/local skill snapshot is not an admissible managed declaration source. Root schema 1 offers one server; multi-server authors can use existing companion context packages. Malformed sidecar parsing may warn and remain inert, but source-audit blocking findings do not disappear. The existing declaration surfacing row also omits HTTP URL (§2.3); exact-plan consent still needs safe endpoint review, not a blind row reuse.

The skill snapshot fixes bytes; it does not grant authority or verify source authorship. Environments §1.3 expressly says a lock is a record, not an authorization token or provenance proof. Recorded origin, verified signature policy, and operator consent are separate claims. Native writers stay outside marker-owned managed homes and reserved channel files, using their own protected per-entry ownership.

## Smallest changes to the base

1. Keep current `hint`, documentary `transport`, and `required_in`; remove authoritative `server.package`/`server.endpoint` and new auth-class wire fields from this slice.
2. Reuse operator-selected `requires.mcp`, profile resolution and existing declarations for managed provisioning. Keep native writers separately reviewed. No requirement grants write, execution, allowlist or credential-routing authority.
3. Add the smallest governed operator-owned binding/evidence contract, combining alias and opaque-provider reliance, scoped to requirement and selected launch. Revalidate observable fingerprints; changed scope/content requires renewed reliance/consent. Do not place authority in repository-controlled state.
4. Define observation, assertion, unknown and authoritative negatives, aggregation and launch precedence. Use existing managed profile/channel evidence. Keep assertion labels in status and markers, never masquerading as old observed `FoundIn`.
5. Apply the amended E3 bound explicitly, retaining the original literal limitation. Native auth remains native; no health check, proxy or credential broker is added.
6. Optionally surface a same-snapshot existing declaration recommendation for a git skill. Keep it removable without changing dependency semantics; enforce all admission, audit and consent gates on actual import.
7. Freeze the governed binding/status grammar and positive/negative vectors before claiming E7=2.

## Proof status

B is not proved elegant. N/N+A lead this seat's amended-E3 comparison and both beat retaining authoritative package identity. Same-host scores from astra-01 differ by at most one row point; that is useful corroboration, not the mission's cross-host proof. The mini adversarial seats have not yet supplied a complete independently evidenced score vector in the material I have received. Final proof status remains pending and must be updated before PARK.

## Round-3/4 refinement: unchanged preference and scores

The revised composite sketch at `$e5s3ZnvCckXlXR8HgOhJu7XHsOUk3W_5O2ueV0Ga37I` accepts this seat's provider-selector/requirement-identity/context-change objections. The scored N/N+A now expressly chooses a successor of the existing protected manager-configuration family and a marker successor, not an uncounted standalone authority-record format. That retains E1=1; a standalone family would score 0.

Reliance may batch an enumerated set of exact skill requirement identities in one operator decision. Changed members or targets do not silently inherit it. Provider provisioning consent has a separate lifecycle: a new skill's use of an unchanged observed provider is not a new write or credential route and does not require fictional per-skill runtime permission. Bindings assert reliance, never enforce tool access.

Evidence belongs to each requirement/target/selected-launch tuple. Old found-agent markers establish only **legacy native presence**; they need fresh scoped observation before supporting a new-lane claim. Manager-recorded origin is orthogonal provenance metadata, not an independent way to establish current satisfaction or verified source authenticity.

Completeness must be adapter-specific. A present, applied strict Claude channel can exclude other native MCP entries; a profile name alone cannot. Section 5.8 emits no MCP fragment for an empty resolved set. OpenCode retains higher-precedence project overrides, so a valid lock/marker alone is not complete evidence of the effective entry. The supplied Codex trusted-project residual remains an explicitly unverified input to this review. E7 stays 1 until a closed completeness table and resulting vectors settle these cases.

A-standalone was narrowed explicitly by its author: only shipped recommendation, metadata-only candidate notice and operator-selected existing provisioning; checking remains legacy §6. I score that separate subset **[2,2,2,0,2,1,2,1] = 12**, original E3=0 and original total=10. E1/E2/E7 benefit from existing shapes and a bounded recommendation convention; E4=0 follows the literal anchor because an invisible connector remains excluded, and E6=1 retains legacy checking limitations. It must not borrow N's checker/assertions for free. It is a useful independently shippable subset, not the complete zoo solution. N/N+A remain tied at 13; the tie is deliberate, not an arithmetic claim that the optional recommendation adds a point to the already-configured E8 ceiling.

Under cold first setup, N/N+A's E8 is 1 rather than 2 (selection/consent and client auth; no universal one-action setup), for totals of 12. The primary 13-point comparison uses the rubric seat's explicit already-configured common case. Wonder-02 corrected its earlier erroneous N+A total from 14 to 13 at `$biOtkvfKBYfAg78ALG0Qkbz0DpsF-rAKHaxk3E4VC1E`.
