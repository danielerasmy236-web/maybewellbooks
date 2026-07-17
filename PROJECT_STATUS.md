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
- **Two company manifestos** ("On Offline Content", "On Printing It") as
  in-app pages: footer link → index → two detail pages. Content lives in
  `assets/manifesto-content.js` (same pattern as legal-content.js); English
  only, ES block is a `ready:false` placeholder that falls back to EN —
  TODO: translate. Pull-quotes surface on the home hero (M1) and product
  buy CTA (M2).
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

**Lemon Squeezy store activation is pending** (submitted, waiting on their
~2-3 business day review — as of last check, still waiting). Until that
clears:

1. User needs to go to Lemon Squeezy, click "Activate your store", get
   approved.
2. **Products created in test mode do NOT carry over** — once approved, use
   "Copy to Live Mode" on the product, which generates a **new Store ID and
   Variant ID** (the test-mode ones currently in Netlify env vars,
   `432241` / `93e3c734-...`, will need to be replaced).
3. Still needed (none of these were ever shared in chat, by design — they're
   secrets):
   - `LEMONSQUEEZY_API_KEY`
   - `LEMONSQUEEZY_WEBHOOK_SECRET` (from a webhook pointed at
     `https://maybewellbooks.com/.netlify/functions/ls-webhook`, subscribed
     to `order_created`)
   - `RESEND_API_KEY` (domain `maybewellbooks.com` is already verified in
     Resend — confirmed working)
   - `DOWNLOAD_TOKEN_SECRET` (any random string, e.g. `openssl rand -hex 32`)
   - All of these get set directly in **Netlify → Site configuration →
     Environment variables** — never in chat.
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

1. **Always rename `index-*.js` when you change it**, and update the
   `<script src>` in `index.html` to match. `/assets/*` is cached
   `must-revalidate, max-age=300` (deliberately NOT `immutable` — that bit
   us once already, see git history "Fix stale browser cache").
   `/assets/previews/*` IS cached immutable long-term since those files are
   genuinely append-only.
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
