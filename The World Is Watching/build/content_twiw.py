"""All written content for The World Is Watching — A Field Guide for Face Hunters.

Prompts are the approved list from the build brief, verbatim. Hints are short
one-liners in the DWYI voice: curious, a little wondrous, never childish.
Stars: 1 = easy, 2 = some effort, 3 = real challenge. 0 = blank template (no rating).
"""

TITLE = "The World\nIs Watching"
SUBTITLE = "A Field Guide for Face Hunters"
TAGLINE = "everything is looking back."
EYEBROW = "FIELD NOTES · VOLUME ONE"
BADGE = "AN OBSERVATION BOOK"
HASHTAG = "#TheWorldIsWatching"

INTRO_TITLE = "Before You Begin"
INTRO_KICKER = "HOW TO HUNT FACES"
INTRO_PARAS = [
    "You've done this your whole life. A socket gasping at the wall. A car "
    "that woke up grumpy. A cloud with an opinion. Scientists call it "
    "pareidolia — the mind's habit of finding faces in things that were "
    "never given one. We're just giving it a name and a place to collect it.",
    "This book works in three moves:",
    ("FIND", "Each page tells you where or how to look. That's all the help "
     "you get, and all you need."),
    ("LOG", "Write down where you found it, and when. A find without a "
     "location is just a doodle. A find with one is a record."),
    ("DRAW", "Put the face in the box. Draw exactly what you saw, or what "
     "the face was clearly about to become. Both count as true."),
    "The stars tell you how hard the hunt is:",
    ("STARS", ""),  # placeholder: the generator draws the three star rows here
    "There is no wrong way to log a find. Faces don't hold still, and "
    "neither do the rules.",
    "Go slowly. Look closer. Everything is looking back.",
]

STAR_LEGEND = [
    (1, "easy — it's probably in the room with you"),
    (2, "some effort — you'll have to go looking"),
    (3, "a real challenge — patience, timing, maybe luck"),
]

CLOSING_TITLE = "Finished? That's not a thing."
CLOSING_BODY = "The world doesn't stop looking back. Keep hunting."
CLOSING_STATS = "80 finds  ·  7 sections  ·"  # the generator draws the infinity mark after this
CLOSING_SHARE = "Share your collection: " + HASHTAG

