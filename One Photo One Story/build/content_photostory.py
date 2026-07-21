"""All written content for One Photo, One Story (Una Foto, Una Historia).

For Every Chapter line. Template F adapted for photo-anchoring: ~30
repeating card pages, each with a marked photo-mounting area, four anchor
prompts, one rotating deeper prompt, and a large-print writing area.
"""

CFG = {
    "EYEBROW": "FOR EVERY CHAPTER · A PHOTO KEEPSAKE BOOK",
    "TITLE_LINES": ["One Photo,", "One Story"],
    "SUBTITLE": "The Stories Behind the Photographs You Already Have",
    "SPANISH_NOTE": "Una Foto, Una Historia",
    "BADGE": "A LARGE-PRINT BOOK",
    "TAGLINE": "every photo is holding a story.",
}

INTRO_KICKER = "HOW TO USE THIS"
INTRO_TITLE = "Choosing the Photos"
INTRO_PARAS = [
    "Somewhere in your home there is a box, a drawer, or an album of "
    "photographs that nobody has asked about in years. This book is how "
    "you answer them anyway.",
    "Pick a photo. Tape or glue it to the marked space. Then write the "
    "story around it — who is in it, when it was, and what the camera "
    "didn't catch.",
    ("CHOOSE", "Photos with people in them beat photos of scenery. Blurry "
     "is fine. The photo you almost skip is usually the one with the best "
     "story in it."),
    ("MOUNT", "Any tape or glue stick works. Photo corners work too, if "
     "you have them — the printed guides show you where."),
    ("WRITE", "Answer the printed questions first. They will pull the rest "
     "of the story out on their own."),
    "Thirty photos is enough for a lifetime, or just one summer. Either "
    "way, when it's full, it isn't a photo box anymore — it's a book "
    "someone will keep.",
]

# Rotating deeper prompts, cycled across the 30 card pages.
DEEP_PROMPTS = [
    "What sound do you remember from this moment, even if it's not in the photo?",
    "Who's missing from this photo that you wish were there?",
    "What would you tell the person in this photo if you could talk to them now?",
    "What happened to the place in this photo? Does it still exist?",
    "What did that day smell like — food, weather, someone's perfume?",
    "If this photo had a title, like a painting in a museum, what would it be?",
]

CARD_COUNT = 30

CLOSING_TITLE = "Now hand it over."
CLOSING_PARAS = [
    "A finished book like this is not for a shelf. Give it to the person "
    "who will ask you about page four. Read it out loud at a holiday. "
    "Let a grandchild flip through it and interrupt you.",
    "The photos already survived this long. Now the stories will too.",
]
CLOSING_STATS = "30 photos  ·  30 stories  ·"
