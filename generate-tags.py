#!/usr/bin/env python3
"""
Generate tag pages for Jekyll site.

This script scans all markdown files in the docs/ directory, extracts tags from
front matter, and generates:
1. A tags index page at /docs/tags.md
2. Individual tag pages at /docs/tags/<tag-slug>.md

Usage:
    python3 generate-tags.py

The script is designed to be run from the repository root directory and is
idempotent - it can be run multiple times safely.
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime, date


def normalize_date_for_sorting(d):
    """
    Normalize a date value to datetime for comparison.
    
    Converts datetime.date objects to datetime.datetime so they can be compared
    with datetime.max (used for pages without dates). Python 3 raises TypeError
    when comparing date and datetime objects directly.
    
    Args:
        d: A datetime.date, datetime.datetime, or None
        
    Returns:
        datetime.datetime: Normalized datetime value, or datetime.max if None
    """
    if d is None:
        return datetime.max
    elif isinstance(d, datetime):
        return d
    elif isinstance(d, date):
        # Convert date to datetime at midnight
        return datetime.combine(d, datetime.min.time())
    else:
        return datetime.max


# Configuration
DOCS_DIR = Path(__file__).parent / "docs"
TAGS_DIR = DOCS_DIR / "tags"
TAGS_INDEX = DOCS_DIR / "tags.md"
EXCLUDE_DIRS = ["_site", "_templates", ".jekyll-cache", "vendor", ".bundle"]
REPO_URL = "https://danmartinez78.github.io/autonomy-systems-research"

# Tag page styles are now defined in /docs/_sass/custom/custom.scss


def slugify(text):
    """Convert text to URL-friendly slug."""
    # Convert to lowercase and replace spaces/special chars with hyphens
    slug = text.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')


def escape_html(text):
    """Escape HTML special characters for safe insertion into HTML."""
    if not text:
        return text
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#x27;'))


def extract_front_matter(file_path):
    """Extract YAML front matter from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match front matter between --- delimiters
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None
        
        front_matter_text = match.group(1)
        return yaml.safe_load(front_matter_text)
    except Exception as e:
        print(f"Warning: Could not parse {file_path}: {e}")
        return None


def should_exclude_path(path):
    """Check if a path should be excluded from scanning."""
    parts = path.parts
    for exclude_dir in EXCLUDE_DIRS:
        if exclude_dir in parts:
            return True
    return False


def sanitize_url(url):
    """Sanitize URL path to prevent path traversal and ensure valid URLs."""
    # Remove any path traversal sequences
    url = url.replace('..', '')
    # Normalize multiple slashes
    url = re.sub(r'/+', '/', url)
    # Ensure it starts with /
    if not url.startswith('/'):
        url = '/' + url
    return url


def collect_tags_and_pages():
    """
    Scan all markdown files and collect tags with associated pages.
    
    Returns:
        dict: Mapping of tag -> list of page info dicts
    """
    tag_pages = defaultdict(list)
    
    # Walk through docs directory
    for md_file in DOCS_DIR.rglob("*.md"):
        # Skip excluded directories
        if should_exclude_path(md_file.relative_to(DOCS_DIR)):
            continue
        
        # Skip the tags index itself
        if md_file == TAGS_INDEX:
            continue
        
        # Skip files in tags directory (they are generated)
        if md_file.parent == TAGS_DIR:
            continue
        
        # Extract front matter
        front_matter = extract_front_matter(md_file)
        if not front_matter or 'tags' not in front_matter:
            continue
        
        # Get page info
        title = front_matter.get('title', md_file.stem.replace('-', ' ').title())
        tags = front_matter.get('tags', [])
        summary = front_matter.get('summary', '')
        page_type = front_matter.get('type', '')
        
        # Get date (could be date, date_read, or last_updated)
        date = front_matter.get('date') or front_matter.get('date_read') or front_matter.get('last_updated')
        
        # Calculate relative URL and sanitize it
        rel_path = md_file.relative_to(DOCS_DIR)
        url = '/' + str(rel_path.with_suffix('')).replace(os.sep, '/')
        url = sanitize_url(url)
        
        # Build page info
        page_info = {
            'title': title,
            'url': url,
            'summary': summary,
            'type': page_type,
            'date': date,
            'file_path': md_file
        }
        
        # Add to each tag's page list
        if isinstance(tags, list):
            for tag in tags:
                tag_pages[tag].append(page_info)
    
    return tag_pages


def generate_tag_index(tag_pages):
    """Generate the main tags index page at /docs/tags.md."""
    
    # Sort tags alphabetically
    sorted_tags = sorted(tag_pages.keys())
    
    # Generate content
    content = f"""---
layout: default
title: Tags
nav_order: 7
permalink: /tags/
nav_exclude: false
search_exclude: false
---

# Browse by Tag

This page shows all tags used across the knowledge base. Click on a tag to see all pages with that tag.

<!-- Generated by generate-tags.py on {datetime.now().strftime('%Y-%m-%d')} -->

<div class="tag-cloud">
"""
    
    for tag in sorted_tags:
        tag_slug = slugify(tag)
        tag_escaped = escape_html(tag)
        page_count = len(tag_pages[tag])
        plural = 'page' if page_count == 1 else 'pages'
        
        content += f"""  <div class="tag-item">
    <h3><a href="{{{{ site.baseurl }}}}/tags/{tag_slug}/">{tag_escaped}</a></h3>
    <p>{page_count} {plural}</p>
  </div>
"""
    
    content += """</div>

## All Tags (Alphabetical)

"""
    
    for tag in sorted_tags:
        tag_slug = slugify(tag)
        tag_escaped = escape_html(tag)
        page_count = len(tag_pages[tag])
        plural = 'page' if page_count == 1 else 'pages'
        content += f"- [**{tag_escaped}**]({{{{ site.baseurl }}}}/tags/{tag_slug}/) ({page_count} {plural})\n"
    
    return content


