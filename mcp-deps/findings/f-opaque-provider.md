# Opaque plugins and cloud connectors need explicit evidence semantics

- Lens: zoo compatibility.
- Author: astra-03, ivmbp.
- Status: proposed.
- Confidence: high for the logical gap; no claim that every individual plugin is opaque.
- Room topic: `f-opaque-provider`, `MCP 2026-10-14, f-opaque-provider, note 01`.

## Problem

BASE Provide has two conjuncts: an enabled configured entry with the required or mapped name, and a matching identity when requested. Its explicit operator binding appears as an alternative in the identity conjunct. That binding does not establish the configured/enabled conjunct for a provider which exposes no inspected native entry or existing safe client report.

The base admits a cloud connector only when the client reports it, while E4 requires every zoo member to be able to satisfy a requirement without a client change. No universal reporting mechanism is established. An unknown connector cannot silently count as present merely because its alias or endpoint was approved.

## Evidence

- `BASE-DESIGN.md`, Provide: configured/enabled presence AND identity; cloud support is conditional on a client report. Its open points explicitly leave invisible plugins and connectors unresolved.
- curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`, `profiles/manager.md` §6: six native project/user file surfaces, no generic connector/plugin inventory or operator-assertion contract.
- curator `5234cf38833554542e68afade15951c6e56ed89e`, `internal/mcp/mcp.go:24-61,245-287`: the existing evidence comes from those filesystem maps. It contains no client-report channel.

The counterexample needs only one provider invisible through existing permitted observations. Two states—connector enabled in the provider account, connector absent—can yield identical manager inputs. No deterministic checker can distinguish them without another observation or an explicit external assertion. This is an information boundary, not a demand to add OAuth, health checks or client APIs.

## Proposed change

Choose and state one of these policies:

1. Keep unknown unsatisfied. This preserves automatic evidence honesty but cannot earn universal E4 coverage.
2. Define an operator-owned, target-scoped reliance assertion for opaque/external providers. It must remain visibly `asserted`, with configuration and authentication unknown to the manager. A policy may accept that reliance for the requirement; it must not relabel it as observed configuration, verified identity or connectivity.

The second is the smallest general escape hatch found in this review. It is a real additional binding/evidence concept and must count in E1/E2/E7. Protect it outside repository-controlled state, bind it to the requirement and actual selected target, and invalidate it when that binding changes. Known disabled, mismatched, excluded or shadowed evidence cannot be erased by an assertion. A known-negative waiver, if ever desired, would be a different explicit policy, not this assertion mechanism.

Use existing safe client metadata where available. Never make a client change, a new proxy, authentication execution or silent duplicate provisioning a prerequisite for satisfying an already working opaque provider.

Minimum conformance cases:

| Inputs | Evidence and acceptance |
| --- | --- |
| No visible entry/report; alias only | Unknown, not satisfied |
| No visible entry/report; protected assertion for this requirement/target | Asserted; only an explicit assertion-accepting policy may proceed |
| Same assertion in another project/agent/launch context | Unknown; assertion does not apply |
| Repository contains its own approval/assertion | No authority |
| Known disabled or excluded entry plus assertion | Contrary evidence remains; no silent success |
| `any` with one observed success and other unknown targets | Can succeed through the observed target; retain per-target unknowns |
| `all` with an unresolved unknown target | Does not succeed |

## Rubric impact

E4 and E6 are in tension until the observation/assertion distinction is explicit. E1/E2/E7 must count the state and semantics that close it. E8 can remain zero/one action for a working opaque connector through one scoped operator decision, without repeated native wiring.

## Confirmed by

- astra-01 on ivmbp, review citation `MCP 2026-10-14, f-opaque-provider, note 02`: independently confirmed that BASE binding discharges only the identity conjunct; protected scoped reliance is new evidence semantics, not a rename-only alias.
- astra-13 on Mac mini, review citation `MCP 2026-10-14, f-opaque-provider, note 03`: independently confirmed after freezing initial scores. Indistinguishable enabled/absent account states expose the AND-premise gap. It retains E4=1 for conditional source-category coverage; my response `MCP 2026-10-14, f-opaque-provider, note 04` confirms this never means universal effective availability, authentication or machine verification. A known excluded launch or unsupported header materialization cannot be repaired by assertion. This supersedes the original pending request to the earlier `mini_*` addressee.
- wonder-12 on Mac mini, review citation `MCP 2026-10-14, f-opaque-provider, note 05`: independently confirms the conjunction gap and protected target-scoped reliance as additional evidence semantics. Known-incapable targets and authoritative contrary evidence remain failures; the assertion mechanism counts in E1/E2/E7.

## Round-2 corroboration and absence qualification

- wonder-02 review citation `MCP 2026-10-14, f-opaque-provider, note 06` independently confirms both the AND-premise gap and the missing report surface. It requires asserted labels to remain visible in status/markers and forbids duplicate provisioning as a workaround.
- wonder-01 review citation `MCP 2026-10-14, f-opaque-provider, note 07` confirms the gap and emphasizes invalidation on contrary later evidence.
- astra-01 review citation `MCP 2026-10-14, f-opaque-provider, note 08` confirms that alias and reliance can share one new contract, but old observed `FoundIn` cannot silently represent assertions.

Negative evidence must be authoritative for the **same bound provider and selected launch**. No entry in the six native files remains unknown for an opaque connector; it is not proof of absence. A complete authoritative provider inventory or an explicit launch-channel exclusion can establish absence. Similarly, a disabled unrelated same-name native entry must not be mistaken for the separately bound connector. This clarification was posted at `MCP 2026-10-14, f-opaque-provider, note 09`.
