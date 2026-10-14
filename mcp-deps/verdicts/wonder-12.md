# wonder-12 verdict (Mac mini, third pass): adversarial elegance rubric and proof

Seat: `wonder-12` (`macmini_swarma-mcp-deps_wonder-12`). Lens: independent
adversarial pass on `wonder-02` (rubric and proof). This file's **initial
scores were formed and saved before reading any other seat's verdict file**,
any findings file, or the body of any `alt-*`, `f-*` or `scores` room topic.
Exposure during onboarding was limited to: the `a2a topics` listing (slugs and
titles), the last `rounds` markers (which contained total fragments), and the
file names under `mcp-deps/`. Nothing below uses a peer's argument; every
score cites `BASE-DESIGN.md`, `mcp-deps/inputs/`, `curator-spec` text/schemas,
or `curator` code, all read directly.

Artifact name follows the convener's newer canonical directive relayed in
`rounds` (`verdicts/<seat>.md`), superseding the launch prompt's
`macmini-` prefix. No other seat's file was overwritten.

Source pins read: `curator-spec` `a9c03be`, `curator` `5234cf3`,
`swarma-architecture-review` `b5e7dab`.

## Verdict in one paragraph

The base design **as written is not yet elegant**: it scores 8/16 (amended E3)
and 7/16 (original E3) under the mechanical tests below, with no row at 2,
because each row carries exactly one unstated or contradicted piece. A
corrected base (BASE′, nine small changes in §6) scores 11/16 amended, 9/16
original, and is **close to elegant**: the remaining 1s are either priced
honestly (E1, E2), specifiable in one drafting pass (E7), or in one case
provably capped for every design (E4 ≤ 1, §5). No goal-covering alternative
beats BASE′. The context-package-only design ties BASE′ at 11 on points but
does not meet the operator's goal, which exposes a missing precondition in
the rubric's definition of "elegant" (§5). **Proof status: not claimed.**
Cross-seat agreement can only be assessed after comparing with the other
fives; this file is the independent mini input to that comparison.

## 1. Mechanical tests (how each row was scored)

- **E1 count:** count every new named field, object, file format and enum
  value across *all* wire surfaces a design touches (skill manifest, Skillfile,
  declaration package, machine config, lock, install marker, manager state).
  2 = at most one new optional field in total; 0 = a new object family or
  file format.
- **E2 count:** count new *stateful subsystems* (own state, format, lifecycle).
  A stateless extension of the existing §6 checker is not a subsystem. 2 =
  zero new subsystems; 0 = a parallel materializer, resolver, broker or proxy.
- **E3 trace:** list every manager operation. Amended 2 requires both (a) no
  credential *value* is used, stored, forwarded, logged or tested, and (b) an
  explicit bound for foreign-byte handling (fields extracted, size cap, no
  raw argv/URL/env persisted/logged/surfaced). Per the mission note, no stated
  bound caps the score at 1. Original 2 additionally requires that the manager
  never *reads* a credential; a code path that deserializes a foreign file
  containing credential fields reads them. Process-environment inheritance at
  launch (names allowlisted, values never opened by the manager) is not
  reading or forwarding by the manager.
- **E4 matrix:** the five zoo rows of `BASE-DESIGN.md:16-22`, checked per
  launch universe (native vs Curator managed). 2 = every row can satisfy by
  evidence without a client change; 1 = some rows satisfy only by operator
  assertion, or only in one universe; 0 = whole rows excluded by construction.
- **E5 test:** the same skill manifest bytes, presented to another host,
  client set and conforming manager, keep their meaning; no range, path,
  host or client value is baked in.
- **E6 truth table:** unknown / malformed / disabled / shadowed / transport-
  or identity-mismatched entries; consent gate before each write class;
  status wording must not claim connected or authenticated.
- **E7 test:** could a third party write positive and negative conformance
  vectors from the design text alone, and is the schema-series owner clear
  (`COMPATIBILITY.md:17-24`, `GOVERNANCE.md` "Decision record")?
- **E8 count:** operator actions in the *new-dependency* case (the required
  server is not configured yet), applied uniformly to every design. A client
  authentication flow is an operator action. (The already-configured case is
  zero actions for every name-preserving design and does not discriminate.)

A **goal-coverage precondition** is applied before totals are compared: the
operator's goal requires that (i) skills declare the dependency, (ii) the
requirement combines with the existing zoo, (iii) authentication is handled
without the manager taking on credentials. A design failing (i) or (ii) is
reported for calibration but cannot win, whatever its total.

