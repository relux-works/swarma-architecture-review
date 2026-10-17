# Coverage and source concordance

`kernel` means the consolidated kernel contract, `companion` the bounded-support
semantic companion, and `design` the bounded-evidence design. These citations
identify provenance only: an implementer needs only this package. Owner decisions
D-001–D-008 take precedence over all three sources. Source clause numbers are the
versions supplied for this draft. All 52 normative clause ids are exercised by at
least one fixture; there are no unlisted normative clauses or not-vector-tested
clauses. A citation does not claim exhaustive testing of every sentence.

| Vector id | Profile | Normative clauses in kernel/semantics.md | Source clause |
| --- | --- | --- | --- |
| S01 | semantic | K-SCOPE-1, K-EVAL-1, K-EVAL-3, K-VEC-1, K-TIME-1 | companion §4, §9 S01; kernel §1 |
| S02 | semantic | K-EVAL-1, K-REC-2, K-REC-3 | companion §4, §9 S02 |
| S03 | semantic | K-EVAL-4, K-RULE-1, K-RULE-2 | companion §4, §9 S03; kernel §6.1 |
| S04 | semantic | K-REV-2, K-EVAL-1, K-RULE-2 | companion §§5–6, §9 S04 |
| S05 | semantic | K-REV-2, K-EVAL-1 | companion §§4–6, §9 S05 |
| S06 | semantic | K-EVAL-2, K-API-3, K-NI-2 | companion §§4–5, §9 S06 |
| S07 | semantic | K-EVAL-7, K-EVAL-2 | companion §5, §9 S07 |
| S08 | semantic | K-RULE-1, K-API-1, K-REF-1 | companion §3, §9 S08 |
| S09 | semantic | K-TIME-1, K-REV-2 | companion §§3,6, §9 S09 |
| S10 | semantic | K-TIME-1, K-DOM-2, K-DOM-3 | companion §3, §9 S10; kernel §4 |
| S11 | semantic | K-REC-2, K-REC-3 | companion §6, §9 S11 |
| S12 | semantic | K-EVAL-5, K-ERASE-1, K-TIME-1 | companion §6, §9 S12; kernel §§3,6.1 |
| S13 | semantic | K-AUTH-1, K-NI-1, K-NI-2, K-VEC-2 | companion §4, §9 S13 normalization paragraph; kernel §7.3 |
| S14 | semantic | K-JSON-1, K-JSON-2, K-API-1 | companion §8, §9 S14 |
| S15 | semantic | K-REC-2, K-PROJ-1 | companion §7, §9 S15 |
| S16 | semantic | K-RULE-2, K-ENV-3, K-REC-2 | companion §3, §9 S16 |
| S17 | semantic | K-EVAL-8, K-API-1, K-REV-1 | companion §5, §9 S17 |
| S18 | semantic | K-JSON-1, K-API-2, K-REF-1 | companion §3, §9 S18; kernel §4 |
| S19 | semantic | K-REV-1, K-REV-3, K-SCOPE-1 | companion §§6–8, §9 S19; kernel §§5.1–5.3 |
| S20 | semantic | K-DISC-1, K-ERASE-1, K-ERASE-2 | companion §6, §9 S20; kernel §7.1 |
| S21 | semantic | K-RULE-1, K-RULE-2, K-EVAL-1 | companion §3, §9 S21 |
| S22 | semantic | K-REC-1, K-REC-3, K-RULE-2 | companion §3, §9 S22 |
| S23 | semantic | K-REC-1, K-REV-3, K-PROJ-1, K-PUB-2 | companion §3, §9 S23; design Stores and authority |
| S24 | semantic | K-NI-1, K-NI-2, K-VEC-2, K-EVAL-8, K-AUTH-1 | companion §4, §9 S24 normalization paragraph; kernel §7.3 |
| S25 | semantic | K-ERASE-3, K-ERASE-2 | companion §6, §9 S25; design Retention and derived information |
| S26 | semantic | K-ERASE-3, K-DISC-1 | companion §6, §9 S26 |
| S27 | semantic | K-NI-1, K-NI-2, K-NI-3, K-API-3, K-VEC-2 | companion §4, §9 S27 normalization paragraph; design Context seam |
| S28 | semantic | K-REV-3, K-EVAL-9 | kernel §5.3, §12 S28; review-1 gaps §2.3 |
| S29 | semantic | K-REV-3, K-TIME-1, K-EVAL-9 | kernel §5.3, §12 S29; review-1 gaps §2.3 |
| S30 | semantic | K-EVAL-3, K-REC-1, K-DISC-3 | kernel §6.1, §12 S30; review-1 gaps §2.1 |
| S31 | semantic | K-EVAL-4, K-EVAL-7 | kernel §6.1, §12 S31; review-1 gaps §2.4 |
| S32 | semantic | K-EVAL-5, K-REC-2, K-ERASE-1 | kernel §6.1, §12 S32; companion §6 |
| S33 | semantic | K-DOM-1, K-JSON-1 | kernel §4, §12 S33; companion §3 |
| P01 | semantic | K-ENV-1, K-ENV-3, K-PROJ-1, K-SCOPE-1 | kernel §§2,6.2,8, §12 P01; profiles gaps A2 |
| P02 | semantic | K-ENV-2, K-REV-1, K-ENV-1, K-ENV-3 | kernel §§2,5.1, §12 P02; profiles gaps A2 |
| P03 | semantic | K-REV-1, K-ENV-1, K-PROJ-1 | kernel §§5.1,6.2, §12 P03; profiles gaps A3 |
| P04 | semantic | K-EVAL-6, K-DOM-1, K-TIME-1 | kernel §6.3, §12 P04; profiles gaps A3 |
| P05 | semantic | K-DISC-1, K-DISC-2, K-DISC-4, K-JSON-2, K-PUB-1 | kernel §§7.2,9.1–9.2, §12 P05; profiles gaps A4 |
| P06 | semantic | K-PUB-1, K-AUTH-1 | kernel §9.3, §12 P06; profiles gaps A5 |
| P07 | semantic | K-DISC-3, K-PUB-2, K-EVAL-3 | kernel §§6.1,9.2, §12 P07; profiles gaps A5 |
| P08 | semantic | K-ERASE-1, K-ERASE-2, K-DISC-1, K-API-1, K-AUTH-1 | kernel §7.1, §12 P08; profiles gaps A4 |
| P09 | semantic | K-DISC-4, K-DISC-2, K-NI-1 | kernel §9.4, §12 P09; profiles gaps A5 |
| P10 | semantic | K-REV-1, K-ENV-2, K-API-1, K-TIME-1 | kernel §5.2, §12 P10; profiles gaps A3 |
| P11 | semantic | K-DISC-1, K-AUTH-1, K-ENV-3, K-API-1, K-API-2, K-TIME-1 | kernel §7.1, §12 P11; profiles gaps A4; explicit retention purpose |
| P12 | semantic | K-SNAP-1, K-PUB-1, K-AUTH-1, K-SCOPE-1 | kernel §§1,6.4,9.3, §12 P12 |
| P13 | semantic | K-DISC-1, K-ENV-3, K-PROJ-1, K-NI-1, K-AUTH-1, K-API-1 | kernel §§7.1,8, §12 P13; known-input retention and atomic intake |
| P14 | semantic | K-REV-4, K-REV-1, K-API-1 | kernel §§5.2,5.4, §12 P14 |
| P15 | semantic | K-PROJ-2, K-PROJ-1, K-REV-2, K-DISC-4 | kernel §9.3, §12 P15 |
| B01 | semantic | K-REV-1, K-REV-3, K-REF-1, K-API-1, K-EVAL-8, K-EVAL-9 | design First-slice acceptance vectors, row 1; kernel §11.1 |
| B02 | semantic | K-REV-3, K-REC-1, K-ENV-3 | design First-slice acceptance vectors, row 2; kernel §5.3 |
| B03 | semantic | K-REC-1, K-REV-3, K-BOUND-1 | design First-slice acceptance vectors, row 3; companion §3 |
| B04 | deployment | K-BOUND-1, K-PUB-1, K-REC-3 | design First-slice acceptance vectors, row 4; kernel §10; D-001 |
| B05 | deployment | K-AUTH-1, K-PUB-1, K-BOUND-2 | design First-slice acceptance vectors, row 5; companion §§4,6 |
| B06 | deployment | K-AUTH-1, K-NI-1, K-EVAL-9, K-BOUND-2 | design First-slice acceptance vectors, row 6; companion §4 |
| B07 | semantic | K-NI-1, K-NI-2 | design First-slice acceptance vectors, row 7; companion §4, S24 |
| B08 | semantic | K-AUTH-1, K-EVAL-2, K-NI-1, K-API-3 | design First-slice acceptance vectors, row 8; companion §4, S27 |
| B09 | deployment | K-NI-3, K-BOUND-2, K-VEC-2 | design First-slice acceptance vectors, row 9; companion §4, S27 |
| B10 | deployment | K-ERASE-1, K-ERASE-2, K-ERASE-3, K-BOUND-2 | design First-slice acceptance vectors, row 10; companion §6, S25 |
| B11 | deployment | K-ERASE-3, K-BOUND-2 | design First-slice acceptance vectors, row 11; companion §6, S26 |
| B12 | semantic | K-API-1, K-JSON-2 | design First-slice acceptance vectors, row 12; companion §8, S14 |
| B13 | semantic | K-EVAL-5, K-EVAL-3 | design First-slice acceptance vectors, row 13; kernel §6.1; companion §6 |
| B14 | semantic | K-EVAL-1, K-EVAL-2, K-API-3 | design First-slice acceptance vectors, row 14; companion §5, S04 |
| B15 | semantic | K-EVAL-1, K-EVAL-2, K-API-3 | design First-slice acceptance vectors, row 15; companion §5, S06 |
| B16 | deployment | K-BOUND-1, K-BOUND-2 | design First-slice acceptance vectors, row 16; design Context seam |
| B17 | deployment | K-BOUND-1, K-REC-3, K-API-2 | design First-slice acceptance vectors, row 17; design APIs and effects |

