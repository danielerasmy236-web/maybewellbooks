"""All written content for Interview Me — Group Edition (Entrevistame).

For Every Chapter line. Template E adapted for group use: a facilitator
reads each question aloud; each page has three side-by-side answer columns
so a room can compare answers to the same question. 40 questions across
the six Grandparents' Book categories, rewritten for short spoken-then-
written answers (not duplicates of the one-on-one book).
"""

CFG = {
    "EYEBROW": "FOR EVERY CHAPTER · A GROUP INTERVIEW BOOK",
    "TITLE_LINES": ["Interview Me", "Group Edition"],
    "SUBTITLE": "One Question, a Room Full of Answers",
    "SPANISH_NOTE": "Entrevistame",
    "BADGE": "A LARGE-PRINT BOOK",
    "TAGLINE": "one question, a room full of answers.",
}

INTRO_KICKER = "FOR THE FACILITATOR"
INTRO_TITLE = "How to Run a Session"
INTRO_PARAS = [
    "This book turns an interview into a group event. One facilitator, one "
    "room, three to eight people who each lived a whole life before they "
    "met each other.",
    ("READ", "Read the question aloud, twice, slowly. The large print "
     "means anyone can also read along over your shoulder."),
    ("WRITE", "Give everyone a quiet minute. Each page has three answer "
     "columns — write a name over each column, or pass the book and let "
     "people write their own."),
    ("COMPARE", "Then the real game: go around the room and hear the "
     "answers out loud. Always ask the printed follow-up — \"Did anyone "
     "have a very different answer?\" That question does all the work."),
    "Ten questions is a full session. Mark where you stopped; different "
    "people next week make the same questions brand new.",
]

# Per-section facilitator hints, printed on each question page.
SECTIONS = [
    ("Childhood",
     "Everyone in the room was eight years old once. Start there.",
     "Read it aloud twice, then give a quiet minute before anyone answers.",
     [
      "What street did you grow up on?",
      "What was your favorite meal as a child?",
      "What did you want to be when you were ten?",
      "What got you in trouble at school?",
      "What did summer smell like where you grew up?",
      "Who was your childhood best friend?",
      "What chore was yours, and yours alone?",
     ]),
    ("Love & Family",
     "The names change. The stories rhyme.",
     "Invite one story per answer — a sentence is plenty to start.",
     [
      "How did you meet your great love — in one sentence?",
      "What is the best wedding you ever attended?",
      "What pet does your family still talk about?",
      "What is a phrase your mother or father always said?",
      "What family recipe should never be lost?",
      "What did your family argue about at the dinner table?",
      "Who in your family could make everyone laugh?",
     ]),
    ("Work & Ambition",
     "Between everyone here, there are centuries of work in this room.",
     "Ask what surprised them most about the jobs others name.",
     [
      "What did you spend your very first paycheck on?",
      "What job did you hold the longest?",
      "What skill did you have that few people have now?",
      "What was your longest commute, and how did you make it?",
      "What was the best boss you ever had like?",
      "What work are you proudest of, paid or not?",
      "If you'd had one more career, what would it have been?",
     ]),
    ("Hard Times",
     "A slower pace here. Let silence sit — someone will fill it.",
     "Read gently. Remind the room that passing is always allowed.",
     [
      "What is the hardest winter — or season of life — you remember?",
      "What shortage or hard stretch did you live through?",
      "What got your family through the leanest year?",
      "What is a goodbye you still remember?",
      "What is something you rebuilt after losing it?",
      "What advice actually helped you in the worst of it?",
     ]),
    ("Joy & Small Pleasures",
     "The easy section. Let it run long.",
     "Encourage interruptions here — joy is contagious on purpose.",
     [
      "What song can still make you dance?",
      "What is the best meal you have ever eaten?",
      "What trip would you take again tomorrow?",
      "What always makes you laugh, no matter what?",
      "What is your favorite time of day, and why?",
      "What is the best gift you ever received?",
      "What small luxury do you refuse to give up?",
     ]),
    ("Advice for Later",
     "Write these down word for word. Someone will want them.",
     "Ask the room to vote for the answer they want written largest.",
     [
      "What is worth doing slowly?",
      "What do people worry about that they shouldn't?",
      "What habit served you well for fifty years?",
      "What would you tell your thirty-year-old self?",
      "What is the secret to a good friendship?",
      "What should the youngest person in this room know?",
     ]),
]

COMPARE_PROMPT = "Then ask:  \"Did anyone have a very different answer?\""

assert sum(len(s[3]) for s in SECTIONS) == 40

CLOSING_TITLE = "Same questions, different room —"
CLOSING_BODY = "and it's a whole new book. Run it again next month."
CLOSING_STATS = "40 questions  ·  6 sections  ·  3 voices a page  ·"