## 2. Designs scored

- **BASE** — `BASE-DESIGN.md` exactly as written (Require / Provide / Bind,
  `server.package {git, range}` or `server.endpoint`, auth class, aliases).
- **BASE′** — the base plus the nine corrections in §6. Scored separately so
  "the base is close" is a measured statement, not a compliment.
- **ALT-LOCAL** — skills keep name+`hint` only; identity, aliasing and
  provisioning intents live exclusively in operator machine policy
  (name → exact package or endpoint). Constructed in its strongest form,
  including a stated metadata-only parse bound.
- **ALT-CTX** — MCP dependencies declared only in context packages via the
  existing `requires.mcp` (environments §2, §2.2, §5.8, §7.8); skills carry
  no server identity. This machinery exists today.
- **ALT-SHIP** — the skill snapshot ships `agent-mcp.json` declaration(s);
  the manifest points at them; the skill snapshot identity is the pin.
- **ALT-CSK** — the inputs as frozen: operator-root Skillfile declarations
  compiled by native writers (`csk-mcp-design-proposal-v1` as amended by
  `csk-slice1-decisions`).
- **ALT-CAP** — skills require tools/capabilities instead of server names;
  satisfaction proved by probing servers.
- **ALT-GW** — a manager-side MCP gateway/proxy owns connections and auth.

## 3. Score table

E3 is shown as amended/original wherever the two differ; totals are amended
first and original in parentheses. "Elegant" per the mission also requires
no 0 in E3 or E6.

| Design | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BASE as written | 1 | 1 | 1/0 | 1 | 1 | 1 | 1 | 1 | 8 (7) |
| BASE′ (preferred) | 1 | 1 | 2/0 | 1 | 2 | 2 | 1 | 1 | 11 (9) |
| ALT-LOCAL | 1 | 1 | 2/0 | 1 | 2 | 1 | 1 | 1 | 10 (8) |
| ALT-CTX (fails goal i, ii) | 2 | 2 | 2/2 | 0 | 1 | 1 | 2 | 1 | 11 (11) |
| ALT-SHIP | 1 | 1 | 2/0 | 1 | 1 | 1 | 1 | 1 | 9 (7) |
| ALT-CSK | 0 | 0 | 1/0 | 1 | 1 | 1 | 1 | 1 | 6 (5) |
| ALT-CAP (E3 = 0) | 0 | 0 | 0/0 | 0 | 1 | 1 | 0 | 0 | 2 (2) |
| ALT-GW (E3 = 0) | 0 | 0 | 0/0 | 0 | 0 | 1 | 1 | 0 | 2 (2) |

Among goal-covering designs BASE′ > ALT-LOCAL > ALT-SHIP > BASE > ALT-CSK,
with ALT-CAP and ALT-GW disqualified on E3. The margin BASE′ over ALT-LOCAL
is exactly E6: only a skill-carried identity lets the manager distinguish
"the server the skill meant" from "any server with this name" in the
absence of local policy.

## 4. Row-by-row justification

**E1.** BASE claims "one new optional field" (`BASE-DESIGN.md:62`). The
count across surfaces is higher: `server` with two nested variants
(`package.git/range`, `endpoint`); an *auth class* (`BASE-DESIGN.md:55`)
which exists nowhere in `agent-mcp-v1.schema.json` (closed `oneOf`,
`transport/command/args/env_names/environments`, `additionalProperties:
false`) and therefore needs a declaration or requirement field of its own;
the Bind alias map and operator binding (new machine/project config object);
and marker semantics beyond "agents where found" (manager §6). That is more
than one field but not a new file format: 1. The frozen schemas forbid
smuggling the manifest field in-cost-free: `mcpRequirement` in
`common.schema.json` is closed, `dependenciesV5` is shared by manifest
schemas 5–8, the parser rejects unknown entry keys
(`curator/internal/skillspec/parse.go` `parseMcpServers`), and
`COMPATIBILITY.md:22-24` requires a new `schema_version`, schema file,
vectors for both versions, and never redefines old bytes in place.
ALT-CTX adds nothing: 2. ALT-CSK adds a Skillfile schema, a declaration
object family (`scope/agents/auth/git_policy/headers/reference`), ledger and
consent formats and a refusal-code family: 0.

