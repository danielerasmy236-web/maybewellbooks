"""Content data for 'Road Trip Games' (id: tripgames, line: Field Notes).

Field Notes version of the old 'Paper Games for Road Trips' concept, per
the resolved decision in PRODUCT_QUEUE.md (2026-07-20): one merged product
under the Field Notes line, Template H (game rules + scorecard), replacing
the old standalone 'roadtrip' id — do not confuse this with that retired
product (its content/generator files are kept untouched as a historical
record).
"""

TITLE = "Road Trip\nGames"
SUBTITLE = "Eighteen two-player games that only need a pencil and a lap"
TAGLINE = "shotgun picks first."
ACCENT = "TEAL"

INTRO_BODY = [
    "Every game in this book is built for two players, a flat lap, and",
    "one pencil you'll probably have to share.",
    "",
    "No pieces to lose under the seat. No timer except the drive itself.",
    "A few games ask for scissors — we gave you a fold-only way to play",
    "those too, for when scissors aren't an option at 70 miles an hour.",
    "",
    "Score sheets are built into every spread. Play best-of-three.",
    "Loser picks the next game.",
]

# board types: grid, bracket, checklist, dots, foldtemplate, ladder, table, freeform

GAMES = [
    {
        "title": "Dots and Boxes",
        "rules": "Take turns drawing one line between two neighboring dots. Complete the fourth "
                 "side of a box and it's yours — go again. Most boxes when the grid is full wins.",
        "board": ("dots", 6, 6),
    },
    {
        "title": "Tic-Tac-Toe, Best of Five",
        "rules": "Classic rules, five boards in a row. Alternate who goes first each round. "
                 "First player to win three boards takes the match.",
        "board": ("multigrid", 3, 5),
    },
    {
        "title": "Five in a Row",
        "rules": "Take turns marking a square with X or O on the big grid. First to line up five "
                 "in a row — across, down, or diagonal — wins.",
        "board": ("grid", 13, None),
    },
    {
        "title": "Fleet Hunt",
        "rules": "Each player secretly marks 5 ships on their own grid (in the back of the book), "
                 "without showing the other. Call out coordinates to hunt — a hit means go again.",
        "board": ("coordgrid", 10, None),
    },
    {
        "title": "License Plate Bingo",
        "rules": "Cross off a square every time you spot that state or country on a license "
                 "plate. First to five in a row calls 'Bingo' and wins the round.",
        "board": ("bingo", None, None),
    },
    {
        "title": "Hangman Relay",
        "rules": "Player 1 thinks of a word and draws blanks. Player 2 guesses letters — each "
                 "wrong guess adds a piece to the gallows. Swap roles after every word.",
        "board": ("hangman", 6, None),
    },
    {
        "title": "Rock-Paper-Scissors Tournament",
        "rules": "Best of three per round, fill in winners as you climb the bracket. Great for "
                 "settling literally any argument in the car.",
        "board": ("bracket", 8, None),
    },
    {
        "title": "MASH",
        "rules": "Draw a spiral, pick a random number of loops. Fill in the categories, then count "
                 "around the circle by that number, crossing out choices until one remains in each.",
        "board": ("mash", None, None),
    },
    {
        "title": "Category Sprint",
        "rules": "Pick a letter (close your eyes and point at the alphabet strip). Both players "
                 "race to fill every category with a word starting with that letter. First done — or "
                 "most after two minutes — wins.",
        "board": ("categories", None, None),
    },
    {
        "title": "Mystery Dot-to-Dot",
        "rules": "Connect the dots in number order to reveal what's hiding. No peeking at the "
                 "answer key until you're done.",
        "board": ("dottodot", None, None),
    },
    {
        "title": "Sprouts",
        "rules": "Draw 3 dots. Take turns connecting any two dots (or a dot to itself) with a "
                 "line, then add a new dot on that line. No line may cross another, and no dot "
                 "may have more than 3 lines. Last player to move wins.",
        "board": ("sprouts", None, None),
    },
    {
        "title": "Word Ladder Race",
        "rules": "Change the top word into the bottom word by swapping one letter at a time, "
                 "making a real word at every step. Fewest rungs wins the round.",
        "board": ("ladder", None, None),
    },
    {
        "title": "Alphabet Spotting",
        "rules": "Find each letter A to Z, in order, on signs and plates outside the window. "
                 "Say it out loud and cross it off. First to Z wins — no skipping ahead.",
        "board": ("checklist26", None, None),
    },
    {
        "title": "Fold-Only Fortune Teller",
        "rules": "No scissors needed — just eight folds turn this page into a working fortune "
                 "teller. Fold lines and instructions are printed for you.",
        "board": ("foldtemplate", None, None),
    },
    {
        "title": "Road Trip Bingo",
        "rules": "Cross off a square every time you spot that item out the window. First to five "
                 "in a row wins the round — then clear your board and go again.",
        "board": ("bingo", None, None),
    },
    {
        "title": "Four in a Row",
        "rules": "Take turns marking the lowest open square in any column. First to line up four "
                 "in a row — any direction — wins.",
        "board": ("grid", 7, 6),
    },
    {
        "title": "Draw & Guess Relay",
        "rules": "Pick a word from the list without showing your partner. You have 60 seconds "
                 "to draw it — no letters, no numbers. Guess right, you both score a point.",
        "board": ("drawguess", None, None),
    },
    {
        "title": "Would You Rather: Debate Edition",
        "rules": "Pick a card, pick a side, and defend it for 30 seconds. The other player is the "
                 "judge — switch roles each round. Best argument, not best answer, wins.",
        "board": ("cards", None, None),
    },
]

