# Satisfaction must be scoped to the selected launch

- Lens: zoo compatibility.
- Author: astra-03, ivmbp.
- Status: proposed.
- Confidence: high for the specification/source mismatch; native release behavior is only as strong as the source's recorded evidence.
- Room topic: `f-launch-universe`, `$3jMMc2o4Phy7P3ht6PyomB9g2iFHa9i4-yEQ-nE1lFQ`.

## Problem

BASE Provide accepts some configured, enabled entry for a target agent, then applies identity matching. It never specifies whether the target is the operator's native launch or a particular Curator managed launch. These sets differ. Applying the existing native name union to the stronger zoo-wide claim can accept an entry excluded from the selected launch, miss a managed-only entry, or conceal an overriding entry with a different endpoint.

This does not retroactively turn manager §6's legacy configured-presence check into a runtime-availability promise. It identifies the missing boundary when BASE extends that check.

## Evidence

Sources were read from clean local snapshots, without builds, tests, browser access or real configuration reads:

- curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`, `profiles/manager.md` §6: the native project/user configuration table and read-only name-based verification.
- Same spec, `protocol/environments.md` §5.8: the managed set materializes into marker-recorded channel files, including `.agent-context/mcp/claude_code.json` and `curator-mcp.config.toml`, outside that native table.
- Same spec, §7.8: managed Claude's `--strict-mcp-config` excludes other MCP configuration; OpenCode's documented merge permits project configuration to override a same-name managed entry. Claude is recorded as verified on 2.1.261; OpenCode remains docs-confidence. This review did not rerun either client.
- curator `5234cf38833554542e68afade15951c6e56ed89e`, `internal/mcp/mcp.go:24-61`: the reader has native roots and unions project/home maps; `Env` carries no managed launch descriptor. Equal names are overwritten by the later home map, not a general effective-precedence model.
- Same implementation, `internal/contextmaterialize/mcp.go:31-35,79-107`: managed channel paths and adapter selection are already distinct; `internal/envprofile/managed.go:205-229,298-364` loads the profile lock's declarations and composes a per-adapter home.
- Supplied `inputs/curator-review-of-csk-design.md`, H4 and S2: native writers must not mutate managed homes; native project configuration is inactive for managed Claude. The Codex trusted-project residual is supplied review evidence, not a native fact independently reproduced here.

## Proposed change

Specify the target evidence context as the selected agent, project/scope, and native-or-managed launch. This context comes from the manager operation; it need not add a skill-manifest field.

For a managed launch, consume the existing resolved profile/channel set and its marker/drift evidence, then account for documented precedence and residuals. A profile declaration alone does not override contrary effective configuration. For legacy native checks retain the existing §6 meaning and label its limited evidence; introduce any stronger semantics through a governed optional/versioned contract.

Keep native writers away from marker-owned managed homes and reserved channel files. Do not silently duplicate a native entry into a managed profile or weaken Claude's strict launch channel to manufacture satisfaction.

Minimum conformance cases:

| Case | Result for the selected managed launch |
| --- | --- |
| Native Claude X exists; profile X absent | X is not satisfied by that native entry |
| Managed channel X exists; native X absent | Native absence alone does not reject managed evidence |
| OpenCode project X overrides managed X with a different endpoint | The managed digest alone cannot establish the effective identity; report mismatch or bounded unknown |
| Native writer destination carries an environments marker | Refuse this writer's mutation of the managed home |

## Rubric impact

E4: no universal zoo claim without target-specific visibility. E6: a configured entry excluded or shadowed in the selected launch must not become a stronger silent success. E7: target, precedence and residual cases need a closed contract and vectors. E2 benefits from reusing existing profile/channel evidence rather than inventing another server registry.

## Confirmed by

- astra-01 on ivmbp, event `$vmTiv-XDm2nS_z1xPQ8q9pg3xh1Eny2-Yp4RfWUxQFo`: independently confirmed §5.8/§7.8 and the implementation's native union; explicitly preserved legacy semantics and required a versioned optional contract for stronger claims.
- Cross-host adversarial confirmation requested from astra-13 at `$JCvsGaqk38u16fORG-wM5k2v3iq4jWmo4YDVDmj_ejM`; pending when this finding was first written.

## Round-2 corroboration and bounds

- wonder-02 event `$wo5YNm48iTnPqXqJqcxbFC_00nZSLnCcFlkpgTMZ138` independently confirms the native union, disjoint managed paths and precedence issue. It additionally notes that the current reader's disabled-entry filters are not uniform across clients; stronger evidence must not inherit a false uniform-enabled claim.
- wonder-01 event `$Zd7y6tD0c9N7xmCDrBul5sYd7h88H19v10Le9Xg1W2s` identifies `internal/install/install.go:1582-1605` and `internal/marker/marker.go:253`. I independently read those at the pinned implementation: the gate takes only project/user roots, and the marker maps names to found-agent lists without a launch descriptor.
- Operator assertions cannot make pi support MCP, make project-scoped Windsurf acquire a nonexistent project surface, or make strict managed Claude consume excluded native header configuration. Zoo-source compatibility is not a claim that every unsupported client/launch combination becomes feasible.
- New observed/asserted evidence must not be silently stored in the legacy marker's `FoundIn` representation as if it had identical meaning. The governed extension must retain provenance of the evidence category as well as target context.
