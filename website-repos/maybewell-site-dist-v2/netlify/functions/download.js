// GET /.netlify/functions/download?id=mazes&order=123&token=...
//
// Serves a purchased PDF only if the token matches what ls-webhook.js
// generated for that (order, product) pair. The file itself is bundled
// into this function (see netlify.toml included_files) and is never a
// public static asset, so there is no way to reach it without a valid
// token from a real order confirmation email.

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { PRODUCTS } = require("./lib/_catalog");
const { rateLimit, tooManyRequests } = require("./lib/_ratelimit");

function expectedToken(orderId, productId, secret) {
  return crypto.createHmac("sha256", secret).update(`${orderId}:${productId}`).digest("hex");
}

exports.handler = async (event) => {
  const { id, order, token } = event.queryStringParameters || {};
  const secret = process.env.DOWNLOAD_TOKEN_SECRET;

  if (!id || !order || !token || !secret || !PRODUCTS[id]) {
    return { statusCode: 400, body: "Invalid download link." };
  }

  // A real buyer might re-download a few times; a script trying to guess
  // tokens (computationally hopeless against HMAC-SHA256, but still free
  // to attempt without this) or just hammering the endpoint should not.
  const limit = rateLimit("download", event, { max: 20, windowMs: 5 * 60 * 1000 });
  if (!limit.allowed) {
    return tooManyRequests(limit.retryAfterSeconds, "Too many download attempts. Please wait a few minutes and try again.");
  }

  const expected = expectedToken(order, id, secret);
  const valid =
    expected.length === token.length &&
    crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(token));

  if (!valid) {
    return { statusCode: 403, body: "This download link is invalid or has expired." };
  }

  const filePath = path.join(__dirname, "_assets", PRODUCTS[id].file);
  let fileBuffer;
  try {
    fileBuffer = fs.readFileSync(filePath);
  } catch (err) {
    console.error("download.js: file missing", filePath, err);
    return { statusCode: 500, body: "File temporarily unavailable — contact support." };
  }

  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/pdf",
      "Content-Disposition": `attachment; filename="${PRODUCTS[id].file}"`,
    },
    body: fileBuffer.toString("base64"),
    isBase64Encoded: true,
  };
};
