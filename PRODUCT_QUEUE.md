# Product Queue — Daily Build Batch

_Single source of truth for the daily-product-builder agent. The agent takes
the topmost non-Shipped, non-blocked item each day, builds it through
Figma → PDF → QA, then STOPS for Dan's review. Nothing ships to
maybewellbooks.com without explicit approval in chat._

Status values: `Pending` → `Built (awaiting review)` → `Approved` → `Shipped`.
(If review requests changes: back to `Pending` with a note.)

## Queue status (this batch)

| Day | Product | Line | Format | Status |
|-----|---------|------|--------|--------|
| 1 | Wander Without a Destination | Field Notes | Template B | Pending |
| 2 | The Map You Draw | Field Notes | Template B, single continuous atlas | Pending |
| 3 | 15-Minute Micro-Adventures | Field Notes | Template B, compact | Pending |
| 4 | Questions They Never Ask You | Field Notes | Template B, two-answer format | Pending |
| 5 | Letter to the Future | Field Notes | Template D, correspondence | Pending |
| 6 | The Grandparents' Book | Field Notes | Template E, interview Q&A, large-print | Pending |
| 7 | Looking Up | Field Notes | Template A, field log | Pending |

Remaining backlog after this batch (briefs exist from prior sessions): the
other Field Notes products, the Teachers line follow-ups, and core catalog
items (Mazes/Word Search/Story Starters generators in `agent-tools/`).

## Resolved decisions (do not relitigate)

- **Road Trip Games**: one product only, under Field Notes (Template H —
  game rules + scorecard). The old catalog's "Paper Games for Road Trips"
  is retired/merged into it — do not build both.
- **Postcards from Planets Nobody Found**: build as Option A — pure drawing
  prompts, same pipeline/buyer as the Imagine line (not the STEM hybrid).
  A STEM "Vol. 2" may be revisited later.

---

## Day 1 — Wander Without a Destination ("Camina Sin Rumbo")

Concept: a walk with no destination, guided by playful semi-random
instructions instead of a map — an accessible take on the psychogeography
"dérive".

Structure: 7 sections by instruction type — Turns & Chance, Follow a Sense,
Follow at a Distance (ethical people-watching, e.g. "follow the next person
wearing blue, from a distance, until they turn a corner"), Time Limits,
Reverse Instructions, Weather-Led, Free Wander. Expand each section to a
full prompt complement in DWYI's voice and ★☆☆/★★☆/★★★ difficulty system.

Sample prompts (tone reference):
- ★☆☆ Turn left at the third corner you reach. Keep walking until something makes you stop.
- ★★☆ Walk toward the loudest sound you can hear right now.
- ★★☆ Pick a direction using nothing but which way the wind is blowing.
- ★★★ Walk for exactly 8 minutes, then turn around and walk home a completely different way.
- ★☆☆ Follow the color yellow for as long as you can find it.
- ★★☆ Walk without your phone in your hand for 10 minutes. Notice what you notice.

## Day 2 — The Map You Draw ("El Mapa que Tú Dibujas")

Concept: the reader cartographs their own neighborhood from memory and
observation — personal geography, not literal geography.

Structure: no sections — one continuous 40–50 page personal atlas.
Large-format blank map pages; prompts scattered as marginalia guiding what
to add on each visit.

Sample prompts:
- Mark the place that smells the best on your street.
- Mark somewhere you've walked past 100 times but never entered.
- Mark where you'd hide if you were 8 years old again.
- Mark the loudest spot and the quietest spot within five minutes of home.
- Mark a place that belongs to someone else's memory, not yours.

## Day 3 — 15-Minute Micro-Adventures ("Micro-Aventuras de 15 Minutos")

Concept: missions short enough for real dead time — waiting for a bus, a
work break — designed to complete before the moment passes.

Structure: 80 prompts, no chapters; organized loosely by small setting
icons (indoor / outdoor / anywhere) instead of sections.

Sample prompts:
- ★☆☆ Find three things within reach that are the same color.
- ★★☆ Strike up a two-sentence conversation with a stranger about the weather.
- ★★☆ Find the oldest object visible from where you're standing.
- ★★★ Write down a full conversation you can overhear, word for word, for one minute.
- ★☆☆ Close your eyes for 60 seconds and count every distinct sound.

## Day 4 — Questions They Never Ask You ("Preguntas que Nunca te Hacen")

Concept: a face-to-face conversation manual for dinners, car rides, waiting
rooms — deliberately avoids generic icebreaker clichés in favor of strange,
real, or oddly specific questions.

Structure: 6 sections — Odd & Absurd, Quietly Deep, About the Past, About
Right Now, About Someone Else at the Table, Hypotheticals. Written-answer
format with TWO answer lines per page (two people both answer).

Sample prompts:
- If you had to teach a stranger one skill in 10 minutes, what would you pick?
- What's a smell that instantly takes you back to being a kid?
- What's something you believed as a child that you were embarrassed to unlearn?
- If today had a soundtrack, what's the one song stuck in it?
- What's a rule you follow that you've never explained to anyone?

## Day 5 — Letter to the Future ("Carta al Futuro")

Concept: a personal correspondence manual — letters to open in 1, 5, or 10
years. A physical object meant to be sealed and stored, not scanned.

Structure: 3 sections by time horizon (1 / 5 / 10 years), each with a short
prompt page before its blank letter pages, plus a closing "instructions for
storage" page (where to keep it, who gets it if you forget). Correspondence
template: sealed "open on ___" date field, envelope-style closing flap
graphic.

Sample prompts:
- Before you write: what do you hope has changed by the time you read this? What do you hope hasn't?
- Write to the version of you who's forgotten what today felt like.
- Leave a question for your future self that only they can answer.

## Day 6 — The Grandparents' Book ("El Libro de los Abuelos")

Concept: a structured interview manual for a younger person to
hand-transcribe an older relative's answers — serves the older-adult /
multigenerational segment directly.

Structure: 6 sections — Childhood, Love & Family, Work & Ambition, Hard
Times, Joy & Small Pleasures, Advice for Later. Interview Q&A template:
printed question + generous lined space for a hand-transcribed answer.
Default to large-print type (accessibility approach of the Word Search
Safari line).

Sample prompts:
- What's a game you played as a child that no one plays anymore?
- What's the hardest decision you ever had to make?
- What did you want to be when you were my age, and did it happen?
- What's something you've never told anyone in this family?
- What's one piece of advice you'd want me to remember after you're gone?

## Day 7 — Looking Up ("Mirando Arriba")

Concept: sky-watching field journal — clouds, stars, weather — no app, no
"correct" identification, just looking and logging.

Structure: 4 sections — Clouds, Stars & Night Sky, Weather Moments, Your
Own Sky (blank templates). Field-log template: Find → Log (pin icon
where / calendar icon date — drawn vector icons, not emoji) → Draw,
matching The World Is Watching's three-zone layout.

Sample prompts:
- ★☆☆ Find a cloud with a face. What's its expression?
- ★★☆ Find the brightest star you can see tonight. Log where and when.
- ★★★ Watch the sky change for 10 minutes without looking away. Log what changed.
- ★☆☆ Find a cloud shaped like something ordinary — an animal, an object.
