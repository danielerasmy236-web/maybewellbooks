"""Content data for 'Little Logic Lab' (id: logic, cat: puzzles)."""

TITLE = "Little\nLogic Lab"
SUBTITLE = "Grid puzzles, deduction cases, and pattern riddles"
TAGLINE = "no luck required."
ACCENT = "VIOLET"

INTRO_BODY = [
    "Three kinds of puzzle live in this book, and none of them need luck.",
    "",
    "Logic grids: three friends, three things, three more things. Read",
    "every clue before you guess — the answer is always fully provable,",
    "never a coin flip.",
    "",
    "Pattern riddles: figure out the rule, then continue it.",
    "",
    "Detective cases: read every witness carefully. One of them is",
    "always lying, or leaving something out.",
    "",
    "Full solutions are in the back — but try not to peek early.",
]

NAME_POOL = [
    "Ana", "Ben", "Cleo", "Maya", "Theo", "Lily", "Omar", "Nadia", "Kai",
    "Zara", "Milo", "Ivy", "Ruby", "Finn", "Nora", "Eli", "Tess", "Gus",
    "Iris", "Dev", "Coco", "Sam", "Wren", "Max", "Bea", "Otto", "Juno",
    "Leo", "Mia", "Cy",
]

GRID_THEMES = [
    {"attr_b": "pet", "b_values": ["cat", "dog", "fish"], "attr_c": "color", "c_values": ["red", "blue", "green"]},
    {"attr_b": "instrument", "b_values": ["drum", "violin", "flute"], "attr_c": "color", "c_values": ["purple", "orange", "yellow"]},
    {"attr_b": "dessert", "b_values": ["cupcake", "pie", "cookie"], "attr_c": "color", "c_values": ["pink", "teal", "gold"]},
    {"attr_b": "pet", "b_values": ["rabbit", "hamster", "parrot"], "attr_c": "color", "c_values": ["red", "green", "blue"]},
    {"attr_b": "toy", "b_values": ["kite", "robot", "yo-yo"], "attr_c": "color", "c_values": ["silver", "crimson", "navy"]},
    {"attr_b": "instrument", "b_values": ["guitar", "trumpet", "drum"], "attr_c": "color", "c_values": ["maroon", "cyan", "lime"]},
    {"attr_b": "fruit", "b_values": ["mango", "peach", "plum"], "attr_c": "color", "c_values": ["red", "yellow", "purple"]},
    {"attr_b": "pet", "b_values": ["turtle", "lizard", "frog"], "attr_c": "color", "c_values": ["green", "brown", "blue"]},
    {"attr_b": "game", "b_values": ["chess set", "checkers set", "dominoes set"], "attr_c": "color", "c_values": ["black", "white", "red"]},
    {"attr_b": "dessert", "b_values": ["brownie", "muffin", "tart"], "attr_c": "color", "c_values": ["brown", "pink", "orange"]},
    {"attr_b": "gadget", "b_values": ["telescope", "drone", "camera"], "attr_c": "color", "c_values": ["black", "silver", "blue"]},
    {"attr_b": "instrument", "b_values": ["piano", "cello", "clarinet"], "attr_c": "color", "c_values": ["ivory", "brown", "gold"]},
    {"attr_b": "pet", "b_values": ["gecko", "ferret", "chinchilla"], "attr_c": "color", "c_values": ["gray", "tan", "white"]},
    {"attr_b": "fruit", "b_values": ["kiwi", "fig", "pear"], "attr_c": "color", "c_values": ["green", "purple", "yellow"]},
    {"attr_b": "ride", "b_values": ["skateboard", "scooter", "bicycle"], "attr_c": "color", "c_values": ["red", "blue", "black"]},
]

PATTERN_RIDDLES = [
    {"title": "Number Riddle #1", "seq": ["2", "4", "6", "8", "?"], "answer": "10", "rule": "add 2 each time"},
    {"title": "Number Riddle #2", "seq": ["1", "2", "4", "8", "16", "?"], "answer": "32", "rule": "double each time"},
    {"title": "Number Riddle #3", "seq": ["1", "1", "2", "3", "5", "8", "?"], "answer": "13", "rule": "add the two numbers before it"},
    {"title": "Number Riddle #4", "seq": ["100", "90", "80", "70", "?"], "answer": "60", "rule": "subtract 10 each time"},
    {"title": "Letter Riddle #1", "seq": ["A", "C", "E", "G", "?"], "answer": "I", "rule": "skip one letter each time"},
    {"title": "Number Riddle #5", "seq": ["3", "6", "12", "24", "?"], "answer": "48", "rule": "double each time"},
    {"title": "Number Riddle #6", "seq": ["20", "17", "14", "11", "?"], "answer": "8", "rule": "subtract 3 each time"},
    {"title": "Letter Riddle #2", "seq": ["Z", "Y", "X", "W", "?"], "answer": "V", "rule": "go backward one letter each time"},
    {"title": "Number Riddle #7", "seq": ["1", "4", "9", "16", "?"], "answer": "25", "rule": "each number is a number multiplied by itself (1x1, 2x2, 3x3...)"},
    {"title": "Number Riddle #8", "seq": ["5", "10", "20", "40", "?"], "answer": "80", "rule": "double each time"},
    {"title": "Letter Riddle #3", "seq": ["B", "D", "F", "H", "?"], "answer": "J", "rule": "skip one letter each time"},
    {"title": "Number Riddle #9", "seq": ["2", "3", "5", "7", "11", "?"], "answer": "13", "rule": "each number can only be divided evenly by 1 and itself"},
    {"title": "Number Riddle #10", "seq": ["1", "3", "6", "10", "?"], "answer": "15", "rule": "add one more each time (+2, +3, +4, +5...)"},
    {"title": "Number Riddle #11", "seq": ["64", "32", "16", "8", "?"], "answer": "4", "rule": "cut in half each time"},
    {"title": "Shape Riddle", "seq": ["circle", "square", "circle", "square", "circle", "?"], "answer": "square", "rule": "alternating shapes"},
]

