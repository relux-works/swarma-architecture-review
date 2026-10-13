# astra-02 — authentication and trust verdict

State: provisional, round 3. Host: ivmbp. No implementation or runtime qualification is claimed.

## Position

Prefer **named requirements plus protected local evidence**, the `alt-names-local-evidence` candidate. Keep `dependencies.mcp_servers` unchanged; let the operator choose existing native/plugin/cloud configuration or explicitly selected declaration packages. A requirement is neither installation authority nor a credential grant. The dependency feature should not acquire an auth broker, health checker, server process manager, or parallel package resolver.

The base has the right separation of requirements, provision, and client-owned authentication, but does not yet prove its advertised identity, minimality, secret boundary, or full-zoo claims. Concrete alternatives have been compared below. The preferred direction is not yet a proved winner: different-host scoring remains open. This verdict applies the convener's explicit E3 amendment at review-repository commit `534e3849b3fca07c2479222886aacb34808e5bcc`, and preserves the original literal scores as required by that amendment.

## Evidence basis

Sources were read locally without modification or credential access:

- curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`: core §4; manager §§1, 6, 7.1; environments §§1.3–1.4, 2.2–2.3, 5.8, 6, 7.8, 9.1, 10.3, 12.1–12.2; `common.schema.json` `mcpRequirement`; `agent-mcp-v1.schema.json`; COMPATIBILITY and GOVERNANCE.
- curator `5234cf38833554542e68afade15951c6e56ed89e`: `internal/mcp/mcp.go`, `internal/contextmaterialize/mcp.go`, `internal/envprofile/envprofile.go`, `surfacing.go`, and the managed fragment assembly in `managed.go`.
- `BASE-DESIGN.md` and all three `inputs/` documents. Historical native-client facts in those documents were not rerun.
- CIP-0006/0010/0011 were inspected to avoid confusing proposed operator settings and credential/executor work with already normative MCP dependency machinery. Their pending qualification and schema work are not evidence that this feature already exists.

Source clones are outside the writable sandbox; their clean local checkpoints were used without pulling. No builds, tests, web requests, real native-config reads, or auth operations were performed.

## Designs compared

- **B — Base as written:** new `server` package/endpoint identity, recipe-or-digest matching, aliases, optional provision, and auth class metadata.
- **R — Repaired identity-bearing base:** preserve identity requirements, but add governed immutable resolution/provenance, selected-launch matching, protected assertions for opaque providers, exact-plan consent, and explicit bounded native-file handling. This is a substantial correction, not a one-field implementation.
- **N — Named requirements/local evidence:** no new skill field or auth declaration. Retain the named requirement; combine alias selection and opaque-provider reliance in one protected operator record scoped to the requirement, consumer, agent, and launch. Home that authority in a governed successor of the existing machine-configuration family, with per-target result evidence in a marker successor; curator-spec assigns versions. This is not a new standalone authority-file family. Provision through existing selected profiles/packages or a separately reviewed native writer. Unknown without reliance fails. Existing incompatible/disabled evidence is not overwritten by an assertion.

`alt-names-local-evidence` was independently proposed by astra-01 in event `$-Q10wx4Zpfeu7dJwMNuhMSMvYC2uHkm8FrVKsGK0oy0`; it matches this seat's preferred trust boundary. Native-inspecting N is scored below. A variant that never inspects arbitrary native files may improve literal E3, but its trusted metadata ingress and compatibility with mandatory manager §6 reads have not been specified; it is not credited as a completed solution.

## Rubric

Scores evaluate the described design contracts, not implementation completion. Every row uses the mission's 0–2 range. E3 has an explicit sensitivity analysis; its original literal score is included in the first total, and the amended score in the current-rubric total.

| Criterion | B | R | N | Evidence and reason |
| --- | ---: | ---: | ---: | --- |
| E1 New concepts/fields | 1 | 0 | 1 | B adds requirement identity, declaration auth, and binding state, despite its one-field claim; R additionally needs specified pin/provenance semantics; N removes the skill/declaration changes but honestly counts a new protected evidence record. Closed schemas and `f-schema-budget`. |
| E2 Reuse | 1 | 1 | 1 | All introduce some checker machinery. N keeps requirement grammar and existing profile resolution, allowlist/signer/audit gates, and provisioning channels, but its protected scoped evidence is still new. Round-2 correction applies the rubric's "only existing machinery" literally. Environments §§1.3–1.4, 2.2, 5.8, 6. |
| E3 Literal no credential-byte contact | 0 | 0 | 0 | All three native-inspecting forms read potentially credential-bearing files. `mcp.go:240–288`, supplied csk §§4–5, `f-secret-boundary`. The zero endpoint says the manager touches values. No authentication execution is necessary for this counterexample. |
| E4 Zoo | 1 | 2 | 2 | B's opaque-provider identity binding does not establish configured/enabled presence. R/N admit separately labelled operator reliance without a new client API. This is coverage by reliance, not universal automatic observation. `f-opaque-provider`; manager §6 and environments §7.8. |
| E5 Portability | 2 | 1 | 2 | B's intended operator binding can retain one manifest across machines, although underspecified. R's meaningful source/endpoint identity constrains substitutes; weakening it by waiver must be explicit. N leaves deployment selection local and skill requirements unchanged. Core §4; `f-package-is-not-service`. |
| E6 Honest failure/consent | 1 | 2 | 2 | B promises consent/no auth checks, but identity evidence, scope and authority invalidation remain ambiguous. R/N expressly fail unknown, preserve known negatives, label reliance, and require protected exact-plan consent before their provisioning writes. `f-consent-binding`, `f-launch-universe`. |
| E7 Specifiability | 0 | 1 | 1 | B has no closed binding grammar, identity canonicalization, or lock owner. R/N identify a governable contract and concrete negative vectors, but neither has frozen all schema/state semantics. COMPATIBILITY, GOVERNANCE; confirmed findings. |
| E8 Operator effort | 1 | 1 | 2 | Common case is now explicitly the rubric seat's suitable already-configured provider: N needs zero actions when observed or one scoped reliance decision when opaque. Cold setup still scores 1: provider selection, consent, and native authentication may require separate steps. B/R identity resolution can add setup even for a functionally suitable provider. Inputs csk §§2, 5. |
| **Literal total** | **7/16** | **8/16** | **11/16** | **All fail the literal no-zero E3 gate under this seat's reading.** |
| E3 operational non-management, separately | 1 | 2 | 2 | B omits the native identity matcher's handling boundary. R/N explicitly forbid auth execution, value lookup/expansion, credential-store access, probes, persistence/logging/egress, while permitting bounded private handling of existing bytes. This is a different guarantee. |
| **Current amended-rubric total** | **8/16** | **10/16** | **13/16** | N leads among these designs under the explicitly amended E3. Cross-host proof remains pending. |

Rubric-seat wonder-02 confirmed the byte-contact contradiction, initially assigned literal E3=1 (event `$SNRLfvcWtHxonUgOrpTBaUZnHD9ClzN9jCkBSf7RasI`), and subsequently corrected that original score to 0 in `$W8MSN-HUtmafiXSywrR9ILkYrGHk-7CKJeLiVArHVeU`. The convener resolved the evaluation boundary explicitly in MISSION-MCP. The amended total is not a proof under the original verbatim rubric; the amendment and original score remain visible.

N's E3=2 requires its explicit handling boundary: never resolve/expand a credential, access a credential store, execute authentication, or probe a server; parse foreign native bytes only privately and within bounded reads; do not persist, log, or surface raw foreign argv, URL, env, document fragments, or parser exceptions. Use validated metadata-only evidence/diagnostics. Arbitrary `args` and `url` fields can themselves contain secrets, so a field-name whitelist is insufficient. A separate native writer's private preservation of existing bytes is not delegated secret management and must retain the supplied csk handling limits; it is outside the pure requirement operation.

### Concrete alternatives submitted during round 1

Wonder-01 proposed three alternatives: A (skill-root `agent-mcp.json` recommendation, event `$Oi-yLH129Y6zJ-z0AeVV4E84AOrddTDk6HrcmMGsm4M`), T (tool/capability requirements, `$PzZOjpCVB5M21uS8891NqqjxCDYck2IuhK1HxwTxTqE`), and G (manager-owned authenticated gateway, `$hKTg60s0b50i-kQHeKXD6UWd9VLbQNlygcTkZfZG5ss`). These are actual submitted candidates, not hypothetical rejection targets.

**A+N** means A with N's protected evidence contract and the explicit trust corrections below. It is a complement to N, not a different verification architecture. **A alone** now means the author's corrected standalone scope in round 3: ship/discover/recommend/provision, with the legacy native checker unchanged. It cannot borrow N's observation/reliance mechanism or solve opaque-provider evidence by itself. The first submitted A scored 12 with different weaknesses (E3=1 before the display correction); the current row below supersedes that initial row.

| Criterion | A alone | A+N corrected | T | G | Evidence and reason |
| --- | ---: | ---: | ---: | ---: | --- |
| E1 | 2 | 1 | 1 | 0 | A reuses the existing declaration file with no skill-schema field; A+N still counts protected evidence state. T needs a new manifest/version lane. G introduces a runtime/protocol family. Core §3, environments §2.2, schema-budget finding. |
| E2 | 2 | 1 | 1 | 0 | A uses an existing snapshot and selected profile/MCP admission; A+N adds scoped evidence machinery. T lacks reusable current tool-inventory verification in §6. G owns backend process/auth/session machinery absent from the checker. |
| E3 amended | 2 | 2 | 2 | 0 | Revised A and A+N use metadata-only discovery and strict MCP admission before detailed display; their bounded native handling is explicit. T forbids manager probes. G deliberately forwards backend credentials. |
| E4 | 0 | 2 | 1 | 1 | A alone's unchanged native checker excludes opaque connectors: the mission's zero anchor applies. A+N closes that gap by labelled reliance. T has no generic current client tool inventory in local evidence. A gateway cannot assume access to account-only cloud connectors. |
| E5 | 2 | 2 | 1 | 1 | Inert schema-1 sidecar degrades gracefully with the existing manifest. T tool names have no portable equivalence across providers. G couples clients to its deployment. |
| E6 | 1 | 2 | 1 | 0 | A grants no write authority but intentionally retains legacy name unions and checker limitations. A+N keeps unknowns and independent consent. T's strong connected/tool claim exceeds install evidence. G can mask unavailable backends and collapses native per-server controls. |
| E7 | 2 | 1 | 1 | 1 | Revised A has a bounded existing-file grammar, metadata-only discovery, exact revision/context route, independent admission and concrete vectors. N still owes complete evidence/policy grammar. T exact name sets can be closed without a registry, but trusted inventory/equivalence is unspecified. G is specifiable but undeveloped. |
| E8 | 1 | 2 | 1 | 2 | A improves first-setup discovery but does not cover opaque evidence itself. A+N uses the same explicit already-configured common case as N (zero or one action); cold setup remains 1. T still needs binding. G offers one entry, at unacceptable trust cost. |
| **Amended total** | **12/16** | **13/16** | **9/16** | **5/16** | A+N ties N on this conservative scoring; G fails the E3/E6 gates. |
| E3 original | 0 | 0 | 0 | 0 | A/A+N/T retain native-checker byte contact as submitted; G intentionally handles credentials. |
| **Original total** | **10/16** | **11/16** | **7/16** | **5/16** | Original literal gate fails; no original-rubric proof is claimed. |

The preferred composition is **N, optionally augmented by corrected A**. A lets an author ship exact recommendation bytes without a new `server` field. It is not required for an already configured provider. The source snapshot's pin is integrity, not MCP authorization: selected use still requires canonical Git-source/package admission, signer policy, strict audit, and consent. Recommend the exact resolved revision, not an independent skill version tag that might violate the declaration's version match. Path/local skill snapshots do not gain a canonical network identity; the §2.2 refusal remains. Multiple recommendations can use an existing companion context package; a new directory-discovery convention is unnecessary.

Round-2 score-vector refinement leaves N/A+N totals unchanged at 13: E2 moves from 2 to 1 because new binding/evidence is not existing-only machinery; E8 moves from 1 to 2 after naming the already-configured common-case assumption. Initial cold-start caution remains explicitly recorded rather than erased.

For A alone, this seat applies E4's explicit zero anchor because the unchanged checker excludes opaque providers. Wonder-02's declared partial-coverage interpolation gives A E4=1 and total 13; this one-point difference does not change N/A+N's score or this seat's preference. Both conventions must remain visible rather than implying exact numerical unanimity.

Wonder-01's revised D1–D6 sketch, event `$6Ju0U6dvorEvdtJ0MsUkDEFhhMjnZPdD4btQilsiQhQ`, makes bounded native parsing explicit and adopts source-kind/admission limits. E7 remains 1: its binding record still needs an exact requiring-skill/requirement identity rather than just the local name, and old marker labels cannot be promoted from legacy presence to selected-launch observation without a fresh check. Existing lock records state origin but are not authorization or provenance proofs (environments §1.3); admission gates remain separate.

The author's next revision `$e5s3ZnvCckXlXR8HgOhJu7XHsOUk3W_5O2ueV0Ga37I` accepts those corrections: exact enumerated requirement identities, provider selector, configuration-family successor, per-target/launch evidence, legacy marker limits, and display-only consumer attribution. This seat acknowledged it in `$VvwPuGr1bfxgC_TSwWBc2q7wRuPGrhQ5cRqeAXNWcSc`. The remaining E7 debt is the closed adapter-completeness and authority-policy grammar, not the already-conceded defects in the older sketch.

Further closed-grammar constraints from the debate: evidence is per requirement/target/selected launch, since one target can be observed while another is asserted. An opaque binding needs a safe unambiguous provider selector; a disabled same-name native entry is not authoritative evidence about an unrelated cloud connector. Name-only absence from §6 files cannot invalidate opaque reliance. Using a new standalone protected record instead of the existing configuration family would make E1=0 under the mission's new-format anchor; the score of 1 explicitly assumes the configuration/marker successor route above.

Acceptance and origin are separate axes, as the author's next clarification `$J1PqcY017z6kZyOpvDR5hRvp1aJmGaxJ9hKay561cOQ` accepts. Only scoped observed-effective evidence or explicit reliance can support the new acceptance decision; recorded origin is annotation. A disabled, missing, overridden or excluded effective entry does not become available because it has an old lock/ledger record. Managed completeness is adapter-specific and requires the channel actually be applied: a present strict Claude channel can exclude native entries; an empty profile name alone cannot prove a channel exists (§5.8); OpenCode and Codex retain their recorded precedence/residual qualifications.

The sketch clarification `$R2qT1zuemaAB6XGZYwcsy_Fh-ncIeE1HMRY5f8q64M4` is accepted with E7 unchanged at 1. Its selectors are matching identities, not byte fingerprints: native `(agent, surface, configured name)`, managed `(profile, lock member name)`, opaque `(agent, launch, operator label)`. Opaque reliance promises no durable detection of internal provider drift; revocation, context change, or a contrary authoritative observation of that selector ends validity. Only a present, actually applied strict Claude channel over a non-empty set supplies the stated exclusion evidence; §5.8 emits no channel file for an empty set. Assertion never replaces applicable source/signer/audit admission or suppresses a hardened refusal. Whether protected system policy additionally forbids assertion-grade reliance remains a governed choice. These points close the sketch questions but still require normative configuration/marker grammar and conformance vectors.

A's initial raw surfacing was challenged in `$bpz_PXkFPAIj-yPFT739a8vIRgIlW_9SUVlb_2-dvzE`: normal skill audit may be advisory (manager §7/§7.1), whereas MCP surfacing follows strict profile audit (§9.1). Safe candidate discovery must not print raw argv/URL from an unadmitted sidecar. Syntax invalidity can warn and leave the recommendation inert; actual secret findings keep their applicable blocking policy. This is a pre-display/admission condition, not permission to waive the ordinary source audit.

T is not rejected merely for lacking a global capability registry: exact strings can form a closed grammar. It loses today because current sources do not supply trustworthy, current, target-scoped tool inventory without connection/auth behavior. Reconsider only with such evidence. G remains rejected inside Curator; an independently operated gateway can be an ordinary external provider under N, requiring no dependency-manager auth subsystem.

## Minimum changes to the base

1. Remove normative `server.package`/endpoint identity from skill requirements. Existing `hint`, documentary `transport`, and `required_in` remain unchanged. A package suggestion may be informative only; it cannot select a source or resolve a range inside verification.
2. Replace generic aliasing/identity waiver with one protected operator evidence/binding contract. The repository may request a mapping but cannot approve it. Bind to the requirement identity, consumer and selected launch; invalidate on changed/widened observable inputs. An opaque-provider record means reliance, never observed configuration or authentication.
3. Evaluate evidence in the selected launch universe. A native server ignored by Claude's strict channel cannot satisfy that launch; a profile declaration shadowed by higher-precedence native input cannot establish the effective server. Retain legacy §6 presence semantics under its existing version rather than silently redefining them.
4. Keep provision explicitly operator-selected and outside the pure checker. Reuse source/package allowlists, audit, signer policy, profile locks, and managed materialization. Consent is protected exact-plan authorization, with endpoint visibility and cumulative policy gates. Native writes remain a separately governed capability and must not mutate marker-owned managed homes.
5. Keep authentication in native client/operator workflows. No automatic login, token test, health check, helper execution, or credential-store inspection. Drop the new auth-class wire field unless a separate interoperability need justifies versioning the declaration schema.
6. State the actual secret-handling boundary and the env-union limitation. `passable_env_names` bounds client-launch names, not per-server credential destinations or isolation. Empty `env_names` is not evidence of no exposure. HTTP env names alone do not specify a header binding in current §5.8 output; unsupported auth materialization stays explicit.
7. Version the new evidence/authority semantics through curator-spec with a decision record, compatibility note, and positive/negative vectors. Preserve existing released schemas and `transport` semantics. Treat csk D1's no-env HTTP exception and the mission's consent-before-write gate as separate scopes until explicitly reconciled.

## Required trust vectors

| Input/transition | Required result |
| --- | --- |
| Malicious skill requires a familiar name or supplies a package URL | Requirement only; no automatic fetch-to-execute, config write, or secret-routing authority |
| Repository carries its own alias/approval/provenance digest | Untrusted proposal; no protected binding or ownership is created |
| Approved range selects changed declaration/endpoint/env names | New exact plan and fresh consent; old approval does not float with the range |
| Same command/args from a different package or changed PATH | At most recipe equality; never package/runtime identity |
| Opaque connector, no operator reliance | Unknown and unsatisfied |
| Opaque connector with current scoped reliance | Operator-asserted availability; auth not checked, no invented observation |
| Known disabled entry or launch-excluded provider plus stale reliance | Negative/invalid evidence; no silent satisfaction |
| Hardened empty MCP allowlist or explicit unbounded passthrough | Existing refusal remains; consent cannot bypass it |
| New stdio server beside an env-bearing server | Report shared client-launch exposure; no per-server isolation claim |
| Native file contains secret material or malformed value | Under operational contract, private bounded handling and metadata-only diagnostics; never raw dumps, value logs, diff bodies, or credential-bearing probes |
| Current managed HTTP declaration has env names but no header mapping | No claim that token-header authentication has been wired or tested |

Provisioning consent and opaque-provider reliance are distinct. The requiring skill list should be displayed as attribution, while a new skill requiring an unchanged, observed provider does not by itself create a new provider write or credential route. A reliance record scoped to particular requirements must not be inherited by a different skill with the same local label. These checks do not enforce per-skill access isolation inside a native client's already available tool set. If safe metadata cannot establish provider drift, report the limitation or use operation-scoped reliance; do not persist raw foreign configuration as a substitute.

## Confirmation and remaining proof work

Own findings: `f-secret-boundary.md` and `f-consent-binding.md`, independently confirmed by astra-01 and wonder-02 (also astra-03 for the secret boundary). Recipe/provenance evidence is consolidated into astra-01's `f-package-is-not-service.md`; no duplicate finding is published from this seat.

Still open: second-host adversarial confirmation and independent E1–E8 score of the same winning design; normative protected evidence/adapter-completeness grammar, conformance vectors, and explicit extension policy for hardened machines. Convener event `$h4JEJERFqsHn2uo4CleuMAw2Ylh0NKOdpxvvss87CLA` confirms that mini seats are not yet running and will use `macmini_*` identities; the earlier `mini_*` challenge is parked until exact identities are supplied. Corrected optional A and the substantive trust revisions have been accepted by this seat. E3 evaluation follows the explicit mission amendment while retaining the original score trace. The concrete alternatives above have been reviewed and answered. The collective remains active.
