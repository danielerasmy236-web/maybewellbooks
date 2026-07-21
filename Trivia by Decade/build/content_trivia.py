"""All written content for Trivia by Decade (Trivia con Profundidad).

For Every Chapter line. Template B, four decade sections (1950s-1980s,
range confirmed by Dan 2026-07-20), 15 questions each. Questions reward
specific lived memory — personal experience shapes most answers, so the
"answer notes" at the back are typical-answer guidance and discussion
anchors, not a single textbook answer.
"""

CFG = {
    "EYEBROW": "FOR EVERY CHAPTER · A LARGE-PRINT TRIVIA BOOK",
    "TITLE_LINES": ["Trivia", "by Decade"],
    "SUBTITLE": "Sixty Questions That Reward Having Actually Been There",
    "SPANISH_NOTE": "Trivia con Profundidad",
    "BADGE": "A LARGE-PRINT BOOK",
    "TAGLINE": "you had to be there. you were.",
}

INTRO_KICKER = "HOW TO PLAY"
INTRO_TITLE = "Earned, Not Tested"
INTRO_PARAS = [
    "This is not the kind of trivia anyone can look up. Most of these "
    "questions have no single right answer — they have YOUR answer, the "
    "one you earned by being there.",
    ("ALONE", "Write your answers on the lines. Check the answer notes at "
     "the back for what most people say — then enjoy where your memory "
     "disagrees."),
    ("ALOUD", "Read questions to the room and let people call out answers. "
     "The arguments are the game. Score if you want; nobody ever does for "
     "long."),
    ("COMPARE", "Prices, phrases, and habits differed by town and family. "
     "When two answers clash, you've found the best conversation on the "
     "page."),
    "Four decades, fifteen questions each. Start with the decade you knew "
    "best — or the one you want to argue about.",
]

# (decade title, divider note, [questions]) — 15 each.
SECTIONS = [
    ("The 1950s",
     "Radio evenings, nickel candy, and the first TV on the block.",
     [
      "What was a common thing to say when answering the phone before caller ID existed?",
      "Name a household chore that took real physical effort then but is now automated.",
      "What was a typical price for a loaf of bread in this decade, in your area?",
      "What did your family call the evening meal — dinner or supper — and what time was it served?",
      "What was considered a \"modern\" kitchen appliance in this decade?",
      "What did a soda fountain sell besides soda — and what did you order?",
      "How did you find out school was closed for bad weather?",
      "What toys could you make yourself, with things found around the house?",
      "What did families do together in the evening before most homes had a television?",
      "What did you wear to school that no child would recognize today?",
      "Who in your neighborhood had the first TV set — and did you go watch it?",
      "What did the milkman, iceman, or door-to-door salesman bring to your street?",
      "What songs did adults consider scandalous that seem tame now?",
      "What could a nickel or a dime actually buy you?",
      "What's a slang word from this decade that's completely fallen out of use?",
     ]),
    ("The 1960s",
     "Transistor radios, drive-ins, and the whole world changing at once.",
     [
      "Where were you when you heard the biggest news story of this decade — and how did you hear it?",
      "What was your first record, and where did you buy it?",
      "What did your school consider a dress-code violation?",
      "What appliance arrived in your home this decade and changed everything?",
      "What slang did you use that your parents couldn't stand?",
      "How did you arrange to meet friends with no way to call ahead?",
      "What was a night at the drive-in actually like — food, sound, and all?",
      "What did a first date typically cost, and what did you do?",
      "What hairstyle did you or your friends wear that took real work to maintain?",
      "What was on your family's table on an ordinary weeknight?",
      "What black-and-white show did your family never miss?",
      "Do you remember watching the Moon landing — where, and with whom?",
      "What job did you or your friends have that barely exists now?",
      "What was the first car you rode in that felt genuinely fancy?",
      "What rule at home was non-negotiable that would surprise kids today?",
     ]),
    ("The 1970s",
     "Long lines, loud music, and doing it yourself because you had to.",
     [
      "What did you do while waiting in lines before phones filled every silence?",
      "What was the family car, and how many people could you actually fit in it?",
      "What did gas cost when you first paid for it yourself — and do you remember the gas lines?",
      "What music did you play loud when no one else was home?",
      "What did you wear then that you'd never admit to now?",
      "How did your family get the news — which paper, which anchor, which hour?",
      "What fad swept through and vanished — pet rocks, mood rings, CB radio?",
      "What did a full night out cost — movie, dinner, dancing?",
      "What did you cook from a box or can that felt modern at the time?",
      "What was your first job interview like — what did you wear, what were you asked?",
      "Which household repair did people do themselves that they'd hire out today?",
      "What TV moment did everyone talk about the next morning?",
      "How did long-distance calls work in your family — who could make them, and when?",
      "What did you save up for the longest — and was it worth it?",
      "What's a smell that instantly means the 1970s to you?",
     ]),
    ("The 1980s",
     "Answering machines, mixtapes, and the mall in its prime.",
     [
      "What did you think of the first personal computer you ever saw — and where did you see it?",
      "How did you make a mixtape — and who did you make one for?",
      "What did renting a movie involve, start to finish?",
      "What style of this decade required hairspray, shoulder pads, or neon?",
      "What did an answering machine change about your household?",
      "What slang from this decade would confuse your grandchildren completely?",
      "What was the mall like in its prime — where did you go first?",
      "What news event of this decade do you remember watching live?",
      "What did you drive in this decade, and what did it cost to fill the tank?",
      "What was the first thing you ever cooked in a microwave?",
      "Which arcade or video game did you get good at — or watch someone play for hours?",
      "What did \"dressing up for a flight\" mean — and when did it stop?",
      "What music did the young people around you play that you secretly liked?",
      "What did concert tickets cost — and which show do you still talk about?",
      "By the end of this decade, what invention could you no longer imagine living without?",
     ]),
]

