---
layout: default
title: Timeline
nav_order: 10
permalink: /timeline/
---

# 🕐 Timeline

Chronological view of all research activity — reading notes, syntheses, knowledge base entries, surveys, journal, and strange seeds.
{: .fs-5 .text-grey-dk-100 }

---

<div class="timeline-controls">
  <div class="timeline-filter-group" role="group" aria-label="Filter by content type">
    <span class="timeline-filter-label">Filter:</span>
    <button class="timeline-filter-btn active" data-filter="all">All</button>
    <button class="timeline-filter-btn" data-filter="reading">Reading</button>
    <button class="timeline-filter-btn" data-filter="synthesis">Synthesis</button>
    <button class="timeline-filter-btn" data-filter="knowledge-base">Knowledge Base</button>
    <button class="timeline-filter-btn" data-filter="journal">Journal</button>
    <button class="timeline-filter-btn" data-filter="survey">Survey</button>
    <button class="timeline-filter-btn" data-filter="strange">Strange</button>
  </div>
  <button class="timeline-sort-btn" id="timeline-sort-btn" aria-label="Toggle sort order" title="Toggle sort order">
    <span class="timeline-sort-label">Newest first</span>
    <span class="timeline-sort-icon">↓</span>
  </button>
</div>

<ul class="timeline-list post-list" id="timeline-list">

  {% comment %}Reading notes — date field: date_read{% endcomment %}
  {% assign reading_pages = site.pages | where_exp: "page", "page.path contains 'reading/'" | where_exp: "page", "page.title != nil" | where_exp: "page", "page.date_read != nil" %}
  {% for item in reading_pages %}
  <li class="timeline-item" data-date="{{ item.date_read }}" data-type="reading">
    <div class="timeline-item__meta">
      <span class="content-badge content-badge--reading">Reading</span>
      <span class="post-meta">{{ item.date_read }}</span>
    </div>
    <h4><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h4>
    {% if item.authors %}<span class="post-meta">{{ item.authors }}</span>{% endif %}
    {% if item.summary %}<p class="post-summary">{{ item.summary | escape }}</p>{% endif %}
  </li>
  {% endfor %}

  {% comment %}Syntheses — date field: last_updated{% endcomment %}
  {% assign synthesis_pages = site.pages | where_exp: "page", "page.path contains 'syntheses/'" | where_exp: "page", "page.title != nil" | where_exp: "page", "page.last_updated != nil" %}
  {% for item in synthesis_pages %}
  <li class="timeline-item" data-date="{{ item.last_updated | date: '%Y-%m-%d' }}" data-type="synthesis">
    <div class="timeline-item__meta">
      <span class="content-badge content-badge--synthesis">Synthesis</span>
      <span class="post-meta">{{ item.last_updated | date: '%Y-%m-%d' }}</span>
    </div>
    <h4><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h4>
    {% if item.summary %}<p class="post-summary">{{ item.summary | escape }}</p>{% endif %}
  </li>
  {% endfor %}

  {% comment %}Knowledge Base — date field: date{% endcomment %}
  {% assign kb_pages = site.pages | where_exp: "page", "page.path contains 'knowledge-base/'" | where_exp: "page", "page.title != nil" | where_exp: "page", "page.date != nil" %}
  {% for item in kb_pages %}
  <li class="timeline-item" data-date="{{ item.date | date: '%Y-%m-%d' }}" data-type="knowledge-base">
    <div class="timeline-item__meta">
      <span class="content-badge content-badge--knowledge-base">Knowledge Base</span>
      <span class="post-meta">{{ item.date | date: '%Y-%m-%d' }}</span>
    </div>
    <h4><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h4>
    {% if item.summary %}<p class="post-summary">{{ item.summary | escape }}</p>{% endif %}
  </li>
  {% endfor %}

  {% comment %}Surveys — date field: date{% endcomment %}
  {% assign survey_pages = site.pages | where_exp: "page", "page.path contains 'survey/'" | where_exp: "page", "page.title != nil" | where_exp: "page", "page.date != nil" %}
  {% for item in survey_pages %}
  <li class="timeline-item" data-date="{{ item.date | date: '%Y-%m-%d' }}" data-type="survey">
    <div class="timeline-item__meta">
      <span class="content-badge content-badge--survey">Survey</span>
      <span class="post-meta">{{ item.date | date: '%Y-%m-%d' }}</span>
    </div>
    <h4><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h4>
    {% if item.summary %}<p class="post-summary">{{ item.summary | escape }}</p>{% endif %}
  </li>
  {% endfor %}

  {% comment %}Strange seeds — date field: date, direct children of the Strange section only{% endcomment %}
  {% assign strange_pages = site.pages | where_exp: "page", "page.path contains 'strange/'" | where_exp: "page", "page.title != nil" | where_exp: "page", "page.date != nil" | where: "parent", "The Backlog of the Strange" %}
  {% for item in strange_pages %}
  <li class="timeline-item" data-date="{{ item.date | date: '%Y-%m-%d' }}" data-type="strange">
    <div class="timeline-item__meta">
      <span class="content-badge content-badge--strange">Strange</span>
      <span class="post-meta">{{ item.date | date: '%Y-%m-%d' }}</span>
    </div>
    <h4><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h4>
    {% if item.summary %}<p class="post-summary">{{ item.summary | escape }}</p>{% endif %}
  </li>
  {% endfor %}

  {% comment %}Journal year pages — date field: date (added to yearly front matter){% endcomment %}
  {% assign journal_pages = site.pages | where_exp: "page", "page.path contains 'journal/'" | where_exp: "page", "page.title != nil" | where_exp: "page", "page.date != nil" %}
  {% for item in journal_pages %}
  <li class="timeline-item" data-date="{{ item.date | date: '%Y-%m-%d' }}" data-type="journal">
    <div class="timeline-item__meta">
      <span class="content-badge content-badge--journal">Journal</span>
      <span class="post-meta">{{ item.date | date: '%Y-%m-%d' }}</span>
    </div>
    <h4><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h4>
    {% if item.summary %}<p class="post-summary">{{ item.summary | escape }}</p>{% endif %}
  </li>
  {% endfor %}

