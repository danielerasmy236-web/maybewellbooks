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
};

module.exports = { PRODUCTS };
