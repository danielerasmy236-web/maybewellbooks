"""All written content for Letter to the Future (Carta al Futuro).

Field Notes line, Volume Six. Template D, correspondence variant: a physical
object meant to be sealed and stored, not scanned. Three sections by time
horizon (1 / 5 / 10 years), each opening with a short reflection-prompt page
before its blank letter pages, plus a closing "Instructions for Storage"
page.
"""

TITLE = "Letter to\nthe Future"
TITLE_LINES = ["Letter to", "the Future"]
SUBTITLE = "A Correspondence Book for Sealing, Storing, and Opening Later"
TAGLINE = "some things are worth waiting for."
EYEBROW = "FIELD NOTES · VOLUME SIX"
BADGE = "A CORRESPONDENCE BOOK"
HASHTAG = "#LetterToTheFuture"
SPANISH_NOTE = "Carta al Futuro"

INTRO_TITLE = "Before You Begin"
INTRO_KICKER = "HOW TO USE THIS"
INTRO_PARAS = [
    "This isn't a journal you'll reread next week. It's built to be sealed "
    "and put away — in a drawer, a box, wherever you keep things you mean "
    "to come back to — and opened on purpose, later, by the person you'll "
    "have become by then.",
    "This book works in three moves:",
    ("REFLECT", "Each section opens with a few questions to sit with before "
     "you write. You don't have to answer them on the page — they're just "
     "there to get you thinking honestly before you start."),
    ("WRITE", "Write the letter itself on the ruled pages that follow. Be as "
     "honest as you'd be with someone you trust completely — because you "
     "are."),
    ("SEAL", "When you're done, fold the section shut, write the open-on "
     "date on the cover line, and store it somewhere you won't stumble on "
     "it by accident. The waiting is part of the gift."),
    "There is no wrong way to write to yourself. Say the true thing, not "
    "the impressive one.",
]

CLOSING_TITLE = "Instructions for Storage"
CLOSING_INTRO = (
    "This book only works if you actually put it away. A few notes before "
    "you do:"
)
CLOSING_POINTS = [
    ("WHERE", "Somewhere physical, not digital — a drawer, a shelf, a box "
     "of things that matter. Somewhere you'll find it by accident in a few "
     "years, not somewhere you'll check every week."),
    ("WHEN", "Mark each section's open-on date somewhere you'll actually "
     "see it again — a calendar reminder works, even if the letter itself "
     "doesn't get opened digitally."),
    ("WHO", "If you forget, or if something happens before you get there, "
     "name someone below who should make sure this book finds its way back "
     "to you — or gets opened with care if it can't."),
]
CLOSING_WHO_LABEL = "If I forget, this book belongs to:"
CLOSING_BODY = "Then put it down. It'll be exactly where you left it."
CLOSING_STATS = "3 letters  ·  1 / 5 / 10 years  ·"
CLOSING_SHARE = "Share when you open one: " + HASHTAG

# (horizon label, years word, reflection prompts, letter page count)
HORIZONS = [
    ("1 Year", "one year",
     [
      "What do you hope has changed about your daily life by the time you read this? What do you hope hasn't?",
      "What's something happening right now that feels bigger than it will probably look in a year?",
      "Write to the version of you who's already forgotten what today actually felt like.",
     ], 5),
    ("5 Years", "five years",
     [
      "What do you hope you've built, learned, or finally let go of by the time you read this?",
      "What's a question about your life you can't answer yet, but might be able to in five years?",
      "Leave a message for the person you're becoming — even the parts you can't picture yet.",
     ], 5),
    ("10 Years", "ten years",
     [
      "What do you hope is still true about you in ten years? What do you hope has changed completely?",
      "Who do you hope is still in your life? Who do you hope you've forgiven, or been forgiven by?",
      "Leave a question for your future self that only they will be able to answer.",
     ], 5),
]
