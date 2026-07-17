/* Company manifestos for Maybewell Books.
 * Loaded as a plain global before the app bundle (same pattern as
 * legal-content.js) so the minified, no-build React app can read
 * window.__MW_MANIFESTO__ without embedding long copy in the bundle.
 *
 * i18n: English is the source of truth for now. The `es` block is a
 * placeholder — `ready:false` makes the app fall back to English until a
 * real translation lands. TODO: translate to Spanish and set ready:true.
 */
window.__MW_MANIFESTO__ = {
  en: {
    ready: true,
    index_title: "Our Manifesto",
    index_sub: "Three promises we print at the front of everything we make.",
    read_it: "Read it",
    // Pull-quotes surfaced elsewhere in the site:
    pull1: "We don't make apps. We make paper.",   // homepage, near the hero
    pull2: "Print it. Keep it. Mark it up. It's yours.", // product page, at the buy CTA
    pull3: "Print what you'll actually use.",      // product pages over ~50 pages, at the buy CTA
    m1: {
      kicker: "MANIFESTO 01 — ON OFFLINE CONTENT",
      title: "On Offline Content",
      lead: "We don't make apps. We make paper.",
      paras: [
        "We live surrounded by screens built, on purpose, to never let go. Every notification, every infinite scroll, every “just one more” was engineered by very smart people who want your attention more than you want it back.",
        "We don't compete with that. We can't, and we don't want to.",
        "What we make instead is simpler and more stubborn: paper, a pencil, and a question strange enough to pull you out of the current for a while. No autoplay. No “next episode in 5 seconds.” No one measuring how long they kept you looking.",
        "If you finish this page and want to keep drawing instead of reaching for your phone, we win. If it gave you an excuse to talk to whoever's sitting next to you, we win twice.",
        "The world already has enough asking for your attention inward, toward the screen. We only ask you one thing:",
      ],
      closer: "Go outside.",
      sign: "— Maybewell Books",
    },
    m2: {
      kicker: "MANIFESTO 02 — ON PRINTING IT",
      title: "On Printing It",
      lead: "Print it. Really.",
      paras: [
        "This wasn't meant to stay a PDF, or to be read on a tablet with the brightness turned halfway down. It was made to come out of the printer still warm, a little crooked at the edges if your printer's anything like ours, and to be held in your hands.",
        "Break the spine if you want. Spill coffee on a corner. Draw outside the lines — honestly, we're asking you to.",
        "A file in the cloud isn't fully yours: it lives on a server, syncs, updates, can vanish with a forgotten password. A sheet of paper with your handwriting on it is yours in a way no file can be. It gets kept in a drawer, lent to a friend, found by accident ten years later, and reminds you who you were when you filled it in.",
        "We didn't make this book for you to look at. We made it for you to use until it's worn out.",
      ],
      closer: "Print it. Keep it. Mark it up. It's yours.",
      sign: "— Maybewell Books",
    },
    m3: {
      kicker: "MANIFESTO 03 — ON PAPER AND TREES",
      title: "On Paper and Trees",
      lead: "Trees are the heroes of this moment.",
      paras: [
        "Trees give us air to breathe. They give us shade on a hot day. They give us a place to sit down when we need one. And they give us paper — paper that lets us live a moment fully, immediately, without a screen standing between us and it. That's why we use paper.",
        "We know what we're asking. Some of our books run 80 pages or more, and in a moment when everyone's counting what they consume, that's not nothing. We don't pretend otherwise.",
        "So we mean it when we say: print what you'll actually use. Skip the pages you know you won't fill. Share one copy between a family instead of printing five. And when you can, choose recycled paper, or a printer that plants what it uses.",
        "A tree spent years growing so a handful of its pages could hold your handwriting, your drawings, a kid's terrible-wonderful joke scribbled in the margin.",
      ],
      closer: "That's a fair trade only if we don't waste it.",
      sign: "— Maybewell Books",
    },
  },
  es: {
    // TODO: Spanish translation pending — app falls back to English while
    // ready is false. Keep the same structure as `en` when translating.
    ready: false,
    index_title: "",
    index_sub: "",
    read_it: "",
    pull1: "",
    pull2: "",
    pull3: "",
    m1: { kicker: "", title: "", lead: "", paras: [], closer: "", sign: "" },
    m2: { kicker: "", title: "", lead: "", paras: [], closer: "", sign: "" },
    m3: { kicker: "", title: "", lead: "", paras: [], closer: "", sign: "" },
  },
};

/* Language-aware accessor with English fallback while a translation isn't
 * ready. The bundle calls this instead of poking the object directly. */
window.__MW_MANIFESTO_GET__ = function (lang) {
  var m = window.__MW_MANIFESTO__ || {};
  return (m[lang] && m[lang].ready) ? m[lang] : (m.en || {});
};