B01, B02, B03, B07, B08, B12, B13, B14 and B15 are in `semantic/`: their
assertions concern selected decisions, attribution, logical budgets, metadata,
idempotency, availability and support computation. Their source table placement
does not make them isolation tests. B04, B05, B06, B09, B10, B11, B16 and B17 remain
in `deployment/` because their acceptance requires observing real delivery,
authentication/revocation, resource reservation, storage/restore, delayed writes,
independent controls or absence of execution across an actual protection boundary.

S25/S26 and P06/P08 model boundary state transitions as plain data. Passing these
semantic fixtures proves only the modeled response contract; B10/B11 and actual
service qualification must establish enforcement. S13/S24/S27 compare semantic
outputs and metadata distributions; no fixture proves constant-time behavior.

The checker validates structure, references, coverage and internal expected-output
consistency. It does not run an evaluator. The complete expected output in each
vector is a hand-derived oracle; its source is the cited normative clauses.
Additional controls inside S01, S10, S30, S32 and P04 pin unknown valid time,
cross-assertion incompatibility, declared coverage, surviving attestation states
and exact freshness expiry, respectively.

Release 0.2.0-draft targets kernel v0.2. P05 includes missing-owner rejection, two-owner release/delivery and revocation. B10 includes a stale external witness refusal before current-complete reconciliation. These controls do not qualify deployment enforcement.
