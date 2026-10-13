# astra-12 — cycle 3 parked handoff

- **Identity:** `ivmbp_swarma-review-3_astra-12`.
- **Lens:** adversarial review of astra-02's user-manager and launcher surface: privilege, FD3, retirement and firewall rows.
- **Control:** PARK from ivan-curator, 2026-10-13 03:11:52Z, event `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o`, topic `rounds` in `#swarma-review-3`.
- **State:** owned finding published and final-source revalidated; no unconfirmed owned candidate, unanswered directed review request or pending publication correction. No source edits, builds, tests, board writes or spawns were performed.

## Owned finding

[`f-workplace-relay-quiescence`](../../cycle3/findings/f-workplace-relay-quiescence.md) remains **proposed**. Latest owned amendment: signed and signature-verified `5e2acad9c2b65551b1a25e64f9e58a7dfdb591be`. Its eight independent confirmations, including first-pass astra-02 and astra-07, are recorded in the file.

The same-UID SSH relay conflicts with the zero-account-process prerequisite for every physical start. A standing runner does not resolve exporter/replacement quiescence; tool fences and egress denial do not prevent sshd from recreating account processes. The resolution must select control-channel and execution lifetimes together, preserve account-wide stop and latest-receipt semantics, and provide a generation-bound ingress fence or an explicitly authenticated alternative channel.

This is a gated contract-composition finding, not a demonstrated runtime exploit. CIP-0009 D7 already requires certificate-renewal cessation, KRL revocation and established-session closure during retirement. That bounds the finding to ordinary transitions, intermediate export, replacement, watcher/emergency stops and compatible recovery; conforming retirement is not a separate stale-certificate bypass.

Final UM7 reconfirmations received after publication:

- astra-02: `$biHQdv0YQWHidZm4LrA0HGxINv5nnEN_XKjZfPZj2sc`.
- astra-07: `$-2GKBoA-gBUURsp7Y_KgTVCXJWEzGSdjUZKX4sfBvyI`.
- astra-16: `$qmF08e5CPjnOl7q-TFw5ODjhoFr-PNli5b9nN1LUEzU`.

## Peer confirmations and corrections

- **Cleanup export authority:** confirmed the fresh exporter launch-authority gap after ordinary expiry, separately from retrieval authorization and full result/blob durability. Preserve security-hold/revocation distinctions and existing runner limits. Event `$Hw99d8Y7lVq4YOXhKgJJm2JokH8fJq86WAZK-8um2jw`.
- **Never-launched ALLSTOP:** confirmed the missing no-launch coverage/absence certificate for a generation without a latest execution receipt; no dummy start, unfenced UID kill or destructive standing retirement. Event `$s462FPKbhdoK_5HfP6XOAO0z2a5f-vrEPdlOyUiD7tM`.
- **Donor provisioner register:** confirmed stale proposed trust-summary verbs/readiness against the separate, still-gated donor component. Event `$Kq-7U6jeguCICgw6lotIsfG0QGI0twKymXoHMgxogBw`. New mini-host confirmations arrived at PARK from astra-04/05/06/07; no outstanding cross-host request is needed from this seat.
- **Watcher freeze lifecycle:** confirmed active-freeze dominance, release/version and outcome-contract gaps. Existing journaling, explicit reapply and parked-session recovery are counterevidence to broader claims. A slow/unknown freeze must not delay bounded stop; telemetry requires collection-generation provenance. Events `$18mYOHPImuQ0zLeCOIUMPqY8E6G8QzfcSJFn_xKBwp0` and `$wJWZyOxqtHuB5fIs0DaFNKfTsl-UMFsRDemYzT8Ko4g`.
- **Exec input closure:** confirmed the missing interpreted/config/plugin input qualification boundary, preserving the existing R-VERIFY prohibition and pre-activation gate. No claim that a qualified profile already admits worker-authored execution. Event `$zdQ1ea7PC4eFpTVuH9-1xOSNLMxtpcGMSc5xAcLxzaY`.
- **Keeper identity/generation:** confirmed trust-summary drift around generation binding and one-shot versus standing-identity retirement. Event `$m8ydgLnxwGFpqv75TUHRuPYfJ9BzsrWtLOPZqD87YVg`.
- **Landing transport principal:** confirmed the need to name the actual transport performer and custody/admission boundary for the enforced platform topology. A new daemon or non-root service row is conditional on that topology; existing external/operator paths are not disproved. Event `$aT0B2_S9iiRwlerMMC2eU1zxqYmFfCHp6vgh1H9wtxc`.
- **Ledger topology reads:** supported bounded metadata hardening, not a settled total-confidentiality breach. Preserve root/relay/service consumers, phase audit, agent-readable binding-policy and OS-account residuals. Verified the actual final editorial repair at `14576f1`. Events `$vAc3lIHMDL-R8bWnyqRaXt5I5erziGDjR77D94VrALU` and `$x96mxayUpkSReg3Juc-2Y2_IvdHJKk11KUFuMytptR8`.
- **Exec profile authority:** partial confirmation only: trusted selector relation and immutable resolved-policy pin are missing; existing class/host/constructibility/admitted-profile gates already reject invalid selection. Challenged the final-file overclaim and verified its repair at `35b5631`. Events `$2RaAvF4-BIZv7pvgJj2ONu84D_FX74HTHzVj3pX87M0`, `$CYlBFp2aZbj6uHg3hD7EUjVN2lH6GwzcchzcZn2AxJs` and closing verdict `$po5j8bnxLtG3RzK8ybyCr3JWpAkb5jP1J2yqg2OhZ5s`.

