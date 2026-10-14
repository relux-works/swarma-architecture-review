# Verdict: wonder-01 (alternatives hunter)

Seat: `wonder-01` (ivmbp, Muse Wonder full 1.0). Sources read at curator-spec
`a9c03be`, curator `5234cf3`; this repository fast-forwarded by the convener
to `4d94105` (my sandbox cannot pull or sign: uid-502 SSH/signing failure;
newer peer commits are known from the room). The amended E3 row was verified
on disk at `534e384` and matches the convener's in-room disposition exactly.
Round-4 revision: supersedes rounds 1–3 where they differ (two-axis
evidence, completeness table, dual E8 readings).

## Preferred design

**Composite: alt-skill-ships-declaration (provisioning) + alt-names-local-evidence
(checking/binding), with no change to any skill-manifest byte.**

1. **Require — unchanged.** `dependencies.mcp_servers` keeps the v5 grammar
   (name key, mandatory `hint`, documentary `transport`, `required_in`).
   The key is an author-chosen capability label, not a deployment identity.
2. **Ship — the snapshot is the pin, two-stage surfacing.** A skill
   package root MAY contain `agent-mcp.json` (environments §2.2 schema 1,
   unmodified). It is not agent-facing context (same position as
   `agent-skill.json` under core §3.1). Because skill-lane audit can be
   advisory, pre-admission display is **metadata-only**: on an
   unsatisfied requirement whose key equals the declaration's `name`,
   the manager shows a candidate notice (name, transport, detector
   verdict class, remediation route) — never raw `args`/`url`. Full
   §2.3 rows appear only at their existing point, after strict profile
   audit at declaration admission, and admission re-runs the MCP
   allowlist, signer policy and audit on the declaration source (skill
   admission proves nothing about MCP admission). The shipped
   `args`/`url` enter the `context-secret-material` detector scope
   (§2.2 line 508, §9.1) as an admission gate. A malformed shipped file
   MUST warn (metadata-only), never fail the skill install, never stay
   silent; credential material follows normal blocking policy. At most
   one root declaration; multi-server authors ship a companion context
   package. Remediation references the exactly resolved skill
   *revision*, never a skill version tag, and routes through an existing
   context package (`requires.mcp`) — profile install consumes context
   roots (§9.1); no naked-declaration install or new command is added.
   Source kind stays §2.2 git-only for the profile lane: a declaration
   from a path/local snapshot may be displayed but not adopted into a
   profile (no canonical identity for the allowlist); the csk native
   lane may use it only under exact-plan consent binding the snapshot
   digest, under its own separately reviewed contract.
3. **Provision — existing channels only.** A shipped declaration is a
   recommendation with no authority. It takes effect only when the
   operator selects it into a profile (`requires.mcp`; §2.2 allowlist,
   signer policy, strict profile audit, §5.8 materialization unchanged)
   or accepts a csk native write under protected exact-plan consent
   (f-consent-binding; the requiring-skills list is display attribution
   only — consent renews on changed execution, routing, targets or
   destination, never because another skill uses an unchanged provider,
   and no per-skill MCP use-authorization is claimed). Transitive
   skills surface; they never provision.
4. **Check — launch-scoped, two evidence axes.** Manager §6 name
   semantics are scoped to (agent, scope, selected launch);
   profile-lock MCP names are eligible evidence for profile-scoped
   installs; channel-excluded entries never count for that launch
   (f-launch-universe). *Acceptance* is recorded per (requirement
   identity, target agent, selected launch) — never per server — as
   **observed-effective** or **asserted**, in an install-marker
   successor; *origin* (**recorded-origin** | foreign) is orthogonal
   annotation from existing lock/ledger evidence (a record, never
   provenance proof, §1.3 lines 205–206) and never satisfies anything
   by itself — a locked declaration whose effective entry is missing,
   disabled or overridden satisfies nothing, and stale origin never
   outranks current negative evidence. Old markers read as *legacy
   native presence* only and never discharge a managed-launch claim.
   Which surfaces are authoritative-and-complete is a per-launch table
   the governed text must carry (claude managed: complete only under an
   actually applied strict channel — §5.8 writes no channel file for an
   empty set; codex managed: complete only under seed revision B with
   the trusted-project residual inspected; opencode managed:
   incomplete by merge; pi: complete-empty for the revision-1 managed
   adapter (§7.8, recorded on 0.84.2; no claim about native/plugin
   integration or later releases); native: incomplete for
   plugins/connectors, so file-absence is never authoritative-negative
   there). Floor rules: an assertion never replaces allowlist, signer
   or audit admission and never suppresses a hardened refusal; the
   provider selector is a matching identity, never a byte fingerprint,
   and opaque asserted providers carry **no durable drift detection** —
   internal change behind the operator label is explicitly unverified. Binding
   records enumerate exact requirement identities (skill package
   identity + requirement name, batched, no name wildcard), consumer
   scope, target, launch descriptor, and a provider selector (configured
   name + surface/handle class), since name+agent+kind cannot
   distinguish an opaque connector from an unrelated disabled native
   entry. Changed membership, scope, target or launch descriptor is a
   non-matching context; invalidation is otherwise the closed list
   (revocation; bound selector observed disabled/absent in a surface
   authoritative for that launch; launch excludes the provider class) —
   absence from the six native files alone never defeats an assertion.
   No identity matching against native bytes.
