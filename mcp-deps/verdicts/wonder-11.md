# Verdict — macmini wonder-11 (third pass, independent adversarial alternatives hunt)

Seat: `wonder-11` on Mac mini, identity `macmini_swarma-mcp-deps_wonder-11`.
Lens: challenge `wonder-01`; construct at least two genuinely different designs and try to beat the base.

**Independence statement.** The scores and alternatives in the "Initial" sections below were formed and saved
before I read any other seat's verdict file or finding file. Sources read for the initial pass:
`MISSION-MCP.md`, `BASE-DESIGN.md`, the three files in `inputs/`, curator-spec (`protocol/core.md` §4,
`profiles/manager.md` §§6–7.1, `protocol/environments.md` §§2.2–2.3, 5.8, 7.8, `schemas/v1/common.schema.json`,
`schemas/v1/agent-mcp-v1.schema.json`, `COMPATIBILITY.md`, `GOVERNANCE.md`), and curator `internal/mcp/mcp.go`.
Later revisions after the debate will be marked as revisions; initial scores will not be silently rewritten.

## Preferred design (initial)

**Name-only skills, launch-aware checking, operator-root binding.** Three parts:

1. **Skills change not at all.** `dependencies.mcp_servers` stays exactly the v5 grammar
   (`{hint, transport?, required_in?}`, core §4; `common.schema.json` `mcpRequirement`, `additionalProperties: false`).
   No `server` field, no identity, no executable content in a skill manifest.
2. **Fix the checker's universe (the actual elegance bug).** Manager §6 satisfaction is computed over the
   universe the launch will really see: native surfaces for a native install; the active profile's resolved
   MCP set for a managed launch. Report the source of satisfaction (`native` / `profile` /
   `operator-asserted external` / `unknown`) as distinct states; never merge them silently, never count
   `unknown` as satisfied. Malformed native files keep §6 semantics (configure nothing, warn).
3. **Optional provisioning lives in an operator-authored root object, never in a skill.** A project/machine
   root (Skillfile via a spec extension reserving its schema, or a manager-owned file with its own series)
   may bind a required name to: an exact-pinned `agent-mcp.json` schema-1 package whose package `name`
   equals the binding key, an inline §2.2 `server` object, or an external assertion (optionally naming the
   differently-named configured entry — this absorbs aliasing into the same one concept). Provisioning goes
   to managed homes through §5.8 as today, or to native configs only in a manager that implements the csk
   slice-1 contract (consent by authority, consent bound to the exact plan digest, per-entry protected
   ledger, typed read states, refusal inside marker-carrying managed homes). Authentication gains no new
   field anywhere: the report derives "env names listed / client OAuth possible / auth not checked" from the
   declaration shape, surfaces the endpoint URL in the plan, and the manager never probes.

## The designs scored

- **BASE** — `BASE-DESIGN.md`: one new optional `server` field on the skill requirement
  (`{package:{git,range}}` or `{endpoint}`), identity matching against configured entries, a machine/project
  alias map, optional consent+allowlist provisioning, an auth class on declarations, no health checks.
- **ALT-A "Zero-field"** — preferred parts 1+2 only: no new field anywhere; launch-aware §6 checking;
  on an unsatisfied requirement the manager MAY non-normatively suggest allowlisted declaration packages
  whose `agent-mcp.json` `name` equals the required name. No provisioning semantics in the spec at all.
- **ALT-E "Operator-root declarations"** — preferred part 3 with skills name-only: provisioning declarations
  authored in the operator's root object (the csk input design, trimmed to `agent-mcp` schema-1 shapes),
  native writers under the csk slice-1 decision contract.
- **ALT-B "Closure linkage"** — skills name-only; the skill+server bundle is authored by a distributor as a
  context package whose closure requires both the skill and the `agent-mcp` declaration package, so managed
  profiles provision the server through existing §5.8 machinery; native zoo members satisfy through §6.
- **ALT-C "Capability requirement"** — skills require tool/capability names instead of server names/identity.
- **ALT-D "Manager MCP proxy/broker"** — the manager hosts/proxies servers and handles auth centrally.
- **PREF** — A+E combined (my preferred design above).

## Initial rubric scores (0–2 per row, mission rubric E1–E8)

