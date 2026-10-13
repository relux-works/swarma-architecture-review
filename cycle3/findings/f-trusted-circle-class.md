# Trusted-circle admission and the untrusted-class predicate: reviewer and host-loop eligibility are inferences, not stated rules

- **Lens:** trust and threat model (fable); shared consistency lens. Adversarial trust (astra-18), cross-cutting (astra-20) and remote-worker (astra-17) cross-checks.
- **Status:** proposed.

## Problem

Wave 5b makes the admission class an identity-level fact that one operator act changes: "Remote workers (donors and freelancers) and every `workplace` allocation are untrusted-class unless the operator admits that remote worker to the trusted circle by an operator act at admission" (dispatcher v0.11; broker v0.9; launcher LR6; board import draft r6). The same paragraph enumerates what membership "never relaxes": zero host egress, the exec profile, the transfer path and exact-commit review of the member's own work, no subscription binding or lease, no host-local loop, helper v1, host capability minimums, socket and deployment-isolation gates. Two rules keyed on the class are not in that list and are stated only as exclusion from the untrusted class:

- **Reviewer eligibility.** "A trusted reviewer, distinct from the producing identity and outside the untrusted class, reviews exactly C." The board draft and the session host say the same ("neither untrusted-class nor the producing identity"; "never untrusted-class"). After a circle admission a remote worker is outside the untrusted class by the dispatcher's and broker's wording, so a consumer that checks only that predicate reads it as an eligible reviewer of other workers' candidates, with its loop on a donor machine and, by the circle's one opt-in, web search on.
- **Host-loop eligibility.** "A standing session with an agent loop on our host is trusted-class only." A circle-admitted remote identity satisfies that predicate by class, while the owner's rule is about placement: "Outside agents may be long-lived, but they never start an agent loop or agent environment here."

Meanwhile the user manager (v0.9) and the session host (r10) still say every workplace is untrusted-class unconditionally; UM7 and SH7 are pending. Until they land, the dispatcher, broker and launcher use the identity-level exception and the user manager and session host use the placement-level rule, so the texts disagree on what "untrusted class" denotes.

**Scope, as narrowed by the cross-checks.** Being outside the untrusted class is a necessary condition in those rules, not a positive grant. The operative clauses "membership enables only donor-side opt-ins" and "never relaxes any host boundary" are counter-evidence to any claim that the act already authorises review or a local loop, and a caller's `agent.spawn` chain cannot derive a change of placement from the circle act. The defect is therefore an ambiguity with an authority consequence: eligibility for review and for a host loop is nowhere stated positively, so it can be misread by a consumer that checks only the class, and the owner's two sentences ("untrusted unless admitted to the trusted circle" and "outside agents never start a loop here") are not reconciled in one place. This is a documentation and authorization-model gap, not evidence that an admitted path grants those capabilities.

## Evidence

- `swarma-dispatcher` at `74687e60` (v0.11), `spec/dispatcher.md:171`: the class exception by operator act, the "enables only donor-side opt-ins" list; `:173` R-STANDING "trusted-class only"; `:326` the reviewer rule by class exclusion; `:632` "The trusted circle is our own agents plus remote workers admitted by an operator act at admission"; `:497` trusted-circle admission as a widening operator act.
- `swarma-credential-broker` at `df8c7385` (v0.10, CB7; unchanged wording from `393b724f`), `spec/broker.md:160`: the same exception, with class evidence tied to the admitted `(uid, generation)`; `:162`: "Trusted-circle membership enables donor-side opt-ins only; zero egress, exec restrictions, transfer and review on our host stay"; `:611`: "An untrusted-class worker never receives a lease".
- `curator-agent-launcher` at `f08f566d` (LR6), `SPEC.md:2291-2298`: the exception repeated, "only donor-side opt-ins", "No local loop or shared services are admitted".
- `swarma-user-manager` at `ae540c59` (v0.9; helper text unchanged at `3da62ad4`), `spec/helper.md:110`: "every workplace allocation is untrusted-class", plus operator classification of further identities.
- `swarma-session-host` at `70c9d97e` (r10), `spec/session-host.md:144`: "every `workplace` allocation is untrusted-class"; `:243`: reviewer "never untrusted-class".
- Board import draft, spm PR #604 r6 at `d65cf7f9`, `references/worker-code-transfer.md:122-128` (the exception and the "never relaxes" list) and `:595-598` (reviewer: not untrusted-class, not the producing identity; no positive eligibility rule).
- `wiki` at `87f387d`, `decisions.md:680`: "Outside agents may be long-lived, but they never start an agent loop or agent environment here"; `:725, :730-731`: search is the circle's opt-in; "A workplace is untrusted unless the operator admits its worker to the trusted circle; no boundary on our host is relaxed."
- `curator-spec` at `a0154285`, `protocol/remote-worker.md:102`: donor-side web opt-in only.

