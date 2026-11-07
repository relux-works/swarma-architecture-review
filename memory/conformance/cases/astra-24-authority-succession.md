# ASTRA24-10: a canonical receipt must also succeed the replaced receipt

Status: judge-classified R7-047 (source), R7-048 (package), and R7-049
(package refusal mapping). Source repair `4772258` independently verified;
package runtime repair `942bdee` independently verified. Mapping release
`ef02647` independently checked; formal judge closures remain separate.
Owner: astra-24. Package `0.2.3-draft` at `23290b3`; first execution checkout
`d077064`. Both evaluators accept the forbidden replacement variants below.
No architecture change is proposed.

## Contract and competing readings

K-REV-3 requires an authoritative replacement's new receipt to succeed its prior
receipt. Canonical status and issuer identity alone establish a receipted event,
not its precedence over the event being replaced. K-REV-1 requires an exact
current head and atomic immutable replacement. Kernel section 5.3 forbids memory
arrival or revision order from overriding the authority's own order.

The convenient reading checks the current target and the new receipt's canonical
status independently, then accepts any such replacement. The required reading
also checks a strict predecessor path from the new receipt to the old receipt
before storing either proposed record. A memory replacement cannot manufacture
an authority edge. Incomparable canonical events remain separately importable
through plain admission; that exception does not authorize a replacement.

## Minimal separating input

Start from canonical B01 without changing actor, grants, review allowances,
lineage facts, retention context, current head, replacement values or CAS token.
There is one admitted decision d1/r1, an admitted canonical receipt r2, and one
registered dependent. The operation replaces d1 with d2/r2.

- Ordered positive: retain `r2.predecessors = [r1]`; replacement must succeed.
- Incomparable negative: change only `r2.predecessors = []`; replacement must
  refuse atomically because r2 does not succeed r1.
- Reused-receipt negative: keep the original receipt graph but cite r1 in both
  proposed replacement and revision; a receipt does not strictly succeed itself.

The complete input triples are in
[astra-24-authority-succession.input.json](astra-24-authority-succession.input.json).
Their input bundle SHA-256 is
`5dcc51600aaed1a2253c9c8ebbde951556521ccea982a55fa3f60d055965ecd4`.
Closed input grammar and initial-state reference checks pass for all three.
These are contract probes, not falsely reported exact-output vector passes.

## Observed results

Both independent evaluators accept all three variants at `d077064`:

| Observable | Ordered positive | Both forbidden variants | Required negative invariant |
| --- | --- | --- | --- |
| Operation result | revised receipt | revised receipt | typed refusal |
| Stored records | 7 records | 7 records | 5 records |
| Memory cut | 102 | 102 | 100 |
| Dirty dependent | present | present | absent |
| Stored idempotency entries | 1 entry | 1 entry | 0 entries |

The negative probes therefore reach admission and commit observable forbidden
state; they are not parser/setup failures. Full operation results, inventories,
state-equality checks, input hash and every evaluator module hash are preserved
in [astra-24-authority-succession.first.json](astra-24-authority-succession.first.json).
The ordered positive prevents an unconditional rejection from satisfying this
case. No query after an invalid new cut is used as the failure witness.

## Refusal mapping requiring adjudication

The rejection invariant is explicit. Its exact closed wire code is not:
K-REF-1 describes `authority_receipt_required` as a missing canonical receipt,
whereas these canonical receipts exist but lack required succession.
`version_conflict` is a current-head mismatch, which is absent here.
`invalid_reference` and `invalid_domain_value` describe other broad conditions.

Recommend the same atomic refusal for unrelated and reused receipts, with
`authority_receipt_required` if the judge/editor confirm that a required
qualifying successor receipt is considered missing. Do not present that choice
as already normative. Request a classification of both accepted-write failures
and the code mapping; then add exact package-format vectors with the adjudicated
code. This is a narrow package-contract clarification, not an owner product or
architecture question. Existing CAS head-selection fixes remain separately valid.

## Round 25 adjudicated exact vectors

The judge's decision assigns
R7-047/R7-048 to the two implementation gaps and R7-049 to the missing wire-code
mapping. The required negative result is `authority_receipt_required`,
`retryable=false`, including an incomparable, prior or identical receipt. A
current-head mismatch remains `version_conflict`; no architecture decision is
needed. The editor will publish this mapping in a normal package release.

Five 0.2.3 package-format vectors now express that explicit adjudication:

| Vector | Required result | Source at d990131 | Package at d990131 |
| --- | --- | --- | --- |
| ASTRA24-10 | Incomparable successor refuses atomically | forbidden receipt and writes | forbidden receipt and writes |
| ASTRA24-10-SAME | Identical receipt refuses atomically | forbidden receipt and writes | forbidden receipt and writes |
| ASTRA24-10-PRIOR | Prior canonical receipt refuses atomically | forbidden receipt and writes | forbidden receipt and writes |
| ASTRA24-10-CONTROL | Direct successor admits replacement | pass | pass |
| ASTRA24-10-TRANSITIVE | Transitive successor admits; d2 becomes current | write passes; currentness fails | pass |

