# Verdict — wonder-02 (rubric and proof)

Seat: `wonder-02` (Muse Wonder, ivmbp). Lens: own the elegance rubric, score the base and every
alternative, verify every claim of the base against the spec text mechanically.

Sources checked read-only: curator-spec `a9c03be` (core §4/§5, manager §§1/6/7.1,
environments preamble/§§1.3–1.4/2/2.1–2.3/5.8/6/7.8/9.1/10.3/12.1, `common.schema.json`,
`agent-mcp-v1.schema.json`, skill schemas v5–v9-draft, COMPATIBILITY.md, GOVERNANCE.md,
CIP-0006), curator `5234cf3` (`internal/mcp/mcp.go`, `internal/contextmaterialize/mcp.go`,
`internal/envprofile/surfacing.go`, `internal/skillspec/types.go`), `BASE-DESIGN.md` and all
three `inputs/` at `1c6010a`. `git pull` from this sandbox fails (uid/SSH; source clones are
read-only), so all citations are to the local pins above.

Status: **Round 1 draft — updated as the debate moves.** Live table: room topic `scores`
(`$mTl0E_Eso4-XNeWtQR8osepFdQ7_K2nPIEFeKZsH2u4`).

## Mechanical claim-check of BASE-DESIGN

| # | Base claim | Verdict | Evidence |
|---|---|---|---|
| C1 | Zoo surfaces = `.mcp.json`, `~/.claude.json`, `.codex/config.toml`, `.cursor/mcp.json`, `opencode.json`, `~/.gemini/settings.json` | TRUE | manager §6 table (lines 1090–1097) — plus windsurf user-only surface the base omits |
| C2 | Existing requirement: `dependencies.mcp_servers` `{hint, transport?: stdio\|http, required_in?: any\|all}` (v5+) | TRUE | core §4.4 (1175–1177); `common.schema.json` `mcpRequirement` (610–618), shared by ref in agent-skill/csk-skill v5–v8 and draft v9 |
| C3 | Manager §6 verifies read-only: presence by name, disabled excluded, missing command warns, project-only warns | TRUE in spec; PARTIAL in code | manager §6 (1087–1109). Code: `internal/mcp` filters disabled only for OpenCode `enabled:false` (mcp.go:260–264) and Claude project `disabledMcpjsonServers` (222–226); Codex/JSON branches have no enabled filter. Spec/implementation gap predates the base |
| C4 | Extension = **one optional field** `server` | REFUTED as a total count | `mcpRequirement` is closed (`additionalProperties:false`); schemas 2–8 reject unknown fields and draft 9 "adds only the `directory` member" (core §4, 193–198). Full base also needs an auth class (no home: `agent-mcp-v1` closed, no `auth`) and an alias/binding store (manager §1 rejects unknown config fields). Total ≥3 wire members across ≥2 series + governance (COMPATIBILITY 17–24; GOVERNANCE decision record). See `f-schema-budget` |
| C5 | `server.package = {git, range}` identifies an `agent-mcp.json` package | UNSUPPORTED as identity | Ranges exist only where a lock pins them (env §1.3 "The lock is the identity"; §1.4 line 349); skill dependencies forbid branch/range (core §4.4, 1168–1169). A standalone skill has no lock owner. See `f-package-is-not-service` |
| C6 | `server.endpoint` = "HTTPS origin plus path" identity | UNDER-SPECIFIED | §2.2 URL rule is `https` + ASCII host + no userinfo/query/fragment (506–507) with a schema regex; the base states no grammar or canonicalization (port, trailing slash, case, encoding). Reusing §2.2 verbatim closes this at zero concept cost |
| C7 | Satisfaction: name (or bound name) + identity match "same declaration digest or command/args … same origin+path, or explicit operator binding" | REFUTED as stated | No declaration digest exists for native entries; §5.8 emits provenance-free entries; argv equality is recipe equivalence, not provenance (§2.2 bare command/PATH; "a binary allowlist bounds nothing"); http packages have no argv. Identity also tightens §6 presence-success and core §4 documentary `transport` (cf. curator-review H3). See `f-package-identity` |
| C8 | "Where the server came from does not matter" — incl. "a cloud connector the client reports" | FALSE for opaque providers | §6/`internal/mcp` read six file surfaces only (mcp.go:23–44); no client-report surface exists. Operator binding discharges only the identity conjunct, not configured+enabled presence. See `f-opaque-provider`. Also: `pi` has no MCP channel (§7.8) and windsurf no project surface (§6), so `required_in: all` including them is unsatisfiable by construction |
| C9 | Name-union satisfaction ("some configured, enabled server") | FALSE across launch kinds | Managed channel files are disjoint from §6 paths (§5.8; `contextmaterialize/mcp.go:32–34`); Claude `--strict-mcp-config` excludes native config, OpenCode project entries override managed ones (§7.8); `ConfiguredServers` unions project+home, home winning (mcp.go:54–63), hiding shadowing. See `f-launch-universe` |
| C10 | Optional provisioning "through the existing §5.8 channel" | WRONG CHANNEL | §5.8 materializes a *profile's* locked MCP set into managed homes only, "never … into a native in-place home"; native write management is outside environments rev. 1 (preamble, lines 14–16). A skill requirement is not a profile member; no skill→profile-lock path exists. Native provisioning is the separately reviewed csk feature (414-line proposal), not reuse |
| C11 | Provisioning only with explicit consent, under allowlist/audit/signer policy; endpoints never auto-provisioned | DIRECTION TRUE, CONTRACT MISSING | §2.3 surfacing is informative-only and has no `url` column (cannot show an http destination); §2.2 allowlist admits sources, not exact actions; §10.3 passes an env-name *union* (no per-server confinement); project-homed bindings are repository-authored authority. csk D1 (http/no-env without consent) contradicts "consent before any write" if merged into one contract. See `f-consent-binding` |
| C12 | Auth entirely the client's: declarations carry auth class + env **names**; manager never reads/stores/forwards/tests values; no health checks; status "configured / auth not checked" | TRUE as intent; LITERALLY FALSE on "reads" | §2.2 "Values never appear in any package, lock, marker, fragment, or materialized file" (523); §5.8 no value enters materialized files (1128). But native inspection reads whole mixed files that may contain credential literals (`os.ReadFile`+unmarshal; csk §§4–5). Dual E3 scoring required. See `f-secret-boundary` |
| C13 | "Curator and csk share one declaration format and one requirement semantics" | CONDITIONAL | Holds only while headers/auth stay out of `agent-mcp.json`; csk needs both (D1 header env refs) and curator-review H2 forbids minting declaration schema 2 outside the spec. The base's own auth class breaks the sharing unless governed upstream |
| C14 | Aliases: machine *or project* config maps required→configured name | UNSAFE as written | Project-homed authority lets a hostile repository self-bind (`figma → attacker`). Bindings that waive identity must be protected machine state (csk §2/A6 pattern); project data may request, never authorize |

