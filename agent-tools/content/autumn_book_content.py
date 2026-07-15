"""Content data for 'The Autumn Book' (id: autumn, cat: seasonal)."""

TITLE = "The\nAutumn Book"
SUBTITLE = "Leaf rubbings, harvest counting, and a scarecrow to build"
ACCENT = "CORAL"

INTRO_BODY = [
    "One cozy season, one book. Some pages want a crayon on its side",
    "for rubbing textures. Some want counting. Some just want your",
    "imagination and a pencil.",
    "",
    "Grownups: this book is built for ages 5-8, so the activities are",
    "short on purpose — little hands finish a page and move to the next.",
    "",
    "Save the last few pages for game night. Everyone plays.",
]

SECTIONS = [
    {
        "name": "Leaf & Nature Rubbings",
        "note": "Place a real leaf underneath, rub a crayon on its side",
        "activities": [
            {"title": "Oak Leaf", "type": "rubbing", "shape": "oak"},
            {"title": "Maple Leaf", "type": "rubbing", "shape": "maple"},
            {"title": "Birch Leaf", "type": "rubbing", "shape": "birch"},
            {"title": "Gingko Leaf", "type": "rubbing", "shape": "gingko"},
            {"title": "Acorn", "type": "rubbing", "shape": "acorn"},
            {"title": "Pinecone", "type": "rubbing", "shape": "pinecone"},
        ],
    },
    {
        "name": "Harvest Counting",
        "note": "Count carefully, then write the number",
        "activities": [
            {"title": "Count the Pumpkins", "type": "counting", "icon": "pumpkin", "count": 7},
            {"title": "Count the Acorns", "type": "counting", "icon": "acorn", "count": 9},
            {"title": "Count the Apples", "type": "counting", "icon": "apple", "count": 6},
            {"title": "How Many Leaves Fell?", "type": "addition", "a": 3, "b": 4},
            {"title": "Guess How Many Seeds", "type": "estimate", "shape": "pumpkin"},
        ],
    },
    {
        "name": "Mazes & Dots",
        "note": "Trace the path, or connect the dots in order",
        "activities": [
            {"title": "Pumpkin Patch Maze", "type": "maze", "grid": (7, 7)},
            {"title": "Scarecrow's Cornfield Maze", "type": "maze", "grid": (9, 9)},
            {"title": "Connect the Dots: Pumpkin", "type": "dots", "shape": "pumpkin"},
            {"title": "Connect the Dots: Leaf", "type": "dots", "shape": "leaf"},
        ],
    },
    {
        "name": "Build-Your-Own Scarecrow",
        "note": "Circle your favorites, then draw the finished scarecrow",
        "activities": [
            {"title": "Choose a Hat", "type": "choices", "options": ["Straw hat", "Bucket", "Bandana", "Nothing — go wild"]},
            {"title": "Choose a Face", "type": "choices", "options": ["Button eyes", "Stitched smile", "Painted freckles", "Surprised look"]},
            {"title": "Choose an Outfit", "type": "choices", "options": ["Flannel shirt", "Overalls", "Patchwork coat", "Mismatched socks"]},
            {"title": "Draw Your Scarecrow", "type": "draw_blank"},
        ],
    },
    {
        "name": "More Autumn Activities",
        "note": "A little bit of everything",
        "activities": [
            {"title": "Color by Number: Autumn Tree", "type": "colorbynumber"},
            {"title": "Match the Autumn Words", "type": "wordmatch"},
            {"title": "Weather Journal", "type": "weather"},
            {"title": "Gratitude Leaves", "type": "gratitude"},
            {"title": "Design Your Own Pie", "type": "pie"},
        ],
    },
    {
        "name": "Family Game Night",
        "note": "Everyone plays — no reading level required",
        "activities": [
            {"title": "Leaf & Acorn Tic-Tac-Toe", "type": "tictactoe"},
            {"title": "Autumn Bingo", "type": "bingo"},
            {"title": "Autumn I-Spy", "type": "ispy"},
            {"title": "Autumn Charades", "type": "charades"},
        ],
    },
]

COLOR_KEY = [("1", "OCHRE"), ("2", "CORAL"), ("3", "SAGE"), ("4", "SLATE")]

WORD_MATCH_PAIRS = [
    ("Pumpkin", "A round orange squash"),
    ("Harvest", "Gathering the crops"),
    ("Scarecrow", "Guards the cornfield"),
    ("Acorn", "An oak tree's seed"),
    ("Migrate", "Birds flying south"),
    ("Hibernate", "A long winter sleep"),
]

BINGO_ITEMS = [
    "Falling leaf", "Pumpkin", "Scarf", "Hot cocoa", "Acorn", "Rake",
    "Wool sweater", "Apple", "Owl", "Foggy morning", "Squirrel", "Corn stalk",
    "Flannel", "Bonfire", "Migrating\nbirds", "Pinecone", "Hay bale", "Full moon",
    "Sweater\nweather", "Crunchy\nleaves", "Cider", "Spider web", "Orange sky", "Wind",
]

ISPY_ITEMS = [
    "Something red", "Something round", "Something with a stem",
    "Something you can wear", "Something that crunches",
    "Something bigger than your hand", "Something you can eat",
    "Something with a face on it",
]

CHARADES_ITEMS = [
    "Raking leaves", "A scarecrow in the wind", "Picking an apple",
    "A turtle hibernating", "Carving a pumpkin", "A bird flying south",
    "Drinking hot cocoa", "Jumping in a leaf pile", "A gust of wind",
    "Planting a seed", "An owl at night", "Squirrel hiding acorns",
]
