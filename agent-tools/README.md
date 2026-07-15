# PDF Factory — Maybewell Books

A narrowly-scoped local agent whose only job is: generate the next planned
PDF product, once a week, and leave it for human review. It never touches
git, Netlify, or the live site.

## How it works

- `catalog_manifest.json` — the queue. 7 products, taken from the
  placeholder catalog already baked into the site's shop UI. Each has a
  `status`: `pending` or `generated`.
- `run_next.py` — picks the first `pending` item, calls its generator,
  saves the PDF to `../New Products - Pending Review/`, and marks it
  `generated` in the manifest.
- `run_weekly.sh` — thin wrapper that sets up the Python environment
  (via `uv`) and calls `run_next.py`. This is what launchd actually runs.
- `mw_lib/` — shared building blocks: brand colors/cover/section templates
  (`brand.py`), maze generation (`mazes.py`), word search grids
  (`word_search.py`), logic grid puzzles with a real solver that
  guarantees a unique solution (`logic_grid.py`), paper game boards
  (`game_boards.py`), autumn nature icons (`autumn_shapes.py`).
- `content/` — all the actual writing (prompts, word lists, puzzle
  themes, game rules) as plain data, so `run_next.py` never needs an LLM
  call at runtime.
- `generators/` — one script per product, assembling content + `mw_lib`
  into a finished PDF.

## The schedule

A macOS LaunchAgent (`~/Library/LaunchAgents/com.maybewellbooks.pdffactory.plist`)
runs `run_weekly.sh` every **Monday at 9:00 AM**, as long as this Mac is on.
If the Mac is asleep or off at that time, launchd runs it at the next
opportunity rather than skipping it.

Useful commands:

```bash
# check it's loaded
launchctl list | grep maybewellbooks

# see recent activity
cat "agent-tools/logs/run_log.txt"

# run it manually right now, without waiting for Monday
cd agent-tools && ./run_weekly.sh

# turn it off
launchctl unload ~/Library/LaunchAgents/com.maybewellbooks.pdffactory.plist

# turn it back on
launchctl load ~/Library/LaunchAgents/com.maybewellbooks.pdffactory.plist
```

## The queue (in order)

1. **Mazes of the Lost City** (puzzles) — generated 2026-07-15, in review.
2. **Space STEM Pack** (stem)
3. **Story Starters** (writing)
4. **The Autumn Book** (seasonal)
5. **Paper Games for Road Trips** (games)
6. **Little Logic Lab** (puzzles)
7. **Word Search Safari** (puzzles)

At one per week, the queue finishes in ~6 more weeks. After that, `run_next.py`
logs "queue empty" and does nothing — it will not invent new products on
its own. Add a new entry to `catalog_manifest.json` (and a matching
generator) when you're ready for more.

## Reviewing a new product

Check `New Products - Pending Review/`. Nothing here is committed to git,
pushed, or connected to the live site — that's a deliberate, separate step
you take by hand once you've looked a PDF over.
