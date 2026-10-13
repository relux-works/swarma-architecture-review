# astra-04 — independent spec-fit and minimality verdict

Seat: `ivmbp_swarma-mcp-deps_astra-04`, second independent five, ivmbp.
Date: 2026-10-14. State: independent round 1; adversarial comparison pending.

## Independence and evidence boundary

This table and preference were formed before reading any first-five verdict
file or debate body. The mandatory onboarding `a2a topics` exposed topic
titles, not their arguments. The evidence read was the complete mission,
base, all three inputs, and the local specification and implementation.
No web, credential reads, source edits, builds, or runtime tests were used.
The source clones are read-only under this seat's sandbox; they were not
updated. Evidence pins:

- curator-spec: `a9c03be237b723b5bf87aed070165ad6f68b2586`.
- curator: `5234cf38833554542e68afade15951c6e56ed89e`.
- Base and inputs: this review repository as initially pulled.

Normative evidence outranks an implementation or an accepted CIP. In
particular, GOVERNANCE.md says CIP acceptance does not amend released prose,
schemas, or vectors; CIP-0006's adopted direction is not shipped MCP policy.

## Candidates and independent scores

**B — base as written:** Require / Provide / Bind, including skill-side
package or endpoint identity, recipe equality, aliases, optional provisioning,
and declaration auth classes.

**N — named requirements, operator-selected providers and evidence:** retain
the existing portable skill requirement; use existing declaration packages and
profile resolution for optional operator provisioning. Add one protected
machine-configuration binding map only where a native label differs or a
provider is opaque. Its records are explicitly new evidence/authority, not
existing machinery disguised by a small JSON diff. A record is scoped to the
requiring skill source, logical requirement, target client/configuration
instance, and native versus managed launch context. It identifies either an
observed provider label or an operator assertion of an opaque provider.
Package acquisition identity remains in the existing provisioning lane.

The effective result distinguishes observed configuration, explicit operator
acceptance, absent/disabled, and unknown. An assertion is never printed as
observation or authentication, cannot defeat a known disable or strict-channel
exclusion, and is not written by a repository. It is invalid outside its
recorded scope or after observable context changes; invisible provider changes
remain an explicit limitation of operator assertion. Any/all quantifies over
the originally selected targets, never a filtered capable subset. Legacy
manager §6 behavior is retained as a separately identified static check;
stronger effective-launch claims require their own governed contract.

**I — repaired identity base:** N's evidence, launch and authority rules plus
a versioned, closed skill identity selector. It separates endpoint identity,
package provenance and explicit binding; command/args equality never proves
provenance. It adds a governed declaration auth extension only if independently
needed. This is viable, but carries more contracts than the owner's goal needs.

**C — context-package-only provisioning:** leave skill name requirements
unchanged and provision only existing profile `requires.mcp` packages; do not
add bindings or opaque-provider evidence. This is a useful bounded deployment
pattern, not a solution for the entire zoo.

| Row | B | N | I | C | Evidence and justification |
|---|---:|---:|---:|---:|---|
| E1 New concepts/fields | 0 | 0 | 0 | 2 | B adds an identity union, alias/binding authority and auth grammar, not merely one field. N honestly budgets a new binding/evidence record family; I adds still more. C adds no wire object. Core §4; common.schema.json:610–642; environments §2.2. |
| E2 Reuse | 1 | 1 | 1 | 2 | B/N/I reuse declarations, materialization and audit, but all need new evidence/binding machinery. C uses existing profile resolution unchanged. Environments §§2.2, 5.8, 6; internal/envprofile/managed.go:205–226. |
| E3 Secrets, amended | 1 | 2 | 2 | 2 | B's foreign-config parsing bound is unstated. N/I/C explicitly limit foreign bytes to private bounded parsing, emit names/state only, perform no auth or health request, and never retain raw native argv/URL/env. internal/mcp/mcp.go:245–283 proves generic native parsing already occurs. Environments §§5.8, 10.3 separate manager metadata from launcher value transport. |
| E4 Zoo | 1 | 2 | 2 | 0 | B requires client reporting it has not established. N/I provide explicit scoped operator evidence for opaque providers, without claiming discovery. C excludes opaque external satisfaction and forces provisioning into its one lane. Environments §7.8; manager §6. |
| E5 Portability | 2 | 2 | 2 | 1 | B/N/I preserve a client-neutral manifest; machine-local decisions remain local. C makes complete fulfillment depend on the optional environments capability, although managers may conform without it (environments preamble). |
| E6 Honest failure | 1 | 2 | 2 | 2 | B leaves unknown/any and effective-launch visibility open and its explicit binding has no authority/freshness contract. N/I keep negative and unknown states, quantify actual selected targets, and require consent before every provisioning or binding write. C can truthfully refuse unsupported external cases. Manager §6; environments §§7.8, 10.2; csk proposal §§2, 4. |
| E7 Specifiability | 0 | 2 | 2 | 2 | B has no closed identity/binding grammar, range-lock ownership or version path. N's finite evidence states and context-qualified matching admit concrete vectors; I is specifiable only with additional versioned contracts. C is already specified. COMPATIBILITY.md:17–24; GOVERNANCE.md:7–19,75–80. |
| E8 Operator effort | 1 | 1 | 1 | 0 | Existing configured cases need zero actions; first-use provisioning, env admission and client auth can require several. No prevalence data establish a common-case 0/1-action claim. C requires manual repackaging/wiring for external providers. csk proposal §§2,5; environments §§2.2,10.3. |
| **Total, amended** | **7** | **12** | **12** | **11** | N/I tie on the deliberately coarse rubric; N has fewer concrete new contracts. |