# Answer notes: one terse typical-answer / discussion anchor per question,
# aligned by index with SECTIONS above.
ANSWER_NOTES = [
    [
     "Usually the family surname: \"Smith residence\" — or just the phone number.",
     "Common answers: wringer laundry, beating rugs, hand-washing dishes, shoveling coal.",
     "Mid-decade, roughly 15-20 cents in much of the US — regional spread is the fun part.",
     "\"Supper\" in the country, \"dinner\" in town — and usually earlier than anyone eats now.",
     "Electric refrigerators, chest freezers, mixers — the dishwasher if you were fancy.",
     "Malts, phosphates, egg creams, sundaes — plus comic books by the rack.",
     "You didn't, until the radio said so — or a neighbor kid knocked.",
     "Slingshots, stilts, kites, rag dolls, scooters from crates and skate wheels.",
     "Radio programs, cards, board games, front porches, and going visiting.",
     "Common: dresses or skirts required for girls; boys in slacks — never denim.",
     "Whoever it was, half the block found a reason to visit at eight o'clock.",
     "Milk in glass bottles, block ice, brushes, encyclopedias, vacuum demonstrations.",
     "Early rock and roll — Elvis's hips scandalized a generation of parents.",
     "Candy bars, a phone call, a comic book; a dime got you a soda or the matinee.",
     "\"Swell,\" \"keen,\" \"made in the shade,\" \"daddy-o\" — collect the room's list.",
    ],
    [
     "Most rooms split between the Kennedy assassination and the Moon landing.",
     "45s from a five-and-dime, department store, or the local record shop.",
     "Hair over the collar for boys; skirts above the knee for girls.",
     "Color TV, automatic washers, dishwashers — the second car in the driveway.",
     "\"Groovy,\" \"far out,\" \"outta sight\" — ask who still says one of them.",
     "You made a plan and kept it — or rode past their house to check.",
     "Speaker on the window, kids in pajamas in the back seat, snack bar at intermission.",
     "A few dollars covered a movie and burgers — many remember under $5 total.",
     "Beehives and bouffants — sponge rollers, sleeping sitting up, a can of spray.",
     "Meatloaf, casseroles, pot roast on Sunday — Jell-O salad optional but likely.",
     "Ed Sullivan, Bonanza, Andy Griffith, The Twilight Zone — expect a debate.",
     "July 20, 1969 — most remember the room, the set, and who was beside them.",
     "Elevator operator, gas station attendant, telephone operator, paper route.",
     "Anything with fins or a name like Imperial, Riviera, Continental.",
     "Home when the streetlights came on; church clothes stayed on till supper.",
    ],
    [
     "Talked to strangers, read whatever was in reach, or just waited — a lost skill.",
     "Station wagons ruled — and the answer to \"how many kids fit\" was \"all of them.\"",
     "Around 36-60 cents through the decade; the 1973-74 lines nobody forgets.",
     "Answers run from Led Zeppelin to ABBA to the Eagles — the split IS the game.",
     "Bell-bottoms, platform shoes, leisure suits, wide collars over wider lapels.",
     "One paper, one anchor — Cronkite for many — and the six o'clock hour.",
     "Pet rocks, mood rings, streaking, CB radio — \"breaker one-nine\" gets a laugh.",
     "Many remember $10-15 covering a whole evening for two.",
     "Hamburger Helper, TV dinners, onion-soup dip, anything \"instant.\"",
     "A suit or your Sunday best, a firm handshake, and \"When can you start?\"",
     "Cars, plumbing, appliances — the garage was full of tools that got used.",
     "The M*A*S*H finale is 1983 — this decade it's Roots, All in the Family, the moon buggy.",
     "After 5 p.m. or Sunday only, timed with an egg timer, and Mom hovering.",
     "A car, a stereo system, a color TV — the layaway counter remembers.",
     "Shag carpet, wood paneling, cigarette smoke, and gasoline at full-service pumps.",
    ],
    [
     "Common firsts: an Apple II or Commodore 64 at school, a friend's TRS-80.",
     "Two tape decks, a finger on pause, and a crush who never knew the effort.",
     "Membership card, aisles of boxes, \"Be kind, rewind,\" and late fees.",
     "Big hair, shoulder pads, leg warmers, neon everything — often all at once.",
     "You could finally leave the house — and screen calls you didn't want.",
     "\"Gnarly,\" \"grody,\" \"gag me with a spoon,\" \"totally tubular.\"",
     "Food court first or record store first — the answer says everything.",
     "The Challenger disaster and the Berlin Wall coming down lead most lists.",
     "K-cars, minivans, hatchbacks — and a full tank often under $15.",
     "Popcorn, then everything — many admit to microwaved scrambled eggs.",
     "Pac-Man, Donkey Kong, Space Invaders — a quarter at a time.",
     "Jackets and dresses for the airport — most say it faded by the 1990s.",
     "Michael Jackson, Madonna, Prince — someone will confess to all three.",
     "Many remember $15-25 tickets for shows people still brag about seeing.",
     "The microwave, the VCR, the answering machine — cable TV closes the vote.",
    ],
]

for s, n in zip(SECTIONS, ANSWER_NOTES):
    assert len(s[2]) == 15 and len(n) == 15

CLOSING_TITLE = "The best answers weren't in here."
CLOSING_BODY = "They were in the room, the whole time."
CLOSING_STATS = "60 questions  ·  4 decades  ·"
