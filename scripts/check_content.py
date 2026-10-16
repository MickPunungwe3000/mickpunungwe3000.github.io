"""Dependency-free source checks; historical issues remain visible as warnings."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors, warnings = [], []
files = sorted((root / "_posts").glob("*.md")) + sorted((root / "_drafts").glob("*.md")) + sorted((root / "_projects").glob("*.md"))
for path in files:
    text = path.read_text(encoding="utf-8")
    label = str(path.relative_to(root))
    parts = text.split("---", 2)
    if not text.startswith("---\n") or len(parts) != 3:
        errors.append(label + ": missing frontmatter boundaries")
        continue
    front, body = parts[1:]
    if not re.search(r"^title:\s*\S", front, re.M):
        errors.append(label + ": missing title")
    if path.parent.name == "_drafts" and not re.search(r"^published: false\s*$", front, re.M):
        errors.append(label + ": draft must explicitly set published: false")
    if path.parent.name == "_posts" and not re.search(r"^published: (true|false)\s*$", front, re.M):
        errors.append(label + ": declare publication status explicitly")
    fence = None
    for line in body.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, suffix = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not suffix.strip():
                fence = None
    if fence:
        warnings.append(label + ": unclosed code fence")
    for asset in set(re.findall(r"/assets/[^\s\"'<>)}]+", text)):
        if not (root / asset.lstrip("/")).is_file():
            warnings.append(label + ": missing asset " + asset)
config = (root / "_config.yml").read_text(encoding="utf-8")
for item in ("editorial", "scripts", "AGENTS.md", "_config.preview.yml", "_site-preview"):
    if "  - " + item + "\n" not in config:
        errors.append("Production exclusion missing: " + item)
if "published: false" not in config:
    errors.append("Missing unpublished default; inspect posts scope")
for warning in warnings:
    print("WARN " + warning)
for error in errors:
    print("ERROR " + error)
print(f"Checked {len(files)} content files: {len(errors)} errors, {len(warnings)} warnings.")
sys.exit(bool(errors))
