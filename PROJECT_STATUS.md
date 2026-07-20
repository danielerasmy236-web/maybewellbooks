# Maybewell Books — Project Status / Handover Brief

_Last updated: 2026-07-20. Written to be read cold, at the start of a brand
new Claude Code conversation with zero prior context. If you're that
conversation: read this whole file before touching anything._

## What this is

An e-commerce site selling printable PDF activity books, at
**maybewellbooks.com** (hosted on Netlify, GitHub repo
`danielerasmy236-web/maybewellbooks`). Target market: US + Southeast Asia.
Prices $2–5 USD. Owner/operator: Dan.

The site is a **pre-built, minified React SPA with no build tooling** —
`website-repos/maybewell-site-dist-v2/assets/index-*.js` is the only
source file for the frontend (no package.json, no bundler; the hash in the
filename changes on every edit — always check `index.html` for the current
one, never hardcode a hash from memory). All frontend changes are surgical
string-replacements on that minified file, verified with `node --check`
before anything touches git. **This is the single most important thing to
know before touching the site**, and it has burned people before — see
"Hard-won lessons" below.

## What's live right now

**22 real, purchasable products**, in four lines:

- **Imagine** (solo drawing prompts, $5 each): Draw What You Imagine (94pp),
  The Impossible Garden (73pp), Machines Nobody's Built Yet (72pp).
- **Field Notes** (observation/journaling, $3–5): The World Is Watching
  (91pp, pareidolia), Wander Without a Destination (81pp, dérive walks),
  15-Minute Micro-Adventures (84pp), Questions They Never Ask You (58pp,
  two-answer conversation manual), The Grandparents' Book (52pp,
  large-print interview book), The Map You Draw (40pp, continuous personal
  atlas), Letter to the Future (22pp, correspondence/sealed-envelope book).
- **Puzzles / STEM / Writing / Seasonal** (the original "PDF-factory"
  catalog, $3–4): Mazes of the Lost City (61pp), Little Logic Lab (48pp),
  Space STEM Pack (16pp — genuinely short but complete, 12 real projects),
  Story Starters (72pp), Word Search Safari (47pp), The Autumn Book (36pp).
- **For Teachers & Educators** (classroom activities, $2 single-sheet / $4
  weekly-module, 6 files): Chain Story, Group Detective, Build Without
  Words — each in both formats.

Full file-by-file list with prices/paths: **`PRODUCT_INVENTORY.md`** at
repo root (kept in sync with the server catalog, meant for eventually
creating these as Lemon Squeezy products).

Also live: real cart/checkout UI, a "Teachers" nav section, **three company
manifestos** ("On Offline Content," "On Printing It," "On Paper and Trees"
— footer link → index → detail pages, pull-quotes on the home hero and
product buy CTAs), Privacy/Terms/Cookies (EN+ES, not lawyer-reviewed), a
clickable/expandable lightbox on every product's preview images, and a
hand-drawn nav-underline hover animation (GSAP).

**Not yet available on the site**: Paper Games for Road Trips — a generator
exists but was deliberately NOT built. It's retired/merged into a future
Field Notes "Road Trip Games" product per a resolved decision in
`PRODUCT_QUEUE.md`. Don't build it under the old `roadtrip` id without
re-checking that decision first.

## What's blocking a real sale right now

**Resend (delivery email) is fully done** — domain verified, a scoped
sending-only API key is set as a Netlify secret (`RESEND_API_KEY`,
production context), `ORDERS_FROM_EMAIL` is set, and a real test send was
confirmed `delivered` via the Resend API. Not Resend's problem anymore.

**Lemon Squeezy (payment processor) is the one real remaining blocker.**
Last known state: store activation submitted, pending their ~2-3 business
day review — check for an approval email. Once approved:

1. "Copy to Live Mode" on the product → generates a **new Store ID and
   Variant ID** (test-mode ones currently in place will need replacing).
2. Set these secrets directly in **Netlify → Site configuration →
   Environment variables** (never in chat, never via a tool that would
   echo the value back into conversation):
   - `LEMONSQUEEZY_API_KEY`
   - `LEMONSQUEEZY_WEBHOOK_SECRET` (from a webhook pointed at
     `https://maybewellbooks.com/.netlify/functions/ls-webhook`, subscribed
     to `order_created`)
   - `DOWNLOAD_TOKEN_SECRET` (any long random string, e.g.
     `openssl rand -hex 32`)
