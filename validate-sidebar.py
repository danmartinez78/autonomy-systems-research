#!/usr/bin/env python3
"""
validate-sidebar.py - Validate sidebar navigation child cap convention.

For each content section (a first-level subdirectory of docs/), this script:
  1. Counts direct-child .md pages that are visible in the sidebar
     (i.e. do NOT have nav_exclude: true in their front matter).
  2. If the total number of content pages exceeds CAP, requires that a
     view-all.md redirect exists in that section directory.
  3. Fails if the number of visible pages exceeds CAP.

Usage:
    python3 validate-sidebar.py [--cap N] [--docs-dir PATH]
"""

import argparse
import os
import sys

import yaml

DEFAULT_CAP = 5
DEFAULT_DOCS_DIR = "docs"

# Directories to skip entirely (not content sections)
SKIP_DIRS = {"_templates", "_site", "tags", ".git"}


def parse_front_matter(filepath):
    """Return the YAML front matter of *filepath* as a dict, or None."""
    try:
        with open(filepath, encoding="utf-8") as fh:
            content = fh.read()
    except OSError:
        return None

    if not content.startswith("---"):
        return None

    end = content.find("\n---", 3)
    if end == -1:
        return None

    try:
        return yaml.safe_load(content[3:end]) or {}
    except yaml.YAMLError:
        return None


def collect_sections(docs_dir):
    """
    Walk *docs_dir* and return a dict keyed by section name (first-level
    subdirectory relative to docs_dir).

    Each value is a dict with:
        parent       - value of the 'parent' front-matter field (or None)
        visible      - list of file paths without nav_exclude: true
        nav_excluded - list of file paths with nav_exclude: true
        has_view_all - True if view-all.md was found in this directory
    """
    sections = {}

    try:
        top_entries = os.listdir(docs_dir)
    except OSError as exc:
        print(f"❌ Cannot read docs directory '{docs_dir}': {exc}")
        sys.exit(1)

    for entry in sorted(top_entries):
        if entry in SKIP_DIRS or entry.startswith("."):
            continue

        section_path = os.path.join(docs_dir, entry)
        if not os.path.isdir(section_path):
            continue

        info = {
            "parent": None,
            "visible": [],
            "nav_excluded": [],
            "has_view_all": False,
        }

        for fname in sorted(os.listdir(section_path)):
            if not fname.endswith(".md"):
                continue

            fpath = os.path.join(section_path, fname)
            if not os.path.isfile(fpath):
                continue

            if fname == "view-all.md":
                info["has_view_all"] = True
                continue

            fm = parse_front_matter(fpath)
            if fm is None:
                # No front matter — skip
                continue

            # Capture the parent field from the first file that has one.
            # (Only used as a human-readable label in error messages.)
            if info["parent"] is None and fm.get("parent"):
                info["parent"] = fm["parent"]

            if fm.get("nav_exclude", False):
                info["nav_excluded"].append(fpath)
            else:
                info["visible"].append(fpath)

        # Only validate sections that contain at least one content page
        if info["visible"] or info["nav_excluded"]:
            sections[entry] = info

    return sections


def validate(sections, cap, docs_dir):
    """Return a list of error strings (empty means all checks passed)."""
    errors = []

    for section_dir, info in sorted(sections.items()):
        parent_label = info["parent"] or section_dir
        visible = info["visible"]
        nav_excluded = info["nav_excluded"]
        has_view_all = info["has_view_all"]
        total = len(visible) + len(nav_excluded)
        visible_count = len(visible)

        # Check 1: visible children must not exceed cap
        if visible_count > cap:
            file_list = "\n".join(f"    - {f}" for f in visible)
            errors.append(
                f"Section '{parent_label}' ({section_dir}/):\n"
                f"  {visible_count} visible pages exceed the cap of {cap}.\n"
                f"  Add 'nav_exclude: true' to {visible_count - cap} page(s) to bring the\n"
                f"  visible count down to {cap}. Currently visible:\n{file_list}"
            )

        # Check 2: sections over cap must have a view-all.md redirect
        if total > cap and not has_view_all:
            view_all_path = os.path.join(docs_dir, section_dir, "view-all.md")
            template_path = os.path.join(docs_dir, "_templates", "view-all.md")
            errors.append(
                f"Section '{parent_label}' ({section_dir}/):\n"
                f"  {total} total pages exceed the cap of {cap} but 'view-all.md' is missing.\n"
                f"  Create {view_all_path} using the template at {template_path}"
            )

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate sidebar navigation child cap.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--cap",
        type=int,
        default=DEFAULT_CAP,
        metavar="N",
        help=f"Max visible children per section (default: {DEFAULT_CAP})",
    )
    parser.add_argument(
        "--docs-dir",
        default=DEFAULT_DOCS_DIR,
        metavar="PATH",
        help=f"Path to the Jekyll docs directory (default: {DEFAULT_DOCS_DIR})",
    )
    args = parser.parse_args()

    sections = collect_sections(args.docs_dir)
    errors = validate(sections, args.cap, args.docs_dir)

    if errors:
        print("❌ Sidebar validation failed!\n")
        for i, err in enumerate(errors, 1):
            print(f"Error {i}:\n{err}\n")
        print(f"Cap is set to {args.cap}. Pass --cap N to change it.")
        print("See CONTRIBUTING.md § 'Sidebar Navigation Convention' for details.")
        sys.exit(1)
    else:
        total_sections = len(sections)
        print(
            f"✓ Sidebar validation passed! "
            f"All {total_sections} section(s) are within the cap of {args.cap}."
        )
        sys.exit(0)


if __name__ == "__main__":
    main()
