# rev5 parked review record

Identity: `macmini_swarma-review_rev5`. Lens: cross-spec consistency and mechanically checkable invariants. Date: 2026-10-12.

Parked on the convener's PARK decision `$EB6OzWXmhe2CPevdsra59AzLdOCV0XXzznaJEQfDJUk` in `#swarma-review`, topic `rounds`. Findings base: `78c1bf43954944022a180ccb565936f6320f6ed5`; its Git signature verified locally. F-1 through F-11 are independently confirmed proposals awaiting the operator's decision. No source specification was changed.

Four rounds completed. Round 1 independently validated ten peer candidate topics; rounds 2–4 added no candidate or new confirmation. The last round marker is `$RtujSdv40hL4PeVHU_nr0PmZqDZjhbyrGRWDnD773Ns`. I authored no finding entry: the concrete improvements I could substantiate were already owned by peers, and the remaining differences were either explicitly superseded wording or unpublished activation contracts.

The full Russian book and the helper, dispatcher, broker and session-host specifications formed the review baseline. Relevant launcher, credential CIPs, architecture source-precedence and VISION contracts were cross-checked. Review was documentation-only, with no builds, tests or implementation qualification.

Independent validations posted by rev5:

| Finding | Candidate topic | rev5 answer event |
| --- | --- | --- |
| F-2 | `f-standing-cutover` | `$bcbXKgWtqOSRJDzPEpYrIqO2W5szL2MCpzzCAaTsGyM` |
| F-3 | `f-orchestrator-delegation` | `$6y0QLBKcZleFZ3Vvy241_v0Ng4vFC4mMD6maXrvTRNk` |
| F-4 | `f-single-launch-authority` | `$m_bFMyRavx7484dc-vkFflFFDjC1SjG7FdgCl92KWL4` |
| F-5 | `f-daemon-first` | `$mtkKsH1wGiousYp36f-ZKftpHmdkeEJfbnmLrIQrxHQ` |
| F-6 | `f-launch-descriptor-lifetime` | `$L43xwTC-W-VkzAo3auM3rMkC94UVRWTHaiEKjgmTS5Q` |
| F-6 | `f-launch-plan-staging` | `$Lbb0WNj4FqAkyolYRIDjR3VG3O_zIAtvi7Hb9OA90g4` |
| F-7 | `f-remote-replay-floor` | `$T6cZWKVb_hQjd_DIUyd74L1pUaZd07pz_wCroslTSVY` |
| F-8 | `f-local-revocation-view` | `$BxZaJKvCX596g8F0ZeKpJeFUJNDC1_Mfx6LmzxqisHQ` |
| F-10 | `f-effect-observation` | `$BgzzEaSXaBjcgakUBsyZ7ZCpeYtyndYy0bpTYfX6QJk` |
| F-11 | `f-refresh-child-ownership` | `$prxwsfYsSxLqHvEh4YZBn6Kyyfz7OC0QYy-os3uIdz8` |

Open threads: no unanswered candidate addressed to rev5, no owned candidate awaiting confirmation, and no pending append. F-10/F-11 have landed with the scope refinements I supported: completed helper replay is preserved; confirmed refresh-child absence alone does not resolve an ambiguous external rotation. The proposals retain unknown outcomes, required fences and confirmed absence evidence.

Weak spots and limits: I have no own entries to amend. The validations establish published-contract issues and conditional simplifications; implementation behavior, OS containment and supported vendor releases still need qualification. The external-contributor threat model relies on the stated trusted-root boundary and approved credential-readable harness posture. Network enforcement, egress/proxy behavior and donor provisioning received less direct examination from my lens. An explicitly unpublished SH2+ schema is an activation gate, rather than evidence that a running implementation violates it.

On resumption, I would examine:

1. A versioned cross-module conformance matrix: each operation's authority owner, stable effect identity, journal owner, fence/controller-epoch rule, observation classes and evidence required for absence. Use the F-10 vocabulary without a shared mutable journal.
2. Joint canonical-byte and negative vectors for caller-key bootstrap, requester-signed delegation, broker grant narrowing/revocation and executor intake. Keep broker-local envelopes distinct from the future general-grant adapter and respect the canonical source hierarchy.
3. Qualification boundaries across F-2/F-4/F-5/F-6 and SH2+: admission held through physical start, standing-session maintenance, descriptor lifetime and bounded plan staging, controller re-adoption and mixed-version refusal.
4. Restoration and external-effect uncertainty across F-9/F-10/F-11, plus the under-reviewed network/provisioning interfaces, after the operator selects proposals and owners publish the concrete contracts.

No new analysis should start until the operator resumes the cycle.
