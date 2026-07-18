# Maybewell Books — Project Status

_Last updated: 2026-07-15. Written as a handoff summary for a fresh conversation._

## What this is

An e-commerce site selling printable PDF activity books, at **maybewellbooks.com**
(hosted on Netlify, GitHub repo `danielerasmy236-web/maybewellbooks`). Target
market: US + Southeast Asia. Prices $3–5 USD.

The site is a **pre-built, minified React SPA with no build tooling** —
`Website - Repos/maybewell-site-dist-v2/assets/index-c3f2afa1.js` is the only
source file for the frontend (no package.json, no bundler; the hash in the
filename changes on every edit — check index.html for the current one). All frontend
changes are done via careful surgical string-replacement on that minified
file, verified with `node --check` before deploying. **This is the single
most important thing to know before touching the site.**

## What's live right now

- **4 real, purchasable products**: Draw What You Imagine ($5), The
  Impossible Garden ($5), Mazes of the Lost City ($4), The World Is Watching
  ($5, flagship "Field Notes" line, built 2026-07-16 — pareidolia field guide,
  91 pages; build pipeline lives in `The World Is Watching/build/`, Figma
  cover + samples at https://www.figma.com/design/qrEdlUEXAdmcLiIofEgoL5).
  Each has a real PDF, real page count, and 3 real preview-page images shown
  on its product page.
- **"For Teachers and Educators" line — 6 more purchasable products**
  (built 2026-07-17): Chain Story, Group Detective, and Build Without Words,
  each as a $2 Single Sheet (3pp: activity / teacher guide / alternate) and
  a $4 Weekly Module (7pp: teacher intro + 5 days + closing). All full-sheet,
  no cutting, black-&-white-copier-safe (QA enforces a text-luminance check).
  Build pipeline in `For Teachers and Educators/build/` (reuses TWIW fonts).
  Own site section: "Teachers" nav item → landing page (`teachers` route,
  component `MWTeach`, category `classroom`), copy explicitly positions the
  line as enrichment, not curriculum.
- **Three company manifestos** ("On Offline Content", "On Printing It",
  "On Paper and Trees") as in-app pages: footer link → index → detail pages.
  Content lives in `assets/manifesto-content.js` (same pattern as
  legal-content.js); English only, ES block is a `ready:false` placeholder
  that falls back to EN — TODO: translate. Pull-quotes surface on the home
  hero (M1), product buy CTA (M2, all available products), and buy CTA of
  products over 50 pages (M3).
- **Two standing Claude Code agents** (2026-07-18), separate from the local
  PDF-factory `launchd` agent below: `daily-product-builder` (runs daily,
  builds the next `Pending` row of `PRODUCT_QUEUE.md` through
  Figma → ReportLab → PyMuPDF QA, sends a push notification, then hard-stops
  for Dan's approval before touching git/the site at all — nothing ships
  without his explicit sign-off in chat) and `product-brainstormer` (runs
  weekly, proposes 3–5 new product ideas from catalog/manifesto context,
  and only files an idea into the queue once Dan approves it specifically).
  Agent definitions: `Website - Repos/maybewell-site-dist-v2/.claude/agents/`.
  Queue + specs + status table: `PRODUCT_QUEUE.md` at repo root (currently a
  7-day Field Notes batch). Notifications use the built-in `PushNotification`
  tool (reaches Dan's phone via Claude Code's Remote Control) — no Telegram
  bot or external service involved.
- **6 more products are "Coming soon"** in the catalog (not purchasable —
  gated both in the UI and server-side): Little Logic Lab, Space STEM Pack,
  Story Starters, Word Search Safari, The Autumn Book, Paper Games for Road
  Trips. Real PDFs for these already exist as generators, just not yet
  copied into the site (see "PDF factory agent" below).
- **Real cart + checkout UI**, wired to Lemon Squeezy (Merchant of Record)
  via a Netlify Function. Email delivery (not instant download) via Resend.
  **Payments aren't actually live yet** — see "What's blocking a real sale"
  below.
- **Privacy Policy, Terms of Service, Cookie Policy** — real, business-
  specific content in EN + ES (not a lawyer-reviewed doc — flagged to the
  user to get one before fully relying on it).
- **Hand-drawn underline hover animation** on the Shop/About/FAQ nav links
  (GSAP DrawSVGPlugin, loaded via CDN, brand coral color).
- A local, weekly, fully-offline **"PDF factory" agent** (`agent-tools/`)
  that generates the remaining 6 planned products, one per week, into
  `New Products - Pending Review/` for human approval. Runs via macOS
  `launchd` (`com.maybewellbooks.pdffactory`, Mondays 9am). It only
  generates files — never touches git, Netlify, or pricing.

## What's blocking a real sale right now

**Resend is fully wired as of 2026-07-18** — done, not just "should work":
domain `maybewellbooks.com` verified in Resend (DKIM + SPF, all records
`verified`, region `sa-east-1`), a scoped API key
(`maybewellbooks-netlify-production`, sending-only, restricted to this
domain) created and set as a **secret** `RESEND_API_KEY` env var in Netlify
(context: production), plus `ORDERS_FROM_EMAIL` set to
`Maybewell Books <orders@maybewellbooks.com>`. Deployed and live. (An older
API key named "Maybewell Books" from 2026-07-15 also exists in the Resend
account but its token was never captured anywhere — harmless to ignore or
delete later, it's not referenced by anything.) Not yet done: an actual
end-to-end test send through `ls-webhook.js` to confirm delivery works in
practice, not just that the config is correct.

**Lemon Squeezy store activation is still pending** — this is the one real
remaining blocker, and only Dan can clear it:

1. Go to Lemon Squeezy, click "Activate your store", get approved (submitted
   a few days ago, ~2-3 business day review — check for the approval email).
2. **Products created in test mode do NOT carry over** — once approved, use
   "Copy to Live Mode" on the product, which generates a **new Store ID and
   Variant ID** (the test-mode ones currently in Netlify env vars,
   `432241` / `93e3c734-...`, will need to be replaced).
3. Still needed (secrets — set directly in Netlify, never in chat):
   - `LEMONSQUEEZY_API_KEY`
   - `LEMONSQUEEZY_WEBHOOK_SECRET` (from a webhook pointed at
     `https://maybewellbooks.com/.netlify/functions/ls-webhook`, subscribed
     to `order_created`)
   - `DOWNLOAD_TOKEN_SECRET` (any random string, e.g. `openssl rand -hex 32`)
4. Full step-by-step is in
   `Website - Repos/maybewell-site-dist-v2/netlify/functions/SETUP.md`.
5. Once configured: **the `ls-webhook.js` payload shape should be verified
   against a real Lemon Squeezy test webhook** (dashboard → Webhooks → "Send
   test event") before trusting it with real orders — the field names in
   that file are a best guess from docs, not yet confirmed against a live
   payload.

## Key files

```
MAYBEWELL BOOKS/
├── PROJECT_STATUS.md              <- this file
├── The Impossible Garden/, Draw What You Imagine/, Mazes of the Lost City/
│   └── real PDFs for the 3 live products
├── New Products - Pending Review/  <- weekly agent drops new PDFs here
├── agent-tools/                   <- the local PDF-factory agent
│   ├── README.md                  <- how it works, how to run/pause it
│   ├── catalog_manifest.json      <- queue + status of the 7 planned products
│   ├── run_next.py / run_weekly.sh
│   └── generators/, mw_lib/, content/
└── Website - Repos/maybewell-site-dist-v2/   <- the actual deployed site
    ├── index.html                  <- loads legal/manifesto content, GSAP CDN, then the bundle
    ├── assets/index-c3f2afa1.js    <- THE frontend (minified, hand-edited)
    ├── assets/legal-content.js     <- Privacy/Terms/Cookies text (EN+ES)
    ├── assets/manifesto-content.js <- the two manifestos (EN, ES pending)
    ├── assets/previews/            <- product preview page images
    ├── netlify.toml                <- functions config + cache headers
    └── netlify/functions/
        ├── SETUP.md                 <- Lemon Squeezy + Resend setup steps
        ├── lib/_catalog.js          <- SERVER-SIDE source of truth for what's purchasable
        ├── create-checkout.js       <- builds a Lemon Squeezy checkout
        ├── ls-webhook.js            <- receives payment confirmation, sends delivery email
        ├── download.js              <- token-gated PDF serving (not public URLs)
        └── _assets/                 <- the 3 real PDFs, bundled privately into the function
```

## Hard-won lessons (read before editing the bundle again)

0. **GitHub → Netlify auto-deploy is connected but currently BROKEN —
   every push-triggered build fails, verified 2026-07-18.** The Netlify
   site (`maybewellbooks`, site id `12dd4eba-e81c-4fa7-87d5-ad18b5d37496`)
   has GitHub linked (`base directory: Website - Repos/maybewell-site-dist-v2`,
   provider github, webhook confirmed firing on push) — but every build
   Netlify has attempted for a real commit has failed at the same stage:
   `"checking build content for changes": Canceled build due to no
   content change"`, a false positive almost certainly caused by
   **Publish directory being left blank** while Base directory is set (a
   known Netlify monorepo footgun). Confirmed by listing deploys via the
   API: two consecutive real pushes (commits `5962b9f` and `a10ee19`)
   both auto-triggered a build and both were cancelled this way, while the
   site kept serving a day-old deploy. **Until Dan sets Publish directory
   explicitly** (same value as Base directory) in Netlify → Site
   configuration → Build & deploy → Build settings, and that's verified
   with a real push, treat `git push` as NOT a deploy — it's still
   `netlify deploy --prod` (CLI) that actually ships, same as before
   2026-07-18. **Always verify** after any release (push or CLI) by
   fetching a newly-added asset URL and confirming `image/jpeg`, not
   `text/html` — never assume either path worked. If a push-triggered
   deploy is suspected to have silently failed, check
   `npx netlify-cli api listSiteDeploys --data '{"site_id":"12dd4eba-e81c-4fa7-87d5-ad18b5d37496","per_page":5}'`
   for the same "no content change" error before re-pushing (re-pushing
   alone won't fix it — it's a settings problem, not a transient one).
   Separately fixed 2026-07-18: missing `/assets/*` now 404s (new
   `404.html`) instead of falling through to the SPA rewrite and getting
   cached as HTML under the previews' long-lived cache header — that
   SPA-fallback cache poisoning was the original cause of a "previews are
   broken" report, compounded by the site being two days stale from the
   pre-Git-integration gap.

1. **Always rename `index-*.js` when you change it**, and update the
   `<script src>` in `index.html` to match. `/assets/*` is cached
   `must-revalidate, max-age=300` (deliberately NOT `immutable` — that bit
   us once already, see git history "Fix stale browser cache").
   `/assets/previews/*` is cached `max-age=86400` (one day, NOT immutable —
   downgraded 2026-07-18: "append-only" wasn't a strong enough guarantee,
   since a URL can get cached as missing/HTML before its file actually
   deploys; a daily revalidation makes that self-healing instead of
   permanent).
2. **Never trust brace/paren counts alone when inserting new code into the
   minified bundle.** A statement that "looks like" a clean boundary
   (`})};` before `function ap(...)`) can actually be the tail end of a
   still-open expression. Verify with `node --check` on the *exact* patched
   file, and if it fails, bisect: test the prefix-up-to-insertion-point
   alone via `node --check` to confirm it's really a complete, valid
   program before assuming your insertion point is safe.
3. Large new content blocks (legal text, catalog data) go in **separate
   plain `<script>` files loaded before the module bundle** (`window.X = ...`
   globals), not spliced into the minified file directly — much lower risk,
   much easier to edit later.
4. The Browser pane test tool in this environment sometimes reports
   `document.hidden = true`, which pauses `requestAnimationFrame` — GSAP
   tweens will appear "stuck" there even though they work fine for real
   users. Don't chase that as a bug; verify tween mechanics with
   `tween.progress(x)` instead of waiting for real-time playback.
5. Server-side purchasability (`netlify/functions/lib/_catalog.js`) and
   client-side catalog (`available:!0` flags in the bundle) are **two
   separate lists that must be updated together** — the server list is the
   real gate (verified: posting a fake cart item for an unavailable product
   is correctly rejected), the client list just controls what the UI shows.

## Immediate next steps, in order

1. Wait for Lemon Squeezy store activation email.
2. Copy the product to live mode, get new Store ID / Variant ID.
3. Update `LEMONSQUEEZY_STORE_ID` / `LEMONSQUEEZY_VARIANT_ID` in Netlify
   (these two are NOT secret, safe to paste in chat for help).
4. Get the 4 secrets (API key, webhook secret, Resend key, download token
   secret) and set them directly in Netlify's dashboard.
5. Send a Lemon Squeezy test webhook, check the Netlify function log for
   `ls-webhook`, confirm the payload field names match what the code
   expects (`payload.data.attributes.user_email`,
   `payload.meta.custom_data.cart`) — adjust if not.
6. Do one real test purchase (Lemon Squeezy has a test-card mode) end to
   end: pay → land on `/order-success.html` → email arrives → download
   link in the email actually works.
7. Ongoing: each Monday, `agent-tools/` drops a new product PDF into
   `New Products - Pending Review/`. To publish one: copy its PDF into its
   own top-level folder + into `netlify/functions/_assets/`, add it to
   `netlify/functions/lib/_catalog.js`, add `available:!0` to its entry in
   the client bundle, generate 3 preview images, commit, push, deploy.
