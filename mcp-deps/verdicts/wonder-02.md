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

Status: **Round 5 — updated as the debate moves.** Live table: room topic `scores`
(`$mTl0E_Eso4-XNeWtQR8osepFdQ7_K2nPIEFeKZsH2u4`; Round-2 table
`$vs1Dh-X9Qz7UpTacOzyxz-sSO-IbX9iqztugvcRd18c`; Round-3 arithmetic correction
`$biOtkvfKBYfAg78ALG0Qkbz0DpsF-rAKHaxk3E4VC1E`; Round-4 canonical-scope ruling
`$lNHT93BO3iTyCsO7GbLTGNzPtl99qTEU3D3lpTXGlHA`). The Round-1 version of this file was landed
by the convener at `0cd68b9`; this version is written in the clone and ready for the
convener's next landing (this sandbox cannot signed-commit/push; SSH fails with "No user
exists for uid 502", and unsigned commits are prohibited). **Correction on the record:** the
Round-2 table printed N+A as 14/16; its digits sum to 13 (caught by wonder-01). No cell
changed intent — the total alone was wrong, here and in the Round-2 rounds marker.

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
`$0UDTCuNu5d7WXGg4RlDrUvZNvVb8lhL1b1VJ-6wUOtA` (consolidated finding file:
`findings/f-package-is-not-service.md`, astra-01, per `$xAUlhuqfMP5tvUDDL_WNZ8V_7prYFeFtk7j16YVzqh8`).

Additional verified evidence folded in during Round 2: shipped parser rejects unknown
requirement keys (`internal/skillspec/parse.go` `rejectUnknown` on
{hint, transport, required_in}); install gate reads exactly two roots, never a managed home
(`internal/install/install.go` `mcpVerifier` comment + body); §5.8 serializers emit URL/type
only, so no HTTP header env binding exists in current machinery (astra-02,
`$V8qAIOXAUtmT49-cACD7FccLjSLAFXqmwSfSoWAab8c`); COMPATIBILITY partial-client baseline lets
cocoaskills stay on rc.10 core (lines 304–306), making new-schema manifests uninstallable
there while inert extra files degrade gracefully.

## Rubric scores (Round 5)

Mechanical tests per row are stated in room topic `scores`. E3 was expressly disposed of by
the convener in MISSION-MCP.md at `534e384` (re-read from disk in this clone after the
convener's sync; text matches the in-room quote at
`$FnzEHL5onBPh1J0YMZAUCkfxrSEpNS2yZ-u7A8rogA` / `$ropOGjw3dqPFz1fjx0hkU8dYrqD4iOS6X3jfs7L5y9o`):
2 = never uses, stores, forwards, logs or tests a credential value, with unavoidable
foreign-byte handling explicit, bounded and metadata-only; an unstated bound caps the score
at 1; the proof cites the amended row and reports the original alongside. Under the
**original** wording ("touches values" = 0), every native-inspecting design scores
E3-original 0 — this seat's Round-1 score of 1 is withdrawn in favour of the
astra-01/02/03 reading. Bounded handling also means raw foreign argv/URL are never
persisted, logged or surfaced (they can carry credentials); diagnostics stay metadata-only.

E8 is dual-reported like E3: the table's E8 uses the stated test (common case = a suitable
provider already configured). Cold first-setup is reported in the notes, never averaged:
every provisioning design scores E8-cold 1 (selection/consent + client-side auth), status
quo 0. Cold totals: N 12, A 13, N+A 12. A proof must name its E8 reading.

