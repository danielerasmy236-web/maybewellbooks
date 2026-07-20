"""Content data for 'Space STEM Pack' (id: stem, cat: stem)."""

TITLE = "Space\nSTEM Pack"
SUBTITLE = "Twelve hands-on projects for future astronomers and engineers"
TAGLINE = "no kit required."
ACCENT = "SLATE"

INTRO_BODY = [
    "Every project here does real science with paper, a pencil, and",
    "sometimes scissors and sunlight.",
    "",
    "Some pages are math. Some are charts you fill in over real nights",
    "outside. Some are things you build. None of them need a kit.",
    "",
    "Teacher and parent notes are in the back — what each project",
    "teaches, and how long it usually takes.",
]

PROJECTS = [
    {"n": 1, "title": "Build a Paper Sundial", "type": "sundial",
     "brief": "Cut out the gnomon (the triangle) and fold it upright along the dashed line on the dial. "
              "Set it outside facing true north, and check it every hour on a sunny day."},
    {"n": 2, "title": "Chart the Big Dipper", "type": "constellation", "stars": "big_dipper",
     "brief": "Connect the stars in order to trace the Big Dipper, part of the constellation Ursa Major. "
              "Look for it in the northern sky after dark."},
    {"n": 3, "title": "Chart Orion", "type": "constellation", "stars": "orion",
     "brief": "Orion the Hunter is one of the easiest constellations to find — look for three stars "
              "in a short, straight line. That's his belt."},
    {"n": 4, "title": "Chart Cassiopeia", "type": "constellation", "stars": "cassiopeia",
     "brief": "Cassiopeia looks like a wide letter W (or M, depending which way is up). It's visible "
              "year-round from most of the northern hemisphere."},
    {"n": 5, "title": "Moon Phase Wheel", "type": "moonwheel",
     "brief": "Color each moon shape to match its phase name, then cut out the wheel and the window "
              "card, and pin them together in the center so the wheel spins."},
    {"n": 6, "title": "Rocket Math: Fuel Check", "type": "mathsheet", "problems": "fuel",
     "brief": "Real rockets are mostly fuel by weight. Work through the problems to see just how much."},
    {"n": 7, "title": "Rocket Math: Countdown", "type": "mathsheet", "problems": "countdown",
     "brief": "Practice the kind of quick arithmetic mission control does under pressure."},
    {"n": 8, "title": "Build a Star Finder", "type": "starfinder",
     "brief": "Cut out the wheel and the cover, layer them, and rotate to the current month and time — "
              "the oval window shows which constellations are up tonight."},
    {"n": 9, "title": "Scale of the Solar System", "type": "scale",
     "brief": "If the Sun were the size shown here, how far away would each planet really be? Fill in "
              "your guesses before checking the answers at the bottom."},
    {"n": 10, "title": "Design Your Own Spacecraft", "type": "design",
     "brief": "Every spacecraft needs to solve the same problems: power, life support, propulsion, "
              "and coming home. Label your design."},
    {"n": 11, "title": "Gravity Drop Experiment", "type": "experiment",
     "brief": "Drop two different objects from the same height at the same time. Record what you "
              "predicted and what actually happened."},
    {"n": 12, "title": "Name Your Own Constellation", "type": "namestars",
     "brief": "Connect these unnamed stars into a shape, give it a name, and write the myth behind it."},
]

CONSTELLATIONS = {
    "big_dipper": {
        "label": "The Big Dipper",
        "points": [(0.08, 0.42), (0.24, 0.5), (0.4, 0.44), (0.56, 0.4), (0.56, 0.62), (0.76, 0.68), (0.92, 0.5)],
    },
    "orion": {
        "label": "Orion",
        "points": [(0.25, 0.85), (0.75, 0.85), (0.65, 0.15), (0.35, 0.15), (0.4, 0.5), (0.5, 0.47), (0.6, 0.44)],
    },
    "cassiopeia": {
        "label": "Cassiopeia",
        "points": [(0.05, 0.35), (0.28, 0.7), (0.5, 0.3), (0.72, 0.7), (0.95, 0.25)],
    },
}

FUEL_PROBLEMS = [
    "A rocket weighs 2,970,000 kg fully fueled. Empty, it weighs 130,000 kg. How many kg of fuel is that?",
    "If fuel burns at 8,400 kg per second, how many seconds until the tank above is empty?",
    "A smaller rocket carries 45,000 kg of fuel and uses 15,000 kg per stage. How many stages can it fuel?",
    "Mission control needs a 12% fuel reserve on a 60,000 kg fuel load. How many kg is the reserve?",
]

COUNTDOWN_PROBLEMS = [
    "T-minus 45 seconds. A system check takes 12 seconds. How many seconds remain after the check?",
    "Three checks of 8 seconds each must finish before T-minus 10. What's the latest they can start?",
    "The countdown holds for 90 seconds at T-minus 20. What is the new T-minus after the hold ends and 90 more seconds pass?",
]

SCALE_ROWS = [
    ("Sun", "the size of a beach ball"),
    ("Mercury", "a peppercorn, 12 steps away"),
    ("Venus", "a pea, 22 steps away"),
    ("Earth", "a pea, 30 steps away"),
    ("Mars", "a peppercorn, 46 steps away"),
    ("Jupiter", "a grapefruit, 155 steps away"),
    ("Saturn", "an orange, 287 steps away"),
]

EXPERIMENT_TABLE_ROWS = ["Object 1", "Object 2", "Object 3"]

TEACHER_NOTES = [
    ("Projects 1, 5, 8", "Best done a day ahead — sundial and star finder need daylight or a clear night to test."),
    ("Projects 2-4, 12", "No equipment needed. Great for a car ride or a waiting room."),
    ("Projects 6-7, 9", "Calculator optional but not required — numbers are chosen to stay simple."),
    ("Project 10", "No wrong answers. Encourage kids to explain their choices out loud."),
    ("Project 11", "Needs two small objects of different weight and a safe place to drop them."),
]
