# Going live: what only you can do

The code is done and tested (cart, checkout call, webhook, secure download
all verified locally with `netlify dev`). What's left is account creation
and secret keys — things Claude can't do on your behalf. This is the
complete checklist.

## 1. Lemon Squeezy (payment processor)

1. Create an account at lemonsqueezy.com and create a **Store** for
   Maybewell Books.
2. Create **one Product** with **one Variant** that has a **"Pay what you
   want" / custom price** enabled (minimum price can be $0.50 or so — the
   real price is set per-order by `create-checkout.js` via `custom_price`).
   Name it something generic like "Maybewell Books order" since every
   purchase — one book or several — flows through this single variant.
3. Note down:
   - Your **Store ID** (Settings → Stores)
   - The **Variant ID** you just created (open the product, the ID is in
     the URL or the API)
4. Settings → API → create an **API key**. Copy it once — Lemon Squeezy
   won't show it again.
5. Settings → Webhooks → **Add webhook**:
   - URL: `https://maybewellbooks.com/.netlify/functions/ls-webhook`
   - Event: `order_created`
   - Copy the **signing secret** it generates.
6. Settings → Webhooks → your webhook → **"Send test event"** — then check
   the function logs (Netlify dashboard → your site → Functions → ls-webhook
   → logs) to confirm the payload shape matches what `ls-webhook.js`
   expects (see the comment at the top of that file). Adjust the field
   names there if Lemon Squeezy's actual payload differs.

## 2. Resend (delivery email)

1. Create an account at resend.com.
2. Add and verify your sending domain (e.g. `maybewellbooks.com`) — this
   means adding a few DNS records at wherever your domain is registered.
   Until this is verified, Resend can only send from their own test domain.
3. API Keys → create a key with "Sending access".

## 3. Set these in Netlify (Site settings → Environment variables)

| Variable | Value |
|---|---|
| `LEMONSQUEEZY_API_KEY` | from Lemon Squeezy step 4 |
| `LEMONSQUEEZY_STORE_ID` | from Lemon Squeezy step 3 |
| `LEMONSQUEEZY_VARIANT_ID` | from Lemon Squeezy step 3 |
| `LEMONSQUEEZY_WEBHOOK_SECRET` | from Lemon Squeezy step 5 |
| `RESEND_API_KEY` | from Resend step 3 |
| `ORDERS_FROM_EMAIL` | e.g. `Maybewell Books <orders@maybewellbooks.com>` |
| `DOWNLOAD_TOKEN_SECRET` | any long random string — this signs download links, it doesn't come from either service. Generate one with `openssl rand -hex 32` in Terminal. |

Set these directly in Netlify's dashboard (Site configuration → Environment
variables) — never paste secret keys into chat with Claude, including this
one. None of this needs a code change or a new deploy; functions read
`process.env` at request time.

## 4. Go live

Once the env vars are set, no further deploy is needed — just try a real
$0.50-ish test purchase (Lemon Squeezy has a test mode toggle in their
dashboard so you don't need to use a real card) and confirm:

1. Checkout redirects you to Lemon Squeezy correctly.
2. After paying, you land on `/order-success.html`.
3. Within a minute or two, an email arrives with a working download link.

## Adding a product once it's approved

Only 3 of 9 catalog products are wired for sale right now (`dwyi`,
`garden`, `mazes`) — see `netlify/functions/lib/_catalog.js`. When you
approve a new product from the weekly PDF-factory queue (see
`agent-tools/README.md`):

1. Copy its PDF into `netlify/functions/_assets/`.
2. Add it to `PRODUCTS` in `netlify/functions/lib/_catalog.js` (id, name,
   price in cents, filename).
3. Add `available:!0` to that product's entry in the client catalog inside
   `assets/index-*.js` (ask Claude to do this part — it's a minified bundle
   edit, same pattern as the other product launches).
4. Commit, push, deploy.
