---
layout: page
title: Reading Notes
permalink: /reading/
---

# Reading Notes

Structured notes on papers, articles, and technical reports relevant to autonomy and robotics research.

Each reading note includes:
- Citation and source links
- Summary and key claims
- Evidence quality assessment
- Relevance to current research
- Open questions and follow-up items

---

## Recent Reading

{% assign reading_posts = site.pages | where_exp: "page", "page.path contains 'reading/'" | where_exp: "page", "page.title != nil" | sort: "date_read" | reverse %}
{% for post in reading_posts limit:15 %}
  {% if post.title %}
### [{{ post.title }}]({{ post.url | relative_url }})
{% if post.authors %}**Authors**: {{ post.authors }}{% endif %}  
{% if post.date_read %}**Date Read**: {{ post.date_read }}{% endif %}  
{% if post.summary %}{{ post.summary }}{% endif %}
  {% endif %}
{% endfor %}

{% if reading_posts.size == 0 %}
*No reading notes yet. [Add one using the template](https://github.com/{{ site.github.repository_nwo }}/blob/main/docs/_templates/reading-note.md).*
{% endif %}

---

## By Topic

Filter by tags:
{% assign all_tags = "" | split: "" %}
{% for post in reading_posts %}
  {% if post.tags %}
    {% assign all_tags = all_tags | concat: post.tags %}
  {% endif %}
{% endfor %}
{% assign all_tags = all_tags | uniq | sort %}
{% for tag in all_tags %}
  {% if tag != "" %}- {{ tag }}{% endif %}
{% endfor %}

---

*To add a new reading note, see the [reading note template](https://github.com/{{ site.github.repository_nwo }}/blob/main/docs/_templates/reading-note.md).*
