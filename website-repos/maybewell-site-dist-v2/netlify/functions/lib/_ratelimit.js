// Best-effort rate limiting for public serverless functions.
//
// This is a fixed-window counter kept in module-scope memory. It is NOT a
// distributed rate limiter: Netlify Functions run in separate, ephemeral
// containers, so a burst spread across multiple cold starts (or multiple
// concurrent warm containers) won't all see the same counter. What this
// DOES stop, reliably: a script hammering an endpoint in a tight loop,
// which keeps hitting the same warm container and gets cut off fast — the
// most common real-world abuse pattern (accidental retry loops, naive
// scrapers, a broken frontend stuck in a request loop). Defense in depth,
// not a guarantee — Netlify's own platform-level abuse protection sits
// above this regardless.
//
// If real abuse shows up in the logs despite this, the next step up is a
// shared store (Netlify Blobs) so every container sees the same counts.

const buckets = new Map(); // key -> { count, resetAt }

function clientIp(event) {
  const h = event.headers || {};
  return (
    h["x-nf-client-connection-ip"] ||
    (h["x-forwarded-for"] || "").split(",")[0].trim() ||
    "unknown"
  );
}

// Opportunistic cleanup so `buckets` doesn't grow forever in a long-lived
// warm container — runs on every call, cheap for realistic traffic volumes.
function sweep(now) {
  for (const [key, bucket] of buckets) {
    if (bucket.resetAt <= now) buckets.delete(key);
  }
}

/**
 * @param {string} scope - a short name for the endpoint, e.g. "checkout"
 * @param {import("aws-lambda").APIGatewayProxyEvent} event
 * @param {{max: number, windowMs: number}} opts
 * @returns {{allowed: boolean, retryAfterSeconds: number}}
 */
function rateLimit(scope, event, opts) {
  const now = Date.now();
  sweep(now);

  const key = `${scope}:${clientIp(event)}`;
  let bucket = buckets.get(key);

  if (!bucket || bucket.resetAt <= now) {
    bucket = { count: 0, resetAt: now + opts.windowMs };
    buckets.set(key, bucket);
  }

  bucket.count += 1;

  if (bucket.count > opts.max) {
    return { allowed: false, retryAfterSeconds: Math.ceil((bucket.resetAt - now) / 1000) };
  }
  return { allowed: true, retryAfterSeconds: 0 };
}

function tooManyRequests(retryAfterSeconds, message) {
  return {
    statusCode: 429,
    headers: { "Content-Type": "application/json", "Retry-After": String(retryAfterSeconds) },
    body: JSON.stringify({ error: message || "Too many requests. Please try again shortly." }),
  };
}

module.exports = { rateLimit, tooManyRequests, clientIp };