G0 (proof precondition, not a rubric row): the design must let a skill dependency actually
reach a configured state (the operator's goal), not merely be checked.

| Design | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | Total | G0 | E3-orig |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Status quo (manager §6) | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 0 | **11/16** | fail | 0 |
| BASE as written | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **8/16** | partial | 0 |
| BASE corrected, identity kept (astra-01/03 row) | 0 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | **10/16** | pass | 0 |
| BASE guidance-only (astra-01 row) | — | — | — | — | — | — | — | — | **12/16** | pass | 0 |
| N — `alt-names-local-evidence` (astra-01) | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | **13/16** | pass | 0 |
| A-standalone — `alt-skill-ships-declaration` (wonder-01) | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | **13/16** | pass | 0 |
| **N+A composite (preferred on goal fit)** | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | **13/16** | pass | 0 |
| B — `alt-capability-tools` (wonder-01) | 1 | 1 | 2 | 1 | 1 | 1 | 0 | 1 | **8/16** | partial | 0* |
| C — `alt-gateway-proxy` (wonder-01) | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 2 | **5/16** | pass | 0 |

\* B's strong form needs no native inspection, so a metadata-only variant could reach
E3-original 2 at the price of its E6/E7 cells; not scored as submitted. Status-quo E3 is 1
(not 2) because today's checker states no bounded-handling bound (convener cap); Round 1
said 2, total corrected 12→11. This seat's Round-1 "BASE′ repaired (13/16 forecast)" is
retired as dominated by N+A (same guidance at zero schema cost). N, A-standalone and N+A
**tie at 13/16** from this seat; the preference below is a goal-fit tie-break, not a points
win. E4 mechanical rule (Round 4, gating reading): 2 iff all five provider sources can
satisfy with no client change (opaque via labeled assertion); 1 iff every file-observable
source can satisfy and opaque fails honestly (status-quo parity); 0 iff a source satisfying
today is excluded or a client must change. The mission defines only the 2/0 anchors, so "1"
is a declared interpolation; under astra-01's strict reading (opaque exclusion ⇒ 0) totals
become status quo 10, BASE 7, A-standalone 12, B 7, C 4, N/N+A unchanged at 13 — ranking of
goal-meeting designs is invariant and every per-row spread stays ≤1. Second-host scorers
must state their E4/E8 conventions, as with E3.

Per-cell justification, BASE as written:

- **E1=1** — one member name on the manifest, but a 2-variant union plus unhomed auth class
  plus unhomed binding store (C4/C12/C14). Not 0 only because each piece *could* home in an
  existing object; if bindings need protected state (they do, C11), E1→0 risk stands.
- **E2=1** — reuses the requirement shell, declaration-package kind, allowlist/audit names;
  but needs new skill-range resolution without a lock (C5), per-client identity+enabled
  decoders (C3/C7), launch-scoped evidence (C9), and a skill→profile provisioning path that
  does not exist (C10). §5.8/§6 used outside their specified scope is not reuse.
- **E3=1** — no auth execution, no health checks, names-only declarations (C12); but the
  new identity matcher states no bounded-handling bound (convener cap). Earning 2 needs the
  bound spelled out, including: raw foreign argv/URL never persisted, logged or surfaced —
  field-name whitelisting alone does not make them safe to echo.
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
Its 11/16 with G0=fail is the calibration proof that the rubric alone cannot crown a winner:
elegance must be judged among designs that meet the goal.

Alternative cell notes (this seat; room events `$3d9O9Uc62m7vnEKzYzImIYeAgm3L7FicZAfQzpjcoHU`,
`$-61mWLy5FbJ529QmYJc1-_T5XMH9qzFy9E2yIV0M_3c`, `$c21CsS25eMJM5jIw4mAD3ftGeFb306ZCe5u8h5G1ECQ`,
`$4jeyuHCKp9bzs8shoky21WlBwTQSYATy33N6lwY1QOM`):

- **N (13/16)** — row identical to astra-01's; astra-03 differs only on E2. E1=1 contingent
  on the binding homing in an existing protected object (manager-config v4 or existing
  manager-home state); a new standalone format makes E1=0. E3=2 requires the bounded-handling
  bound spelled verbatim in the spec delta. E4=2 over the five provider sources on
  MCP-capable clients, opaque via labeled assertion (weakness charged to E6, which N
  satisfies); pi/windsurf bounds are client-capability limits outside every design.
  Unanswered-in-N: name-meaning/squatting sentence, closed invalidation-observable set,
  assertion batching (E8 fan-out), first-setup hand-wiring (needs A).
- **A-standalone (13/16)** — author's explicit Round-3 scope: ship + metadata-only candidate
  notice + operator-selected provisioning; checking = today's §6 legacy presence, unchanged
  (this seat's earlier launch-aware A row is superseded). Verified: core §3 mandates only
  `SKILL.md` at root; §3.1 eligibility governs agent-facing context (`agent-skill.json` is
  itself outside it); §2.2 package = snapshot/directory whose root contains `agent-mcp.json`.
  Two-stage surfacing: pre-admission display metadata-only (name, transport, verdict class,
  route); full §2.3 rows only after strict MCP admission; shipped args/url inside the
  secret-material detector scope as an admission gate; malformed ⇒ metadata-only MUST-warn,
  never fail/silence; credential material never warn-only ⇒ E3=2. E2=2 honestly under this
  scope (no borrowed checker); the price is E6=1 (inherited §6 debts: non-uniform disabled
  decoding, launch-unscoped unions, labelled legacy) and E4=1 (opaque = unknown-fails).
  Equals wonder-01's row exactly; astra-01's bounded-A (10) is within 1 on every row.
  Source kind stays git-only for profile adoption (§2.2); path/local snapshots display-only;
  remediation names the resolved revision and the context-package route (no naked-declaration
  install). Evidence label is "manager-recorded origin", never provenance (§1.3 lock
  discipline, verified lines 205–206), and recorded origin is orthogonal metadata — never
  satisfaction evidence.
- **B (8/16)** — within 1 of author's self-scoring on every row. E7=0 (no closed tool
  namespace; no client inventory surface in local evidence) kills it as a deliverable today.
  Framing retained: requirement key = author-chosen capability label. Record as
  deferred-pending-client-inventory with its stated re-score trigger.
- **C (5/16)** — identical to author's row. E3=0/E6=0 under both readings (gateway uses and
  forwards values, terminates auth; single entry masks backend state and destroys
  per-server disable semantics; pi has no channel). CIP-0011 verified: broker/dispatcher
  are separate modules, Curator a client. Record as **rejected-with-reason**.

