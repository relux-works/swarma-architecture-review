# ASTRA26-08 — an excluded record cannot veto another item's delivery

Status: judge-classified **R7-034 impl-bug**, owner astra-23; behavior verified
at `f10c7ba`, judge closure pending. Original package
`0.2.1-draft` at `f31d58f`; observed in package evaluator `8b9baf3` (runtime
`f5fdd8b`). Targets P06/P12 exact prepared-item delivery and P15 exclusion.

## Clauses and two readings

K-PUB-1 rechecks current read/use/forward rights using the prepared view's exact
selected items. K-SNAP-1 keeps that binding and refuses rather than silently
substituting a context. K-PROJ-2 removes exact excluded items from selection,
without changing their issuer sequence. Read/use permission and forward
permission are distinct under K-AUTH-1.

1. **Recheck every readable assertion with the same schema.** An excluded
   assertion lacking forward permission vetoes delivery of a different item.
2. **Recheck the exact prepared item binding and its required dependencies.**
   The excluded unrelated assertion is not being forwarded and has no content
   or evidence dependency into the selected item. Its forward permission cannot
   veto the selected item's otherwise authorized delivery.

Recommend reading 2, already explicit in K-PUB-1. This is an implementation
finding if the judge confirms that interpretation; no wider forwarding authority
or architecture change is proposed.

## Minimal witness

[Complete fixture](astra-26-excluded-forward-right.vector.json) starts from P06.
There are two independent multi-valued self-declarations under the same schema:
`rec:interest` (gardening) and `rec:unselected-interest` (pottery). The audience
rule excludes the second exact reference. Both are readable with metadata;
only the selected first assertion has a forward grant for the requested public
purpose. Both have explicit direct lineage and no logical/content dependency.

The sequence is capture -> deliver -> revoke selected-principal forward right ->
deliver again. The first delivery must succeed, and the later one must return
`disclosure_revoked`. Capture/final views each contain only gardening. Both
records remain admitted; no erasure, revision or simulated external effect occurs.

The [nearby control](astra-26-excluded-forward-right-control.vector.json) adds
only forward permission to the excluded record. It has exactly the same expected
outputs. Since that record is not part of the prepared delivery, this extra grant
must not change the result. The post-revocation refusal also prevents a permissive
implementation from satisfying the positive control by ignoring current rights.

## Independent observation and limits

The package evaluator returns `disclosure_revoked` on the first delivery in the
minimal witness, while the nearby control passes exactly. Its implementation
checks all visible same-schema assertions for forward rights after recovering the
selected binding, including the excluded assertion. The minimal witness's first
capture, final capture, unchanged inventory and later revocation refusal all
match; only the required first receipt is replaced by a refusal. The source
adapter at `512d006` explicitly reports both fixtures unsupported for deliver/
revoke. That is no pass or corroborating behavior claim.

Both new fixtures pass closed grammar, initial references, normalization and
expected forbidden checks. Evidence in seat `.temp/r7-astra-26/`:
`cases-structural-06.log`, `owned-cases-astra23-06.json` and
`owned-cases-astra22-04.json`, with exact differences and implementation/input
hashes. A fixture-author draft addressed projection rules through a nonexistent
`ref` field and failed with KeyError before this vector was written; it was
corrected to the documented id/version pair. No product or expected-output
change was used to hide that authoring failure. No live publication is tested.

## Judge disposition

Judge independently validated both fixtures and reproduced the first delivery
refusal with the valid extra-grant control and later selected-right refusal.
R7-034 belongs to the package implementation; no package change is required.
Closure must narrow the unrelated-assertion check while preserving every current
selected-item read/use/forward, owner-release, freshness and erasure check. The
source's unsupported delivery remains a coverage gap, not a second observed bug.

## Phase 2 round 12 — exact selected binding verified

Implementation `f10c7ba` checks forward authorization only for the protected
selected references after performing the existing fresh read/disclosure checks.
Both original 0.2.1 fixtures now pass exactly, including first delivery, excluded
item omission, unchanged record inventory and later selected-right revocation.
All eleven owned fixtures pass after the explicit profile-only 0.2.2 migration.

Reviewed and ran neighboring controls: removing selected read, use or forward
after capture refuses; selected erasure fencing refuses; horizon expiry refuses
publication_stale; each refusal preserves stored state. Joint-owner release and
revocation controls remain passing. No expected content or right was relaxed.
Exact old/new package reports and control logs are
`owned-cases-astra23-07.json`, `owned-cases-astra23-08.json`,
`astra23-semantics-04.log` and `astra23-controls-06.log` in seat
`.temp/r7-astra-26/`. The source delivery path remains separately unsupported
in its last pinned report. No deployment claim follows from these traces.
