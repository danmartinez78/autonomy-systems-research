---
layout: default
title: Knowledge Base
nav_order: 4
has_children: true
permalink: /knowledge-base/
has_toc: false
---

# 📚 Knowledge Base

Evergreen reference pages on concepts, patterns, checklists, and practical considerations.
{: .fs-5 .text-grey-dk-100 }

---

{% assign kb_posts = site.pages | where_exp: "page", "page.path contains 'knowledge-base/'" | where_exp: "page", "page.title != nil" | sort: "title" %}

<ul class="post-list">
{% for post in kb_posts %}
  {% if post.title %}
  <li>
    <span class="content-badge content-badge--knowledge-base">Knowledge Base</span>
    <h4><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
    {% if post.summary %}<p class="post-summary">{{ post.summary | escape }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

{% if kb_posts.size == 0 %}
*No knowledge base entries yet. [Create one using the template](https://github.com/{{ site.github.repository_nwo }}/blob/main/docs/_templates/knowledge-base.md).*
{% endif %}
