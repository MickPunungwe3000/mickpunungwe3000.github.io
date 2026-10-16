"""Create a private article without overwriting existing work."""
import argparse
import json
from pathlib import Path
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("slug")
parser.add_argument("title")
args = parser.parse_args()
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
    parser.error("Use a lowercase slug containing letters, digits and single hyphens.")
root = Path(__file__).resolve().parents[1]
path = root / "_drafts" / (args.slug + ".md")
path.parent.mkdir(exist_ok=True)
content = "---\ntitle: " + json.dumps(args.title, ensure_ascii=False) + "\npublished: false\nlayout: single\ndescription: \"\"\ncategories: []\ntags: []\n---\n\n[AUTHOR INPUT REQUIRED: State your main argument and intended audience.]\n\n[VERIFY: Add authoritative sources and check examples before drafting.]\n"
try:
    with path.open("x", encoding="utf-8") as draft:
        draft.write(content)
except FileExistsError:
    parser.error("Draft already exists; no files changed.")
print(path)
