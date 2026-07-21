/* Maybewell Books — real URL routing for the SPA.
 *
 * The bundle previously had NONE: every page (home, shop, every product,
 * about, faq...) lived at "/" — pure in-memory `useState({name:"home"})`,
 * no `pushState`, no reading of `location`. That makes a real sitemap
 * impossible (there is nothing to list but "/"), breaks the browser
 * back/forward buttons, and means a product link can't be shared or
 * refreshed — it always lands on the homepage.
 *
 * window.mwRouteFromPath() and window.mwPushPath() below are called from
 * two one-line edits inside the bundle itself (search index.html's current
 * bundle for `mwRouteFromPath` / `mwPushPath` to find them): the view
 * state's initial value now reads the real URL on load, and the app's
 * internal navigate function now also calls pushState when the visitor
 * clicks around.
 *
 * MUST run and define these on `window` before the module bundle evaluates
 * (the bundle calls mwRouteFromPath() during its very first render) — so
 * this loads as a plain, non-deferred, non-module script placed BEFORE the
 * bundle's <script type="module">, same pattern as legal-content.js and
 * manifesto-content.js already use in index.html.
 *
 * Netlify's existing catch-all redirect (`/* -> /index.html`, status 200 —
 * see netlify.toml) already serves this same index.html for any of these
 * paths, so a cold load at e.g. /product/dwyi works with no server changes.
 */
(function () {
  "use strict";

  var MW_ROUTES = [
    ["home", "/"],
    ["shop", "/shop"],
    ["about", "/about"],
    ["faq", "/faq"],
    ["teachers", "/teachers"],
    ["manifesto", "/manifesto"],
    ["library", "/library"],
    ["checkout", "/checkout"],
    ["privacy", "/privacy"],
    ["terms", "/terms"],
    ["cookies", "/cookies"],
  ];

  window.mwRouteFromPath = function () {
    try {
      var path = window.location.pathname.replace(/\/+$/, "") || "/";
      var m = path.match(/^\/product\/([a-z0-9_-]+)$/i);
      if (m) return { name: "product", id: m[1] };
      for (var i = 0; i < MW_ROUTES.length; i++) {
        if (MW_ROUTES[i][1] === path) return { name: MW_ROUTES[i][0] };
      }
    } catch (e) {}
    return { name: "home" };
  };

  window.mwPushPath = function (view) {
    try {
      var path = "/";
      if (view && view.name === "product" && view.id) {
        path = "/product/" + view.id;
      } else {
        for (var i = 0; i < MW_ROUTES.length; i++) {
          if (MW_ROUTES[i][0] === (view && view.name)) { path = MW_ROUTES[i][1]; break; }
        }
      }
      if (window.location.pathname !== path) {
        window.history.pushState({ mw: true }, "", path);
      }
    } catch (e) {}
  };

  // Simplest robust back/forward: a full reload re-runs mwRouteFromPath()
  // on boot, which reads the (now browser-updated) URL. Avoids needing a
  // reference into React's closed-over setState from outside React itself.
  window.addEventListener("popstate", function () {
    window.location.reload();
  });
})();
