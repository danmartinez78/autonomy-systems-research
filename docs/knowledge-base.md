---
layout: page
title: Knowledge Base
permalink: /knowledge-base/
---

# Knowledge Base

Evergreen reference pages on concepts, patterns, checklists, and practical considerations for autonomy and robotics systems.

Each knowledge base entry includes:
- Clear definition
- When to use (and when not to use)
- Tradeoffs and design considerations
- Common pitfalls and gotchas
- References and examples

---

## Topics

{% assign kb_posts = site.pages | where_exp: "page", "page.path contains 'knowledge-base/'" | where_exp: "page", "page.title != nil" | sort: "title" %}
{% for post in kb_posts %}
  {% if post.title %}
### [{{ post.title }}]({{ post.url | relative_url }})
{% if post.summary %}{{ post.summary }}{% endif %}
  {% endif %}
{% endfor %}

{% if kb_posts.size == 0 %}
*No knowledge base entries yet. [Create one using the template](https://github.com/danmartinez78/autonomy-systems-research/blob/main/docs/_templates/knowledge-base.md).*
{% endif %}

---

## Categories

- **Concepts**: Fundamental ideas and definitions
- **Patterns**: Recurring solutions and design patterns
- **Checklists**: Step-by-step procedures and validation lists
- **Gotchas**: Common pitfalls and things to watch out for

---

*To add a new knowledge base entry, see the [knowledge base template](https://github.com/danmartinez78/autonomy-systems-research/blob/main/docs/_templates/knowledge-base.md).*
