// Lemon Squeezy webhook receiver.
// Configure this URL (https://maybewellbooks.com/.netlify/functions/ls-webhook)
// in Lemon Squeezy: Settings -> Webhooks, subscribed to "order_created",
// with a signing secret set in LEMONSQUEEZY_WEBHOOK_SECRET.
//
// NOTE: verify the exact payload shape against a real test webhook (Lemon
// Squeezy dashboard -> Webhooks -> your webhook -> "Send test event") before
// going live — field names below match their documented format as of this
// writing, but this is the one integration point worth double-checking with
// a live payload before trusting it with real orders.

const crypto = require("crypto");
const { PRODUCTS } = require("./lib/_catalog");

function isValidSignature(rawBody, signatureHeader, secret) {
  if (!signatureHeader) return false;
  const expected = crypto.createHmac("sha256", secret).update(rawBody).digest("hex");
  const a = Buffer.from(expected);
  const b = Buffer.from(signatureHeader);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

function downloadToken(orderId, productId, secret) {
  return crypto.createHmac("sha256", secret).update(`${orderId}:${productId}`).digest("hex");
}

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method not allowed" };
  }

  const webhookSecret = process.env.LEMONSQUEEZY_WEBHOOK_SECRET;
  const downloadSecret = process.env.DOWNLOAD_TOKEN_SECRET;
  const resendKey = process.env.RESEND_API_KEY;
  const fromAddress = process.env.ORDERS_FROM_EMAIL || "Maybewell Books <orders@maybewellbooks.com>";
  const siteUrl = process.env.URL || "https://maybewellbooks.com";

  if (!webhookSecret || !downloadSecret || !resendKey) {
    console.error("ls-webhook: missing required env vars");
    return { statusCode: 500, body: "Not configured" };
  }

  const rawBody = event.body || "";
  const signature = event.headers["x-signature"] || event.headers["X-Signature"];
  if (!isValidSignature(rawBody, signature, webhookSecret)) {
    return { statusCode: 401, body: "Invalid signature" };
  }

  let payload;
  try {
    payload = JSON.parse(rawBody);
  } catch {
    return { statusCode: 400, body: "Invalid JSON" };
  }

  const eventName = payload.meta && payload.meta.event_name;
  if (eventName !== "order_created") {
    // Acknowledge anything we don't act on so Lemon Squeezy doesn't retry it.
    return { statusCode: 200, body: "Ignored" };
  }

  const orderId = payload.data && payload.data.id;
  const attrs = (payload.data && payload.data.attributes) || {};
  const email = attrs.user_email;
  const customData = (payload.meta && payload.meta.custom_data) || {};
  const cartIds = (customData.cart || "")
    .split(",")
    .map((s) => s.trim())
    .filter((id) => PRODUCTS[id]);

  if (!orderId || !email || cartIds.length === 0) {
    console.error("ls-webhook: missing orderId/email/cart", { orderId, email, cartIds });
    return { statusCode: 200, body: "Missing data, nothing delivered" };
  }

  const links = cartIds.map((id) => {
    const token = downloadToken(orderId, id, downloadSecret);
    const url = `${siteUrl}/.netlify/functions/download?id=${id}&order=${orderId}&token=${token}`;
    return `<li><a href="${url}">${PRODUCTS[id].name}</a></li>`;
  });

  const html = `
    <p>Thank you for your order! Your books are ready:</p>
    <ul>${links.join("")}</ul>
    <p>Each link downloads your PDF directly — save it somewhere safe, it's yours to print as many times as you like.</p>
    <p>— Maybewell Books</p>
  `.trim();

  try {
    const res = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${resendKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: fromAddress,
        to: [email],
        subject: "Your Maybewell Books order is ready",
        html,
      }),
    });

    if (!res.ok) {
      const errText = await res.text();
      console.error("Resend send failed:", errText);
      return { statusCode: 502, body: "Email delivery failed" };
    }
  } catch (err) {
    console.error("ls-webhook: Resend call threw", err);
    return { statusCode: 500, body: "Unexpected error sending email" };
  }

  return { statusCode: 200, body: "Delivered" };
};
