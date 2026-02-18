---
layout: page
title: Tags
permalink: /tags/
---

# Browse by Tag

This page shows all tags used across the knowledge base. Click on a tag to see all pages with that tag.

{% comment %}Collect all tags and build tag-to-pages mapping in a single pass{% endcomment %}
{% assign all_tags = "" | split: "" %}
{% assign tag_pages = "" | split: "" %}

{% for page_item in site.pages %}
  {% if page_item.tags %}
    {% for tag in page_item.tags %}
      {% unless all_tags contains tag %}
        {% assign all_tags = all_tags | push: tag %}
      {% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% comment %}Sort tags alphabetically{% endcomment %}
{% assign sorted_tags = all_tags | sort %}

<div class="tag-cloud">
{% for tag in sorted_tags %}
  {% assign tag_count = 0 %}
  {% for page_item in site.pages %}
    {% if page_item.tags contains tag %}
      {% assign tag_count = tag_count | plus: 1 %}
    {% endif %}
  {% endfor %}
  <div class="tag-item">
    <h3><a href="#{{ tag | slugify }}">{{ tag }}</a></h3>
    <p>{{ tag_count }} {% if tag_count == 1 %}page{% else %}pages{% endif %}</p>
  </div>
{% endfor %}
</div>

---

## All Tags (Alphabetical)

{% for tag in sorted_tags %}
<h3 id="{{ tag | slugify }}">{{ tag }}</h3>
<ul class="post-list">
{% for page_item in site.pages %}
  {% if page_item.tags contains tag and page_item.url != page.url %}
  <li>
    <span class="post-meta">
      {% if page_item.type %}{{ page_item.type }}{% endif %}
      {% if page_item.date %}
        &middot; {{ page_item.date | date: "%b %-d, %Y" }}
      {% elsif page_item.date_read %}
        &middot; {{ page_item.date_read | date: "%b %-d, %Y" }}
      {% elsif page_item.last_updated %}
        &middot; {{ page_item.last_updated | date: "%b %-d, %Y" }}
      {% endif %}
    </span>
    <h4>
      <a href="{{ page_item.url | relative_url }}">{{ page_item.title | escape }}</a>
    </h4>
    {% if page_item.summary %}
      <p class="post-summary">{{ page_item.summary | escape }}</p>
    {% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>
{% endfor %}

<style>
.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 30px 0;
}

.tag-item {
  border: 1px solid #e8e8e8;
  border-radius: 4px;
  padding: 15px;
  min-width: 150px;
  background: #fafafa;
}

.tag-item h3 {
  margin: 0 0 10px 0;
  font-size: 1.1em;
}

.tag-item p {
  margin: 0;
  color: #666;
  font-size: 0.9em;
}

.post-list {
  list-style: none;
  padding-left: 0;
}

.post-list li {
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #e8e8e8;
}

.post-meta {
  color: #828282;
  font-size: 0.9em;
}

.post-list h4 {
  margin: 5px 0;
}

.post-summary {
  margin: 5px 0 15px 0;
}
</style>
