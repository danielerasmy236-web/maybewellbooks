"""All written content for Wander Without a Destination (Camina Sin Rumbo).

Field Notes line, Volume Two. Template B: two-zone layout (WALK / LOG+NOTICE) —
no draw box, since this book is about walking, not sketching. Prompts are
semi-random instructions for a destination-less walk, in DWYI's voice: curious,
a little wondrous, never childish.

Stars: 1 = easy, 2 = some effort, 3 = real challenge. 0 = open/blank instruction
(the reader supplies the rule).
"""

TITLE = "Wander Without\na Destination"
TITLE_LINES = ["Wander Without", "a Destination"]
SUBTITLE = "An Instruction-Led Guide to Getting Pleasantly Lost"
TAGLINE = "get a little lost."
EYEBROW = "FIELD NOTES · VOLUME TWO"
BADGE = "A WANDERING BOOK"
HASHTAG = "#WanderWithoutADestination"
SPANISH_NOTE = "Camina Sin Rumbo"

INTRO_TITLE = "Before You Wander"
INTRO_KICKER = "HOW THIS WORKS"
INTRO_PARAS = [
    "The French call it a dérive — a drift. Walking guided by nothing "
    "but instinct, a whim, or in this case, a page. No map, no destination, "
    "no app buzzing turn-by-turn directions in your ear. Just you, outside, "
    "following a rule strange enough to take you somewhere you wouldn't have "
    "gone on your own.",
    "This book works in two moves:",
    ("WALK", "Each page gives you one instruction. That's your only map for "
     "this walk — no shortcuts, no peeking ahead to see where it leads."),
    ("LOG", "When you stop, jot down where you ended up and when. Then use "
     "the lines below to note one thing you noticed along the way. A "
     "wander without a record is just an errand."),
    "The stars tell you what kind of walk you're in for:",
    ("STARS", ""),  # placeholder: the generator draws the three star rows here
    "There is no wrong way to get lost. The map was never really the point.",
    "Go outside. Follow the instruction. See where you end up.",
]

STAR_LEGEND = [
    (1, "easy — a short detour from your normal route"),
    (2, "some effort — you'll have to commit to it"),
    (3, "a real challenge — time, patience, maybe a little nerve"),
]

CLOSING_TITLE = "Arrived? That's not really the point."
CLOSING_BODY = "There's no destination to check off here. Just the next walk."
CLOSING_STATS = "70 walks  ·  7 sections  ·"  # generator adds infinity mark after
CLOSING_SHARE = "Share your route: " + HASHTAG