DETECTIVE_CASES = [
    {
        "title": "The Missing Cupcake",
        "setup": "There were six cupcakes on the counter. Now there are five. Three suspects were in "
                 "the kitchen this afternoon.",
        "suspects": [
            "Priya says she was doing homework at the table the whole time.",
            "Jonah says he was outside until dinner.",
            "Sasha says she only had a glass of water in the kitchen.",
        ],
        "clues": [
            "There are crumbs on the homework table.",
            "The back door was locked all afternoon and nobody used it.",
            "Sasha's glass is still full of water, untouched.",
        ],
        "solution": "Priya. Jonah's alibi (outside) is impossible since the locked door means nobody went "
                    "outside. Sasha's glass is untouched, so her story checks out. The crumbs on the "
                    "homework table point to Priya.",
    },
    {
        "title": "Who Broke the Window?",
        "setup": "A window in the garage is cracked. A ball, a kite, and a bicycle were all nearby.",
        "suspects": [
            "Deshawn says he was flying his kite in the front yard.",
            "Lucia says she was riding her bike around the block.",
            "Theo says he was practicing soccer kicks against the garage.",
        ],
        "clues": [
            "The crack is at the exact height of the garage's basketball hoop, low and round.",
            "The kite string is tangled in the tree, nowhere near the garage.",
            "Lucia's bike tires are dry, but it rained an hour before the window broke.",
        ],
        "solution": "Theo. The kite is confirmed elsewhere by the tangled string. Lucia's dry tires mean she "
                    "wasn't riding recently. A round crack at kicking height points to Theo's soccer ball.",
    },
    {
        "title": "The Library Mystery",
        "setup": "A rare map is missing from the library's glass case. Three visitors signed in that day.",
        "suspects": [
            "Ms. Alvarez says she was reading in the history section all morning.",
            "Mr. Finch says he was fixing the sink in the staff bathroom.",
            "Ms. Okafor says she was returning books to the far shelves.",
        ],
        "clues": [
            "The glass case was opened with the librarian's spare key, kept behind the front desk.",
            "The staff bathroom sink was not touched — it's been broken for a week and still is.",
            "Ms. Okafor's returned books are all sorted perfectly onto the far shelves, exactly as she said.",
        ],
        "solution": "Mr. Finch. His alibi is disproven by the untouched sink. Ms. Okafor's task is verified by "
                    "the sorted books. That leaves Mr. Finch, who must have taken the spare key from the "
                    "front desk while claiming to fix the sink.",
    },
    {
        "title": "The Case of the Muddy Footprints",
        "setup": "Muddy footprints lead from the garden straight into the kitchen. Three people were home.",
        "suspects": [
            "Grandpa says he was napping in his armchair all afternoon.",
            "Ren says he was watering the garden in rain boots.",
            "Ivy says she was doing a puzzle at the kitchen table, barefoot.",
        ],
        "clues": [
            "The footprints are small, bare, and end right at the kitchen table.",
            "Grandpa's armchair still has his glasses balanced on the armrest, exactly where he left them.",
            "Ren's rain boots are by the garden hose, still muddy on the outside only.",
        ],
        "solution": "Ivy. The footprints are bare, matching Ivy, not Ren's boots. They lead to the kitchen "
                    "table, right where she says she was. Grandpa's undisturbed glasses confirm he never "
                    "got up.",
    },
    {
        "title": "The Vanishing Trophy",
        "setup": "The class trophy disappeared from the shelf sometime during lunch. Three classmates "
                 "stayed inside.",
        "suspects": [
            "Amara says she was drawing at her desk the entire lunch period.",
            "Beckett says he was helping the teacher organize the supply closet.",
            "Dani says she was reading near the window, closest to the trophy shelf.",
        ],
        "clues": [
            "Amara's drawing is finished and dated with the exact time lunch started.",
            "The supply closet is locked, and only the teacher has that key — Beckett never went in.",
            "A bookmark shaped like the trophy is now sitting on the windowsill where Dani was reading.",
        ],
        "solution": "Dani. Amara's dated drawing confirms she was busy the whole time. Beckett couldn't have "
                    "entered the locked closet. The trophy-shaped bookmark left behind points to Dani, who "
                    "was closest to the shelf the whole time.",
    },
]
