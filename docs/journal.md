---
layout: page
title: Journal
permalink: /journal/
---

# Research Journal

Chronological entries documenting research activities, progress, decisions, and next steps.

Entries are organized by date (YYYY/YYYY-MM-DD-title.md) and typically cover weekly progress.

---

## Recent Entries

{% assign journal_posts = site.pages | where_exp: "page", "page.path contains 'journal/'" | where_exp: "page", "page.title != nil" | sort: "date" | reverse %}
{% for post in journal_posts limit:10 %}
  {% if post.title %}
### [{{ post.title }}]({{ post.url | relative_url }})
**Date**: {{ post.date | date: "%Y-%m-%d" }}  
{% if post.summary %}{{ post.summary }}{% endif %}
  {% endif %}
{% endfor %}

---

## Archive

Browse by year:
- [2026](/journal/2026/)

---

*To add a new journal entry, see the [journal entry template](https://github.com/danmartinez78/autonomy-systems-research/blob/main/docs/_templates/journal-entry.md).*
