# astra-23 — package implementer verdict

Current package **0.2.4-draft**, `ef0264702d3ff937bd34410ea80660b196b6f1b0`:
all canonical and explicitly migrated supplemental semantic vectors pass after
the R7-048 strict authority-succession correction. Independent review is pending.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Supplemental semantic | 54 | 0 | 0 |
| Canonical / supplemental deployment | 0 / 0 | 0 / 0 | 8 / 1 |

Twenty-four product plus four checker controls pass. Package structural validation
passes94JSON/65vectors/52clauses and33 intended violation plants. Replace/correct
now require a strictly succeeding canonical receipt. Missing, prior, reused and
incomparable receipts refuse atomically with authority_receipt_required/false;
same-key retry, direct/transitive successors, plain incomparable import and exact
replay after a later head pass. Entire state, dirty-since, captures and bindings
remain unchanged on refusal. Prior CAS head selection and replay precedence survive.

PHASE2-SUCCESSION-FIRST47c0205, exact0641033 and RELEASE-0.2.4-FIRSTe689cf2
preserve all pre-fix failures. Earlier first reports remain immutable; expected
vectors were never edited. Explicit supplemental profile migrations belong to
fixture authors21/24/25/26, not runtime normalization.

PHASE2-DEADLINE-FIRSTe689cf2 independently preserves ASTRA25-11 fresh storage
at/after inherited expiry and at own expiry, plus before-expiry admission and
expired replay with no state mutation. Exact expiry code/order/replay mapping is
pending judge/editor; those native probes stay outside the vector totals and
are queued after the authority correction.

Judge closed R7-031 receipt/replay at a016781, R7-041 CAS at53266dd,
R7-044/045 import coverage/transitive review atf6c339d, R7-046 actor binding
at3ce8ee3 and R7-037 scoped retention at4af0360. Specification039/042 closed
at23290b3; new049 release awaits judge closure. Existing deadline behavior is
explicitly not included in those grant-scope closure claims.

Phase1 supported score was2/2 (judgeb1ae299). Phase2 remains **1/2, active**.
Last judge-verified dual canonical coverage is50/57 on0.2.3 after source8a42945.
Current0.2.4 source still has a separate B01 transitive-projection failure and
seven unsupported erasure/restore/load paths; package passes do not close those.
Early PARK requires source57/57 and no new open item for a complete round;
hard cap13:00Z. Unsupported is never counted as pass. Deployment unqualified.

Implementation remains package-derived. Original blind first0008dc3 is immutable;
no source evaluator code was consulted. Evidence: ../impl-astra-23/RESULTS.md/JSON,
SUPPLEMENTAL.md/JSON, all FIRST reports, WORKLOG.md, DIVERGENCES.md and controls.
Historical0.2.2 reports remain separately labeled with their recorded runtime.
