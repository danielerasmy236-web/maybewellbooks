# Product Inventory — Ready for Lemon Squeezy

_Every product that's a real, finished PDF file today, live on maybewellbooks.com
and sellable the moment Lemon Squeezy is activated. Prices already match what's
live on the site (`netlify/functions/lib/_catalog.js` is the source of truth —
this file is a snapshot of it, dated 2026-07-20). Paths are relative to
`MAYBEWELL BOOKS/` (repo root)._

**How to use this for Lemon Squeezy:** for each row, download the PDF at the
given path and upload it as that product's file when you create it in Lemon
Squeezy, using the same name and price. All 17 currently sell through the
single "pay what you want" checkout variant already wired in
`create-checkout.js` — you likely don't need 17 separate Lemon Squeezy
products/variants unless you want per-title analytics; ask if you want help
deciding which model fits.

## Imagine line — solo drawing prompts ($5 each)

| Product | Price | Pages | Size | File |
|---|---|---|---|---|
| Draw What You Imagine | $5.00 | 94 | 184K | `Draw What You Imagine/draw-what-you-imagine_v1.1_letter.pdf` |
| The Impossible Garden | $5.00 | 73 | 148K | `The Impossible Garden/the-impossible-garden_v1.0_letter.pdf` |
| Machines Nobody's Built Yet | $5.00 | 72 | 160K | `Machines Nobody's Built Yet/machines-nobodys-built-yet_v1.0_letter.pdf` |

## Field Notes line — observation & journaling books

| Product | Price | Pages | Size | File |
|---|---|---|---|---|
| The World Is Watching | $5.00 | 91 | 204K | `The World Is Watching/the-world-is-watching_v1.0_letter.pdf` |
| Wander Without a Destination | $5.00 | 81 | 192K | `Wander Without a Destination/wander-without-a-destination_v1.0_letter.pdf` |
| 15-Minute Micro-Adventures | $5.00 | 84 | 168K | `15-Minute Micro-Adventures/15-minute-micro-adventures_v1.0_letter.pdf` |
| Questions They Never Ask You | $4.00 | 58 | 128K | `Questions They Never Ask You/questions-they-never-ask-you_v1.0_letter.pdf` |
| The Grandparents' Book (large-print) | $4.00 | 52 | 116K | `The Grandparents' Book/the-grandparents-book_v1.0_letter.pdf` |
| The Map You Draw | $4.00 | 40 | 108K | `The Map You Draw/the-map-you-draw_v1.0_letter.pdf` |
| Letter to the Future | $3.00 | 22 | 92K | `Letter to the Future/letter-to-the-future_v1.0_letter.pdf` |

## Puzzles

| Product | Price | Pages | Size | File |
|---|---|---|---|---|
| Mazes of the Lost City | $4.00 | 61 | 176K | `Mazes of the Lost City/mazes-of-the-lost-city_v1.0_letter.pdf` |

## For Teachers & Educators line — classroom activities

Each activity ships as two separate files/products: a $2 Single Sheet and a
$4 Weekly Module.

| Product | Price | Pages | Size | File |
|---|---|---|---|---|
| Chain Story — Single Sheet | $2.00 | 3 | 64K | `For Teachers and Educators/chain-story-single-sheet_v1.0_letter.pdf` |
| Chain Story — Weekly Module | $4.00 | 7 | 72K | `For Teachers and Educators/chain-story-weekly-module_v1.0_letter.pdf` |
| Group Detective — Single Sheet | $2.00 | 3 | 64K | `For Teachers and Educators/group-detective-single-sheet_v1.0_letter.pdf` |
| Group Detective — Weekly Module | $4.00 | 7 | 72K | `For Teachers and Educators/group-detective-weekly-module_v1.0_letter.pdf` |
| Build Without Words — Single Sheet | $2.00 | 3 | 64K | `For Teachers and Educators/build-without-words-single-sheet_v1.0_letter.pdf` |
| Build Without Words — Weekly Module | $4.00 | 7 | 72K | `For Teachers and Educators/build-without-words-weekly-module_v1.0_letter.pdf` |

**Total: 17 real, finished products — all live and purchasable on
maybewellbooks.com today** (pending only Lemon Squeezy activation to
actually process payment; see PROJECT_STATUS.md).

---

## Not ready yet — do not list in Lemon Squeezy

These exist only as **generator code**, with no PDF actually produced —
`New Products - Pending Review/` is currently empty and
`agent-tools/catalog_manifest.json` marks all six `status: "pending"`. They
appear as "Coming soon" (grayed out, not purchasable) in the site's catalog.
The weekly local PDF-factory agent (`agent-tools/`, macOS `launchd`, Mondays
9am) generates one of these at a time into `New Products - Pending Review/`
for review — nothing here is a file yet:

- Little Logic Lab (puzzles)
- Space STEM Pack (stem)
- Story Starters (writing)
- Word Search Safari (puzzles)
- The Autumn Book (seasonal)
- Paper Games for Road Trips (games) — note: per `PRODUCT_QUEUE.md`'s
  resolved decisions, this one may end up retired/merged into a Field
  Notes "Road Trip Games" product instead of shipping as-is; don't build
  it without checking that decision first.

Also not yet built (approved concepts sitting in `PRODUCT_QUEUE.md`, no PDF):
Looking Up (Field Notes), and five new Teachers-line ideas — The Rumor Mill,
The Object Court, The Prediction Vault, The One-Minute Museum, The
Two-Minute Expedition.
