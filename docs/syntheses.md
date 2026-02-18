---
layout: page
title: Syntheses
permalink: /syntheses/
---

# Syntheses

Topic-level living documents that consolidate understanding across multiple sources. These pages synthesize research findings, competing hypotheses, and current best understanding on specific topics.

Each synthesis includes:
- Problem statement and context
- Current best understanding
- Competing hypotheses or approaches
- Source map with references
- Open questions and next research directions

---

## Active Syntheses

{% assign synthesis_posts = site.pages | where_exp: "page", "page.path contains 'syntheses/'" | where_exp: "page", "page.title != nil" | sort: "title" %}
{% for post in synthesis_posts %}
  {% if post.title %}
### [{{ post.title }}]({{ post.url | relative_url }})
{% if post.summary %}{{ post.summary }}{% endif %}  
{% if post.last_updated %}**Last Updated**: {{ post.last_updated }}{% endif %}
  {% endif %}
{% endfor %}

{% if synthesis_posts.size == 0 %}
*No syntheses yet. [Create one using the template](https://github.com/danmartinez78/autonomy-systems-research/blob/main/docs/_templates/synthesis.md).*
{% endif %}

---

## By Topic Area

Syntheses organized by research area:
- Perception
- Planning
- Control
- Learning
- System Architecture

---

*To create a new synthesis, see the [synthesis template](https://github.com/danmartinez78/autonomy-systems-research/blob/main/docs/_templates/synthesis.md).*
