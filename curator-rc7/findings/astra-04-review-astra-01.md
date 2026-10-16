# astra-04 adversarial review of the delivery plan

Reviewed PLAN at `3b13aac`, X5 at `6186899`, and C5/C7/M6 at `75dc718` on 2026-10-16. This is a review of proposed work, ownership and evidence gates. It is not implementation acceptance or provider qualification.

## Confirmed findings and dispositions

| Challenge | Evidence and required change | Disposition in the integrated plan |
| --- | --- | --- |
| Export does not migrate live sessions | D4 and snapshots §6 apply to native and headless routes as well as hosted routes | D4-N and D4-S now separately own actual entrypoints, original resume identity and failure effects |
| A pure snapshot is not an initialized runtime home | Snapshots §§1–4 exclude seeds, credentials and source/backend policy; hosted §§3–4 require a usable private home | HOST-HOME-SPEC/CODE own Curator initialization and protected-input verification; route owners retain real provider lifecycle qualification |
| Existing helpers do not satisfy capture/publication | Current capture entry recovers journals; current no-follow helper permits root ancestry links | SNAP-LOCK and SNAP-PUBLISH retain independent stronger contracts, no recovery/provisioning and retained-handle no-follow/no-replace controls |
| Content verification currently executes a vendor | `verifyHome -> checkToolRelease -> detected -> detectRelease` reaches `exec.CommandContext` | L15-2 owns the common pure verification/observation split with SNAP-LOCK; status and both materialize forms retain separate production CLI tripwires |
| Early Muse qualification need not wait for the new exporter | environments §7.9 requires the real loader on both representations, not one specific fixture producer | M2 uses verified frozen regular-file bytes and the real loader; SNAP-CLI still owns actual `materialize -> loader` integration |
| Hosted work was grouped too broadly | Reservation, authority admission, provider lifecycle, process forms and public activation have different boundaries | Nine H leaves now identify these owners, tests and joins; the first advertised release still requires all three providers and operations |
| Same-user proof cannot qualify cross-account execution | X3 archive verification and D4-N do not test a different executing account or writable-ancestor protection | X5 owns actual protected projection and start/login/model/native-resume per provider/platform/account; X4 remote activation requires it |
| Codex private base ownership could drift into the receiver | New hosted §4 permits tools/trust narrowing and preserves the planned process/MCP; legacy host code writes config and auth links | Revised C5 and PLAN keep initial base bytes in Curator, preserve profile MCP/single selector and refuse an unowned gateway intersection |
| Daemon secret lookup conflicts with the current hosted restart contract | Hosted §§4/6 preserve the exact provider process and caller-side fresh-secret resolution | T3a/T3b/T4 now define the separate same-user headless final-exec route; tb-sessiond lookup/restart remains unavailable without a separate amendment |

The underlying source evidence is pinned in [the evidence ledger](astra-04-evidence.md), [helper boundaries](snapshot-helper-boundaries.md), [runtime seam](hosted-home-seam.md), [Muse dependency split](muse-snapshot-replay-dependency.md), and [vendor-probe finding](materialize-version-probe.md).

## Remaining synthesis check

At `3b13aac`, the published C7 activation owner and M6 broker-key backend seam still need canonical PLAN links and coverage/dependency rows. Their detailed contracts at `75dc718` are accepted; this is a traceability completion, not another runtime design finding. Final scoring must use the integrated revision rather than the earlier placeholder plan.

## Review limits and retained implementation gates

- Runtime B still requires the expressly retained operator confirmation of a concrete protection mechanism. A chmod-only tree under writable ancestry is not sufficient.
- Fresh and resumed runtime verification must retain the original protected-input baseline while permitting declared native state writes. Neither a whole-home hash nor a freshly rewritten baseline meets both requirements.
- Schema/fixture acceptance does not prove locking, filesystem races, vendor loading, child-secret containment or authentication. The proposed tests must exercise production entrypoints and demonstrate their intended negative detector with bounded controls.
- The additive Curator tag does not complete D4 migration, token-backed spawned authentication, hosted activation or archive delivery. Every advertised destination/platform/route requires its own evidence.
- Shared `managed.go`, carrier identities, module pins and executor entrypoints must follow the explicit serialization table; new disjoint snapshot helper files may proceed in parallel against frozen interfaces.

No new source edits, builds, credentials, vendor execution or web research were used for this review. A read-only Markdown target audit at `3b13aac` checked 56 plan/leaf/verdict files and 86 targets with zero missing local targets; the existing-target control passed and a known missing target was detected. This checks file existence only, not anchors, external URLs or normative completeness.
