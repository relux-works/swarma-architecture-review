# F-HOSTED-HOME — Export identity is not runtime preparation or authorization

Author: astra-04. Confirmed independently by astra-01 in round 1.

Evidence: curator-spec `5509499`, snapshots §§1/3/4/6/7 and local-hosted-launches §§1/3/4/5/8.

1. Pure snapshot output excludes credential files/links, provisioning seeds, native config, mutable state, backend policy and profile Codex settings. `manifest-only` observes the selected source; it does not attest any session directory.
2. Hosted admission needs a Curator verification API/receipt. Fresh launch validates initial materialization; restart validates original provenance and Curator-defined protected inputs while allowing runtime-owned state changes. The complete initial private home and any credential strategy are Curator responsibilities.
3. These requirements compose only through an explicit additional runtime-preparation/verification contract. Copying native config or reconnecting auth in the receiver violates ownership; sneaking either into snapshot v1 violates the export schema/closure. Whole-home initial hashes on resume reject legitimate runtime writes, while refreshing the baseline blesses drift.
4. Claude native login is config-dir-bound in the supplied facts. A source-home `login: present` is not evidence that a newly relocated home can authenticate. A separately admitted setup-token path can address that runtime row, but never by storing the token in the snapshot or assuming login metadata authorizes secret delivery.
5. Runtime B needs operator confirmation and actual backend qualification. Archive bytes/caps and cross-account transport remain unpublished. A local plan digest is neither source authority nor a hostile-same-user isolation boundary.

Proposed repair: HOST-HOME-SPEC followed by HOST-HOME-CODE, alongside the jointly versioned launcher/receiver hosted plan. Pure SNAP-* delivery can ship independently with precise non-activation notes. If hosted capability is part of a release's acceptance, all three runtime rows and every publication/credential/policy gate are blockers.

Related completeness check: D4 applies to live agent sessions generally. Local-hosted-launches §1 explicitly leaves headless task-board spawn adoption separate. Keep native curator-run and spawn migrations in the implementation graph, even when outside the immediate additive Curator release; do not mark D4 fully delivered by exporting a snapshot once.