**E2.** BASE/BASE′ reuse the §6 checker, §2.2 packages, the package
allowlist (§2.2), strict profile audit with the secret detector (§9.1 via
manager §7), signer verification (§1.4) and §5.8 materialization — but only
indirectly: §5.8 materializes "the lock's `mcp` members" (§5.8 first
paragraph), so a skill's package can reach §5.8 only by entering a profile
closure and lock; that glue, plus the identity matcher and a consent record
for skill-triggered provisioning (the §8 approval record covers project env
files, not MCP), are new. One new mechanism, no parallel system: 1.
ALT-CSK builds a deliberately parallel materializer (per-client span
writers, protected ledger, consent store) beside §5.8: 0. ALT-CTX: 2.

**E3.** BASE states "the manager never reads, stores or forwards values"
(`BASE-DESIGN.md:57`, cf. 64). The incumbent checker reads whole native
files and unmarshals every entry into memory (`curator/internal/mcp/mcp.go`,
`entriesInFile` and `ConfiguredServers`), including any `env`/header
literals; identity matching additionally requires extracting argv/URL from
foreign entries. The claim is therefore false under the **original** row for
every design that checks native entries (score 0; ALT-CTX, which checks a
lock and declarations that must carry no values, keeps 2/2). Under the
**amended** row this parsing is admissible only with a stated bound; BASE
states a stronger contrary claim and no bound, so the mission cap applies:
1. BASE′ and the strongly-constructed ALT-LOCAL/ALT-SHIP state the bound
(extract only name/enabled/transport/command/args/URL; capped size; never
persist, log or surface env/headers/raw bytes; mismatch reports field names,
not values): 2. ALT-CSK states most of a bound (proposal §§4–5) but stages
whole-file copies containing possible foreign literals beside their targets,
which *persists* raw foreign bytes transiently: 1. No design that health-
checks could score 2; BASE's "no health checks" (`BASE-DESIGN.md:58`) is
correct and is retained in BASE′. `env` values never appear in any design's
files (§2.2 "values never appear"; §5.8 no `env` member); `passable_env_names`
(§2.2, §10.3, manager §7.1) bounds names at launch without the manager
opening values.

**E4.** Hand-written, csk-written and profile-provided servers can satisfy
by evidence. Plugins and cloud connectors cannot: manager §6 defines only
file surfaces, no client-report channel exists, and `BASE-DESIGN.md:42`
"a cloud connector *the client reports*" names an input no spec supplies.
They can satisfy only by explicit operator binding, i.e. assertion, in
BASE, BASE′ and ALT-LOCAL: 1. ALT-CTX excludes those zoo rows by
construction (a managed Claude launch under `--strict-mcp-config` ignores
every other MCP configuration, §7.8): 0. See §5 for the proof that E4 = 2 is
unattainable in the managed universe (`pi`).

**E5.** BASE's `server.package` carries a semver `range` on the *skill*
surface. environments §1.4 closes with: "Project `Skillfile.json` and the
skill manifest keep core §4.4 unchanged: no range enters a surface that has
no lock", and core §4.4 admits only exact `tag`/`revision` refs for skill
dependencies. As written the field borrows the `requires.mcp` range grammar
into a lockless object, tightening the manifest to lock-bearing manager
behavior: 1. BASE′ uses the exact-ref grammar of a skill requirement
(`git` + `ref {kind: tag|revision}`, optionally `directory` as in draft
manifest schema 9) and the §2.2 HTTPS URL grammar for endpoints: 2.
ALT-SHIP ties server evolution to skill snapshots and creates cross-skill
conflicts for one name with no closure rule over declarations: 1.

**E6.** Strengths kept from BASE: status exactly "configured / auth not
checked", never "connected" (`BASE-DESIGN.md:42,58`), consent before
provisioning (line 51). But BASE leaves the decisive rule open — "Is
'unknown' acceptable for `required_in: any`?" (line 69) — and lets *project*
configuration carry aliases (line 46) and an operator binding satisfy
identity (line 40) without distinguishing *asserted* from *verified*
satisfaction; project data is checkout-controlled. Precedence is also
unaddressed: §6 defines presence over project and user surfaces, and the
implementation unions them (`ConfiguredServers`), so a shadowed entry and
an effective entry are indistinguishable today. Hence 1. BASE′ fixes the
table: unknown never satisfies `any` or `all`; disabled entries never count
(manager §6); malformed configures nothing and warns (manager §6); only the
client-effective entry counts, and unknown precedence yields *unknown*, not
*satisfied*; machine-owned bindings record `operator-asserted` distinctly
from `verified` in the marker: 2. ALT-LOCAL without local policy collapses
to §6 name-presence, which silently satisfies a skill through a squatting
same-name server: 1. ALT-CSK's refusal machinery is strong, but decision D1
publishes `http` declarations with `auth none|oauth` and no env reference
*without consent*; the rubric's 2 requires consent before *any* write: 1.
ALT-CTX surfaces every declaration before lock publication (§2.3) but
surfacing "is informative … never fails the operation" — it is not
consent: 1.

