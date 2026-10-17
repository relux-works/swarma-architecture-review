# astra-23 — package implementer verdict

**Reopened D-009 round: locally green, judge verification pending; score 1/2
until closure.** The old 06:33Z PARK is historical. The new convener PARK has
not yet arrived. [Park note](../parked/astra-23.md) preserves the earlier handoff.

Implementation remains derived from `memory/spec/` only. No other evaluator
implementation, source design, decision document or reviewer input was read for
this correction. D-009 is implemented through released K-REV-3 in package
**0.2.6-draft**, `77b951eb86d5ba9198921d058930884918a39942`.

| Evidence | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Current 0.2.6 canonical semantic | 66 | 0 | 0 |
| Historical 0.2.5 supplemental semantic | 68 | 0 | 0 |
| Current canonical deployment | 0 | 0 | 8 |
| Historical supplemental deployment | 0 | 0 | 1 |

The supplemental run uses the current runtime with exact frozen0.2.5 grammar
`6a04e8c` and unchanged author-owned inputs. It is a separate regression result,
not additional canonical0.2.6 coverage. No fixture or behavioral oracle migrated.

The shared authority relation now restricts canonical events to their protected
policy issuer before predecessor traversal. Assertion-free intermediates count;
foreign paths do not contract and foreign branches cannot cancel an all-H path.
Projection currentness, revision CAS head and strict replacement succession use
this same relation. Mixed-only succession refuses authority_receipt_required/false
without mutation; ordinary import remains admissible and yields ambiguity.
Authorized exact replay and version_conflict retain their prior meanings.

[The immutable first](../impl-astra-23/RELEASE-0.2.6-FIRST.md), signed `1be6026`,
records unchanged runtime `104fbe8`:64pass/2fail, S34/S39 only. It was published
and sent to the judge before correction. All original first failures, including
blind baseline `0008dc3` and issuer-native `d4ddc45`, remain unchanged.

Four new product groups pass64 three-event graph variants, both exact foreign-only
invariance pairs, both replacement relations, atomic refusal, same-key recovery,
ordinary import, stale/ambiguous CAS and exact replay. They first produced eight
intended failures on the old runtime, with no setup errors. The separate audit
validates125 state instances/74unique states and25 native write observations,
including11exact refusals with the entire native tuple unchanged. See
[D009 controls](../impl-astra-23/D009-CONTROLS.json).

All30legacy product groups rerun and pass against frozen0.2.5, and all4checker
groups pass. The legacy suite's initial14version-label subtest mismatches against
live0.2.6 remain logged; an explicit package-root option selects the original
contract without changing any expectation. Package validation is green:103JSON,
74vectors,52clauses and38intended checker controls. Semantic coverage is bounded;
no arbitrary-graph exhaustion or protected-deployment qualification is claimed.

Current exact reports are [canonical](../impl-astra-23/RESULTS.md) and
[historical supplemental](../impl-astra-23/SUPPLEMENTAL.md), with complete actuals
and hashes in adjacent JSON. [README](../impl-astra-23/README.md) gives reproducible
entry points. [Worklog](../impl-astra-23/WORKLOG.md) and
[divergences](../impl-astra-23/DIVERGENCES.md) preserve prior closures and boundaries.

D-009 resolves the owner decision; R7-055 still requires the judge's independent
closure and the collective's quiet round. The earlier restore/retention/erasure
corrections retain their regression coverage. Eight canonical and one historical
deployment fixture remain unsupported: simulation does not establish physical
purge, outside-domain witness authenticity, live delivery or hostile-writer isolation.
