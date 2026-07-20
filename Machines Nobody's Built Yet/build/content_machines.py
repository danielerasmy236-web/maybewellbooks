"""All written content for Machines Nobody's Built Yet (Máquinas que Nadie Ha
Construido).

Imagine line, third title — same pure-drawing-prompt template as Draw What
You Imagine and The Impossible Garden (one prompt per page, generous blank
space, no difficulty tiers, no Field Notes ★ system). Voice: curious, a
little wondrous, never childish.
"""

TITLE = "Machines Nobody's\nBuilt Yet"
TITLE_LINES = ["Machines Nobody's", "Built Yet"]
SUBTITLE = "Sixty prompts to draw the inventions that don't exist — yet"
FROM_THE_MAKERS = "from the makers of Draw What You Imagine and The Impossible Garden"
TAGLINE = "it only has to be imagined."
EYEBROW = "IMAGINE LINE · VOLUME THREE"
BADGE = "A CREATIVITY BOOK"
HASHTAG = "#MachinesNobodysBuiltYet"
SPANISH_NOTE = "Máquinas que Nadie Ha Construido"

DEDICATION = "For you, who still hears something humming that isn't there yet."

BEFORE_TITLE = "Before You Begin"
BEFORE_KICKER = "HOW THIS WORKS"
BEFORE_PARAS = [
    "This is not an engineering book.",
    "Nothing here needs to actually work. There are no blueprints to follow, "
    "no parts lists, no rules about what a machine is allowed to run on. It "
    "won't tell you how gears mesh or how a motor turns. Real machines are "
    "wonderful — but they've already been built.",
    "This book is about the other kind. The ones that only exist because "
    "someone asked the right strange question and you happened to be "
    "holding a pencil. A machine that runs on sadness. A machine that keeps "
    "one flower alive and does nothing else. A machine too big to see all "
    "at once.",
    "Every page asks you to invent something that has never been built, and "
    "never really needs to be.",
]

HOW_TITLE = "How to use this book"
HOW_PARAS = [
    "Start anywhere. There's no assembly order. Every machine in here stands "
    "on its own.",
    "Take your time. One invention a day, or ten in an afternoon. Both are "
    "correct.",
    "Nothing is a malfunction. A gear that doesn't line up is just a gear "
    "with its own ideas.",
    "Rebuild freely. The same prompt invents a completely different machine "
    "next time you draw it.",
    "There is only one rule:",
]
HOW_RULE = "Draw what nobody's built, not what already exists."
HOW_CLOSING = [
    "It doesn't matter if you're an engineer or you've never drawn a straight "
    "line. All that matters is that some part of you still believes the "
    "impossible machine is buildable, on paper, right now.",
    "This book is yours. Invent it.",
]

CLOSING_TITLE = "Finished? That's not a thing."
CLOSING_BODY = "There's no final machine to unveil here. Just the next blueprint."
CLOSING_STATS = "60 machines  ·  6 sections  ·"  # generator adds infinity mark after
CLOSING_SHARE = "Show us what you built: " + HASHTAG

COLOPHON_LINE1 = "Machines Nobody's Built Yet — Sixty prompts to draw the inventions that don't exist — yet"
COLOPHON_EDITION = "First edition · 2026"
COLOPHON_RIGHTS = "© 2026 Maybewell Books. All rights reserved."
COLOPHON_LICENSE = (
    "Personal use license: this book may be printed as many times as you "
    "like for use within your own home or classroom. It may not be resold, "
    "redistributed, or shared as a digital file."
)
COLOPHON_MADE_FOR = (
    "Made for hands that reach for a pencil before a manual. For anyone who "
    "still thinks the best machines are the ones nobody's built yet."
)
COLOPHON_URL = "maybewellbooks.com"

