"""All written content for the Activity Coordinator Kit.

For Every Chapter line. Template G, facilitator/instructional format: the
institutional bundle for senior-center activity coordinators — one
purchase, one facilitator, a whole group served (the Teachers-line B2B2C
model, aimed at care communities). Covers the five group-ready activities
in the line, plus a photocopiable weekly planning grid.
"""

CFG = {
    "EYEBROW": "FOR EVERY CHAPTER · FACILITATOR EDITION",
    "TITLE_LINES": ["Activity", "Coordinator Kit"],
    "SUBTITLE": "Five Group Activities, One Kit, a Whole Calendar",
    "SPANISH_NOTE": None,
    "BADGE": "FOR ACTIVITY COORDINATORS",
    "TAGLINE": "one kit, a whole calendar.",
}

INTRO_KICKER = "HOW TO USE THIS KIT"
INTRO_TITLE = "Built for Your Job"
INTRO_PARAS = [
    "You run activities for a room of people with eighty-year head starts "
    "on each other. This kit gives you five sessions that need almost "
    "nothing: paper, pencils, and the lives already in the room.",
    ("GUIDES", "Each activity gets two pages: how to run it, then how to "
     "adapt it for mobility, vision, and hearing needs — because a plan "
     "that only works for the healthiest half of the room isn't a plan."),
    ("MATERIALS", "Always minimal, always listed. Nothing here needs a "
     "budget meeting."),
    ("PLANNING", "The weekly grid at the back is photocopiable — schedule "
     "which activity runs which day and pin it where families see it."),
    "Two of these activities pair with their own full books (Interview Me "
    "Group Edition, Memory Bingo). The other three run straight from this "
    "kit. Mix freely; repeat monthly — different rooms make them new.",
]

