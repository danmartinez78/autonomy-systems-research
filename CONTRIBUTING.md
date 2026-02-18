# Contributing to Autonomy Systems Research Knowledge Base

Thank you for contributing to the Autonomy Systems Research knowledge base! This guide explains how to add content and maintain the site.

## Table of Contents

- [Getting Started](#getting-started)
- [Content Types](#content-types)
- [Adding Content](#adding-content)
- [Style Guidelines](#style-guidelines)
- [Pull Request Process](#pull-request-process)
- [Local Development](#local-development)

## Getting Started

This knowledge base is built with Jekyll and hosted on GitHub Pages. Content is written in Markdown and organized into different types of artifacts.

### Quick Start

1. **Fork** this repository
2. **Clone** your fork locally
3. **Create a branch** for your contribution
4. **Add or edit** content following the guidelines below
5. **Test locally** (optional but recommended)
6. **Submit a pull request** using the PR template

## Content Types

We organize content into five main types:

### 1. Reading Notes (`/docs/reading/`)

Structured notes on papers, articles, and technical reports.

**When to create**: After reading a paper relevant to robotics/autonomy research

**File naming**: `short-descriptive-title.md`

**Template**: [reading-note.md](docs/_templates/reading-note.md)

**Required front matter**:
```yaml
---
title: "Paper Title"
date_read: YYYY-MM-DD
authors: "Author names"
link: "URL to paper"
tags: [tag1, tag2]
summary: "One-sentence summary"
---
```

### 2. Syntheses (`/docs/syntheses/`)

Topic-level living documents that consolidate understanding across multiple sources.

**When to create**: When you've read several papers on a topic and want to synthesize understanding

**File naming**: `topic-name.md`

**Template**: [synthesis.md](docs/_templates/synthesis.md)

**Required front matter**:
```yaml
---
title: "Synthesis Title"
last_updated: YYYY-MM-DD
tags: [topic-area]
summary: "What this synthesis covers"
---
```

### 3. Journal Entries (`/docs/journal/YYYY/`)

Dated entries documenting research progress, decisions, and next steps.

**When to create**: Weekly (or as major milestones occur)

**File naming**: `YYYY-MM-DD-short-title.md`

**Template**: [journal-entry.md](docs/_templates/journal-entry.md)

**Required front matter**:
```yaml
---
title: "Week of Month DD, YYYY"
date: YYYY-MM-DD
tags: [research-area]
summary: "Brief summary"
---
```

### 4. Knowledge Base Pages (`/docs/knowledge-base/`)

Evergreen reference material on concepts, patterns, checklists, and gotchas.

**When to create**: When you have practical wisdom or reference material worth capturing permanently

**File naming**: `concept-or-pattern-name.md`

**Template**: [knowledge-base.md](docs/_templates/knowledge-base.md)

**Required front matter**:
```yaml
---
title: "Concept Name"
date: YYYY-MM-DD
tags: [category, topic]
summary: "Brief description"
---
```

### 5. References (`/docs/references.md`)

Glossary, definitions, and canonical links. This is a single page that grows over time.

**When to update**: When adding new terminology or canonical resources

## Adding Content

### Adding a Reading Note

1. Copy the template:
   ```bash
   cp docs/_templates/reading-note.md docs/reading/your-paper-title.md
   ```

2. Fill in all sections of the template:
   - Update front matter with paper details
   - Write summary and key claims
   - Assess evidence quality
   - Note relevance to current research
   - List open questions

3. Add tags that describe the paper's topics (e.g., `perception`, `planning`, `learning`)

4. Submit a pull request using the PR template

### Adding a Synthesis

1. Copy the template:
   ```bash
   cp docs/_templates/synthesis.md docs/syntheses/your-topic.md
   ```

2. Fill in all sections:
   - Clearly state the problem being synthesized
   - Document current understanding with confidence levels
   - Compare competing approaches with evidence
   - Map sources (link to reading notes or external papers)
   - Identify open questions

3. Link to related reading notes and knowledge base pages

4. Submit a pull request - syntheses benefit from review and discussion

### Adding a Journal Entry

1. Create directory for current year if needed:
   ```bash
   mkdir -p docs/journal/2026
   ```

2. Copy the template:
   ```bash
   cp docs/_templates/journal-entry.md docs/journal/2026/2026-02-18-descriptive-title.md
   ```

3. Fill in the sections:
   - What changed (understanding, implementation, direction)
   - Decisions made (with rationale)
   - Blockers and challenges
   - Next steps

4. Link to relevant reading notes and syntheses

5. Journal entries are less formal - submit PR directly

### Adding a Knowledge Base Entry

1. Copy the template:
   ```bash
   cp docs/_templates/knowledge-base.md docs/knowledge-base/your-concept.md
   ```

2. Fill in all sections:
   - Clear definition
   - When to use (and when not to)
   - How it works
   - Tradeoffs
   - Common pitfalls with solutions
   - Concrete examples
   - References

3. Focus on practical, actionable guidance

4. Submit a pull request for review

### Updating the References Page

1. Edit `docs/references.md` directly

2. Add new entries in alphabetical order within their section

3. Keep definitions brief (1-2 sentences)

4. Submit PR for review

### Regenerating Tag Pages

After adding or updating content with new tags, you should regenerate the tag index and individual tag pages.

The repository includes a Python script that automatically generates:
- A tags index page at `/docs/tags.md`
- Individual tag pages at `/docs/tags/<tag-name>.md`

**To regenerate tag pages:**

1. Run the generation script from the repository root:
   ```bash
   python3 generate-tags.py
   ```

2. The script will:
   - Scan all markdown files in `docs/` for tags
   - Update `/docs/tags.md` with the current list of all tags
   - Create/update individual tag pages in `/docs/tags/`

3. Commit the generated/updated files with your content changes:
   ```bash
   git add docs/tags.md docs/tags/
   git commit -m "Regenerate tag pages"
   ```

**When to regenerate:**
- After adding new content with tags
- When you introduce new tags that don't exist yet
- Periodically to ensure tag pages are up-to-date

**Note:** A CI workflow automatically checks that tag pages are up-to-date when you create a pull request. If the workflow fails, simply run `python3 generate-tags.py` and commit the updated files.

**Requirements:**
- Python 3.6 or higher
- PyYAML library (`pip install pyyaml` if not already installed)

The script is idempotent - you can run it multiple times safely without causing issues.

## Style Guidelines

### Writing Style

- **Be clear and concise**: Prefer simple language over jargon
- **Be specific**: Provide concrete examples and details
- **Be honest**: Note uncertainty, limitations, and open questions
- **Be professional**: No codenames, no lore, clean and boring
- **Cite sources**: Link to papers, documentation, and related content

### Markdown Conventions

- Use `#` for page title, `##` for main sections, `###` for subsections
- Use **bold** for emphasis, `code` for technical terms
- Use bullet lists for items without ordering
- Use numbered lists for sequential steps or ranked items
- Include blank lines between sections for readability

### Front Matter

All content pages must include YAML front matter with at minimum:
- `title`: Page title
- `tags`: Array of relevant tags
- `summary`: One-sentence description

Additional fields depend on content type (see templates).

### Links

- Use relative links for internal pages: `[Link text](../path/to/page.md)`
- Use descriptive link text (not "click here")
- Verify links work before submitting PR

### Tags

Use consistent, descriptive tags:
- Lowercase
- Hyphenated for multi-word tags
- Common tags: `perception`, `planning`, `control`, `learning`, `state-estimation`, `localization`, `safety`, `architecture`

## Pull Request Process

1. **Create a descriptive branch name**: `add-reading-note-slam` or `update-synthesis-perception`

2. **Fill in the PR template**:
   - Purpose of the addition/change
   - Sources/links referenced
   - Summary of content
   - Key takeaways
   - Tags used
   - What changed (if updating existing content)

3. **Request review** from team members familiar with the topic

4. **Respond to feedback**: Be open to suggestions and improvements

5. **Merge**: Once approved, squash and merge to keep history clean

## Local Development

To preview changes locally before submitting:

### Setup (First Time)

1. Install Ruby (version 2.7 or higher)

2. Install Bundler:
   ```bash
   gem install bundler
   ```

3. Install dependencies:
   ```bash
   cd docs
   bundle install
   ```

### Running Locally

```bash
cd docs
bundle exec jekyll serve
```

Then open http://localhost:4000 in your browser.

Changes to Markdown files will be reflected automatically (refresh browser).

### Building Locally

To build without serving:

```bash
cd docs
bundle exec jekyll build
```

Output will be in `docs/_site/`.

## Quick Edit on GitHub

For small changes (typos, clarifications), you can edit directly on GitHub:

1. Navigate to the file on github.com
2. Click the pencil icon (Edit this file)
3. Make your changes
4. Scroll down and commit to a new branch
5. Submit pull request

This is convenient but skip local preview - use for minor edits only.

## Questions or Issues?

- Open an issue on GitHub for questions about contributing
- Tag issues with `question` or `documentation`
- For content discussions, consider opening an issue before writing a full synthesis

## License

By contributing, you agree that:
- **Documentation/content** (Markdown files, images) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code** (scripts, tools) is licensed under [MIT License](https://opensource.org/licenses/MIT)

See README.md for full licensing details.

---

Thank you for contributing to the knowledge base! Your work helps the entire research community.