# (section title, note, [(prompt, hint), ...]) — 6 sections x 10 prompts = 60
SECTIONS = [
    ("Machines That Feel",
     "Every one of these machines runs on something you can't plug in.",
     [
      ("Draw a machine that only works when someone is sad.",
       "What does it do with the sadness once it has it?"),
      ("Draw a machine that hums louder the happier the room gets.",
       "Not everyone would notice it's humming at all."),
      ("Draw a machine built to hold someone's fear so they don't have to.",
       "Where does the fear go once it's inside?"),
      ("Draw the machine that turns boredom into something useful.",
       "Useful doesn't have to mean important."),
      ("Draw a machine that only turns on for people who are lying.",
       "Does it announce it, or just quietly know?"),
      ("Draw a machine built to keep a secret safe forever.",
       "Forever is a long time. Design accordingly."),
      ("Draw a machine that gets nervous before it starts.",
       "Give it a tell — something it does right before switching on."),
      ("Draw the machine that waits with you when you're waiting for "
       "something.",
       "It doesn't make the wait shorter. It just doesn't leave."),
      ("Draw a machine that only works while someone is missing another "
       "person.",
       "What happens to it once they're reunited?"),
      ("Draw a machine that laughs first so you don't have to.",
       "Some machines break the ice better than people do."),
     ]),
    ("Machines From Before",
     "Impossible history: the machines nobody credits with inventing the "
     "world's oldest things.",
     [
      ("Draw the machine that made the first sound anyone ever heard.",
       "Before this machine, everything was silent."),
      ("Draw the machine that mixed the very first color.",
       "What did the world look like the moment before?"),
      ("Draw the machine that built the first shadow.",
       "Something had to teach light where not to go."),
      ("Draw the machine that wound up the first clock and never got "
       "credit.",
       "It's still running somewhere. Probably tired."),
      ("Draw the machine that taught the ocean how to make waves.",
       "Before this, water just sat there, apparently."),
      ("Draw the machine that planted the first dream in someone's sleep.",
       "It had to guess what dreaming even was."),
      ("Draw the machine that gave the wind its first direction.",
       "It picked one. It could have picked any of them."),
      ("Draw the machine that lit the very first star, on purpose or by "
       "accident.",
       "Either way, it never told anyone which."),
      ("Draw the machine that folded the first paper airplane, before "
       "paper existed.",
       "It had to invent the paper too. Busy day."),
      ("Draw the machine that gave the first laugh its sound.",
       "Something had to decide what funny sounds like."),
     ]),
    ("One Job, Forever",
     "No backup plan, no second setting. These machines do exactly one "
     "thing, and they do it completely.",
     [
      ("Draw a machine with one job, done perfectly, forever.",
       "What's the one job? Decide before you draw the rest."),
      ("Draw a machine whose only job is to catch things before they fall.",
       "It has to be fast. Draw it mid-catch."),
      ("Draw a machine that exists only to say \"you can do this.\"",
       "Some machines are basically just very reliable friends."),
      ("Draw a machine built to hold a door open, and nothing else, ever.",
       "Give it dignity anyway. It's important work."),
      ("Draw a machine whose only purpose is keeping one specific flower "
       "alive.",
       "One flower. Not a garden. Just the one."),
      ("Draw a machine that only counts things, and has been counting for "
       "years.",
       "What number is it on? You decide."),
      ("Draw a machine that exists to remember a single date, exactly.",
       "Whose date? You don't have to say. Just draw how it remembers."),
      ("Draw a machine whose only job is folding one perfect paper crane.",
       "It has made thousands. Every one is the same. Draw the one it's on "
       "now."),
      ("Draw a machine built only to turn the page of one book, slowly, "
       "forever.",
       "Which book? Give it a spine we'd recognize, or invent one."),
      ("Draw a machine that exists purely to say goodbye properly.",
       "Some goodbyes need a whole machine. Draw what that looks like."),
     ]),
    ("Machines for Problems Nobody Has",
     "Every great invention starts by solving a problem nobody asked "
     "about.",
     [
      ("Draw something built to fix a problem nobody has yet.",
       "Invent the problem first, quietly, in your head."),
      ("Draw a machine that solves the problem of socks disappearing in "
       "the laundry.",
       "Where do they actually go? This machine knows."),
      ("Draw a machine built to un-spill something that's already spilled.",
       "Time doesn't usually work backward. Let this machine be the "
       "exception."),
      ("Draw a machine that fixes the problem of forgetting someone's name "
       "mid-sentence.",
       "It has to work fast, and quietly, without anyone noticing."),
      ("Draw a machine that solves the problem of a song stuck in your "
       "head.",
       "Does it remove the song, or just finish it for you?"),
      ("Draw a machine built to solve the problem of a too-short "
       "afternoon.",
       "It doesn't add time. It just makes the afternoon feel longer. "
       "How?"),
      ("Draw a machine that fixes the specific problem of a wobbly table "
       "leg.",
       "The most heroic machines solve the smallest problems."),
      ("Draw a machine built to solve the problem of an alarm clock nobody "
       "wants to hear.",
       "Gentle counts as a solution too."),
      ("Draw a machine that solves the problem of a joke that didn't "
       "land.",
       "Give it a second chance, somehow."),
      ("Draw a machine that fixes the problem of running out of things to "
       "say.",
       "Some silences don't need fixing. This machine disagrees."),
     ]),
    ("Tiny & Enormous",
     "Scale is optional. Some of these machines fit in a pocket. Others "
     "don't fit anywhere.",
     [
      ("Draw a machine small enough to hide inside a walnut.",
       "What does something that small even need to do?"),
      ("Draw a machine so big it needs its own weather.",
       "Weather that only happens near this one machine. What kind?"),
      ("Draw a machine that fits in the palm of your hand but does "
       "something enormous.",
       "The size of the machine and the size of its job don't have to "
       "match."),
      ("Draw a machine too large to fit in this book — just draw the part "
       "that does.",
       "A gear, a dial, a single enormous button. Pick one piece."),
      ("Draw the smallest machine that could still change someone's whole "
       "day.",
       "Small effort. Big result. That's the whole idea."),
      ("Draw a machine built into a single button, no bigger than a coin.",
       "What happens when someone presses it?"),
      ("Draw a machine so large that people who live near it have never "
       "seen the whole thing.",
       "Draw just the part visible from where you're standing."),
      ("Draw a machine that lives inside a matchbox and only comes out at "
       "night.",
       "It's shy about being seen. Give it a reason."),
      ("Draw a machine the size of a mountain that does something "
       "surprisingly gentle.",
       "Size and gentleness aren't opposites here."),
      ("Draw a machine small enough to wear, built to do one quiet thing "
       "all day.",
       "A ring, a pin, a button on a coat. What does it do while no one's "
       "looking?"),
     ]),
    ("Yours to Build",
     "No theme left to follow. The blueprint is entirely yours now.",
     [
      ("Draw the machine you'd build if you had exactly one afternoon and "
       "no rules.",
       "One afternoon isn't long. Keep it simple, or don't."),
      ("Draw a machine built entirely out of things already in this room.",
       "Look around before you start. Everything is fair game."),
      ("Draw the machine you wish existed the last time something went "
       "wrong.",
       "What would it have fixed, exactly?"),
      ("Draw a machine that only you would know how to operate.",
       "Give it a control only you'd understand."),
      ("Draw the machine your younger self would have wanted more than "
       "anything.",
       "What did you wish for, back then, that a machine could have "
       "solved?"),
      ("Draw a machine that runs on something nobody's thought to power a "
       "machine with before.",
       "Sound, static, stubbornness — pick something unlikely."),
      ("Draw the machine you'd build for someone you miss.",
       "It doesn't have to bring them back. It just has to help."),
      ("Draw a machine with a single switch you'd be a little afraid to "
       "flip.",
       "Don't flip it yet. Just draw what it might do."),
      ("Draw the last machine anyone will ever need to build.",
       "After this one, what's left to invent?"),
      ("Draw a machine with no known purpose — build it first, decide "
       "what it does later.",
       "Some of the best machines get invented backwards."),
     ]),
]

assert sum(len(s[2]) for s in SECTIONS) == 60, "prompt count must be exactly 60"
