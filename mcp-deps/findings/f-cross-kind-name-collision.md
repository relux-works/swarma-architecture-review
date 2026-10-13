# Same-name skill and MCP packages do not compose as two existing resolver members

- Lens: spec fit and minimality, adversarial second five.
- Author: `ivmbp_swarma-mcp-deps_astra-04`.
- Status: proposed.
- Confidence: high for the pinned implementation constraint; no runtime test.
- Topic: `f-cross-kind-name-collision`; originating debate in
  `alt-skill-ships-declaration`.

## Problem

BASE offers to provision a skill's declaration package through existing
environments machinery. Alternative A similarly recommends addressing a
co-located `agent-mcp.json` through an existing context root. Neither recipe
can assume that a selected skill `docs` and an MCP declaration package `docs`
will coexist as two members of the current resolver's closure.

File co-location and package-kind selection are different facts. Identical
source, directory and commit do not remove the resolver's one-kind-per-name
behavior. This constrains the claimed reuse; it does not invalidate an inert
recommendation, distinct-name packages, or named external fulfillment.

## Evidence

Sources: curator `5234cf38833554542e68afade15951c6e56ed89e` and curator-spec
`a9c03be237b723b5bf87aed070165ad6f68b2586`, read-only. No code changes,
execution probes, builds, or tests were performed.

1. `internal/contextresolve/contextresolve.go:316–317` stores constraints and
   kinds by name. `add():409–420` explicitly coerces a later different kind to
   the already recorded kind, with the comment “One name, one kind”.
2. `build():907–920` traverses one selected entry per name and emits its one
   selected kind into the lock/result.
3. `internal/envprofile/gitsource.go:721–755` constructs the root's skill and
   MCP edges, then sorts by name/kind. `Manifest():238–275` loads only the
   selected package kind; it does not load both manifests because they coexist.
4. `internal/envprofile/managed.go:205–226` materializes MCP servers only from
   lock members whose kind is MCP. A skill-kind member is not also a server.
5. The distinction is important: `internal/contextlock/contextlock.go:245–249`
   checks lock uniqueness by `(kind,name)`, and environments §1.3 describes
   sorting by `(kind,name)`. The finding therefore does **not** assert that the
   normative lock format expressly prohibits two kinds with the same name.
   Environments §1.4's one-name/one-commit resolution invariant does not itself
   prove dual-kind loading either. The current resolver is the concrete limit.

Source-derived counterexample: an operator root declares both `requires.skills.docs`
and `requires.mcp.docs` at the same source and revision. Both manifests exist.
The current resolver has a single selected `docs` slot, so this cannot be
represented as both a selected skill and a selected MCP member through the
claimed unchanged path. Which kind wins depends on how the edges enter; no
claim of a reproduced end-user error or security exploit is made here.

## Proposed change

Qualify provisioning guidance and adoption vectors: the selected joint closure
must have distinct package names for the skill and MCP member. A colliding
adoption plan must be detected and deferred/refused, not advertised as successful
dual-kind reuse. An existing external provider can still satisfy the named
skill requirement through N's evidence contract.

Recommend distinct package names when authors choose new names. Do not silently
rename an existing skill, change the declared server name, invent an alias, or
rewrite the resolver as part of a “zero-schema” recommendation feature. A future
kind-aware resolution change needs its own specification/compatibility review.
This is also a testable qualification of BASE's optional package-provisioning
offer, not only of co-location.

## Rubric rows affected

- **E2:** reuse is conditional on what the existing resolver actually accepts;
  silently adding kind-aware identity would be new machinery.
- **E7:** positive distinct-name and negative same-name joint-adoption vectors
  must be in the governed adoption contract. E7 for N/A+N remains 1 pending it.
- **E8:** an existing colliding package may require author/operator remediation;
  do not advertise the optional recommendation as a universal one-action setup.

## Confirmed by

- `ivmbp_swarma-mcp-deps_astra-06`, event
  `$cjkXXsAKqa1RgA871RL9IIK9QBe3kTfn9G17XP4UnYU`, independently traced the
  name-keyed resolver, single-kind build and MCP-only materialization at the
  same implementation pin. Confirmed distinct-name adoption or deferral;
  explicitly did not claim that N or distinct-name co-location is defeated.
- Initial request: `$iUc_uDX_kiEwtByLrYzC4qpzhIODJGkvPXIehrKehkk`.
- Author's clarification, including lock-format distinction:
  `$DXLx6b3LVuLDCnJ_1jDtgxYMXNQ3NEp521MCqE3HO2k`.
