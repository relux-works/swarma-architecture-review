# sol-14 parked — cycle 3

- **Seat:** `ivmbp_swarma-review-3_sol-14`, scenario lens on ivmbp.
- **Status:** parked, 2026-10-13, under ivan-curator's PARK event `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o`.
- **Published findings:** none. No owned candidate, unconfirmed finding or unanswered directed request remains.

## Completed scenario cut

The seven full flows were already owned by sol-01/02/03/11/12/13. Coverage coordination selected a distinct residual: an off-host verification result for J1/C1 arriving after C2 or protected-trunk movement, through historical result recording, current testing-state progress and exact-C landing.

Board draft r6 at `d65cf7f9529d726b5e17e4654ac11b34c14765d4`, `references/worker-code-transfer.md`, supplies the decisive boundaries:

- §§5/7: exact-C/H job inputs, pool-signed results matched to the requested job, and no predecessor-verdict carry-over to a new candidate.
- §§9/12: exact signed non-forced C landing, fresh protected-ref resolution, and ordinary base refresh with re-review. Tree-only and patch-containment close proofs are excluded.
- §§7/11/12: the receipt-to-testing adapter remains a publication gate. No contrary published transition was found; no stale-green landing or implemented adapter was inferred.

The cut is **publication/qualification input**, not a new confirmed contradiction. Historical J1 data must not satisfy or regress C2's gate. No amendment to `f-verify-network-phase` is proposed; its N16 phase-propagation scope remains separate.

Peer closure in that existing topic:

- astra-05: `$bXuQQ4DyVljsABg4FOVZYSurjfmwzNNkbe9Mgl8jDnQ`.
- astra-15: `$cm16pqFpZjYGAY_MytFsSbhX8lrlDJ4flgfBa62rZVQ`.
- sol-01: `$rgzp4zQeumQWaNqWDSPtqAbzaa74AHaJQcciSVFXsH8`.

Additional ordinary-kernel precedent was independently read at `skill-project-management@6fb1e4ff38eb7b94138d070ccda2ae78b36b2cd3`, `.specs/validation-binding.md:3-6/104-123` and `.specs/separate-owner-completion.md:145-166`. It is not proof of the future R-VERIFY adapter and is outside the older-checkout peers' source confirmations. The branch-justified already-checkpointed replay exception does not authorize cross-candidate result reuse.

## What to examine next

When the verification-wiring leaf is published, check current candidate/request identity at the progress mutation and again during recovery. Preserve separate durable historical receipts. Include late success and red results, duplicate delivery, infrastructure retry, equal-tree/different-commit C1/C2, trunk movement, and a crash between result recording and testing-state advancement. Preserve at most one infrastructure retry and no retry of genuine test failure. No particular CAS encoding or new wire field is required by this review.

## Quiet-period audit

At review `dc14ab7`, eight sampled findings already had both-host confirmations in files or topic history: archive/egress examples, resume/env-report, donor provisioner/mailbox, inherited flags and goal authority. Short aliases and post-publication confirmations explain the apparent file-only gaps. This was a bounded audit, not an exhaustive 42-file coverage claim; no redundant ask or merge proposal followed. The owner-withdrawn provisioning-activation finding was not carried forward as proposed.

## Evidence and limits

Final announced source pins examined: wiki `87f387d`, dispatcher `74687e6`, broker `df8c738`, host `798a321`, user manager `7b59da7`, launcher `f08f566`, CIPs `a015428`, trust contract `6b3f983`; worker-jail protocol `0635a513b783`.

Detailed local notes and readiness evidence remain under `.temp/sol-14/`, particularly `scenario-walk.md` and `source-pins-01.log`. Only this parking note is committed. No source edits, task-board writes, builds, tests, spawns or web access were performed.
