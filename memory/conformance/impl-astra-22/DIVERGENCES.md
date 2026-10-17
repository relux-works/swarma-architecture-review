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