**E7.** BASE is vector-shaped but not vector-ready: endpoint normalization
(host case, default port, path equality) is unstated; "the same declaration
digest" (line 40) is undefined for a foreign native entry, which carries no
digest — declaration identity in a closure is source/commit/directory under
§1.3–§1.4 and §2; command/args equality must invert per-client renderings
that §5.8 itself marks *docs-confidence* for two adapters; transport
(`BASE-DESIGN.md:70`) and the schema home (line 71) are open. Core §4.4 says
a requirement "MAY *document* `transport`", so enforcing it is a §6 change.
BASE′ narrows all of this (§6), but per-client *effective-precedence* rules
remain partly docs-confidence (environments §7.8, §5.8), so an honest 1
until a drafting pass writes the tables and vectors. ALT-CTX is already
specified: 2. ALT-CSK has closed grammar and frozen vectors (V01–V13) but
an unresolved schema-series fork (curator review H1/H2) and a §6
transport/malformed tightening (H3): 1.

**E8.** Uniform new-dependency count. BASE/BASE′/ALT-SHIP: one exact-plan
consent, plus the client's own auth flow when the server needs one, equals
two actions in the authenticated common case: 1 (zero actions when the zoo
already provides a matching server — recorded, non-discriminating).
ALT-LOCAL adds policy authoring per name per machine before consent: 1
(zero only after the fleet-wide repetition is amortized). ALT-CTX requires
choosing/authoring a context package and a profile install: 1. ALT-CAP and
ALT-GW require enrolling credentials with the manager per server: 0.

## 5. Two structural results about the rubric itself

**E4 = 2 is unattainable in the managed launch universe.** §5.8 gives
adapter `pi` "none — no file and no fragment `mcp` section", and §7.8 records
as *verified* that pi 0.84.2 has no MCP channel. Therefore no design can make
every zoo member satisfy a requirement in every universe without a client
change, and any score sheet giving E4 = 2 must have quietly scoped E4 to
native launches only. The rubric should state its universe; until it does,
E4 is capped at 1, and the attainable ceiling is 15, not 16. (If E4 is
scoped native-only, BASE′ and ALT-LOCAL rise to E4 = 2 and ALT-CTX stays 0;
ranking is unchanged.)

**"Highest total, no 0 in E3/E6" does not by itself select a goal-covering
design.** ALT-CTX ties the winner at 11 with E4 = 0 and without letting
skills declare anything new — it is, in substance, the incumbent profile
machinery restated. The proof therefore needs the goal-coverage
precondition of §1 (or an explicit "no 0 in E4" clause) in addition to the
mission's E3/E6 gate; otherwise the collective could "prove elegant" a
design the operator would recognize as not doing the job.

## 6. Smallest changes to the base (the BASE′ delta)

1. **Package identity is an exact ref, never a range** on the skill surface:
   `{"package": {"git": "…", "ref": {"kind": "tag"|"revision", "value": "…"},
   "directory"?}}`, reusing the core §4.4 skill-requirement ref grammar
   (environments §1.4 lockless rule). Ranges remain available at the profile
   layer (`requires.mcp`), where a lock exists. (E5, E7)
2. **Endpoint identity reuses §2.2 verbatim**: the `https` scheme, ASCII
   host, no userinfo/query/fragment, plus stated normalization (host
   case-folded, default port elided, path compared byte-exact).
   (E7)
3. **Delete the auth class.** It is information a deliberately thin manager
   does not need: `env` is already expressed by declaration `env_names`;
   `oauth` vs `none` is indistinguishable in `agent-mcp` schema 1 and only
   the client acts on it; `hint` carries author guidance. This avoids
   minting `agent-mcp` schema 2 (curator review H2) and removes a field.
   Consent becomes uniform instead (§6.5). Surfacing should print the
   endpoint (curator review S1). (E1, E2, E6)
