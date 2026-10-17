# Choices closing the draft

The owner decisions are binding. The consolidated kernel supersedes the companion
only where it explicitly amends it; its attribution roles, five-record names,
revision authority, projection rules, corpus coverage, premise quality, source
state and disclosure additions are used throughout. The former note that the
context-channel decision was open is obsolete under D-001. This package implements
D-001 as data-only delivery and makes no change to any integration repository.

All choices below are draft normative choices, not claims that the sources already
specified exact bytes. None requires an implementer to consult the source files.

| Id | Gap or tension in sources | Choice and reason | Pin |
| --- | --- | --- | --- |
| A01 | Companion §3 left concrete field names and canonical bytes open; kernel §13 asks R7 to close them | Fixed closed envelope/body objects, field-value lists for schema-governed content, integer-only JSON and framed SHA-256 canonical bytes. Exact strings and sets avoid inferred textual identity. No floating-point normalization or executable schema logic. | K-JSON-1/2, K-DOM-1; S14, S18, S33, P05 |
| A02 | Companion used claim/SourceRef and fewer revision relations | Kernel assertion/source names win; challenge is admitted but never supersedes. All five records carry the expanded envelope. | K-ENV-1, K-REV-1/2; S19, P01–P03 |
| A03 | Schema cardinality did not say how slots are encoded | Single slots are canonical ordered slot-field values, multi slots are `[]` and include assertion id in the sequence key. Plain admission cannot overwrite a head. | K-DOM-2; S10, P10 |
| A04 | Incompatibility across different assertions versus signed conflict on one exact assertion was not operationally specified | Report deterministic cross-assertion opposition separately as `incompatible_with`. It does not synthesize a trusted negative assessment or bypass the sufficient-rule DAG. Two differently valued unassessed statements cannot establish each other's falsity. This is a deliberately conservative closure of kernel §4 and review §2.2. | K-DOM-3; S10 includes an overlapping positive control and non-overlap control |
| A05 | Sources did not order same-batch validation or competing errors | A finite validation priority is fixed; transactions are atomic. Idempotency intent excludes the fresh intake time; replay precedes CAS, and CAS precedes duplicate replacement detection. Malformed-wire tests use a closed `admit_raw` harness variant rather than invalid vector structure. | K-API-1/2; S08, S14, S18, P10 |
| A06 | Kernel §5.2 names expected_version while the gap note sometimes says expected_revision | Exact `(id,version)` expected_version is used. Replacement uses the same id and next version; stale representatives receive version_conflict without partial writes. | K-REV-1; P10 |
| A07 | “Authority order” did not give a total-order algorithm and the companion has no S28/S29 | Canonical receipt predecessors form a partial DAG. Maximal eligible receipted assertions are current; incomparable maxima are ambiguous. Admission order never breaks ties. | K-REV-3; S28, S29, B01 |
| A08 | “Unreceipted replacements stay proposals” could imply automatic kind coercion | Refuse a submitted decision_record without a canonical receipt. Admit only an explicitly resubmitted proposal under its own schema. No silent downgrade or reinterpretation. | K-REV-3; B02, S19 |
| A09 | Bounds lacked a deterministic traversal and unit of accounting | Roots before rules, exact reference order, depth-first sorted premises, per-target/per-polarity counters and memoization; zero is permitted. Hidden/inapplicable work costs no logical budget. Proof enumeration is independently capped. | K-EVAL-2/7, K-API-3; S06, S07, B08, B15 |
| A10 | Extended premise_quality lacked aggregation rules | Any demonstrated clean path wins. Conflicted-only requires complete own enumeration and every found path tainted. Opposite search uncertainty stays not_fully_checked; no witness also uses that label. Root paths have no assertion premises. | K-EVAL-4; S02, S03, S31 |
| A11 | No qualification ordering, root-count format or independence binding was given | Sorted qualification unions and sorted admitted root origins; copies share the original root. Cardinality is not confidence and model reviews do not become deterministic checks. | K-EVAL-3, K-DISC-3; S16, S30, P07 |
| A12 | Source disappearance left room to conflate complete computation, fresh resolution and retained evidence | Current-required roots become incomplete when unavailable; retained checks and independent attestations remain explicitly qualified. A signature alone is never a signed semantic root. The three source states are pinned by positive controls. | K-EVAL-5; S12, S32, B13 |
| A13 | The mandated source_state enum has no “no evidence” member | For a sourceless not-found channel, resolvable_now is vacuous and must never be rendered as fresh verification. Unavailable associated documentary/assessment sources give prior_assessment_only. No additional enum value is invented. | K-EVAL-5; S01, S22, S32 |
| A14 | Corpus coverage declaration shape and compact-view omission behavior were open | Coverage is an exact authorized declaration reference or unknown; declarations are not completeness proofs. Compact/full preserve the entire polarity shape. | K-EVAL-3/7; S30 has unknown and declared controls; S31 |
| A15 | Half-open time, unknown time and freshness boundaries needed exact comparison | UTC seconds only; unknown validity appears only in an any-time query. Freshness expires at now >= usable_until, and unknown confirmation with a duration is stale. Query overrides the schema horizon. | K-TIME-1, K-EVAL-6; S01, S09, S10, P04 |
| A16 | Freshness defaults were illustrative rather than numeric | Synthetic location and intent: seven days; availability: one day; decision/rule/assumption and other supplied domains: none. These are synthetic domain defaults, not deployment retention promises. | Domain documents, K-EVAL-6; P04, P05, B01 |
| A17 | Historical source cuts need resolution evidence, but no resolver protocol was selected | A complete snapshot includes one source frontier and its resolution facts. A query must use that frontier; another frontier needs another complete snapshot. Empty means admitted references only, not a new external read. Current authorization still overrides historical cuts. | K-TIME-1; S09, S12, S29 |
| A18 | Dirty propagation permitted asynchronous recomputation but did not define a scheduling API | Runtime dirty is explicit snapshot state; a dirty response is incomplete. The read evaluator does not clear it implicitly. Recomputed complete snapshots are supplied explicitly; no background worker is invented. Initial S04/S05 are post-withdrawal recomputed states. | K-EVAL-8; S04–S06, S17, B01 |
| A19 | Disclosure label combination and declassification output identity were open | Intersect audiences/purposes, take the earliest retention deadline, union field classes, and preserve all lineage. Owner release is pinned to exact inputs, transformation, output body digest, schema, audience and purpose. | K-DISC-1/2; P05, P11, S20 |
| A20 | Public projection could expose subject linkage through secondary identity fields | Redact internal refs and derivation; map subject and matching issuer/submitter/perspective identities to the audience handle. Other principals need public aliases. No shared internal id or digest appears on the public card. | K-DISC-2/4; P05, P09 |
| A21 | Companion §4 proposed but did not choose a handle scheme | Fixed-length fresh random handles per successful view, exact receipt replay on idempotency, explicit equality/freshness slots. No fresh response timestamps. Normalization cannot hide result, count, refusal or completeness differences. | K-NI-2, K-VEC-2; S13, S14, S24, S27 |
| A22 | Revocation after preparation could silently change a pinned policy | Live revocations are separate runtime facts overriding grants. The policy interpretation remains version-pinned; deliver checks current live rights and requires an audience_projection. | K-AUTH-1, K-PUB-1; P06, B04, B06 |
| A23 | Changes/pagination cursors were not fully specified | This draft has no resumable evaluation cursor; retry the same protected snapshot with different bounds. In fixtures, changes.since is a saved capture index. An authorization removal may yield changed with no current refs. No numeric global cursor is disclosed. | K-EVAL-9, K-API-3; B06, S06, S24 |
| A24 | Kernel publication boundary is defined, but no publisher record is allowed | Delivery is a boundary request/receipt using an external publication id/revision; no sixth record is added. Imported currentness needs an admitted current-version check and horizon. Unconfirmed imports are last_received. | K-PUB-1/2; P06, P07, B04 |
| A25 | An erasure job might omit a sink or treat an old backup inventory as complete | Fence the full lineage closure first; only accounted reachable controlled sinks are purged. Incomplete requests remain fenced and can finish under a new key. Restore uses the vector's explicit initial backup and needs an outside witness before reopening. | K-ERASE-1/2/3; S20 has incomplete/complete controls; S25, S26, P08, B10, B11 |
| A26 | Public availability changes could be invented after a failed hidden-load test | Only predeclared coarse_unavailable may differ. Equal-envelope pairs remain equal; a later explicitly admitted degradation is asserted separately. The default permits no such disclosure. | K-NI-1/3; S27, B08, B09, B16 |
| A27 | Semantic and protected-deployment vectors were mixed in the earlier tables | Keep all original ids/rows. Reclassify nine B cases as semantic; keep eight as deployment. Model erasure/control transitions do not certify enforcement. | K-BOUND-2, K-VEC-1; COVERAGE.md and B01–B17 |
| A28 | Hypotheses, adoption proposals and released coarse location need different statement/disclosure meanings from their base schema | Add decision_proposal, interest_hypothesis and location_city domain documents; do not add kernel kinds or reinterpret a self_declaration as a proposal. | K-DOM-1, K-ENV-3; B02, P01, P05 |
| A29 | Read-only packaging versus full operation vocabulary could overstate conformance | Full semantic conformance requires every semantic vector. The documentary adapter may implement reads over reviewed complete snapshots but cannot claim the full mutation or protection profile. | K-SCOPE-1, K-BOUND-2; README.md, B05/B10/B16 |
| A30 | Notes called the instruction-overlay choice open; D-001 explicitly closes it | The separate data-only frame is normative for the adapter, with original issuer, scope and provenance. A fixed snapshot is historical data and no standing authorization. No instruction weight exists. | K-BOUND-1; B04; adapter D-001 contract |

