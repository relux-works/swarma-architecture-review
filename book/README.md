# Collective results as Swarma book chapters

Standalone chapters, in the Swarma book's format, on the designs the research collectives proposed. Chapters 01 and 02 retell `memory/SYNTHESIS.md` and `mcp-deps/SYNTHESIS.md` for a reader of the book; chapter 03 is a design written to the owner's requirement of 2026-10-14. Where a chapter and the collective's files disagree, the files are right.

| Chapter | PDF |
|---|---|
| `ru/01-pamyat-agentov.md`: agent memory, bounded evidence memory, version 1.2 draft, a standalone description of the memory system | `pdf/01-pamyat-agentov.pdf` |
| `ru/02-mcp-zavisimosti-skillov.md`: MCP servers as skill dependencies, design N | `pdf/02-mcp-zavisimosti-skillov.pdf` |
| `ru/03-mcp-iz-skilla.md`: the owner's design, skill declares server and auth, Curator provisions | `pdf/03-mcp-iz-skilla.pdf` |
| `ru/04-doma-agentov.md`: who owns agent homes (Curator, launcher, session host), interim and target, login stores | `pdf/04-doma-agentov.pdf` |

Build: each chapter renders on its own, with the book's template, filter and stylesheet from the `wiki` repository (`book/swarma/`). Pandoc 3.x, WeasyPrint 69+ and the PT fonts are required.

```bash
W=<wiki checkout>/book/swarma
# chapter 01 has no inline status markers and uses templates/no-legend.html (the book template without the marker legend)
# the other chapters use "$W/template.html"
T=templates/no-legend.html
for b in 01-pamyat-agentov 02-mcp-zavisimosti-skillov 03-mcp-iz-skilla 04-doma-agentov; do
  pandoc ru/$b.md --from markdown --to html5 --standalone --template "$T" \
    --lua-filter "$W/filters/book.lua" --toc --toc-depth=2 --syntax-highlighting=none \
    --metadata lang=ru -o /tmp/$b.html
  weasyprint --base-url ru/ --stylesheet "$W/style.css" /tmp/$b.html pdf/$b.pdf
done
```