4. **State the metadata-only parse bound** (§4 E3) and replace the absolute
   "never reads" claim with it. (E3 amended 1 → 2; original stays 0 and is
   reported.)
5. **Honest-satisfaction table (fix the open point against satisfaction):**
   unknown never satisfies `any` or `all`; provisioning of every class
   (stdio, endpoint, env-referencing) requires exact-plan operator consent;
   endpoint-only requirements are never provisioned (BASE already keeps
   this). (E6)
6. **Bind lives in machine configuration only** — delete "or project" from
   the alias layer — and an operator binding is recorded as
   `operator-asserted`, never merged with `verified` in markers or status.
   (E6, E4 honesty)
7. **Satisfaction is launch-scoped and precedence-aware.** Native universe:
   manager §6 surfaces, client-effective entry only. Managed universe: the
   profile lock's MCP set for that adapter (§5.8, §7.8; `pi` has the empty
   set). Status always names its universe. (E4, E6)
8. **Schema home: draft skill-manifest schema 9 only**, via a new
   dependencies definition; manifest schemas 5–8 stay frozen
   (`COMPATIBILITY.md:22-24`); decision record and positive/negative
   vectors under `GOVERNANCE.md`. A requirement without `server` keeps its
   exact current meaning, and `transport` remains documentary unless
   `server` identity makes a mismatch an identity mismatch under an amended
   §6. (E1 counted, E7)
9. **Provisioning paths are named honestly.** Managed: the manager offers
   the exact-ref declaration *into the operator's profile closure* (root or
   machine overlay, §6/§9), after which the existing lock, surfacing (§2.3),
   allowlist, audit and signer machinery is used unchanged — never a direct
   skill-to-§5.8 write. Native in-place writes are a separate, optional
   capability under its own review (environments preamble), owned by the
   ALT-CSK lane, not a claim of this design. Identity comparison against a
   foreign entry compares the normalized recipe (transport, command, args
   or normalized endpoint) and is reported as *recipe match*; a declaration
   digest is claimed only where the manager itself recorded the declaration
   (the lock). (E2, E6, E7)

With these changes Curator and csk can still share one declaration format
and one requirement semantics (`BASE-DESIGN.md:65`), but they share the
*schema-9 exact-ref* form, not the range form, and neither mints a schema
series outside `curator-spec`.

## 7. Challenges to the first-pass rubric seat (to be answered in debate)

These are stated against the claims of `BASE-DESIGN.md`, and against **any**
score sheet whose rows would be contradicted by the evidence cited; they
are recorded here before the first-pass verdicts are opened.

1. Show a field/object count across *all* surfaces that yields one;
   the manifest-only count omits auth class, Bind, and marker (§4 E1).
2. Show how a skill-carried `range` survives the §1.4 lockless rule, or
   concede the exact-ref form.
3. Reconcile "never reads values" with whole-file unmarshalling in the
   incumbent checker, under *both* E3 wordings.
4. Name the channel by which a client "reports" plugins and cloud
   connectors to the manager, or score those rows by assertion.
5. State the universe of your E4 row and account for `pi` in it.
6. Say whether §2.3 surfacing or any existing record constitutes consent
   under E6's literal text in your sheet, uniformly for all designs.
7. State how a winner with E4 = 0 (or without skill-carried declarations)
   is excluded from "elegant" in your proof.
8. Define "declaration digest" for a hand-written foreign entry, or
   downgrade that identity claim to recipe match.

## 8. Preferred design and proof status

Preferred: **BASE′** = the base design with §6 applied. The base's core
move — one optional identity field on the existing name requirement,
requirements separated from provisioning, authentication left entirely to
clients, no health checks — survives adversarial testing; its published
justification ("one field, only existing machinery, no secrets ever")
does not survive unedited. No proof is claimed by this seat: proof needs a
second seat from an independent five agreeing within one point per row on
the winning design, with evidence. This file will be reconciled row by row
with the first five's rubric seat in the rounds that follow; this seat's
initial numbers above will not be edited silently — any movement will be
dated and attributed to the argument that caused it.

---

## Addendum — Round 2 (after opening peer verdicts and findings)

