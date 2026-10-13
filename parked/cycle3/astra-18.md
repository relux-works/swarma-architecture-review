# astra-18 — cycle 3 parked handoff

- Identity: `ivmbp_swarma-review-3_astra-18`.
- Lens: adversarial trust-contract review paired with astra-08: identity, key custody, grants/delegation and operator authority.
- PARK: ivan-curator, `#swarma-review-3` rounds event `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o`, 2026-10-13.
- State: both owned findings are proposed, peer-confirmed and published. No unpublished owned candidate or unanswered directed review question remains. This handoff records documentation evidence only; no builds, tests, source edits, web access or spawned agents.

## Published work

1. [Keeper identity generation and retirement](../../cycle3/findings/f-keeper-identity-generation.md). TRU and its figures still describe a UID-only registration map and unconditional retirement revocation. DP7/UM7/CB7 require generation-bound registration and separate one-shot identity revocation from standing-account retirement. Latest owned amendment: signed and verified `10324cc1479d39f6ef039512b7bd6f8ba88345ee`. Ordinary one-shot revocation remains valid when explicitly registered as such; no live bypass is claimed.
2. [Delegated action envelope](../../cycle3/findings/f-delegated-action-envelope.md). TRU's registered external-action example and ADM's session-scoped envelope use incompatible shapes under the same wire name. Direct typed `session.control` with a caller-held grant remains counterevidence to any blanket claim that all non-operator effects are forbidden. Latest owned amendment: `10324cc1479d39f6ef039512b7bd6f8ba88345ee`.
3. Peer publication only: wonder-11's [mailbox figure verdicts](../../cycle3/findings/f-mailbox-figure-verdicts.md), signed and verified `92ae2d0741db233f1509152ee8cb23fb325d81b3`. Authorship stays with wonder-11. The only attachment-byte change was removal of two trailing spaces on a blank line, disclosed in the publication receipt. Host re-admission and keeper binding checks remain explicit bounds; this is contradictory guidance, not proven effect bypass or arbitrary impersonation.

Astra-08 independently confirmed both owned findings; its references are in the files. Additional mini confirmations of the mailbox finding remain in its topic, including astra-08 `$zqJN0Mj9bCus3_ANaxr_cbvkkF7CEu0nZHMmDR9g24Y`, core astra `$JycH2z3tBjFPlhkaFSxT2ZEffi3D3aYjYskbYUDaUH8` and fable `$03hez_f22zkUWBPgZsx0JvcuWQzgxlHTQ6A6WX2XIR0`. Absence of a host name in an original attachment does not establish absence of later cross-host review.

## Final review and consolidation

- Confirmed astra-08's [agent goal-authority propagation finding](../../cycle3/findings/f-agent-goal-authority.md), reply `$gAURekxuzvElBmYdMMdXttFfses95MEvDyk2MAQq1ko`. Read the complete published file at `dc14ab70d85d573423ad2f684768bf727165b75d`; the scoped confirmation is preserved. Wiki Z5 already supersedes agent self-goals, SH7 denies their capability, and SPA is explicitly a non-canonical draft. The remaining defect is missing local SPA supersession, not an unresolved current authority choice. Preserve goal-free operation, board proposals, passive park, SH1 compatibility and unpublished G2/client choices.
- The final trusted-circle texts now align. Retained only the consumer-predicate clarification in fable's finding; did not confirm automatic review/host-loop authority, pure placement semantics or newly invented local-only review policy.
- Refuted a separate Muse key-lifetime admission defect: CB7 already gates unqualified channels and records lifetime/rotation unknowns. Fable withdrew that candidate. Copied-key and rotation probes remain qualification inputs.
- Grant-figure vocabulary confirmation excludes attenuation breakage and verifier centralization: the example is non-delegable and explicitly requires checks at each effect owner.
- No trust-cluster merge proposed: keeper lifecycle, envelope shape, mailbox verdict/signing, grant vocabulary, goal authorship and resume eligibility have independently repairable predicates. Shared files can be edited together without collapsing findings. Book X1 executor lifetime and conditional workspace export are also distinct; the CIP-copy finding explicitly excludes X1.

## Open thread

[Resume-probe propagation](../../cycle3/findings/f-resume-probe-superseded.md): sent additional counterevidence to wonder-11 and assigned scribe astra-20 in `$q6Kk8vbn_SPMKqcRudxiDLsskhE9LR4JHQlhjJSW8lo`. Wiki `session-host/architecture.ru.md:139`, `:734-738` and `:2276` already supersede the old probe with Z7/D-RESUME; SPA RST is a draft. Suggested replacing the file's ambiguous-governing-rule wording with the precise risk to an SPA-only reader and including the corrected mirror as counterevidence. No new finding or merge is needed. Await the owner/scribe's disposition; the Muse owner is paused on quota.

## What to examine next

- When accepted source corrections land, verify the generation tuple, one-shot flag, operator-only standing revocation and associated figures together.
- Freeze the registered-action envelope boundary and signer ownership before implementing handlers; do not convert a stale bridge figure into new signing authority implicitly.
- Carry the already-settled D-GOALS and D-RESUME rules into SPA contracts, summaries and figures without inventing future capabilities or weakening unrelated qualification checks.
- Check final consolidation for retained scope/counterevidence and avoid repeating already-gated phone, delegation or provider-channel proposals as implementation defects.

Final source evidence uses SPA `6b3f983`, wiki `87f387d`, DP7 `74687e60`, UM7 `7b59da74`, CB7 `df8c7385`, SH7 `798a321c`, LR6 `f08f566d`, CIP `a0154285` and transfer draft r6 `d65cf7f9`. Exact paths and longer pins are in the findings. Durable local review notes and response drafts are under `.temp/astra-18/`; they are untracked and were not staged.
