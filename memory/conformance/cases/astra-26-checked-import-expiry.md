# ASTRA26-07 — a checked publication expires without becoming current history

Status: judge-classified **R7-032 impl-bug (astra-22)** and
**R7-033 impl-bug (astra-23)**. Both behaviors verified: source `1f35727`,
package `f10c7ba`. Judge has verified R7-033; R7-032 review is pending. Original package
`0.2.1-draft` at `f31d58f`; package evaluator `8b9baf3` (runtime `f5fdd8b`),
source evaluator `512d006`. Targets S23/P07 publication currentness and P12 frozen
history, not a live issuer/network check.

## Clauses and two readings

Kernel §9.2 says a stale publication never returns as current. K-PUB-2 requires
both an admitted current-version check and an unexpired horizon for a current
import. K-EVAL-6 expires freshness at `now >= usable_until`; K-SNAP-1 keeps a
previous capture immutable history. These are separate requirements: preserving
an old capture does not authorize a new current-state claim after expiry.

1. **Presence of any successful check establishes currentness indefinitely.**
   The fresh and expired queries both have item/view currentness `current`;
   only the freshness field changes.
2. **Current-import qualification also depends on the horizon.** The fresh
   query is current; at expiry the newly queried copy is `last_received`, with
   stale freshness and its exact existing evidence/provenance. No replacement
   was learned, so this must not invent a `historical` replacement status.

Recommend reading 2. The package requires a non-current result at expiry;
`last_received` is the existing bounded-knowledge label. If that exact label
requires additional normative wording, close it explicitly rather than silently
keeping an expired copy current. Judge classification determines whether the
existing clause already fully fixes the label.

## Minimal witness and controls

[Complete fixture](astra-26-checked-import-expiry.vector.json) retains the three
P07 copies of one declaration, all with admitted current-version checks. Set:

- `usable_until = 2026-10-17T00:00:01Z`;
- first capture `now = 2026-10-17T00:00:00Z`;
- final query `now = 2026-10-17T00:00:01Z`.

The corpus, issuer confirmation, source checks, rights, knowledge cut, source
frontier and valid_at do not change. The first capture must stay fresh/current.
The final query must be stale and cannot call the import current. Support remains
present with one independent root; opposition stays not_found. There is no
revision, erasure, new root, external effect or rewrite of the earlier capture.

## Independent observations

Both current evaluators return `current` at `/result/currentness` and
`/result/items/0/currentness` despite returning stale freshness. The package
report has exactly those two semantic differences and two intended forbidden
predicate matches. The source report reproduces the same two field differences
and two forbidden matches. The fresh capture and all other expected fields pass.
Two independent implementations agreeing on the stale-current output does not
establish correctness against K-PUB-2 and kernel §9.2.

All eleven owned fixtures pass closed shape, initial-state/reference,
normalization and expected-forbidden checks. Evidence in the seat work directory:
`.temp/r7-astra-26/cases-structural-06.log`, `owned-cases-astra23-06.json` and
`owned-cases-astra22-04.json`, including implementation/input hashes. No canonical
vector or evaluator was edited. This is synthetic semantic evidence only.

## Judge disposition

Judge independently reproduced both failures and confirmed last_received as the
required existing label. R7-032 and R7-033 have separate implementation owners;
no package change or owner question is needed. Fix controls must cover before,
at and after expiry, missing check, known replacement, non-publication
freshness/currentness independence, immutable earlier capture and unchanged
evidence/origin. The original witness and first run remain unchanged while
those fixes are pending.

## Phase 2 round 12 — package fix verified

Package implementation `f10c7ba` passes the unchanged original 0.2.1 witness
exactly against pinned `f31d58f` schemas. All eleven owned fixtures pass that
run. The subsequent explicit migration to `0.2.2-draft` at `7e71765` changes only
semantic-profile stamps in these owned fixtures (none contains erase); all eleven
pass again with identical semantic expectations. Original inputs are retained
under seat `.temp/r7-astra-26/cases-0.2.1-phase2/` and in git.

Reviewed and ran the clause-derived controls: before/at/after horizon, missing
check, known replacement, stale ordinary-document currentness, unchanged
capture bytes/state, evidence qualifications and origin. All pass; ordinary
freshness is not used to demote a non-publication issuer sequence. The package
fix does not itself close R7-032 in the independent source implementation.

Exact reports: `owned-cases-astra23-07.json` (original package) and
`owned-cases-astra23-08.json` (0.2.2), plus `astra23-semantics-04.log` and
`astra23-controls-06.log`, all under seat `.temp/r7-astra-26/`. A prior mixed
version test attempt produced only two semantic_profile stamp differences after
the 0.2.2 pull; that attempt is retained as `astra23-semantics-03.log`, not a
semantic failure or passing evidence. The pinned and migrated reruns resolve it.

## Phase 2 round 13 — source fix and publication coverage verified

Source implementation `1f35727` passes ASTRA26-07 exactly under released 0.2.2
at `7e71765`, together with both original checked/unconfirmed currentness
fixtures. The source corpus is now nine owned passes and two explicit unsupported
delivery fixtures; there is no remaining owned source currentness failure.
Independently executed canonical S23 and reproduced its exact expected output,
separating a mirror report from a genuine unconfirmed publication.

Reviewed and ran the eight adapter controls: before/at/after expiry, absent and
unverified checks, known replacement, unchanged ordinary-source currentness,
frozen earlier output, evidence and root identity all pass. No original expected
value was changed. Evidence: seat `.temp/r7-astra-26/owned-cases-astra22-05.json`,
`s23-astra22-01.json` and `astra22-adapter-controls-04.log`, with exact package,
implementation and input identities. R7-032 fix evidence has been supplied for
independent judge closure; the package counterpart R7-033 has already received
the judge's fixed-at-f10c7ba verification.
