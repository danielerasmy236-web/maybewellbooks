// Server-side source of truth for what's actually purchasable.
// Prices are in cents. Keep this in sync with the client catalog in
// assets/index-*.js whenever a product's price changes or a new product
// is published (moved from "New Products - Pending Review" to a real file
// in netlify/functions/_assets/).
//
// A product only appears here once its PDF has been reviewed and copied
// into _assets/ — never add an id before the file exists, or a customer
// could pay for something we can't deliver.

const PRODUCTS = {
  dwyi: { name: "Draw What You Imagine", price: 500, file: "draw-what-you-imagine_v1.1_letter.pdf" },
  garden: { name: "The Impossible Garden", price: 500, file: "the-impossible-garden_v1.0_letter.pdf" },
  mazes: { name: "Mazes of the Lost City", price: 400, file: "mazes-of-the-lost-city_v1.0_letter.pdf" },
  twiw: { name: "The World Is Watching", price: 500, file: "the-world-is-watching_v1.0_letter.pdf" },
  // For Teachers & Educators line — singles $2, weekly modules $4
  chain: { name: "Chain Story — Single Sheet", price: 200, file: "chain-story-single-sheet_v1.0_letter.pdf" },
  chainwk: { name: "Chain Story — Weekly Module", price: 400, file: "chain-story-weekly-module_v1.0_letter.pdf" },
  detective: { name: "Group Detective — Single Sheet", price: 200, file: "group-detective-single-sheet_v1.0_letter.pdf" },
  detectivewk: { name: "Group Detective — Weekly Module", price: 400, file: "group-detective-weekly-module_v1.0_letter.pdf" },
  silent: { name: "Build Without Words — Single Sheet", price: 200, file: "build-without-words-single-sheet_v1.0_letter.pdf" },
  silentwk: { name: "Build Without Words — Weekly Module", price: 400, file: "build-without-words-weekly-module_v1.0_letter.pdf" },
};

module.exports = { PRODUCTS };
