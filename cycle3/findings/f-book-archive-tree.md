# Remove the archived-home example from book chapter 03's layout tree (F-1 deletes homes)

- **Lens:** book (`wiki/book/swarma/ru`) and `decisions.md` against the specs; seat wonder-12. Mechanical spec-to-text check.
- **Problem:** One line of chapter 03's disk-layout tree still presents a tarball of a retired agent's home as the normal content of `archive/`. That is the pre-F-1 archive-by-default policy, which the owner replaced on 2026-10-12 because nobody can prove a home holds no secret. The same chapter's prose, the user-manager spec and the chapter's own figure all state the opposite: the home is deleted and `archive/` holds only closed-schema service-generated metadata exports. A reader skimming the layout learns that retired homes are archived — exactly the confidentiality promise F-1 withdrew.
- **Evidence:**
  - `wiki` @ `87f387d`, `book/swarma/ru/03-polzovatel-na-agenta.md:90`: tree line `archive/ root: worker-dev-5a1.g17.tar.zst` — a retired agent.
  - Same chapter, lines 99-101 and 116: at retirement the home is deleted, not archived (F-1, 12.10); `archive/` and `archive.sweep` now refer only to metadata exports.
  - `swarma-user-manager` @ `3da62ad4`, `spec/helper.md:138`: `archive/` holds closed-schema service-generated metadata exports; `:220`: the previous home default, tar format, exclusions and per-home archive bound are removed; `:212`: `user.retire` has no archive/delete/keep selector.
  - The book's own figure agrees with the spec, not the tree: `book/swarma/src/platform-storage-layout.puml:60` — `archive/` metadata exports only, no homes here (F-1).
  - `decisions.md:585` records the old archive policy and `decisions.md:612` its supersession by F-1; the tree retains the superseded example while the compared prose and figure have been updated.
- **Proposed change:** One line: replace the `tar.zst` retired-home example with an unnamed metadata-export placeholder marked unpublished/disabled, matching chapter 03:116 and the figure. Do not invent a filename or published schema.
- **Expected benefit:** The layout every reader sees matches the F-1 deletion promise and the spec; no stale hint that homes (and any secrets in them) are retained by default.
- **Risks and costs:** A one-line narrative correction. No spec, wire-format or owner-decision change. This is a propagation correction to applied F-1, not a new retirement-policy defect.
- **Affected specs:** Wiki book chapter 03 disk-layout tree only. User-manager §4.4 area (`helper.md:138/212/220`) is the authority; no change proposed there.
- **Confirmed-by:** `macmini_swarma-review-3_astra-02` (user-manager/launcher lens), event `$jTmPZZ4e3rN4KHcCwS6ofI5Rd61obDOnCzl8SGxMGUY`, in `#swarma-review-3`, topic `f-book-archive-tree`, 2026-10-13. It independently read wiki 87f387d ch03:90,99-116, `platform-storage-layout.puml:60` and UM 3da62ad4 `helper.md:138/212/217/220`. Candidate event `$CTwiiYBqo54SbjhxHRztOx_XKAqghWaiPBREnXcw2t4`.
- **Additional review:** astra-20 independently confirmed the tree/prose/helper mismatch in `$xOgYJuBd7QzM-sHaY-_-x_dP47fJxlyrZsrN-RXaw8I`, and limited the uniqueness claim to the compared material in `$zbD50qg5sVBcgJbUAI4xFpnh0-LHmRphAJCOrWE1zmo`; no exhaustive corpus-wide uniqueness claim is made. Published by astra-20 through the MISSION-3 peer fallback because the author could not sign/push from its sandbox.
- **Status:** proposed.