# (section title, note, [(stars, prompt, hint), ...])
SECTIONS = [
    ("Household Faces",
     "Start where you live. The residents have been waiting.",
     [
      (1, "Find an outlet, switch, or socket that's watching you. Draw its expression.",
          "Two holes and a slot is all a face needs. Check the quiet corners of the room."),
      (2, "Search your kitchen appliances for an angry face.",
          "Toasters hold grudges. Kettles whistle about it."),
      (1, "Find a doorknob or handle with a surprised look.",
          "Round mouths everywhere. Some have been gasping for years."),
      (2, "Look at your bathroom fixtures. Find one that looks worried.",
          "Faucets frown. Drains worry. The mirror has seen it all."),
      (1, "Find a face hiding in the folds of a curtain or towel.",
          "Soft faces rearrange when the window opens. Catch one first."),
      (2, "Search your furniture for a face that looks tired.",
          "Old chairs slump. Handles droop. Wood remembers being a tree."),
      (3, "Find two different objects with faces that seem to be talking to each other.",
          "What would a lamp say to a fan? Draw both sides of the conversation."),
      (1, "Find a face in the pattern of a rug, tile, or wallpaper.",
          "Patterns repeat, but faces hide in the breaks and smudges."),
      (2, "Look inside a drawer or cupboard. Find a face among the clutter.",
          "Faces assemble themselves when nobody tidies."),
      (3, "Find a face that only appears when the light hits an object a certain way.",
          "Come back at a different hour. The face keeps its own schedule."),
      (1, "Find a face in a knot of wood — a table, a door, a floorboard.",
          "Every knot was a branch once. Some of them still look out."),
      (2, "Search your closet. Find a face made by hanging clothes or shadows.",
          "Sleeves make ears. Hangers make shoulders. Shadow does the rest."),
     ]),
    ("Urban Faces",
     "Streets, walls, machines. The city practices its expressions.",
     [
      (1, "Find a window that looks like an eye. Where is it looking?",
          "Follow its gaze. Draw what it's been staring at, too."),
      (2, "Search a building's façade for a full face — two windows and a door.",
          "Buildings wear their faces slowly. Cross the street for the full portrait."),
      (3, "Find a face that only appears from one specific angle.",
          "Move until it appears. One step further and it's gone."),
      (1, "Find a traffic light, sign, or fixture with a face.",
          "Signals blink. Signs stare. Some fixtures never learned to look away."),
      (2, "Search a parking lot for a car that looks surprised or grumpy.",
          "Headlights are eyes. Grilles are mouths. Some cars are furious about it."),
      (2, "Find a manhole cover, drain, or grate with a face.",
          "The street looks up more often than anyone looks down."),
      (3, "Find a face made from two unrelated things — one from a building, one from the street.",
          "A window for one eye, a lamppost for a nose. Cities collage themselves."),
      (1, "Find a mailbox or trash bin with an expression.",
          "Slots and lids — mouths that swallow all day and never chew."),
      (2, "Search a construction site or scaffolding for a hidden face.",
          "Scaffolding makes cheekbones. Tarps make sleeping eyelids."),
      (2, "Find a face in a crack, stain, or patch on a wall or sidewalk.",
          "Damage has a face. Usually a surprised one."),
      (3, "Find a face made by shadows between buildings, only visible at a certain time of day.",
          "Note the time next to your date. This face keeps office hours."),
      (1, "Find a bicycle, scooter, or bench with a face.",
          "Handlebars are eyebrows waiting to be noticed."),
     ]),
    ("Natural Faces",
     "The originals. Nature invented the face and never stopped doodling.",
     [
      (1, "Find a cloud with a face. What expression does it have?",
          "Fast workers, clouds. Sketch quickly — the expression won't hold."),
      (2, "Search tree bark or a tree trunk for a sleeping face.",
          "Old trees sleep standing up. Look at trunk height, then look up."),
      (2, "Find a rock or stone with a face.",
          "The oldest faces on earth. They're in no hurry to be found."),
      (3, "Find a face that only appears when the sun is low (shadow makes the expression).",
          "Golden hour is face hour. The light does the drawing; you do the copying."),
      (1, "Find a face in a puddle, pond ripple, or water reflection.",
          "Water borrows faces from everything above it."),
      (2, "Search a garden or a patch of leaves for a hidden face.",
          "Somewhere between the stems, something is peeking."),
      (1, "Find a face in the grain of a piece of wood or driftwood.",
          "The grain flows around what used to be there. Faces snag in the current."),
      (3, "Find a face made by the arrangement of several small stones or pebbles.",
          "Nobody arranged them. That's the strange part."),
      (2, "Search fallen leaves for a face made by their shapes.",
          "Autumn drops a thousand faces and keeps walking."),
      (3, "Find a face in a root system or tangle of branches.",
          "Tangles hide profiles. Follow one line until it becomes a nose."),
      (1, "Find a face in the pattern of a plant's leaves or petals.",
          "Symmetry helps. Two leaves and one bloom — that's a face."),
      (2, "Search moss or lichen on a wall or rock for a face.",
          "Slow-growing portraits. This one took decades to look at you."),
     ]),
    ("Faces in Motion",
     "Shadows, reflections, things seen for a moment. Fast sketches only.",
     [
      (2, "Find a shadow that makes a face — yours or something else's.",
          "Shadows rehearse expressions all day. Catch one mid-performance."),
      (3, "Find a face that only exists for a few seconds and then disappears.",
          "Draw from memory. Field hunters trust their first impression."),
      (1, "Find a face in a reflection on glass, metal, or a screen.",
          "A dark screen is a mirror that remembers nothing."),
      (2, "Find a face made by steam, smoke, or fog.",
          "Breath-faces. They last about as long as a sigh."),
      (3, "Find a face made entirely of light and shadow — no real edges, just contrast.",
          "Squint until it appears. Then don't blink."),
      (1, "Find a face in the ripples of water when something is dropped in.",
          "Drop a pebble. The water makes a face about it."),
      (2, "Find a face made by two moving things crossing paths for a moment.",
          "A bus passes a lamppost, and for one second — someone."),
      (3, "Find a face in the way light flickers through moving leaves.",
          "Dappled light blinks. Some blinks have eyes."),
      (1, "Find a face in your own shadow on the ground.",
          "You've walked with this stranger your whole life."),
      (2, "Find a face made by a curtain or flag moving in the wind.",
          "Wind gives fabric a temper. Draw the mood, not the cloth."),
      (3, "Find a face that appears only in a photo, not to the naked eye.",
          "Cameras catch what the eye edits out. Check your last few photos."),
      (2, "Find a face in the spray or splash of water.",
          "Freeze it mid-splash: crown, eyes, open mouth."),
     ]),
    ("Food Faces",
     "A short section. Good finds here are rare — and usually delicious.",
     [
      (1, "Before eating something today, look for a face on your plate. Draw it before it disappears.",
          "Breakfast is the most-watched meal of the day."),
      (2, "Find a sad face in the foam of a drink or coffee.",
          "Foam faces sink slowly. Sketch before your next sip."),
      (1, "Find a face in a piece of fruit or vegetable.",
          "Peppers are dramatic. Potatoes have seen things."),
      (2, "Find a face in the arrangement of food on a table.",
          "Nobody set the table to look at you. And yet."),
      (3, "Find a face made by crumbs, spills, or leftovers.",
          "The meal leaves a self-portrait behind."),
      (1, "Find a face in a slice of bread, toast, or a pastry.",
          "Toast is the classic: browned unevenly, watching evenly."),
      (2, "Find a face in the pattern of a plate, mug, or napkin.",
          "Someone decorated the dishes. The face snuck in on its own."),
      (3, "Find a face made by the shadow of food on a table or wall.",
          "Even a face's shadow can have a face. Tilt the lamp."),
     ]),
    ("Nocturnal Faces",
     "After dark, every light is a lantern and every shadow applies for a face.",
     [
      (2, "Find a face that only appears when a light turns on — a lamp, a car.",
          "Flip the switch. Someone arrives."),
      (3, "Find a face made entirely of shadows, with no drawn edges — just light and dark.",
          "The hardest faces to prove. The best ones to draw."),
      (1, "Find a face in a streetlamp, porch light, or lit window at night.",
          "Night lights hold still. Take your time with this one."),
      (2, "Find a face made by headlights on a wall or ceiling.",
          "Passing cars throw faces across the room, then take them away."),
      (3, "Find a face in the stars, or in the way you imagine a constellation.",
          "People have done this for ten thousand years. Add yours to the record."),
      (1, "Find a face in a night-light or the glow of a screen in the dark.",
          "Small lights make gentle faces. Mostly."),
      (2, "Find a face made by moonlight through a window.",
          "The moon draws with a cold pencil. Look on the floor."),
      (3, "Find a face that seems to change expression as a light source moves.",
          "Carry a lamp, a phone, a candle. Watch the face watch you back."),
      (1, "Find a face in the reflection of a lit window on a dark street.",
          "A face made of somebody else's evening."),
      (2, "Find a face hiding in the dark corner of a room, made by shapes and shadow.",
          "It was always there. You just never said hello."),
      (3, "Find a face made by two different light sources overlapping.",
          "Double light makes double shadow. Double shadow makes strange faces."),
      (1, "Find a face in the pattern city lights make from a window or rooftop.",
          "A skyline is a crowd. Find one face in it."),
     ]),
    ("Your Own Collection",
     "Blank field logs. The hunt is yours now.",
     [
      (0, "Indoor find.",
          "Your choice of object — anywhere under a roof counts. No prompt, no rules. Just look."),
      (0, "Outdoor find.",
          "Anything under open sky. Weather counts. Weather especially counts."),
      (0, "Vehicle find.",
          "Cars, bikes, buses, trains — anything that moves people around."),
      (0, "Nature find.",
          "Plants, rocks, water, sky. The oldest hunting grounds."),
      (0, "Kitchen find.",
          "Anywhere food is prepared or stored. Faces gather where crumbs do."),
      (0, "Bathroom find.",
          "Fixtures, tiles, mirrors. A room full of round mouths."),
      (0, "Street find.",
          "Anything found while walking outside. Keep your pace slow."),
      (0, "Night find.",
          "Anything found after dark. Bring patience, not a flashlight."),
      (0, "Reflection find.",
          "Mirrors, glass, water, screens. Faces that borrow other faces."),
      (0, "Texture find.",
          "Fabric, wood grain, stone, patterns. Run your eyes over it like fingertips."),
      (0, "Someone else's find.",
          "Ask a friend or family member to hunt one with you. Log it together."),
      (0, "Free find.",
          "Anywhere, anytime, your rules. The book is yours now."),
     ]),
]

assert sum(len(s[2]) for s in SECTIONS) == 80, "prompt count must be exactly 80"
