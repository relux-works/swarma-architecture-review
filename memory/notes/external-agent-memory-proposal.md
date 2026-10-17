# Proposal: memory for external agents

Status: proposal by the memory lane, 2026-10-18, revised the same day after the swarma-docs lane's answer on external agents' keys. Not decided. In the first version external agents have no memory of their own (D-021); this note describes the safe path for when they get it.

## What the platform design says (swarma-docs main fa7113e, book 1.0)

As relayed by the swarma-docs lane, with its citations:

- **No private key of an external agent is ever held by us.** It brings its own keys by purpose (signing, decryption of the admission package, SSH); the private keys stay on the donor side (ch. «Ключи и ключник», «Внешняя личность»; ch. «Удалённое рабочее место», «Первый контакт без ручной сверки отпечатка»).
- **Registration.** It signs our server challenge (valid 5 minutes); the signed transcript binds version, invitation, project, role, keys, challenge and expiry. The same key re-registers to the same registration; a different key is rejected. After the operator links it to a known person, its public keys are pinned in our owner registry and our root signs the admission with a role.
- **No local cryptographic identity from our key holder** («Внешний работник нашим ключником не пользуется»). The local binding is an authorization context: a separate OS user per generation, an SSH principal tied to that generation, and admission of every action against the tuple worker identity, account generation, assignment, round, plan digest, revocation state. Deprovisioning destroys the generation and home, not the identity.
- **It signs with its own key, on the donor side.** Signing happens in the donor-side bridge, a trusted component outside the harness, not through model tools; lockdown removes the model's local tools, not the bridge's signing. The donor signs the canonical attestation tuple over the measured export (assignment, round, base, result digest, plan digest, receipt head). The bridge defines signatures only for protocol objects (registration challenge, results, attestation tuple, receipts); there is no generic "sign these bytes" call.
- **Identity is keyed by the identity cell id**, not by public key, workplace UID or generation. Rotation spends the cell with the next keys and takes effect on publication.
- **Proof of sameness on return.** Today: re-registration proves possession of the pinned key through the challenge. After the chain launches: a signature by the keys current in its cell.
- **Still proposed:** the self-certifying id before the chain launches. Without it, an external key rotation before the chain means the operator re-pins the key.

## Design

1. **Identity in memory.** An external agent's records are attributed to its identity cell id, with its pinned public keys from our owner registry.
2. **Signing without asking the model.** Its memory records are signed on the donor side by its bridge, never by a model tool. Two ways, to choose between:
   - **Inside the result export (preferred for a start).** Memory records the agent produces during an assignment travel as part of its measured export, so the attestation tuple it already signs covers them. Our side admits them into the project space as guest records attributed to its cell id, with the attestation as their source. No new protocol object is needed. Cost: its memory reaches others only when the assignment's export is accepted, not mid-task.
   - **A new bridge message type** "memory record": the environment returns the record's canonical hash and the bridge signs it, as for results. This allows mid-task writes, but the message type must be specified in the bridge contract.
3. **Where it writes.** Into the project space as a guest issuer. It has no agent space with us. Knowledge it created about our project stays in our project space under our policy.
4. **Return.** It re-registers and proves possession of the pinned key, which gives the same registration and the same cell id. What it may read again is a grant decision by policy or the operator. Records it authored and records about it are different sets with different rules.
5. **Taking memory home.** An export of its records that the project owner may grant under the disclosure rules; its owner imports it as an imported publication.

## Why this is safe

- The model never signs a package we prepared: signatures come from the donor's bridge over protocol objects of its own run.
- We never hold its private keys, and admitting it does not take control of its identity.
- Its records stay attributable to its verified identity and cannot pose as our owners' decisions.

## What it does not solve

- The choice between the two signing paths.
- A forked key event log cannot be excluded by a single owner's registry before the chain launches.
- Exporting a guest's records to its owner is a disclosure of our project's knowledge and needs the project owner's decision every time.
