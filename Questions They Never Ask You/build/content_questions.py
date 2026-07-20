"""All written content for Questions They Never Ask You (Preguntas que Nunca
te Hacen).

Field Notes line, Volume Five. Template B, two-answer variant: written-answer
format with TWO answer zones per page (two people both answer the same
question) instead of a single log/draw zone. Deliberately avoids generic
icebreaker clichés in favor of strange, real, or oddly specific questions.
"""

TITLE = "Questions They\nNever Ask You"
TITLE_LINES = ["Questions They", "Never Ask You"]
SUBTITLE = "A Conversation Manual for Dinners, Car Rides, and Waiting Rooms"
TAGLINE = "these are the ones worth asking."
EYEBROW = "FIELD NOTES · VOLUME FIVE"
BADGE = "A CONVERSATION BOOK"
HASHTAG = "#QuestionsTheyNeverAskYou"
SPANISH_NOTE = "Preguntas que Nunca te Hacen"

INTRO_TITLE = "Before You Begin"
INTRO_KICKER = "HOW TO USE THIS"
INTRO_PARAS = [
    "Most conversation starters ask the same six questions in different "
    "clothes. This book doesn't. Every question here was picked because it's "
    "specific enough to get a real answer instead of a rehearsed one.",
    "This book works in two moves:",
    ("ASK", "Pick a question — in order or at random. Read it out loud to "
     "whoever you're with. Give it a second before anyone answers; the good "
     "answers usually come after the pause."),
    ("ANSWER", "Both of you write your own answer, in your own space, at "
     "the same time. Read them out loud after — not before. The differences "
     "are the interesting part."),
    "There's no scoring, no winning, no correct answer. A short answer is "
    "still an honest one.",
    "Pick a question. Ask it out loud. See what comes back.",
]

CLOSING_TITLE = "Out of questions? Good."
CLOSING_BODY = "That means it's time to make up your own."
CLOSING_STATS = "48 questions  ·  6 sections  ·"
CLOSING_SHARE = "Share your favorite answer: " + HASHTAG

NUM_WORDS = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]

# (section title, note, [question, ...])
SECTIONS = [
    ("Odd & Absurd",
     "No wrong answers here — just the more interesting ones.",
     [
      "If you had to teach a stranger one skill in 10 minutes, what would you pick?",
      "If you could swap lives with one animal for exactly one day, which would you choose?",
      "What's the strangest thing you've ever eaten on a dare — or almost did?",
      "If your life had a laugh track, what moment would it play right now?",
      "What's one food combination you love that everyone else finds disgusting?",
      "If you had to give up one sense for a year to keep the other four sharper, which would you give up?",
      "What's the weirdest thing you've ever looked up at 2 a.m.?",
      "If you could instantly become fluent in one made-up language, which fictional one would you pick?",
     ]),
    ("Quietly Deep",
     "Slow down for these. They reward it.",
     [
      "What's something you believed as a child that you were embarrassed to unlearn?",
      "What's a rule you follow that you've never explained to anyone?",
      "What does \"home\" actually mean to you, beyond an address?",
      "What's a compliment you received once that you still think about?",
      "What's something you're quietly proud of that no one ever asks about?",
      "What would you want people to remember about how you made them feel?",
      "What's a fear you've never said out loud?",
      "What's something you forgive yourself for now that you didn't used to?",
     ]),
    ("About the Past",
     "Old ground, asked in a way that makes it new again.",
     [
      "What's a smell that instantly takes you back to being a kid?",
      "What's the first thing you remember wanting to be when you grew up?",
      "What's a small decision that changed the direction of your life?",
      "Who was the first person who ever really believed in you?",
      "What's a place from your childhood you wish you could visit one more time?",
      "What's something you got in trouble for that you'd do again?",
      "What's the best piece of advice you ignored — and later wished you hadn't?",
      "What did a year of your life look like that no one else was around to see?",
     ]),
    ("About Right Now",
     "Present tense. No looking back, no looking ahead.",
     [
      "If today had a soundtrack, what's the one song stuck in it?",
      "What's something you're looking forward to this week that you haven't told anyone?",
      "What's occupying more of your headspace than it probably should right now?",
      "What's the last thing that made you genuinely laugh out loud?",
      "If you had one unplanned free hour today, what would you actually do with it?",
      "What's a small thing that's been going right lately that you haven't celebrated?",
      "What's something you're currently learning, on purpose or by accident?",
      "What mood best describes you today, in exactly one word?",
     ]),
    ("About Someone Else at the Table",
     "Turn these outward. The best answers are about the person across from you.",
     [
      "What's one thing about the person to your right that you've always admired but never said out loud?",
      "Think of whoever's been quietest tonight — what do you think they're thinking about right now?",
      "What's a strength in someone else at this table that they probably underestimate?",
      "If you had to guess, what's on someone else's mind that they haven't shared tonight?",
      "What's something you've learned from someone here without them ever teaching it on purpose?",
      "Who here would you trust with a secret, and why?",
      "What's a compliment you've never said to someone at this table — and why not?",
      "If you could ask one person here anything and get an honest answer, what would you ask?",
     ]),
    ("Hypotheticals",
     "Made up, but the answers never are.",
     [
      "If you woke up tomorrow with any one superpower, which would you pick — and would you actually tell anyone?",
      "If you could relive one ordinary day exactly as it happened, which would you choose?",
      "If you had to move to a country you've never visited, tomorrow, which would you pick?",
      "If you could send a message back to yourself five years ago, what's the one thing you'd say?",
      "If you had to trade your phone for one object for a month, what would you pick?",
      "If you could instantly master one skill overnight, what would you choose — and what would you do with it first?",
      "If your life became a book tomorrow, what would the title be?",
      "If you could have dinner with any three people, living or not, who would be at the table?",
     ]),
]

assert sum(len(s[2]) for s in SECTIONS) == 48, "question count must be exactly 48"
