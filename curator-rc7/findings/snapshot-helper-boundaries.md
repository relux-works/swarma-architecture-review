# F-SNAPSHOT-HELPERS — Existing helpers do not satisfy the export boundary

Author: astra-04. Status: confirmed by source inspection; no code executed.

Normative requirement: `protocol/managed-home-snapshots.md` §§2/5 at curator-spec `55094992185521dba470d80e1745d60af7bf496c` requires all-ancestor retained-handle no-follow destination access and non-recovering capture.

Evidence at curator `0d00a109ad1da77a5506747c89f24af9442eb341`:

- `internal/envprofile/nofollow.go:17–20`: `managedPath` explicitly permits components at or above root to resolve normally. It performs lstat checks and returns a pathname; `atomicManagedFile` subsequently opens/stages by path. This is the managed-home contract, not proof of the stronger snapshot destination contract.
- `internal/envprofile/lock.go:37–70`: `beginOperation` calls `beginOperationValidated`; both reach `transaction.Engine.Recover`. Adding only a validation callback does not make it a read-only acquisition.
- `internal/managerlock/managerlock.go:73–95,291–318`: `AcquireHomeOnly` invokes `prepare`, which can create manager directories. Retain the lock primitive, but explicitly prevent materialize from provisioning an absent source. Do not confuse ordinary lock bookkeeping with recovery or source population.
- `internal/transaction/engine.go:322–353`: recovery may commit, roll back or clean pending state. Materialize needs an observer of pending recovery, not a successful recovery invocation.
- `internal/snapshot/capture.go:233–280,326–393` implements source-package snapshot acquisition, using different identity/modes and pathname-based copies. Its name is not evidence that it implements managed-home-snapshot-v1.
- `internal/buildcache/protection_unix.go:18–49,108–143` demonstrates existing retained-descriptor patterns worth auditing for narrow reuse; it does not by itself prove all destination ancestors or publication.

Impact: a single large “reuse snapshot helpers and add CLI” leaf is unsafe and hard to review. SNAP-LOCK and SNAP-PUBLISH are independent acceptance surfaces, followed by CLI entry-point tests. Required controls are pending-journal preservation, linked-ancestor/target swaps and same-fragment ABA, each with a successful adjacent control.

No production vulnerability or observed data loss is asserted here: the new materialize command is absent from this source baseline. This finding prevents importing weaker contracts into its implementation.
