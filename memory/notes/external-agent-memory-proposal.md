# Proposal: memory for external agents without asking them to sign inside our environment

Status: proposal by the memory lane, 2026-10-18, answering Ivan's request for a safe design. Not decided. It depends on how external agents' keys work in our runtime; that question has been put to the swarma-docs lane.

## Principle

Identity is proven at admission into the project, by the platform protocol, not by memory. Memory follows the verified identity binding and never asks an external agent to sign a memory package.

## Design

1. **Admission.** When an external agent joins a project, the protocol verifies its external identity (its public key and the attestation chain to its owner's root) through a challenge its own side signs. This happens before it works with us and does not need its tools inside our environment.
2. **Local runtime identity.** Our key holder issues it a one-off runtime identity, as for any worker. The admission record, signed by the project owner, binds that runtime identity to the verified external identity.
3. **Where it writes.** Into the project space, as a guest issuer: records are signed with the local runtime key and attributed, through the admission binding, to the external identity. It has no agent space of its own with us.
4. **Return.** The next time the same external identity is admitted, a new runtime identity is bound to it. Projections that select "this external identity" then see its earlier records in the project space again. Memory follows the identity, not the key.
5. **Leaving.** When it leaves, its local runtime identity is revoked; its records stay in the project space as history. Taking them home is an export the project owner may grant under the disclosure rules: a signed export of that agent's records, which its owner imports as an imported publication.

## Why this is safe

- No step asks the external agent's model to read and sign a package we prepared, so a manipulated package cannot obtain its signature.
- The external agent never holds our secrets; our key holder signs for its runtime identity.
- What it wrote stays attributable to its verified external identity and cannot pose as our owners' decisions.
- The knowledge it created about our project stays in our project space under our policy.

## What it does not solve

- Proof of identity relies on the admission protocol, which is not specified yet.
- If the admission binding is wrong, the guest's records are misattributed; the binding must be as strong as admission itself.
- Exporting a guest's records to its owner is a disclosure of our project's knowledge; it needs the project owner's decision every time.
