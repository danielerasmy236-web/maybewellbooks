# Maybewell Books — Project Status / Handover Brief

_Last updated: 2026-07-21. Written to be read cold, at the start of a brand
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
  atlas), Letter to the Future (22pp, correspondence/sealed-envelope book),
  Road Trip Games (22pp, $4, 18 two-player pencil games + scorecard).
- **Puzzles / STEM / Writing / Seasonal** (the original "PDF-factory"
  catalog, $3–4): Mazes of the Lost City (61pp), Little Logic Lab (48pp),
  Space STEM Pack (16pp — genuinely short but complete, 12 real projects),
  Story Starters (72pp), Word Search Safari (47pp).
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

**Interactive layer (added 2026-07-20, replaces the old hero drawing
board):** `assets/mw-interactive.js` — a plain deferred script, loaded
AFTER the bundle, zero React internals. Two features: (1) **"Margins
mode"** — a pencil FAB (bottom-right) that turns the whole page into a
drawing overlay, with rotating REAL prompts from the Imagine-line books
(real page numbers, verified against the shipped PDFs), a "Get the book"
CTA that navigates the SPA to the product card, and a "Print your page"
button that prints prompt+drawing as a Maybewell-style book page via a
hidden iframe; scroll is locked while drawing (mobile scroll/draw
conflict). The hero's right column (`.mw-hero-r`) now renders EMPTY in the
bundle (the old drawboard's call site `s.jsx(ap,{t:n})` was replaced with
`null`; the dead `ap` function remains, harmless) and the script mounts an
invitation card into it. (2) **"My library" as a bookshelf of 3D books** —
CSS-only styling (no bundle surgery, no React-DOM insertion) plus one
small JS pass. The CSS restyles the bundle's `.mw-libgrid`/`.mw-librow`
(a plain row list) into covers standing on warm wooden shelf ledges,
labels hanging beneath, lift-on-hover revealing the download button; the
empty state becomes an empty shelf (the bundle's own copy already says
"waiting on the shelf"). Each cover is a real 3D book — ported from a
React/Tailwind `<Book>` component Dan supplied, since this repo has no
build tooling to compile JSX or resolve Tailwind: `perspective:900px` on
the wrapper, `preserve-3d` on `.mw-cover`, `::before` = back cover at
`translateZ(-13px)`, `::after` = page block rotated 90° on the right
edge, spine shading in `.mw-cover`'s existing 9% padding, and a
`rotateY(-20deg)` hover. **Never put `filter` on those ancestors — it
flattens `preserve-3d`** (this silently killed the effect once; the
shadow lives in `box-shadow` instead).

`fitLibraryCovers()` auto-sizes each cover title: the bundle hardcodes
`fontSize:19px` inline (sized for full-page covers), which overflowed the
120px book both ways. It steps 15px→8px per book until the longest whole
word fits the width and lines fit the height, writing inline with
`important` (must beat React's inline size *and* the stylesheet
fallback). **Mid-word breaking is deliberately off** — a `break-word`
attempt "fit" by butchering words ("The Impossibl/e Garden"), which reads
worse than overflow; `.mwi-break` is a last-resort class only.

Everything is scoped `.mw-root .mw-librow ...` so only the library gets
3D books — shop/product/cart covers stay flat (verified). The
MutationObserver watches childList/characterData but **not attributes**,
so the JS writing inline styles can't retrigger it.

To DEMO the library with content: owned books live in React state
(`[d,v]=I.useState([])`, no persistence — populated only by real
checkout), so seed a throwaway preview bundle by replacing `useState([])`
with a few `{id,date}` objects and point index.html at it; **never ship
that seed**. Language is detected from `.mw-langbtn` (it shows the OTHER
language: "ES" = site in EN). (A dot-to-dot shop star was built and then
removed at Dan's request; don't reintroduce it.)

**Road Trip Games shipped 2026-07-20** (id `tripgames`) — the resolved
decision in `PRODUCT_QUEUE.md` to merge the old "Paper Games for Road
Trips" (id `roadtrip`, never built/shipped) into a single Field Notes
product is now fully implemented. The old `roadtrip` id/placeholder no
longer appears anywhere on the site; its content/generator files remain in
`agent-tools/` untouched as a historical record only — never build or ship
under that old id.

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

## ⛔ DEPLOYS ARE BLOCKED (2026-07-21): Netlify credits exhausted

**Nothing has reached production since commit `f541509`.** Every deploy
after it is rejected before it starts:

```
"state": "error", "skipped": true,
"error_message": "Skipped due to account credit usage exceeded"
```

This is an **account-level block, not a build problem** — `netlify deploy
--prod` from the CLI also fails (`JSONHTTPError: Forbidden`), so there is
no workaround from this side. Netlify migrated this Free account to a
**shared credit pool** (`type_slug: "credit-free"`, 300 credits/month
covering builds, dev servers, etc.), and the 2026-07-20 session burned
through it diagnosing the push-to-deploy bug (many forced `clear_cache`
rebuilds).

- Usage period: **2026-07-13 → 2026-08-13** (auto-resets on that date)
- A grace top-up was already auto-granted 2026-07-21 01:26 and was not enough
- `has_stripe_payment_method: true` but `auto_topup_enabled: false`

**Only Dan can unblock it** (all three options involve money or waiting;
do not attempt billing changes on his behalf): enable **Auto top-up**, or
upgrade the plan, or wait for the 2026-08-13 reset. Check current state:

```bash
npx --yes netlify-cli api getAccount --data '{"account_id":"698faf9b0daa0ff131996bc0"}'
```

