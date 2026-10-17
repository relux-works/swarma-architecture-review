# Package releases

## 0.2.4-draft

Corrects judge-classified R7-049: K-REV-3 already required an authoritative
replacement receipt to succeed its target's receipt, but K-REF-1 did not name the
exact refusal when a canonical receipt exists without that ordering. Missing,
prior, identical and incomparable receipts now explicitly yield
`authority_receipt_required`, `retryable: false`. Strict succession requires one
or more predecessor edges, including paths through receipt-only intermediate
events. Refusal commits no records, cut, dirty state or idempotency entry.
`version_conflict` remains reserved for the current-head CAS contract. Exact
currently authorized successful replay precedes CAS and preserves its receipt.
Ordinary incomparable canonical plain import remains permitted; it creates no
memory-side replacement relation. No new code enum or owner decision is added.

Migration: package/schema/view identifiers advance to 0.2.4-draft (schema URNs
use 0.2.4). No input shape changes. Only B01 changes after version normalization;
all other 64 expected reports and inputs are unchanged. B01 first refuses four
invalid receipt classes under the same key, checks unchanged currentness and no
new cut, then accepts a direct and a transitive successor. It returns the original
direct-write receipt on exact replay after the next head, and separately refuses
a stale new-key request with `version_conflict`. The registered dependent remains
review-required after the successful replacement. The reusable two-version pilot
fixture stays byte-identical; B01's direct-successor capture pins its behavior.

The inventory stays 65 vectors (57 semantic / 8 deployment), 52 clauses,
14 schemas and 94 JSON artifacts. Structural validation and deterministic
regeneration pass. All 33 checker controls detect their intended violations,
including a forbidden receipt for B01's prior event. The accepted-revision
lineage-fact plant now locates the successful write rather than assuming the
first operation succeeds. These controls do not execute evaluator semantics.

The unchanged package evaluator gives 56 semantic passes and one B01 failure;
eight deployment cases remain unsupported. Separate identical-prestate probes
preserve forbidden commits for prior, identical and incomparable receipts; the
missing-receipt control is already atomically refused. Prescribed direct and
transitive successes, exact replay and separate CAS refusal match every expected
field after declared handle normalization. Ordinary incomparable plain import
also succeeds with two ambiguous candidates and no revision or dirty state.
These are retained regression and positive controls, not a corrected full-release
conformance claim. Independent evaluator fixes and explicit supplemental fixture
migrations remain required.

## 0.2.3-draft

Corrects judge-classified R7-039 (missing retention wire scope) and R7-042
(premature existence checks on future integration facts). The inventory remains
65 vectors, 57 semantic and 8 deployment, with 52 clauses and 14 schemas.

Breaking wire change: admit, admit_raw, revise and declassify require
`context.retention_context: {audience, purpose}`. The authenticated actor is the
fixed storage principal. Retain must match that actor, each output/input record's
exact space and id, and this single audience/purpose. Traverse complete content
inputs and incomplete-lineage known lower bounds transitively, using the admitted
pre-state plus the whole atomic batch. Future integration facts alone do not make
a record present. Storage scope is independent of onward disclosure labels;
empty labels can be retained but cannot grant disclosure. No operation, read/use,
metadata or release permission substitutes for retain.

Live revocations now also accept `right: retain`, under the existing exact
principal/audience/purpose scope across records and spaces governed by that
policy. This blocks new retention and authorized write replay; it does not itself
revoke read/use/forward or erase stored records. Context is canonical intent.
Exact replay rechecks current retain authority over the original output/input
closure and either returns the unchanged receipt or refuses `not_authorized`
without state mutation. An authorized context change under the same key conflicts.

Migration: explicitly bind every write's intended retention scope. Canonical
writes use public/read where that actor already has grants; P03's observer and
the narrowed P11/P13 controls use private/read. This is a deliberate fixture
choice, not a default that implementations may infer. All previous expected
reports are unchanged apart from profile version except P11 and P13.

P11 pairs exact principal/space/record/audience/purpose refusals with narrow
private/read admission despite broader disclosure labels. It also checks direct
and transitive input authority, no committed cut or reserved key after refusal,
exact later-stamp replay, changed-context conflict and retain-revoked replay/new
write refusal. Read permission and the private view survive a retain-only
revocation. P13 retains unknown-lineage known-input checks, a future-input refusal
followed by same-key whole-batch success, an input appearing later in proposal
order, and empty-label storage with no disclosed item. The canonical inventory
checks are supplemented by implementer full-state assertions for refused writes;
the vector postcondition shape does not expose every internal state component.

The checker defers input existence only when an integration fact's output is not
yet admitted. Admitted complete and unknown-lineage lower bounds still require
actual inputs. Accepted operation checks include prior successful writes and the
whole current batch. Duplicate/direct-fact integrity remains unchanged. The
ASTRA25-10 pre-fix false positive was reproduced before correction; its independent
fixture and expected outputs remain untouched.

Validation: 94 JSON artifacts and 32 intended checker violations. New controls
cover all four required contexts, forbidden principal override, unauthorized
receipt output, an accepted batch missing an input, and dangling complete/unknown
admitted inputs. The unchanged package evaluator produces the intended P11/P13
red result: 55 semantic passes, two failures, zero unsupported; deployment eight
unsupported. Isolated authorized P11/P13 traces pass every expected field,
including same-batch input resolution and non-disclosure. This is regression
evidence, not a corrected evaluator conformance claim. Independent 0.2.3 behavior
and adversary migration remain required.

