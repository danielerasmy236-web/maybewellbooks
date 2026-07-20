"""All written content for The Map You Draw (El Mapa que Tú Dibujas).

Field Notes line, Volume Three. Template B variant: no sections, no dividers —
one continuous personal atlas. Each atlas page carries a single marginalia
prompt ("MARK") above a large blank map canvas the reader fills in over
repeat visits. This book is personal geography, not literal geography: there
is no correct map, no scale, no north.
"""

TITLE = "The Map\nYou Draw"
TITLE_LINES = ["The Map", "You Draw"]
SUBTITLE = "A Personal Atlas of Everywhere You Actually Go"
TAGLINE = "it only has to make sense to you."
EYEBROW = "FIELD NOTES · VOLUME THREE"
BADGE = "A CARTOGRAPHY BOOK"
HASHTAG = "#TheMapYouDraw"
SPANISH_NOTE = "El Mapa que Tú Dibujas"

INTRO_TITLE = "Before You Begin"
INTRO_KICKER = "HOW TO MAP IT"
INTRO_PARAS = [
    "Forget scale. Forget north. This isn't the map a satellite would draw — "
    "it's the one only you could draw, built from memory, habit, and the "
    "hundred small decisions that make a neighborhood yours instead of "
    "anyone else's.",
    "This book works in one move, repeated:",
    ("MARK", "Each page gives you one thing to place on your map — a "
     "feeling, a memory, a fact only you'd know. Draw roads, buildings, "
     "landmarks, or just a shape and a label. There's no wrong way to draw "
     "a street you've never measured."),
    "You don't have to fill a page in one sitting. This book is built to be "
    "carried, opened, and added to over weeks or months — a mark today, "
    "another next time you think of it. Some pages might connect to each "
    "other. Some won't. Both are fine.",
    "There is no correct version of your neighborhood. There's only the one "
    "you carry around in your head — half memory, half habit. This book is "
    "just where you finally put it down on paper.",
    "Start anywhere. Draw slowly. It only has to make sense to you.",
]

CLOSING_TITLE = "The map is never finished."
CLOSING_BODY = "Neither is the neighborhood. Keep adding to it."
CLOSING_STATS = "36 marks  ·  one continuous atlas  ·"
CLOSING_SHARE = "Share your atlas: " + HASHTAG

# One flat list of 36 marginalia prompts — no sections, no chapters.
MARKS = [
    "Mark the place that smells the best on your street.",
    "Mark somewhere you've walked past a hundred times but never entered.",
    "Mark where you'd hide if you were eight years old again.",
    "Mark the loudest spot within five minutes of home.",
    "Mark the quietest spot within five minutes of home.",
    "Mark a place that belongs to someone else's memory, not yours.",
    "Mark the spot where you always run into someone you know.",
    "Mark somewhere that looks completely different at night.",
    "Mark the shortest way somewhere, even if you never take it.",
    "Mark the longest way somewhere — the one you take on purpose.",
    "Mark a place you've never seen anyone else visit.",
    "Mark somewhere you'd take a visitor first.",
    "Mark somewhere you'd never take a visitor.",
    "Mark a place that changed since you last paid attention to it.",
    "Mark somewhere you associate with one specific season.",
    "Mark the place you go when you need to think.",
    "Mark a spot that's disappeared — torn down, closed, gone.",
    "Mark somewhere you've cried, even a little.",
    "Mark a place you've only ever passed through, never stopped.",
    "Mark somewhere that smells like a memory you can't quite place.",
    "Mark a spot with the best light in the late afternoon.",
    "Mark somewhere a stranger once did something kind.",
    "Mark a place you'd go if you had exactly one free hour.",
    "Mark a corner that still scares you a little, even now.",
    "Mark somewhere you've celebrated something.",
    "Mark a place you pass constantly but have never actually looked at.",
    "Mark somewhere you'd go to be found, if you were lost.",
    "Mark a spot you associate with a sound, not a sight.",
    "Mark somewhere that belongs entirely to your childhood.",
    "Mark a place you discovered completely by accident.",
    "Mark somewhere you go on purpose to be alone.",
    "Mark a spot where the ground tells a story — a crack, a root, a step worn smooth.",
    "Mark somewhere you'd bury a time capsule.",
    "Mark a place that only exists at a certain time of day.",
    "Mark somewhere you've never been, but can see from where you live.",
    "Mark the edge of your map — the place you consider \"away.\"",
]

assert len(MARKS) == 36, "prompt count must be exactly 36"