SCORE_NOTE = "Score sheet: tally wins below, best of three per game."

BINGO_ITEMS = [
    "Red car", "Cow", "Gas station", "Motorcycle", "Bridge", "License plate\nfrom far away",
    "Water tower", "Dog in a car", "Road work sign", "Rest stop", "Truck with a\ntrailer",
    "Church steeple", "Billboard", "Bicycle", "Train tracks", "Horse", "Flag",
    "Tunnel", "Fast food sign", "Windmill or\nsolar panel", "Convertible", "Hay bales",
    "Someone waving", "Roundabout",
]

DOT_TO_DOT_STAR = [
    (0.5, 0.95), (0.6, 0.62), (0.95, 0.62), (0.67, 0.42), (0.78, 0.08),
    (0.5, 0.28), (0.22, 0.08), (0.33, 0.42), (0.05, 0.62), (0.4, 0.62),
]

CATEGORIES = ["Animal", "Food", "Country", "Name", "Movie or show", "Thing in this car"]

MASH_CATEGORIES = {
    "Where you'll live": ["Mansion", "Apartment", "Shack", "House"],
    "Who you'll marry": ["", "", "", ""],
    "Car you'll drive": ["", "", "", ""],
    "Job you'll have": ["", "", "", ""],
    "Number of kids": ["0", "1", "2", "3+"],
}

WORD_LADDERS = [
    {"start": "COLD", "end": "WARM", "rungs": 3},
    {"start": "CAT", "end": "DOG", "rungs": 2},
]

DRAW_GUESS_WORDS = [
    "Traffic jam", "Sunburn", "Suitcase", "GPS", "Rest stop", "Toll booth",
    "Snack aisle", "Backseat", "Windshield", "Road trip", "Map", "Compass",
    "Campsite", "Sunset", "Gas pump", "Bridge", "Tunnel", "Cooler",
]

WOULD_YOU_RATHER = [
    "Would you rather ride in a car with no music, or no air conditioning?",
    "Would you rather the trip be 2 hours too long, or 2 hours too short?",
    "Would you rather pick every song, or never pick a song again?",
    "Would you rather stop every hour, or never stop at all?",
    "Would you rather sit in the middle seat the whole trip, or hold everyone's snacks?",
    "Would you rather have unlimited snacks or unlimited legroom?",
]
