---
layout: default
title: "The Backlog of the Strange"
nav_order: 7
has_children: true
permalink: /strange/
has_toc: false
summary: "Deliberately weird research seeds—captured before they evaporate."
tags: [strange]
---

# 🌀 The Backlog of the Strange

Deliberately weird research seeds—captured before they evaporate.
{: .fs-5 .text-grey-dk-100 }

---

High uncertainty is allowed here. Ungrounded certainty is not.

**Every entry must include:**

- **Why it might work** — a plausible mechanism or analogy
- **Why it might fail** — the most likely way this falls apart
- **Cheap next test** — a concrete, low-cost step to make progress

---

{% assign strange_posts = site.pages | where_exp: "page", "page.path contains 'strange/'" | where_exp: "page", "page.title != nil" | sort: "date" | reverse %}

<ul class="post-list">
{% for post in strange_posts limit:15 %}
  {% if post.title %}
  <li>
    <span class="content-badge content-badge--strange">Strange Seed</span>
    {% if post.date %}<span class="post-meta">{{ post.date }}</span>{% endif %}
    <h4><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
    {% if post.summary %}<p class="post-summary">{{ post.summary | escape }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

{% if strange_posts.size == 0 %}
*No strange seeds yet. Add one by creating a file in `/docs/strange/` following the front matter pattern of this section.*
{% endif %}
