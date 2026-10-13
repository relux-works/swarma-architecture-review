# astra-03: zoo compatibility verdict

Status: round-1 position; debate and cross-host scoring remain open. Seat: ivmbp astra-03. No implementation or runtime certification is claimed.

The base has the right separation between requirements, provision and native authentication, but its claimed zoo coverage is not established. A native entry is not necessarily effective in a managed launch, and an opaque connector supplies no observable configured/enabled premise. My preferred practical candidate is **named skill requirements with scoped operator evidence**, `alt-names-local-evidence`: retain the current skill grammar, keep provisioning operator-selected, and make observed configuration and explicit operator reliance different evidence states.

The literal no-credential-read promise is incompatible with unrestricted mixed-native-file inspection. Operational and literal E3 readings are therefore reported separately. This is not a declaration that the mission rubric has been amended.

## Evidence basis

- **S**: curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`, clean local checkout: core §4; manager §§1,6; environments preamble, §§2.2,2.3,5.8,7.8,10.3; `schemas/v1/common.schema.json` `$defs.mcpRequirement`; `agent-mcp-v1.schema.json`; COMPATIBILITY.md; GOVERNANCE.md.
- **I**: curator `5234cf38833554542e68afade15951c6e56ed89e`, clean local checkout: `internal/mcp/mcp.go:24-61,245-287`; `internal/contextmaterialize/mcp.go:31-107`; `internal/envprofile/managed.go:205-229,298-364`; `internal/envprofile/surfacing.go`.
- **C**: supplied csk proposal §§1–5, slice-1 decisions D1/D5/D6/D7 and A4/A6, curator review H1–H4 and S2/S3. These are proposal/review evidence, not implemented-client certification.
- **F1**: [launch universe finding](../findings/f-launch-universe.md); **F2**: [opaque provider finding](../findings/f-opaque-provider.md). Each has independent same-host confirmation and event ids; cross-host challenge remains pending.

External clones were not pulled because the sandbox makes them read-only. No web, builds, tests or actual credential/config-store reads were performed. Source-recorded native facts keep their original verified/docs-confidence labels.

## Candidates and scores

**B** is BASE exactly as written. **B+** retains its authoritative package/endpoint requirement but adds scoped evidence, protected assertions/consent, honest static-versus-provenance labels and governed schema changes. **N** is `alt-names-local-evidence`: current named requirements, operator-selected existing provisioning, and one scoped local binding/evidence concept. **S-only** is N's strict metadata-only branch: no arbitrary native-file inspection or native writing in this dependency operation; use already secret-free managed metadata or an explicit operator assertion. It needs a governed capability boundary and cannot silently claim unchanged manager §6 scanning.

| Criterion | B | B+ | N | S-only | Evidence / reason |
| --- | ---: | ---: | ---: | ---: | --- |
| E1 new concepts/fields | 0 | 0 | 1 | 1 | B has requirement identity, package auth and local binding state, not just one optional field. N drops the first two but its protected evidence record is not free. S common schema + agent-mcp schema; C review H1/H2. |
| E2 existing machinery | 1 | 1 | 2 | 1 | B/B+ import identity comparison and unresolved package-lock ownership. N reuses named requirements, profile locks, materialization and policy, extending checker evidence. S-only sacrifices native scanning and native writer reuse. S §§2.2/5.8; I. |
| E3 literal | 0 | 0 | 0 | 2* | I reads/unmarshals entire native files; C §§4–5 admits foreign credential literals. This is byte contact under the literal zero anchor. S-only's 2 applies only to its explicitly restricted dependency operation, not all existing Curator launcher functionality. |
| E4 zoo | 0 | 2 | 2 | 2 | B lacks opaque presence and selected-launch rules. B+/N/S-only use target-scoped operator reliance where observation is unavailable, without pretending an excluded provider is available. F1/F2. |
| E5 portability | 1 | 1 | 2 | 2 | A required package/endpoint couples the manifest to an acquisition/deployment unless local exceptions intervene. N/S-only preserve the portable named request; provision and deployment remain local. S core §4, C §1. |
| E6 honest failure | 1 | 2 | 2 | 2 | B promises consent/auth-not-checked but leaves unknown, alias authority and effective precedence unresolved. Corrected candidates retain per-target unknowns and reject contrary known evidence; assertions are explicit reliance, never observed truth. F1/F2; C §2. |
| E7 specifiability | 0 | 1 | 1 | 1 | B has no closed identity/equivalence/binding grammar or assigned schema lane. Corrected candidates have a concrete governance path and writable cases, but their complete grammar/vectors are not yet frozen. S COMPATIBILITY/GOVERNANCE. |
| E8 operator effort | 1 | 1 | 2 | 1 | N's already-working visible provider needs zero extra action; opaque provider needs one scoped assertion. B/B+ additionally resolve identity or mismatches. S-only makes assertions necessary for otherwise inspectable native state. Authentication remains native and is never counted as completed. |
| **Literal total** | **4** | **8** | **12** | **12*** | B/B+/N fail the literal E3 gate. S-only is conditional, with its reduced capability explicit. |
| E3 operational, separately reported | 1 | 2 | 2 | 2 | Operational means no credential resolution/expansion/auth execution, logging, durable credential copies or egress; bounded private parsing of mixed native bytes is disclosed, with an explicit non-secret projection. The checker/provisioner boundary excludes the existing authorized launcher inheritance mechanism. |
| **Operational total** | **5** | **10** | **14** | **12*** | Comparative evidence only until the gating interpretation is explicitly settled. |

The rubric seat proposed literal E3=1 for bounded byte contact. I use 0 because the mission's zero anchor says the manager “touches values.” The numerical difference is one, but it changes eligibility; that difference must be resolved openly, not hidden by the totals. Event `$SNRLfvcWtHxonUgOrpTBaUZnHD9ClzN9jCkBSf7RasI` records that seat's interpretation.

## Compatibility matrix for the preferred practical candidate

| Provider source | Evidence that can count | Limit / operator action |
| --- | --- | --- |
| Hand-written native config | Read-only static projection in the selected native context | Does not prove auth, connection or runtime executable identity; mixed-byte E3 limit disclosed |
| Client plugin | Existing safe report/metadata when available | Otherwise one protected, scoped reliance assertion; no plugin install or client change implied |
| Cloud connector | Existing client report when available | Otherwise asserted reliance with configuration/auth unknown; no duplicate native provider silently provisioned |
| Curator profile | Existing lock, adapter selector, marker and channel evidence | Respect Claude strict exclusion and OpenCode override residuals; do not equate profile membership with every launch's effective set |
| csk entry | Same external static evidence as a hand-written entry | Requirement use conveys no ownership. Equal foreign entry may satisfy checking while a provision attempt conflicts (D6) |

`any` needs one accepted target; `all` needs every target. Unknown targets remain visible even when `any` succeeds elsewhere. Known disabled, mismatched or excluded evidence is never erased by an assertion. The new lane cannot silently strengthen or reinterpret legacy manager §6 and documentary `transport` semantics.

## Authentication and ownership constraints

Native clients retain OAuth and secret handling. `agent-mcp.json` schema 1 does not contain `auth` or HTTP header bindings; §5.8 writes argv or URL, while `env_names` only requests launch passthrough. Therefore passing a token's variable name does not tell a client which HTTP header uses it. Preserve existing native configuration where effective, report unsupported managed materialization honestly, or govern a separate names-only routing extension. An auth-class label alone solves none of that mapping.

The existing native-writer feature remains separate. Its managed-home guard and protected ownership/consent state are mandatory boundaries, not a common byte-writer abstraction. csk D1's consent-free HTTP-without-env case is not the same as BASE's consent-before-any-write promise. Do not claim that one proves the other.

## Smallest changes to reach N

1. Keep `hint`, documentary `transport`, and `required_in`; remove the authoritative `server.package`/`server.endpoint` addition from this dependency slice. Package suggestions can remain non-authoritative guidance until machine-readable recommendations demonstrate a concrete need.
2. Reuse operator-selected context `requires.mcp` and declaration packages for managed provisioning. Keep independently reviewed native writers separate. No skill gains write, execution, allowlist or credential-routing authority.
3. Specify one operator-owned binding/evidence record outside repository control, including requirement and selected target identity. Let it express a name mapping or explicit reliance on an opaque provider; neither conveys config ownership. Revalidate observable fingerprints; stale or widened scope requires a new decision.
4. Define observed, asserted, unknown and known-negative evidence, target aggregation and launch precedence. Use existing profile/channel/marker metadata for managed contexts. Preserve old schema/checker meanings through a governed extension.
5. State the auth boundary and the native mixed-byte exception explicitly, or choose S-only and its loss of automatic native discovery. Do not call either choice a proof of the other.
6. Publish the minimal governed config/status grammar and conformance cases before claiming E7=2. No extra identity registry, proxy, credential broker or native inventory API is required.

## Proof status and open debate

The base is not proved elegant. N currently dominates the corrected base under the operational boundary while using fewer portable concepts. S-only is the honest strict-boundary alternative, but its qualification cannot be collapsed into the unchanged Curator behavior. Two hosts have not yet agreed a complete score vector, and the E3 gating interpretation is open. Findings F1/F2 already have independent same-host confirmations; cross-host attacks and alternative-hunter results must be incorporated before PARK.
