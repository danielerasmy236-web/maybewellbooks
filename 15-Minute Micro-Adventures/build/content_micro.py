"""All written content for 15-Minute Micro-Adventures (Micro-Aventuras de 15
Minutos).

Field Notes line, Volume Four. Template B, compact variant: no sections, no
dividers — 80 flat missions tagged by setting (IN / OUT / ANY) instead of
chapters, sized for real dead time (a bus stop, a work break). Voice: DWYI's
curious/wondrous/never-childish, same ★ difficulty system as TWIW/Wander.
"""

TITLE = "15-Minute\nMicro-Adventures"
TITLE_LINES = ["15-Minute", "Micro-Adventures"]
SUBTITLE = "Missions Built to Finish Before the Moment Passes"
TAGLINE = "dead time isn't dead."
EYEBROW = "FIELD NOTES · VOLUME FOUR"
BADGE = "A POCKET-SIZED BOOK"
HASHTAG = "#MicroAdventures"
SPANISH_NOTE = "Micro-Aventuras de 15 Minutos"

INTRO_TITLE = "Before You Begin"
INTRO_KICKER = "HOW THIS WORKS"
INTRO_PARAS = [
    "The bus is late. The kettle's boiling. The meeting hasn't started yet. "
    "Most of a day is made of these small gaps — and most of us spend them "
    "staring at a phone. This book is for the other option.",
    "This book works in one move:",
    ("MISSION", "Each page gives you one small thing to do, right where you "
     "already are. No setup, no supplies, no leaving early. Just look, "
     "notice, or act — then log it and get back to your day."),
    "Missions are tagged by where they work best:",
    ("TAGS", ""),  # placeholder: the generator draws the three tag icons here
    "The stars tell you how much attention a mission asks for:",
    ("STARS", ""),  # placeholder: the generator draws the three star rows here
    "No mission takes longer than the gap you're already standing in. "
    "Start whenever. Stop whenever it's done.",
]

TAG_LEGEND = [
    ("IN", "works indoors — home, office, waiting room"),
    ("OUT", "works outdoors — street, park, bus stop"),
    ("ANY", "works absolutely anywhere"),
]

STAR_LEGEND = [
    (1, "easy — barely slows you down"),
    (2, "some effort — you'll have to actually pay attention"),
    (3, "a real challenge — takes the whole gap, maybe longer"),
]

CLOSING_TITLE = "That's the gap filled."
CLOSING_BODY = "There's another one coming. There always is."
CLOSING_STATS = "80 missions  ·  zero setup  ·"
CLOSING_SHARE = "Share your mission: " + HASHTAG