# (section title, note, [(stars, prompt, hint), ...])
SECTIONS = [
    ("Turns & Chance",
     "Let luck pick your corners. You just have to follow through.",
     [
      (1, "Turn left at the third corner you reach. Keep walking until something makes you stop.",
          "Don't pick the something. Let it pick you."),
      (2, "Flip a coin at every corner — heads turns right, tails turns left. Walk until you're bored of flipping.",
          "No coin? Use a leaf, a pebble, whichever hand is closer to your pocket."),
      (1, "Pick a direction using nothing but which way the wind is blowing.",
          "No wind today? Follow the first breeze you feel, even a small one."),
      (2, "At every intersection, take whichever street looks less familiar.",
          "Familiar is a habit. Today you're breaking it on purpose."),
      (3, "Think of a number from 1 to 6 before you leave. Turn that many times before choosing a direction to commit to.",
          "Count out loud if it helps. This is the closest thing to a rule this walk has."),
      (1, "Turn toward whichever direction has more trees in view.",
          "Green counts even if it's just one stubborn tree in a parking lot."),
      (2, "Let a stranger's turn decide yours — follow the direction of the next person who crosses your path, until they're out of sight, then choose your own.",
          "You're not following them. You're borrowing their decision for thirty seconds."),
      (3, "At each corner, alternate: first right, next left, next right, and so on, no matter how it backtracks you.",
          "Keep a mental tally. Losing count is allowed — just restart from right."),
      (1, "Choose your first turn by whichever direction the nearest door is facing.",
          "Any door. A house, a shop, a gate. It's just there to get you started."),
      (2, "Walk until you reach a color you weren't expecting, then turn toward it.",
          "Unexpected doesn't mean rare. It means it surprised you specifically."),
     ]),
    ("Follow a Sense",
     "Let your eyes, ears, and nose do the navigating for once.",
     [
      (2, "Walk toward the loudest sound you can hear right now.",
          "Traffic counts. So does a dog, a fountain, someone's music through a window."),
      (1, "Follow the color yellow for as long as you can find it.",
          "A door, a sign, a flower, a jacket. Yellow is more common than you think."),
      (2, "Close your eyes for ten seconds, then walk toward whatever smell reaches you first.",
          "Bread, exhaust, cut grass — the nose doesn't get to be picky today."),
      (3, "Walk with your eyes mostly on the ground for five minutes. Follow whatever texture changes under your feet — pavement to grass to gravel.",
          "Keep your peripheral vision for safety. The point is what's underfoot, not what's ahead."),
      (1, "Walk toward the coolest patch of shade you can see.",
          "Shade moves all day. So will you, chasing the next one."),
      (2, "Find the quietest street nearby and walk its full length before deciding what's next.",
          "Quiet is relative. Just quieter than where you started."),
      (3, "Walk without your phone in your hand for 10 minutes. Notice what you notice.",
          "Pocket it, don't just silence it. The point is not reaching for it."),
      (1, "Follow whichever direction smells the most like food.",
          "A bakery, a food cart, someone's kitchen window. Let your stomach navigate."),
      (2, "Walk toward the brightest patch of sunlight you can see, then find the next one from there.",
          "Chain the bright spots together like stepping stones."),
      (3, "Walk with one hand trailing along every fence, wall, or railing you pass, and let your route bend to keep the touch unbroken.",
          "When the surface ends, walk to the nearest one that continues it."),
     ]),
    ("Follow at a Distance",
     "Ethical, gentle, at-a-distance people-watching. A borrowed direction, nothing more.",
     [
      (2, "Follow the next person wearing blue, from a distance, until they turn a corner.",
          "A respectful distance. You're a shadow, not a tail."),
      (1, "Pick someone walking a dog ahead of you and match their pace for one block.",
          "The dog won't mind. It's used to being interesting."),
      (3, "Follow someone until they stop for any reason, then continue on your own from wherever that was.",
          "A red light, a shop window, a phone call — any stop counts. Peel off after."),
      (2, "Choose the next person who looks like they know exactly where they're going, and follow their confidence for two minutes.",
          "You're not copying their route. You're borrowing their certainty."),
      (1, "Follow whoever is walking fastest within view, until they're gone.",
          "You don't have to match their speed. Just their direction."),
      (3, "Follow the next cyclist you see, on foot, for as long as you reasonably can.",
          "You will lose them quickly. That's fine — note where you lost them."),
      (2, "Pick someone carrying something interesting — a bag, an instrument, flowers — and let their path be yours for a few minutes.",
          "Curiosity about the object is allowed. Following them home is not."),
      (1, "Follow the next person who checks their phone, until they put it away.",
          "This one usually doesn't take long. Have a backup plan ready."),
      (2, "Watch which way the next person glances before crossing a street, and cross the same way.",
          "Their glance is a tiny decision. Borrow it."),
      (3, "Follow two strangers walking together, at a distance, until their conversation — or their path — ends.",
          "You're not eavesdropping. You're just walking the same way, coincidentally."),
     ]),
    ("Time Limits",
     "The clock decides when the walk turns. You just keep your feet moving.",
     [
      (3, "Walk for exactly 8 minutes, then turn around and walk home a completely different way.",
          "Set a timer. The turnaround is non-negotiable, even mid-step."),
      (1, "Walk in one direction for 3 minutes, then decide what happens next once you stop.",
          "Three minutes is shorter than it feels. Don't check the clock early."),
      (2, "Give yourself exactly 15 minutes to reach somewhere you've never been, using any route.",
          "It doesn't have to be far. New counts more than distant."),
      (1, "Walk for 60 seconds, stop completely, and just look around before continuing.",
          "A full minute of walking is longer than you think — don't rush it."),
      (3, "Set a timer for 20 minutes. Walk until it rings, no matter where that leaves you, then find your own way home.",
          "This is the closest thing to genuinely getting lost on purpose."),
      (2, "Walk for exactly 5 minutes toward the tallest thing you can see.",
          "A building, a crane, a tree. It'll probably take longer to reach than five minutes — that's fine."),
      (1, "Give yourself 2 minutes to find somewhere to sit, then sit there for 2 more.",
          "A bench, a step, a curb. The sitting matters as much as the finding."),
      (2, "Walk for 10 minutes without checking the time once — guess when it's up.",
          "You'll be off. Log both the guess and the real number."),
      (3, "Alternate one minute walking, one minute standing completely still, for as long as you can keep track.",
          "The standing-still minutes are the hard part. Let people wonder about you."),
      (2, "Walk until you've counted to 100 steps, then pick a new direction.",
          "Count out loud or in your head. Losing count means starting the count over, not the walk."),
     ]),
    ("Reverse Instructions",
     "Undo your own habits. Walk the walk you'd never normally choose.",
     [
      (3, "Walk your usual route to somewhere familiar, but backwards — start from the destination and retrace it in reverse, step by step.",
          "Everything looks different walking toward what's usually behind you."),
      (2, "Walk normally for five minutes, then retrace your exact steps back to where you started.",
          "Try to remember the actual path — not just the general direction."),
      (1, "Walk backward, safely and slowly, for as long as you comfortably can.",
          "Find a straight, empty stretch. Glance back often. Safety beats commitment here."),
      (3, "Pick a walk you've done a hundred times and do the opposite of every instinct — turn where you'd usually go straight, and vice versa.",
          "Your feet will try to autopilot. Catch them and redirect."),
      (2, "Start at what would normally be your endpoint and walk toward what would normally be your start.",
          "Same route, opposite intention. Notice what you see first this way that you never do."),
      (1, "Walk to the last place you can clearly remember visiting, using only memory, no directions.",
          "Getting it slightly wrong is part of the exercise."),
      (2, "Walk away from home first, in any direction, before turning back — stretch the trip by wandering the 'wrong' way before heading in.",
          "The point is delaying arrival, not efficiency."),
      (1, "Take the mirror-image route of a walk you took recently — every left becomes a right.",
          "You don't need the exact same walk. Just flip the turns as you go."),
      (3, "Walk somewhere with the specific goal of getting mildly turned around, then find your way out using only landmarks, not directions.",
          "Pick landmarks you'll actually remember: a red door, a big tree, a mural."),
      (2, "Recall your favorite walk from this book and do the exact opposite instruction on the same street.",
          "If it said turn toward, turn away. If it said follow, ignore."),
     ]),
    ("Weather-Led",
     "Sun, wind, rain, and shade are all willing to give directions.",
     [
      (1, "Walk toward wherever the sun is hitting a wall or building most directly.",
          "Sun-warmed brick has its own smell. See if you notice it."),
      (2, "Walk against the wind for as long as you can stand it, then turn and let it push you home.",
          "The turnaround feels like relief. That's the whole point."),
      (3, "After rain, follow the largest puddles you can find, tracing a path from one to the next.",
          "Reflections count as scenery. Look down as much as up."),
      (1, "On a cloudy day, walk toward the brightest patch of sky.",
          "Even gray has a brighter gray. Trust your eyes."),
      (2, "Walk until you find shade, rest there until you're cool, then walk until you find sun again.",
          "Let your body pick the pace, not the clock."),
      (3, "On a windy day, follow whatever the wind is visibly moving — a flag, a plastic bag, loose leaves — for as long as you can track it.",
          "You'll lose it and find a new one. That's a new instruction, not a failure."),
      (1, "Walk toward the nearest sound of water — a fountain, a sprinkler, a gutter running.",
          "Water finds its way downhill. So can you."),
      (2, "On a cold day, walk the sunniest route you can find, corner by corner.",
          "Your body already knows how to do this. Just follow it on purpose."),
      (3, "Time your walk to a change in weather — leave right as the sky is shifting and walk until the shift is complete.",
          "Check the sky before you check anything else today."),
      (2, "Walk with your face turned toward wherever the air feels different — cooler, warmer, damper — chasing the change.",
          "Micro-weather is real: one corner is always a few degrees off from the last."),
     ]),
    ("Free Wander",
     "No instruction left to give you. The hunt — the walk — is yours now.",
     [
      (0, "No-instruction walk.",
          "Go outside. Walk wherever you want. Log it like you followed a rule anyway."),
      (0, "Five-minute walk.",
          "Short and undirected. Sometimes that's the whole assignment."),
      (0, "Write your own instruction first, then follow it.",
          "Make up a rule as strange as any in this book, then obey it."),
      (0, "Walk somewhere you've never walked before.",
          "Even a street you've only ever driven past counts."),
      (0, "Walk with someone else's instruction.",
          "Ask a friend to make one up for you. Borrowed rules are still rules."),
      (0, "Repeat your favorite instruction from this book, on a different day.",
          "Same instruction, different day, different walk. That's the whole trick."),
      (0, "Walk at a time of day you don't usually go outside.",
          "Early, late, midday lull — pick whichever feels unfamiliar."),
      (0, "Walk your own neighborhood as if you were a visitor seeing it for the first time.",
          "Notice what you'd point out to a stranger."),
      (0, "A walk with no destination and no instruction at all.",
          "This is the whole book, distilled. Just go."),
      (0, "Design tomorrow's walk tonight.",
          "Write the instruction here, follow it when you wake up. Leave yourself something strange to do."),
     ]),
]

assert sum(len(s[2]) for s in SECTIONS) == 70, "prompt count must be exactly 70"
