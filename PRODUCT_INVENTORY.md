# Product Inventory — Ready for Lemon Squeezy

_Every product that's a real, finished PDF file today, live on maybewellbooks.com
and sellable the moment Lemon Squeezy is activated. Prices already match what's
live on the site (`netlify/functions/lib/_catalog.js` is the source of truth —
this file is a snapshot of it, dated 2026-07-20). Paths are relative to
`MAYBEWELL BOOKS/` (repo root)._

**How to use this for Lemon Squeezy:** for each row, download the PDF at the
given path and upload it as that product's file when you create it in Lemon
Squeezy, using the same name and price. All 22 currently sell through the
single "pay what you want" checkout variant already wired in
`create-checkout.js` — you likely don't need 22 separate Lemon Squeezy
products/variants unless you want per-title analytics; ask if you want help
deciding which model fits.

## Imagine line — solo drawing prompts ($5 each)

| Product | Price | Pages | File |
|---|---|---|---|
| Draw What You Imagine | $5.00 | 94 | `Draw What You Imagine/draw-what-you-imagine_v1.1_letter.pdf` |
| The Impossible Garden | $5.00 | 73 | `The Impossible Garden/the-impossible-garden_v1.0_letter.pdf` |
| Machines Nobody's Built Yet | $5.00 | 72 | `Machines Nobody's Built Yet/machines-nobodys-built-yet_v1.0_letter.pdf` |

## Field Notes line — observation & journaling books

| Product | Price | Pages | File |
|---|---|---|---|
| The World Is Watching | $5.00 | 91 | `The World Is Watching/the-world-is-watching_v1.0_letter.pdf` |
| Wander Without a Destination | $5.00 | 81 | `Wander Without a Destination/wander-without-a-destination_v1.0_letter.pdf` |
| 15-Minute Micro-Adventures | $5.00 | 84 | `15-Minute Micro-Adventures/15-minute-micro-adventures_v1.0_letter.pdf` |
| Questions They Never Ask You | $4.00 | 58 | `Questions They Never Ask You/questions-they-never-ask-you_v1.0_letter.pdf` |
| The Grandparents' Book (large-print) | $4.00 | 52 | `The Grandparents' Book/the-grandparents-book_v1.0_letter.pdf` |
| The Map You Draw | $4.00 | 40 | `The Map You Draw/the-map-you-draw_v1.0_letter.pdf` |
| Letter to the Future | $3.00 | 22 | `Letter to the Future/letter-to-the-future_v1.0_letter.pdf` |
| Road Trip Games | $4.00 | 22 | `Road Trip Games/road-trip-games_v1.0_letter.pdf` |

## Puzzles, STEM, Writing & Seasonal — PDF-factory catalog

Published 2026-07-20. Note: the client catalog's placeholder page counts
(written before these were generated) were wrong for all five — the numbers
below are the real, verified counts, corrected at publish time.

| Product | Price | Pages | File |
|---|---|---|---|
| Mazes of the Lost City | $4.00 | 61 | `Mazes of the Lost City/mazes-of-the-lost-city_v1.0_letter.pdf` |
| Little Logic Lab | $4.00 | 48 | `Little Logic Lab/little-logic-lab_v1.0_letter.pdf` |
| Space STEM Pack | $4.00 | 16 | `Space STEM Pack/space-stem-pack_v1.0_letter.pdf` |
| Story Starters | $4.00 | 72 | `Story Starters/story-starters_v1.0_letter.pdf` |
| Word Search Safari | $3.00 | 47 | `Word Search Safari/word-search-safari_v1.0_letter.pdf` |

Space STEM Pack is genuinely short (16pp for 12 one-page projects) — the
content itself is real and complete (sundial, 3 constellation charts, moon
wheel, 2 math sheets, star finder, scale model, spacecraft design, gravity
experiment, name-your-own-constellation), just leaner than the rest of the
catalog. Worth a look if you want it padded out later; not blocking as-is.

## For Teachers & Educators line — classroom activities

Each activity ships as two separate files/products: a $2 Single Sheet and a
$4 Weekly Module.

| Product | Price | Pages | File |
|---|---|---|---|
| Chain Story — Single Sheet | $2.00 | 3 | `For Teachers and Educators/chain-story-single-sheet_v1.0_letter.pdf` |
| Chain Story — Weekly Module | $4.00 | 7 | `For Teachers and Educators/chain-story-weekly-module_v1.0_letter.pdf` |
| Group Detective — Single Sheet | $2.00 | 3 | `For Teachers and Educators/group-detective-single-sheet_v1.0_letter.pdf` |
| Group Detective — Weekly Module | $4.00 | 7 | `For Teachers and Educators/group-detective-weekly-module_v1.0_letter.pdf` |
| Build Without Words — Single Sheet | $2.00 | 3 | `For Teachers and Educators/build-without-words-single-sheet_v1.0_letter.pdf` |
| Build Without Words — Weekly Module | $4.00 | 7 | `For Teachers and Educators/build-without-words-weekly-module_v1.0_letter.pdf` |

**Total: 22 real, finished products — all live and purchasable on
maybewellbooks.com today** (pending only Lemon Squeezy activation to
actually process payment; see PROJECT_STATUS.md).

---

## Not built — do not list in Lemon Squeezy

**Paper Games for Road Trips** (old id `roadtrip`) — retired per
`PRODUCT_QUEUE.md`'s resolved decision, merged into the new Field Notes
**Road Trip Games** product (id `tripgames`, Template H — game rules +
scorecard), published 2026-07-20. The old id/placeholder no longer appears
anywhere on the site; do not reuse it.

Also not yet built (approved concepts in `PRODUCT_QUEUE.md`, no PDF yet):
Looking Up (Field Notes), and five new Teachers-line ideas — The Rumor Mill,
The Object Court, The Prediction Vault, The One-Minute Museum, The
Two-Minute Expedition.

## Bug fixed across the whole PDF-factory catalog (2026-07-20)

Every `agent-tools/generators/generate_*.py` file (mazes, logic, stem,
story, words, autumn, and roadtrip for consistency) was calling
`brand.draw_cover(c, title, subtitle, "maybewellbooks.com", accent)` —
passing the site URL as the **tagline** argument. `draw_cover()` already
draws the real `SITE_URL` unconditionally on its own line, so every cover
showed "maybewellbooks.com" twice (visually overlapping/redundant) and
never showed an actual tagline. Fixed by adding a real `TAGLINE` to each
product's `content/*.py` and passing `ct.TAGLINE` instead. **Mazes of the
Lost City was already live with this bug** — it's been regenerated and
republished with the fix; no catalog/price change, just the corrected file.
