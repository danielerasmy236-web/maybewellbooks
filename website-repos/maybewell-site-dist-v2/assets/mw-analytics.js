// Umami analytics, gated behind cookie consent (window.mwConsent(), defined
// in mw-interactive.js). Nothing is injected until the visitor accepts.
(function () {
  "use strict";
  var loaded = false;

  function inject() {
    if (loaded) return;
    loaded = true;
    var s = document.createElement("script");
    s.defer = true;
    s.src = "https://cloud.umami.is/script.js";
    s.setAttribute("data-website-id", "92f23b47-3fea-4cf9-b57a-aada71efd821");
    document.head.appendChild(s);
  }

  // Called on boot (consent from a prior visit) and again right after the
  // visitor clicks "accept" in the cookie banner.
  window.mwLoadAnalytics = function () {
    try {
      if (window.mwConsent && window.mwConsent()) inject();
    } catch (e) {}
  };

  window.mwLoadAnalytics();
})();
