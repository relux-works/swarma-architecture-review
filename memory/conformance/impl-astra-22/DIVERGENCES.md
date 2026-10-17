# astra-22 first-run divergences

All observations are from package 0.1.0-draft at `0ef608a` against unchanged core
`4d4ef45` (SHA-256 `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`).
The exact field differences and actual reports are in `runs/0.1.0-first.md` and
`runs/0.1.0-first.json`. No vector was edited. Classification is the judge's.

## ASTRA22-01 — Current-required unavailable evidence is incomplete

Vectors S12 and B13. Source clauses: companion §§4–6; kernel §6.1. Package
clauses K-EVAL-2/5. A root assessment requests current resolution of an erased or
unavailable source. The baseline correctly finds no witness, but marks support
`evaluation: complete` and emits no cutoff. The package expects `incomplete` and
`source_unavailable`. This is distinct from an absent root or retained assessment.

Recommended classification: impl-bug in the core's unavailable-current-root path.
The missing root must remain unqualified without silently treating failed
resolution as a completed check. Nearby controls should include resolvable,
retained, independent and hidden source inputs; hidden inputs must not create a
cutoff or spend work. No fix applied before this report.

## ASTRA22-02 — No-witness source state loses retained association

Vectors S12, B13 and S32 (also opposite channels of S32's positive controls).
Kernel §6.1/S32 and package K-EVAL-5 require unavailable associated evidence to
remain `prior_assessment_only`. The frozen core aggregates source state only from
found witnesses, so it reports `resolvable_now` for no-witness channels even when
a retained signature or documentary association names an erased source.

Recommended classification: impl-bug. Preserve separately authorized source
association without promoting signature/source binding into signed evidence.
The no-source case must retain the documented vacuous `resolvable_now` state.
S32's forbidden source-state predicate catches this defect. No fix applied yet.

## ASTRA22-03 — Wire source-reference mapping is incomplete

Vectors S23/B03 and S28/S29. All polarity, currentness and authority-order fields
agree; `source_refs` is empty where one exact associated source is expected.
The first adapter collects target-bearing assessments and source premises, but
does not collect the decision's authority receipt and non-root subject-pinned
assessment associations. This is output/provenance mapping, not a new root.

Recommended classification: impl-bug in adapter output. Include only separately
authorized exact source references; do not expose hidden sources or upgrade
mirror attribution to canonical authority. No fix applied before classification.

## Unsupported coverage

29 semantic vectors are unsupported by this initial wire mapping, principally
transactions, exact explanation paths, cross-assertion incompatibility, audience
redaction and dirty closure. Their full reasons are in the report. They are not
passes or package defects. Eight protected deployment vectors remain unsupported
because this seat does not exercise an actual protected deployment.

## ASTRA22-04 — AND-path source state is flattened across premises

Adversarial case `astra-24-mixed-source-state.vector.json` at `a46eb98` was run
against the same frozen core. Expected conclusion support source state is
`prior_assessment_only`; actual is `independent_attestation`. The core unions
source states across premises, then applies the preference that should apply
between complete alternative paths. One independent premise does not remove the
other retained-only premise's dependency on unavailable source bytes.

Recommended classification: impl-bug, subject to the judge's disposition of
ASTRA24-03. This run also reproduces ASTRA22-02 on two opposite channels, and
extends ASTRA22-03: derived conclusion source_refs misses its premise source.
Raw normalized actual reports and all fields: `runs/case-first.json`. Source
qualification must be joined across all AND premises before comparing OR paths;
provenance association must traverse found paths without exposing hidden inputs.
No correction has been applied.

## Classified corrections (current working revision)

Judge decisions: ASTRA22-01 = R7-011, ASTRA22-02 = R7-012, ASTRA22-03 =
R7-013, ASTRA22-04 = R7-015; all are impl-bug owned by astra-22. R7-014 is
the companion package clarification for mixed AND-path source states.

Corrections now implemented: unavailable current-required roots propagate
incompleteness/cutoffs; empty channels retain authorized source associations;
exact source references include documentary sources, authority receipts and
found premise assessments; AND paths preserve their weakest required source
state before OR preference. Source headers retain their own attribution and are
not filtered by the observer assertion's perspective; grants still gate them.

Validation: 24 source controls, one adapter visibility control and five harness
controls pass. Canonical 0.1.0 package: 24 pass / 0 fail / 29 unsupported semantic,
8 deployment unsupported. Supplemental cases: 3 pass / 0 fail / 11 unsupported
(`runs/case-corrected.*`). First-run evidence remains unchanged. Final closure
awaits judge verification of the published fix; unsupported coverage remains.

## ASTRA22-05 — Explicit self-declaration identity gate omitted

The unchanged new transaction mapping's first 0.2.1 f31d58f run fails P02.
`operation_results[1]` admits rec:foreign-interest/1 rather than refusing
`invalid_domain_value`. That forbidden write advances the sequence and makes
the valid own admission unavailable at its intended cut. Exact 15 field
differences and actual state are preserved in `runs/0.2.1-transactions-first.*`.

K-ENV-1 now supplies the explicit trusted subject/principal binding grammar
introduced by R7-022. The implementation validates issuer/submitter delegation
and own perspective but omits the subject binding. Recommended classification:
impl-bug owned by astra-22. Required regression controls: wrong subject refused
atomically, distinct subject/principal identifiers with a binding accepted,
equal spellings without a binding refused, and delegated own declaration accepted.
No correction was applied before this report.

## ASTRA22-06 / R7-025 — History escaped an explicit selection

Judge supplied a valid S24-derived static state at f31d58f with an unrelated
visible replaced sequence. Source 8b97e1e and independently rerun df499a1 return
that sequence's old reference when only rec:a is selected. K-EVAL-9 requires
history from the selected sequences only; K-REV-1 keeps distinct multi IDs in
distinct sequences. Classification: impl-bug astra-22, judge event
$NFG9lnMN_Ql0SjgWplmeYuSgEls8vZ1lCHuf8uJ-9YA.

The exact fixture and pre/post results are preserved in
`fixtures/selected-history.json` and `runs/selected-history-*.json`. Fix filters
visible historical refs by the full normalized selected sequence including space,
without changing unfiltered history or duplicating explicitly displayed old refs.
Three adapter tests pass, including the red-before/green-after regression and
hidden old-reference control.

## R7-026 correction

Judge event $gNzv1EBEGCjOIytU0Lp1_ddeF0ws8MUTAmojWZQMdvE classified ASTRA22-05
as impl-bug. Admission now enforces an explicit trusted subject/principal binding
and issuer-own perspective for self-declaration statement kind or intake class
before committing. Seven transaction controls pass; the three intended identity
violations were observed failing before the fix. P02 now exactly passes. Current
0.2.1 totals are 43 pass / 0 fail / 14 unsupported semantic. Both new fixes await
independent judge verification; historical first evidence is unchanged.

## ASTRA25-06 — Shared quality/existence budget (source defect)

Source 26d8cc6 independently reproduces adversary astra-25's case on f31d58f:
one A+ root and one checked A+ -> B+ rule suffice for B+, while A- is an
independent quality lookup. The shared topological counter visits A- first and
loses B+ at roots=1; roots=2 succeeds. Exact report and negative predicates are
retained in `runs/cases-0.2.1-first.*`. ASTRA25-01's visible control exposes the
same property; its hidden pair remains equal, so this is not a demonstrated
hidden-data leak. New unit regression is red before correction and a two-root
AND boundary remains correctly limited. Awaiting judge classification.

## R7-027 correction

Judge events $7rEaswg27z-hkIdE5isHAV_uJfgKZEugsBVak3pMDu8 and
$Dp4_riQyF6haSd2qyOmKMURbHNt2rkZrFJBDw9-Ctlw classify ASTRA25-01/06 and
ASTRA24-05 as one source counter-scope defect. The core now uses independent
depth-first existence and opposite-quality walks with local memoization and
stable reference order. Bounds are unchanged; genuine exhaustion still produces
incompleteness. Quality uncertainty does not consume existence counters or
create conclusion evidence.

All three case witnesses exactly pass, including their paired and forbidden
checks. Canonical 0.2.1 stays 43/0/14; current supplemental is 13/0/8. Twenty-nine
source tests, three adapter tests, seven transaction tests and five harness
controls pass. Exact original evidence is in signed f39af13; current outputs in
`runs/cases-0.2.1-corrected.*`. Judge review pending. R7-025/026 are judge-closed.

## ASTRA24-06 — Omitted current-source resolution bound

The root/quality correction at 4e647ea still fails the new ASTRA24-06 source
allowance case. Adapter did not pass source_resolutions into the core; a
zero-resolution query still found the one-source derived witness. Exact first
result retained in `runs/cases-source-budget-first.*`. Positive allowance one
passes. Recommended impl-bug; judge determines classification.

## ASTRA22-07 — Independent marker overrides resolved/empty sources

The retained source core chooses independent_attestation before testing whether
the named sources resolve. K-EVAL-5 explicitly puts resolvable_now first, including
an empty named-source set. A closed-shape S32-derived fixture with rec:att sources
changed to [] reproduces independent_attestation on 4e647ea instead of
resolvable_now. Input, exact query, output and single required field are stored in
`fixtures/independent-vacuous-source-first.json`. Recommended impl-bug; no fix or
canonical expected-output edit before classification. A prior source-level
stronger-alternative test encoded the same assumption; correction must preserve
its actual mixed-AND/OR claim while giving that independent alternative an
unavailable named source, and add empty/resolved/unavailable precedence controls.

## R7-028 correction

Judge event $_nHN4l4lurg4x7z88Ie7my2bKrY65tHxu33Tb4NG5j8 classifies ASTRA24-06
as a separate impl-bug. Adapter/core now enforce min(query, policy) distinct
current-source visits within each independent walk. Synthetic source groups carry
the original references; repeated resolution shares its visit, hidden candidates
cost nothing and retained/independent evidence is exempt. Zero-budget failure
withholds the unsupported witness and its derived source provenance. All exact
case fields and forbidden predicates pass. 32 source + 4 adapter + 7 transaction
+ 5 harness controls support the correction; canonical 43/0/14 and supplemental
14/0/8 semantic. First evidence preserved; closure pending. ASTRA22-07 remains
separate and uncorrected pending judge disposition.

## R7-029 correction

Judge event $R6pEZvOBTW2UVbOfj04NRa4KfMIWwHX2EYq2GMksDS4 classifies ASTRA22-07
as impl-bug and supplies a nonempty-resolvable neighbor. Both exact probes and
the unavailable independent control are retained. Resolution/vacuity now precedes
independent fallback. After normalizing snapshot values, only the two intended
support.source_state fields change; unavailable behavior is identical.

The source-unit assumption in the earlier stronger-OR fixture was made explicit
by adding an unavailable named source, preserving its real AND/OR claim. New
current/retained/independent controls reject the former empty/resolved priority.
33 source, 5 adapter, 7 transaction and 5 harness controls pass. Canonical remains
43/0/14; supplemental remains 14/0/8 semantic. Expected package/case outputs were
not edited. R7-027 is judge-closed; R7-028/029 fixes await independent verification.

## R7-030 — Initial snapshot idempotency ignored

Judge event $hbbJ9rJ7PJw8UKe81INSkYADsT_zK_WLJPPHBW3fgtQ classifies the separate empty transaction idempotency map as impl-bug. Full judge snapshot and source first output are preserved at f2c1570. The old path rejects exact/later-stamp replay and changed intent as duplicate_record. The correction derives replay lookup from runtime.idempotency and persists successful receipt entries there. Four new controls exercise initial state, reconstruction, actor/space/key isolation and current authorization, with original handle/time and atomic refusal assertions. Eleven transaction controls pass; exact judge operation differences are zero with unchanged state. Canonical remains 44/0/13. Closure awaits independent judge verification.

## Phase-2 supplemental first failures

Signed f2c1570 retains runs/phase2-expanded-first.* (30 semantic vectors: 17 pass / 2 fail / 11 unsupported). R7-032 classifies expired imported-publication currentness as source impl-bug; fixing it is queued next. ASTRA25-08 reports missing independent retain authority; classification is pending. Neither expected output is changed. Exact proof case ASTRA24-07 passes, preserving four paths versus two independent origins and cap-three truncation.

## R7-032 correction

Judge event $d-fCrpCafaGdZmlnjrNnqpKXqFOs7Um-npNJhPU8IJ8 classifies expired imports as impl-bug in both evaluators. Source correction follows kernel9.2 and K-PUB-2: publication association, admitted current check and unexpired horizon jointly constrain currentness. Known replacement stays historical; missing/unverified knowledge is last_received; ordinary mirror-report freshness is independent. Three red-before wire groups cover endpoint neighbors, source origin preservation, old capture immutability, missing/current/replaced facts and non-publication controls. Eight adapter controls pass. ASTRA26-07 passes exactly; S23 newly executes and passes. Canonical0.2.2 package7e71765 is45/0/12; pinned0.2.1 expanded supplement19/1/12, retaining R7-036 failure. Closure awaits judge verification.

## ASTRA24-08 — Ambiguous authoritative head accepted by CAS

During dirty coverage, the unchanged0.2.2 adversary pair independently reproduces the source defect: the primary returns revised plus a stored withdrawal instead of version_conflict/unchanged inventory; unique-head control passes. Exact first data is runs/phase2-dirty-targeted-first.json, with twelve comparison differences and all implementation/input hashes. The head helper follows target revision links without establishing a unique authoritative slot head. Await judge classification before correcting; no expectation changed.

## R7-040 correction

Judge $jWF7PS9bJWLBKtoGF2OqBiJIlvcfYJB7WzuI6j5fxPw classifies ambiguous and historical authoritative candidate acceptance as one source implementation bug. The head helper now selects a unique maximal canonical receipt over the exact full slot before following local CAS transitions. Target naming cannot resolve incomparability or select a historical candidate. Original first outputs remain e38c37c and5d079be; corrected exact four-case family is in runs/phase2-cas-cases-corrected.*. Thirteen transaction controls pass, including atomic full-state refusal, unique head, challenge, later common-successor admission and exact replay precedence; red-before evidence is transaction-checks-11-red.log. Canonical49/0/8 unchanged, current41-case supplement31/1/9. No expected output changed; independent closure pending.

## R7-043 — Changed rule/check did not invalidate target

Judge $lXcUN46jxrVt_c0amm5LNbwyvqnzNvPyTOc6omMPOmk supplied two validated S17 derivatives and a passing premise control. Inputs and judge/source first results are immutable at4744e62; both failures previously omitted global causes and public dirty/incomplete state. The registered dependency set now includes its own justification and certificate refs. All three exact vectors pass, with nine native impact controls covering hidden/private and challenge separation, transitive closure, pre-cause cut, recomputation, replay and zero-budget dirty handling. Full canonical remains49/0/8; current43-case supplement33/1/9. Correction evidence: runs/dirty-rule-certificate-corrected.*; independent judge closure pending.

## R7-040 NEXT completion

The original four-case correction omitted active-candidate filtering. ASTRA24-08-NEXT and judge $BSYR9IhidtbVLFuL40uRFVy2WnLYNDLe4_GprgvY60I require withdrawing the remaining current authority candidate after the latest was withdrawn. First failure and red control are signed bd75f4f. Authority CAS now selects among non-withdrawn candidates and uses that exact reference; ordinary revision tokens cannot override authority order. Fourteen transaction controls and all five CAS fixtures pass with pinned0.2.2 grammar; full code/input hashes and results are in runs/phase2-cas-next-pinned-*.json. Judge independent closure remains pending. The concurrent0.2.3 release is separately red on retention P11/P13 and old-fixture shape/profile migration; no successful0.2.3 retention claim.

## R7-036 — Exact retention authority correction

The independent-retain implementation defect follows the explicit R7-039 release23290b3. Admission/revision now check fixed actor, each resolved record's space/id and one declared audience/purpose across outputs and transitive complete/unknown integration inputs. Current checks precede receipt replay. Missing authority refuses atomically without changing the stored receipt; output labels and metadata grants do not substitute. Original canonical first47/2/8 remains99b5a85, and own eight control groups preserve12intended old failures in runs/retention-controls-first.json. All eight now pass. Canonical0.2.3 is49/0/8; author-migrated46-case supplement37/0/9. All four retention cases pass, including the transitive unknown lower-bound pair. Reports: runs/phase2-retention-corrected.* and phase2-retention-cases-corrected.*. Eighty-nine controls pass on current grammar; judge closure pending. No expected case or package answer changed.

## Declassification expansion first mismatch — unframed output digest

First wire expansion runs/phase2-declassification-first.* is49/1/7; matching supplemental first is37/1/8. P05/ASTRA25-02 valid release rejects because releases.py compares raw canonical-body SHA-256 instead of K-JSON-2 framed sha256-cjson-v1. The supplied expected digest is5de83fb8e3155c49b882fb716b571a54038bee18f06cc1989900cb49b16c2a3b; the unframed computed digest is c47edea8d46ce4fd367b430ade8f53aa72a2b7e44a8902193cd87ab939a4a63c. Both cover synthetic city body only. Evidence and implementation are frozen before correction; judge classification requested. This is an implementation mapping candidate, not a claimed spec failure.

## R7-050 correction

Judge $Jxqff_h8h6pJHraJVkiriHrvMIYcTlLKLCO1QAjUMuI confirms source impl-bug. releases.py now hashes ASCII bounded-evidence:cjson-v1, a single NUL, and canonical UTF-8 body bytes exactly as K-JSON-2 requires. Both ASCII/Unicode framed positives and raw negatives pass with atomic-state checks. Nine release control groups pass; the later private-rule test setup correction is separately documented. Canonical50/0/7, supplemental38/0/8; P05/ASTRA25-02 exact. First36983de and native firste1ba8db remain immutable. Corrected reports are runs/phase2-declassification-corrected.* and phase2-declassification-cases-corrected.*. Judge closure pending; no package/oracle change.

## R7-047 strict successor correction; R7-051 kept separate

R7-047 first52-case output and six native forbidden-acceptance witnesses are immutable64ef86e. Authoritative replace/correct now require a strictly succeeding canonical receipt; CAS and exact replay stay separate. Four native groups and14existing transaction groups pass. Canonical50/0/7; current54-case supplement44/2/8. Remaining failures ASTRA24-10-TRANSITIVE and ASTRA24-11 are the distinct R7-051 query adapter defect, classified by judge $lL-KfgsFVYJ8Kpol9-2KlrnISzbIcOa-A7-1Pv5Z2-k; their first actuals are preserved before changing projection. Strict successor write correction awaits judge closure. R7-050 is judge-closed at8a42945; original release failures remain unchanged.

## R7-051 projection correction

The wire adapter now traverses complete canonical receipt ancestry by issuer, then relates exact same-sequence/space assertion candidates. This preserves transitive ordering through receipt-only intermediates without creating candidates, weakening visibility, or imposing arrival order. Four native groups and all106current controls pass. Canonical0.2.4 is50/0/7; current54-case supplement46/0/8. B01 and both original transitive/read-only cases are exact. First0.2.4/natived5f07be and earlier64ef86e/4772258 reports remain immutable. Closed-shape test setup corrections and B01/profile control maintenance are documented separately in WORKLOG. Judge closure pending; no expected answer or package edit.

## R7-052 current retention expiry correction

Judge $JPRw0HAxhQiEJ-rN4erBtnvRBnBXixLi2Rap_jcFAN0 classifies source052/package053/spec054; release6a04e8c pins strict time, not_authorized,false and ordering. First nativec9e1faf exposes17intended failures; first full0.2.5 on exact old transaction bytes is49/1/7, P11 only. Retention checks now require current trusted context.at before every non-null deadline in the proposed outputs and resolved transitive known closure. Exact replay and different-intent key reuse cannot bypass expiry or change stored receipts. Six deadline groups pass, including all four intake APIs, own/transitive/unknown/same-batch sources, null/unrelated neighbors, both batch orders and duplicate-identity authorization priority. All112controls and canonical50supported vectors pass; seven canonical gaps remain. Supplemental author profile migration is separate and pending. Current reports are runs/phase2-deadline-corrected.*; full green native evidence is runs/deadline-controls-corrected.json.052 closure awaits independent review.047/051 are judge-closed at4772258/427fed5.

## ASTRA22-08 — Initial degraded availability cannot recover

First erasure/load coverage implements set_availability by toggling runtime.memory_available, while reads still also check policy.public_availability. An admitted initial degraded public state with coarse_unavailable, owner operation state=available, and otherwise identical S27 query returns availability_changed but stays unavailable. Nearby available -> degraded -> available control passes. K-NI-3 permits the owner transition under the predeclared coarse policy; the success receipt should reflect the requested current availability. Full closed-shape input/actuals and first red native control are runs/availability-recovery-first.json. No exact vector changed: all57canonical and61supplemental semantic cases pass. The125thnative/comparator control fails; prior124pass. Await judge classification before changing current public availability mapping.

## ASTRA22-09 — Erase changed-context versus replay metadata priority

Unclassified native probe in runs/erase-changed-context-first.json: a successful private/read erasure stores visible A/D refs; same identity with an ungranted receipt purpose returns not_authorized; identical changed-purpose fresh-key erase succeeds with an empty receipt. Current operation authority remains present and full state is preserved on refusal. K-API-1 says a changed receipt_context is a conflict, while stored-ref current metadata authorization is described for replay. Recommend digest conflict before receipt metadata gating for non-identical requests, after current erase authority. Await judge classification; no oracle/code correction or foreign evaluator comparison is claimed.

## R7-056 initial public availability corrected

Judge $JwiSCClsftcbsOR8UrOJoe2h7NZWY12YYcjSgWm4S6c classifies ASTRA22-08 as source impl-bug. The owner transition now updates current public availability as well as the existing runtime availability stimulus. All four state transitions, non-owner/undeclared/malformed atomic refusal and logical-load/control neighbors pass. Public and runtime state changes are isolated; policy pins/grants and all unrelated state remain exact. Original dbf4892 first and expanded stale-policy matrix remain immutable. All125controls, canonical57/57 and supplemental61/61 pass; evidence is runs/availability-controls-corrected.json and phase2-availability-*. Judge closure pending. ASTRA22-09 remains separate and uncorrected.