| Row | BASE | ALT-A | ALT-E | ALT-B | PREF |
|---|---|---|---|---|---|
| E1 New concepts/fields | 1 | 2 | 1 | 2 | 1 |
| E2 Reuse | 1 | 2 | 1 | 2 | 1 |
| E3 Secrets (amended) | 1 | 2 | 2 | 2 | 2 |
| E3 Secrets (original) | 0 | 1 | 1 | 1 | 1 |
| E4 Zoo | 2 | 1 | 2 | 1 | 2 |
| E5 Portability | 1 | 2 | 2 | 1 | 2 |
| E6 Honest failure | 1 | 1 | 1 | 1 | 1 |
| E7 Specifiability | 1 | 2 | 2 | 2 | 2 |
| E8 Operator effort | 2 | 1 | 1 | 1 | 1 |
| **Total (amended E3)** | **10** | **13** | **12** | **12** | **12** |

ALT-C scores at most 7 and is disqualified if satisfaction requires probing (E3=0: a tool-list/health probe
can itself send a credential; if satisfaction instead trusts advertised tool lists, `agent-mcp` schema 1 has
no such field and the claim is unverifiable, E6=0). ALT-D is disqualified (E3=0, E2=0): environments §2.2
states "The manager never executes, installs, updates, or launches a server", and a proxy that routes calls
must hold or forward credentials — exactly what the operator asked Curator not to take on.

"Elegant" per the mission = highest total with no 0 in E3 or E6. On my initial scores ALT-A (13) beats BASE
(10), and PREF (12) buys real provisioning for points the rubric does not directly reward. BASE also carries
E3=0 under the original rubric row (see below), which no other scored design does.

## Justification per row (initial, with evidence)

### E1 — New concepts and fields

BASE=1. The headline ("one new optional field") is true only of the skill manifest. The design as a whole
also introduces: two `server` variants with different pinning (`package{git,range}` vs `endpoint`); a
machine/project alias map (Bind layer, BASE lines 46–47); an auth class that "declarations carry"
(BASE line 55) — but `agent-mcp-v1.schema.json` is a closed object with no auth/headers member, so this
field needs either `agent-mcp` schema 2 (which the curator review input, H2, says must not be minted outside
the spec) or a second new field somewhere else; and a provisioning-offer flow. That is one field plus three
concepts. ALT-A/ALT-B=2 (literally zero new fields). ALT-E/PREF=1 (one new optional map on an operator
object; its value grammar reuses §2.2, but it is a real addition and needs a schema-series decision,
curator-review H1).

### E2 — Reuse

BASE=1. It reuses §2.2 packages, §5.8, the allowlist and audit — genuinely. But identity matching is new
parallel machinery: today's checker (`internal/mcp/mcp.go` `Verify`, lines 89–166) uses presence by name
plus a positively-stdio command PATH warning; BASE requires normalizing six clients' entry shapes
(Claude `env:{"T":"${T}"}`, Codex `env_vars`/`bearer_token_env_var`, OpenCode argv-array `command`, Cursor
`${env:T}` — csk input §3 table) into a comparable "same command/args / same origin+path" identity. Native
provisioning ("for a manager that implements native writes") imports the entire csk writer apparatus
(span-preserving editors, protected ledger, consent store, CAS journal — csk input §§3–4).
ALT-A/ALT-B=2 (only §6, profile closure, §2.2/§2.3/§5.8 as they stand). ALT-E/PREF=1 for the same writer
machinery, admitted openly and capability-gated; the managed-only subset of PREF would score 2.

### E3 — Secrets

Amended row. BASE=1: to verify "the same declaration digest or command/args … the same origin+path"
(BASE line 40) against a hand-written native entry, the manager must semantically use foreign
`args`/`url`/header/env material. The spec itself puts `args` and `url` inside the secret-material
detector scope (environments §2.2: "a token in an argument or a URL is a blocking finding"). BASE states
no bound on persistence, logging or surfacing of those compared bytes, while simultaneously claiming the
manager "never reads, stores or forwards values" (BASE line 57) — under the mission's E3 note an unstated
bound caps the score at 1. Original row: BASE=0, because the comparison *uses* values beyond names
(including material the spec classifies as potentially credential-bearing). ALT-A/B/E/PREF amended=2,
original=1: they add nothing beyond the status-quo §6 parse (whole-file parse into memory already happens
in `entriesInFile`, `internal/mcp/mcp.go` lines 240–289, and only names plus a positively-stdio command
name are used). PREF additionally binds any native writer to the csk-stated bound (digests only in the
ledger/journal, foreign bytes never logged or surfaced, no diff bodies — csk input §4), and identity is
never computed over foreign bytes at all: it exists only inside operator-authored declarations, where
`args`/`url` are already audit-gated.