</ul>

<p class="timeline-empty-msg" id="timeline-empty-msg" style="display:none;">No items match the selected filter.</p>

<script>
(function () {
  var list = document.getElementById('timeline-list');
  var emptyMsg = document.getElementById('timeline-empty-msg');
  var sortBtn = document.getElementById('timeline-sort-btn');
  var filterBtns = document.querySelectorAll('.timeline-filter-btn');
  var sortLabel = sortBtn ? sortBtn.querySelector('.timeline-sort-label') : null;
  var sortIcon  = sortBtn ? sortBtn.querySelector('.timeline-sort-icon')  : null;

  var currentFilter = 'all';
  var ascending = false; // newest first by default

  function getItems() {
    return Array.prototype.slice.call(list.querySelectorAll('.timeline-item'));
  }

  function sortItems() {
    var items = getItems();
    items.sort(function (a, b) {
      var da = a.getAttribute('data-date') || '';
      var db = b.getAttribute('data-date') || '';
      if (da < db) return ascending ? -1 : 1;
      if (da > db) return ascending ? 1 : -1;
      return 0;
    });
    items.forEach(function (item) { list.appendChild(item); });
  }

  function applyFilter() {
    var items = getItems();
    var visible = 0;
    items.forEach(function (item) {
      var type = item.getAttribute('data-type');
      var show = (currentFilter === 'all' || type === currentFilter);
      item.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    if (emptyMsg) emptyMsg.style.display = visible === 0 ? '' : 'none';
  }

  // Initial sort
  sortItems();

  // Filter button listeners
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterBtns.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      currentFilter = btn.getAttribute('data-filter');
      applyFilter();
    });
  });

  // Sort toggle
  if (sortBtn) {
    sortBtn.addEventListener('click', function () {
      ascending = !ascending;
      if (sortLabel) sortLabel.textContent = ascending ? 'Oldest first' : 'Newest first';
      if (sortIcon)  sortIcon.textContent  = ascending ? '↑' : '↓';
      sortItems();
      applyFilter();
    });
  }
})();
</script>
