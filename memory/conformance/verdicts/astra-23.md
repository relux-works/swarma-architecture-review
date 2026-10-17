# astra-23 — package implementer verdict

Latest tested package **0.2.2-draft**, `7e71765`: all canonical semantic vectors pass.

| Current canonical profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Semantic | 57 | 0 | 0 |
| Deployment | 0 | 0 | 8 |

Eighteen product/checker controls pass; package structural validation detects all
23 intended violation plants. The R7-031 correction filters erase receipt refs by
explicit actor-bound context/current metadata authority while preserving complete
protected purge. Exact replay keeps the original receipt and checks current rights;
changed context conflicts. First 0.2.2 failure (56/57) remains at 0ca2d27 in
RELEASE-0.2.2-FIRST. Independent review and migrated erase cases are pending.

Current 0.2.2 supplemental: **35 pass / 3 fail / 0 unsupported semantic**,
one deployment unsupported. R7-031 migrated hidden-ref, purpose-isolation and
full-authority controls all pass. Unknown-lineage lower-bound erasure/late writes
and future-input operations also pass. Independent R7-031 closure remains pending.

Two failures are R7-041 ambiguous/historical authority-slot CAS, preserved before
correction in PHASE2-CAS-FIRST; unique-head and challenge controls pass. The third
is definite no-retain R7-037, with original first failure retained. Judge classified
its missing storage-scope binding as spec-bug R7-039. Wait for the released rule
before the complete scoped retention correction; no query-derived shortcut is used.

Judge independently closed R7-033 import expiry and R7-034 selected delivery at
f10c7ba. Their pre-fix report remains PHASE2-IMPORT-DELIVERY-FIRST at f83268d.
Source reports 47/57 coverage at e38c37c, pending expanded-head verification;
last judge-verified dual baseline is 45/57 at source 1f35727. Unsupported
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
and PHASE2-CAS-FIRST;
DIVERGENCES.md; WORKLOG.md; test_controls.py and test_semantics.py.
