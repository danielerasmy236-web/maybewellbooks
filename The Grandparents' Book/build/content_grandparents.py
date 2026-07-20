"""All written content for The Grandparents' Book (El Libro de los Abuelos).

Field Notes line, Volume Seven. Template E, interview Q&A variant, large-print:
a younger person hand-transcribes an older relative's answers. Serves the
older-adult / multigenerational segment directly. All text renders in ink
(never the ochre accent) to stay photocopy-legible under the grayscale
luminance check — ochre is reserved for decorative shapes only.
"""

TITLE = "The Grandparents'\nBook"
TITLE_LINES = ["The Grandparents'", "Book"]
SUBTITLE = "A Large-Print Interview Book for the Stories Worth Keeping"
TAGLINE = "some stories only get told once."
EYEBROW = "FIELD NOTES · VOLUME SEVEN"
BADGE = "A LARGE-PRINT BOOK"
HASHTAG = "#TheGrandparentsBook"
SPANISH_NOTE = "El Libro de los Abuelos"

INTRO_TITLE = "Before You Begin"
INTRO_KICKER = "HOW TO USE THIS"
INTRO_PARAS = [
    "This book only works with two people: someone asking, and someone "
    "answering. Sit down together — at a kitchen table, on a porch, "
    "wherever's comfortable — and let the questions do the work.",
    "This book works in two moves:",
    ("ASK", "Read the question out loud, printed large so it's easy to read "
     "from across a table. Let the answer take as long as it takes."),
    ("WRITE", "Write down what they say, in their words, on the lines "
     "provided. You don't have to capture every word — just the story."),
    "Some questions will get a short answer. Some will take twenty minutes. "
    "Both are the right length.",
    "There's no order you have to follow. Skip around. Come back next "
    "visit. The only rule is to actually sit down and ask.",
]

CLOSING_TITLE = "The stories don't run out."
CLOSING_BODY = "There's always one more question worth asking."
CLOSING_STATS = "42 questions  ·  6 sections  ·"
CLOSING_SHARE = "Share a story you kept: " + HASHTAG

NUM_WORDS = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]

# (section title, note, [question, ...])
SECTIONS = [
    ("Childhood",
     "Start at the beginning. Most stories do.",
     [
      "What's a game you played as a child that no one plays anymore?",
      "What did your childhood home look like? Describe a room you remember clearly.",
      "Who took care of you when you were small, and what do you remember most about them?",
      "What was your favorite way to spend a free afternoon as a child?",
      "What's a smell or sound that instantly takes you back to being young?",
      "What was school like for you? Did you have a favorite teacher or subject?",
      "What's the naughtiest thing you ever did as a child — and did you get caught?",
     ]),
    ("Love & Family",
     "The people who made the family what it became.",
     [
      "How did you meet the person you loved most?",
      "What's a tradition your family had that you still think about?",
      "What's something your parents taught you without ever saying it out loud?",
      "What did your wedding day feel like, if you had one?",
      "What's the hardest part of raising a family that people don't talk about enough?",
      "Who in the family were you closest to, and why?",
      "What's a moment with someone you loved that you'd want me to know about?",
     ]),
    ("Work & Ambition",
     "What they built, chased, or wanted before it became a whole life.",
     [
      "What did you want to be when you were my age, and did it happen?",
      "What was your very first job, and what did it teach you?",
      "What's the work you're proudest of, paid or not?",
      "Did you ever take a big risk in your career or life? What happened?",
      "What's something about \"a hard day's work\" that's changed since you were young?",
      "Who inspired your ambitions when you were starting out?",
      "If you could do one thing differently in your working life, what would it be?",
     ]),
    ("Hard Times",
     "These deserve a slower pace. Let the silence sit if it needs to.",
     [
      "What's the hardest decision you ever had to make?",
      "What's a hard time in your life that you came out stronger from?",
      "What did you do when things felt like they were falling apart?",
      "Who did you lean on when times were difficult?",
      "What's something you lost that you still think about?",
      "What's a mistake you made that taught you something important?",
      "How did you keep going when you didn't feel like you could?",
     ]),
    ("Joy & Small Pleasures",
     "The good stuff. Don't rush past it.",
     [
      "What's a small thing that still makes you happy, every single time?",
      "What's the best meal you can remember, and who was there?",
      "What makes you laugh the hardest, even now?",
      "What's a place that always makes you feel at peace?",
      "What's something simple you look forward to in an ordinary day?",
      "What's a piece of music, or a song, that always lifts your mood?",
      "What's a moment of pure joy you still carry with you?",
     ]),
    ("Advice for Later",
     "The ones worth writing down word for word.",
     [
      "What's something you've never told anyone in this family?",
      "What's one piece of advice you'd want me to remember after you're gone?",
      "What do you wish someone had told you when you were my age?",
      "What's the secret to a life well lived, in your own words?",
      "What do you hope people remember about you?",
      "What's something you want me to know about who you really are?",
      "If you could leave me with just one sentence, what would it be?",
     ]),
]

assert sum(len(s[2]) for s in SECTIONS) == 42, "question count must be exactly 42"