3. `LEMONSQUEEZY_STORE_ID` / `LEMONSQUEEZY_VARIANT_ID` are NOT secret —
   safe to paste in chat for help setting them.
4. Full checklist: `website-repos/maybewell-site-dist-v2/netlify/functions/SETUP.md`.
5. **Before trusting it with real orders**: send a real Lemon Squeezy test
   webhook (dashboard → Webhooks → "Send test event") and check the
   Netlify function log for `ls-webhook` — the payload field names in that
   file are a best guess from docs, never yet confirmed against a live
   payload.
6. Then one real end-to-end test purchase (Lemon Squeezy has a test-card
   mode): pay → `/order-success.html` → email arrives → download link
   actually works.

Confirmed via Netlify API as of this writing: env vars are `ORDERS_FROM_EMAIL`
and `RESEND_API_KEY` only — no Lemon Squeezy secrets set yet.

## Deploying: GitHub is connected but auto-deploy is STILL BROKEN — verify, don't assume

The Netlify site (`maybewellbooks`, site id
`12dd4eba-e81c-4fa7-87d5-ad18b5d37496`) has GitHub linked (base directory
`website-repos/maybewell-site-dist-v2`) — but **push-to-deploy is not
reliable**, root-caused (2026-07-20 session) but not fully fixed. Two
separate bugs found, one fixed, one still open:

1. **FIXED**: `build_settings.dir` (Publish directory) was `null`, and
   since `base_rel_dir: true`, the correct value is `.` (meaning "same
   folder as Base directory") — NOT the full path repeated (that
   duplicates into `base/base`, which was tried and produced a hard
   "Deploy directory ... does not exist" failure, confirmed via the
   public deploy log at `https://app.netlify.com/projects/maybewellbooks/deploys/<id>`,
   click into the "Deploying" step to see the actual error — the
   top-level `error_message` from `getSiteDeploy` is often misleadingly
   generic, e.g. always says `"Failed during stage 'building site'"`
   even when the real failure is in the deploy step). This is now set
   correctly (`dir: "."`) and confirmed via `getSite`.