# (tag, stars, prompt) — flat list, no sections. tag in {"IN","OUT","ANY"}
MISSIONS = [
    ("IN", 1, "Find three things within reach that are the same color."),
    ("OUT", 2, "Strike up a two-sentence conversation with a stranger about the weather."),
    ("ANY", 2, "Find the oldest object visible from where you're standing."),
    ("ANY", 3, "Write down a full conversation you can overhear, word for word, for one minute."),
    ("ANY", 1, "Close your eyes for 60 seconds and count every distinct sound."),
    ("IN", 1, "Find the smallest object in the room and guess its story."),
    ("OUT", 1, "Find a person wearing your favorite color and silently thank them."),
    ("IN", 2, "Rearrange three objects on a nearby surface into a small sculpture."),
    ("OUT", 2, "Count how many different modes of transportation pass in two minutes."),
    ("ANY", 1, "Name five things you can see that are man-made."),
    ("ANY", 1, "Name five things you can see that occur in nature."),
    ("IN", 3, "Find an object that's been in the same place so long nobody notices it anymore."),
    ("OUT", 1, "Find the tallest thing in view. Guess its height out loud."),
    ("ANY", 2, "Text someone a compliment you've been meaning to send."),
    ("IN", 1, "Find something in the room older than you are."),
    ("OUT", 3, "Follow a single cloud with your eyes until it changes shape."),
    ("ANY", 2, "Come up with a two-word nickname for a stranger nearby, kept to yourself."),
    ("IN", 2, "Find a smell in the room and try to name it exactly."),
    ("OUT", 1, "Find a plant growing somewhere it wasn't planted on purpose."),
    ("ANY", 3, "Predict what the next person to walk by will be wearing. Check."),
    ("IN", 1, "Count the light sources in the room."),
    ("OUT", 2, "Find a shadow and guess what time it is from its length."),
    ("ANY", 1, "Think of the first three words that come to mind. Write them down."),
    ("ANY", 2, "Find a sound you can't identify. Guess three possible sources."),
    ("IN", 3, "Memorize the exact position of five objects. Look away. Recall them."),
    ("OUT", 1, "Find a bird. Watch it until it moves."),
    ("ANY", 1, "Notice the last thing you touched before this page. Describe its texture."),
    ("IN", 2, "Find something in the room you've never really looked at closely."),
    ("OUT", 3, "Guess the age of the oldest tree or building in sight."),
    ("ANY", 1, "Take one full minute to just breathe and do nothing else."),
    ("IN", 1, "Find something that makes a satisfying sound when you tap it."),
    ("OUT", 1, "Find a crack in the pavement shaped like something."),
    ("ANY", 2, "Give the next stranger you see a one-word title, like a job description."),
    ("ANY", 3, "Write a six-word story about wherever you are right now."),
    ("IN", 2, "Find the newest object in the room."),
    ("OUT", 1, "Look for a color you didn't expect to see outside today."),
    ("ANY", 1, "Find something within reach that's cold to the touch."),
    ("IN", 3, "Guess how many objects are in the room without counting on your fingers."),
    ("OUT", 2, "Find a person walking with a purpose and imagine where they're headed."),
    ("ANY", 1, "Find the quietest sound you can hear right now."),
    ("IN", 1, "Find a pattern repeating somewhere nearby — tiles, fabric, wallpaper."),
    ("OUT", 3, "Stand still for one minute and notice everything that moves."),
    ("ANY", 2, "Think of a question you've never asked someone you know well. Save it for later."),
    ("IN", 2, "Find an object you could describe without naming its actual use."),
    ("OUT", 1, "Find something you'd only see at this exact time of day."),
    ("ANY", 3, "Write down the exact time. Guess what you'll be doing in exactly one hour."),
    ("IN", 1, "Find something soft within arm's reach."),
    ("OUT", 2, "Find two people who seem to know each other. Guess how."),
    ("ANY", 1, "Notice one thing that's the same about today and yesterday."),
    ("IN", 3, "Find an object and imagine its entire life before it got here."),
    ("OUT", 1, "Find a piece of litter and imagine one honest story for how it got there."),
    ("ANY", 2, "Name a smell you associate with exactly where you are right now."),
    ("IN", 1, "Find the brightest object in the room."),
    ("OUT", 3, "Watch traffic — foot or vehicle — for one minute. Guess the average speed."),
    ("ANY", 1, "Find something within reach that reminds you of a place you've never been."),
    ("IN", 2, "Find an object that doesn't belong to you but you wish did."),
    ("OUT", 1, "Find a window and guess what's on the other side without looking."),
    ("ANY", 3, "Hold completely still and let someone else move first. Notice who does."),
    ("IN", 1, "Find something you could fix in under ten seconds."),
    ("OUT", 2, "Find the wind. Which direction is it coming from?"),
    ("ANY", 1, "Find one thing that's exactly the temperature you'd expect it to be."),
    ("IN", 3, "Find an object and invent a rule for how it must always be used."),
    ("OUT", 1, "Find a puddle, drain, or gutter and guess where the water goes."),
    ("ANY", 2, "Notice the last thing that made you laugh, even a little."),
    ("IN", 1, "Find something in the room that's a gift from someone."),
    ("OUT", 3, "Follow one person's footsteps with your eyes until they're out of sight."),
    ("ANY", 1, "Find something you're grateful is nearby right now."),
    ("IN", 2, "Find the object closest to the door. Guess who touches it most."),
    ("OUT", 1, "Find a sign and read it as if it were a poem."),
    ("ANY", 3, "Notice three sounds happening at once. Name the loudest, then the faintest."),
    ("IN", 1, "Find something you could hide in one hand."),
    ("OUT", 2, "Watch a vehicle until it turns a corner or disappears from view."),
    ("ANY", 1, "Find something that's been the same color your whole life."),
    ("IN", 3, "Guess the last time someone cleaned the space you're in."),
    ("OUT", 1, "Find the shortest shadow in view."),
    ("ANY", 2, "Think of one thing you're looking forward to today. Say it out loud, quietly."),
    ("IN", 1, "Find the object you'd grab first if you had to leave in ten seconds."),
    ("OUT", 3, "Find a stranger's routine in progress and guess what happens next in it."),
    ("ANY", 1, "Notice how your body feels right now, without changing anything about it."),
    ("ANY", 3, "Look at the time. In exactly two minutes, notice what's different."),
]

assert len(MISSIONS) == 80, "prompt count must be exactly 80"