## 0.2.2-draft

Corrects judge-classified R7-031: erase authority and full protected erasure closure do not authorize disclosure of hidden closure identifiers. K-ERASE-2 now agrees with K-API-1 and the source metadata contract. The inventory stays 65 vectors (57 semantic / 8 deployment), 52 clauses and 14 schemas.

Breaking wire change: every erase operation requires `receipt_context: {audience, purpose}`. The authenticated actor is its fixed recipient. Resolve exact current read/use/metadata and disclosure permission before the new fence; no later query supplies this context and unrelated audience/purpose grants cannot be combined. Existing erased payloads do not automatically revoke approved structural metadata, so a separately authorized later receipt may still name its tombstone. The full protected closure, fences and custody dispositions remain mandatory regardless of which refs are disclosed.

The receipt context is canonical idempotency intent. Changing it under the same actor/space/key is `idempotency_conflict`. Exact authorized retry preserves the original receipt and handle. If any stored receipt ref is no longer metadata-authorized in that same context, retry returns `not_authorized` without a write; it does not redact, regenerate or overwrite the original receipt.

Migration: explicitly choose the intended audience/purpose for each erase operation. Existing canonical erases use private/read, preserving their original authorized lists. P08 deliberately gives private/read metadata only for the sensitive target and private/publish metadata for both target and derivative. It proves filtered receipt plus full purge, exact replay, changed-context conflict, an authorized full-list control and read-revoked replay refusal. Of 65 expected reports, only P08 changes after normalizing the profile version.

Validation: 94 JSON artifacts, 23 intended checker violations. New plants reject missing receipt context and a recipient override, and detect the hidden-ref forbidden outcome. The unchanged pre-fix package evaluator produces the intended P08 red witness (metadata leak and revoked replay), while all other 56 semantic vectors still pass; this is regression detection, not a corrected behavioral pass. Independent implementers must align to this release and rerun. No protected deployment is qualified.

## 0.2.1-draft

Corrects judge-classified R7-014, R7-018, R7-019, R7-021 and R7-022. The canonical set remains 65 vectors: 57 semantic and 8 deployment; 52 clauses. Grammar and semantic profile identifiers advance together.

- **R7-014:** K-EVAL-5 combines necessary AND-premise states before preferring complete OR alternatives. Extended S32 has direct independent/retained controls, mixed AND limitation and a stronger complete current alternative.
- **R7-018:** runtime.dirty_causes records unresolved exact assertion/revision pairs. K-EVAL-8 filters each cause and affected path through current authorization; a global dirty bit cannot affect an unchanged public projection. S24/B07 preserve protected dirty inventory, public equality and a private-authorized dirty control. Completed recomputation must remove resolved causes, so old visible revisions cannot incorrectly explain later hidden invalidation.
- **R7-019:** publication currentness follows actual authorized publication-source associations. Admission class alone does not change an attributed mirror report to last_received. S23 adds a genuine unchecked-publication contrast; B03/S23 main currentness stays unchanged.
- **R7-021:** B01 now supplies the missing direct integration fact for its decision revision. Its expected report is unchanged. The checker gates facts for accepted writes and deliberately permits missing-fact refusal cases; the original omission and a bounded plant fail for the intended reason.
- **R7-022:** policy.subject_principals explicitly binds subjects to principals for self-declaration assertions, independently of opaque spelling and public aliases. P02 adds wrong-subject atomic refusal and valid own admission with distinct subject/principal strings; P10 retains valid delegated admission. Initial-state plants reject foreign self-attribution and equal strings lacking a binding. P15 uses a neutral organisation-issued fact for its exclusion controls.

The only new required snapshot fields are policy.subject_principals and runtime.dirty_causes. The former is trusted adapter identity evidence; the latter is protected unresolved invalidation provenance. Neither is a new semantic record, public identifier or authority registry. Existing fixtures must be migrated explicitly; a schema-valid old snapshot cannot be silently interpreted as a new profile.

Validation: all 94 JSON artifacts regenerate byte-for-byte; 20 intended structural checker violations are detected beside valid controls. Behavioral evidence belongs to independent evaluator reports. No protected deployment is qualified.

## 0.2.0-draft

Released at cde5754, upgrading the source kernel from v0.1 to v0.2 and addressing R7-006/008/009/010. Added P12–P15, normalized input tuple, three distinct conflict outcomes, frozen-view applicability, integration-established/unknown lineage, each constrained owner's current exact release, projection exclusion, qualified external restore witness and exact public-alias lookup.

Breaking grammar: lineage is a reference array or unknown; policy.lineage_facts supplies the integration's controlled input set; policy.constraint_owners and declassification_decisions supply per-owner release facts; disclosure.declassification is an array; declassify.assessments is plural; assessments pin a decision ref; runtime.revoked_declassifications records live revocations; revoke_declassification is an owner-event boundary stimulus; projection rules carry excluded_refs. P05 adds missing/revoked-owner controls; B10 adds a stale/current witness pair.

The 0.2.0 report contained 65 vectors (57 semantic / 8 deployment), 52 clauses and 16 checker controls. The later B01 missing-fact defect is corrected in 0.2.1; structural success in that earlier report was not semantic correctness.

## 0.1.0-draft

Producer package landed at 0ef608a with 61 vectors (53 semantic / 8 deployment), 49 clauses and 13 structural controls. Both implementers retain their independent first-run evidence for this version.
