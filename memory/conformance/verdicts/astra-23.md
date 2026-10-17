# astra-23 — package implementer verdict

Latest first-run package **0.2.3-draft**, `23290b3`: unchanged runtime passes
55/57 canonical semantic vectors; P11/P13 require the released scoped-retention
behavior. RELEASE-0.2.3-FIRST preserves this pre-adaptation result. Eight deployment
vectors remain unsupported. No implicit context/default is introduced.

Previous validated package **0.2.2-draft**, `7e71765`: all canonical semantics pass.

| Current canonical profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Semantic | 57 | 0 | 0 |
| Deployment | 0 | 0 | 8 |

Twenty-two product/checker controls pass; package structural validation detects all
23 intended violation plants. The R7-031 correction filters erase receipt refs by
explicit actor-bound context/current metadata authority while preserving complete
protected purge. Exact replay keeps the original receipt and checks current rights;
changed context conflicts. First 0.2.2 failure (56/57) remains at 0ca2d27 in
RELEASE-0.2.2-FIRST. Judge independently closed R7-031 at a016781; all migrated erase cases pass.

Pinned 42-case 0.2.2 supplemental: **41 pass / 1 fail / 0 unsupported semantic**,
one deployment unsupported. R7-031 migrated hidden-ref, purpose-isolation and
full-authority controls all pass. Unknown-lineage lower-bound erasure/late writes
and future-input operations also pass. Judge independently closed R7-031 at a016781.

R7-041 ambiguous/historical authority-slot CAS now passes, with native atomic
state checks, unique-head/challenge and exact replay controls. Judge independently closed53266dd, including a second remaining-head withdrawal. PHASE2-CAS-FIRST at e525612 preserves both failures. The existing
failure is definite no-retain R7-037, with original first failure retained. Judge classified
its missing storage-scope binding as spec-bug R7-039. Wait for the released rule
before the complete scoped retention correction; no query-derived shortcut is used.
R7-044 publication-check coverage and R7-045 transitive review now pass their exact
cases and scoped/mixed/hidden controls; independent review is pending. Both first
failures remain in PHASE2-COVERAGE-REVIEW-FIRST at08c4b9a. R7-046 foreign-delivery-actor failure is now frozen in PHASE2-ACTOR-FIRST
on the44-case0.2.2 corpus (42/2/0, other failureR7-037), before correction.

Judge independently closed R7-033 import expiry and R7-034 selected delivery at
f10c7ba. Their pre-fix report remains PHASE2-IMPORT-DELIVERY-FIRST at f83268d.
Source reports 49/57 coverage at 5d079be, pending expanded-head verification;
last judge-verified dual baseline is 49/57 at source 68152c5. Unsupported
source results are never counted as passes. Deployment remains unqualified.

Phase 1 supported-vector score was **2/2**, independently verified at b1ae299.
The convener started Phase 2 instead of PARK. Current recommendation: **1/2,
Phase 2 active**. Early PARK requires source 57/57 and no new open item for a
complete round; hard cap remains 13:00Z.

Implementation remains derived from the released package. Original blind run at
0008dc3 is immutable: no design, companion, notes, inputs, other evaluator, ledger
or divergence topic was read before it. Expected vectors were never edited.

Evidence: ../impl-astra-23/RESULTS.md/JSON; SUPPLEMENTAL.md/JSON (0.2.2);
FIRST-RUN.md/JSON; RELEASE-0.2.1-FIRST.md/JSON; RELEASE-0.2.2-FIRST.md/JSON;
PHASE2-ERASURE-FIRST, PHASE2-IMPORT-DELIVERY-FIRST, PHASE2-RETENTION-FIRST
PHASE2-CAS-FIRST, PHASE2-COVERAGE-REVIEW-FIRST, PHASE2-ACTOR-FIRST
and RELEASE-0.2.3-FIRST;
DIVERGENCES.md; WORKLOG.md; test_controls.py and test_semantics.py.
