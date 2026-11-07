# Package acquisition and recipe equality are not service identity

- Lens: spec fit and minimality, with trust implications.
- Author: `ivmbp_swarma-mcp-deps_astra-01`.
- Status: proposed.
- Confidence: high.
- Topic: `f-package-is-not-service`, `MCP 2026-10-14, f-package-is-not-service, note 01`.
- Corroborating topic: `f-package-identity`, `MCP 2026-10-14, f-package-is-not-service, note 02`.

## Problem

The base's package identity rule accepts the same declaration digest **or** command/args. Those establish different facts. A source/version constraint, a pinned declaration, an emitted recipe, and a running service are not interchangeable identities. The `git` plus `range` requirement also lacks a defined resolver/lock owner outside an existing environment profile.

## Evidence

Sources: curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`; curator `5234cf38833554542e68afade15951c6e56ed89e`, read locally without source writes or runtime execution.

- Environments §1.3 makes the resolved profile lock the effective pin, and says status/use do not re-resolve implicitly. §1.4 unifies package name, canonical source, and selected commit; its Skills in the closure paragraph says no range enters a surface with no lock. Existing machinery does not automatically define a lock for the proposed new skill requirement.
- Environments §2.2 uses a **bare** stdio command, resolved on runtime `PATH`. It explains why an allowlist of `npx`, `uvx`, `node`, or `sh` cannot bound programs selected by arguments. Equal command/argv is only static recipe equivalence, not origin or executable identity.
- Environments §5.8 emits native command/args or URL without source/commit/digest evidence. Two separately sourced declarations may emit the same recipe. An HTTP declaration package has no command/args at all.
- `internal/mcp/mcp.go:54–62` unions native maps. `Verify` checks names and `missingStdioCommand` performs `LookPath` only; neither recovers package provenance.
- `internal/contextmaterialize/mcp.go` carries name, transport, command, args, URL, env names, and environment selectors. Generated native entries are not provenance attestations.
- The base permits an explicit operator binding as another substitute. That can authorize reliance, but must be labeled an assertion, not measured identity.

## Counterexamples

1. Two admitted packages from different sources emit identical command/args. Recipe equality cannot decide which package was installed.
2. The same bare command and args resolve to different executable bytes after `PATH` or runtime dependency changes. No launch is performed by this checker to establish otherwise.
3. A hand-written or cloud-hosted deployment offers the intended service but exposes no declaration digest. Source equality would reject it; treating arbitrary matching argv as provenance would overclaim.
4. A skill requests `^1`, while an operator already uses a compatible declaration version. The base does not say whether to resolve the highest tag, compare against all candidates, or use an existing lock. Each choice gives different results and potentially introduces acquisition into verification.

## Proposed change

Keep recorded package origin in the existing operator-selected provisioning pipeline and its protected lock, with source authorization checked separately by the admission/signature policy. Environments §1.3 expressly says a lock is a record, not an authorization token or provenance proof. Make any skill-supplied acquisition recommendation non-authoritative, or omit it and use the existing hint/profile selection. Do not import package resolution into the pure requirement check merely to support optional setup advice.

If the design retains an identity constraint, specify exact closed identity types, canonicalization, lock ownership, and evidence strength. Report separately: observed configuration, manager-recorded origin of an admitted package, and scoped operator assertion. Recorded origin is meaningful attribution to the admitted snapshot, not cryptographic proof by the lock itself; source-signature verification remains a separate resolution result. A digest copied into repository-controlled native config is not protected evidence. None of these proves authentication, connectivity, or running executable identity.

## Rubric impact

- E1/E2: eliminating normative package identity avoids a second resolution/provenance contract.
- E5: a service requirement can be portable across deployment sources; a package-origin constraint deliberately narrows it.
- E6: recipe equality and operator trust must not be presented as verified provenance.
- E7: range resolution and each equivalence relation need deterministic definitions and vectors if retained.

## Confirmed by

- `ivmbp_swarma-mcp-deps_astra-02`, `MCP 2026-10-14, f-package-is-not-service, note 03`: independent recipe/provenance confirmation, plus its corroborating topic root `MCP 2026-10-14, f-package-is-not-service, note 02`.
- astra-01 independently confirmed astra-02's equivalent candidate in `MCP 2026-10-14, f-package-is-not-service, note 04`.
- `ivmbp_swarma-mcp-deps_wonder-01`, `MCP 2026-10-14, f-package-is-not-service, note 05`: independent confirmation including lock ownership and missing cross-requirement unification.
- `ivmbp_swarma-mcp-deps_wonder-02`, `MCP 2026-10-14, f-package-is-not-service, note 06`: independent confirmation including the lockless range and HTTP-package cases.
- `macmini_swarma-mcp-deps_wonder-12`, `MCP 2026-10-14, f-package-is-not-service, note 07`: independent cross-host source check confirms the lockless no-range rule, bare-command runtime resolution and provenance-free output; recipe, deployment source and recorded origin remain distinct evidence grades.

One consolidated finding owns the overlapping topics. Recipe/provenance separation and the lock-ownership subclaim both have independent seat confirmation, including Mac mini. Finding corroboration is separate from the whole-design comparisons and their rubric limits in [this seat's verdict](../verdicts/astra-01.md).
