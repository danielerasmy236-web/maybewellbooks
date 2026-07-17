"""All written content for the "For Teachers and Educators" line.

Three activities, each in two formats:
  - single: 3 pages (activity sheet / teacher's quick guide / alternate sheet)
  - weekly: 7 pages (teacher intro + 5 day sheets + closing sheet)

Design constraints baked into the copy:
  - Full printable sheets only. No cards, no cutting. Folding only where the
    activity itself is a fold (Chain Story).
  - A teacher must be able to print and use each sheet as-is: all rules are
    printed on the sheet itself.
  - Black & white first: nothing here refers to color except as a bonus.
"""

LINE_NAME = "FOR TEACHERS & EDUCATORS"
FOOTER = "maybewellbooks.com · print freely for your own classroom"

# ---------------------------------------------------------------- CHAIN STORY

CHAIN = {
    "id": "chain",
    "title": "Chain Story",
    "subtitle": "A story written by everyone — and read by no one, until the end.",
    "teacher_line": "GROUPS OF 3–6 · ~10 MINUTES · PENCILS ONLY · NO PREP — ONE SHEET PER GROUP",
    "zone_caption": "write your line, then fold back along this line and pass left",
    "zone_caption_draw": "draw your part, then fold back along this line and pass left",
    "closing": "UNFOLD & READ ALOUD — every group reads its story to the class. Expect chaos.",
    "single_open": ("THE STORY STARTS HERE:",
                    "Once, at exactly midnight, the school's pet hamster opened one eye and said…"),
    "single_alt_open": ("THE CASE STARTS HERE:",
                        "The locker at the end of the hall had been sealed for twenty years — until this morning."),
    "guide": [
        ("Why it works", "Nobody sees the whole story until the end, so there is no wrong line and no way to fall behind. Reluctant writers only ever owe one sentence."),
        ("How to run it", "Hand one sheet to each group. Point at the sheet. That's the whole setup — the rules are printed at every fold."),
        ("Drawing mode", "Groups that write slowly can draw their line instead. Same folds, same chaos."),
        ("Mixed ages", "Seat stronger writers at zones 1 and 6 (the opening and the ending) and let everyone else land anywhere in the middle."),
        ("Timing", "About 90 seconds per fold keeps a class of groups roughly in sync. Call the passes out loud if the room drifts."),
        ("The read-aloud", "It's the whole payoff. Keep it — even if you have to cut the writing short."),
    ],
    "week_arc": "Five stories, five moods. The fold-and-pass mechanic never changes, so by Tuesday your class runs it without you — only the opening line changes each day.",
    "week_tip": "Keep Friday's genre vote quick: thirty seconds, majority wins, no campaigning.",
    "days": [
        ("MONDAY", "Silly", "THE STORY STARTS HERE:",
         "Once, at exactly midnight, the school's pet hamster opened one eye and said…", False),
        ("TUESDAY", "Mystery", "THE CASE STARTS HERE:",
         "The locker at the end of the hall had been sealed for twenty years — until this morning.", False),
        ("WEDNESDAY", "What if", "THE QUESTION IS:",
         "What if gravity took the day off, starting right after breakfast?", False),
        ("THURSDAY", "No words", "NO WORDS TODAY.",
         "The first artist draws a character. Fold. The next draws where it lives. Fold. Keep building its world — pictures only.", True),
        ("FRIDAY", "Your genre", "YOUR GROUP PICKS THE GENRE:",
         "Scary, funny, epic, heartbreaking — vote, then write your own opening line below and start the chain.", False),
    ],
    "closing_title": "Story Gallery",
    "closing_sub": "Friday's last ten minutes: every group copies its best unfolded story of the week onto this sheet, signs it, and pins it up for the class to read.",
    "closing_note": "Group names & authors:",
}

# ------------------------------------------------------------ GROUP DETECTIVE

