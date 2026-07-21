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
  wander: { name: "Wander Without a Destination", price: 500, file: "wander-without-a-destination_v1.0_letter.pdf" },
  map: { name: "The Map You Draw", price: 400, file: "the-map-you-draw_v1.0_letter.pdf" },
  micro: { name: "15-Minute Micro-Adventures", price: 500, file: "15-minute-micro-adventures_v1.0_letter.pdf" },
  questions: { name: "Questions They Never Ask You", price: 400, file: "questions-they-never-ask-you_v1.0_letter.pdf" },
  letter: { name: "Letter to the Future", price: 300, file: "letter-to-the-future_v1.0_letter.pdf" },
  grandparents: { name: "The Grandparents' Book", price: 400, file: "the-grandparents-book_v1.0_letter.pdf" },
  machines: { name: "Machines Nobody's Built Yet", price: 500, file: "machines-nobodys-built-yet_v1.0_letter.pdf" },
  // For Teachers & Educators line — singles $2, weekly modules $4
  chain: { name: "Chain Story — Single Sheet", price: 200, file: "chain-story-single-sheet_v1.0_letter.pdf" },
  chainwk: { name: "Chain Story — Weekly Module", price: 400, file: "chain-story-weekly-module_v1.0_letter.pdf" },
  detective: { name: "Group Detective — Single Sheet", price: 200, file: "group-detective-single-sheet_v1.0_letter.pdf" },
  detectivewk: { name: "Group Detective — Weekly Module", price: 400, file: "group-detective-weekly-module_v1.0_letter.pdf" },
  silent: { name: "Build Without Words — Single Sheet", price: 200, file: "build-without-words-single-sheet_v1.0_letter.pdf" },
  silentwk: { name: "Build Without Words — Weekly Module", price: 400, file: "build-without-words-weekly-module_v1.0_letter.pdf" },
  // PDF-factory catalog (agent-tools/) — published 2026-07-20
  logic: { name: "Little Logic Lab", price: 400, file: "little-logic-lab_v1.0_letter.pdf" },
  stem: { name: "Space STEM Pack", price: 400, file: "space-stem-pack_v1.0_letter.pdf" },
  story: { name: "Story Starters", price: 400, file: "story-starters_v1.0_letter.pdf" },
  words: { name: "Word Search Safari", price: 300, file: "word-search-safari_v1.0_letter.pdf" },
};

module.exports = { PRODUCTS };
