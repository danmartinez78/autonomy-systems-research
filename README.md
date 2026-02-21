# Autonomy Systems Research

A public knowledge base for robotics and autonomy research. This repository contains structured reading notes, syntheses, and evergreen reference material on perception, planning, control, learning, and system architecture.

## Purpose

This knowledge base serves as a public repository for research artifacts, enabling:

- **Structured Learning**: Capture and organize understanding from papers and technical resources
- **Knowledge Synthesis**: Consolidate insights across multiple sources into coherent narratives
- **Evergreen Reference**: Maintain practical, actionable guidance on concepts and patterns
- **Transparent Research**: Document progress, decisions, and evolving understanding
- **Team Collaboration**: Enable research team members to build shared understanding

## Organization

The knowledge base is organized into several content types:

- **[Reading Notes](https://danmartinez78.github.io/autonomy-systems-research/reading/)**: Structured summaries and analysis of papers and articles
- **[Syntheses](https://danmartinez78.github.io/autonomy-systems-research/syntheses/)**: Topic-level consolidation of understanding across sources
- **[Surveys](https://danmartinez78.github.io/autonomy-systems-research/survey/)**: Comprehensive surveys of software stacks, ecosystems, and tooling for specific platforms
- **[Journal Entries](https://danmartinez78.github.io/autonomy-systems-research/journal/)**: Chronological progress logs and research decisions
- **[Knowledge Base](https://danmartinez78.github.io/autonomy-systems-research/knowledge-base/)**: Evergreen reference pages on concepts and patterns
- **[References](https://danmartinez78.github.io/autonomy-systems-research/references/)**: Glossary, definitions, and canonical links
- **[Tags](https://danmartinez78.github.io/autonomy-systems-research/tags/)**: Browse content by topic tags
- **[Search](https://danmartinez78.github.io/autonomy-systems-research/search/)**: Full-text search across all content

## Quick Start

### Browse Online

Visit the published site: **https://danmartinez78.github.io/autonomy-systems-research**

### Add Content

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions on adding reading notes, syntheses, journal entries, and knowledge base pages.

Quick workflow:
1. Copy appropriate template from `/docs/_templates/`
2. Fill in the content following the template structure
3. Submit a pull request using the PR template

### Local Development

To preview changes locally:

```bash
# Install dependencies (first time only)
cd docs
bundle install

# Run local server
bundle exec jekyll serve

# Open http://localhost:4000/autonomy-systems-research/ in browser
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed setup instructions.

## Maintenance Tasks

### Regenerating Tag Pages

After adding or modifying content with tags, regenerate the tag pages:

```bash
# From repository root
python3 generate-tags.py
```

This updates `/docs/tags.md` and all individual tag pages in `/docs/tags/`. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Publishing

This site is built with **Jekyll 4** using the **just-the-docs** theme and deployed via **GitHub Actions**:
- **Source**: `/docs` directory on `main` branch
- **URL**: https://danmartinez78.github.io/autonomy-systems-research
- **Theme**: [just-the-docs](https://just-the-docs.com/) — sidebar navigation, built-in search, dark/light mode
- **Build**: Automated via `.github/workflows/pages.yml` on every push to `main`

No manual build or deployment steps required.

### GitHub Pages Setup

To enable GitHub Pages:

1. Go to repository Settings → Pages
2. Under "Build and deployment":
   - **Source**: GitHub Actions
3. The workflow in `.github/workflows/pages.yml` handles the rest

## Repository Structure

```
autonomy-systems-research/
├── docs/                          # Jekyll site source (GitHub Pages)
│   ├── _config.yml               # Jekyll configuration (just-the-docs theme)
│   ├── Gemfile                   # Ruby dependencies (Jekyll 4 + just-the-docs)
│   ├── _layouts/                 # Custom layouts
│   │   └── home.html             # Dashboard-style home page
│   ├── _includes/                # Custom includes
│   │   ├── head_custom.html      # Critical CSS, favicon, theme-swap script
│   │   └── header_custom.html    # Dark/light theme toggle button
│   ├── _sass/                    # Custom SCSS
│   │   ├── color_schemes/        # Dark and light color schemes
│   │   │   ├── research-dark.scss
│   │   │   └── research-light.scss
│   │   └── custom/
│   │       ├── custom.scss       # All custom component styles
│   │       └── setup.scss        # Pre-theme variable overrides
│   ├── assets/
│   │   ├── css/                  # Theme stylesheet variants
│   │   │   ├── just-the-docs-research-dark.scss
│   │   │   └── just-the-docs-research-light.scss
│   │   └── images/
│   │       └── favicon.svg       # Site favicon
│   ├── index.md                  # Landing page (dashboard)
│   ├── journal.md                # Journal index page
│   ├── reading.md                # Reading notes index page
│   ├── syntheses.md              # Syntheses index page
│   ├── survey.md                 # Surveys index page
│   ├── knowledge-base.md         # Knowledge base index page
│   ├── references.md             # References and glossary
│   ├── tags.md                   # Tags index (generated)
│   ├── tags/                     # Individual tag pages (generated)
│   │   └── *.md
│   ├── journal/                  # Journal entries by year
│   │   └── 2026.md
│   ├── reading/                  # Reading notes
│   │   └── *.md
│   ├── syntheses/                # Synthesis documents
│   │   └── *.md
│   ├── survey/                   # Survey documents
│   │   └── *.md
│   ├── knowledge-base/           # Evergreen reference pages
│   │   └── *.md
│   └── _templates/               # Content templates (not published)
│       ├── reading-note.md
│       ├── synthesis.md
│       ├── survey.md
│       ├── journal-entry.md
│       ├── knowledge-base.md
│       └── view-all.md           # Sidebar "View all…" redirect
├── generate-tags.py              # Script to generate tag pages
├── .github/
│   ├── workflows/
│   │   └── pages.yml             # GitHub Actions: build & deploy
│   ├── PULL_REQUEST_TEMPLATE.md  # PR template
│   └── ISSUE_TEMPLATE/           # Issue templates
│       ├── reading-to-ingest.md
│       └── synthesis-kb-task.md
├── CONTRIBUTING.md               # Contribution guidelines
├── LICENSE-DOCS                  # CC BY 4.0 for documentation
├── LICENSE-CODE                  # MIT for code
└── README.md                     # This file
```

## Licensing

This repository uses dual licensing:

### Documentation and Content: CC BY 4.0

All documentation, reading notes, journal entries, syntheses, knowledge base pages, and media are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

You are free to share and adapt this content with attribution.

See [LICENSE-DOCS](LICENSE-DOCS) for full terms.

### Code: MIT License

All code (scripts, tools, automation, code examples) is licensed under the **MIT License**.

You are free to use, modify, and distribute this code.

See [LICENSE-CODE](LICENSE-CODE) for full terms.

### What This Means

- **Reading a paper summary?** You can freely share, adapt, and build upon it with attribution (CC BY 4.0)
- **Using a code snippet?** You can freely use it in your own projects (MIT)
- **Not sure which applies?** Markdown content and prose are CC BY 4.0; code and scripts are MIT

## Disclaimer

**This knowledge base is provided for educational and research purposes.**

⚠️ **Important Limitations**:

- **No Warranty**: Content is provided "as is" without warranty of any kind
- **Not Safety-Certified**: Information has not been validated for safety-critical applications
- **Not Production-Ready**: Concepts and code examples are for research and learning
- **Validate Before Use**: Always validate any information before applying to real autonomous systems
- **Active Research**: Content reflects current understanding which may change as research progresses

The contributors make no representations about the suitability, reliability, accuracy, or completeness of any information for any purpose. 

**Do not use this content in safety-critical systems or real-world deployments without thorough validation, testing, and safety certification appropriate for your application.**

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- How to add different types of content
- Style guidelines and conventions
- Pull request process
- Local development setup

## Questions or Issues?

- Open an issue for questions, suggestions, or discussions
- Use the issue templates for content suggestions
- See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidance

## Acknowledgments

This knowledge base structure is inspired by best practices from research note-taking systems, evergreen note methodologies, and open science principles.

---

**Visit the site**: https://danmartinez78.github.io/autonomy-systems-research