DETECTIVE = {
    "id": "detective",
    "title": "Group Detective",
    "subtitle": "Your group has something in common that nobody knows yet. Find it.",
    "teacher_line": "GROUPS OF 3–5 · 10–15 MINUTES · PENCILS ONLY · NO PREP — ONE SHEET PER GROUP",
    "brief": "THE CASE: somewhere in this group hides something you all share — a habit, a fear, a tiny joy. Ask, compare, interrogate. When every member matches, the case is solved.",
    "solved_label": "CASE SOLVED",
    "solved_line": "We all…",
    "signed_line": "Signed by the whole squad:",
    "single_qs": [
        "What's something you do every single night before falling asleep?",
        "What sound instantly puts you in a good mood?",
        "What's a small thing you're afraid of that most people aren't?",
        "What's a rule at your house that other houses don't seem to have?",
        "What's something tiny that made you happy this week?",
        "What do you always notice about a room that nobody else notices?",
    ],
    "single_alt_qs": [
        "What's the first thing you check when you walk into a new room?",
        "What food do you refuse to let touch other food on your plate?",
        "What's a sound that instantly annoys everyone in your family?",
        "What do you save that other people throw away?",
        "What's something you've never told anyone is actually easy for you?",
        "What tiny superstition do you secretly follow?",
    ],
    "guide": [
        ("Why it works", "It's social-emotional learning wearing a trench coat. Finding a real, specific commonality builds group identity faster than any icebreaker about favorite colors."),
        ("How to run it", "One sheet per group. The case brief on the sheet does the explaining. Your only job is to enforce the 'every member matches' rule."),
        ("Push past the obvious", "If a group 'solves' the case in one minute ('we all breathe'), send them back for something that surprised at least one member."),
        ("Quiet students", "The questions are answered around the group one at a time, so nobody has to fight for a turn."),
        ("Mixed ages", "Younger groups can answer out loud and have one scribe. The commonality still has to be written down to count."),
        ("The reveal", "If time allows, each group announces its commonality to the class. The weirder, the better received."),
    ],
    "week_arc": "Five cases, five categories. Each day the investigation digs somewhere different — what you've done, what you love, what you fear, where you come from — and Friday the detectives write their own case.",
    "week_tip": "Keep the groups identical all week. The point is watching the same people keep discovering each other.",
    "days": [
        ("MONDAY", "Shared experiences", "TODAY'S CASE: find one thing you have ALL done.", [
            "What's a place you've all been?",
            "What's a small disaster you've all survived? (a lost tooth counts)",
            "What's something you all did before turning six?",
            "What's a food you've all tried — and all hated?",
            "What's a game you've all played?",
        ]),
        ("TUESDAY", "Shared preferences", "TODAY'S CASE: find one opinion you ALL hold.", [
            "What's a smell you all like?",
            "What's the worst chore — can you agree unanimously?",
            "What's the best season? Debate until you match.",
            "What's a movie or show you've all watched twice?",
            "What's something you all collect — or would, if you could?",
        ]),
        ("WEDNESDAY", "Fears & dreams", "TODAY'S CASE: find one fear or one dream you ALL share.", [
            "What's a tiny fear you all have?",
            "What would you all try if you knew you couldn't fail?",
            "Where would you all go tomorrow if you could?",
            "What's a skill you all wish you had?",
            "What do you all worry about the night before school?",
        ]),
        ("THURSDAY", "Family patterns", "TODAY'S CASE: find one thing all your homes have in common.", [
            "What's a rule that exists at all of your houses?",
            "What's a phrase your grown-ups all say?",
            "What dish shows up at every one of your family tables?",
            "Who's the loudest person at home — is it the same answer?",
            "What's a family habit you all secretly like?",
        ]),
        ("FRIDAY", "The open case", "TODAY'S CASE: yours. Write your own five questions, interrogate, solve.", [
            "", "", "", "", "",
        ]),
    ],
    "closing_title": "Certificate of Detection",
    "closing_sub": "One full-sheet certificate per squad — fill it in, sign it, pin it up.",
    "closing_fields": ["This certifies that the squad known as", "solved five cases this week, including their finest discovery:", "Witnessed and confirmed on this day"],
}

# --------------------------------------------------------- BUILD WITHOUT WORDS

SILENT = {
    "id": "silent",
    "title": "Build Without Words",
    "subtitle": "One scene. Many hands. Zero talking.",
    "teacher_line": "GROUPS OF 3–6 · ~10 MINUTES · PENCILS OR MARKERS · NO PREP — WORKS AS A CALM-DOWN OR TRANSITION",
    "rules": [
        "No talking, no pointing, no mouthing words. Silence is the whole game.",
        "Take turns: about 30 seconds each, then slide the sheet to your left.",
        "Add to the scene. Never cross out or draw over what someone made.",
        "Three rounds each, then stop, sit back, and admire what nobody planned.",
    ],
    "canvas_label": "THE SCENE — start anywhere",
    "single_alt_note": "GRID VARIANT: each artist owns one panel — but the scene must connect across every border. Roads, rivers, wires, weather: make it one world.",
    "guide": [
        ("Why it works", "Silence removes negotiation, which removes conflict. The group coordinates through the drawing itself — it's teamwork with the arguing surgically removed."),
        ("How to run it", "One sheet per group, pencils out, point at rule 1. The room goes quiet on its own."),
        ("As a calming tool", "This is a legitimate transition activity: after recess, before a test, during an overstimulated afternoon. Ten silent minutes that feel like a game."),
        ("Mixed ages", "Nothing to read beyond four rules, nothing to write. Fives and twelves can share a sheet."),
        ("If someone talks", "Their next turn is a single dot. House rule — enforce it with a smile."),
        ("Keep the art", "Date the sheets and keep them. A month of silent scenes makes a surprisingly good wall."),
    ],
    "week_arc": "Five silent scenes, one new constraint per day. The rule 'no talking' never changes — everything else slowly gets stranger, and Friday the whole week gets taped into one class mural.",
    "week_tip": "Save every sheet all week. Friday needs them.",
    "days": [
        ("MONDAY", "Free scene", "Today's constraint: none. Draw anything, together, silently."),
        ("TUESDAY", "Shapes only", "Today's constraint: shapes only — no letters, no numbers, no symbols you could read."),
        ("WEDNESDAY", "One color", "Today's constraint: the group picks ONE pencil or marker color before starting. Everyone shares it. (In a black-and-white world, one shade of gray counts.)"),
        ("THURSDAY", "Eyes closed first", "Today's constraint: every artist draws their FIRST mark of each turn with eyes closed. Open, look at what happened, and build from there."),
        ("FRIDAY", "The mural tile", "Today's sheet is one tile of a class mural. Draw to every edge — the marks on the borders show where your world must connect to your neighbors' worlds."),
    ],
    "closing_title": "Assembling the Mural",
    "closing_sub": "No scissors, no glue sticks: the mural is a taped-edge grid.",
    "closing_steps": [
        "Collect every group's Friday tile (and any earlier sheet the class wants to include).",
        "Lay them face-down in a grid on the floor, edges touching.",
        "Tape along every seam on the back — painter's tape peels off walls cleanly later.",
        "Flip the whole grid over. The edge marks on each tile should meet their neighbors.",
        "Hang it. Title it as a class — that vote can be out loud.",
    ],
}

PRODUCTS = [CHAIN, DETECTIVE, SILENT]
