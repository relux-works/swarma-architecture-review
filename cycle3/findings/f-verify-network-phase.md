# Preserve N16 fetch-only egress and offline execution in board verification

- **Lens:** R-TRANSFER; cross-spec consistency; verification isolation.
- **Author:** astra-05 (`macmini_swarma-review-3_astra-05`).
- **Status:** proposed.
- **Topic:** `f-verify-network-phase` in `#swarma-review-3`, root
  `$pzJwFtIdyL6ffmgmEtFLykN6ZR5rHdlQfZ0g6U9C3IU`.

## Problem

The board import draft's concrete runner recipe describes dependency
connectivity at job scope: use `GOPROXY=off` for fully vendored jobs,
otherwise let the job reach the Go module proxy and checksum database.
Its qualification checks cover credentials, internal routes and residue,
but do not establish the network boundary between dependency fetching and
candidate execution.

N16 specifies that boundary for this exact consumer: fetching runs no
candidate code, install scripts or build hooks; build and test then run
without external networking, a resolver or the job's egress-service
socket. An unfetched dependency fails offline. The board draft names N15
and its allowlist/cap values but does not carry N16's phase ordering into
the recipe, job lifecycle or qualification.

For example, a non-vendored candidate's test could contact an allowed
module endpoint in a runner that implemented only the draft's job-wide
allowlist. That runner would violate N16. The same problem applies to a
vendored candidate: `GOPROXY=off` controls Go dependency resolution, not
the candidate's ability to open connections. Approved harness H, separate
H/C caches, no secrets and no internal route do not establish offline
candidate execution.

The draft already says dependency egress follows R-NET-TOOL. It therefore
does not grant permission to override the stronger owner rule. This is a
propagation and qualification defect in the concrete draft contract, not
new network authority or an implemented bypass. Its existing gate against
using an unqualified pool remains valid.

## Evidence

- `skill-project-management` PR #604, draft r6 at
  `d65cf7f9529d726b5e17e4654ac11b34c14765d4`,
  `references/worker-code-transfer.md` (local review copy
  `swarma-review/context/inputs/worker-code-transfer.spm-pr604.md`):
  - Lines 711–714 retain the general R-NET-TOOL dependency-egress rule.
  - Lines 819–876 isolate trusted H drivers and candidate execution;
    these are integrity boundaries, not a network phase transition.
  - Lines 983–991 refer the network contract to N15.
  - Lines 1045–1056 describe job-wide registry/checksum connectivity and
    H/C cache separation without the fetch/offline-execution split.
  - Lines 1076–1081 qualify credentials, internal routes and residue,
    without N16's offline-execution and disabled-fetch-hook controls.
  - Lines 1261–1274 name infrastructure and N15 dependency-egress values,
    without carrying N16's already selected phase boundary.
- `curator-network-profiles` at `359365e`,
  `spec/network-profiles.md`, N16 lines 238–244: this is explicitly the
  board verification consumer; items 1–2 separate fetch from offline
  build/test and withhold the egress socket from execution; item 5 binds
  the fetch log to the candidate digest.
- The same revision, `docs/harness-verification.md`, lines 132–134:
  V1 probes outbound packets and name resolution during build/test; V2
  qualifies permitted fetches; V3 probes disabled install/build hooks.
- `wiki` at `87f387d`, `decisions.md`, line 724: the owner-selected
  runner path fetches without candidate code, then builds/tests offline.

## Proposed change

1. Reference N16 explicitly in board sections 7–8 and their implementation
   and dependency lists. Make its two phases part of the concrete recipe
   and job lifecycle, for both vendored and non-vendored candidates.
2. Fetch only from the admitted dependency inputs, with install scripts
   and build hooks disabled and no candidate code running. Preserve the
   existing independently approved H inputs and H/C cache separation.
3. Before candidate execution, establish the qualified offline sandbox:
   no external interface, no resolver and no egress-service socket or
   inherited route to it. N16 permits loopback; this is not a blanket
   prohibition of every local socket. Missing dependencies fail instead
   of reopening the fetch route while candidate code runs.
4. Bind fetch evidence to the candidate in the job result, and include
   N16 V1–V3 with positive controls in the board pool's pre-activation
   qualification. Exercise both vendored and non-vendored jobs.

## Expected benefit

The runner recipe and its acceptance checks enforce the existing owner
boundary directly. Candidate tests cannot inherit dependency-fetch
authority merely because they run in the same logical job.

## Risks and costs

The runner contract must express and qualify the phase transition and
candidate-bound fetch evidence. Incomplete dependency inputs can fail a
build offline; that is N16's intended behavior. No new service, proxy,
numeric cap, repository mutation or owner-decision change is required.
No build, test or live network probe was performed in this review.

Final-corpus recheck on 2026-10-13: user-manager UM7 at
`7b59da740037865dd42936982e5a069ea05eab53`, `spec/helper.md` lines
439, 486 and 548–555, retains off-host verification ownership in the
board/infrastructure lanes. Its network, web and task-resource alignment
does not change the board r6 recipe or N16's fetch/execution split.
This finding remains proposed at the final announced source pins.

## Affected specs

- Board import draft sections 7–8, 11 item 6 and 12 verification wiring.
- N16 and its V1–V3 qualification rows as the existing contract to reuse.

## Confirmed by

Independent confirmations in the same room topic, 2026-10-13:

- astra-15 (`ivmbp_swarma-review-3_astra-15`), R-TRANSFER adversarial lens,
  `$g-H5n141Tc0Mut5uR1XjO-Yx35m99-6R1TNumIWWVsg`: confirms the concrete
  recipe/qualification omission; preserves the general R-NET-TOOL rule
  and distinguishes `GOPROXY=off` from enforced offline execution.
- astra-16 (`ivmbp_swarma-review-3_astra-16`), network adversarial lens,
  `$QoNskLMD1aDTO0761mE2A6vmwzxOMBQ13ppYFcKTFIo`: independently confirms
  the N16 propagation defect, candidate-bound fetch evidence and both
  vendored/non-vendored scope; preserves loopback/local control and the
  existing unqualified-pool gate.
- astra-06 (`macmini_swarma-review-3_astra-06`), network first-pass lens,
  `$iyPVUdylNQe0QVrVlG3yBkVmqvImYBnwokY69A6VdjU`: independently confirms
  the phase-boundary omission at N15/N16 and board r6; requires a
  post-fetch candidate-code probe against proxy/resolver access and
  distinguishes `GOPROXY=off` from an OS boundary.

The peers' scope corrections are incorporated above.
