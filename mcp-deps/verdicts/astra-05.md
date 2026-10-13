# astra-05: authentication and trust, independent adversarial verdict

Seat: `ivmbp_swarma-mcp-deps_astra-05`, second independent five, ivmbp. Date: 2026-10-14.

## Independence and evidence boundary

The initial scores below were written before reading any first-five verdict file or topic body. I had read the mission, base, all three inputs, the room topic index, and the local specification and implementation sources. The topic index exposed candidate names, not their arguments or scores. This section preserves that initial assessment; later debate is recorded separately.

Review repository baseline: `b5e7dabf6f548e727a9933e2e6371d7b6a0d83f7`. Local read-only source pins: curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`; curator `5234cf38833554542e68afade15951c6e56ed89e`. These are local source observations, not a claim of fresh remote main or of executed conformance tests. Source clones are outside the writable sandbox; I did not pull or modify them. The requested initial review-clone `git pull --rebase` failed with an SSH connection closure on port 22. No credentials or real native configs were read. No web, builds, tests, task-board writes, or worker spawns were used.

## Initial independent scores

Scores use amended E3. Original-E3 differences follow the table.

- **B — base as written:** Require / Provide / Bind, with package or endpoint identity in the skill, aliases, optional provisioning and auth classes.
- **N — named requirements with local operator evidence:** preserve the portable v5+ requirement exactly; select/provision providers separately in operator policy. Distinguish observed configuration from a protected, scoped operator assertion for opaque providers. An assertion is not authentication or measured availability. No skill authority over bindings or provisioning.
- **I — repaired identity-bearing base:** retain the new skill selector, but distinguish package provenance from recipe similarity, close endpoint grammar, scope protected bindings to the consumer and effective launch, and adopt N's evidence and consent boundaries.

| Row | B | N | I | Evidence and justification |
| --- | ---: | ---: | ---: | --- |
| E1 New concepts and fields | 0 | 0 | 0 | B's optional `server` hides a selector union, local binding authority and a declaration auth extension. N still needs a new protected local evidence contract; it earns no free 2 merely by leaving the skill schema alone. I retains both additions. Existing requirement and declaration objects are closed (common schema `mcpRequirement`; environments §2.2). |
| E2 Reuse | 1 | 1 | 1 | All reuse §6 verification and §2.2/§5.8 acquisition/materialization, but local evidence/consent are additional machinery. Environments §2.3 only surfaces declarations; it does not grant protected exact-plan consent. |
| E3 Secrets, amended | 1 | 2 | 2 | B forbids active auth/health checks but does not bound native-file parsing or raw command/URL handling. N/I explicitly use the bounded metadata-only path below. Curator `entriesInFile` reads whole files and retains entry maps; the csk input §§4–5 already explains the necessary foreign-byte boundary. |
| E4 Zoo | 1 | 2 | 2 | B's unqualified satisfaction rule cannot account for unobservable cloud/plugin state. N/I permit a separately labeled operator assertion without a client change, tied to an actual supported launch; known exclusion/disable defeats it. Environments §7.8 makes configuration existence different from launch availability. |
| E5 Portability | 1 | 2 | 1 | Names retain the existing portable manifest; local provider choice can vary. A package coordinate identifies a source, not the equivalent cloud service; a fixed endpoint may identify a tenant-specific route. I repairs safety but keeps that coupling. |
| E6 Honest failure | 1 | 2 | 2 | B requires consent and disclaims authentication but leaves opaque evidence, authority and precedence unresolved. N/I keep unknown distinct, label assertions, preserve known negative evidence, and require consent before protected assertion creation or config publication. |
| E7 Specifiability | 0 | 1 | 1 | B leaves identity equality, range-to-digest, aliases, auth schema and legacy compatibility open. N/I have a describable bounded contract and vectors below, but neither is an accepted closed schema with executable conformance evidence yet. GOVERNANCE requires prose/schema/vectors and a trust decision record. |
| E8 Operator effort | 1 | 2 | 1 | B/I may require binding plus provider selection plus native sign-in for a usable deployment. N's normal already-configured provider costs zero actions; opaque provider assertion or new provisioning can be a single plan approval. First-time sign-in stays a separately disclosed client operation. |
| **Total / 16** | **6** | **12** | **10** | N is preferred among these defined candidates; no universal optimality claim. |

Under original literal E3, B/N/I are all **0**, giving totals **5/10/8**. Parsing a mixed native file can read a credential byte even when it neither interprets nor releases the credential. Amended E3 permits that bounded incidental handling; the original rule is not honestly met by a native reader/writer design.

A manager auth proxy is rejected at the E3 gate rather than treated as a close competitor: if it terminates OAuth, carries tokens or authenticates requests, it violates the owner's desired responsibility boundary. A transparent transport that avoids credentials does not solve unavailable provider evidence or consent.

## Trust conclusions and attack cases

### 1. A variable-name allowlist is not a server-recipient allowlist

Environments §10.2 emits the sorted **union** of `env_names` for the adapter's MCP set; §7.8 lets the launcher add those names to the client's process environment. §5.8 deliberately writes no per-server env member. Implementation agrees: `internal/contextmaterialize/mcp.go:MCPEnvNames`, then `internal/envprofile/managed.go:2444–2458` applies `ResolvePassthrough` to that union.

Counterexample: approved server A requests `A_TOKEN`. Later an approved declaration B has `env_names: []`. The launch still receives `A_TOKEN`; nothing in this contract confines that variable to A's child. A client that inherits its environment to both stdio children can expose it to B. This is a contract-level possible path, not a newly executed native-client exploit. Removing a name from B's declaration does not remove the recipient risk.

The smallest correction is honest launch-wide consent: show the effective env-name union and its shared inheritance boundary when admitting another executable server; changes to the approved recipient set or env-name set invalidate that plan. Continue to let the client/launcher own actual values. Do not invent a manager proxy to claim isolation. If the operator needs per-server confinement, require independently supported client/launcher isolation and refuse the stronger claim when unavailable.

Hardened also does not automatically mean bounded passthrough during every rollout: manager §7.1 and environments §10.3 refuse explicit `null`, while absent still follows `s4-warn` versus `s4-enforce`. Report the effective rollout and policy, not just the `hardened` label.

### 2. A package, its recipe, a process, and a service are different identities

Environments §2.2 explicitly says a bare binary allowlist cannot bound `npx`, `uvx`, `node` or `sh`; args select programs. Conversely, identical command/args do not prove the configured entry was acquired from an approved declaration snapshot, nor that the runtime executable has unchanged identity. PATH and transitive runtime downloads remain outside the declaration digest.

Only verified acquisition/ownership evidence may assert declaration provenance. A native entry can offer observed recipe compatibility; it cannot mint provenance by looking identical. An operator may accept an equivalent provider, but that is an explicit separate assertion, never a digest-equality result or a package-allowlist waiver.

### 3. Same name is legacy configuration evidence, not trust in a publisher

Core §4 and manager §6 deliberately define a name check. A hostile checkout can provide a same-name entry; the legacy check can report it configured, with the required project-trust warning. No package trust, credentials, sign-in, runtime compatibility or permission grant follows from that result. A new native writer must not overwrite an identically named foreign entry merely because the requirement matches it (csk decisions D6).

Strengthening every legacy result into verified identity would silently redefine released bytes. Keep its reported scope truthful; introduce any stronger identity/effective-launch predicate through governance. An alias in repository data cannot authorize a protected binding or laundering of a disabled/unknown provider.

### 4. Secret-free manager activity needs a concrete foreign-byte boundary

No auth execution, credential stores, env expansion, endpoint requests, credential-presence checks or raw native dumps. Native reads are size-bounded and privately parsed; immediately project only admitted metadata. Unrecognized or secret-bearing identity syntax becomes unknown, without printing the raw field. Do not persist raw argv, URL, env, headers or whole foreign entries in a binding, log or diagnostic. Do not hash secret-bearing literals into a durable identity and call that metadata-only.

For native writes, private transient whole-file staging required for lossless atomic replacement is the explicit csk §4 exception; it remains adjacent to the protected target, is not a reusable backup/cache or evidence artifact, and is removed after recovery. The contract must state that exception rather than promise bytes were never touched. Existing audited declaration surfacing and arbitrary foreign native entry surfacing are different trust domains.

### 5. Consent must bind what will actually gain authority

Protect consent outside attacker-controlled checkout bytes and bind canonical consumer, targets, scope, writer interpretation, admitted source/declaration digest, endpoint or execution intent, env names and affected effective launch. Revalidate all relevant gates before publication. Replaying a consent after a range update, target expansion, endpoint change, package-policy revocation or launch-channel change must fail. Package signatures and allowlists establish admission constraints, not universal execution consent.

The base's endpoint is only an identity hint unless separately selected by the operator. An endpoint cannot gain network access through a supposedly read-only identity check. Remote `auth:none` does not prove the native client has no stored credentials; manager claims must stay about declared references, not actual native auth state. The csk D1 no-prompt HTTP subset and the base's consent-before-any-write are distinct policies, not interchangeable implementations of E6.

## Preferred design and smallest changes to the base

Prefer N: keep the existing named skill requirement and put provider selection, provisioning and trust evidence at the operator's local boundary. Auth stays wholly with client/launcher; no manager auth broker or health probe.

1. Drop normative package/endpoint identity from the skill for the minimal slice. Existing hints may recommend a provider without granting selection authority. Keep separately selected declaration packages and existing managed materialization.
2. Specify one local evidence contract, including asserted versus observed provenance, consumer/agent/launch scope, invalidation, known-negative precedence and the no-credential bound. A names-only legacy result remains available; a launch-aware assertion is an explicit new extension, not a covert §6 change.
3. Make provisioning an independently approved operation, with package admission and signing policy unchanged and managed-home/native-writer ownership boundaries preserved.
4. Treat env passthrough as launch-wide. Require the plan to disclose the shared union and changed recipient set; never describe `env_names` as per-server isolation.
5. Defer `auth` fields/header mapping to a separately governed declaration revision only when provisioning needs them. The current schema-1 declaration and §5.8 bytes cannot express arbitrary HTTP env-header auth; a configured endpoint may still satisfy an existing requirement via client-managed setup.

Conformance work should distinguish: foreign same-name collision; identical recipes from different packages; stale range/digest consent; disabled/shadowed provider versus assertion; opaque provider without assertion; `any` with one observed match plus one unknown versus `all` with an unknown; no-channel client; literal secret hidden in URL/argv; project-forged bindings; a newly admitted stdio server with no env names in a launch carrying another server's variable; hardened plus absent passthrough policy under both S4 profiles; revoked package or env policy; and status after failed publication.

## Debate updates

### Round 1 comparison after independent freeze

The initial assessment above is preserved in signed, locally verified commit `ff552b3`. A bounded SSH retry successfully updated the review clone to `ebdc698` before that commit; the earlier network failure was transient. Only after the signed checkpoint did I read astra-02's verdict and the room discussion bodies.

**Current preference: N, optionally supplemented by corrected inert recommendation A.** Astra-02's defended N is more concrete than my initial independent record: authority belongs to a governed successor of an existing machine-configuration family, not a new standalone authority-file family. Status can be transient and scoped; no portable install-marker bump is mandatory unless new evidence is persisted there. On that explicitly narrowed same-design contract, E1 rises from my independent 0 to **1**, and all other N scores remain unchanged:

| Current candidate | E1 | E2 | E3 amended | E4 | E5 | E6 | E7 | E8 | Total amended | E3 original | Total original |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| N, existing configuration family | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | **13** | 0 | **11** |
| N + corrected A below | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | **13** | 0 | **11** |
| A alone, unchanged legacy checker | 2 | 2 | 2 | 0 | 2 | 1 | 1 | 1 | **11** | 0 | **9** |

The base remains 6 and I remains 10 under my initial amended scores. This is not silent rescoring of the independent checkpoint. My current N row matches astra-02's first-five vector exactly; even the independently formed N vector differed in only E1, by one. This meets the mission's pairwise independent-five row tolerance for this bounded candidate, not a universal optimum or implementation qualification. The matching cross-host astra-12 result is additional corroboration, not the basis of my original scores. Cold setup changes N/N+A E8 to 1: total 12 amended, 10 original.

E4=2 means all five provider-source categories can supply observed evidence or labeled operator reliance **within a supported selected launch**. It does not mean a client without MCP capability becomes capable, a strict channel admits a native server it excludes, or unknown connection/auth state becomes observed. `any` needs one acceptable per-target result; `all` needs every target. Provider selectors distinguish a native same-name entry from an unrelated cloud connector. A known negative invalidates reliance only when it authoritatively addresses that selector and launch; mere absence from native files says nothing about an opaque provider. Opaque internal drift cannot be measured by this design and remains explicitly unverified.

**A's exact scope:** an optional skill-root `agent-mcp.json` recommends bytes from the already resolved snapshot. Discovery is metadata-only; raw argv/URL display cannot inherit advisory skill audit as if it were strict MCP admission. Explicit selection still needs canonical Git identity, MCP allowlist, source signatures, strict profile audit and protected consent. A local/path skill cannot bypass §2.2 by carrying a sidecar. Select the exact resolved revision; a declaration version need not equal the skill's tag. Multiple recommendations may use an existing companion context package. No directory scan convention, auth schema or transitive authority is implied. These are required corrections to the original A topic, not properties of unmodified current code.

A alone has E4=0 because the unchanged native checker excludes opaque connectors. It keeps E6=1 for legacy presence/launch limitations. E7 remains 1 in my assessment because the joint-closure name constraint needs an explicit supported-path/refusal contract; N+A already carries that same E7 debt. Astra-02's A-standalone E7=2 and total 12 precede this adversarial qualification; the difference is one point, and neither A-alone score changes my choice.

### Confirmations and additional discriminating cases

- My launch-env counterexample independently agrees with astra-12's two-set challenge `$GZBY9lcDf42utPLdr5lWYmjFhFsu_NRu3vLxiPDYuww`, astra-02's acceptance `$PMpF2s8kuwv8JuapOho3DNn2vgIQ1-KZaSLeNpPlumE`, and astra-01's confirmation `$8vlD9K1dEBlA3K2U7MljLO727hSFzZBFNE8V3hSQrbs`. My own corroboration is `$kWsgP-hAvuOG5nO9QulLw7A8VHmQWaHLW_KEfJEA0Lo` in `f-consent-binding`. A single batched approval may cover the shared launch trust domain with its visibility limits. The MCP union is an additive contribution, not necessarily the client's complete inherited environment. Neither credential values nor foreign runtime policing are required.
- The existing no-raw-output bound must include the native `command`/argv[0] field, even a syntactically bare string. `internal/mcp/mcp.go:142–145` currently echoes it. Manager §6 requires the warning but does not require printing the raw value. An arbitrary program name is not guaranteed secret-free. This agrees with the correction acknowledged by astra-03 in `$fnkj2eHkDYXUPjF0V74XOw9Bxlj0V4BjmZ_7HiQaDq8`; it is a required future contract/implementation fix, not a present guarantee.
- The managed HTTP env-auth limitation cannot be solved merely by pointing to an existing native entry. The selected launch must actually include that native route; an applied nonempty strict Claude channel excludes it. URL/type-only §5.8 materialization and the implementation renderers have no header binding. Native provision eligibility and requirement satisfaction need the same launch boundary.
- I source-checked astra-04's optional-A collision challenge `$iUc_uDX_kiEwtByLrYzC4qpzhIODJGkvPXIehrKehkk` and astra-06's confirmation `$cjkXXsAKqa1RgA871RL9IIK9QBe3kTfn9G17XP4UnYU`: `internal/contextresolve/contextresolve.go:316–318` keys by name; `add` at 409–420 preserves the first kind; `build` around 915 emits one kind per selected name. `internal/envprofile/managed.go:205–226` materializes only MCP-kind members. Co-locating files does not make same-name skill and MCP packages both load in one closure. Corrected A must require distinct package names in that joint closure or explicitly defer/refuse the collision. No implicit rename, dual-kind resolver or untested success is credited.

No duplicate finding file is needed: the trust/byte cases strengthen `f-consent-binding` and `f-secret-boundary`; the A collision stays with its originating topic/seat. E7 remains 1 until the evidence grammar, admission/reliance policy (including any system policy forbidding assertion-grade evidence), aggregate exposure rules, compatibility handling and discriminating vectors are governed. The collective remains active until convener PARK.
