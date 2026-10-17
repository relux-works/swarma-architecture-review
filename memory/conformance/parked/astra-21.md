# astra-21 park note

Status: **PARKED**, following convener `ivmbp_swarma-memory_orch` at
**2026-10-17T19:12Z**, event
`$wTjjxPAdO1lPYyIX7BgMky5ptiS0vPzX6HGGgE99C0U` in `rounds`.
Seat: package editor, sole writer of `memory/spec/`.

## Delivered

Package **0.2.6-draft**, signed release
`77b951eb86d5ba9198921d058930884918a39942`, encodes owner decision D-009 in
K-REV-3. Currentness and strict replacement/correction use nonempty reachability
after restricting to the protected deciding issuer's event subgraph. Events
without assertions count; one own path suffices; foreign nodes are not contracted
and foreign branches cannot cancel that path. Mixed graphs remain admissible.
Existing refusal codes, CAS and replay rules stay intact.

Nine new vectors S34-S42 cover the original separating pair, no contraction,
assertion-free intermediates, a direct own path beside a mixed branch, two exact
foreign-only invariance pairs, refused/accepted revisions, ordinary import and
protected event attribution independent of carrier. All 65 older vectors retain
their complete semantics after version substitution; pilot bytes are unchanged.

Fresh PARK readback at `715d7a74e323ce9a0e04b7a11e9a6bd04b9549eb` confirms the
package tree `6988e98dd87eb7e08ab5c51dd06699b942cae373` equals the release.
Validation: 103 JSON files, 14 closed schemas, 14 domain documents, one fixture,
74 vectors, 52 clauses and 38 intended checker controls. All JSON regenerates
byte-for-byte. Source designs and other seats' artifacts were not edited.

## Verified outcome

| Evidence | Result and pin |
| --- | --- |
| R7 score | **2/2**, judge closure `75c13d2`, quiet readback `715d7a7` |
| Current canonical 0.2.6 | **66/66 semantic** for both independent evaluators |
| Historical regression 0.2.5 | **68/68 semantic** for both; unchanged fixtures and exact frozen grammar, separate denominator |
| Source evaluator | Runtime `946cbd8` unchanged; report/harness `c7e86d5`, all 134 controls pass |
| Package evaluator | Runtime `5897520`; four current product groups, 30 historical product groups and four comparer groups pass |
| Editor review | Signed `1e222f6`: full current report reproduction, 125 valid state instances, 25 operations and 11 atomic full-state refusals |
| Negative control | Frozen old package runtime gives eight intended failures, zero setup errors |
| Ledger | 59 items: 48 fixed, ten rejected, one ambiguity resolved; no open finding or owner question |
| Deployment | Eight canonical plus one historical case unsupported; no qualification claim |

R7-055 is **closed by D-009 and dual verification**. R7-059 is the separate
source test-profile binding correction, fixed without product-runtime or
behavioral-oracle changes. Original witness `4424598`, first package failure
`1be6026`, first source run `31d77d2` and original cases remain immutable.
Audit metadata `fddb403` documents typed-map hashing and run-local nonces;
nonce-free input hashes and within-run state equality reproduce independently.

## Open threads and handoff

**None for this bounded round.** All directed editor requests were answered;
quiet round `04390b3` added no case, divergence or package change. The convener
confirmed all four active seats' quiet markers before PARK. Seats 24-26 stayed
parked. This note supersedes the historical 06:33Z / 0.2.5 park note, retained
in signed `962a21d`; its former owner hold no longer applies.

The [verdict](../verdicts/astra-21.md), [release notes](../../spec/RELEASES.md),
[build evidence](../../spec/checks/BUILD_NOTES.md), [score](../R7-SCORE.md) and
[owner-question closure](../OWNER-QUESTIONS.md) retain the delivery evidence.
Local continuity is `.temp/tasks.md`; focused review is
`.temp/astra-21/d009-review.md`; final hashes are in
`.temp/astra-21/park-026-readback.json`. No foreground wait or worker remains.
The next task, if explicitly reopened, starts with a fresh signed pull and its
current brief. No pilot or deployment work is included in this PARK.
