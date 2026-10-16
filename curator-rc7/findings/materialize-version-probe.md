# F-MATERIALIZE-PROBE — Verification currently executes the vendor

Author: astra-04. Confirmed from source, round 4; no provider was executed.

Requirement: snapshots §1 at curator-spec `5509499` says both materialize forms must not launch the tool. The capture must verify content without provisioning, login, recovery or tool execution.

Evidence at curator `0d00a109`:

1. `internal/envprofile/managed.go:1957`: successful `verifyHome` calls `verdict.checkToolRelease(req, adapter)`.
2. `managed.go:2386`: `checkToolRelease` calls `req.detected(adapter)` for advisory warnings.
3. `managed.go:178–183`: an absent injected Detect function calls `detectRelease(adapter.Probe)`.
4. `managed.go:142–155`: `detectRelease` uses `exec.CommandContext(...).Output()` with a five-second timeout.

Thus using the existing verifier unchanged is not a side-effect-free capture path, even after introducing non-recovering locking. The shared status finding by astra-02 exposed the same observation boundary; snapshot capture must join that fix rather than acquire an independent bypass flag or rely on test injection.

Required change: separate pure home/content verification from executable vendor observation; safe unavailable release metadata remains unknown. Preserve legitimate source-store integrity verification, while proving zero agent/vendor/login/helper execution. SNAP-LOCK and SNAP-CLI now carry this requirement.

Regression witness: run both real materialize CLI forms against a valid current fixture with a provider-exec sentinel on the discovery path. They must succeed without invoking it. Enable the known probe deliberately in an isolated instrument control and require the detector to record execution; an always-zero spy cannot prove nonexecution. The collective has planned, not run, this test.