### E4 — Zoo

BASE=2, but only through its escape hatch: file-invisible members (client plugins, cloud connectors —
"not on disk", BASE zoo table) cannot identity-match, and "a cloud connector the client reports"
(BASE line 42) names a reporting channel that neither manager §6's closed surface table nor
`internal/mcp` has. What saves the row is "or an explicit operator binding" (BASE line 40): every zoo
member *can* satisfy, at operator-action cost moved to E8. ALT-A=1 and ALT-B=1: with no assertion channel
an invisible-but-present cloud server fails the check (a false negative), and ALT-B provisions nothing
outside managed profiles (`pi` has no MCP channel at all, environments §7.8). ALT-E/PREF=2: name-only
§6 acceptance for everything on disk, plus the operator-asserted-external binding for what is not.

### E5 — Portability

BASE=1. A skill manifest carrying `server` is rejected by every current reader: `mcpRequirement` has
`additionalProperties: false` and is shared by manifest schemas 5–8 and draft 9 via `$ref`
(`common.schema.json` lines 610–619; `agent-skill-v9.schema.json` references the same member).
COMPATIBILITY.md: "A release never redefines old schema bytes in place", so `server` needs a new manifest
schema version — after which the manifest is portable only across managers implementing it, and an
`endpoint` value can still pin a tenant/host-specific origin into a supposedly portable skill.
ALT-A/E/PREF=2: the skill manifest is byte-identical to today's and readable by old managers; machine-
and project-specific data lives in machine/project objects, where it belongs. ALT-B=1: the manifest is
portable but the *bundle* only provisions under an environments-capable manager with the right profile.

### E6 — Honest failure

All scored designs=1; nobody earns 2 yet, for different stated reasons. BASE: (a) "unknown" for opaque
providers is left as an open point ("Is 'unknown' acceptable for `required_in: any`?"), so the design as
written does not yet forbid silent satisfaction; (b) satisfaction is judged in the install-time native
universe while the launch universe differs by adapter — Claude `--strict-mcp-config` ignores the native
entries §6 just counted, Codex seed revision B strips them, OpenCode lets a project entry override the
profile's (environments §7.8 residuals table) — so "satisfied" can be false at the only moment that
matters, and a profile-provided server is invisible to the §6 checker (false "missing").
ALT-A/B/E/PREF keep name-only semantics, so a wrong server under the right name still silently satisfies
(name squatting/collision is inherited from §6 and not solved by any design here); PREF fixes (b) and
labels asserted-external distinctly, but that does not remove the collision residual, so I do not claim 2.

### E7 — Specifiability

BASE=1. The `server` grammar itself is writable, but conformance needs vectors for identity: URL
normalization (default port, trailing path, `/mcp` vs SSE aliases), cross-client argv equivalence,
two skills requiring one name with different `server` values, and `range: "^1"` resolution — note core
§4.4 forbids branch/range for skill dependencies (`ref.kind` is `tag` or `revision`), and a ranged
package has no fixed digest for BASE's own "same declaration digest" test until a lock concept is added
to skill installs. The schema home (new manifest version vs extension) is listed as open; GOVERNANCE.md
requires a decision record for new schema versions and trust-semantics changes.
ALT-A=2 (no grammar; the launch-universe rule is vector-testable against §5.8/§7.8 facts).
ALT-E/PREF=2 on grammar/governance (closed grammar and frozen vectors V01–V12 already exist in the csk
input; the H1 fix is a stated either/or), with the caveat that per-client writer conformance is
capability-gated, docs-confidence for several clients (csk input §3), and must refuse rather than guess.
ALT-B=2 (already specified end to end).

### E8 — Operator effort

