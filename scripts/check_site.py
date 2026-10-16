"""Validate a generated Jekyll site without third-party Python dependencies."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.canonical = []
        self.description = False
        self.has_title = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "title":
            self.has_title = True
        if tag == "meta" and attrs.get("name") == "description":
            self.description = bool(attrs.get("content", "").strip())
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href", ""))
        if tag in ("a", "link") and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in ("img", "script") and attrs.get("src"):
            self.links.append(attrs["src"])

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("site", nargs="?", default="_site")
parser.add_argument("--origin", default="http://localhost:4000", help="Origin used by this build")
parser.add_argument("--forbid", action="append", default=[], help="Private marker that must not occur anywhere in output")
args = parser.parse_args()
site = Path(args.site).resolve()
if not (site / "index.html").is_file():
    parser.error("No generated index.html; run Jekyll build first")
errors, warnings, pages = [], [], {}
for path in site.rglob("*.html"):
    page = Page()
    page.feed(path.read_text(encoding="utf-8"))
    pages[path] = page
    for field, present in (("title", page.has_title), ("description", page.description), ("canonical", len(page.canonical) == 1)):
        if not present:
            errors.append(f"{path.relative_to(site)}: missing or duplicate {field}")
    if len(page.canonical) == 1:
        canonical = urlsplit(page.canonical[0])
        if canonical.scheme not in ("http", "https") or canonical.netloc != urlsplit(args.origin).netloc:
            errors.append(f"{path.relative_to(site)}: canonical origin differs from build origin")
for path, page in pages.items():
    rel = path.relative_to(site).as_posix()
    url = "/" + (rel[:-10] if rel.endswith("index.html") else rel)
    for link in page.links:
        target_url = urlsplit(urljoin(args.origin.rstrip("/") + url, link))
        if target_url.scheme not in ("http", "https") or target_url.netloc != urlsplit(args.origin).netloc:
            continue
        target = site / unquote(target_url.path).lstrip("/")
        if target.is_dir():
            target = target / "index.html"
        if not target.is_file():
            errors.append(f"{rel}: broken local reference {link}")
        elif target_url.fragment and target in pages and unquote(target_url.fragment) not in pages[target].ids:
            warnings.append(f"{rel}: missing fragment {link}")
for name in ("feed.xml", "sitemap.xml"):
    path = site / name
    if not path.is_file():
        errors.append("Missing " + name)
    else:
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"{name}: invalid XML: {exc}")
for name in ("editorial", "scripts", "AGENTS.md", "_config.preview.yml", "_site-preview"):
    if (site / name).exists():
        errors.append("Private source leaked into output: " + name)
for path in site.rglob("*"):
    if path.is_file() and path.suffix in (".html", ".xml", ".json", ".js", ".md", ".txt"):
        content = path.read_text(encoding="utf-8", errors="replace")
        for marker in args.forbid:
            if marker in content:
                errors.append(f"{path.relative_to(site)}: private marker {marker} found")
for warning in sorted(set(warnings)):
    print("WARN " + warning)
for error in sorted(set(errors)):
    print("ERROR " + error)
print(f"Checked {len(pages)} HTML pages: {len(set(errors))} errors, {len(set(warnings))} warnings.")
raise SystemExit(bool(errors))
