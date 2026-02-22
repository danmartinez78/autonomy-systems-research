---
layout: default
title: Review
nav_order: 10
permalink: /review/
has_toc: false
---

# 🔁 Spaced Review

Review prompts drawn from notes across the knowledge base. Use these to reinforce and test your understanding of key concepts.
{: .fs-5 .text-grey-dk-100 }

---

{% assign review_pages = site.pages | where_exp: "p", "p.review_questions != nil and p.review_questions.size > 0" | sort: "title" %}

{% if review_pages.size == 0 %}
*No review prompts yet. Add a `review_questions:` list to any note's front matter to have it appear here.*
{% else %}

<div class="review-controls">
  <label for="review-filter-type"><strong>Filter by type:</strong></label>
  <select id="review-filter-type" onchange="applyReviewFilter()">
    <option value="">All types</option>
    <option value="reading">Reading Notes</option>
    <option value="synthesis">Syntheses</option>
    <option value="knowledge-base">Knowledge Base</option>
    <option value="survey">Surveys</option>
  </select>

  <label for="review-filter-tag" style="margin-left:1rem;"><strong>Filter by tag:</strong></label>
  <select id="review-filter-tag" onchange="applyReviewFilter()">
    <option value="">All tags</option>
    {% assign all_review_tags = "" | split: "" %}
    {% for p in review_pages %}
      {% if p.tags %}
        {% assign all_review_tags = all_review_tags | concat: p.tags %}
      {% endif %}
    {% endfor %}
    {% assign all_review_tags = all_review_tags | uniq | sort %}
    {% for tag in all_review_tags %}
    <option value="{{ tag }}">{{ tag }}</option>
    {% endfor %}
  </select>
</div>

<div id="review-list">
{% for p in review_pages %}
  {% assign page_type = p.type | default: "" %}
  {% assign page_tags_str = p.tags | join: "," | downcase %}
  <div class="review-entry" data-type="{{ page_type }}" data-tags="{{ page_tags_str }}">
    <h3>
      <a href="{{ p.url | relative_url }}">{{ p.title }}</a>
      {% if p.type %}<span class="content-badge content-badge--{{ page_type }}">{% if page_type == "knowledge-base" %}Knowledge Base{% elsif page_type == "reading" %}Reading Note{% elsif page_type == "synthesis" %}Synthesis{% elsif page_type == "survey" %}Survey{% elsif page_type == "journal" %}Journal{% elsif page_type == "strange" %}Strange Seed{% else %}{{ page_type | capitalize }}{% endif %}</span>{% endif %}
    </h3>
    {% if p.tags %}
    <p class="post-meta">Tags: {{ p.tags | join: ", " }}</p>
    {% endif %}
    <ol>
    {% for question in p.review_questions %}
      <li>{{ question }}</li>
    {% endfor %}
    </ol>
  </div>
{% endfor %}
</div>

<p id="review-empty-msg" style="display:none;"><em>No prompts match the selected filter.</em></p>

<script>
function applyReviewFilter() {
  var typeFilter = document.getElementById('review-filter-type').value;
  var tagFilter  = document.getElementById('review-filter-tag').value;
  var entries    = document.querySelectorAll('.review-entry');
  var visible    = 0;

  entries.forEach(function(el) {
    var type = el.getAttribute('data-type') || '';
    var tags = el.getAttribute('data-tags') || '';
    var typeMatch = !typeFilter || type === typeFilter;
    var tagMatch  = !tagFilter  || tags.split(',').indexOf(tagFilter.toLowerCase()) !== -1;
    if (typeMatch && tagMatch) {
      el.style.display = '';
      visible++;
    } else {
      el.style.display = 'none';
    }
  });

  document.getElementById('review-empty-msg').style.display = (visible === 0) ? '' : 'none';
}
</script>

{% endif %}