BASE=2: already-configured-by-anyone costs zero actions; the packaged missing case costs one consent.
This is BASE's best row and I score it as such. ALT-A=1 (the operator still wires the server; a suggestion
only shortens the search). ALT-E/PREF=1 (someone must author or accept a root binding per project; when
the manager can propose an exact binding from an allowlisted package of the required name, the missing
case is also one consent — I would raise PREF to 2 if that proposal flow were made normative rather than
optional). ALT-B=1 (adopting a profile is a heavy answer to "this one skill needs a server").

## Problems with BASE that any winner must answer (initial list)

1. **Range vs pin discipline.** `{"package":{"git":"…","range":"^1"}}` contradicts the exact-ref rule for
   skill dependencies (core §4.4) and makes digest-identity, consent binding and the package allowlist act
   on a moving target. Ranges are legitimate only where a lock records the resolution (profile closure).
2. **Package name ≠ required name is unhandled.** Provisioning an `agent-mcp` package materializes a server
   under the package's identity (§5.8 keys the map by server name from the declaration). BASE never states
   package `name` MUST equal the required key, so a successful provision can leave the requirement still
   unsatisfied (then "fixed" by an alias — the second concept rescuing the first).
3. **Remote env-auth cannot be provisioned faithfully.** §5.8 http materialization emits only
   `{"type":"http","url":…}` — no headers — and `agent-mcp` schema 1 has no header/env-reference grammar.
   An `endpoint`/http declaration with `env` auth therefore provisions (at best) an unauthenticated entry
   outside a managed launch; BASE's auth section does not mention this. The csk input solves it with
   per-client header env-references (its §3), which is exactly the writer machinery BASE leaves unnamed.
4. **Credential routing needs endpoint visibility + consent by authority.** An http entry whose header
   references `$GITHUB_TOKEN` routes a credential to a declaration-chosen URL (csk decision D1).
   §2.3 surfacing prints `command=- args=[]` for http — no URL column. Any provisioning design must surface
   the URL and treat env-referencing http like stdio for consent; BASE's single "explicit operator
   consent" plus allowlist does not distinguish authority classes, and under `hardened` an inline/ranged
   declaration reached from a *skill* (not a profile closure) may fall outside the
   `mcp_package_allowlist_empty` resolution error, which manager §7.1 phrases over profile closures.
5. **Consent is not bound to bytes.** BASE requires consent but does not bind it to the exact normalized
   plan (name, agents, scope, argv/url, env names, pin digest). With `range`, the resolved declaration can
   change under a standing consent. The csk contract (input §2) is the bar.
6. **Identity is opt-in by the wrong party.** A hostile or lazy skill omits `server` and inherits §6
   name-only satisfaction by any same-name entry, including a hostile project's `.mcp.json`. The security
   upgrade therefore protects only skills whose authors ask for it, while its costs (E3 parsing, E7
   normalization) are paid by everyone. In PREF, strictness is expressed by the operator's root binding —
   the party whose machine it is.

## Smallest set of changes from BASE to PREF

1. Delete `server` (both variants) from the skill requirement; core §4 and `mcpRequirement` stay frozen.
2. Manager §6: define the satisfaction universe per install/launch mode and the reported source dimension
   (`native`/`profile`/`asserted`/`unknown`); `unknown` never satisfies; malformed stays warn+empty.
3. Move Bind into an operator-root binding map (spec extension reserving the Skillfile schema, or a
   manager-owned file): key = required name; value = exact-pinned `agent-mcp` schema-1 package (name must
   equal key), inline §2.2 `server`, or external assertion (absorbs the alias map; no ranges).
4. Provisioning: managed homes via §5.8 unchanged; native writes only under the csk slice-1 contract
   (D1 consent-by-authority, exact-plan consent binding, per-entry ledger, typed reads, managed-home
   marker refusal, `curator-mcp.config.toml` never touched); hardened posture stated to cover
   root-provisioned declarations (allowlist + consent for every inline declaration under `hardened`).
5. Auth: no new field; derive the auth report from declaration shape; add the URL to surfacing/plan output
   (the §2.3 `url=` fix); status stays "configured / auth not checked"; no probes, no health checks.

## Status

Initial independent verdict, saved before reading other seats' verdicts/findings and before joining the
room debate. Revisions will be appended below this line with round markers.

---

## Revision 1 (round 1, after reading wonder-01 and the alt topics)

