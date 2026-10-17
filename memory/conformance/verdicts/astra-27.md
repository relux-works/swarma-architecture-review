# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Final status: **PARKED**, 2026-10-17 19:12Z. Final score: **2/2**.

**R7-055 is closed as resolved by D-009.** Ivan's decision at `2c3100d` is
mapped exactly by 0.2.6 `77b951e`. Both independent evaluators pass every
canonical semantic vector: **66/66, zero failures, zero unsupported**, including
all nine new vectors S34–S42. Both also pass **68/68 unchanged historical
semantic cases** on frozen 0.2.5 `6a04e8c`, reported separately.

Source runtime `946cbd8` needed no semantic change. Harness/report `c7e86d5`
closes R7-059 with two explicit version-only fixture copies; all 134 controls
pass and original fixture/first-report bytes stay unchanged. The non-version
mutation guard detects both intended violations before execution.

Package correction `5897520` restricts the event graph by protected issuer
before the shared reachability walk. Four new current-profile groups, 30 legacy
0.2.5 groups and four comparer groups pass. The old runtime fails exactly eight
new assertions, with no setup errors. Independent checks validate 125 state
instances and 25 writes, including 11 full-state-preserving refusals.

The original mixed chain now gives ambiguous d1/d3 in both readers. Assertion-
free all-H paths and the mixed-plus-direct path select d3. The two exact foreign-
only invariance pairs, protected event issuer versus carrier, both revision
relations, ordinary mixed import, same-key recovery, stale/ambiguous CAS and
exact authorized replay pass. Evidence is bounded to the declared fixtures and
controls; no universal graph-size or deployment proof is claimed.

All 103 package artifacts regenerate byte-identically; 38 intended checker
plants pass. The 94 prior JSON artifacts are unchanged except version labels.
Every corrected canonical/historical report row, module hash and input hash
reproduces independently; both readers' normalized semantic outputs agree.
Original `4424598` witness/firsts, package first `1be6026`, source first `31d77d2`
and earlier failures remain immutable. Later source runs are not another blind run.

The ledger has 59 items: 48 fixed, ten rejected, one owner ambiguity resolved.
No open specification/implementation finding, owner question or unclassified
submission remains. Eight canonical and one historical deployment case remain
unsupported. Convener PARK event
`$wTjjxPAdO1lPYyIX7BgMky5ptiS0vPzX6HGGgE99C0U` confirms the four-seat
quiet-round gate. All assigned work and directed replies are complete.
See the [final park note](../parked/astra-27.md).
See [LEDGER.md](../LEDGER.md), [R7-SCORE.md](../R7-SCORE.md) and
[OWNER-QUESTIONS.md](../OWNER-QUESTIONS.md); detailed local closure audit:
astra-27 seat `.temp/judge-r055-round07-closure-review-01.json`.
