---
layout: default
title: Reading Notes
nav_order: 2
has_children: true
permalink: /reading/
has_toc: false
---

# 📖 Reading Notes

Structured notes on papers, articles, and technical reports relevant to autonomy and robotics research.
{: .fs-5 .text-grey-dk-100 }

---

{% assign reading_posts = site.pages | where_exp: "page", "page.path contains 'reading/'" | where_exp: "page", "page.title != nil" | sort: "date_read" | reverse %}

<ul class="post-list">
{% for post in reading_posts limit:15 %}
  {% if post.title %}
  <li>
    <span class="content-badge content-badge--reading">Reading Note</span>
    {% if post.date_read %}<span class="post-meta">{{ post.date_read }}</span>{% endif %}
    <h4><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
    {% if post.authors %}<span class="post-meta">{{ post.authors }}</span>{% endif %}
    {% if post.summary %}<p class="post-summary">{{ post.summary | escape }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

{% if reading_posts.size == 0 %}
*No reading notes yet. [Add one using the template](https://github.com/{{ site.github.repository_nwo }}/blob/main/docs/_templates/reading-note.md).*
{% endif %}
