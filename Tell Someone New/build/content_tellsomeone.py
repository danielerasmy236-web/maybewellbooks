"""All written content for Tell Someone New (Cuentaselo a Alguien que
Recien Conoces).

For Every Chapter line. Template B/E hybrid: one question per page with
space for BOTH people in a new pairing to answer. 30 questions ordered
lighter to more personal, mirroring how real trust builds. Written for the
newest resident in a care community — the loneliest chair in the room.
"""

CFG = {
    "EYEBROW": "FOR EVERY CHAPTER · A BOOK FOR NEW FRIENDS",
    "TITLE_LINES": ["Tell", "Someone New"],
    "SUBTITLE": "Thirty Questions for the Newest Person in the Room",
    "SPANISH_NOTE": "Cuentaselo a Alguien que Recien Conoces",
    "BADGE": "A LARGE-PRINT BOOK",
    "TAGLINE": "everyone here was new once.",
}

INTRO_KICKER = "HOW TO USE THIS"
INTRO_TITLE = "Being New Is the Hard Part"
INTRO_PARAS = [
    "Moving somewhere new — at any age — means being surrounded by people "
    "who all seem to already know each other. This book is the shortcut.",
    "It takes two: you, and someone you've just met. A neighbor, a "
    "tablemate, whoever sat down next to you. Both of you answer every "
    "question — nobody just interviews anybody.",
    ("START", "The early questions are easy on purpose. Coffee or tea is "
     "how strangers warm up."),
    ("KEEP GOING", "The questions get more personal as the pages go — the "
     "same way real trust does. Stop anywhere; skip anything."),
    ("TAKE TURNS", "One reads the question aloud, both talk, then both "
     "write. The talking matters more than the writing."),
    "Ten pages in, you won't be strangers. Thirty pages in, you'll wish "
    "you'd met sooner. The last page tells you what to do about that.",
]

# 30 questions, deliberately ordered lighter -> more personal.
QUESTIONS = [
    # warming up (1-10)
    "What's a place you lived that you still think about?",
    "What's a small thing that made you laugh recently?",
    "Coffee or tea — and how do you take it?",
    "What's a food you could eat every week for the rest of your life?",
    "What did you do on a perfect Saturday, back when Saturdays were all yours?",
    "What's the best thing about the place where you grew up?",
    "Are you a morning person or a night owl — and were you always?",
    "What music do you turn up when it comes on?",
    "What's a show or film you've gladly watched more than three times?",
    "What's the best pet you ever had — or the best one you ever met?",
    # getting somewhere (11-20)
    "What's something you're still curious about, even now?",
    "What work did you do — and what did people misunderstand about it?",
    "What's a skill you have that might surprise people here?",
    "What's a place you traveled that changed how you saw things?",
    "Who taught you something you still use every day?",
    "What tradition from your family do you miss the most?",
    "What's a book or story that stayed with you?",
    "What were you doing the last time you completely lost track of time?",
    "What's something you made — a meal, a garden, a home, a family — that you're proud of?",
    "What would your oldest friend say is the best thing about you?",
    # the real ones (21-30)
    "What's a hard season of life that shaped who you are?",
    "What do you miss that you didn't expect to miss?",
    "What's something you've changed your mind about over the years?",
    "What's a kindness from a stranger you never forgot?",
    "What are you hoping this next chapter holds?",
    "What do you wish people here would ask you about?",
    "Who do you carry with you, even though they're gone?",
    "What still feels like home to you?",
    "What's one thing you'd want a new friend here to know about you?",
    "If we talk again next week — what should we talk about?",
]

assert len(QUESTIONS) == 30

CLOSING_TITLE = "Don't let it end here."
CLOSING_PARAS = [
    "You just spent thirty questions becoming friends. Make it official: "
    "trade room numbers, phone numbers, or a standing coffee time — and "
    "write it below so neither of you can politely forget.",
]
CLOSING_FIELDS = ["Name", "Where to find me", "When we'll talk next"]
CLOSING_STATS = "30 questions  ·  2 people  ·  1 new friend  ·"