2. **STILL OPEN, unresolved**: even with `dir` correct, every real
   push-triggered build still gets `Canceled build due to no content
   change` — a genuine false positive, reproduced 3 times in a row on
   trivial real edits to `robots.txt`. Very likely tied to the **space in
   the base directory name** (`website-repos/...`) confusing Netlify's
   monorepo "did anything change under this path" diff heuristic — this
   matches publicly reported Netlify bugs with space/special-character
   base directories. **Do not try to "fix" this by setting
   `build_settings.build_filter`** (the "Ignore build command" UI
   field) to force always-build (e.g. `"false"`) — tried twice in this
   session, reproducibly: it does NOT stop the false-positive skip, and
   it appears to make GitHub-webhook-triggered builds stop being created
   entirely (no deploy record shows up at all, confirmed via
   `listSiteDeploys` after 5+ minutes of waiting both times, vs. under a
   minute normally). Reverting `build_filter` to `null` restored normal
   (if still false-positive-prone) webhook behavior immediately both
   times — this was not a coincidence. Setting an explicit no-op
   `build_settings.cmd` (e.g. `"true"`) was also tried and did not help
   either. **The only durable real fix identified but not yet applied**:
   rename the base folder to remove the space (e.g.
   `website-repos-maybewell-site-dist-v2`), then update Base/Publish
   directory to match — a real structural change with meaningful blast
   radius (repo layout, local folder path, this file's own instructions),
   so it needs Dan's explicit go-ahead before anyone does it.

**Net result: `git push` is still NOT a deploy** — it reliably reaches
Netlify (webhook fires within ~1 minute when `build_filter` is left at
its default `null`) but the build almost always self-cancels as "no
content change" even when content genuinely changed. The only reliable
release path remains:

```bash
cd "website-repos/maybewell-site-dist-v2"
npx --yes netlify-cli deploy --prod
```

**Always verify** after *any* release (push or CLI) by fetching a
newly-added asset URL and confirming `image/jpeg`, not `text/html`:

```bash
curl -s -o /dev/null -w "%{content_type} %{http_code}\n" \
  "https://maybewellbooks.com/assets/previews/<some-id>-1.jpg?cb=$RANDOM"
```

Never assume a push or a "Deploy complete" CLI message means it's actually
live — check. If a push-triggered deploy is suspected to have silently
failed, list recent deploys and look for the same error before re-pushing
(re-pushing alone won't fix it, it's a settings problem):

```bash
npx --yes netlify-cli api listSiteDeploys \
  --data '{"site_id":"12dd4eba-e81c-4fa7-87d5-ad18b5d37496","per_page":5}'
```

## Two standing Claude Code agents

Defined in `website-repos/maybewell-site-dist-v2/.claude/agents/`:

- **`daily-product-builder`** — runs daily (scheduled cloud task, ~9am),
  builds up to 5 `Pending` rows from `PRODUCT_QUEUE.md` per run (Figma →
  ReportLab → PyMuPDF QA), sends one `PushNotification`, then **hard-stops
  for Dan's explicit per-product approval before touching git or the site
  at all.** Nothing ships without his sign-off in chat, ever — approval is
  never inferred, never bulk, never carried over from a previous product.
- **`product-brainstormer`** — runs weekly (Mondays ~9:30am), reads
  business/catalog/manifesto context, proposes 3–5 new ideas, and only
  files an idea into `PRODUCT_QUEUE.md`'s buildable queue for the specific
  ideas Dan approves.

Both notify via the built-in `PushNotification` tool (reaches Dan's phone
via Claude Code's Remote Control) — no Telegram, no external service.

**Current queue state** (`PRODUCT_QUEUE.md` at repo root): Days 1–6 and 8
are `Shipped`. **Day 7 (Looking Up, Field Notes field-log) and Days 9–13
(five new Teachers-line ideas from product-brainstormer: The Rumor Mill,
The Object Court, The Prediction Vault, The One-Minute Museum, The
Two-Minute Expedition) are still `Pending`** — not built yet. Resolved
decisions in that file (Road Trip Games merged into Field Notes; Postcards
from Planets Nobody Found = Option A pure-drawing) are settled, don't
relitigate them.

## Key files

```
MAYBEWELL BOOKS/
├── PROJECT_STATUS.md              <- this file
├── PRODUCT_QUEUE.md                <- daily-product-builder's queue + specs + status table
├── PRODUCT_INVENTORY.md            <- every finished PDF, price, path — for Lemon Squeezy
├── <Product Name>/                 <- one folder per product: the real PDF + build/ + samples/
│   └── build/content_*.py, generate_*.py, qa_scan_*.py   <- ReportLab pipeline for that title
├── agent-tools/                    <- the OLDER local "PDF factory": logic/stem/story/words/autumn/mazes/roadtrip
│   ├── catalog_manifest.json       <- status per title (published/pending/retired)
│   ├── generators/, mw_lib/, content/  <- shared brand.py drawing helpers + per-title content
│   └── run_next.py / run_weekly.sh <- weekly launchd job, generates one pending item for review
└── website-repos/maybewell-site-dist-v2/   <- the actual deployed site
    ├── index.html                  <- loads legal/manifesto content, GSAP CDN, then the bundle
    ├── assets/index-e55cf50b.js    <- THE frontend (minified, hand-edited) — VERIFY this hash is current
    ├── assets/legal-content.js     <- Privacy/Terms/Cookies text (EN+ES)
    ├── assets/manifesto-content.js <- the three manifestos (EN done, ES is a ready:false placeholder)
    ├── assets/previews/            <- 3 preview JPGs per product, {id}-1.jpg / -2.jpg / -3.jpg
    ├── netlify.toml                <- functions config + cache headers
    ├── .claude/agents/             <- daily-product-builder.md, product-brainstormer.md
    └── netlify/functions/
        ├── SETUP.md                 <- Lemon Squeezy + Resend setup steps
        ├── lib/_catalog.js          <- SERVER-SIDE source of truth for what's purchasable
        ├── create-checkout.js       <- builds a Lemon Squeezy checkout
        ├── ls-webhook.js            <- receives payment confirmation, sends delivery email via Resend
        ├── download.js              <- token-gated PDF serving (not public URLs)
        └── _assets/                 <- every live product's PDF, bundled privately into the function
```

## Hard-won lessons (read before editing the bundle again)

0. **See "Deploying" section above** — GitHub auto-deploy is connected but
   broken; CLI deploy + live verification is the only trustworthy path
   until Dan fixes Publish directory.
1. **Always rename `index-*.js` when you change it**, and update the
   `<script src>` in `index.html` to match. `/assets/*` is cached
   `must-revalidate, max-age=300` (deliberately NOT immutable).
   `/assets/previews/*` is cached `max-age=86400` (one day, not immutable —
   a URL requested before its file exists can get cached as missing/HTML,
   so a daily revalidation makes that self-healing instead of permanent).
   Missing `/assets/*` returns a real 404 (`404.html`) rather than falling
   through to the SPA rewrite — that fallthrough used to cause genuine
   cache-poisoning of broken preview URLs.
2. **Never trust brace/paren counts by hand when inserting code into the
   minified bundle.** A visual "looks balanced" read is not reliable
   enough — this has caused real breakage more than once. If a manual
   count is uncertain, write a small Python bracket-matcher that walks the
   file respecting strings/template literals (skip `"..."`, `'...'`,
   `` `...` `` including `${...}` interpolation) and returns the exact
   matching-bracket byte offset, then splice at that offset. Always
   `node --check` the *exact* patched file before going further; on
   failure, bisect rather than guess again.
3. Large new content blocks (legal text, catalog data, manifesto text) go
   in **separate plain `<script>` files** loaded before the module bundle
   (`window.X = ...` globals), not spliced into the minified file — lower
   risk, easier to edit later.
4. The Browser-pane test tool sometimes reports `document.hidden = true`,
   pausing `requestAnimationFrame` — GSAP tweens look "stuck" there even
   though real users see them fine. Don't chase it; verify tween mechanics
   with `tween.progress(x)` instead of watching real-time playback.
5. **Client catalog (`available:!0` in the bundle) and server catalog
   (`netlify/functions/lib/_catalog.js`) are two separate lists that must
   move together.** The server list is the real purchase gate (verified:
   posting a fake cart item for an unavailable product is correctly
   rejected); the client list only controls what the UI shows. A product
   needs both, plus its PDF physically present in
   `netlify/functions/_assets/`, before it's real.
6. **Never ship a page count or claim the file doesn't back up.** Twice
   now, placeholder catalog metadata (written before a PDF existed)
   claimed a page count that didn't match the real generated file once it
   was actually built — correct the `pages` field to the verified real
   count at publish time, every time.
7. The `agent-tools/mw_lib/brand.py` cover-drawing helper
   (`draw_cover()`) already draws the real site URL unconditionally on its
   own line — never pass `"maybewellbooks.com"` as its `tagline` argument
   (that was a real, previously-shipped bug affecting every title built
   through that pipeline, including the live Mazes of the Lost City, fixed
   2026-07-20). Every `content/*.py` for that pipeline should define a real
   `TAGLINE`.
8. The Netlify MCP connector's `manage-env-vars` update tool has reported
   success without actually persisting the value (confirmed by immediately
   re-reading — the var wasn't there). The Netlify CLI
   (`netlify env:set KEY value --secret --context production`) is the
   reliable path for env vars; verify afterward via
   `npx netlify-cli api getEnvVars --data '{"account_id":"...","site_id":"..."}'`.

## Immediate next steps, in order

1. Check whether Lemon Squeezy store activation has come through.
2. If yes: follow "What's blocking a real sale" above — copy to live mode,
   set the 3 secrets in Netlify, verify the webhook payload shape, do one
   real test purchase end to end.
3. Separately, ask Dan whether he's fixed Netlify's Publish directory
   setting yet; if so, verify a real push actually deploys before trusting
   push-to-deploy again (see "Deploying" section — don't take "I fixed it"
   as proof on its own, check a live asset after the next real push).
4. Review whatever `daily-product-builder` has queued up as
   `Built (awaiting review)` — check `PRODUCT_QUEUE.md`'s status table
   first thing; there may already be something waiting.
5. Ongoing: the two standing agents keep the queue moving on their own
   schedule. Your job when picking this project back up is mostly
   reviewing what they've already built/proposed and clearing blockers
   like the two above — not necessarily starting new build work from
   scratch.
