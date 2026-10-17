# Source implementation worklog

Seat: astra-22. Task: R7 source-derived independent evaluator.

## Reading boundary

Read before implementation: `memory/MISSION-R7.md`, `memory/designs/kernel.md`
v0.2, `memory/designs/bounded-support-semantics-astra-03.md`, and
`memory/designs/bounded-evidence.md`, at repository commit
`6d148282de0a3927e606f037b572134cc911d1f4`.
No `memory/spec/` file has been read. No other evaluator will be used as an
implementation source. There were no project-local skill files at the three
specified discovery locations. The a2a CLI's printed skill supplies room usage;
the mission's narrower ownership, direct signed main delivery and no-spawn rules
control this seat.

## Plan and status

1. Complete: pull, full brief/source reading, tool readiness and identity onboarding.
2. Complete: source-only semantic core and 20 local controls; baseline frozen before package intake.
3. Pending: after PACKAGE LANDED, write a wire adapter and run every package vector
   without changing the frozen core to match expected answers.
4. Pending: commit field-level results; report every disagreement to the judge.
5. Pending: apply only classified implementation corrections, rerun releases,
   finalize verdict and park note on PARK, and acknowledge in rounds.

## Required and forbidden behavior

The evaluator keeps polarity and computation completeness separate, preserves
conflicted premises, uses explicit sufficient rules only, filters authorization
before charging logical budgets, preserves historical cuts and attribution,
rejects invalid revision authority and stale expected versions atomically, and
keeps disclosure/lineage and publication effects separate from knowledge.

Forbidden outcomes to exercise include opposition from missing support,
contraposition, evidence laundering, hidden-record influence, arrival-order
supersession, dropping lineage, stale permission reuse, partial failed writes,
and side effects outside this evaluator's in-memory synthetic state.

Deployment claims (OS isolation, real retention sinks, timing distributions,
network permissions and external authority behavior) will be reported separately
and unsupported where no actual deployment experiment exists.

## Evidence

- `.temp/astra-22/readiness-01.log`: git, Python 3.14.7 and a2a readiness.
- Source rules and unresolved normalization choices will be documented in README.

## Source baseline validation

20 controls pass under Python 3.14.7 (`.temp/astra-22/source-checks-02.log`).
The initial temporal positive-control fixture accidentally put a simulated root
on a real assertion; the model correctly excluded it. The fixture was corrected
to make both simulated. No package was inspected to fix this fixture.
Self-review: source boundaries, no external side effects, independent polarity,
refusal atomicity and explicit limitations reviewed.
