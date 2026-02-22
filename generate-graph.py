#!/usr/bin/env python3
"""
Generate knowledge graph data for the Jekyll site.

Scans all markdown files in docs/ to extract nodes (pages) and edges:
  - shared-tag: two pages that share at least one tag
  - internal-link: a page that contains a markdown link to another page

One edge per unique node pair is created (even if they share multiple tags).
Outputs docs/assets/graph-data.json.

Usage:
    python3 generate-graph.py
"""

import json
import os
import re
from itertools import combinations
import yaml
from pathlib import Path

DOCS_DIR = Path(__file__).parent / "docs"
OUTPUT_FILE = DOCS_DIR / "assets" / "graph-data.json"

# Directories to skip during scan
EXCLUDE_DIRS = {"_site", "_templates", ".jekyll-cache", "vendor", ".bundle", "tags", "assets"}
# Top-level files that are nav/index pages, not content
SKIP_FILES = {"tags.md", "search.md", "graph.md", "index.md"}

# Tags used by more than this many pages are considered "category" tags and are
# skipped when building shared-tag edges, to keep the graph readable.
MAX_SHARED_TAG_PAGES = 6


def extract_front_matter_and_body(file_path):
    """Return (front_matter_dict, body_text) for a markdown file."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as exc:
        print(f"Warning: could not read {file_path}: {exc}")
        return None, ""

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
    if not match:
        return None, content

    try:
        fm = yaml.safe_load(match.group(1))
    except Exception as exc:
        print(f"Warning: could not parse YAML in {file_path}: {exc}")
        return None, match.group(2)

    return fm, match.group(2)


def should_exclude(rel_path):
    """Return True if this path falls inside an excluded directory."""
    for part in rel_path.parts:
        if part in EXCLUDE_DIRS:
            return True
    return False


def infer_type(rel_path, front_matter):
    """Infer content type from front matter or directory structure."""
    ft_type = (front_matter or {}).get("type", "")
    if ft_type:
        return str(ft_type)

    directory_types = {
        "reading": "reading",
        "syntheses": "synthesis",
        "knowledge-base": "knowledge-base",
        "journal": "journal",
        "strange": "strange",
        "survey": "survey",
    }
    top_dir = rel_path.parts[0] if rel_path.parts else ""
    if top_dir in directory_types:
        return directory_types[top_dir]
    if rel_path.name == "references.md":
        return "reference"
    return "other"


def resolve_link(href, source_id):
    """Resolve a relative or absolute markdown href to a page ID string."""
    href = href.strip().split("#")[0].rstrip("/")
    if not href:
        return None
    # Skip external links and Liquid template syntax
    if href.startswith(("http://", "https://", "{", "mailto:")):
        return None
    # Remove .md extension
    href = re.sub(r"\.md$", "", href)
    if href.startswith("/"):
        return href.lstrip("/") or None
    # Resolve relative to the source page's directory
    source_dir = source_id.rsplit("/", 1)[0] if "/" in source_id else ""
    combined = (source_dir + "/" + href) if source_dir else href
    parts = combined.split("/")
    resolved = []
    for part in parts:
        if part == "..":
            if resolved:
                resolved.pop()
        elif part and part != ".":
            resolved.append(part)
    result = "/".join(resolved)
    return result if result else None


def extract_links(body, source_id):
    """Return list of resolved page IDs linked from the markdown body."""
    links = []
    i = 0
    while i < len(body):
        start = body.find("[", i)
        if start == -1:
            break
        end_text = body.find("]", start + 1)
        if end_text == -1 or end_text + 1 >= len(body) or body[end_text + 1] != "(":
            i = start + 1
            continue

        # Parse href with balanced parentheses to handle links like (foo(bar).md)
        j = end_text + 2
        depth = 1
        href_chars = []
        while j < len(body) and depth > 0:
            ch = body[j]
            if ch == "(":
                depth += 1
                href_chars.append(ch)
            elif ch == ")":
                depth -= 1
                if depth > 0:
                    href_chars.append(ch)
            else:
                href_chars.append(ch)
            j += 1

        if depth == 0:
            href = "".join(href_chars)
            resolved = resolve_link(href, source_id)
            if resolved:
                links.append(resolved)
            i = j
        else:
            i = start + 1

    # De-duplicate while preserving first-seen order
    seen = set()
    unique = []
    for link in links:
        if link not in seen:
            seen.add(link)
            unique.append(link)

    return unique


def collect_pages():
    """Scan docs/ and return a list of page dicts."""
    pages = []
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        rel = md_file.relative_to(DOCS_DIR)
        if should_exclude(rel):
            continue
        if md_file.name in SKIP_FILES:
            continue

        fm, body = extract_front_matter_and_body(md_file)
        if fm is None:
            continue
        # Skip section-index / parent-nav pages (has_children: true)
        if fm.get("has_children"):
            continue

        title = fm.get("title", md_file.stem.replace("-", " ").title())
        tags = fm.get("tags", [])
        if not isinstance(tags, list):
            tags = []
        tags = [str(t) for t in tags]

        page_id = str(rel.with_suffix("")).replace(os.sep, "/")
        pages.append(
            {
                "id": page_id,
                "title": str(title),
                "type": infer_type(rel, fm),
                "tags": tags,
                "links": extract_links(body, page_id),
            }
        )
    return pages


def build_edges(pages):
    """
    Build shared-tag and internal-link edges.

    At most one edge is created per ordered or unordered node pair, so pages
    sharing multiple tags still produce a single 'shared-tag' edge.
    """
    page_ids = {p["id"] for p in pages}
    edges = []
    # Separate sets so shared-tag edges are undirected, while internal-link
    # edges are directed (A -> B distinct from B -> A).
    shared_edge_set = set()
    link_edge_set = set()

    # --- shared-tag edges ---
    tag_to_ids = {}
    for page in pages:
        for tag in page["tags"]:
            tag_to_ids.setdefault(tag, []).append(page["id"])

    shared_pair_tags = {}
    for tag, ids in tag_to_ids.items():
        # Skip hub/category tags that appear on many pages — they would
        # create O(n²) edges that add noise without topical signal.
        if len(ids) > MAX_SHARED_TAG_PAGES:
            continue
        unique_ids = sorted(set(ids))
        for a, b in combinations(unique_ids, 2):
            key = tuple(sorted((a, b)))
            shared_edge_set.add(key)
            shared_pair_tags.setdefault(key, set()).add(tag)

    for a, b in sorted(shared_edge_set):
        tags = sorted(shared_pair_tags.get((a, b), set()))
        edges.append(
            {
                "source": a,
                "target": b,
                "type": "shared-tag",
                "tags": tags,
                "tag_count": len(tags),
            }
        )

    # --- internal-link edges ---
    for page in pages:
        for target in page["links"]:
            if target in page_ids and target != page["id"]:
                key = (page["id"], target)
                if key not in link_edge_set:
                    link_edge_set.add(key)
                    edges.append(
                        {
                            "source": page["id"],
                            "target": target,
                            "type": "internal-link",
                        }
                    )

    return edges


def main():
    print("=" * 60)
    print("Generating knowledge graph data")
    print("=" * 60)

    pages = collect_pages()
    print(f"  Scanned {len(pages)} content pages")

    edges = build_edges(pages)
    tag_edges = sum(1 for e in edges if e["type"] == "shared-tag")
    link_edges = sum(1 for e in edges if e["type"] == "internal-link")
    print(
        f"  Built {len(edges)} edges  "
        f"({tag_edges} shared-tag, {link_edges} internal-link)"
    )

    nodes = [
        {
            "id": p["id"],
            "label": p["title"],
            "type": p["type"],
            "tags": p["tags"],
        }
        for p in pages
    ]
    graph_data = {"nodes": nodes, "edges": edges}

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        json.dump(graph_data, fh, indent=2)

    print(f"  Written → {OUTPUT_FILE}")
    print()
    print("Run 'make graph' to regenerate whenever content changes.")


if __name__ == "__main__":
    main()
