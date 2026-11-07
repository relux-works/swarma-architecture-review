# Bindings and provisioning consent need protected exact-action scope

- Lens: authentication and trust.
- Author: astra-02 (ivmbp).
- Status: proposed.
- Confidence: high.
- Base: `BASE-DESIGN.md`, Bind and Authentication.

## Problem

The base calls for explicit operator consent, but it does not specify the authority, scope, persistence, or invalidation of consent and operator bindings. Its machine-or-project alias map can become an authority confusion if repository data is accepted as an operator's decision to substitute a provider or waive an identity mismatch. A source allowlist, a signature, and a printed declaration are distinct controls; none proves consent to the exact resolved action.

The environment-name allowlist is also narrower than a credential-destination policy. It bounds which operator names can reach a client launch. It does not isolate each server from every other server, authorize a particular endpoint to receive the value, or prove that a native client delivers only each declaration's listed names.

## Evidence

Read-only source checkpoints: curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`; curator `5234cf38833554542e68afade15951c6e56ed89e`.

- `protocol/environments.md` §2.3 says surfacing is informative and never fails. Its closed HTTP row omits the endpoint. `internal/envprofile/surfacing.go` and `internal/contextmaterialize/mcp.go`, `FormatDeclarationRows`, implement that boundary.
- Environments §§1.4, 2.2 and manager §7.1 admit source identities, resolved candidates, and signer policy. A new signed in-range release can change the declaration; source admission is not exact-action consent.
- Environments §10.3 and §5.8 pass a union of names to the launch plan. `internal/contextmaterialize/mcp.go`, `MCPEnvNames`, and `internal/envprofile/managed.go:2442–2458` build and bound that union. No per-server secret-isolation guarantee follows.
- Environments §10.3:3310–3345 preserves the shipped S4 absent-knob behavior under hardened: `s4-warn` is unbounded with warnings, while `s4-enforce` defaults to an empty list. Hardened refuses explicit `passable_env_names: null`; it does not turn warning-profile absence into default deny. The local implementation sets `ActiveS4Profile = S4Warn` in `internal/envfragment/envfragment.go:246–250` and implements the distinction in `EffectivePassable`/`ResolvePassthrough`.
- Schema-1 managed HTTP output carries URL/type only (`contextmaterialize/mcp.go:244–327`); `env_names` supplies no HTTP header mapping. The supplied csk proposal explicitly needs a separately governed header-reference grammar/client mapping. An `auth: env` label cannot repair the absent routing semantics.
- `inputs/csk-mcp-design-proposal-v1.md` §2 already binds protected consent outside checkout to consumer identity, scope, selected agents, normalized execution/endpoint/env names, reference digest, and writer interpretation.
- `inputs/csk-slice1-decisions.md` D1 expressly allows no-env HTTP declarations without consent. This is the supplied csk feature's policy, not proof of the base/mission's stronger consent-before-any-write statement.

## Abuse cases

| Case | Required outcome |
| --- | --- |
| Repository adds `figma -> attacker` plus a committed approval flag | Treat as an untrusted request; no write, provenance waiver, or operator assertion is authorized |
| Previously approved `^1` resolves to a new signed endpoint/recipe or wider env-name set | Old consent does not authorize the changed plan |
| An allowlisted package requests an already passable token | Source admission and env-name eligibility remain necessary but insufficient for a new credential route |
| A new stdio server has empty `env_names`, while another server contributes a sensitive name to the client launch | Do not claim isolation; client inheritance may expose the shared launch environment |
| Existing stdio B has empty `env_names`; later A adds an already passable name | Reassess launch-level consent: B may gain exposure although its own declaration did not change |
| B is added beside env-bearing A, without changing the name union | Reassess launch-level consent: the recipient set widens even though the union does not |
| Hardened machine has absent `passable_env_names` under `s4-warn` | Report the warning-profile unbounded residual; never infer default deny from hardened alone |
| Managed HTTP declaration names a token variable but has no header binding | No claim that env authentication was materialized; native auth is eligible only in a launch that includes it |
| A project-supplied binding targets a globally configured provider | Do not silently widen consumer scope or transfer ownership |

## Proposed change

Reuse the supplied exact-plan consent pattern instead of creating an auth subsystem:

1. Keep authority in operator-controlled protected machine state outside the repository. Project files may propose aliases/bindings; they cannot authorize them. Same-OS-user compromise remains outside this file-based threat model and must not be solved with a fictitious human-only flag.
2. Bind provider-write consent to the exact resolved declaration identity and the consumer project/profile, target agents, launch context, scope/destination, effective recipe or endpoint, requested env names, and interpretation version. The requiring skill set is attribution, not a provider-consent renewal trigger. Bind opaque reliance separately to exact enumerated requirement identities as described below. Revalidate inputs before publication. Changed or widened authority needs renewed consent.
3. Keep source allowlist, package allowlist, strict audit, signer policy, system locks, native ownership, and consent cumulative. An approval does not bypass a hardened refusal or turn a foreign native entry into an owned one.
4. Show the endpoint and relevant shared-launch exposure in the reviewed plan. Existing §2.3 rows alone cannot review HTTP credential routing.
5. Distinguish rename-only selection, observed public metadata, manager-recorded origin, and operator reliance. Origin is annotation, not availability or authorization. A binding never changes known disabled/conflicting configuration of that provider into an observed healthy provider. Opaque reliance is labelled as such.
6. Keep `passable_env_names` as client-launch admission. Do not claim per-server isolation or require a new broker to make the dependency feature usable. Authentication remains with the client/operator.
7. State separately how the base's stronger consent rule composes with csk D1. Do not silently change either supplied contract or declare them identical.

Exact-plan consent must cover the aggregate launch exposure, not only the changed declaration. Reassess the effective passed MCP-name union after rollout/policy composition, potential inheriting provider recipients, adapter/launch mode, and effective policy. A changed union or recipient set invalidates an exact-plan grant that did not authorize the resulting exposure. One approval may cover the complete changed plan; a separate prompt for every unchanged server is unnecessary. Where the adapter cannot enumerate recipients reliably, require explicit approval of the named shared launch trust domain and its visibility limitation, or keep the proposed mutation unapproved. Never manufacture a complete recipient inventory, inspect credential values, or claim isolation. This controls manager-authorized mutations; it does not police independent changes to foreign clients.

The MCP-name union is additive (§7.8), not a complete inventory of the client environment. Other environment inherited through the launcher/native runtime remains part of the shared-domain exposure warning. Use safe names and declared policy where observable; retain the visibility limit where the complete environment or recipient set cannot be established. Astra-12 accepted this aggregate-plan repair and sharpened the additive boundary in `MCP 2026-10-14, f-consent-binding, note 01`.

Provisioning consent and reliance have different lifecycles. Display the requiring skill set as attribution. Renew provider-write consent for changed execution/routing/targets/destination; adding a consumer of the same observed provider does not itself change that plan. In contrast, a reliance record granted to a particular requirement cannot automatically cover another skill with the same local label. Batching an explicitly enumerated set is permitted, but it is not a wildcard or per-skill runtime tool isolation. Astra-01 independently confirmed this distinction in review citation `MCP 2026-10-14, f-consent-binding, note 02`.

## Rubric rows affected

- **E1/E2:** protected binding/consent semantics are real additional machinery even when the skill adds only one field; reuse the csk pattern and existing policy gates.
- **E3:** decisions depend on public identities and names, never credential lookup or use. Any unavoidable native-file byte handling must independently meet the amended boundary in `f-secret-boundary.md`.
- **E6/E7:** authority provenance, exact-plan invalidation, and honest env-scope reporting must be vectored.
- **E8:** an unchanged exact plan can reuse consent; a changed credential route correctly requires a new action.

## Confirmed by

- ivmbp astra-01, review citation `MCP 2026-10-14, f-consent-binding, note 03`, topic `f-consent-binding`.
- ivmbp wonder-02, review citation `MCP 2026-10-14, f-consent-binding, note 04`, confirming the independent gates, env-union limitation, and absent HTTP endpoint in existing surfacing rows.
- macmini astra-12, independently frozen third-pass review followed by review citation `MCP 2026-10-14, f-consent-binding, note 05`: confirms the union residual and supplies the two launch-set consent vectors plus the hardened/S4 qualification. These are source-derived cases, not reproduced exploits.
- ivmbp astra-05, independently frozen second-five review in signed `ff552b3` before first-five/topic-body reads, confirms the aggregate exposure/S4 boundary and the proposed shared-domain repair in `MCP 2026-10-14, f-consent-binding, note 06`. Its published verdict at `8cad898` preserves the original counterexample and the later comparison.
- ivmbp astra-06, independently frozen second-five review followed by `MCP 2026-10-14, f-consent-binding, note 07`, and macmini astra-12 in `MCP 2026-10-14, f-consent-binding, note 08`, confirm the existing schema-1 HTTP routing limit. This author confirms its inclusion here in `MCP 2026-10-14, f-consent-binding, note 09`; no duplicate finding is needed.
- macmini wonder-12, `MCP 2026-10-14, f-consent-binding, note 10`, independently confirms protected exact-plan authority, cumulative gates, endpoint/aggregate-env visibility, and separate provisioning-consent/reliance lifecycles.
- Candidate review note: `MCP 2026-10-14, f-consent-binding, note 11`.
- Different-host adversarial confirmation is now present from the actual `macmini_swarma-mcp-deps_astra-12` identity; the earlier `mini_*` alias was not used as evidence.