| A31 | A content grant without metadata could not fill the mandatory attributed view shape | Such a record is ineligible for this draft view; no partial anonymous shape or existence-dependent refusal is invented. Source/certificate access is also checked before work accounting. | K-AUTH-1; B05, S13, B08 |

| A32 | Consecutive record sequences inside one atomic batch could expose half a transaction at an arbitrary historical cut | A snapshot explicitly lists committed_cuts; only completed transaction boundaries may be queried. The first representative update commits at 102, and an attempted read at 101 is invalid_time. | K-TIME-1, K-API-1; P10, S08, S09 |

The choices above are closed for this draft. If the owner rejects a choice, the
normative clause and its fixtures must change together before profile release;
implementers must not silently reinterpret the field. In particular A04 is an
explicit cross-assertion-opposition design choice, not an unnoticed claim that the
source already specified an inference rule.

Open owner inputs are **deployment inputs, not missing semantic defaults**:

1. **O01 — Source custody and retention.** Which real source classes, excerpts,
   structural identifiers, metadata and external sinks may be retained, for what
   purpose and duration, and inside which erasure boundary? D-003's non-sensitive
   reviewed register remains the only authorized pilot corpus. No sensitive class
   is admitted by this package. K-REC-1, K-ERASE-2; S12/P08/B10.
2. **O02 — Protected resource envelope.** Exact production write/read/storage
   limits, disclosure-scoped reservations and outside-witness restore mechanism
   need the deployment owner. Fixture numbers are executable test inputs, not a
   capacity recommendation. D-006 still gates building the protected service.
   K-API-3, K-BOUND-2; S27/B09/B10/B16.
3. **O03 — Trust and policy bindings.** Which concrete identities, account
   generations, review authorities, representative records, canonical authority
   receipts and origin-binding assessors are admitted by the real adapter?
   Synthetic policy facts cannot make that decision. K-ENV-2, K-REC-3,
   K-REV-3; P02/P07/P10/B03/B05.
4. **O04 — Permitted public degradation.** Does the real policy owner authorize
   the draft's coarse_unavailable disclosure, and for which audience/purpose?
   Until that decision, the default is none; failed isolation cannot be excused
   retroactively. K-NI-3; S27/B09.

There is no open choice about real profile admission: it is excluded from this
pilot by D-003/D-006/D-008. Domain disclosure consent and real profile rollout must
be separately approved when that later product work is authorized. There is no
open kernel question needed to run any of the 61 supplied fixtures.
