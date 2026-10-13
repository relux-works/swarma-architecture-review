# astra-02 — authentication and trust verdict

State: provisional, round 1. Host: ivmbp. No implementation or runtime qualification is claimed.

## Position

Prefer **named requirements plus protected local evidence**, the `alt-names-local-evidence` candidate. Keep `dependencies.mcp_servers` unchanged; let the operator choose existing native/plugin/cloud configuration or explicitly selected declaration packages. A requirement is neither installation authority nor a credential grant. The dependency feature should not acquire an auth broker, health checker, server process manager, or parallel package resolver.

The base has the right separation of requirements, provision, and client-owned authentication, but does not yet prove its advertised identity, minimality, secret boundary, or full-zoo claims. The preferred direction is not yet a proved winner: different-host scoring and concrete alternative comparison remain open. This verdict applies the convener's explicit E3 amendment at review-repository commit `534e3849b3fca07c2479222886aacb34808e5bcc`, and preserves the original literal scores as required by that amendment.

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
- **N — Named requirements/local evidence:** no new skill field or auth declaration. Retain the named requirement; combine alias selection and opaque-provider reliance in one protected operator record scoped to the requirement, consumer, agent, and launch. Provision through existing selected profiles/packages or a separately reviewed native writer. Unknown without reliance fails. Existing incompatible/disabled evidence is not overwritten by an assertion.

`alt-names-local-evidence` was independently proposed by astra-01 in event `$-Q10wx4Zpfeu7dJwMNuhMSMvYC2uHkm8FrVKsGK0oy0`; it matches this seat's preferred trust boundary. Native-inspecting N is scored below. A variant that never inspects arbitrary native files may improve literal E3, but its trusted metadata ingress and compatibility with mandatory manager §6 reads have not been specified; it is not credited as a completed solution.

## Rubric

Scores evaluate the described design contracts, not implementation completion. Every row uses the mission's 0–2 range. E3 has an explicit sensitivity analysis; its original literal score is included in the first total, and the amended score in the current-rubric total.

| Criterion | B | R | N | Evidence and reason |
| --- | ---: | ---: | ---: | --- |
| E1 New concepts/fields | 1 | 0 | 1 | B adds requirement identity, declaration auth, and binding state, despite its one-field claim; R additionally needs specified pin/provenance semantics; N removes the skill/declaration changes but honestly counts a new protected evidence record. Closed schemas and `f-schema-budget`. |
| E2 Reuse | 1 | 1 | 2 | B/R package identity goes beyond native §6 and needs resolution/evidence machinery; N keeps requirement grammar and uses existing profile resolution, package allowlist, signer/audit gates, and provisioning channels. Environments §§1.3–1.4, 2.2, 5.8, 6. |
| E3 Literal no credential-byte contact | 0 | 0 | 0 | All three native-inspecting forms read potentially credential-bearing files. `mcp.go:240–288`, supplied csk §§4–5, `f-secret-boundary`. The zero endpoint says the manager touches values. No authentication execution is necessary for this counterexample. |
| E4 Zoo | 1 | 2 | 2 | B's opaque-provider identity binding does not establish configured/enabled presence. R/N admit separately labelled operator reliance without a new client API. This is coverage by reliance, not universal automatic observation. `f-opaque-provider`; manager §6 and environments §7.8. |
| E5 Portability | 2 | 1 | 2 | B's intended operator binding can retain one manifest across machines, although underspecified. R's meaningful source/endpoint identity constrains substitutes; weakening it by waiver must be explicit. N leaves deployment selection local and skill requirements unchanged. Core §4; `f-package-is-not-service`. |
| E6 Honest failure/consent | 1 | 2 | 2 | B promises consent/no auth checks, but identity evidence, scope and authority invalidation remain ambiguous. R/N expressly fail unknown, preserve known negatives, label reliance, and require protected exact-plan consent before their provisioning writes. `f-consent-binding`, `f-launch-universe`. |
| E7 Specifiability | 0 | 1 | 1 | B has no closed binding grammar, identity canonicalization, or lock owner. R/N identify a governable contract and concrete negative vectors, but neither has frozen all schema/state semantics. COMPATIBILITY, GOVERNANCE; confirmed findings. |
| E8 Operator effort | 1 | 1 | 1 | Repeated use of a current approved plan needs no action, but cold setup can require provider selection, consent, and native authentication. Opaque providers require reliance; env-auth GUI setup may be manual. No evidence supports a universal one-action first-use claim. Inputs csk §§2, 5. |
| **Literal total** | **7/16** | **8/16** | **11/16** | **All fail the literal no-zero E3 gate under this seat's reading.** |
| E3 operational non-management, separately | 1 | 2 | 2 | B omits the native identity matcher's handling boundary. R/N explicitly forbid auth execution, value lookup/expansion, credential-store access, probes, persistence/logging/egress, while permitting bounded private handling of existing bytes. This is a different guarantee. |
| **Current amended-rubric total** | **8/16** | **10/16** | **13/16** | N leads among these designs under the explicitly amended E3. Cross-host proof remains pending. |

Rubric-seat wonder-02 confirms the byte-contact contradiction but initially assigns literal E3=1 rather than 0 (event `$SNRLfvcWtHxonUgOrpTBaUZnHD9ClzN9jCkBSf7RasI`). The convener subsequently resolved the evaluation boundary explicitly in MISSION-MCP. The amended total is not a proof under the original verbatim rubric; the amendment and original score remain visible.