Under **original E3**, all candidates that inspect native configurations score
**0**, including N/I/C when retaining manager §6. Original totals are B **6**,
N **10**, I **10**, C **9**, and none qualifies as elegant under the original
no-zero rule. The amended E3 makes explicit, bounded foreign-byte handling
eligible. These are design scores, not claims that today's implementation
already enforces that bound. In particular, unbounded `os.ReadFile` is not the
proposed bounded reader.

## Preferred design and smallest change set

Prefer **N**, with a tie rather than a claim of unique numerical victory.
The owner's first requirement already exists: core §4's required `hint`,
documentary `transport`, and `required_in:any|all`. Adding package identity to
the portable skill is unnecessary to let an operator fulfill that dependency.

1. Remove `server.package` and `server.endpoint` from the minimum skill change.
   Keep the existing manifest bytes and the documentary transport semantics.
2. Replace separate aliases plus identity fallback with one protected,
   context-scoped provider binding/evidence mechanism. A project file may
   propose a binding, never authorize it. Report assertion as assertion.
3. Keep acquisition, allowlist, signer policy, consent and runtime auth in
   their existing distinct lanes. A package pin is not runtime identity.
4. Define foreign-byte bounds and sanitized outputs. The manager neither
   reads dedicated credential stores nor evaluates secret references; the
   native client performs auth and the launcher may pass authorized values.
5. Evaluate any stronger availability claim in the selected launch context.
   Keep the old manager §6 check identified as static presence. Native files
   excluded by Claude strict MCP cannot satisfy a managed-launch claim.
6. Govern the new binding/configuration and evidence semantics through a CIP,
   decision, new affected schema versions and positive/negative vectors. Do
   not edit the shared `mcpRequirement` definition in place: v5–v8 depend on it.
   Leave declaration auth classes out unless their own use case needs them.

## Adversarial vectors derived independently

| Input/counterexample | Required conclusion |
|---|---|
| v5 manifest receives `server` | Old closed schema rejects; an optional field cannot be retrofitted into old bytes. |
| Two packages have identical command/args and different `env_names`, selectors or origin | Recipe equality does not establish package provenance or runtime executable identity. |
| Native Claude `.mcp.json` contains `figma`, managed channel contains another set | Static native presence may pass the legacy check; managed availability must not pass. |
| Targets are Claude and an unsupported/opaque client, `required_in:all` | Do not drop the latter from the denominator. Without accepted scoped evidence, result is unsatisfied/unknown. |
| `any` sees one positively configured target and one opaque target | Overall any can succeed because of the positive target; the opaque target remains unknown. |
| Repository proposes a binding that already has the required name | No authority follows from spelling or a project-local approval file. |
| HTTP endpoint stays equal while a native entry becomes disabled | Identity equality does not defeat disabled state. |
| `auth:none` HTTP publication | Base consent rule still requires consent; csk owner decision D1 is a different extension rule, not a spec-wide exemption. |
| Same endpoint is exposed by a connector and a local package | Alternative fulfillment needs no claim that the connector came from the package. |

## Contract homes and implementation map

- Core §4 and `schemas/v1/common.schema.json`: **no change for N**. An I
  extension needs a new manifest node/version; draft v9 is not assumed free.
- Manager §§1,6 and the next available manager/system configuration schema:
  binding authority, scope, evidence vocabulary and pure verification rules.
  Existing marker `FoundIn` must not silently relabel operator assertion as a
  server observed on disk.
- Environments §§2.2,5.8,7.8,10.2–10.3,12: reuse package and launch channels;
  document how managed evidence joins the checker, not native in-place writes
  into a managed home. Auth metadata, if added, belongs to a separately
  governed declaration revision, not schema-1 package bytes.
- `internal/mcp/mcp.go`: current native name union, read states and result
  provenance are the checker seam, not a place for installing or logging in.
- `internal/envprofile/managed.go:205–226,2436–2457` and
  `internal/contextmaterialize/mcp.go`: already expose resolved declarations,
  channel set and env names; consume their provenance rather than rediscover
  generated files as if they were unrelated native sources.

## Round record

- Independent round 1: the scores above were frozen locally before opening
  first-five verdicts. No peer-confirmed finding file has been authored yet.
