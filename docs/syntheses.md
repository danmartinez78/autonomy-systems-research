---
layout: default
title: Syntheses
nav_order: 4
has_children: true
permalink: /syntheses/
has_toc: false
---

# 🔬 Syntheses

Topic-level living documents that consolidate understanding across multiple sources.
{: .fs-5 .text-grey-dk-100 }

---

{% assign synthesis_posts = site.pages | where_exp: "page", "page.path contains 'syntheses/'" | where_exp: "page", "page.title != nil" | sort: "title" %}

{% comment %} Confidence dashboard: aggregate counts by level {% endcomment %}
{% assign conf_high = 0 %}
{% assign conf_med = 0 %}
{% assign conf_low = 0 %}
{% assign conf_unknown = 0 %}
{% for post in synthesis_posts %}
  {% if post.title %}
    {% if post.confidence == "high" %}
      {% assign conf_high = conf_high | plus: 1 %}
    {% elsif post.confidence == "med" %}
      {% assign conf_med = conf_med | plus: 1 %}
    {% elsif post.confidence == "low" %}
      {% assign conf_low = conf_low | plus: 1 %}
    {% else %}
      {% assign conf_unknown = conf_unknown | plus: 1 %}
    {% endif %}
  {% endif %}
{% endfor %}

## 📊 Confidence Dashboard

<div class="confidence-row">
  <div class="confidence-card confidence-card--high">
    <span class="confidence-card__number">{{ conf_high }}</span>
    <span class="confidence-card__label">High</span>
  </div>
  <div class="confidence-card confidence-card--med">
    <span class="confidence-card__number">{{ conf_med }}</span>
    <span class="confidence-card__label">Medium</span>
  </div>
  <div class="confidence-card confidence-card--low">
    <span class="confidence-card__number">{{ conf_low }}</span>
    <span class="confidence-card__label">Low</span>
  </div>
  <div class="confidence-card confidence-card--unknown">
    <span class="confidence-card__number">{{ conf_unknown }}</span>
    <span class="confidence-card__label">Unknown</span>
  </div>
</div>

{% assign needs_review = "" | split: "" %}
{% for post in synthesis_posts %}
  {% if post.title %}
    {% unless post.confidence == "high" or post.confidence == "med" %}
      {% assign needs_review = needs_review | push: post %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% if needs_review.size > 0 %}
### 🔍 Topics Needing Review

The following syntheses have **low** or **missing** confidence and may benefit from additional research:

<ul class="post-list">
{% for post in needs_review %}
  {% if post.title %}
  {% assign conf_value = post.confidence | default: 'unknown' %}
  {% case conf_value %}{% when "high" %}{% assign conf_label = "High" %}{% when "med" %}{% assign conf_label = "Medium" %}{% when "low" %}{% assign conf_label = "Low" %}{% else %}{% assign conf_label = "Unknown" %}{% endcase %}
  <li>
    <span class="confidence-badge confidence-badge--{{ conf_value }}">{{ conf_label }}</span>
    <h4><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
    {% if post.summary %}<p class="post-summary">{{ post.summary | escape }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>
{% endif %}

---

## All Syntheses

<ul class="post-list">
{% for post in synthesis_posts %}
  {% if post.title %}
  {% assign conf_value = post.confidence | default: 'unknown' %}
  {% case conf_value %}{% when "high" %}{% assign conf_label = "High" %}{% when "med" %}{% assign conf_label = "Medium" %}{% when "low" %}{% assign conf_label = "Low" %}{% else %}{% assign conf_label = "Unknown" %}{% endcase %}
  <li>
    <span class="content-badge content-badge--synthesis">Synthesis</span>
    <span class="confidence-badge confidence-badge--{{ conf_value }}">{{ conf_label }}</span>
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

<details class="toc-wrapper" markdown="block">
<summary>Maintenance notes</summary>

Add `confidence: high`, `confidence: med`, or `confidence: low` to any synthesis front matter. Syntheses without this field are shown as **unknown** and listed under "Topics Needing Review". Confidence reflects the author's assessment of how well-supported the synthesis content is by cited evidence.

</details>
