"""Content data for 'Mazes of the Lost City' (id: mazes, cat: puzzles)."""

TITLE = "Mazes of the\nLost City"
SUBTITLE = "Forty-two hand-drawn mazes that grow from friendly to fiendish"
TAGLINE = "no map needed."
ACCENT = "TEAL"

INTRO_BODY = [
    "Somewhere under the jungle canopy, a city nobody remembers building is",
    "slowly waking up. Every maze in this book is a real place in it —",
    "a gate, a courtyard, a stairway that spirals further than it should.",
    "",
    "Start at the little triangle. Find your way to the other one.",
    "Trace with a pencil so you can erase and try again — every maze",
    "has exactly one true path, and no dead end is a wrong turn, just",
    "a place the city wanted you to notice.",
    "",
    "Solutions for every maze are in the back, in case the jungle wins.",
]

TIERS = [
    {
        "key": "easy",
        "name": "Friendly Alleys",
        "note": "Easy · warm up here",
        "grid": (8, 8),
        "captions": [
            "The Vine Gate", "Sunken Courtyard", "Temple Steps", "Moss Colonnade",
            "Market Ruins", "Canopy Bridge", "Whispering Well", "Stone Serpent Path",
            "Sundial Plaza", "Lichen Stairs", "River Gate Ruins", "Toucan Perch Path",
        ],
    },
    {
        "key": "medium",
        "name": "Twisting Courtyards",
        "note": "Medium · the jungle gets opinions",
        "grid": (11, 11),
        "captions": [
            "Broken Aqueduct", "Jaguar Shrine", "Idol Chamber", "Crumbling Archive",
            "Hidden Reservoir", "Root-Bound Stair", "Obsidian Gate", "Toppled Watchtower",
            "Glyph Corridor", "Firefly Grotto", "Golden Mask Vault", "Howler's Ledge",
            "Emerald Cistern", "Silent Bell Tower",
        ],
    },
    {
        "key": "hard",
        "name": "The Fiendish Depths",
        "note": "Hard · the city stops being friendly",
        "grid": (15, 15),
        "captions": [
            "Overgrown Amphitheater", "Cracked Causeway", "Feathered Serpent Wall", "Twin Idol Gate",
            "Echoing Cenote", "Buried Observatory", "Vine-Choked Plaza", "Ember Altar",
            "Tangled Aviary", "Spiral Reliquary", "Moonlit Terrace", "Lost Archivist's Hall",
            "Sunken Ballcourt", "Ivory Tusk Gate", "The Deepest Courtyard", "The Final Descent",
        ],
    },
]

BONUS_MAP_TITLE = "The City, All at Once"
BONUS_MAP_BODY = [
    "Every gate, courtyard, and stairway you just walked through fits together —",
    "here's how. Trace your favorite route from the jungle edge to the",
    "deepest chamber, and see how many rooms from this book you can spot.",
]
