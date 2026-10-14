# Verdict: wonder-03 (alternatives hunter, adversarial pass, second independent five)

Seat: `wonder-03` (ivmbp, Muse Wonder full 1.0). Lens: independent second
alternatives hunt against `wonder-01`'s row. Independence: my scores were frozen
and posted (room `rounds`, `$ucKJ71qB4RIXv_eoBGHzHbX_F7RdS2m3zzQyyxNkQsQ`) before
any first-five verdict file, findings file or topic body was opened; only topic
titles were listed, as the mission requires. Sources: curator-spec `a9c03be`,
curator `5234cf3`, this repository at `b5e7dab`, all read locally (pulls blocked
by the sandbox: SSH/uid). Status: round-1 position of this seat; adversarial
attacks outstanding in `alt-skill-ships-declaration`
(`$LhiQrl1xcV4aSfL927TfTRhlk3xPcBmd9K66MLUnzPQ`).

## Independent pre-reading scores (frozen)

Designs I constructed before reading the first five: BASE as written; ALT-A
(skills stay name-only; identity/alias/provisioning in one operator-owned local
binding; provisioning only from operator roots; opaque providers by labelled
assertion; stated metadata bound); ALT-B (skill-level package requirement shaped
exactly like environments §2 `requires.mcp`, identity = lock member); ALT-E
(skill snapshot ships declarations, snapshot is the pin); ALT-C (capability/tool
requirements, strong verification form); ALT-D (manager-side gateway).

| Design | E1 | E2 | E3 (amended [original]) | E4 | E5 | E6 | E7 | E8 | Total |
|---|---|---|---|---|---|---|---|---|---|
| BASE as written | 1 | 1 | 1 [0] | 1 | 1 | 1 | 1 | 1 | 8 |
| ALT-A (mine) | 1 | 2 | 2 [1] | 2 | 2 | 2 | 1 | 1 | 13 |
| ALT-B (mine) | 1 | 1 | 2 [1] | 1 | 1 | 2 | 2 | 1 | 11 |
| ALT-E (mine) | 1 | 1 | 2 [1] | 1 | 1 | 1 | 1 | 2 | 10 |
| ALT-C strong (mine) | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 4 |
| ALT-D (mine) | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 4 |

BASE at 8 (all ones) matched wonder-01/wonder-02 exactly once their verdicts
were read. My ALT-A converged with astra-01's `alt-names-local-evidence` (N)
independently; my ALT-E converged in direction with wonder-01's shipped
declaration, but wonder-01's form is strictly better (recommendation with no
authority, adoption only through existing profile/csk lanes — mine provisioned
from the shipped declaration under consent, which is the transitive-authority
hole the first five correctly closed).

## Post-reading adversarial scores

| Design | E1 | E2 | E3 (amended [original]) | E4 | E5 | E6 | E7 | E8 | Total |
|---|---|---|---|---|---|---|---|---|---|
| BASE as written | 1 | 1 | 1 [0] | 1 | 1 | 1 | 1 | 1 | 8 |
| Composite N+A (D1–D6 round-3 sketch) | 1 | 1 | 2 [0] | 2 | 2 | 2 | 1 | 1 | 12 |
| A standalone (canonical-A) | 2 | 2 | 2 [0] | 1 | 2 | 1 | 1 | 1 | 12 |
| Capability-tools, weak/label variant | 1 | 1 | 2 [0] | 1 | 1 | 1 | 1 | 1 | 9 |
| Gateway | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 4 |

Deltas from the first five, with reasons:

- **Composite E2**: I concede 1 (was 2 in my pre-reading ALT-A). Wonder-02's
  mechanical test is right: launch-scoped evidence and the binding lifecycle are
  new checker machinery; provisioning reuse does not cover them.
