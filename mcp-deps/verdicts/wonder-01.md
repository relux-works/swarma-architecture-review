# Verdict: wonder-01 (alternatives hunter)

Seat: `wonder-01` (ivmbp, Muse Wonder full 1.0). Sources read at curator-spec
`a9c03be`, curator `5234cf3`, this repository at `1c6010a`. Pulls were blocked
by the sandbox; all citations are to the local clones named in the mission.
Status: round-1 position; will update as the debate moves.

## Preferred design

**Composite: alt-skill-ships-declaration (provisioning) + alt-names-local-evidence
(checking/binding), with no change to any skill-manifest byte.**

1. **Require — unchanged.** `dependencies.mcp_servers` keeps the v5 grammar
   (name key, mandatory `hint`, documentary `transport`, `required_in`).
   The key is documented as an author-chosen capability label, not a
   deployment identity.
2. **Ship — the snapshot is the pin.** A skill package root MAY contain
   `agent-mcp.json` (environments §2.2 schema 1, unmodified). It is not
   agent-facing context (same position as `agent-skill.json` under core
   §3.1). On an unsatisfied requirement whose key equals the declaration's
   `name`, the manager prints the §2.3 surfacing row and the exact
   remediation. Malformed or non-matching files are inert (warning at
   most). The declaration bytes ride inside the resolved, audited skill
   snapshot, so no range resolution, lock owner, or second pin exists.
3. **Provision — existing channels only.** A shipped declaration is a
   recommendation with no authority. It takes effect only when the
   operator selects it into a profile (`requires.mcp`, git source = the
   skill's canonical source; §2.2 allowlist, signer policy, strict
   profile audit, §5.8 materialization unchanged) or accepts a csk
   native write under protected exact-plan consent (f-consent-binding).
   Transitive skills surface; they never provision.
4. **Check — launch-scoped, three evidence labels.** Manager §6 name
   semantics are scoped to the selected launch (f-launch-universe);
   profile-resolved MCP names count for profile-scoped installs. Status
   distinguishes observed configuration, manager-protected provenance,
   and scoped operator assertion for opaque providers (f-opaque-provider,
   f-package-identity). Assertions live in protected manager state,
   never in a checkout, and stop satisfying when later observation
   contradicts them. No identity matching against native bytes anywhere.
5. **Auth — nothing new.** No auth field, no agent-mcp schema 2.
   `env_names` drive guidance; OAuth stays in the native client; status
   stays "configured / auth not checked"; no health checks. HTTP header
   env-binding is honestly out of scope for schema-1 declarations
   (§5.8 serializers emit URL/type only); such servers are configured
   natively and satisfy by name.

## Rubric scores

E3 is scored **literally** (the manager never *reads* a credential): every
design that keeps §6 native inspection reads mixed native files wholesale
(curator `internal/mcp/mcp.go:240-276`), so none earns E3=2 as the rubric is
written. The "bounded" column applies the interpretation "no credential
semantics (no expansion, resolution, auth execution, persistence, logging,
egress)"; choosing between them is an operator disposition (f-secret-boundary),
and I report both until it is made. Totals compare only designs that meet the
goal; the status quo (12 literal, E8=0 — repeated manual wiring, no
dependency carrying) is listed for calibration and excluded for that reason.

| Design | E1 | E2 | E3 lit | E4 | E5 | E6 | E7 | E8 | Total (lit / bounded) |
|---|---|---|---|---|---|---|---|---|---|
| Status quo (§6 only) | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 0 | 12 / 13 (fails goal) |
| Base (Require/Provide/Bind, as written) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8 / 9 |
| alt-names-local-evidence (astra-01) | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 12 / 13 |
| alt-skill-ships-declaration (wonder-01 A) | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 13 / 14 |
| **Composite A + names (preferred)** | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | **12 / 13** |
| alt-capability-tools (wonder-01 B) | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 7 / 8 |
| alt-gateway-proxy (wonder-01 C) | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 2 | 5 / 5 (disqualified) |

The composite scores one point below A alone and I still prefer it: A's
E4=1 is a real exclusion (a connector invisible to §6 file surfaces can
never satisfy), and the operator's goal names the zoo explicitly. The
rubric guides; it does not outvote the goal. A alone is my fallback if
the collective judges the binding record one concept too many for
revision 1 — it can be added later without touching A.

### Row justifications (only where a design scores below 2, or the base's claim differs)

