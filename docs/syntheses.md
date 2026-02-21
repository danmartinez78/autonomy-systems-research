---
layout: default
title: Syntheses
nav_order: 3
has_children: true
permalink: /syntheses/
has_toc: false
---

# 🔬 Syntheses

Topic-level living documents that consolidate understanding across multiple sources.
{: .fs-5 .text-grey-dk-100 }

---

{% assign synthesis_posts = site.pages | where_exp: "page", "page.path contains 'syntheses/'" | where_exp: "page", "page.title != nil" | sort: "title" %}

<ul class="post-list">
{% for post in synthesis_posts %}
  {% if post.title %}
  <li>
    <span class="content-badge content-badge--synthesis">Synthesis</span>
    {% if post.last_updated %}<span class="post-meta">Updated {{ post.last_updated }}</span>{% endif %}
    <h4><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
    {% if post.summary %}<p class="post-summary">{{ post.summary | escape }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

{% if synthesis_posts.size == 0 %}
*No syntheses yet. [Create one using the template](https://github.com/{{ site.github.repository_nwo }}/blob/main/docs/_templates/synthesis.md).*
{% endif %}