# (name, kicker, overview paras, group size, time, materials,
#  steps[], adaptations[(label, text)], variation)
ACTIVITIES = [
    ("Interview Me — Group Edition",
     "ACTIVITY ONE · CONVERSATION",
     "A facilitator-led group interview: you read one question aloud, "
     "everyone answers, then the room compares. The companion book gives "
     "each page three answer columns; without it, index cards work fine.",
     "3-8 people", "45-60 minutes", "The companion book (or index cards), pencils",
     [
      "Pick one category for the day — Childhood is the safest opener.",
      "Read each question aloud twice, slowly. Give a quiet minute.",
      "Everyone writes a short answer — a phrase is enough.",
      "Go around the room and hear the answers out loud.",
      "Always close the round with: \"Did anyone have a very different answer?\"",
     ],
     [
      ("MOBILITY", "Nothing to pass or carry; a helper can scribe for "
       "anyone whose hands tire. Answers can be fully spoken."),
      ("VISION", "The question is read aloud, so eyes are optional. Seat "
       "low-vision residents beside a neighbor who'll reread quietly."),
      ("HEARING", "Write the question big on a whiteboard as you read it. "
       "Face the room; don't walk while talking."),
     ],
     "VARIATION — Pair week: split into pairs, each pair interviews each "
     "other with the same three questions, then reports the best answer "
     "they heard (not their own)."),

    ("Memory Bingo",
     "ACTIVITY TWO · GAME",
     "Bingo where every square is a life experience — \"Learned to drive "
     "on a manual transmission\" — so every marked square is a story "
     "waiting to be asked for. The companion book has the caller list and "
     "ten unique cards, photocopiable.",
     "4-16 people", "30-45 minutes", "The companion game book (photocopy the cards), pencils or bold markers",
     [
      "Hand out one card per player; no two neighbors need the same card.",
      "Call phrases from the list in any order, big and slow, twice each.",
      "Players mark squares that are true of THEM — honor system.",
      "Every few calls, ask someone who marked: \"Tell us about that.\"",
      "Four in a row wins. Play a second round; the stories change.",
     ],
     [
      ("MOBILITY", "Bold markers beat pencils for weaker grips. A helper "
       "can mark for anyone who calls out their squares."),
      ("VISION", "Cards are large-print 4x4 by design. For very low "
       "vision, pair players — one reads, both decide."),
      ("HEARING", "Hold up a written card of each phrase as you call it, "
       "or write it on a whiteboard. Repeat on request, always."),
     ],
     "VARIATION — Story bingo: winner must retell (kindly) the best story "
     "someone ELSE told during the game to claim the win."),

    ("Tell Someone New",
     "ACTIVITY THREE · WELCOME",
     "A paired icebreaker built for the newest resident. Questions start "
     "light and get personal the way real trust does. The companion book "
     "runs one pair for thirty pages; in a group, run it as a welcome "
     "session with rotating pairs.",
     "2, or pairs in a group", "20-40 minutes", "The companion book (one per pair), or this kit's questions read aloud; pencils",
     [
      "Pair the new resident with a settled, warm one. That pairing IS the activity.",
      "Both people answer every question — nobody just interviews anybody.",
      "Start with the light questions; never open with a heavy one.",
      "Let pairs go at their own pace; ten questions is a fine session.",
      "End by having each pair set a next time to talk — and write it down.",
     ],
     [
      ("MOBILITY", "Seat pairs before starting; nothing moves after that. "
       "Writing is optional — talking is the point."),
      ("VISION", "One partner reads aloud for both. The book's large "
       "print keeps the reader from straining either."),
      ("HEARING", "Quiet corner, chairs angled close, faces visible. Slip "
       "the reader a card: \"speak slowly, not loudly.\""),
     ],
     "VARIATION — Welcome circle: whole group, one light question, "
     "everyone answers — then the new resident picks the next question."),

    ("One Photo, One Story — Group Circle",
     "ACTIVITY FOUR · KEEPSAKE",
     "The companion keepsake book is solo, but the group version is "
     "simple: everyone brings one photograph and tells the story behind "
     "it. No photo requirement for joining — borrowed prompts work: "
     "\"describe a photo you WISH existed.\"",
     "4-10 people", "30-45 minutes", "One photo per person (requested a week ahead), the book's prompts read aloud",
     [
      "Announce it a week early: \"bring one photo, any photo.\"",
      "Go in a circle: hold the photo up, say who, where, and roughly when.",
      "Then ask one deeper prompt from the book — \"who's missing from "
      "this photo that you wish were there?\"",
      "Let the room ask one question per photo before moving on.",
      "Close by inviting anyone to start the full book with today's photo.",
     ],
     [
      ("MOBILITY", "Photos pass hand to hand, or a helper walks them "
       "around. Nobody stands."),
      ("VISION", "The teller describes the photo out loud first — which "
       "is the activity anyway. Large photos beat small prints."),
      ("HEARING", "One speaker at a time, facilitator repeats each "
       "answer's key line back to the room."),
     ],
     "VARIATION — Mystery pile: photos go face-down in the middle; each "
     "person draws one and the OWNER tells its story when it surfaces."),

    ("Trivia by Decade — Table Teams",
     "ACTIVITY FIVE · GAME",
     "The companion trivia book rewards lived memory — questions like "
     "\"what did a soda fountain sell besides soda?\" In a group, run it "
     "as table teams by decade; arguments between tables are the game "
     "working as intended.",
     "6-20 people, in teams of 2-4", "30-45 minutes", "The companion book, paper and pencils per team",
     [
      "Split into tables; each table names itself after a year they loved.",
      "Read one question aloud, twice. Tables confer for one minute.",
      "Each table reports; the room votes on the best (not just right) answer.",
      "Use the book's answer notes to stir agreement — or an argument.",
      "Rotate decades each round so every table gets its home decade once.",
     ],
     [
      ("MOBILITY", "Teams stay seated the whole session; a runner (staff) "
       "collects any written answers."),
      ("VISION", "All questions are read aloud; nothing needs to be read "
       "at the tables."),
      ("HEARING", "Repeat every question at a second volume, then write "
       "the decade and key phrase on a whiteboard."),
     ],
     "VARIATION — Reverse trivia: a table states a memory (\"bread was 19 "
     "cents\"), the others guess the decade."),
]

PLANNER_TITLE = "This Week at a Glance"
PLANNER_NOTE = ("Photocopy this page. One line per day — activity, time, "
                "room. Pin it where residents and families actually look.")
PLANNER_DAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY",
                "SATURDAY", "SUNDAY"]
PLANNER_COLS = ["ACTIVITY", "TIME", "ROOM"]

CLOSING_TITLE = "The room does the real work."
CLOSING_BODY = "You just put the chairs in a circle. Same time next week."
CLOSING_STATS = "5 activities  ·  1 facilitator  ·  a whole calendar  ·"