- **E1, base = 1, not 2.** The wire delta is three programs, not one
  field: a new manifest schema lane (`mcpRequirement` is closed,
  `common.schema.json`; curator `skillspec/parse.go:724` rejects unknown
  keys; draft 9 reuses the v5 node by `$ref` and "adds only the
  directory member", core.md:195-197), agent-mcp schema 2 for the auth
  class (`agent-mcp-v1.schema.json` is closed, no auth member), and a
  binding-state contract (manager §1 rejects unknown config fields).
  A earns 2: zero fields, zero formats — one MAY clause naming a file
  position that §2.2 already defines. Names/composite earn 1: the
  protected binding record is a genuine new concept.
- **E2, base = 1.** Identity checking needs per-client normalizers over
  six native dialects, an endpoint equivalence relation, and a range
  resolver in the skill lane — where core §4.4 forbids ranges and no
  lock/marker member exists to record a resolution (markers record
  found-agents only). A/names reuse §2.2/§2.3/§5.8, the allowlist,
  audit, and §6 as they stand: 2.
- **E4, base/A = 1; names/composite = 2.** Plugins and cloud connectors
  expose neither a §6 file entry nor an identity the manager can read;
  the base's binding discharges only its identity conjunct, not
  configured presence (f-opaque-provider). Only an explicitly labelled,
  scoped operator assertion lets those members satisfy without a
  client change — hence 2 only where that mechanism exists. (This
  revises my topic post, which scored A at E4=1 for the same reason;
  A alone still does.)
- **E5, base/B = 1.** A new manifest schema version MUST be rejected by
  older readers (COMPATIBILITY.md), including indefinite rc.10-baseline
  partial clients; the skill becomes uninstallable there rather than
  degraded. A/names keep v5 bytes: old managers install, check, show
  the hint, and ignore the extra file. 2.
- **E6, base = 1 as written.** "Unknown" identity semantics and
  "explicit operator consent" are unspecified (f-consent-binding);
  both are fixable, at E1 cost the base does not count. A/names/composite:
  unknown never satisfies silently, assertions are labelled, writes
  require exact-plan consent: 2.
- **E7, base = 1, names/composite = 1, B = 0.** The base leaves identity
  equivalence, range unification across a skill closure, and binding
  invalidation unspecified. The composite's binding semantics still
  need behavioural vectors (manager-profile prose, manager-owned
  storage). B has no closed capability namespace at all: 0.
- **E8, everything serious = 1.** One operator action per new server
  (profile selection or exact-plan consent) is the floor set by E6;
  nobody honest reaches zero. The base additionally imposes alias
  authoring whenever author and operator names differ.

## Smallest set of changes to the base that reaches the preferred design

1. **Delete** `server` from Require, the identity conjunct from Provide,
   endpoint requirements, and the declaration `auth` class. Keep the
   base's correct separations: requirement ≠ provisioning, status never
   claims connected/authenticated, no health checks.
2. **Replace** the alias map with protected, scoped operator bindings/
   assertions in manager state (never project files), carrying the three
   evidence labels; scope all satisfaction evidence to the selected
   launch (f-launch-universe).
3. **Replace** "provision from `server.package`" with: provision only
   operator-selected declarations through §2.2/§5.8 (profiles) or the
   separately governed csk native writer under f-consent-binding's
   exact-plan consent. Endpoint-only provisioning was already excluded
   by the base; this extends the same honesty to packages.
4. **Add** the one MAY clause: skill-root `agent-mcp.json`, surfaced on
   exact name match with an unsatisfied requirement of the same package.
5. Spec work, complete list: core §3/§4 prose (item 4), manager §6 prose
   (launch scoping, surfacing, evidence labels, assertion semantics),
   conformance vectors, one decision record. **No schema file changes.**

## Answers to the base's five open points

1. *Identity for unseen servers:* do not check identity. Observed /
   provenanced / asserted labels replace it; unknown without an
   assertion stays unsatisfied for both `any` and `all`.
2. *Transport:* keep documentary (manager §6; tightening needs a spec
   change first, curator review H3). Report observed transport where
   known; never gate on it in this revision.
3. *Schema home:* moot under the preferred design — no field, no new
   schema version, no fork of draft 9 or Skillfile schema 3.
4. *Native writes vs managed homes:* keep the lanes disjoint by
   destination: native writers refuse marker-carrying managed homes
   and reserved channel files (`curator-mcp.config.toml`); profile
   materialization never writes native in-place homes (§5.8). Same-name
   precedence collisions are launch-scoping facts (§7.8 residuals),
   reported, not hidden by name unions.
5. *Is the alias map one concept too many?* As an identity mechanism,
   yes — delete it. As protected operator binding/assertion state, it
   is the one new concept the zoo genuinely forces; `server` identity
   cannot replace it, because the opaque members expose no identity
   to match.

## What would change my mind

- Evidence that clients expose a read-only, connection-free inventory
  (servers + tools) — re-scores alt-capability-tools upward sharply.
- Evidence that skill-root extra files are stripped before the manager
  can read the snapshot in some conforming lane — would force A to
  name a different carrier (companion context package only).
- An operator ruling that author-pinned server provenance is a hard
  requirement (not a preference) — revives a *narrowed* base: identity
  as manager-protected provenance only, never native-byte inference.