5. **Secrets bound, stated explicitly.** The checker compares in memory
   only server name, disabled state, and stdio-command presence; it
   never persists, logs, or surfaces raw `argv`, `url`, env, or header
   bytes read from native files; diagnostics carry (file, server name,
   reason class) only. The bare stdio command *name* may surface in the
   existing §6 PATH warning; nothing else leaves the checker. §2.3 surfacing of *declaration* args is a
   different surface: audited package bytes inside detector scope.
6. **Auth — nothing new.** No auth field, no agent-mcp schema 2.
   `env_names` drive guidance; OAuth stays in the native client; status
   stays "configured / auth not checked"; no health checks. HTTP header
   env-binding is out of scope for schema-1 declarations (§5.8 emits
   URL/type only); such servers are configured natively and satisfy by
   name *for an effective native launch only* — a strict managed launch
   reports them not materializable, and no assertion erases that.

Spec-delta sketch D1–D6 (core MAY clause + two-stage surfacing; manager
§6 launch-scoping + bound; binding-record semantics; install-marker
successor for per-launch evidence labels; §2.3 `url` visibility;
exact-plan consent) is posted in topic alt-skill-ships-declaration
(round 2 `$6Ju0U6dvorEvdtJ0MsUkDEFhhMjnZPdD4btQilsiQhQ`, revised round 3
`$e5s3ZnvCckXlXR8HgOhJu7XHsOUk3W_5O2ueV0Ga37I`). Homing fork, counted
honestly: bindings as a successor member of the existing manager-config
family (plus the marker successor) retain E1=1; a new standalone record
family is E1=0 under the mission anchor even in manager-owned storage.
The sketch chooses the manager-config successor; system-file lockability
of assertions is flagged as a governed open choice. No skill-manifest,
agent-mcp, Skillfile, or fragment schema changes. Alternative A alone —
ship + candidate notice with *today's* §6 checking unchanged — needs
only D1 + the §6 bound sentence (zero schema files), which is why it is
scored separately below; my round-1 "zero schema files" claim for the
composite is withdrawn.

## Rubric scores

