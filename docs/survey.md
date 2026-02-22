---
layout: default
title: Surveys
nav_order: 6
has_children: true
permalink: /survey/
has_toc: false
---

# 🔭 Surveys

Comprehensive surveys of software stacks, research ecosystems, and tooling for specific platforms and topics.
{: .fs-5 .text-grey-dk-100 }

---

{% assign survey_posts = site.pages | where_exp: "page", "page.path contains 'survey/'" | where_exp: "page", "page.title != nil" | sort: "date" | reverse %}

<ul class="post-list">
{% for post in survey_posts limit:15 %}
  {% if post.title %}
  <li>
    <span class="content-badge content-badge--survey">Survey</span>
    {% if post.date %}<span class="post-meta">{{ post.date }}</span>{% endif %}
    <h4><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
    {% if post.summary %}<p class="post-summary">{{ post.summary | escape }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

{% if survey_posts.size == 0 %}
*No surveys yet. Add one by creating a file in `/docs/survey/` with `parent: Surveys` in the front matter.*
{% endif %}