I have now read wonder-01's verdict, `alt-skill-ships-declaration` (A), and `alt-names-local-evidence`
(N, astra-01). My independent PREF converged with their composite on the core (delete `server`,
launch-scoped name checking, no auth field, no identity over native bytes). I tried to break A and N;
the core survives, with three guards and two concessions from my side.

### Three guards on A (skill ships `agent-mcp.json`), with evidence

1. **Joint-closure name collision (confirming astra-04, with a nuance).** Independently verified in
   `sources/curator/internal/contextresolve/contextresolve.go`: the resolver keys `constraints`,
   `kinds` (line 317: `name → kind`) and `selected` by name alone, and `add()` (lines 411–414) coerces a
   second requirement kind for a known name to the first ("One name, one kind: the closure is keyed by
   name across kinds"). So a profile closure cannot contain both `skill:X` and `mcp:X`. Nuance from my
   read: the *lock format* does not forbid the pair — `contextlock` validation keys uniqueness and
   ordering by `(kind, name)` (`contextlock.go` member validation; `Find(kind, name)`, line 179). The
   limitation is current resolver behavior under environments §1.4 ("one name, one commit"). Revision-1
   answer: the adoption recipe must require the declaration name to differ from every skill-member name
   in the target closure, and must not print a remediation it cannot execute when they collide
   (report deferred/rename-required instead). A governed resolver change is the alternative; distinct
   names cost no machinery and preserve A's E1/E2 scores. The collision needs skill name =
   declaration name = requirement key, so it bounds A; it does not defeat A or N.
2. **Path-source skills: print-only.** Environments §2.2 is git-only for declaration packages
   (`mcp_declaration_path_source_refused`; a path source "has no canonical identity for the allowlist").
   A shipped declaration inside a path-sourced (local/dev) skill therefore can never be adopted into a
   profile through `requires.mcp`. A's surfacing must say so (informational row, no profile remediation)
   in that lane; printing "add it to the profile" there would be an unexecutable remediation.
3. **Secret-material scope needs one explicit sentence in the skill lane** (answer to wonder-01's open
   sub-question iii: yes). Manager §7 makes the `context-secret-material` class REQUIRED for
   profile-snapshot audit under the environments capability (environments §9.1 normative); the general
   skill-audit pipeline is detector-based and does not by that text guarantee `args`/`url` scope for a
   skill-root `agent-mcp.json`. The core §4 MAY clause that admits the file should state its `args`/`url`
   are in secret-material scope at skill audit, mirroring §2.2.

Answers to wonder-01's other sub-questions: (i) multi-server — do **not** add an `mcp/` directory now;
discovering a *set* by layout (ordering, duplicate names across files, partial validity) spends A's
E1=2. Multi-server authors already have the companion context package: `requires.mcp` is a name-keyed
map whose value is `{git, range|tag|revision, directory}` (`agent-context-v1.schema.json`), i.e. my
ALT-B covers the multi-server case with zero new grammar. (ii) malformed shipped file — warn once,
naming the file and requirement key only (never content: `args` may carry secret material), never a new
install failure.

### Two concessions revising PREF

1. **Bindings/assertions live in protected manager state only — never in a checkout.** My initial PREF
   allowed a project Skillfile to carry external assertions. Wonder-03's circularity point is correct:
   a hostile repository must not assert its own skill's requirement satisfied. Revised: project-root
   files may carry provisioning *declarations* only (csk lane, gated by protected exact-plan consent);
   alias/binding/assertion records are manager-protected state, as in N. This removes the weakest part
   of my PREF part 3.
2. **Drop my catalogue-discovery suggestion in favour of A's surfacing.** Discovering declarations "by
   name from allowlisted sources" needs a catalogue/registry concept I did not price; A (the declaration
   rides the audited snapshot; surface on exact name match) achieves the remediation UX with existing
   machinery. Revised preferred design = **N + A with the three guards above**, with csk native writes
   remaining a separately governed manager capability.

### Score revisions (initial table above stands unmodified)

- **E7: my PREF/ALT-E 2 → 1, ALT-A 2 → 1.** The ivmbp pin-downs (launch-completeness table per
  adapter/mode, configuration/marker home for binding records, the hardened-posture policy choice on
  asserted reliance, behaviour vectors) are real governed-text work not yet written; frozen csk grammar
  vectors cover only the writer lane. I overstated specifiability for every launch-aware design,
  including my own.
