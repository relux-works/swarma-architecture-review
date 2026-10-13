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
- `inputs/csk-mcp-design-proposal-v1.md` §2 already binds protected consent outside checkout to consumer identity, scope, selected agents, normalized execution/endpoint/env names, reference digest, and writer interpretation.
- `inputs/csk-slice1-decisions.md` D1 expressly allows no-env HTTP declarations without consent. This is the supplied csk feature's policy, not proof of the base/mission's stronger consent-before-any-write statement.

## Abuse cases

| Case | Required outcome |
| --- | --- |
| Repository adds `figma -> attacker` plus a committed approval flag | Treat as an untrusted request; no write, provenance waiver, or operator assertion is authorized |
| Previously approved `^1` resolves to a new signed endpoint/recipe or wider env-name set | Old consent does not authorize the changed plan |
| An allowlisted package requests an already passable token | Source admission and env-name eligibility remain necessary but insufficient for a new credential route |
| A new stdio server has empty `env_names`, while another server contributes a sensitive name to the client launch | Do not claim isolation; client inheritance may expose the shared launch environment |
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

Provisioning consent and reliance have different lifecycles. Display the requiring skill set as attribution. Renew provider-write consent for changed execution/routing/targets/destination; adding a consumer of the same observed provider does not itself change that plan. In contrast, a reliance record granted to a particular requirement cannot automatically cover another skill with the same local label. Batching an explicitly enumerated set is permitted, but it is not a wildcard or per-skill runtime tool isolation. Astra-01 independently confirmed this distinction in event `$bcQo8dvlG5td3CYYqnAR8O4tAEjgOafREz5sppyue8s`.

## Rubric rows affected

- **E1/E2:** protected binding/consent semantics are real additional machinery even when the skill adds only one field; reuse the csk pattern and existing policy gates.
- **E3:** decisions depend on public identities and names, never credential lookup or use. Any unavoidable native-file byte handling must independently meet the amended boundary in `f-secret-boundary.md`.
- **E6/E7:** authority provenance, exact-plan invalidation, and honest env-scope reporting must be vectored.
- **E8:** an unchanged exact plan can reuse consent; a changed credential route correctly requires a new action.

## Confirmed by

- ivmbp astra-01, event `$Q2vl0tBPG65rCP2-wtTFDYSb3_FXWdIiQiP_QjZq-74`, topic `f-consent-binding`.
- ivmbp wonder-02, event `$5P_OppjPueGB-VRS6PvETkZn8oov-7j-rSGQEeVeeOk`, confirming the independent gates, env-union limitation, and absent HTTP endpoint in existing surfacing rows.
- Candidate event: `$mhovjJEZ0ayL0LlKvIcCl7kjgvweMMaC6RM1F88gg8Q`.
- Different-host adversarial review remains pending. The earlier `mini_*` challenge is parked: convener event `$h4JEJERFqsHn2uo4CleuMAw2Ylh0NKOdpxvvss87CLA` confirms the seats are not yet running and will have `macmini_*` identities.
