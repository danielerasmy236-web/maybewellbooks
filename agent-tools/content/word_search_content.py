"""Content data for 'Word Search Safari' (id: words, cat: puzzles)."""

TITLE = "Word Search\nSafari"
SUBTITLE = "Thirty-five themed word hunts across savannas, reefs, and rainforests"
ACCENT = "SAGE"

INTRO_BODY = [
    "Every puzzle in this book is hiding in a different wild place —",
    "find the words on the list, reading forward, backward, up, down,",
    "and every which way diagonal.",
    "",
    "Then look again. Every grid has one extra animal hiding in it that",
    "isn't on the list. Nobody will tell you which one. That's the game.",
    "",
    "Circle words as you find them. Answers are in the back.",
]

THEMES = [
    {
        "key": "savanna",
        "name": "Savanna Hunt",
        "note": "Grasslands, waterholes, and the long horizon",
        "pool": [
            "LION", "ZEBRA", "GIRAFFE", "ELEPHANT", "HYENA", "CHEETAH", "WARTHOG",
            "ACACIA", "ANTELOPE", "RHINO", "VULTURE", "TERMITE", "BAOBAB", "MEERKAT",
            "OSTRICH", "JACKAL", "BUFFALO", "HIPPO", "GAZELLE", "SAVANNA",
        ],
        "bonus_pool": ["WILDEBEEST", "MONGOOSE", "IMPALA", "HORNBILL"],
        "count": 12,
    },
    {
        "key": "reef",
        "name": "Reef Hunt",
        "note": "Coral gardens and the creatures that hide in them",
        "pool": [
            "CORAL", "CLOWNFISH", "OCTOPUS", "STARFISH", "SEAHORSE", "TURTLE",
            "STINGRAY", "ANEMONE", "SHARK", "DOLPHIN", "JELLYFISH", "LOBSTER",
            "CRAB", "MANTA", "URCHIN", "KELP", "LAGOON", "SPONGE", "SHELL", "EEL",
        ],
        "bonus_pool": ["BARRACUDA", "PARROTFISH", "PUFFERFISH", "TIDEPOOL"],
        "count": 12,
    },
    {
        "key": "rainforest",
        "name": "Rainforest Hunt",
        "note": "Canopy, vines, and the loudest quiet place on Earth",
        "pool": [
            "JAGUAR", "TOUCAN", "MONKEY", "PARROT", "SLOTH", "FROG", "BUTTERFLY",
            "CANOPY", "VINE", "ORCHID", "MACAW", "IGUANA", "TAPIR", "ANTEATER",
            "GECKO", "CHAMELEON", "FERN", "BEETLE", "MOSS", "HOWLER",
        ],
        "bonus_pool": ["ANACONDA", "TARANTULA", "HORNBILL", "WATERFALL"],
        "count": 11,
    },
]

WORDS_PER_PUZZLE = 8
GRID_SIZE = 13
