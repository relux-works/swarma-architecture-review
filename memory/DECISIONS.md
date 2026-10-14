# Memory design: decision log

Owner decisions on the agent-memory design, as Ivan states them in the lane orchestrator's session. Each entry quotes the decision, names its scope and the follow-up. Proposals that are not yet decided stay in `SYNTHESIS.md` §6 and `notes/`.

## D-001. Memory snapshot travels as a data block, not as an overlay (2026-10-14)

- **Question put:** platform book ch. 09 «Память» places the session-start memory snapshot in the operator overlay with a weight below every role module, and calls that "not instructions". Curator weights only order chapters; they do not turn instruction text into data (`findings/memory-data-channel.md`). Should the snapshot reach the session as a separate data block instead, and should ch. 09 be corrected to say so?
- **Decision (Ivan, in session):** «да».
- **Meaning:** the snapshot idea survives (fixed for the session, keeps the prompt cache warm), but its channel is a data-only block with per-item provenance and the `data` classification, never a Curator overlay, `AGENTS.md`, skill root or machine base context. Memory content gets no overlay weight at all.
- **Follow-up:** a change to `wiki/book/ru/09-pamyat.md` (the overlay paragraph and the "это не инструкции" line of the ladder section), through the wiki's normal PR flow; the exact delivery contract of the data block belongs to the R7 package.