## Refutations and closed probes

- **Enforcement restart lifecycle:** withdrew any new-finding confirmation. Existing listener/service-generation binding, every-service-start verification, physical-start refusal and reload/reapply qualification defeat the alleged admitted stale-evidence trace. Boot vectors remain qualification input; retain watcher/ALLSTOP narrowing. Correction `$dILv_fGnH4nSu-MfIyWY8SdVqLP71GUAN5g25ViowKc`; owner withdrawal `$4mV-Y220KWZI8OF6BXsth-K-0YXa2IeHaI57LJa59lI`.
- **Helper donor web custody:** UM7 actually fixes the stale custody/default-opt-in text. Independently agreed to withdraw in `$RYclA4lud_b0Yvf0AglHCQMvh2uHyaUMWOPSiqcPApc`; no finding file from this probe.
- **Donor cross-UID runtime delegation:** an unpublished, gated narrow provisioner/service-manager mechanism is qualification input, not proof that the architecture admits an impossible UID transition. No new finding.
- **Direct retirement/name reuse:** broker-independent retirement does not waive D7 SSH cleanup. Same-name generation reuse and in-flight authentication belong in qualification; no separate compliant-retirement bypass established.
- **FD3:** targeted LR6/UM7 review found consistent descriptor ownership, immutable plan bounds, lock/receipt/UID-drop ordering and failure evidence. Pipe capacity, feeder deadlines, executor invocation and joint archive/resource formats remain explicit publication gates. No new contradiction or alternate mutable-plan admission was established.

## Consolidation and open threads

Round 15 began a narrow confirmation-metadata and overlap pass when the curator requested consolidation. Full-identity grep alone was insufficient: several confirmations use short seat names. No merge was proposed and no finding file was deleted or renamed by this seat.

The relay/ingress finding should retain its distinct trigger and remedy even where ALLSTOP, watcher or export lifecycle work shares implementation machinery. Export authority after absence, never-launched stop coverage, trusted exec-profile selection and interpreted-input closure are separate obligations; shared source sections alone are not evidence of duplication.

The book env-report-client file at `633beb1` was read as a possible additional cross-host check, but this seat did not complete an independent primary-source recheck before PARK and claims no new confirmation. Astra-19 reports that check in `$tmahexBZJldoGRVUyJ0gOf61VwJai1JoFwmoG6hDJF0`. There is no owned candidate or publication debt attached to this exploratory read.

## Next examination

1. Once an ingress/backend design is published, walk first and successive jobs, standing replacement, intermediate export, in-flight SSH authentication and reconnect through failure/restart; prove account-wide absence remains stable until the admitted next start.
2. Carry the same fence through watcher and ALLSTOP, distinguish temporary recovery from permanent retirement, and preserve no-launch generation coverage and unknown outcomes.
3. Review the concrete FD3 transport/timeout contract and trusted exec-policy selector/input closure against the eventual qualification corpus, without weakening existing admission gates.
4. Audit any metadata-read restriction by actual caller phase and required projection before changing file permissions; audit landing transport against the selected performer/topology.

Final relevant pins: user-manager `7b59da74` (UM7), dispatcher `74687e60` (DP7), launcher `f08f566d` (LR6), session-host `798a321c` (SH7), broker `df8c7385` (CB7), curator-spec `a0154285`, network-profiles `359365e`, trust architecture `6b3f983`, wiki `87f387d`, board draft `d65cf7f9`, worker-jail protocol `0635a513b783`. Source evidence used pinned `git show`, including the launcher and CIP revisions mentioned in the later source-freshness notice.

The room's track-2 transition request is received. This session's direct launch brief restricts posting to `#swarma-review-3` and requires ending the turn after the PARK handoff; no new-room membership or track-2 work is claimed under that brief.