E3 primary = **amended** reading (never uses/stores/forwards/logs/tests a
credential *value*; unavoidable foreign-byte handling explicit, bounded,
metadata-only; unstated bound caps at 1). E3-original ("reads/touches
values", 0-anchor) is reported alongside per the convener's disposition;
it is 0 for every native-inspecting design, status quo included — my
round-1 literal 1 is withdrawn. E8 is scored on first setup of an
unconfigured provider (the goal's case); wonder-02/astra seats score
the already-configured common case one point higher on N/composite —
within proof tolerance, flagged, not averaged. A design must also pass
wonder-02's G0 (a skill dependency can actually reach configured state
through the design); the status quo fails G0 and is calibration only.

| Design | E1 | E2 | E3 amd | E4 | E5 | E6 | E7 | E8 | Total | E3-orig | G0 |
|---|---|---|---|---|---|---|---|---|---:|---:|---|
| Status quo (manager §6) | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 0 | 11 | 0 | fail |
| Base as written | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8 | 0 | partial |
| alt-names-local-evidence (astra-01, N) | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 12 | 0 | pass |
| alt-skill-ships-declaration rev.3 (A, standalone scope) | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 13 | 0 | pass |
| **Composite N+A (preferred)** | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | **12** | 0 | pass |
| alt-capability-tools (B) | 1 | 1 | 2 | 1 | 1 | 1 | 0 | 1 | 8 | 0 | partial |
| alt-gateway-proxy (C) | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 2 | 5 | 0 | pass, disqualified |

A-standalone is scored on its own declared scope (provisioning
recommendation + legacy §6 checking), so it keeps E2=2 without borrowing
the composite's checker, and inherits §6's checking debts as E6=1
(labelled legacy presence). A and the composite are therefore a frontier
— minimality (A: E1/E2/E7) versus zoo completeness (composite: E4/E6) —
and the goal text breaks the tie toward the composite; A remains the
shippable revision-1 subset. Convergence so far: wonder-02, astra-01,
astra-02, astra-03 and this seat agree within one point on every row
for every design above (largest spreads: E2 and E8, both test-definition
differences now explicit; wonder-02's composite digits sum to 13,
printed 14 — clarification requested). Proof still requires second-host
independent scoring (astra-11…13, wonder-11/12).

### Row justifications (below 2, or where the base claims otherwise)

- **E1.** Base = three programs, not one field: new manifest schema lane
  (`mcpRequirement` closed; curator `skillspec/parse.go:724`; draft 9
  "adds only the directory member", core.md:195–197, and reuses the v5
  node by `$ref`), agent-mcp schema 2 for the auth class, and binding
  state (manager §1 rejects unknown config fields). A = 2 (zero fields,
  zero formats). N/composite = 1 only on the manager-config-successor
  homing (one new member on an existing object family plus the marker
  successor); a new standalone binding record family is 0 under the
  mission anchor even in manager-owned storage (astra-01, round 3).
- **E2.** Base identity checking needs per-client normalizers, an
  endpoint equivalence relation, and a range resolver where core §4.4
  forbids ranges and no lock/marker records a resolution. Launch-scoped
  evidence-aware checking (N, composite) is new checker machinery
  beyond §6 presence — scored 1 under wonder-02's inside-scope test,
  which I adopt. A alone reuses §2.2/§2.3/§5.8/§6 inside their scopes: 2.
- **E3 (amended).** Base and status quo = 1: no bounded-handling bound
  stated for the (new) checker/matcher. A/N/composite = 2 only with the
  bound, the detector-gate sentence, and metadata-only pre-admission
  display stated as above; A round 1 lacked them and was correctly
  scored 1 by wonder-02.
- **E4.** Opaque plugins/connectors expose neither a §6 entry nor a
  readable identity; only labelled assertions (N, composite) let them
  satisfy without a client change. Pi (no MCP channel in the
  revision-1 managed adapter, §7.8 recorded on 0.84.2) and
  project-scoped Windsurf (§6: none) are client-capability bounds
  outside every design; `required_in: all` naming them is unsatisfiable
  by construction and must say so.
- **E5.** New manifest schema versions MUST be rejected by older
  readers (COMPATIBILITY.md), including indefinite rc.10-baseline
  partial clients — uninstallable, not degraded (base, B = 1). v5 bytes
  plus an inert root file degrade gracefully (A, N, composite = 2).
- **E6.** Base as written leaves unknown-identity semantics and consent
  unspecified (f-consent-binding): 1, fixable at uncounted E1 cost.
  Status quo and A-standalone = 1: pre-existing debt (disabled-entry
  decoding is non-uniform in curator's reader; name unions ignore
  launch scope), honest only when labelled legacy presence. The
  composite earns 2 by launch-scoping, per-launch evidence labels, and
  consent before writes.
- **E7.** Base: equivalence, range unification, binding invalidation
  unspecified. N/composite: D1–D6 must exist as governed text with
  truth-table vectors before 2. B: no closed tool namespace exists: 0.
- **E8.** One consent/selection per newly provided server is the E6
  floor; status quo demands repeated manual wiring (0). C's 2 is real
  and irrelevant given its E3/E6 zeros.

## Smallest set of changes to the base that reaches the preferred design

1. **Delete** `server` from Require, the identity conjunct from Provide,
   endpoint requirements, and the declaration auth class. Keep the
   base's correct separations: requirement ≠ provisioning, status never
   claims connected/authenticated, no health checks.
2. **Replace** alias-as-identity with D3 protected bindings/assertions
   and D2 launch-scoped two-axis evidence (D4).
3. **Replace** "provision from `server.package`" with operator-selected
   declarations via §2.2/§5.8 or the separately governed csk writer
   under D6 exact-plan consent.
4. **Add** D1 (skill-root `agent-mcp.json`, two-stage surfacing) and D5
   (§2.3 `url` visibility). Nothing else.

## Answers to the base's five open points

1. *Identity for unseen servers:* do not check identity. Observed /
   observed-effective / asserted acceptance (origin as annotation)
   replaces it; unknown without an
   assertion stays unsatisfied for both `any` and `all`.
2. *Transport:* keep documentary (manager §6; tightening needs a spec
   change first, curator review H3).
3. *Schema home:* moot — no field, no new manifest/declaration schema
   version; the one successor is the install marker (D4).
4. *Native writes vs managed homes:* disjoint by destination — native
   writers refuse marker-carrying managed homes and reserved channel
   files; §5.8 never writes native in-place homes; §7.8 precedence
   residuals are reported by launch-scoped checking, not hidden.
5. *Alias map one concept too many?* As identity, yes — deleted. As
   protected binding/assertion state it is the one new concept the zoo
   forces; `server` identity cannot replace it because opaque members
   expose no identity to match.

## What would change my mind

- A client read-only, connection-free inventory (servers + tools) in
  local evidence — re-scores alt-capability-tools upward sharply.
- Evidence that skill-root extra files are stripped before manager
  snapshot access in some conforming lane — forces A to companion
  context packages only.
- An operator ruling that author-pinned provenance is a hard
  requirement — revives only a narrowed base: recorded origin from
  manager-protected state, never native-byte inference.
