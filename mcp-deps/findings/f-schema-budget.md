# The base understates its schema and concept budget

- Lens: spec fit and minimality.
- Author: `ivmbp_swarma-mcp-deps_astra-01`.
- Status: proposed.
- Confidence: high.
- Topic: `f-schema-budget`, `$lWt_mcoZ5R8-lyARH6v7AWwa5SutuNS9dl03UoFt62Y`.

## Problem

The base calls itself one new optional field, but it also needs declaration auth metadata, operator binding authority, identity/evidence semantics, and a versioning decision. None is already supplied by the current requirement grammar. An optional member is not backward-compatible with an old closed schema merely because an author may omit it.

## Evidence

Read-only local sources: curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`; curator `5234cf38833554542e68afade15951c6e56ed89e`. Source clones were clean but not fetched because they are outside this seat's writable roots. This is source inspection, not runtime or conformance execution.

1. `schemas/v1/common.schema.json:610–618` permits only `hint`, `transport`, and `required_in` in `mcpRequirement`, with `additionalProperties: false`. Shared `dependenciesV5` refers to that definition. Adding `server` to it changes already released manifest lanes.
2. `protocol/core.md:159–198` says versions are downward gated and released schemas 2–8 reject unknown members. The current unreleased schema 9 adds only dependency `directory`. `schemas/draft-sources-v2/README.md` identifies the separate draft namespace and marker-v6 support for manifest 9.
3. `COMPATIBILITY.md:17–25` governs each schema series separately, requires explicit rejection of unsupported versions, and forbids redefining old schema bytes. `GOVERNANCE.md`, Changes and Decision record, requires affected prose/schemas, positive/negative vectors, compatibility/security analysis, review, and a decision for new versions or changed trust semantics. CIP acceptance alone does not amend a release.
4. `schemas/v1/agent-mcp-v1.schema.json` closes both server variants and the outer object. There is no `auth` or header-reference member. `protocol/environments.md` §2.2 provides `env_names`; §5.8 emits command/args or URL, not HTTP header routing. An auth class alone would not implement generic HTTP environment authentication.
5. `profiles/manager.md:16–32` closes the logical machine configuration. Neither aliases nor opaque-provider authority are existing requirement fields. Machine-local layout can be manager-specific, but an authority-bearing binding is still new semantics, with scope and invalidation rules to specify.
6. The supplied [csk proposal](../inputs/csk-mcp-design-proposal-v1.md) explicitly anticipates a later declaration schema for headers/auth. [The lane review](../inputs/curator-review-of-csk-design.md), H1/H2, rejects private allocation of spec-owned schema versions.

## Proposed change

Preserve released manifest-v5–8 and declaration-v1 bytes and meanings. If identity-bearing requirements remain, introduce a governed schema lane or deliberately amend the unreleased draft; allocate the final version through the specification process. Draft 9 is not claimed immutable, and this finding does not demand a particular next version number. Inspect marker version support and evidence representation alongside the manifest change.

Count auth metadata and protected binding semantics separately. Prefer removing normative `server` identity and machine-readable auth class from this feature when they are not necessary: retain existing named requirements, existing operator-selected declaration packages, and native client auth guidance. If bindings are needed for aliases/opaque providers, combine those uses in one explicit operator-controlled contract rather than inventing two maps. Do not treat a repository-authored alias as operator approval.

Minimal named-requirement checking does not itself require a new install-marker version. Existing `mcp_servers` may remain legacy sorted native observations, with explicit reliance in the governed operator-config successor and stronger selected-launch status computed transiently. Version a richer portable receipt only if that stronger result must be persisted. The new scoped-verification semantics and old-reader behavior still require an explicit extension; unchanged marker bytes do not erase the authority change.

## Rubric impact

- E1: a count of one field on the skill hides additional state and concepts.
- E2: aliases, assertions, auth classes, and generic HTTP routing are not all reuse of existing machinery.
- E7: the exact schema series, evidence carrier, semantics, and governance path must be specified before full credit.

## Confirmed by

- `ivmbp_swarma-mcp-deps_astra-03`, `$4zZN8l-BByqu1Xjm7HaDA1wwxaIef0i2UIAAFxm1nPM`: independent closed-schema confirmation and HTTP-routing limitation.
- `ivmbp_swarma-mcp-deps_astra-02`, `$5cDfMWa8Mcu2048EIASXRlt6A9Hg-7amV9sTif9r9rk`: independent requirement/configuration/declaration confirmation.
- Additional auth evidence from astra-02: `$V8qAIOXAUtmT49-cACD7FccLjSLAFXqmwSfSoWAab8c`.
- `macmini_swarma-mcp-deps_astra-11`, `$KoKVkUqcYkat6O2_XqNcx5zDxclzgzMVkvWTDXBoTpM`: independently froze scores before reading peer verdicts, then confirmed the shared-schema/version trap at the same source pins and sharpened marker minimality. This seat accepted the optional-marker correction in `$rXK97-aRDmaw_fmGgx5GxLtTOhfgfqouVQpV0k90IBo`.
- `ivmbp_swarma-mcp-deps_astra-04`, `$T_QPlXpIGmdMnzwkPeMR6NVRyMAR5IdGLrCPoarg0Bk`: second independent group's frozen-score review confirms all three closed schema/configuration boundaries and the optional-marker minimum.
- `macmini_swarma-mcp-deps_wonder-12`, `$9ifByGUJvKO2piul7qxtF0WQHp-y_ZLwCa99fIsgmoU`: independently confirms shared closed requirement schemas, the closed declaration schema and the compatibility/governance constraint on any retained wire identity.

The finding now has confirmation across hosts. Finding corroboration alone is not the winning-design proof; the separate per-row comparisons and original/amended rubric limitations are recorded in [this seat's verdict](../verdicts/astra-01.md).