N's E3=2 requires its explicit handling boundary: never resolve/expand a credential, access a credential store, execute authentication, or probe a server; parse foreign native bytes only privately and within bounded reads; do not persist, log, or surface raw foreign argv, URL, env, document fragments, or parser exceptions. Use validated metadata-only evidence/diagnostics. Arbitrary `args` and `url` fields can themselves contain secrets, so a field-name whitelist is insufficient. A separate native writer's private preservation of existing bytes is not delegated secret management and must retain the supplied csk handling limits; it is outside the pure requirement operation.

### Concrete alternatives submitted during round 1

Wonder-01 proposed three alternatives: A (skill-root `agent-mcp.json` recommendation, event `$Oi-yLH129Y6zJ-z0AeVV4E84AOrddTDk6HrcmMGsm4M`), T (tool/capability requirements, `$PzZOjpCVB5M21uS8891NqqjxCDYck2IuhK1HxwTxTqE`), and G (manager-owned authenticated gateway, `$hKTg60s0b50i-kQHeKXD6UWd9VLbQNlygcTkZfZG5ss`). These are actual submitted candidates, not hypothetical rejection targets.

**A+N** means A with N's protected evidence contract and the explicit trust corrections below. It is a complement to N, not a different verification architecture. **A alone** means its first submitted recommendation mechanism, before those corrections; it cannot solve opaque-provider evidence by itself.

| Criterion | A alone | A+N corrected | T | G | Evidence and reason |
| --- | ---: | ---: | ---: | ---: | --- |
| E1 | 2 | 1 | 1 | 0 | A reuses the existing declaration file with no skill-schema field; A+N still counts protected evidence state. T needs a new manifest/version lane. G introduces a runtime/protocol family. Core §3, environments §2.2, schema-budget finding. |
| E2 | 2 | 2 | 1 | 0 | A uses an existing snapshot and selected profile/MCP admission. T lacks reusable current tool-inventory verification in §6. G owns backend process/auth/session machinery absent from the checker. |
| E3 amended | 1 | 2 | 2 | 0 | A initially prints §2.3 argv rows in a plain skill lane that need not perform strict MCP secret-material admission. Corrected A+N uses metadata-only discovery and existing admission before detailed display. T forbids manager probes. G deliberately forwards backend credentials. |
| E4 | 1 | 2 | 1 | 1 | A alone retains the opaque evidence gap; A+N closes it by labelled reliance. T has no generic current client tool inventory in local evidence. A gateway cannot assume access to account-only cloud connectors. |
| E5 | 2 | 2 | 1 | 1 | Inert schema-1 sidecar degrades gracefully with the existing manifest. T tool names have no portable equivalence across providers. G couples clients to its deployment. |
| E6 | 2 | 2 | 1 | 0 | A remains a recommendation and grants no write authority. A+N keeps unknowns and independent consent. T's strong connected/tool claim exceeds install evidence. G can mask unavailable backends and collapses native per-server controls. |
| E7 | 1 | 1 | 1 | 1 | A's surfacing/audit/source-kind/remediation rules need closure; N evidence grammar is still pending. T exact name sets can have a closed grammar without a global registry, but trusted inventory/equivalence remains unspecified. G is specifiable but undeveloped. |
| E8 | 1 | 1 | 1 | 2 | A improves discovery while native auth/first setup still costs actions. T still needs binding. G offers one entry, at unacceptable trust cost. Existing-provider N/A+N usage can score 2 under the rubric seat's narrower common-case definition. |
| **Amended total** | **12/16** | **13/16** | **9/16** | **5/16** | A+N ties N on this conservative scoring; G fails the E3/E6 gates. |
| E3 original | 0 | 0 | 0 | 0 | A/A+N/T retain native-checker byte contact as submitted; G intentionally handles credentials. |
| **Original total** | **11/16** | **11/16** | **7/16** | **5/16** | Original literal gate fails; no original-rubric proof is claimed. |

The preferred composition is **N, optionally augmented by corrected A**. A lets an author ship exact recommendation bytes without a new `server` field. It is not required for an already configured provider. The source snapshot's pin is integrity, not MCP authorization: selected use still requires canonical Git-source/package admission, signer policy, strict audit, and consent. Recommend the exact resolved revision, not an independent skill version tag that might violate the declaration's version match. Path/local skill snapshots do not gain a canonical network identity; the §2.2 refusal remains. Multiple recommendations can use an existing companion context package; a new directory-discovery convention is unnecessary.

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

## Confirmation and remaining proof work

Own findings: `f-secret-boundary.md` and `f-consent-binding.md`, independently confirmed by astra-01 and wonder-02 (also astra-03 for the secret boundary). Recipe/provenance evidence is consolidated into astra-01's `f-package-is-not-service.md`; no duplicate finding is published from this seat.

Still open: mini astra-12 adversarial confirmation; independent different-host E1–E8 score of the same winning design; protected evidence grammar and legacy compatibility; final acceptance of corrected optional A. E3 evaluation now follows the explicit mission amendment while retaining the original score trace. The concrete alternatives above have been reviewed and answered. The collective remains active.
