# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 30, phase 2 active. Current score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 55 items: ten rejected as defects, forty-three independently fixed,
one open implementation bug (R7-053), and one owner question (R7-055).
See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

R7-055 records a genuine boundary ambiguity: whether an H1 canonical edge
endorses an H2 predecessor's transitive ordering. The native pair at `4424598`
validates and independently reproduces source ambiguous d1/d3 versus package
current d3; its same-H1 control agrees. Source clauses do not decide the edge's
attestation meaning. The precise choices and tradeoffs are filed in
[OWNER-QUESTIONS.md](../OWNER-QUESTIONS.md) and `q-authority-issuer`. No exact
oracle or new implementation verdict is inferred before an attributed decision;
verified same-issuer closures stand. Other coverage work continues.

R7-052 source expiry closes at signed `4a14a56`. Independent full 0.2.5 canonical
execution exactly reproduces all 65 committed rows and input/module hashes:
50/0/7 semantic. All 112 source controls pass, including six deadline groups
across admit/raw/revise/declassify, every output, original current-time replay,
transitive/incomplete-known closure, both batch orders and null/unrelated limits.
Seven unchanged migrated expiry vectors pass. Ten independent operation checks
now give three positive admissions and seven exact atomic refusals, retaining
the original receipt on denied replay. First failures remain immutable.

Package `942bdee` remains at its verified 56/1/0 first 0.2.5 run, with only P11
failing, so exact dual canonical coverage is **49/57**. Its correction remains
R7-053. The specification `6a04e8c` is verified, with exact regeneration of 94
JSON artifacts and 34 intended checker controls; no specification finding is open.

The source supplemental corpus currently splits by explicit author profile:
41 semantic cases at 0.2.5 give 33/0/8, and twenty pending seat-24 cases pass
20/20 when run explicitly at their original 0.2.4. Their current-version
mismatches are only profile stamps. All 62 artifacts validate in their own
profiles and preserve original semantic inputs/expectations. No unified current
supplemental total or implicit fixture conversion is claimed.

Seven canonical source coverage gaps remain, as do eight canonical plus one
supplemental unsupported deployment case. Synthetic success does not qualify
real custody, authorization or restore boundaries. Later source adaptation is
not another package-blind run. Continue until the convener posts PARK, then
finalize this verdict and park note.
