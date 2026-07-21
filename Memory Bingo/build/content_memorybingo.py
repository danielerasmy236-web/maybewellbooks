"""All written content for Memory Bingo (Bingo de Memoria).

For Every Chapter line. Template H: facilitator rules block + repeatable
bingo cards. Life-experience phrases instead of numbers — every marked
square is a storytelling prompt. 4x4 cards (bigger squares than 5x5, per
the line's large-print/viewing-distance standard), 10 unique layouts drawn
deterministically from a 40-phrase caller list.
"""

CFG = {
    "EYEBROW": "FOR EVERY CHAPTER · A GROUP GAME",
    "TITLE_LINES": ["Memory", "Bingo"],
    "SUBTITLE": "Bingo Where Every Square Is a Life Actually Lived",
    "SPANISH_NOTE": "Bingo de Memoria",
    "BADGE": "A LARGE-PRINT GAME",
    "TAGLINE": "everyone in this room has lived a life.",
}

INTRO_KICKER = "FOR THE FACILITATOR"
INTRO_TITLE = "How to Run a Game"
INTRO_PARAS = [
    "It's bingo — but instead of numbers, the squares are things people "
    "have actually lived. When a square gets marked, there's a story "
    "attached. That's the whole trick.",
    ("SETUP", "4 to 16 players, one card each (there are ten different "
     "cards — photocopy freely). Pencils or big markers. 30-45 minutes."),
    ("CALL", "Read phrases from the caller list in any order, big and "
     "slow, twice each. Cross them off the list as you go."),
    ("MARK", "Players mark a square if it's true of THEM. On the honor "
     "system — and the honor system is where the stories come from."),
    ("TELL", "Every few calls, pick someone who just marked a square: "
     "\"Tell us about that.\" One sentence or five minutes, both fine."),
    ("WIN", "Four in a row, any direction, wins the round. Play again — "
     "cards stay interesting because the stories change."),
    "Prizes are optional and honestly unnecessary. The winning move is "
    "asking the quietest person in the room about the square everyone "
    "was surprised they marked.",
]

# The caller list — 40 life-experience phrases. Dignified, story-bearing,
# and broad enough that every card gives everyone a real shot.
PHRASES = [
    "Had a part-time job before age 16",
    "Danced at a wedding this year",
    "Remembers a phone number by heart",
    "Learned to drive on a manual transmission",
    "Grew up with a party-line telephone",
    "Has been mentioned in a newspaper",
    "Kept a handwritten diary",
    "Met someone famous",
    "Owned a record player",
    "Still writes letters by hand",
    "Grew vegetables they later ate",
    "Can name their first teacher",
    "Was the oldest sibling",
    "Has slept under the stars",
    "Moved to a new city alone",
    "Wore a uniform to work",
    "Has won a trophy or ribbon",
    "Baked bread from scratch",
    "Remembers their childhood address",
    "Has ridden a train overnight",
    "Sang in a choir",
    "Learned to swim in a lake or river",
    "Had milk delivered to the door",
    "Mended their own clothes",
    "Has been to a drive-in movie",
    "Kept the same best friend for 20+ years",
    "Played a musical instrument",
    "Watched the Moon landing live",
    "Has held a newborn grandchild",
    "Built something with their own hands",
    "Speaks more than one language",
    "Had a nickname that stuck",
    "Once stayed up all night talking",
    "Has voted in more than ten elections",
    "Taught someone a family recipe",
    "Remembers life before television",
    "Wore out a favorite pair of dancing shoes",
    "Wrote a love letter",
    "Has forgiven someone for something big",
    "Still has a photo in their wallet",
]

assert len(PHRASES) == 40

CARD_COUNT = 10
CARD_SEED = 20260720   # deterministic layouts: same book, same cards, always

CLOSING_TITLE = "Nobody's card was empty."
CLOSING_BODY = "That was the point all along."
CLOSING_STATS = "40 phrases  ·  10 cards  ·  4 in a row wins  ·"