Negative vectors capture cut 100 before the attempt and query the same cut
afterwards. Their independently derived expected view is the original d1/r1,
with no review or dirty state; inventory and forbidden predicates separately
catch committed writes. Final historical-view equality alone is not atomicity
evidence. The original three first inputs/reports are unchanged. The new prior
neighbor reverses the receipt edge. The transitive positive adds a fully admitted,
readable intermediate receipt, with complete direct lineage, between r1 and r2;
there is deliberately no assertion for that intermediate authority event.

The latter exposes a distinct source projection boundary: replacement succeeds
correctly, but the final view returns both old and new decisions as ambiguous.
Source adapter translation retains only direct predecessor receipts that already
have assertion candidates, dropping the intermediate receipt path. K-REV-3
requires transitive receipt order. Package passes the exact full result. The
source report records eight field/shape differences plus the intended forbidden
old-value predicate. This is submitted separately for judge disposition; a
read-only isolation is the next unit, not a guessed extra ledger classification.

All eighteen owned vectors pass closed shape, state references, normalization,
inventory accounting and intended wrong-result plants in
`.temp/case-vectors-validate-25.log`. Earlier logs 23/24 rejected symbolic handle
names and object-valued forbidden predicates in the local draft; those are
fixture-format errors corrected before any evaluator execution, not divergences.
First exact runs: `.temp/astra22-owned-cases-28.json` = 14 pass / 4 fail;
`.temp/astra23-owned-cases-18.json` = 15 pass / 3 fail. All thirteen previous
fixture hashes and behavior are unchanged. New exact fixture hashes follow.

- `astra-24-authority-succession-control.vector.json`: `d05fda2d702025202849c20cb5fce74fd12432a63395ac86e56dd30a3284365c`.
- `astra-24-authority-succession-prior.vector.json`: `33645742036e006e1e43b0d4e8f5c0913601753a10a8768223f07e4aad0921e3`.
- `astra-24-authority-succession-same.vector.json`: `66dd7cf2b4886d510dd2dde689d928b934d984ff589861cc62d5343a3c330ced`.
- `astra-24-authority-succession-transitive.vector.json`: `26c83be7829eb22c8e72c5e10a6be7f11669547df8424e60db5e88435d137b25`.
- `astra-24-authority-succession.vector.json`: `34b896ca9e27e996fa70d8e7f44c66d96178c15a04b190f08072c30af30365c1`.

## Round 27 profile migration to 0.2.4

Current exact fixtures explicitly name `0.2.4-draft` from release `ef02647`.
Only expected-view `semantic_profile` values changed; initial state, operations,
queries and behavioral expectations are byte-equivalent after that declared
normalization. All twenty owned fixtures pass structural and intended forbidden
controls (log27). `.temp/astra24-profile-024-migration.json` records old/new hashes
and every changed path. Historical hashes and first reports remain unchanged.

## Round 27 source strict-succession repair verified

At checkout `4772258`, all three exact negative fixtures now refuse with the
prescribed code and unchanged inventory/dirty state. Direct successor passes;
the transitive write also succeeds, while its final projection still fails the
separate R7-051 contract. Four native succession groups pass full-state atomic
replace/correct refusals, direct/transitive positives with event array order
reversed, exact replay before CAS, stale new-key rejection, and ordinary
incomparable canonical plain import with no revision or dirty effect.

The new 0.2.4 canonical B01 has exact operation results and postconditions in
source, including four same-key refusals, direct/transitive successes, replay
and separate CAS; only seven final projection differences remain under R7-051.
This seat recommends R7-047 closure after judge review without claiming B01
fully passes. Package still accepts the three exact forbidden variants.
Evidence: source30/package20, `astra22-succession-controls-01.log`, and the
separate `astra22-b01-024-first.json` / `astra23-b01-024-first.json` reports.

Release verification reads K-REV-3/K-REF-1 and confirms exactly B01 changes among
65 canonical vectors after profile normalization; the decisions pilot stays
byte-identical. All 94 JSON artifacts, 52 clauses and 33 intended checker plants
pass. This is independent release/contract verification, not a full runtime or
deterministic regeneration claim. R7-049 judge closure remains separate.

## Round 28 package strict-succession repair verified

At exact checkout `942bdee`, all twenty unchanged owned 0.2.4 vectors pass.
The full expanded canonical B01 report has zero exact field differences and
zero harness/normalization/forbidden failures. Three focused native methods
pass: eight replace/correct-by-receipt-class atomic negatives with same-key
valid recovery; direct/transitive successors, original replay after the next
head, distinct CAS and ordinary incomparable import; and the prior authority
slot CAS/remaining-head regression. Full state, dirty causes and protected
capture/binding preservation are asserted where applicable.

Evidence: `.temp/astra23-owned-cases-21.json`,
`.temp/astra23-b01-024-fixed.json`, and
`.temp/astra23-succession-controls-01.log`. Every fixture hash matches the prior
run; first native `47c0205`, exact `0641033`, and new-release `e689cf2` failures
remain intact. R7-048 closure is recommended after judge review. This does not
close the source projection or other-seat retention-deadline contract.

Round 29 additionally verifies source projection correction `427fed5`: the full
ASTRA24-10-TRANSITIVE result and expanded canonical 0.2.4 B01 now pass exactly,
as do all twenty owned source fixtures. The separate R7-051 evidence and focused
limits are recorded in [ASTRA24-11](astra-24-receipt-only-order.md). No input or
behavioral expectation changed to obtain this result.