**Waiting in the repo, already committed and pushed, will go live on the
first successful deploy:** Road Trip Games (`tripgames`), The
Grandparents' Book cover with the For Every Chapter ribbon, "margins
mode" + the bookshelf library, and the removal of The Autumn Book.

## Deploying: mechanism FIXED (2026-07-20) — but see the credit block above

The Netlify site (`maybewellbooks`, site id
`12dd4eba-e81c-4fa7-87d5-ad18b5d37496`) has GitHub linked (base directory
`website-repos/maybewell-site-dist-v2`). As of 2026-07-20, `git push origin
main` triggers a real, successful automatic deploy — confirmed twice in a
row with genuine content changes (`aac38aa`, `25843e1`), both landing
`state: ready` within ~1 minute of push, no manual intervention. Two bugs
were found and fixed this session:

1. **`build_settings.dir` (Publish directory) was `null`.** Since
   `base_rel_dir: true`, the correct value is `.` (meaning "same folder as
   Base directory") — NOT the full path repeated (that duplicates into
   `base/base` and produces a hard "Deploy directory ... does not exist"
   failure; the real error only shows in the public deploy log at
   `https://app.netlify.com/projects/maybewellbooks/deploys/<id>` → click
   the "Deploying" step — the top-level `error_message` from
   `getSiteDeploy` is often misleadingly generic). Fixed: `dir: "."`.
2. **The base directory name had a space in it** (`Website - Repos/...`),
   which was confusing Netlify's monorepo "did anything change under this
   path" diff heuristic — every real push-triggered build was
   self-cancelling as `Canceled build due to no content change`, a false
   positive, even on genuine edits (reproduced 3 times in a row). Fixed by
   renaming the folder to `website-repos/maybewell-site-dist-v2` (no
   space) at the repo root, updating every path reference in docs/config,
   and updating Netlify's Base directory to match via the API. **Do not
   rename this folder again or reintroduce a space in the path** — this
   was the actual root cause, confirmed by the false-positive disappearing
   immediately after the rename, and re-verified with `.claude/`,
   `netlify/functions`, and all product PDFs intact under the new path.
   (Also tried and explicitly ruled out along the way, in case anyone is
   tempted to revisit them: setting `build_settings.build_filter` to force
   always-build — doesn't stop the false positive and appears to silently
   stop GitHub-webhook-triggered deploys from being created at all; and
   setting an explicit no-op `build_settings.cmd` — no effect either.)

`git push` is now a real deploy. Still, **always verify** after *any*
release (push or CLI) by fetching a newly-added asset URL and confirming
`image/jpeg`, not `text/html` — don't blind-trust a green status:

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
are `Shipped`, and Road Trip Games (the merged-decision item, no day
number) shipped 2026-07-20. **Day 7 (Looking Up, Field Notes field-log) and
Days 9–13 (five new Teachers-line ideas from product-brainstormer: The
Rumor Mill, The Object Court, The Prediction Vault, The One-Minute Museum,
The Two-Minute Expedition) are still `Pending`** — not built yet. The
remaining resolved decision in that file (Postcards from Planets Nobody
Found = Option A pure-drawing) is settled, don't relitigate it.

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
    ├── assets/index-*.js           <- THE frontend (minified, hand-edited) — check index.html for the current hash
    ├── assets/mw-interactive.js    <- "margins mode" drawing overlay + shop dot-to-dot star (plain script, loads after bundle)
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

0. **DEPLOYS ARE CURRENTLY BLOCKED** on exhausted Netlify credits — see
   the "⛔ DEPLOYS ARE BLOCKED" section above before promising anything
   will go live. The push-to-deploy *mechanism* is fixed (2026-07-20);
   once credits are restored, `git push` is a real deploy again — but
   always verify a live asset after anything you actually care about.
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

1. **Ask Dan whether the Netlify credit block is cleared** (auto top-up
   enabled, plan upgraded, or the 2026-08-13 reset passed). Verify with
   `getAccount` — don't take "I fixed it" as proof. Until then **nothing
   ships**, and a pile of finished work is queued behind it (Road Trip
   Games, the Grandparents ribbon cover, margins mode, the bookshelf
   library, the Autumn Book removal).
2. Once unblocked: push (or trigger a build), confirm `state: ready`, then
   fetch a live asset to prove it — e.g.
   `https://maybewellbooks.com/assets/previews/tripgames-1.jpg` should be
   `image/jpeg 200`, and the site's `index.html` should reference the
   current bundle hash.
3. Check whether Lemon Squeezy store activation has come through (as of
   2026-07-21, still not — only the "application received" email from
   2026-07-15 exists, no approval yet). Polar.sh remains the researched
   plan B (MoR, near-instant onboarding; its 2026 free tier is 5% + 50¢,
   so it is no longer *cheaper* than LS — the reason to switch is speed).
4. If approved: follow "What's blocking a real sale" above — copy to live
   mode, set the 3 secrets in Netlify (`DOWNLOAD_TOKEN_SECRET` is already
   set and verified), confirm the webhook payload shape against a real
   test event, then one real end-to-end test purchase.
5. **"For Every Chapter" (6 senior-line products) is built and QA-clean
   but NOT integrated** — no prices agreed, not in either catalog, no
   preview JPGs generated. Needs Dan's per-product approval + pricing
   before shipping (see the line's section in `PRODUCT_QUEUE.md` history
   and the per-product folders at repo root).
6. Review whatever `daily-product-builder` has queued as
   `Built (awaiting review)` in `PRODUCT_QUEUE.md`; as of 2026-07-21
   nothing is in that state (Day 7 and Days 9–13 are still `Pending`).