Peer confirmations by this seat (room events): `f-secret-boundary`
`$SNRLfvcWtHxonUgOrpTBaUZnHD9ClzN9jCkBSf7RasI`; `f-schema-budget`
`$7Z-nfZiiYD5utaTqGhedsfHfc3rYfTgw7ySHzSeuM7U`; `f-launch-universe`
`$wo5YNm48iTnPqXqJqcxbFC_00nZSLnCcFlkpgTMZ138`; `f-opaque-provider`
`$0UgvTzavFWc7rqs4v1V-ynXdb3IBMMQaSoK3X_2XhXs`; `f-consent-binding`
`$5P_OppjPueGB-VRS6PvETkZn8oov-7j-rSGQEeVeeOk`; `f-package-identity`
`$0UDTCuNu5d7WXGg4RlDrUvZNvVb8lhL1b1VJ-6wUOtA`.

## Rubric scores (Round 1)

Mechanical tests per row are stated in room topic `scores`. E3 below is the operational
reading (no semantic access to values); literal E3 (zero credential-byte contact) is 1 for
every native-inspecting design including the status quo, and 2 only for designs restricted to
guaranteed secret-free records. The "elegant" gate (no 0 in E3/E6) needs a convener ruling on
which E3 gates; this seat proposes E3-op gates, E3-lit is reported as a standing limitation.