## Preferred design and smallest changes to the base

Preferred: **N+A composite — named requirements with launch-scoped local evidence and
protected operator bindings (N), plus inert skill-shipped declaration recommendations
surfaced at install and provisioned only through existing operator-selected lanes (A)**,
as sketched in wonder-01's D1–D6 (`$6Ju0U6dvorEvdtJ0MsUkDEFhhMjnZPdD4btQilsiQhQ`, attacked at
`$aRepY_z1bvqhi9Op5HsFbfkmeGMJTnslha6tXpVAz9M`, revised at
`$e5s3ZnvCckXlXR8HgOhJu7XHsOUk3W_5O2ueV0Ga37I`). N, A-standalone and N+A tie at 13/16 from this
seat — a frontier between minimality (A) and zoo completeness (N+A); the tie-break is goal
fit: the operator's goal explicitly centres zoo coexistence, and only the composite covers
opaque zoo members (E4=2 via labeled assertion, E6=2 launch-true status) *and* first-setup
(A's informed one-selection path). A alone is the shippable first subset of the composite and
the minimal fallback if the binding record is rejected. This keeps the base's Require/Provide/Bind separation — the part that survived
every attack — while deleting its normative identity machinery. Author-supplied package
identity is *not* required by the operator's goal: skill dependencies pin because the
manager installs them; MCP requirements are checked, not installed, and provisioning
authority is the operator's in every surviving design. Identity is discovery UX, carried
inertly by A.

Smallest change set from BASE to N+A:

1. **Delete `server` from the skill wire entirely** (vs. base §1): no manifest schema lane,
   no ranges on lockless surfaces, no endpoint grammar, no auth class. Schemas 5–9 keep
   their bytes; old and partial (rc.10-baseline) managers keep installing the same skills.
2. **Ship-inert MAY clause, two-stage surfacing** (A, sketch D1-revised): skill root MAY
   contain `agent-mcp.json` (existing §2.2 schema-1 grammar); not agent-facing context. At
   skill install, on exact `name` == requirement-key match with an unsatisfied requirement,
   show a metadata-only candidate notice (name, transport, detector verdict class, route —
   never raw argv/url); full §2.3 rows only after strict MCP admission. The file's args/url
   enter the secret-material detector scope as an admission gate (lane's normal blocking
   policy; credential material never warn-only); malformed ⇒ metadata-only MUST-warn, never
   fail/silence. Remediation names the exactly resolved revision and the real route (add as
   `requires.mcp` to an operator-selected context package — §9.1 consumes context roots; no
   naked-declaration install, no new command); adoption re-runs allowlist/signers/strict
   audit on the declaration source (skill admission proves nothing); git-only for the
   profile lane (§2.2), path/local snapshots display-only there; csk native lane only under
   exact-plan consent (H4 respected). Transitive skills get surfacing, never authority.
3. **Launch-scoped evidence** (`f-launch-universe`): §6 name semantics evaluated per
   (agent, scope, native-vs-managed launch); managed checks consume the resolved
   marker-validated channel set with §7.8 residuals; per-client disabled semantics specified
   (closing C3); same-name shadowing never hidden by union.
4. **One protected binding/assertion record** (N; `f-opaque-provider`, `f-consent-binding`;
   sketch D3/D4-revised): homed in a governed successor of the existing machine-configuration
   family (a new standalone record family would make E1=0 — storage ownership does not
   dissolve a format). Members: enumerated exact requirement identities (skill package
   identity + requirement name, batched in one operator action, no name wildcard), consumer
   scope, target agent, selected launch descriptor, provider selector (configured name +
   surface/handle class), evidence observed|asserted. Changed enumerated membership,
   requirement identity, scope, target or launch descriptor = non-matching context (no silent
   carry-forward); invalidation observables closed (revocation; bound provider observed
   disabled/absent in a surface authoritative and complete for that launch; launch-kind
   exclusion — absence from the six native files alone never invalidates). Evidence recorded
   per (requirement, target, launch) in a marker successor; old markers read as legacy native
   presence only and discharge no managed claim. Recorded origin is orthogonal metadata in
   lock/ledger evidence, never satisfaction proof, and never outranks current negative
   evidence. Project data may request, never authorize. Consent displays include the
   requiring-skill list as *attribution*; renewal triggers are only the closed widening set
   (declaration digest, agents, destination/scope, argv-or-endpoint, env names) —
   consumer-set changes alone do not renew consent, because per-skill use-authorization is
   unenforceable and asserting it would violate E6 (astra-02's distinction; conceded by
   wonder-01, sketch D6-corrected). §2.3 gains `url` visibility (S1, sketch D5) so
   credential-routing consent is informed; csk D1 remains a separate explicitly scoped
   contract.
5. **Secret bound stated verbatim** (`f-secret-boundary`, amended E3): no value use, storage,
   forwarding, logging or testing; foreign-byte handling bounded and metadata-only (raw
   native argv/URL never echoed); no health checks; status vocabulary
   configured / mismatch-reported / unknown / asserted + "auth not checked".
6. **Name-meaning sentence**: the requirement key is an author-chosen capability label fixed
   by the skill's own documentation; binding prompts enumerate every requiring skill + hint;
   the manager never adjudicates same-name meaning.

Remaining honest costs of N+A: E1=1 (binding record + marker evolution), E2=1
(evidence-aware checking is new checker machinery), E7=1 until the binding grammar,
invalidation set and vectors are actually written. No design scored reaches 15–16 without
hiding one of these.

## Proof status

"Elegant" = highest total with no 0 in E3 (amended) or E6; "proved" = two independent seats
on different hosts agreeing within one point on every row, with evidence. Current state:

- BASE as written is **refuted as already-elegant** (8/16; claims C4–C14 each confirmed by
  ≥2 ivmbp seats; findings landing on `main` by astra-01/02/03).
- On ivmbp, N/N+A rows from astra-01, astra-02, astra-03, wonder-01 and this seat agree
  within 1 on every row (residual spread: dual-reported E8 reading only; common digits
  [1,1,2,2,2,2,1,2]=13); A-canonical equals wonder-01's row exactly and is within 1 per row
  of astra-01's bounded-A; B and C rows match their author's self-scoring within 1 (C
  exactly). Wonder-01's D1–D6 sketch was attacked and revised (enumerated identities,
  provider selector, per-target evidence, legacy-marker limits, config-successor homing,
  D6 concession): composite E7 stays 1 unanimously on ivmbp.