def generate_tag_page(tag, pages):
    """Generate an individual tag page."""
    
    tag_slug = slugify(tag)
    # Escape HTML special characters in the tag name for safe insertion into YAML/HTML
    escaped_tag = tag.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    page_count = len(pages)
    plural = 'page' if page_count == 1 else 'pages'
    
    content = f"""---
layout: default
title: "Tag: {escaped_tag}"
permalink: /tags/{tag_slug}/
nav_exclude: true
search_exclude: true
---

# Tag: {escaped_tag}

{page_count} {plural} tagged with **{escaped_tag}**

[← Back to all tags]({{{{ site.baseurl }}}}/tags/)

<!-- Generated by generate-tags.py on {datetime.now().strftime('%Y-%m-%d')} -->

---

<ul class="post-list">
"""
    
    # Sort pages by date (newest first), then by title
    sorted_pages = sorted(
        pages,
        key=lambda p: (normalize_date_for_sorting(p['date']), p['title']),
        reverse=True
    )
    
    for page in sorted_pages:
        content += "  <li>\n"
        
        # Add metadata line
        meta_parts = []
        if page['type']:
            type_escaped = escape_html(page['type'])
            meta_parts.append(type_escaped)
        if page['date']:
            if isinstance(page['date'], str):
                meta_parts.append(page['date'])
            else:
                meta_parts.append(page['date'].strftime('%b %-d, %Y'))
        
        if meta_parts:
            content += f"    <span class=\"post-meta\">{' &middot; '.join(meta_parts)}</span>\n"
        
        # Add title (escape HTML entities)
        title_escaped = escape_html(page['title'])
        content += f"    <h4><a href=\"{{{{ site.baseurl }}}}{page['url']}/\">{title_escaped}</a></h4>\n"
        
        # Add summary if available (escape HTML entities)
        if page['summary']:
            summary_escaped = escape_html(page['summary'])
            content += f"    <p class=\"post-summary\">{summary_escaped}</p>\n"
        
        content += "  </li>\n"
    
    content += "</ul>\n"
    
    return content


def main():
    """Main function to generate all tag pages."""
    
    print("=" * 60)
    print("Generating tag pages for Jekyll site")
    print("=" * 60)
    print()
    
    # Collect tags and pages
    print("Scanning markdown files for tags...")
    tag_pages = collect_tags_and_pages()
    
    if not tag_pages:
        print("No tags found in any markdown files.")
        return
    
    print(f"Found {len(tag_pages)} unique tags across {sum(len(pages) for pages in tag_pages.values())} page references")
    print()
    
    # Create tags directory if it doesn't exist
    TAGS_DIR.mkdir(exist_ok=True)
    
    # Generate tags index page
    print(f"Generating tags index: {TAGS_INDEX}")
    index_content = generate_tag_index(tag_pages)
    with open(TAGS_INDEX, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"✓ Generated {TAGS_INDEX}")
    print()
    
    # Track which tag files should exist
    current_tag_files = set()
    
    # Generate individual tag pages
    print(f"Generating individual tag pages in {TAGS_DIR}/")
    for tag, pages in sorted(tag_pages.items()):
        tag_slug = slugify(tag)
        tag_file = TAGS_DIR / f"{tag_slug}.md"
        current_tag_files.add(tag_file)
        
        tag_content = generate_tag_page(tag, pages)
        with open(tag_file, 'w', encoding='utf-8') as f:
            f.write(tag_content)
        
        print(f"  ✓ {tag_slug}.md ({len(pages)} pages)")
    
    print()
    
    # Delete obsolete tag pages
    print("Checking for obsolete tag pages...")
    existing_tag_files = set(TAGS_DIR.glob("*.md"))
    obsolete_files = existing_tag_files - current_tag_files
    
    if obsolete_files:
        obsolete_count = len(obsolete_files)
        print(f"Found {obsolete_count} obsolete tag page(s) to delete:")
        for obsolete_file in sorted(obsolete_files):
            print(f"  ✗ Deleting {obsolete_file.name}")
            obsolete_file.unlink()
        print()
    else:
        print("✓ No obsolete tag pages found")
        print()
    
    print("=" * 60)
    print(f"✓ Successfully generated {len(tag_pages)} tag pages")
    if obsolete_files:
        print(f"✓ Deleted {len(obsolete_files)} obsolete tag pages")
    print("=" * 60)
    print()
    print("Tag pages are ready! You can now:")
    print("  1. Commit the generated files")
    print("  2. Push to GitHub")
    print(f"  3. View the tags at {REPO_URL}/tags/")
    print()


if __name__ == "__main__":
    main()
