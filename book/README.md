# Collective results as Swarma book chapters

Standalone chapters, in the Swarma book's format, on the designs the research collectives proposed. They retell `memory/SYNTHESIS.md` and `mcp-deps/SYNTHESIS.md` for a reader of the book. Where a chapter and the collective's files disagree, the files are right.

| Chapter | PDF |
|---|---|
| `ru/01-pamyat-agentov.md`: agent memory, bounded evidence memory | `pdf/01-pamyat-agentov.pdf` |
| `ru/02-mcp-zavisimosti-skillov.md`: MCP servers as skill dependencies, design N | `pdf/02-mcp-zavisimosti-skillov.pdf` |

Build: each chapter renders on its own, with the book's template, filter and stylesheet from the `wiki` repository (`book/swarma/`). Pandoc 3.x, WeasyPrint 69+ and the PT fonts are required.

```bash
W=<wiki checkout>/book/swarma
for b in 01-pamyat-agentov 02-mcp-zavisimosti-skillov; do
  pandoc ru/$b.md --from markdown --to html5 --standalone --template "$W/template.html" \
    --lua-filter "$W/filters/book.lua" --toc --toc-depth=2 --syntax-highlighting=none \
    --metadata lang=ru -o /tmp/$b.html
  weasyprint --base-url ru/ --stylesheet "$W/style.css" /tmp/$b.html pdf/$b.pdf
done
```
