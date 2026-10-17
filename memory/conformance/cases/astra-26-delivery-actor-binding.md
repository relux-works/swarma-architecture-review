# ASTRA26-10 — a prepared view is not another actor's delivery authority

Status: judge-classified **R7-046 impl-bug**, owner astra-23; fixed at `3ce8ee3`, independently verified by this seat and the judge. Package `0.2.2-draft` at
`7e71765`; package evaluator `a016781`; source evaluator `5d079be`.
This is a synthetic boundary trace, not an external send.

## Clauses and competing readings

K-AUTH-1 evaluates grants for the principal, space, audience, purpose and right.
K-API-2 validates policy and actor rights before subsequent operation checks.
K-PUB-1 requires current read/use/forward authority for a prepared delivery;
K-SNAP-1 says a saved view grants no standing permission and the fixture boundary
refuses rather than silently substituting context.

1. **The saved operation index is sufficient authority.** Recover the original
   query principal and use its grants; the authenticated deliver actor is ignored.
2. **Current authority belongs to the authenticated actor and saved binding.**
   A different actor with no grants or delegation cannot reuse the owner's
   prepared view. Refuse not_authorized; the owner's valid delivery still works.

Recommend reading 2. A capture index is an internal fixture binding, not a
bearer grant. This witness needs no decision about how a future delegated
publisher API would work: the foreign actor has no authority of any kind here.

## Minimal witness and controls

The [complete fixture](astra-26-delivery-actor-binding.vector.json) extends
canonical P12 with exactly one request between its capture and valid delivery:

1. Capture an audience projection for subj:h1.
2. Request delivery as principal:ungranted-deliverer, which has no policy grant,
   representation or other delegation. Expect not_authorized, retryable false.
3. Deliver the same saved binding as subj:h1. Expect the existing delivered receipt.
4. Revoke subj:h1's read right as policy owner. Expect the existing revoke receipt.
5. Deliver again as subj:h1. Expect disclosure_revoked.

The captured value stays immutable; the final current query has no selected
item after revocation. The corpus, erased refs, dirty state and simulated external
effects are unchanged. The valid third step rules out a reject-all repair;
the fifth step preserves current-right enforcement. Normalization moves the
existing success-handle paths by one index and does not normalize the refusal.

## Independent observations

Both evaluators receive only state, operations and query before comparison.
Source 5d079be passes the entire trace exactly. Package a016781 returns a
`delivered` receipt for the ungranted actor at `/operation_results/1`, instead of
not_authorized. The other four operations, final view and postconditions match.
The explicit forbidden receipt predicate detects the unauthorized success.

All fifteen owned fixtures pass structural/reference/normalization/forbidden
checks. Current owned totals: source 15 pass / 0 fail / 0 unsupported; package
13 pass / 2 fail / 0 unsupported, the other failure being ASTRA26-09.
First actual results and implementation/input hashes are retained in seat
`.temp/r7-astra-26/owned-cases-astra22-08.json` and
`owned-cases-astra23-10.json`, with their logs and `cases-structural-09.log`.
No canonical fixture, runtime implementation or existing expected result changed.

Source boundary review also independently verified canonical P06/P12, both
selected/excluded forwarding cases and all eight boundary controls, including
actor/audience/purpose binding, owner-only revoke, each selected right, expiry,
erasure/restore fencing and frozen capture values. Those controls corroborate
the contract; they do not define the expected verdict by implementation consensus.

## Judge disposition

Judge event `$g9ovpw6DYL8Zlps7PFLbTJ48DFO_AnuBgVT9hrvJ5tA` independently
reproduces the unauthorized receipt and exact source pass, classifying R7-046 as
a package implementation bug. Required outcome is not_authorized without state
or external effects. The finding is deliberately limited to the ungranted actor;
it does not invent or decide a future delegated publisher API.

Preserve the first failure before correction. Closure requires the rightful
actor success, later selected revocation refusal, immutable binding and exact
audience/purpose/index controls. No package change or owner question is needed.

## Phase 2 round 19 — actor-bound delivery correction verified

Package `3ce8ee3` compares the authenticated deliver actor to the saved query
principal before using the binding. The exact original 0.2.2 fixture and the
explicitly migrated 0.2.3 fixture both pass. All fifteen owned fixtures pass on
each profile; no earlier expected semantic answer was changed.

Reviewed and ran the actor-binding and selected-delivery product controls.
Wrong actor, audience, purpose and capture index each return the exact
not_authorized refusal while preserving the complete state, captures, view
bindings and dirty-since map. The same fixture's rightful actor succeeds, its
later selected revocation refuses, and the original captured bytes remain fixed.
Selected read/use/forward, erasure-fence and expiry refusals also remain passing.
The independent first failure `5416283` and this seat's original reports remain.

Exact evidence in seat `.temp/r7-astra-26/`: `owned-cases-astra23-14.json`
(original 0.2.2), `owned-cases-astra23-15.json` (0.2.3), matching logs and
`astra23-delivery-controls-01.log`. Judge closure is requested separately; this
synthetic result makes no live delivery or protected-deployment claim.

## Judge closure

Judge event `$yjV0b8Np4X4WOpR5twcN5bIDbTo9nRpBvX9zWG8QBkg` closes R7-046
at `3ce8ee3`. Independent byte-pinned 0.2.2 and current 0.2.3 actor vectors and
controls pass, with complete state/binding preservation and rightful/revoked
neighbors. The judge's current package run at `4af0360` passes 57/57 canonical
and 46/46 supplemental semantic inputs. First failure `5416283` remains;
new authority-successor probes and deployment qualification remain separate.