G0 (proof precondition, not a rubric row): the design must let a skill dependency actually
reach a configured state (the operator's goal), not merely be checked.

| Design | E1 | E2 | E3-op | E4 | E5 | E6 | E7 | E8 | Total | G0 |
|---|---|---|---|---|---|---|---|---|---|---|
| BASE as written | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **8/16** | partial |
| Status quo (manager §6) | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 0 | **12/16** | fail |
| BASE′ repaired (forecast) | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | **13/16** | pass |

Per-cell justification, BASE as written:

- **E1=1** — one member name on the manifest, but a 2-variant union plus unhomed auth class
  plus unhomed binding store (C4/C12/C14). Not 0 only because each piece *could* home in an
  existing object; if bindings need protected state (they do, C11), E1→0 risk stands.
- **E2=1** — reuses the requirement shell, declaration-package kind, allowlist/audit names;
  but needs new skill-range resolution without a lock (C5), per-client identity+enabled
  decoders (C3/C7), launch-scoped evidence (C9), and a skill→profile provisioning path that
  does not exist (C10). §5.8/§6 used outside their specified scope is not reuse.
- **E3-op=1** — no auth execution, no health checks, names-only declarations (C12); but the
  new identity matcher has no stated non-secret projection rule. One specified sentence
  (compare only name/transport/command/args/url/env-names; never retain/diff/log other
  fields) earns 2.
- **E4=1** — name-only requirements: whole zoo passes. `server`-carrying requirements:
  opaque plugins/connectors cannot satisfy the presence conjunct (C8); managed-launch
  satisfaction is mis-scoped (C9); `pi`/windsurf-project make some `all` unsatisfiable.
- **E5=1** — endpoint form is portable once §2.2 grammar is adopted; `{git,range}` meaning
  depends on a resolver+lock the skill surface lacks, and argv identity depends on the
  launch machine's PATH (C5/C7). New-schema gating vs older managers is a further tax.
- **E6=1** — consent-before-write and "auth not checked" stated; but unknown/opaque
  semantics left open (one bad resolution = E6 0), shadowing hidden by union (C9),
  project-homed bindings unsafe (C14), csk-D1 merge contradiction (C11).
- **E7=1** — governance path exists and is clear (CIP → decision record → schemas/vectors);
  grammar is not closed (endpoint canonicalization, digest definition, auth/binding/schema
  homes all unnamed; C4/C6/C7).
- **E8=1** — already-configured common case is 0 actions when name+identity happen to match,
  ≥1 (alias/assertion) otherwise; new-server case is consent + client-side auth ≥2 operator
  actions. Better than hand-wiring everything (status quo E8=0), short of the ≤1 bar.

Status-quo notes: E4=1/E6=1 reflect pre-existing debt (C3 disabled-decoder gaps, opaque
providers, launch-universe blindness); E8=0 because every server is hand-wired from a hint.
Its 12/16 with G0=fail is the calibration proof that the rubric alone cannot crown a winner:
elegance must be judged among designs that meet the goal.

## Preferred design and smallest changes to the base

Preferred: **BASE′ — keep Require / Provide / Bind, demote identity from normative to
reported, and route provisioning through lanes that already exist.** No alternative design
has been posted yet (`alt-*` topics: none at Round 1); this preference is explicitly
revisable when wonder-01/wonder-11 alternatives land, and each will be scored in this table.

Smallest delta set from BASE to BASE′ (each maps to a confirmed `f-*` thread):

1. **Governed schema lane** (`f-schema-budget`): preserve v5–v8 bytes; add `server` only via
   a deliberate draft-9 amendment or a new schema version, with decision record, both-version
   vectors, and marker decision. No "v5+ optional extension".
2. **`server` = non-authoritative acquisition hint** (`f-package-identity`,
   `f-package-is-not-service`): endpoint in the closed §2.2 grammar; package as exact-ref
   forms only on the skill surface (ranges only when pinned by a profile lock). Satisfaction
   stays manager-§6 presence; identity is *reported* per launch as
   observed-match / observed-mismatch / unknown / asserted — never silently flipping a
   presence success (any future tightening is its own versioned contract, cf. H3).
3. **Launch-scoped evidence** (`f-launch-universe`): evaluate against
   (agent, scope, native-vs-managed descriptor); managed checks consume the resolved,
   marker-validated channel set with recorded residuals; specify per-client disabled
   semantics (closing the C3 code gap) and never hide same-name shadowing behind a union.
4. **Opaque = asserted, never satisfied-silently** (`f-opaque-provider`): protected,
   scoped operator assertion as the only escape hatch, labeled in status/markers forever;
   no duplicate provisioning to compensate for invisibility.
5. **Bindings/consent as protected exact-plan machine state** (`f-consent-binding`):
   outside any checkout; bound to resolved declaration, consumer, agents, destination,
   argv/endpoint, env names; revalidated before write; §2.3 gains `url` visibility (S1) so
   credential-routing consent is informed; csk D1 stays a separate, explicitly scoped
   contract. Drop the auth-class wire field (hint + `env_names` + client UX already carry
   the guidance; a governed `agent-mcp` v2 can add it later if evidence demands).
6. **Provisioning lanes stay separate** (C10): managed homes only via an explicitly
   operator-selected profile (§5.8 unchanged); native homes only via the separately reviewed
   native-writer feature (csk design, incl. H4: never write into marker-owned managed homes
   or `curator-mcp.config.toml`). A skill requirement alone never provisions anything
   transitively; the hint only makes the operator's one consent action informed.
7. **Secret discipline for the matcher** (`f-secret-boundary`): non-secret projection rule
   as in E3 above; no health checks; status vocabulary fixed to
   configured / mismatched / unknown / asserted + "auth not checked".

Forecast for BASE′ is 13/16 with E4 deliberately capped at 1 (assertion-grade zoo coverage
is not configuration-grade) and E1 at 1 (hint member + binding knob/state exceeds the
one-field bar). If the collective wants E1=2, the only honest route found so far is dropping
`server` from the skill wire entirely (context-package-only declarations) — an alternative
this seat will score on arrival, trading E8/G0 for E1.

## Proof status

"Elegant" requires highest total with no 0 in E3/E6; "proved" requires two independent seats
on different hosts agreeing within one point on every row, with evidence. Current state:
BASE as written is **refuted as already-elegant** (8/16 here; every load-bearing claim above
independently confirmed by ≥2 ivmbp seats; mini adversarial seats pending). BASE′ is a
forecast, not a proof. Open proof obligations: (a) wonder-12 independent scoring from mini;
(b) convener ruling on the E3 gating reading; (c) at least one genuinely different
alternative scored head-to-head; (d) conformance-vector sketches for the E6 truth table
(match/mismatch/unknown/malformed/disabled/shadowed × any/all × native/managed).
