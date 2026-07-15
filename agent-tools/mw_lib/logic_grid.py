"""Generates verified, uniquely-solvable 3x3 logic grid puzzles."""

import itertools
import random


def _solutions(names, pets, colors, clues):
    """Brute-force every (pet-perm, color-perm) assignment and keep ones matching all clues."""
    valid = []
    for pet_perm in itertools.permutations(range(3)):
        for color_perm in itertools.permutations(range(3)):
            assign = {
                names[i]: {"pet": pets[pet_perm[i]], "color": colors[color_perm[i]]}
                for i in range(3)
            }
            if all(clue["check"](assign) for clue in clues):
                valid.append(assign)
    return valid


def _fact_clues(names, pets, colors, solution):
    """Build the pool of true statements about the solution, each with a natural-language form."""
    clues = []
    for n in names:
        p, col = solution[n]["pet"], solution[n]["color"]
        clues.append({
            "text": f"{n} has the {p}.",
            "check": lambda a, n=n, p=p: a[n]["pet"] == p,
        })
        clues.append({
            "text": f"{n} likes {col}.",
            "check": lambda a, n=n, col=col: a[n]["color"] == col,
        })
        clues.append({
            "text": f"{n} does not have the {[x for x in pets if x != p][0]}.",
            "check": lambda a, n=n, p=p: a[n]["pet"] != [x for x in pets if x != p][0],
        })
    for n in names:
        p, col = solution[n]["pet"], solution[n]["color"]
        clues.append({
            "text": f"Whoever has the {p} likes {col}.",
            "check": lambda a, p=p, col=col: all(a[m]["color"] == col for m in a if a[m]["pet"] == p),
        })
    return clues


def generate_puzzle(names, pets, colors, seed):
    rng = random.Random(seed)
    pet_perm = list(range(3))
    color_perm = list(range(3))
    rng.shuffle(pet_perm)
    rng.shuffle(color_perm)
    solution = {names[i]: {"pet": pets[pet_perm[i]], "color": colors[color_perm[i]]} for i in range(3)}

    pool = _fact_clues(names, pets, colors, solution)
    rng.shuffle(pool)

    chosen = []
    for clue in pool:
        chosen.append(clue)
        sols = _solutions(names, pets, colors, chosen)
        if len(sols) == 1:
            break

    # try to trim any redundant clue while keeping uniqueness
    trimmed = list(chosen)
    for clue in list(trimmed):
        candidate = [c for c in trimmed if c is not clue]
        if len(_solutions(names, pets, colors, candidate)) == 1:
            trimmed = candidate

    final_sols = _solutions(names, pets, colors, trimmed)
    assert len(final_sols) == 1, "puzzle is not uniquely solvable"
    assert final_sols[0] == solution

    return {
        "names": names,
        "pets": pets,
        "colors": colors,
        "clues": [c["text"] for c in trimmed],
        "solution": solution,
    }