- **E8: adopt the common-case/cold split.** For N/PREF: already-configured common case = 2 (zero
  actions; one labelled assertion at most), cold setup = 1. My flat 1 was under-specified, not a
  disagreement about facts.
- **E6 remains 1 from this seat (recorded dissent).** Labelled observed/asserted evidence makes status
  truthful about evidence type, but a wrong server under the right name still passes the requirement
  with nothing in the output naming that risk. If the collective rules that name collision is outside
  E6's letter ("unknown is never satisfied silently"), I accept 2 under that ruling and keep collision
  as a named residual; until then I score what the operator sees.
- **Revised scores for the converged design (N + corrected A):** E1=1, E2=1, E3=2 amended (1 original;
  and 0 under the literal "never reads" phrasing astra-01 applies — I report the mission's two rows),
  E4=2, E5=2, E6=1, E7=1, E8=2 common / 1 cold → **12 amended** (13 if E6 is ruled as above). Against
  the ivmbp N vector `[1,1,2,2,2,2,1,2]=13` my only row difference is E6, by one point — within the
  mission's proof tolerance. I do not myself claim the proof; that judgement belongs to the rubric
  seats and the convener. My standalone BASE scores are unchanged: BASE remains beaten (10 amended,
  E3 original 0, plus the six problems listed in my initial verdict, none of which the debate has
  answered in BASE's favour).

## Revision 2 (round 2: wonder-03's three attacks on A; wonder-12's sheet)

Disposition of wonder-03's attacks in `alt-skill-ships-declaration`, each checked against source here:

1. **Stale adoption (snapshot pin decays silently): fact confirmed, mandatory D1b refuted, claim fix
   required.** Adoption into a profile is the operator's independently pinned choice; environments
   §1.3: "Nothing re-resolves implicitly: `profile use`, `profile sync`, `env resolve`, and status read
   the lock they find." A skill updating C1→C2 therefore promises nothing about the adopted
   declaration, and no new comparison machinery should be made mandatory (with astra-11). What is not
   acceptable is the unqualified headline "skill version pins declaration version": it holds for the
   *recommendation bytes at surfacing time* only. Correct the claim to "the recommendation bytes are
   pinned by the skill snapshot; adoption remains independently pinned". A metadata-only stale notice
   (shipped `(source, skill commit)` vs lock member `(source, commit)`) is permissible optional UX,
   never a satisfaction input. If the headline is not corrected, E6 overclaims on this path.
2. **Remediation tuple: confirmed.** `requires.mcp` values carry `directory`
   (`agent-context-v1.schema.json` `mcpRequirement`: `{git, range, tag, revision, directory}`), and
   core §4.4 schema-9 `directory` defaults to `.` when absent. The printed remediation and its vectors
   must carry the full tuple (canonical git, exact revision, directory-or-`.`, expected declaration
   name); omitting `directory` for a subdirectory skill yields a remediation that fails with
   `mcp_declaration_invalid` when followed exactly.
3. **Invocation point: confirmed mechanically.** `mcp.Verify` is reached only through
   `install.mcpVerifier` (`internal/install/install.go:1595`, constructed for project installs at
   `install.go:573` and global installs at `internal/install/global.go:185`); `internal/envprofile`
   has no call site. Profile install today checks no skill MCP requirement. My position: keep the
   checker contract in manager §6 with a selected-launch input on the skill-install lane; do not add
   a new failure gate to profile install (§9.1) — profile-lane reporting, if any, is warning-grade
   status. Until the operation is named in governed text, E2=1 and E7=1 stand (as revised above).

On wonder-12's structural challenge (3) (E4=2 unattainable because `pi` has no MCP channel): E4 as
written is about zoo *sources* satisfying a requirement, not about every target client supporting MCP.
A `required_in: all` requirement whose target set includes `pi` fails honestly under every design,
including the status quo; that is a target-capability fact (§7.8), already reported as such. I score
E4 over provider categories (hand-written, plugin, cloud, profile, csk) for capable targets, hence
E4=2 for N with labelled assertions — the same scoping astra-12 states. If the rubric owners instead
define E4 over (source × target) cells, every design caps at 1 and the row stops discriminating;
either ruling leaves row differences within one point between my sheet and wonder-12's on this row
alone, but it does not rehabilitate a skill-carried `server` identity (BASE′), which still needs the
identity-matching machinery and schema lane that N+A deletes.

No score change in this revision beyond Revision 1. Preferred design unchanged: N + A with the three
guards, headline corrected per attack 1, full remediation tuple per attack 2.

## Revision 3 (round 3: E6 dissent becomes wording-conditional)

Astra-12 answered my E6 dissent in `alt-skill-ships-declaration`, accepting it as a recorded
interpretation and stating their E6=2 as conditional on status rendering "configured by name /
provider identity and authentication not checked" (or "operator-asserted" for reliance), with known
disabled/shadowed/unavailable evidence still defeating satisfaction. I accept that condition: my
E6=1 applies to any rendering of bare satisfied/configured without the qualifier; with the qualifier
normative, E6=2 is defensible and my revised total for N+corrected-A becomes 13 amended (row-identical
to the ivmbp vector), still 12 without it. Author-side cryptographic provider constraint remains a
separate goal gate that N explicitly gives up; no identity machinery is smuggled back by this wording.
Dissent recorded, not erased; no proof claimed by this seat.

## PARK finalization (convener PARK, 2026-10-14T00:16Z) — FINAL

This verdict is final. The initial independent table above is unchanged; the following fold-ins record
accepted corrections from the debate and supersede the corresponding figures in Revisions 1–3:

1. **Original-E3 correction (astra-01, accepted).** Under the original rubric row ("never reads …
   a credential"), ordinary whole-file native inspection reads foreign bytes that may be credential
   values, so original E3 = 0 for every native-inspecting design, regardless of which fields are used
   or output. My earlier "E3 original 1" for the name-only designs is withdrawn. Corrected dual totals
   from this seat: N + corrected A = **13 amended / 11 original** under the E6 wording condition in
   (2), **12 / 10** with my unconditional E6=1; BASE = **10 amended / 9 original**. The proof cites
   the amended row per the mission note.
2. **E6 condition, final form (with wonder-12's project-only sharpening, accepted).** E6=2 holds only
   for the opted-in selected-launch contract whose status renders evidence **source and grade
   together** — "configured by name / provider identity and authentication not checked", or
   "operator-asserted" — where project-only (repository-controlled) presence is never rendered
   observed-effective, known rejected/disabled/excluded state defeats acceptance, unresolved
   client trust/activation stays qualified unknown or scoped-asserted, and legacy §6 `FoundIn`
   (presence plus checkout-trust warning) is not upgraded. Any bare-satisfied variant keeps my E6=1.
   The dissent survives as this condition, not as a numerical dispute over the bounded candidate.
3. **Guards peer-confirmed.** The three Revision-1 guards were independently source-confirmed:
   closure name collision (astra-04's case; confirmed by astra-01/02/05/11/12, wonder-03, wonder-12
   and this seat; the lock format keys by `(kind, name)`, the current resolver by name alone);
   path-source print-only and the skill-lane secret-material scope sentence (astra-01, with
   astra-02/03/04/06/12/13). With the audit contract for manager discovery/surfacing still open,
   A-as-discovery-feature is E7=1 across seats; only the narrower inert-file/manual-adoption reading
   keeps any higher A-alone E7. The waived-secret counterexample (§2.3 raw stdio-args surfacing and
   §5.8 args/URL materialization are not sanitized by admission or waiver) is E7 governance debt in
   §2.3/§5.8/§9.1, already counted in every E7=1 above; it changes no score here.
4. **Final position.** Preferred design: bounded N (name-only skills; launch-scoped checking at the
   existing skill-install gate, opted-in; protected operator bindings/assertions in manager state;
   client-owned auth; "configured / auth not checked") plus optional corrected A (skill-root
   `agent-mcp.json` schema 1 surfaced on exact name match, full remediation tuple, distinct-name
   closure guard, path-source informational-only, explicit skill-lane secret-material scope), with
   csk native writes as a separately governed manager capability. Final vector from this seat:
   `[1,1,2,2,2,2*,1,2]` = 13 amended / 11 original (*E6 under the condition in (2); otherwise
   12/10), E8 cold = 1. BASE as written is beaten (10/9) and not elegant; capability (ALT-C) and
   manager-proxy (ALT-D) alternatives remain disqualified. No cross-host proof is claimed by this
   seat; row comparisons against the ivmbp N vector differ by at most the conditional E6 point.





