/* Maybewell Books — interactive layer ("Margins mode" + bookshelf library).
 *
 * Self-contained vanilla script, loaded as a plain deferred script AFTER the
 * React bundle (see index.html). It never reaches into React internals:
 *  - The pencil button + full-page drawing overlay are appended to <body>.
 *  - The hero invitation mounts into .mw-hero-r, which the bundle renders
 *    EMPTY (the old hero drawing board was removed and its call site
 *    replaced with null), so React never manages children there.
 *
 * All prompts below are real prompts from the printed books, with their
 * real page numbers (verified against the shipped PDFs via PyMuPDF).
 *
 * (Real URL routing — window.mwRouteFromPath / window.mwPushPath — lives in
 * the separate mw-routing.js, loaded synchronously in <head> BEFORE the
 * bundle, because the bundle needs those functions at first render, before
 * this deferred script has even started. See mw-routing.js for why.)
 */
(function () {
  "use strict";

  var INK = "#20303A";
  var PUTTY = "#F3EEE6";
  var OCHRE = "#D99A2B";
  var TEAL = "#2A9D8F";
  var CORAL = "#E8604C";
  var VIOLET = "#7C6FD0";
  var SWATCHES = [INK, OCHRE, TEAL, CORAL, VIOLET];
  var WOOD = "#C08A3E";     // shelf ledge (warm wood, sits with the ochre)
  var WOOD_D = "#946325";   // ledge underside shadow

  // Real prompts, real page numbers. {book id, display name, total pages}
  var BOOKS = {
    dwyi: { name: "Draw What You Imagine", pages: 94 },
    garden: { name: "The Impossible Garden", pages: 73 },
    machines: { name: "Machines Nobody's Built Yet", pages: 72 },
  };
  var PROMPTS = [
    { t: "Sadness built a house. What does it look like inside?", b: "dwyi", p: 9 },
    { t: "The last page of a notebook. What drawing has it been holding for years?", b: "dwyi", p: 27 },
    { t: "Draw the school for animals who taught themselves to read.", b: "dwyi", p: 36 },
    { t: "The last flower of a species nobody ever named. Draw its portrait so it isn't forgotten.", b: "garden", p: 9 },
    { t: "Draw what a tree dreams about in winter.", b: "garden", p: 30 },
    { t: "A lightning bolt struck this tree and now it glows from inside. Draw it at midnight.", b: "garden", p: 37 },
    { t: "Draw the machine that turns boredom into something useful.", b: "machines", p: 9 },
    { t: "Draw the machine that gave the wind its first direction.", b: "machines", p: 23 },
    { t: 'Draw a machine that exists only to say "you can do this."', b: "machines", p: 30 },
  ];

  var STR = {
    en: {
      fab: "Draw on this page",
      hero_kicker: "THE MARGINS ARE YOURS",
      hero_title: "This whole page is a margin.",
      hero_body: "Every Maybewell book starts with a blank space and one good prompt. Try one — right here, on top of everything.",
      hero_btn: "Pick up the pencil",
      credit: function (b, p) { return "— from " + b + ", page " + p; },
      more: function (n) { return "There are " + n + " more pages like this. On paper."; },
      get_book: "Get the book",
      new_prompt: "New prompt",
      clear: "Clear",
      print: "Print your page",
      done: "Done",
      print_footer: "less scrolling, more creating.",
      cookie_body: "We use a few cookies to remember your cart and, if you say yes, to understand what's working.",
      cookie_accept: "Accept",
      cookie_decline: "Only essential",
      cookie_policy: "Cookie Policy",
    },
    es: {
      fab: "Dibuja en esta página",
      hero_kicker: "LOS MÁRGENES SON TUYOS",
      hero_title: "Toda esta página es un margen.",
      hero_body: "Cada libro de Maybewell empieza con un espacio en blanco y una buena consigna. Prueba una — aquí mismo, encima de todo.",
      hero_btn: "Toma el lápiz",
      credit: function (b, p) { return "— de " + b + ", página " + p; },
      more: function (n) { return "Hay " + n + " páginas más como esta. En papel."; },
      get_book: "Ver el libro",
      new_prompt: "Otra consigna",
      clear: "Borrar",
      print: "Imprime tu página",
      done: "Listo",
      print_footer: "menos scroll, más crear.",
      cookie_body: "Usamos algunas cookies para recordar tu carrito y, si nos das el visto bueno, para entender qué está funcionando.",
      cookie_accept: "Aceptar",
      cookie_decline: "Solo esenciales",
      cookie_policy: "Política de Cookies",
    },
  };

  function lang() {
    var btn = document.querySelector(".mw-langbtn");
    // the button shows the OTHER language: "ES" means the site is in English
    if (btn && btn.textContent.trim() === "EN") return "es";
    return "en";
  }
  function T() { return STR[lang()]; }

  // ------------------------------------------------------------- styles
  var css = "" +
    ".mwi-fab{position:fixed;right:18px;bottom:18px;z-index:9998;width:54px;height:54px;border-radius:50%;background:" + PUTTY + ";border:2px solid " + INK + ";cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:2px 3px 0 rgba(32,48,58,.25);transition:transform .15s}" +
    ".mwi-fab:hover{transform:rotate(-8deg) scale(1.06)}" +
    ".mwi-fab[aria-pressed=true]{background:" + OCHRE + "}" +
    ".mwi-fab.mwi-shifted{transition:bottom .2s ease;bottom:92px}" +
    ".mwi-canvas{position:fixed;inset:0;z-index:9990;touch-action:none;cursor:crosshair;display:none}" +
    ".mwi-canvas.on{display:block}" +
    ".mwi-bar{position:fixed;top:12px;left:50%;transform:translateX(-50%);z-index:9995;background:" + PUTTY + ";border:2px solid " + INK + ";border-radius:14px;padding:12px 16px;max-width:min(560px,94vw);box-shadow:3px 4px 0 rgba(32,48,58,.22);display:none;font-family:inherit}" +
    ".mwi-bar.on{display:block}" +
    ".mwi-prompt{font-size:16px;font-weight:700;color:" + INK + ";line-height:1.35;margin:0 0 2px}" +
    ".mwi-credit{font-size:11.5px;font-style:italic;color:" + INK + ";opacity:.75;margin:0 0 8px}" +
    ".mwi-cta{font-size:12.5px;color:" + INK + ";margin:0 0 10px}" +
    ".mwi-cta button{margin-left:8px;background:" + OCHRE + ";border:none;border-radius:999px;padding:4px 12px;font-weight:800;font-size:12px;color:" + INK + ";cursor:pointer}" +
    ".mwi-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap}" +
    ".mwi-sw{width:22px;height:22px;border-radius:50%;border:2px solid transparent;cursor:pointer;padding:0}" +
    ".mwi-sw.sel{outline:2px solid " + INK + ";outline-offset:2px}" +
    ".mwi-btn{background:none;border:1.5px solid " + INK + ";border-radius:999px;padding:4px 12px;font-size:12px;font-weight:700;color:" + INK + ";cursor:pointer}" +
    ".mwi-btn:hover{background:rgba(32,48,58,.08)}" +
    ".mwi-hero{border:2px solid " + INK + ";border-radius:16px;background:" + PUTTY + ";padding:26px 24px;box-shadow:4px 5px 0 rgba(32,48,58,.2);max-width:420px}" +
    ".mwi-hero .k{font-size:11px;font-weight:800;letter-spacing:.18em;color:" + INK + ";opacity:.8;margin:0 0 10px}" +
    ".mwi-hero h3{font-size:24px;margin:0 0 10px;color:" + INK + ";line-height:1.15}" +
    ".mwi-hero p{font-size:14px;color:" + INK + ";line-height:1.5;margin:0 0 16px}" +
    ".mwi-hero button{background:" + OCHRE + ";border:2px solid " + INK + ";border-radius:999px;padding:9px 18px;font-weight:800;font-size:14px;color:" + INK + ";cursor:pointer;box-shadow:2px 2px 0 rgba(32,48,58,.3)}" +
    ".mwi-hero button:hover{transform:translate(-1px,-1px);box-shadow:3px 3px 0 rgba(32,48,58,.3)}" +
    // --- "My library" as a bookshelf. Restyles the bundle's .mw-libgrid /
    //     .mw-librow (a row list) into books standing on wooden shelves.
    //     Scoped under .mw-root so it beats the bundle's single-class rules;
    //     !important only where the bundle sets inline styles (cover width).
    ".mw-root .mw-libgrid{display:grid!important;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));grid-auto-rows:262px;align-items:start;justify-items:center;gap:0!important;margin-top:26px;padding:8px 14px 0;" +
      "background:repeating-linear-gradient(to bottom,transparent 0,transparent 170px," + WOOD + " 170px," + WOOD + " 179px," + WOOD_D + " 179px," + WOOD_D + " 184px,transparent 184px,transparent 262px)}" +
    ".mw-root .mw-librow{flex-direction:column!important;align-items:center;justify-content:flex-start;gap:0;background:transparent!important;border:none!important;box-shadow:none!important;padding:0 8px!important;height:100%;text-align:center;transition:transform .16s ease}" +
    ".mw-root .mw-librow:hover{transform:translateY(-6px);z-index:5}" +
    // --- 3D book (ported from a React/Tailwind <Book> component to vanilla
    //     CSS: this site has no build tooling). The bundle's .mw-cover is the
    //     front face; ::before is the back cover pushed back by --d, ::after
    //     is the page block rotated 90deg on the right edge, and the spine
    //     shading is a gradient in .mw-cover's 9% padding. Library only.
    //     NOTE: no `filter` on the 3D ancestors — it flattens preserve-3d.
    ".mw-root .mw-librow>div:first-child{width:120px!important;perspective:900px;filter:none!important}" +
    ".mw-root .mw-librow .mw-cover{--d:13px;--w:120px;position:relative;transform-style:preserve-3d;" +
      "transition:transform .5s cubic-bezier(.2,.8,.25,1);border-radius:2px 5px 5px 2px;" +
      "box-shadow:0 10px 16px -9px rgba(32,48,58,.5);" +
      "background-image:linear-gradient(to right,rgba(32,48,58,.22) 0,rgba(32,48,58,.12) 4.5%,rgba(32,48,58,.05) 7%,rgba(255,255,255,.4) 8.4%,rgba(255,255,255,0) 10%)!important}" +
    ".mw-root .mw-librow:hover .mw-cover{transform:rotateY(-20deg) scale(1.055) translateX(-6px)}" +
    ".mw-root .mw-librow .mw-cover::before{content:\"\";position:absolute;inset:0;background:#E6DDCE;" +
      "border-radius:2px 5px 5px 2px;box-shadow:0 0 0 1px rgba(32,48,58,.16);transform:translateZ(calc(-1*var(--d)))}" +
    ".mw-root .mw-librow .mw-cover::after{content:\"\";position:absolute;top:3px;left:0;width:calc(var(--d) - 2px);height:calc(100% - 6px);" +
      "background:repeating-linear-gradient(to right,#FDFAF4 0 1.5px,#DFD7C9 1.5px 2.5px);" +
      "transform:translateX(calc(var(--w) - var(--d)/2 - 3px)) rotateY(90deg) translateX(calc(var(--d)/2))}" +
    // cover interior rescaled for the 120px shelf book (the bundle sizes these
    // for full-size product covers). Title size is finished by fitSmallCovers().
    ".mw-root .mw-librow .mw-cover-frame{gap:5px!important;padding:9% 8%!important}" +
    // NEVER break mid-word (that reads worse than overflow: "Grandpar-ents'").
    // Lines break at spaces/hyphens only; fitSmallCovers() shrinks the size
    // until the longest whole word fits. .mwi-break is the last-resort escape
    // hatch it adds for a pathological single long word at the minimum size.
    ".mw-root .mw-librow .mw-cover-title,.mw-root .mw-cartrow .mw-cover-title{font-size:12px!important;line-height:1.14!important;overflow-wrap:normal;hyphens:manual;max-width:100%}" +
    ".mw-root .mw-librow .mw-cover-title.mwi-break,.mw-root .mw-cartrow .mw-cover-title.mwi-break{overflow-wrap:anywhere}" +
    ".mw-root .mw-librow .mw-cover-brand,.mw-root .mw-librow .mw-cover-cat{font-size:5.5px!important;letter-spacing:1.1px!important}" +
    ".mw-root .mw-librow .mw-cover-rule{width:22px!important;height:1.5px!important}" +
    ".mw-root .mw-librow .mw-cover-frame>svg{width:11px!important;height:11px!important}" +
    // The cart's thumbnail (56px — less than half the shelf book) has no
    // room for the brand watermark / category label / star at any legible
    // size, so those are hidden rather than shrunk to unreadable — same
    // pattern any e-commerce cart line-item thumbnail uses (image + border,
    // no repeated label text). Only the title (auto-fit) and accent border
    // survive at this size.
    ".mw-root .mw-cartrow .mw-cover{padding:7%!important}" +
    ".mw-root .mw-cartrow .mw-cover-frame{gap:2px!important;padding:8% 5%!important}" +
    ".mw-root .mw-cartrow .mw-cover-brand,.mw-root .mw-cartrow .mw-cover-cat,.mw-root .mw-cartrow .mw-cover-frame>svg,.mw-root .mw-cartrow .mw-cover-rule{display:none!important}" +
    ".mw-root .mw-libinfo{flex:none!important;display:flex;flex-direction:column;align-items:center;gap:2px;max-width:150px;margin-top:24px}" +
    ".mw-root .mw-libinfo .mw-cardtitle{font-size:13.5px!important;line-height:1.25;text-align:center}" +
    ".mw-root .mw-libinfo .mw-dim{font-size:11px!important;opacity:.6}" +
    ".mw-root .mw-librow .mw-btn-sm{margin-top:8px!important;opacity:0;transform:translateY(4px);transition:opacity .15s,transform .15s;font-size:12px!important;padding:4px 12px!important}" +
    ".mw-root .mw-librow:hover .mw-btn-sm,.mw-root .mw-librow:focus-within .mw-btn-sm{opacity:1;transform:none}" +
    // empty state as an empty wooden shelf (copy already says "on the shelf")
    ".mw-root .mw-empty{border:none!important;background:repeating-linear-gradient(to bottom,transparent 0,transparent 82px," + WOOD + " 82px," + WOOD + " 91px," + WOOD_D + " 91px," + WOOD_D + " 96px,transparent 96px,transparent 130px);min-height:130px;padding-top:24px!important}" +
    "@media(max-width:560px){.mw-root .mw-libgrid{grid-template-columns:repeat(auto-fill,minmax(116px,1fr));grid-auto-rows:222px;background:repeating-linear-gradient(to bottom,transparent 0,transparent 138px," + WOOD + " 138px," + WOOD + " 146px," + WOOD_D + " 146px," + WOOD_D + " 150px,transparent 150px,transparent 222px)}.mw-root .mw-librow>div:first-child{width:96px!important}.mw-root .mw-librow .mw-cover{--w:96px;--d:10px}.mw-root .mw-libinfo{margin-top:20px}}" +
    // --- cookie consent banner
    ".mwi-cookie{position:fixed;left:0;right:0;bottom:0;z-index:9997;background:" + INK + ";color:" + PUTTY + ";" +
      "padding:16px 18px;display:none;box-shadow:0 -2px 12px rgba(0,0,0,.25);font-family:inherit}" +
    ".mwi-cookie.on{display:block}" +
    ".mwi-cookie-inner{max-width:900px;margin:0 auto;display:flex;align-items:center;gap:18px;flex-wrap:wrap}" +
    ".mwi-cookie-text{flex:1;min-width:220px;font-size:13px;line-height:1.45}" +
    ".mwi-cookie-text a{color:" + PUTTY + ";text-decoration:underline}" +
    ".mwi-cookie-row{display:flex;gap:10px;flex-wrap:wrap}" +
    ".mwi-cookie-row button{border-radius:999px;padding:8px 16px;font-size:13px;font-weight:800;cursor:pointer;white-space:nowrap}" +
    ".mwi-cookie-accept{background:" + OCHRE + ";border:2px solid " + OCHRE + ";color:" + INK + "}" +
    ".mwi-cookie-decline{background:transparent;border:1.5px solid " + PUTTY + ";color:" + PUTTY + "}" +
    "@media print{.mwi-fab,.mwi-bar,.mwi-cookie{display:none!important}}";

  var styleEl = document.createElement("style");
  styleEl.id = "mwi-css";
  styleEl.textContent = css;
  document.head.appendChild(styleEl);

  // ------------------------------------------------------- margins mode
  var state = {
    on: false,
    color: INK,
    promptIdx: Math.floor(Math.random() * PROMPTS.length),
    drew: false,
  };

  var canvas = document.createElement("canvas");
  canvas.className = "mwi-canvas";
  canvas.setAttribute("aria-label", "drawing overlay");
  document.body.appendChild(canvas);

  function sizeCanvas() {
    var dpr = window.devicePixelRatio || 1;
    var w = window.innerWidth, h = window.innerHeight;
    if (canvas.width === Math.round(w * dpr) && canvas.height === Math.round(h * dpr)) return;
    // preserve existing drawing through resizes
    var keep = null;
    if (state.drew) {
      keep = document.createElement("canvas");
      keep.width = canvas.width; keep.height = canvas.height;
      keep.getContext("2d").drawImage(canvas, 0, 0);
    }
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    var ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    if (keep) ctx.drawImage(keep, 0, 0, keep.width, keep.height, 0, 0, w, h);
  }

  var drawing = false, last = null;
  function pos(ev) {
    var r = canvas.getBoundingClientRect();
    return { x: ev.clientX - r.left, y: ev.clientY - r.top };
  }
  canvas.addEventListener("pointerdown", function (ev) {
    drawing = true; last = pos(ev);
    canvas.setPointerCapture(ev.pointerId);
  });
  canvas.addEventListener("pointermove", function (ev) {
    if (!drawing) return;
    var ctx = canvas.getContext("2d");
    var p = pos(ev);
    ctx.strokeStyle = state.color;
    ctx.lineWidth = 4;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.shadowColor = state.color;
    ctx.shadowBlur = 2;
    ctx.globalAlpha = 0.95;
    ctx.beginPath();
    ctx.moveTo(last.x, last.y);
    ctx.lineTo(p.x, p.y);
    ctx.stroke();
    last = p;
    state.drew = true;
  });
  function stopDraw() { drawing = false; }
  canvas.addEventListener("pointerup", stopDraw);
  canvas.addEventListener("pointerleave", stopDraw);

  // toolbar
  var bar = document.createElement("div");
  bar.className = "mwi-bar";
  document.body.appendChild(bar);

  function renderBar() {
    var t = T();
    var pr = PROMPTS[state.promptIdx];
    var book = BOOKS[pr.b];
    bar.innerHTML = "";

    var pEl = document.createElement("p");
    pEl.className = "mwi-prompt";
    pEl.textContent = pr.t;
    bar.appendChild(pEl);

    var cEl = document.createElement("p");
    cEl.className = "mwi-credit";
    cEl.textContent = t.credit(book.name, pr.p);
    bar.appendChild(cEl);

    var cta = document.createElement("p");
    cta.className = "mwi-cta";
    cta.textContent = t.more(book.pages);
    var go = document.createElement("button");
    go.textContent = t.get_book + " →";
    go.addEventListener("click", function () { setMode(false); goToProduct(pr.b); });
    cta.appendChild(go);
    bar.appendChild(cta);

    var row = document.createElement("div");
    row.className = "mwi-row";
    SWATCHES.forEach(function (col) {
      var sw = document.createElement("button");
      sw.className = "mwi-sw" + (state.color === col ? " sel" : "");
      sw.style.background = col;
      sw.setAttribute("aria-label", "color " + col);
      sw.addEventListener("click", function () { state.color = col; renderBar(); });
      row.appendChild(sw);
    });
    [[t.new_prompt, nextPrompt], [t.clear, clearCanvas], [t.print, printPage], [t.done, function () { setMode(false); }]]
      .forEach(function (pair) {
        var b = document.createElement("button");
        b.className = "mwi-btn";
        b.textContent = pair[0];
        b.addEventListener("click", pair[1]);
        row.appendChild(b);
      });
    bar.appendChild(row);
  }

  function nextPrompt() {
    state.promptIdx = (state.promptIdx + 1) % PROMPTS.length;
    renderBar();
  }
  function clearCanvas() {
    var ctx = canvas.getContext("2d");
    ctx.save();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.restore();
    state.drew = false;
  }

  var savedOverflow = "";
  function setMode(on) {
    state.on = on;
    if (on) sizeCanvas();
    canvas.classList.toggle("on", on);
    bar.classList.toggle("on", on);
    fab.setAttribute("aria-pressed", on ? "true" : "false");
    if (on) {
      renderBar();
      savedOverflow = document.body.style.overflow;
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = savedOverflow;
    }
  }

  // print: a clean "page of the book" — the prompt + the visitor's drawing,
  // laid out like a Maybewell page, via a hidden iframe (no popups).
  function printPage() {
    var t = T();
    var pr = PROMPTS[state.promptIdx];
    var book = BOOKS[pr.b];
    var img = canvas.toDataURL("image/png");
    var html =
      "<!doctype html><html><head><meta charset='utf-8'><title>Maybewell Books</title>" +
      "<style>@page{margin:14mm}body{font-family:Georgia,serif;background:" + PUTTY + ";color:" + INK + ";margin:0;padding:28px}" +
      ".wm{font-family:Arial,sans-serif;font-weight:800;letter-spacing:.35em;font-size:12px;text-align:center;margin-bottom:34px}" +
      ".pr{font-size:22px;font-weight:700;line-height:1.35;max-width:620px;margin:0 auto 6px;text-align:center}" +
      ".cr{font-style:italic;font-size:12px;text-align:center;opacity:.75;margin-bottom:18px}" +
      "img{display:block;margin:0 auto;max-width:100%;border:1px dashed " + INK + ";border-radius:8px}" +
      ".ft{font-family:Arial,sans-serif;font-size:11px;text-align:center;margin-top:26px;opacity:.8}</style></head><body>" +
      "<div class='wm'>M A Y B E W E L L &nbsp; B O O K S</div>" +
      "<div class='pr'></div><div class='cr'></div>" +
      "<img alt='your drawing'>" +
      "<div class='ft'>maybewellbooks.com &middot; " + t.print_footer + "</div>" +
      "</body></html>";
    var frame = document.createElement("iframe");
    frame.style.position = "fixed";
    frame.style.right = "0";
    frame.style.bottom = "0";
    frame.style.width = "0";
    frame.style.height = "0";
    frame.style.border = "0";
    document.body.appendChild(frame);
    var doc = frame.contentDocument;
    doc.open(); doc.write(html); doc.close();
    doc.querySelector(".pr").textContent = pr.t;
    doc.querySelector(".cr").textContent = t.credit(book.name, pr.p);
    var image = doc.querySelector("img");
    image.onload = function () {
      frame.contentWindow.focus();
      frame.contentWindow.print();
      setTimeout(function () { frame.remove(); }, 4000);
    };
    image.src = img;
  }

  function goToProduct(id) {
    function scrollToIt() {
      var el = document.getElementById(id);
      if (!el) return false;
      el.scrollIntoView({ behavior: "smooth", block: "center" });
      el.style.transition = "box-shadow .4s";
      el.style.boxShadow = "0 0 0 4px " + OCHRE;
      setTimeout(function () { el.style.boxShadow = ""; }, 1800);
      return true;
    }
    if (scrollToIt()) return;
    // navigate the SPA to the shop page (first nav link), then find the card
    var nav = document.querySelector(".mw-navlinks");
    if (nav && nav.children[0]) nav.children[0].querySelector("button, a")
      ? nav.children[0].querySelector("button, a").click()
      : nav.children[0].click();
    var tries = 0;
    var iv = setInterval(function () {
      tries += 1;
      if (scrollToIt() || tries > 30) clearInterval(iv);
    }, 100);
  }

  // pencil FAB
  var fab = document.createElement("button");
  fab.className = "mwi-fab";
  fab.setAttribute("aria-pressed", "false");
  fab.innerHTML =
    '<svg width="26" height="26" viewBox="0 0 24 24" fill="none">' +
    '<path d="M4 20l1.2-4.2L16.4 4.6a1.8 1.8 0 0 1 2.6 0l.4.4a1.8 1.8 0 0 1 0 2.6L8.2 18.8 4 20z" stroke="' + INK + '" stroke-width="1.8" stroke-linejoin="round" fill="' + PUTTY + '"/>' +
    '<path d="M14.8 6.2l3 3" stroke="' + INK + '" stroke-width="1.8"/>' +
    '<path d="M5.2 15.8l3 3" stroke="' + INK + '" stroke-width="1.8"/></svg>';
  document.body.appendChild(fab);
  fab.addEventListener("click", function () { setMode(!state.on); });
  function syncFabLabel() { fab.setAttribute("aria-label", T().fab); fab.title = T().fab; }
  syncFabLabel();

  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape" && state.on) setMode(false);
  });
  window.addEventListener("resize", function () { if (state.on) sizeCanvas(); });

  // -------------------------------------------- hero invitation (mounts
  // into the .mw-hero-r column the bundle now renders empty)
  // --------------------------------------------- auto-fit small cover titles
  // The bundle hardcodes fontSize:19px inline on .mw-cover-title (sized for
  // full-page product covers). Any SMALL rendering of that same cover
  // overflows: the library's 120px shelf book (both ways — horizontally on
  // unbreakable words like "Grandparents'", vertically on long titles like
  // "Build Without Words — Weekly Module") and the cart's 56px line-item
  // thumbnail (worse — spills the title across the whole cart row, see the
  // bug report this was fixed from). Rather than pick one small size (which
  // would shrink short titles needlessly, or still overflow the smallest
  // context), measure each cover and step the size down until it fits both
  // axes — so any future title, at any small size, fits too. Inline +
  // "important" is required: it must beat both React's inline size and the
  // stylesheet fallback above.
  var FIT_MAX = 15, FIT_MIN = 8, FIT_STEP = 0.5;

  function fitSmallCovers() {
    var frames = document.querySelectorAll(".mw-librow .mw-cover-frame, .mw-cartrow .mw-cover-frame");
    for (var i = 0; i < frames.length; i++) {
      var frame = frames[i];
      var title = frame.querySelector(".mw-cover-title");
      if (!title) continue;
      var size = FIT_MAX;
      title.classList.remove("mwi-break");
      title.style.setProperty("font-size", size + "px", "important");
      var guard = 0;
      var overflows = function () {
        // width: the longest unbroken word sticking out. height: too many lines.
        return title.scrollWidth > title.clientWidth + 1 ||
               frame.scrollHeight > frame.clientHeight + 1;
      };
      while (guard++ < 40 && size > FIT_MIN && overflows()) {
        size -= FIT_STEP;
        title.style.setProperty("font-size", size + "px", "important");
      }
      // Only if a single word still can't fit at the smallest size do we allow
      // breaking inside it — better a broken word than text spilling off a book.
      if (overflows()) title.classList.add("mwi-break");
    }
  }

  var heroRenderedLang = null;
  function renderHeroCard() {
    var slot = document.querySelector(".mw-hero-r");
    if (!slot) { heroRenderedLang = null; return; }
    var card = slot.querySelector(".mwi-hero");
    // guard: re-rendering mutates #root, which the MutationObserver watches —
    // only touch the DOM when the card is missing or the language changed.
    if (card && heroRenderedLang === lang()) return;
    heroRenderedLang = lang();
    var t = T();
    if (!card) {
      card = document.createElement("div");
      card.className = "mwi-hero";
      slot.appendChild(card);
    }
    card.innerHTML = "";
    var k = document.createElement("p"); k.className = "k"; k.textContent = t.hero_kicker;
    var h = document.createElement("h3"); h.textContent = t.hero_title;
    var p = document.createElement("p"); p.textContent = t.hero_body;
    var b = document.createElement("button"); b.textContent = t.hero_btn + " ✎";
    b.addEventListener("click", function () { setMode(true); });
    card.appendChild(k); card.appendChild(h); card.appendChild(p); card.appendChild(b);
  }

  // ------------------------------------------------------- cookie consent
  // No analytics/tracking is wired in yet (see PROJECT_STATUS.md) — the
  // site only ever sets functional cookies (cart/session). This banner and
  // window.mwConsent() exist so that WHEN analytics is added, it's built to
  // check consent from day one instead of retrofitting compliance later.
  var COOKIE_KEY = "mw-cookie-consent"; // localStorage: "accepted" | "declined"

  window.mwConsent = function () {
    try { return localStorage.getItem(COOKIE_KEY) === "accepted"; }
    catch (e) { return false; } // no storage access => safest default is no
  };

  var cookieBanner = document.createElement("div");
  cookieBanner.className = "mwi-cookie";
  document.body.appendChild(cookieBanner);

  function setCookieChoice(value) {
    try { localStorage.setItem(COOKIE_KEY, value); } catch (e) {}
    cookieBanner.classList.remove("on");
    fab.classList.remove("mwi-shifted");
    if (value === "accepted" && window.mwLoadAnalytics) window.mwLoadAnalytics();
  }

  var cookieRenderedLang = null;
  function renderCookieBanner() {
    var decided = false;
    try { decided = !!localStorage.getItem(COOKIE_KEY); } catch (e) {}
    if (decided) { cookieBanner.classList.remove("on"); fab.classList.remove("mwi-shifted"); return; }
    if (cookieRenderedLang === lang()) { cookieBanner.classList.add("on"); fab.classList.add("mwi-shifted"); return; }
    cookieRenderedLang = lang();
    var t = T();
    cookieBanner.innerHTML = "";
    var inner = document.createElement("div");
    inner.className = "mwi-cookie-inner";
    var text = document.createElement("div");
    text.className = "mwi-cookie-text";
    text.textContent = t.cookie_body + " ";
    var link = document.createElement("a");
    link.href = "/cookies";
    link.textContent = t.cookie_policy;
    text.appendChild(link);
    var row = document.createElement("div");
    row.className = "mwi-cookie-row";
    var decline = document.createElement("button");
    decline.className = "mwi-cookie-decline";
    decline.textContent = t.cookie_decline;
    decline.addEventListener("click", function () { setCookieChoice("declined"); });
    var accept = document.createElement("button");
    accept.className = "mwi-cookie-accept";
    accept.textContent = t.cookie_accept;
    accept.addEventListener("click", function () { setCookieChoice("accepted"); });
    row.appendChild(decline);
    row.appendChild(accept);
    inner.appendChild(text);
    inner.appendChild(row);
    cookieBanner.appendChild(inner);
    cookieBanner.classList.add("on");
    fab.classList.add("mwi-shifted");
  }

  // --------------------------------------------------- watch the SPA/lang
  var lastLang = null;
  function refreshAll() {
    var l = lang();
    var langChanged = l !== lastLang;
    lastLang = l;
    if (langChanged) {
      syncFabLabel();
      if (state.on) renderBar();
      cookieRenderedLang = null;
    }
    renderHeroCard();     // internally guarded, only mutates when needed
    fitSmallCovers();     // no-op unless a library shelf or cart row is on screen
    renderCookieBanner(); // internally guarded, only mutates when needed
  }
  // Only childList/characterData — NOT attributes, so fitSmallCovers()
  // writing inline styles can never retrigger this observer.
  var mo = new MutationObserver(function () { refreshAll(); });
  window.addEventListener("resize", fitSmallCovers);

  function boot() {
    var root = document.getElementById("root");
    if (!root || !document.querySelector(".mw-root")) {
      setTimeout(boot, 120);
      return;
    }
    refreshAll();
    mo.observe(root, { childList: true, subtree: true, characterData: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
