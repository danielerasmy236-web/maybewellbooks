"""Weekly PDF-factory orchestrator.

Picks the next pending product from catalog_manifest.json, generates it with
the matching generator module, and saves the PDF into
"MAYBEWELL BOOKS/New Products - Pending Review/" for human review.

Scope, on purpose: this script ONLY generates a PDF and updates the local
manifest/log. It never touches git, Netlify, or the live site — new
products stay local until a person reviews and decides to ship them.

Safe to run repeatedly: if the queue is empty, it logs that and exits 0.
"""

import json
import sys
import os
import importlib
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MANIFEST_PATH = os.path.join(BASE_DIR, "catalog_manifest.json")
REVIEW_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "New Products - Pending Review"))
LOG_PATH = os.path.join(BASE_DIR, "logs", "run_log.txt")

sys.path.insert(0, BASE_DIR)


def log(message):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    line = f"[{stamp}] {message}"
    print(line)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")


def main():
    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)

    pending = [item for item in manifest["queue"] if item["status"] == "pending"]
    if not pending:
        log("Queue empty — no pending products. Nothing to do.")
        return 0

    item = pending[0]
    log(f"Generating '{item['title']}' (id={item['id']}, category={item['category']})...")

    os.makedirs(REVIEW_DIR, exist_ok=True)
    output_path = os.path.join(REVIEW_DIR, f"{item['id']}_v1.0_letter.pdf")

    try:
        module = importlib.import_module(f"generators.{item['generator']}")
        page_count = module.build(output_path)
    except Exception as e:
        log(f"ERROR generating '{item['title']}': {e}")
        return 1

    item["status"] = "generated"
    item["output"] = os.path.relpath(output_path, os.path.join(BASE_DIR, ".."))
    item["page_count"] = page_count
    item["generated_at"] = datetime.datetime.now().isoformat(timespec="seconds")

    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    log(f"Done: '{item['title']}' -> {output_path} ({page_count} pages). Awaiting your review.")

    remaining = [i for i in manifest["queue"] if i["status"] == "pending"]
    if remaining:
        log(f"{len(remaining)} product(s) still queued: " + ", ".join(i["title"] for i in remaining))
    else:
        log("Queue is now empty. All 7 planned products have been generated.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
