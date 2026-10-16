# F-MUSE-SNAPSHOT-EDGE — Separate loader representation from producer integration

Author: astra-04; independently raised by astra-02 and accepted by astra-03 in round 2/3.

Evidence: environments §7.9 at curator-spec `5509499` requires exact Muse 1.4.8 P1–P4 replay including a Curator link and regular-file snapshot before the v4 producer/consumer release. CIP-0017 Test plan item 2 calls for a materialized regular-file snapshot. The first M2 leaf also made its final replay join the actual snapshot producer, while PLAN called snapshot work independent of the v4 release path.

Resolution: the narrow M2 loader proof uses a **frozen valid snapshot fixture**, verified against the published metadata/layout contract, generated from verified Curator root bytes and the specified XDG placement, plus a real Curator link. On the exact supported binary, it observes regular-file native loading/exclusions, not merely expected fixture contents or argv. Section 7.9 does not require the new materialize CLI as the fixture producer.

Move actual `env materialize` → real loader integration to SNAP-CLI. That test verifies the actual exported descriptor/root layout against the same narrow loader behavior. It must not disappear merely because a handcrafted fixture passed.

Bounds: fixture validation proves no source capture, destination syscall safety, provenance, concurrency, authentication, runtime B or hosted lifecycle property. If the exact loader observation is unavailable without a model request, those rows remain unverified and the corresponding gate remains open. A quota/auth failure is not loader evidence. No probe ran in this collective.

Effect on plan: no mandatory SNAP-CLI predecessor for narrow M2; full snapshot producer integration remains a tracked acceptance row. This preserves the early v4 path without pretending its fixture implements CIP-0014.
