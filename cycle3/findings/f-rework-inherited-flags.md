# Preserve inherited review obligations across worker rework

- **Lens:** R-TRANSFER adversarial pass; exact-candidate review binding.
- **Status:** proposed.
- **Author:** astra-15 (`ivmbp_swarma-review-3_astra-15`).
- **Topic:** `f-rework-inherited-flags`, root `$cw3U0GUdoywKik_fu6EqIU5-oj1HqfQqenmLWCd1Olc` in `#swarma-review-3`.

## Problem

R-TRANSFER makes an unaccepted candidate C1 the materialization base B for
the next candidate C2. The import flags sensitive hunks, and every new
candidate requires a fresh verdict. However, the contract does not define
the flagged-hunk set against an independently trusted integration baseline.
An implementation that flags only the new B-to-C2 change set can omit a
sensitive C1 change still present in C2. An exact-C2 verdict binds the
identity of the reviewed commit; it does not specify the complete set of
hunk acknowledgements that must exist before acceptance.

Concrete trace:

1. C1 changes `.agents/reviewer-policy.md` and `src/a`. Its review requests
   changes; C1 is not accepted.
2. The next round uses B = C1. The worker changes only `src/a`, producing C2.
3. A flag report computed from that round's export contains no sensitive
   hunk. The instruction change remains in C2's tree.
4. C2 receives a new verdict without a C2-bound acknowledgement of that
   inherited sensitive change. C1's old verdict cannot fill the gap because
   the contract invalidates it.

This is a missing review-contract predicate, not a claim of an implemented
or observed bypass. General review of C2 may catch the change; the mandatory
machine-checkable acknowledgement rule is underdefined.

The same gap affects unresolved web provenance. Section 4 records the
producing run's capability class and requires acknowledgement of incomplete
web-assisted provenance. If unaccepted C1 has that obligation, a web-free
C2 that retains C1 content receives no current-run web flag under that
rule. C1's parent trailers remain traceable, but no C2 acceptance predicate
requires surfacing and acknowledging the inherited unresolved provenance.
The later execution really was web-free; its classification must remain
accurate while the candidate retains a separate review obligation.

## Evidence

- `skill-project-management` at
  `d65cf7f9529d726b5e17e4654ac11b34c14765d4`
  (`origin/docs/worker-code-transfer`, PR #604 draft r6),
  `references/worker-code-transfer.md`:
  - Lines 371–386: import applies the exported change set to B and produces
    the flagged-path report and candidate C.
  - Lines 403–410: changes-requested C1 becomes the next admitted base, and
    the next export yields C2 on C1.
  - Lines 509–523 and 598–614: sensitive hunks require explicit
    acknowledgement; any new candidate invalidates previous verdicts.
    Neither passage defines a cumulative baseline for the flagged set.
  - Lines 545–555: web-assisted and incomplete-provenance flags are derived
    from the producing run; no rule carries unresolved obligations for
    content inherited from an unaccepted candidate into the fresh verdict.
  - Lines 886–900: the verification collector explicitly compares C against
    independently approved H, preserving inherited harness changes. That
    narrower report does not cover every instruction, auto-run or symlink
    path flagged by section 4, and does not supply their required
    candidate-bound acknowledgements.
- `swarma-dispatcher` at
  `19a75e63cd794f93c81c8c6fdb9d176eba1ed87c`,
  `spec/dispatcher.md` section 5.2, lines 317–318: the same flagged-hunk
  obligation and rework-from-C flow, with board ownership of review.

## Proposed change

Keep the materialization base and the review baseline distinct. Define one
trusted integration baseline for the candidate series, then recompute the
final candidate's complete review delta and sensitive-hunk set against
that baseline. Every sensitive change still present in C2 must appear in
its report, even if inherited unchanged from C1. Bind the baseline, flagged
set and explicit acknowledgements to the exact C2 commit OID.

Do not carry a verdict by patch equality. Recompute the obligations and
obtain fresh acknowledgements for each candidate. Sensitive content fully
reverted before C2 need not remain flagged merely because it existed in
an earlier candidate. Changing the trusted baseline follows the ordinary
base-refresh and re-review path. Keep the independently approved harness H
rule; H serves a different purpose and must not be substituted for the
integration review baseline by implication.

For unresolved web provenance inherited from an unaccepted candidate,
preserve a separate candidate-level review obligation without changing the
factual capability class of the current run. Bound inheritance at the
trusted integration baseline. Clearing requires a published conservative
provenance/removal rule or explicit exact-candidate reviewer resolution;
editing or rewording a hunk alone does not prove its dependency disappeared.
Use the candidate ancestry and recorded provenance to make the obligation
visible at acceptance. Already accepted trunk content need not propagate
the flag indefinitely, and an acknowledgement does not retroactively make
incomplete provenance complete.

Qualify an inherited instruction change, inherited symlink, successive
rework rounds, a reverted sensitive change, and a refreshed integration
base. Also qualify web-assisted C1 followed by web-free C2, with retained,
reworded and removed contributing content. In every case the verdict must
name the exact candidate and the complete required acknowledgement set.

## Expected benefit

Rework cannot make retained sensitive changes disappear from mandatory
review obligations. Reviewers and the board get one reproducible scope
for the exact candidate that will land.

## Risks and costs

The board must retain and validate the trusted baseline and recompute the
candidate-wide delta. Repeated acknowledgements cost reviewer attention,
but are consistent with the existing prohibition on verdict carry-over.
Inherited provenance also needs a conservative clearance rule; a tree diff
alone cannot establish that an informational dependency has disappeared.
This proposal does not change the owner-selected rework base or signed
fast-forward path and requires no new service or privileged component.

## Affected specs

- Board import draft, sections 3–5 and 12 (import/verdict/rework leaves).
- Dispatcher workspace contract, section 5.2, for the shared review rule.
- User-manager workspace-transfer summary and CIP-0009 D5a / remote-worker
  protocol, to keep their summaries aligned after the board rule is fixed.
- Book chapter 11, the code-to-main review and rework description.

## Confirmed by

- astra-18, trust-contract adversarial lens,
  `$6E85Xvw52RshNTlYv4ocbblYUDnCz-mhuon9ATV1m0Y`: independently checked
  draft r6 and confirmed that exact-C verdicts and H reporting do not
  define the inherited flagged-hunk acknowledgement set.
- core astra, simplicity/operations lens,
  `$RwcKEZW-Z9ywnxYl_aP2HohfPovqZsvkheAzeWFo4c0`: independently confirmed
  and recommended one trusted integration baseline with a recomputed final
  delta instead of an additional persistent flag ledger.

The inherited web-provenance refinement was independently confirmed in
the same topic by astra-18 at
`$LdPv_CsO0UoDrjOSwA6zw4EHXWUCVcEooeSPd7a2JZ0` and core astra at
`$ZSF57kJ3Sr11yhocKPhr8E0vfpn9P0VPcKQq8Weoi8U`. Both distinguish the
current run's truthful capability class from the candidate's unresolved
inherited review obligations.

All confirmations are in the finding's room topic. Review is documentary;
no builds, tests or source mutations were performed.
