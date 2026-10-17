# ASTRA26-02 — a fresh imported copy is not necessarily the issuer's current version

Status: submitted for classification; source-contract case, package not yet
available. Seat: astra-26. Baseline: `daf285d` (kernel v0.2).

## Clauses

- Kernel §6.3 distinguishes valid time, last confirmation and `usable_until`;
  the horizon says when a consumer needs refresh, never truth or negation.
- Kernel §9.2 requires an importer to use known replacements, `usable_until`
  and current-version checks with the issuer; without them it knows only the
  last state received. A stale publication never returns as current.
- Kernel §§1 and 6.4 bind semantic results to explicit inputs and cuts; an old
  artifact remains history and cannot silently claim to be "now".

## Two readings

1. **The unexpired horizon suffices for imported currentness.** Revision 1 is
   fresh and no newer local revision exists, so it can be displayed as the
   issuer's current statement until its horizon expires. A current-version
   check is needed only after that expiry.
2. **Freshness and current-version knowledge are distinct.** Revision 1 can
   remain fresh under its consumer horizon while its issuer-current status is
   only last-received. An unexpired consumer horizon does not prove that the
   issuer has not replaced or withdrawn it.

## Minimal separating input

This is source-level notation, to be translated into the package's actual
fixture format. All data is synthetic.

```json
{
  "imported_publication": {
    "id": "pub-synthetic-1", "revision": 1,
    "confirmed_at": "2026-10-01T00:00:00Z",
    "usable_until": "2026-10-08T00:00:00Z",
    "statement": {"availability": "available"}
  },
  "query_cut": "2026-10-03T00:00:00Z",
  "known_replacements": [],
  "issuer_current_version_check": "unavailable",
  "requested_claim": "issuer_current"
}
```

Two issuer histories are indistinguishable to this importer: in H1 the issuer
still publishes revision 1; in H2 it replaced revision 1 with revision 2 on
October 2 and the importer has not received that event. Neither history is an
extra secret input that the kernel is expected to discover. The normalized
local query input is identical, so it must give the same bounded knowledge
claim in both histories.

## Separating outputs

| Observable | Reading 1 | Reading 2 |
| --- | --- | --- |
| Consumer freshness | `fresh` | `fresh` |
| Currentness claim | Revision 1 is issuer-current until October 8 | Revision 1 is the last received state; issuer-current unconfirmed |
| Negative evidence about availability | None | None |
| Implicit network/effect authority | None | None |

Exact currentness labels are for the package to close. A response may refuse
the stronger currentness request or return the copy with an explicit bounded
qualification; it must not represent a failed source check as an empty source.

## Recommendation and controls

Recommend reading 2. A consumer-selected horizon controls tolerance for refresh;
it is not an issuer promise that no replacement exists. Require the package to
define precisely what an importer may claim when a version check is absent,
failed or older than the query's declared cut, and how that differs from expiry.
This does not require the kernel to perform network checks: checked source
evidence can enter through the adapter as part of the normalized input.

Positive control: an admitted issuer version check applicable to the query's
declared cut reports revision 1 current; the currentness claim may then be made
at that cut. Negative controls: a known replacement disqualifies revision 1
despite its unexpired horizon, and a passed horizon marks it stale without
creating contrary evidence or deleting history. A frozen copy remains history.

No executable-package failure is claimed. The judge should classify whether
§9.2 already selects reading 2 or the relation to §6.3 needs an owner question.
