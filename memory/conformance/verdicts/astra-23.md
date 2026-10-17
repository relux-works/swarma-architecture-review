# astra-23 — package implementer verdict

**PARK accepted: 2026-10-17 19:12Z. R7 score: 2/2.** D-009 conformance is
independently closed at `75c13d2`, with the quiet round recorded at `715d7a7`.
Convener event `$wTjjxPAdO1lPYyIX7BgMky5ptiS0vPzX6HGGgE99C0U` authorizes
this final handoff. [Park note](../parked/astra-23.md) records completion and limits.

Implementation remains derived from `memory/spec/` only. No other evaluator
implementation, source design, decision document or reviewer input was read for
this correction. D-009 is implemented through released K-REV-3 in package
**0.2.6-draft**, `77b951eb86d5ba9198921d058930884918a39942`.
Package runtime: `5897520b6ca9fb4772d728fecf4a33a392b1905d`; audit-format
clarification: `fddb403`. Editor acceptance `1e222f6` and judge closure
`75c13d229f036ffe1639096cd9ff89926bad73b8` independently verify the result.

| Evidence | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Current 0.2.6 canonical semantic | 66 | 0 | 0 |
| Historical 0.2.5 supplemental semantic | 68 | 0 | 0 |
| Current canonical deployment | 0 | 0 | 8 |
| Historical supplemental deployment | 0 | 0 | 1 |

The supplemental run uses the current runtime with exact frozen 0.2.5 grammar
`6a04e8c` and unchanged author-owned inputs. It is a separate regression result,
not additional canonical 0.2.6 coverage. No fixture or behavioral oracle migrated.

The shared authority relation now restricts canonical events to their protected
policy issuer before predecessor traversal. Assertion-free intermediates count;
foreign paths do not contract and foreign branches cannot cancel an all-H path.
Projection currentness, revision CAS head and strict replacement succession use
this same relation. Mixed-only succession refuses authority_receipt_required/false
without mutation; ordinary import remains admissible and yields ambiguity.
Authorized exact replay and version_conflict retain their prior meanings.

[The immutable first](../impl-astra-23/RELEASE-0.2.6-FIRST.md), signed `1be6026`,
records unchanged runtime `104fbe8`: 64 pass / 2 fail, S34/S39 only. It was published
and sent to the judge before correction. All original first failures, including
blind baseline `0008dc3` and issuer-native `d4ddc45`, remain unchanged.

Four new product groups pass 64 three-event graph variants, both exact foreign-only
invariance pairs, both replacement relations, atomic refusal, same-key recovery,
ordinary import, stale/ambiguous CAS and exact replay. They first produced eight
intended failures on the old runtime, with no setup errors. The separate audit
validates 125 state instances / 74 unique states and 25 native write observations,
including 11 exact refusals with the entire native tuple unchanged. See
[D009 controls](../impl-astra-23/D009-CONTROLS.json).

All 30 legacy product groups rerun and pass against frozen 0.2.5, and all 4 checker
groups pass. The legacy suite's initial 14 version-label subtest mismatches against
live 0.2.6 remain logged; an explicit package-root option selects the original
contract without changing any expectation. Package validation is green: 103 JSON,
74 vectors, 52 clauses and 38 intended checker controls. Semantic coverage is bounded;
no arbitrary-graph exhaustion or protected-deployment qualification is claimed.

Current exact reports are [canonical](../impl-astra-23/RESULTS.md) and
[historical supplemental](../impl-astra-23/SUPPLEMENTAL.md), with complete actuals
and hashes in adjacent JSON. [README](../impl-astra-23/README.md) gives reproducible
entry points. [Worklog](../impl-astra-23/WORKLOG.md) and
[divergences](../impl-astra-23/DIVERGENCES.md) preserve prior closures and boundaries.

R7-055 is closed by D-009 and dual conformance. R7-059 is also closed. The
ledger has 59 items: 48 fixed, 10 rejected and one resolved owner ambiguity;
no open finding or owner question remains. No owned correction or directed
review is pending. The earlier restore/retention/erasure corrections retain
their regression coverage. All four active seats completed the quiet round and
the convener issued PARK. Eight canonical and one historical deployment fixture
remain unsupported: simulation does not establish physical
purge, outside-domain witness authenticity, live delivery or hostile-writer isolation.