_The initial table above is unchanged. This addendum records the comparison
and every movement with its cause. Local repository pin for this addendum is
still `b5e7dab` — sandbox `git fetch` over SSH fails ("No user exists for
uid 501"), so post-`b5e7dab` publications are known to this seat only from
room messages and are labelled as such where used._

### 9. Independent convergence with wonder-02

- **BASE as written:** wonder-02's file scores `[1,1,1,1,1,1,1,1] = 8`
  (E3 operational reading). My initial row is identical on **every cell**,
  reached from the same pins without access to their file. On the original
  E3 wording we also now agree at 0 (their correction recorded in
  `f-secret-boundary`; my initial score was 0).
- Their mechanical claims C1–C14: I confirm C3's code-level disabled-entry
  gap (Codex/JSON branches lack an enabled filter), C4, C5, C7, C8, C9, C10,
  C12, C14 from my own reads at the same lines. C11 and C13 I confirm with
  the narrowings in §10 below.
- All six findings files (`f-consent-binding`, `f-launch-universe`,
  `f-opaque-provider`, `f-package-is-not-service`, `f-schema-budget`,
  `f-secret-boundary`) are confirmed from this seat's independent source
  reads; per-topic cross-host confirmations were posted separately.
- `f-cross-kind-name-collision` (known from its topic): confirmed
  firsthand in `curator/internal/contextresolve/contextresolve.go` — the
  resolver keys constraints and selections by name and coerces a second
  kind to the first ("One name, one kind" in `add`). Optional-A adoption
  must therefore use distinct skill vs declaration names or defer; this is
  an implementation-backed reuse limit, consistent with §1.4's
  name-keyed closure.

**Challenge to wonder-02:** the rubric owner's verdict *file* is still the
Round-1 draft — it forecasts a BASE′ at 13 with E2 = 2 and E7 = 2 and
states that no alternatives have been posted — while room convergence has
since moved to N/N+A at `[1,1,2,2,2,2,1,2]`, with E2 explicitly refined
from 2 to 1 (binding/evidence is not existing-only machinery) and E7 held
at 1. The proof record should cite a rubric file that contains the
converged table and scores the serious alternatives head-to-head, as the
mission requires of that seat. My initial BASE′ E2 = 1 / E7 = 1 stand
against the stale forecast; against the converged sheet there is no
remaining disagreement on those rows.

### 10. Definitional movements (initial → revised, with causes)

1. **E8 common case.** I initially counted the new-dependency case;
   the rubric seat's stated case is *a suitable provider already
   configured*, with cold setup reported separately (E8 = 1, totals drop
   by one). I adopt that dual reporting: it matches the operator's zoo
   premise, and my cold case survives as the published sensitivity, not
   a hidden disagreement.
2. **E4 and assertions.** I accept the refined scope found in the
   findings: a protected, target-scoped operator *reliance* lets an
   unobservable but capable provider satisfy, labelled `asserted`;
   known-incapable targets (current managed `pi`, project-scoped
   Windsurf) still fail honestly and cannot be asserted into having a
   channel. Under this explicit definition E4 = 2 for N-shaped designs.
   My `pi` ceiling argument is thereby narrowed, not withdrawn: it caps
   any reading of E4 that demands evidence-grade satisfaction in every
   launch universe, and it is why the definition above must be written
   into the proof text.
3. **Identity: normative → reported (revision 1).** I concede wonder-02's
   demotion for the first contract: recipe equality is not provenance
   (`f-package-is-not-service`), per-client renderings are partly
   docs-confidence (§5.8), and normative identity would create false
   install failures while over-claiming. My BASE′ item 9 already renamed
   it *recipe match*; making that gate normative is deferred to a
   governed later amendment if provenance evidence ever demands it.
4. **BASE′ E5 deployment tax.** wonder-01's point stands: a manifest
   schema-9 skill MUST be rejected by older readers (`COMPATIBILITY.md`),
   whereas name-keyed v5 bytes degrade gracefully. Under the rubric's
   "any manager" wording that is a real portability cost of putting
   identity on the skill wire now.
5. **ALT-SHIP re-score.** My initial ALT-SHIP assumed a manifest field
   and normative identity. wonder-01's stronger construction (schema-1
   declaration file in the snapshot, recommendation only) plus the
   debate's bounds — exact resolved revision rather than version-tag
   coupling, independent MCP allowlist/signer/audit admission,
   path-source refusal, companion context package for multiple servers,
   distinct-name rule from §9 — answers my multi-server and version
   objections. Re-scored below as A.

