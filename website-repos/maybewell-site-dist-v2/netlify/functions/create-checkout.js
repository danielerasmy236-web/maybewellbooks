// POST { items: ["mazes", "garden"], email: "buyer@example.com" }
// -> { url: "https://maybewellbooks.lemonsqueezy.com/checkout/..." }
//
// Prices are looked up server-side from _catalog.js — never trust a
// client-supplied price. Lemon Squeezy only supports one line item per
// checkout, so a multi-item cart is collapsed into a single custom_price
// checkout with a description listing what's in it; the full list of
// purchased ids travels through as custom_data so the webhook knows what
// to deliver.

const { PRODUCTS } = require("./lib/_catalog");
const { rateLimit, tooManyRequests } = require("./lib/_ratelimit");

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method not allowed" };
  }

  // Real checkout attempts from one visitor are rare; this only ever fires
  // on a retry loop or a script hammering the endpoint (each call reaches
  // Lemon Squeezy's API, which we don't want spammed).
  const limit = rateLimit("checkout", event, { max: 10, windowMs: 5 * 60 * 1000 });
  if (!limit.allowed) {
    return tooManyRequests(limit.retryAfterSeconds, "Too many checkout attempts. Please wait a few minutes and try again.");
  }

  let body;
  try {
    body = JSON.parse(event.body || "{}");
  } catch {
    return { statusCode: 400, body: "Invalid JSON" };
  }

  const items = Array.isArray(body.items) ? body.items.filter((id) => PRODUCTS[id]) : [];
  const email = typeof body.email === "string" ? body.email.trim() : "";

  if (items.length === 0) {
    return { statusCode: 400, body: JSON.stringify({ error: "Cart is empty or contains unavailable items." }) };
  }
  if (!email.includes("@")) {
    return { statusCode: 400, body: JSON.stringify({ error: "A valid email is required." }) };
  }

  const apiKey = process.env.LEMONSQUEEZY_API_KEY;
  const storeId = process.env.LEMONSQUEEZY_STORE_ID;
  const variantId = process.env.LEMONSQUEEZY_VARIANT_ID;
  if (!apiKey || !storeId || !variantId) {
    return { statusCode: 500, body: JSON.stringify({ error: "Checkout is not configured yet." }) };
  }

  const totalCents = items.reduce((sum, id) => sum + PRODUCTS[id].price, 0);
  const description = items.map((id) => PRODUCTS[id].name).join(", ");
  const siteUrl = process.env.URL || "https://maybewellbooks.com";

  const payload = {
    data: {
      type: "checkouts",
      attributes: {
        custom_price: totalCents,
        product_options: {
          name: "Maybewell Books order",
          description,
          redirect_url: `${siteUrl}/order-success.html`,
        },
        checkout_data: {
          email,
          custom: { cart: items.join(",") },
        },
        expires_at: null,
      },
      relationships: {
        store: { data: { type: "stores", id: String(storeId) } },
        variant: { data: { type: "variants", id: String(variantId) } },
      },
    },
  };

  try {
    const res = await fetch("https://api.lemonsqueezy.com/v1/checkouts", {
      method: "POST",
      headers: {
        Accept: "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json",
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify(payload),
    });

    const json = await res.json();
    if (!res.ok) {
      console.error("Lemon Squeezy error:", JSON.stringify(json));
      return { statusCode: 502, body: JSON.stringify({ error: "Could not start checkout." }) };
    }

    const url = json.data && json.data.attributes && json.data.attributes.url;
    if (!url) {
      return { statusCode: 502, body: JSON.stringify({ error: "Checkout URL missing from response." }) };
    }

    return { statusCode: 200, body: JSON.stringify({ url }) };
  } catch (err) {
    console.error("create-checkout failed:", err);
    return { statusCode: 500, body: JSON.stringify({ error: "Unexpected error starting checkout." }) };
  }
};