- **Composite E4=2** (against wonder-02/astra-13's cap at 1): the anchor is
  "can satisfy without a client change"; a labelled scoped assertion achieves
  that for every capable-but-opaque zoo member. Evidence grade belongs to E6,
  where asserted never renders as observed. Bounds: an assertion never rescues
  a known-unsupported (pi), disabled, excluded or shadowed selector.
- **Composite E6=2 is wording-conditional** (wonder-11/12 condition, adopted):
  status normatively renders evidence source and grade together, as
  "configured by name / provider identity and authentication not checked" or
  "operator-asserted", and a project-only entry is never rendered as
  observed-effective availability (legacy §6 keeps its configured-name result
  plus checkout-trust warning). Any variant rendering a bare "satisfied" from
  name presence earns E6=1 from this seat too.
- **Composite E8=1** (first five: 2 on the already-configured reading). The
  goal's common case is a skill whose server the operator does not yet have:
  candidate notice → hand-author `requires.mcp` (full adoption tuple) →
  profile install → per-client auth. That is expert authoring plus several
  actions. I report the already-configured reading (E8=2, total 13) alongside;
  the difference is one point, inside proof tolerance either way.
- **Original E3** for every native-inspecting design, including the composite:
  0 under the literal zero anchor, because `internal/mcp` reads whole mixed
  files (`os.ReadFile` + unmarshal, mcp.go:240-288) that may contain credential
  literals. Under the amended row the composite earns 2 only because D2b states
  the bound; note D2b's command-name exception still surfaces one foreign byte
  string (the existing §6 PATH warning prints the configured command,
  mcp.go:142-145) — accepted as bounded, flagged for the normative text.

## Preferred design

**Composite N+A as the target, A standalone as the shippable first slice** —
the same tie-break as wonder-01, reached independently: A's E4=1 is a real
exclusion of opaque zoo members and the operator's goal names the zoo first.
The rubric's "elegant" test (highest total, no 0 in E3/E6) is therefore
applied among designs meeting the whole goal, where the composite leads.
Score correction recorded during the wait rounds: A-standalone E7 was first
posted as 2 (total 13) conditional on the skill-lane secret-material scope
sentence; the REQUIRED `context-secret-material` class binds context/MCP
snapshots under profile audit (manager §7:1167–1171; environments §9.1),
not the ordinary skill lane, so that sentence with stated
severity/waiver/admission behavior is owed normative work and
A-discovery scores E7=1 (total 12) — the same correction astra-02/03/04/12/13
recorded. A purely inert shipped file with manual adoption is a narrower
variant; preference is unchanged either way.

## New attacks filed against the composite (round-2 resolution)

1. **Stale adoption — conceded in mandatory form.** D1's candidate notice fires
   only on an unsatisfied requirement, so a skill update shipping a changed
   declaration never resurfaces after adoption. Filed as an E6 gap; refuted by
   astra-04 (`$l6t7kxttXHkQRnMJf_ejN3XIgbjA2tzetQB5v3AOwdI`): §1.3 makes the
   adopted profile independently pinned and forbids implicit re-resolution, so
   named satisfaction stays truthful without a staleness notice. Surviving
   residue: retire the headline "skill version pins declaration version" for
   "candidate bytes are pinned by the skill snapshot; adoption is an
   independent operator pin"; an upgrade notice is permissible optional
   guidance, separately counted, never required. No finding filed.
2. **Remediation tuple — confirmed** by astra-04 (distinct seat). Round-3
   remediation must print (canonical git, exact revision,
   directory-or-`.`, declaration name); without `directory`, adopting a
   directory-selected skill's declaration resolves the repo root and fails
   `mcp_declaration_invalid` (core §4.4 directory; environments §2
   `directory` on `requires` entries). Route-aware corollary (wonder-11): for
   a path-sourced skill the notice must not print a profile route at all.
3. **Unnamed check operation in the profile lane — confirmed** as real
   contract debt by astra-04. Today `mcp.Verify` runs only at project/global
   skill install (`internal/install/install.go:1595`); profile install checks
   no skill MCP requirement. Minimum accepted shape: an explicitly opted-in
   scoped-check contract defining how its invocation selects launch context,
   legacy install semantics retained, no silently rejecting profile-install
   gate. Until the invocation is named in normative text, composite E7=1 and
   E2=1 stand on this ground alone.
4. **Joint-closure name collision (peer-raised, independently verified).**
   The resolver keys kinds by name (`contextresolve.go:316-318`), `add()`
   silently coerces a second kind for a known name (409–414), and `mcpsOf`
   loads only KindMCP members (`managed.go:205-226`); the lock format is keyed
   (kind, name) (`contextlock.go:178-181`), so this is resolver behavior, not
   format impossibility. Revision-1 bound: a shipped declaration's name must
   be distinct from every skill-member name in the target closure, including
   the shipping skill's own name when it equals the server name; on collision
   the candidate notice says deferred/rename-required and prints no
   unexecutable remediation. No automatic rename or resolver change.

## Smallest set of changes to the base that reaches the preferred design

1. Delete `server` (package/endpoint identity), the identity conjunct, and the
   declaration auth class from the skill surface; keep the base's correct
   separations (require ≠ provision; no health checks; status never claims
   connected/authenticated).
2. Move alias/assertion into one protected operator binding record homed in a
   governed manager-config successor (plus marker successor for per
   (requirement, target, launch) evidence), never in a checkout; enumerate
   exact requirement identities; asserted never renders as observed.
3. Scope satisfaction evidence to the selected launch; name the checking
   operation per lane (attack 3); old markers read as legacy native presence.
4. Add the MAY clause for skill-root `agent-mcp.json` (schema 1 unmodified):
   metadata-only, route-aware candidate notice on exact name match, full
   remediation tuple (attack 2), distinct-name joint-closure guard (attack 4),
   secret-material scan scope at skill install, MUST-warn on malformed.
   Candidate bytes are pinned by the snapshot; adoption is an independent
   operator pin (attack 1 residue). Provisioning only via operator
   selection into profiles (§2.2/§5.8, allowlist/signers/strict audit re-run)
   or the separately governed csk native writer under exact-plan consent;
   native writers refuse managed-home destinations and reserved channel files.
5. State the bounded foreign-byte handling rule (names, disabled state and
   stdio command name compared in memory only; raw argv/URL/env/header bytes
   never persisted, logged or surfaced) and add the §2.3 `url` column so
   credential-routing consent is informed. Admission is not safe-display
   proof: a §9.1-scoped waiver can clear a secret-material finding in
   declaration args while §2.3 still prints args raw (today's stdout path;
   HTTP has no URL column yet, but §5.8 serializers already copy URL literals
   into generated files, and the new `url` column must inherit the same
   withholding rule), so known or waived
   sensitive argv/URL must be withheld from surfacing/consent display (and if
   withholding prevents meaningful exact-plan review, the write stays
   unapproved), and a credential-bearing declaration must not be provisioned
   through serializers that copy args/url into generated files
   (`contextmaterialize/mcp.go` claude/openCode/codex shapes) under this
   feature's no-secret claim — governed §2.3/§9.1 text, already inside the
   E7=1 debt; delegating to an unmodified legacy lane cannot inherit the
   stronger claim.
6. Governance: CIP + decision record + conformance vectors (incl. directory
   adoption, same-name skill/mcp collision, per-launch completeness, assertion
   invalidation, secret-bearing foreign bytes never in output). No
   skill-manifest, agent-mcp or Skillfile schema changes.

## Proof statement (this seat)

Two independent fives now score the composite within one point on every row
(first five [1,1,2,2,2,2,1,2]=13; this seat [1,1,2,2,2,2,1,1]=12; only E8's
common-case reading differs), with BASE refuted as already-elegant at 8
(vs 5–7 from the astra seats, E1/E7 within one). Under the amended E3 row the
composite has no E3/E6 zero and is the highest-scoring design that meets the
whole goal; under the original E3 row no native-inspecting design passes the
gate, and that limitation stands. E7=1 everywhere means "elegant" is proved at
sketch fidelity, not as governed text. Attacks 1–4 above were answered in
round 2 without score movement (one concession, two confirmations, one
verified peer bound). From this seat the two-independent-fives condition is
met; the mini third pass (wonder-11 at [1,1,2,2,2,1,1,2]=12, E6 dissent within
tolerance) independently bounds the same design.