### 11. Revised scores (unified primary definitions)

Primary E8 case: already-configured suitable provider. Cold setup: E8 = 1
for every row below except ALT-CAP/ALT-GW (already 0), i.e. totals minus
one. Original E3: 0 for every native-inspecting row (totals minus two
where amended E3 = 2); ALT-CAP/ALT-GW stay 0/0 and disqualified.

| Design | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N (names + launch-scoped evidence + protected reliance) | 1 | 1 | 2 | 2 | 2 | **1** | 1 | 2 | 12 |
| N+A (N plus corrected shipped recommendation) | 1 | 1 | 2 | 2 | 2 | **1** | 1 | 2 | 12 |
| A alone (legacy check unchanged; fails goal ii for opaque) | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | 13 |
| BASE′ normative-identity (my initial preference, revised) | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 12 |

**Recorded dissent (sole row vs the ivmbp converged vector): E6 = 1 for N
and N+A, not 2.** Reason: N retains name-based satisfaction over native
surfaces. A same-name entry supplied by a hostile or merely unrelated
checkout (project surfaces are repository-controlled; §6 reports them only
with a trust warning) still *satisfies* — labelled, but satisfying. Until
the contract states whether project-only observed evidence is satisfying
or merely trust-gated-reported, "unknown is never satisfied silently" is
only half discharged: the *wrong known* server is the remaining silent
case. This is a one-point difference, inside the proof tolerance, and it
does not change my preference ordering.

**Preference movement:** staged adoption. Revision 1 = **N, with A as an
optional complement** under the bounds in §10.5/§9. The BASE′ wire
identity is not rejected; it is deferred behind the trigger that N cannot
meet (author-pinned provenance as a hard requirement), because N+A
reaches the same revised total without a schema-series change, without
old-reader rejection, and with the cross-kind and path-source limits
stated. Auth needs no new field in either staging (agreement with my
initial §6.3 and with wonder-02's delta 5).

### 12. Proof status after this comparison

- The converged ivmbp vector for N/N+A is `[1,1,2,2,2,2,1,2] = 13`
  (room messages; astra-01/02/03 verdicts at the local pin converge to it,
  and mini seats have since been reported matching it). My revised
  vector differs on exactly one row (E6) by one point. My **initial,
  pre-reading** ALT-LOCAL vector differed on E4, E6 and E8 by one point
  each — also within the mission's one-point-per-row tolerance, *if* the
  convener rules ALT-LOCAL and N the same design (names only in skills,
  provider resolution in protected operator policy). I do not make that
  ruling from this seat.
- BASE as written is refuted as already-elegant with identical
  independent scores on two hosts (8/16, every row).
- Still not a completed proof from this seat: (a) the same-design and
  definition rulings are the convener's; (b) E7 = 1 everywhere serious
  until the protected binding/marker grammar (existing configuration
  family successor, not a new record family — else E1 = 0 under the
  mission anchor) and the E6 truth-table vectors are written, including
  the project-only case in my dissent; (c) wonder-02's verdict file
  should be brought to the converged state (§9) so the proof cites
  files, not only room messages. No runtime or global-optimality claim
  is made by anyone, correctly.

### 13. E6 condition resolved as a condition (post-addendum movement)

Replies from astra-05, astra-06 and wonder-11 bound the candidate
further: E6 = 2 applies only to the explicitly opted-in selected-launch
contract, in which project-file presence alone cannot establish
observed-effective inclusion, known rejected/disabled/excluded state
defeats acceptance, unresolved activation/trust remains qualified
unknown, status renders evidence source and grade together ("configured
by name; provider identity and authentication not checked", or
"operator-asserted"), and legacy §6 `FoundIn` is not upgraded. For that
bounded candidate this seat's vector becomes `[1,1,2,2,2,2,1,2] = 13`,
an exact match with the converged ivmbp vector. For any variant
rendering a bare "satisfied" from name presence, E6 = 1 stands. The
bounds living across candidate messages rather than one normative text
is precisely the E7 = 1 debt; the dissent above remains in the record as
the condition, not as a numerical dispute over the bounded candidate.
astra-03's E4 scope (source-category coexistence in an already capable
selected launch; managed `pi` and strict-channel exclusions unavailable)
is the definition under which E4 = 2 is accepted here; the stricter
E4 = 1 reading retained elsewhere on the mini should remain visible in
the proof text.