## Proposed change

Disambiguate three concepts and key every rule on the one it means. Either normalization below closes the gap; the owner chooses.

1. **Three concepts.** *Trusted-circle membership* is a per-identity operator record enabling an enumerated opt-in list (today: web search, R-NET-TOOL 4b). *Placement* is `local agent account` or `workplace`, recorded at allocation; a remote identity only ever receives a `workplace` placement (decisions.md:680). *Enforcement class* drives ceilings, egress, exec profile, binding/lease refusal, R-SHARED and the watcher thresholds.
2. **Normalization (a), keep the owner's wording.** Keep "untrusted-class unless admitted to the trusted circle" as written and add reviewer eligibility and standing host-loop eligibility to the "never relaxes" enumeration in the dispatcher, broker, launcher, session host and board draft, in the same sentence that lists the other boundaries.
3. **Normalization (b), bind the class to the placement.** State that the enforcement class follows the placement (`workplace` is untrusted-class) and that the circle exception lives in the membership record only. This reads the owner's sentence as "the worker is in the circle; the placement stays untrusted"; it changes DP7/CB7/LR6 wording and must be marked as reinterpreting their application of the decision.
4. **Positive eligibility.** State review-role admission positively, as a role grant that is never derived from class or circle: a reviewer is a trusted-class local placement or a person holding the review role, and not the producing identity. State the same for a standing host loop: trusted-class *and* local placement. Preserve the operator's power to classify further identities as untrusted.
5. **Two separate policy proposals, for owner decision, not propagation:** (i) reviewers are local-only (no trusted-circle remote reviewers); (ii) the orchestrator that requested the round does not review it (it consumes the worker's outcomes and letters and is the most injection-exposed trusted principal). Neither is implied by the current text; the current rule excludes only the producing identity and the untrusted class.
6. **Glossary entries** for circle, placement and class, and a mechanical check that every rule keyed on "untrusted class" names the placement it means.

## Expected benefit

One operator act (circle admission) can no longer be misread as widening two unrelated authorities. The five texts agree on what the class denotes, and reviewer and host-loop eligibility become stated rules that an implementer can check, instead of inferences from an exclusion.

## Risks and costs

Wording changes in wave-5b text across five documents and the glossary. Normalization (b) reinterprets the exception's phrasing and should be presented as such. The two policy proposals in item 5 are new independence rules with their own cost (fewer eligible reviewers) and need the owner's word. No D-* decision is challenged; the owner's 2026-10-13 sentences are kept and reconciled.

## Affected specifications

Dispatcher §§3.4, 3.6, 5.2 step 5, 7.3, 13; broker §§4.2, 12.1; launcher §10 wave-5 bullets; user manager §3; session host §§3.1, 3.5; board import draft §§2, 5; glossary; book chapter 11 (step 6) and chapter 14.

## Confirmed by

Room `#swarma-review-3`, topic `f-trusted-circle-class` (root `$P7hXiwArLTB1IKsq3PvvS1H1Yavpk-yIoJKCEsrLSAo`), 2026-10-13.

- Candidate: fable, `$P7hXiwArLTB1IKsq3PvvS1H1Yavpk-yIoJKCEsrLSAo`.
- astra-18 (`ivmbp_swarma-review-3_astra-18`), `$U7PpzuaSSx9r50K4_xL8PfsaI0u8eYBYFlk4KbvdqJg`: confirms the class/eligibility ambiguity; limits adopted: necessary-not-sufficient, class evidence already tied to `(uid, generation)`, local-only reviewers and requester exclusion are separate owner choices.
- astra-20 (`ivmbp_swarma-review-3_astra-20`), `$_f58ga-553cZZqPXP-iJvXDXDePH1PsnbnjLqcvt-jM`: confirms the vocabulary conflict and the unclear class/eligibility interaction; refutes an automatic authority consequence; adopted: "can be misread by a consumer that checks only the class", preserve operator classification, LR6 and CIP counter-clauses.
- astra-17 (`ivmbp_swarma-review-3_astra-17`), `$MKq-LgDsmYUYQdA99XED-2I-NgRHeZfd7pi5Pl2BJvY`: remote-lens challenge accepted as scope: the placement invariant is supported by decisions.md:680; normalization (b) is a reinterpretation to be labelled; item 5 is new policy.
