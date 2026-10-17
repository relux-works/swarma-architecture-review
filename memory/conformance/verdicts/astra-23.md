# astra-23 — package implementer verdict

Current package **0.2.5-draft**, `6a04e8cfb1490569cd1de7468d2085dd4840cf51`:
all canonical and explicitly migrated supplemental semantic vectors pass after
the R7-053 live-retention correction. Independent review is pending.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Supplemental semantic | 61 | 0 | 0 |
| Canonical / supplemental deployment | 0 / 0 | 0 / 0 | 8 / 1 |

Twenty-seven product plus four checker controls pass. Package validation passes
94JSON/65vectors/52clauses and34 intended violation plants. All four write APIs
now require current intake strictly before each output/known-input deadline.
At/after expiry refuses not_authorized/false before idempotency, including exact
replay; full state and original receipt remain unchanged, with no purge effect.
Null/before controls, complete/incomplete-known closure, both batch orders,
changed-intent priority and later unlimited same-key recovery pass.

PHASE2-DEADLINE-FIRSTe689cf2, exact0c1b5ca and RELEASE-0.2.5-FIRSTdf58eae
preserve native, supplemental and full-release failures before correction.
All prior first reports remain immutable; no expected fixture was edited.
Explicit migrations belong to the fixture authors. Interim split-profile checks
are labeled in WORKLOG; final reports above use0.2.5 throughout.

Judge closed R7-048 strict succession at942bdee, R7-049 specification at ef02647,
R7-054 deadline mapping at6a04e8c and source052 at4a14a56. Earlier package closures
031/037/041/044/045/046 remain recorded in DIVERGENCES. Original strict-receipt
failures47c0205/0641033/e689cf2 and every same-issuer positive are retained.

New ASTRA24-12 native probes concern a foreign issuer at an intermediate authority
event. Their contract rule is pending adjudication; no exact oracle is presumed,
no source evaluator code is consulted, and they stay outside vector totals.
Own first reproduction is queued after this completed deadline unit.

Phase1 supported score was2/2 (judgeb1ae299). Phase2 remains **1/2, active**.
Source deadline correction4a14a56 is independently verified50/0/7canonical;
this package candidate awaits judge review. Seven source erasure/restore/load
paths remain unsupported. Early PARK requires source57/57 and no new open item
for a complete round; hard cap13:00Z. Deployment remains unqualified.

Implementation remains package-derived; original blind first0008dc3 is immutable.
Evidence: ../impl-astra-23/RESULTS.md/JSON, SUPPLEMENTAL.md/JSON, all FIRST reports,
WORKLOG.md, DIVERGENCES.md and product/checker controls. Historical0.2.2 reports
remain separately labeled with their recorded runtime. Unsupported never means pass.
