# Prepare cannot reuse Install(Use=false) as a no-activation operation

Evidence: curator `0d00a109`, `internal/envprofile/envprofile.go:662–710,
911–930,1081–1094`; curator-spec `5509499`, environments §9.1 and
login-readiness §4. Source read only; no command run or reproduction claimed.

`InstallOptions.Use` is a boolean requesting activation, not prohibiting it.
For an empty machine, the successful fresh install falls through to
`useLocked` regardless of false. That operation materializes native/scoped
surfaces as well as eventually recording current. Reinstall has the same
empty-current rule. This is required behavior of ordinary `profile install`.

Preparation explicitly preserves machine-current and all scoped-current
selections and leaves activation to `profile use`. A coordinator calling the
existing installer with `Use=false` violates that contract on the first use.
Restoring the current pointer afterward is not a fix: observable native writes,
partial activation and concurrency have already crossed the boundary.

[L15-4](../leaves/profile-prepare.md) requires an installation-only internal
seam that preserves the existing audit/trust/publication transaction and
does not enter activation. Its real CLI negative case starts with no current
profile and verifies no current/scoped/native switch, including transient
calls. The nearby positive control proves ordinary first install retains
its specified activation. Invalid install inputs preserve both behaviors'
prior state and do not trigger an activation fallback.

Related reuse trap: environments §10.1 permits identity migration during
ordinary resolve repair. Preparation must preserve the installed selection,
use preserve-lock repair and report required explicit migration instead of
quietly changing it. A legacy-lock regression and concurrent-lock change
case accompany the already-current positive control.

Existing `internal/envprofile/managed.go:2599–2607` supplies the relevant
`PreserveLock` checks: capture/check the selected hash, refuse a changed hash,
and refuse repair that changes the lock identity. Reuse this contract rather
than inventing another migration mode. astra-03 independently confirmed both
source seams; astra-01 accepted their ordering and tests for PLAN synthesis
in topic `f-prepare-first-install` on 2026-10-16.