- Open proof obligations: (a) second-host independent scoring (wonder-12, astra-11..13) of
  N, A-standalone and N+A — still the blocking item (mini seats not yet up per convener
  `$h4JEJERFqsHn2uo4CleuMAw2Ylh0NKOdpxvvss87CLA`; cross-host asks parked until `macmini_*`
  identities post); (b) E7 pin-downs — closed at sketch level in Round 5
  (`$R2qT1zuemaAB6XGZYwcsy_Fh-ncIeE1HMRY5f8q64M4`: completeness sharpening, hardened floor,
  provider selector as matching identity with no durable drift detection claimed for opaque),
  remaining as governed text (CIP + decision record): per-launch authoritative-completeness
  table (managed ≠ universally complete — only an actually applied strict Claude channel
  over a non-empty set excludes authoritatively; OpenCode overrides and Codex trusted-project
  residual persist; §5.8 empty set writes no channel, so vectors use a present strict
  channel), the governed choice whether system files may forbid the asserted class under
  hardened (floor holds either way: assertion never replaces admission or suppresses a
  hardened refusal);
  (c) E6 truth-table conformance vectors (match/mismatch/unknown/malformed/disabled/shadowed
  × any/all × native/managed); (d) under the *original* E3 wording no native-inspecting
  design passes the no-zero gate (all E3-original 0) — the proof therefore stands on the
  convener's amended row, recorded here without substitution; (e) E8 reading (common-case
  vs cold) named in any final proof, since cold totals reorder A above N/N+A.
