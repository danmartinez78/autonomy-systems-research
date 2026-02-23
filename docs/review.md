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

<div class="review-controls" role="search" aria-label="Filter review prompts">
  <label for="review-filter-type"><strong>Filter by type:</strong></label>
  <select id="review-filter-type" aria-controls="review-list review-empty-msg">
    <option value="">All types</option>
    <option value="reading">Reading Notes</option>
    <option value="synthesis">Syntheses</option>
    <option value="knowledge-base">Knowledge Base</option>
    <option value="survey">Surveys</option>
    <option value="journal">Journal</option>
    <option value="strange">Backlog of the Strange</option>
  </select>

  <label for="review-filter-tag" class="review-controls__label--spaced"><strong>Filter by tag:</strong></label>
  <select id="review-filter-tag" aria-controls="review-list review-empty-msg">
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

<div class="review-actions">
  <button id="review-randomize-btn" class="review-btn" type="button">Randomize Prompts</button>
  <button id="review-start-drill-btn" class="review-btn review-btn--primary" type="button">Start 10-Question Drill</button>
</div>

<section id="review-drill" class="review-drill" hidden aria-live="polite">
  <div class="review-drill__meta">
    <strong id="review-drill-progress">Question 1 of 10</strong>
    <button id="review-drill-end" class="review-btn" type="button">End Drill</button>
  </div>
  <p id="review-drill-question" class="review-drill__question"></p>
  <div id="review-drill-answer" class="review-drill__answer" hidden>
    <p id="review-drill-answer-text"></p>
    <a id="review-drill-source-link" href="#">Open source note</a>
  </div>
  <div class="review-drill__actions">
    <button id="review-drill-show-answer" class="review-btn" type="button">Show Answer</button>
    <button id="review-drill-next" class="review-btn review-btn--primary" type="button">Next</button>
  </div>
</section>

<div id="review-list" aria-live="polite">
{% for p in review_pages %}
  {% assign page_type = "" %}
  {% if p.parent == "Reading Notes" %}
    {% assign page_type = "reading" %}
  {% elsif p.parent == "Syntheses" %}
    {% assign page_type = "synthesis" %}
  {% elsif p.parent == "Knowledge Base" %}
    {% assign page_type = "knowledge-base" %}
  {% elsif p.parent == "Surveys" %}
    {% assign page_type = "survey" %}
  {% elsif p.parent == "The Backlog of the Strange" %}
    {% assign page_type = "strange" %}
  {% elsif p.parent == "Journal" %}
    {% assign page_type = "journal" %}
  {% endif %}
  {% if page_type == "" %}
    {% assign page_type = "other" %}
  {% endif %}
  {% assign page_tags_str = p.tags | join: "," | downcase %}
  <div class="review-entry" data-type="{{ page_type }}" data-tags="{{ page_tags_str }}">
    <h3>
      <a href="{{ p.url | relative_url }}">{{ p.title }}</a>
      {% if page_type != "" %}<span class="content-badge content-badge--{{ page_type }}">{% if page_type == "knowledge-base" %}Knowledge Base{% elsif page_type == "reading" %}Reading Note{% elsif page_type == "synthesis" %}Synthesis{% elsif page_type == "survey" %}Survey{% elsif page_type == "journal" %}Journal{% elsif page_type == "strange" %}Strange Seed{% else %}{{ page_type | capitalize }}{% endif %}</span>{% endif %}
    </h3>
    {% if p.tags %}
    <p class="post-meta">Tags: {{ p.tags | join: ", " }}</p>
    {% endif %}
    <ol class="review-question-list">
    {% for question in p.review_questions %}
      {% assign answer_text = "" %}
      {% if p.review_answers and p.review_answers[forloop.index0] %}
        {% assign answer_text = p.review_answers[forloop.index0] %}
      {% elsif p.summary %}
        {% assign answer_text = p.summary %}
      {% endif %}
      <li class="review-card"
          data-question="{{ question | escape }}"
          data-answer="{{ answer_text | escape }}"
          data-source-title="{{ p.title | escape }}"
          data-source-url="{{ p.url | relative_url }}">
        <p class="review-card__question">{{ question | escape }}</p>
        <div class="review-card__answer" hidden>
          {% if answer_text != "" %}
          <p>{{ answer_text | escape }}</p>
          {% else %}
          <p>Use the source note to derive the answer.</p>
          {% endif %}
          <a href="{{ p.url | relative_url }}">Open source note</a>
        </div>
        <button class="review-card__toggle review-btn" type="button">Show Answer</button>
      </li>
    {% endfor %}
    </ol>
  </div>
{% endfor %}
</div>

<p id="review-empty-msg" class="review-empty-msg" aria-live="polite"><em>No prompts match the selected filter.</em></p>

<script>
var DRILL_SIZE = 10;
var drillQueue = [];
var drillIndex = 0;

function applyReviewFilter() {
  var typeFilter = document.getElementById('review-filter-type').value;
  var tagFilter  = document.getElementById('review-filter-tag').value;
  var entries    = document.querySelectorAll('.review-entry');
  var visible    = 0;

  entries.forEach(function(el) {
    var type = el.getAttribute('data-type') || '';
    var tags = el.getAttribute('data-tags') || '';
    var normalizedTags = tags
      .split(',')
      .map(function (t) { return t.trim(); })
      .filter(function (t) { return t.length > 0; });

    var typeMatch = !typeFilter || type === typeFilter;
    var tagMatch  = !tagFilter || normalizedTags.indexOf(tagFilter.toLowerCase()) !== -1;

    if (typeMatch && tagMatch) {
      el.style.display = '';
      visible++;
    } else {
      el.style.display = 'none';
    }
  });

  var emptyMsg = document.getElementById('review-empty-msg');
  if (visible === 0) {
    emptyMsg.classList.add('review-empty-msg--visible');
  } else {
    emptyMsg.classList.remove('review-empty-msg--visible');
  }
}

function getVisibleCards() {
  var cards = [];
  document.querySelectorAll('.review-entry').forEach(function (entry) {
    if (entry.style.display === 'none') return;
    entry.querySelectorAll('.review-card').forEach(function (card) {
      cards.push(card);
    });
  });
  return cards;
}

function shuffleArray(items) {
  var arr = items.slice();
  for (var i = arr.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
  }
  return arr;
}

function randomizeVisiblePrompts() {
  var list = document.getElementById('review-list');
  var entries = Array.from(document.querySelectorAll('.review-entry')).filter(function (entry) {
    return entry.style.display !== 'none';
  });

  shuffleArray(entries).forEach(function (entry) {
    var questionList = entry.querySelector('.review-question-list');
    if (questionList) {
      var cards = Array.from(questionList.children);
      shuffleArray(cards).forEach(function (card) {
        questionList.appendChild(card);
      });
    }
    list.appendChild(entry);
  });
}

function startDrill() {
  var cards = getVisibleCards();
  if (cards.length === 0) {
    alert('No prompts match the current filters.');
    return;
  }

  drillQueue = shuffleArray(cards).slice(0, Math.min(DRILL_SIZE, cards.length)).map(function (card) {
    return {
      question: card.getAttribute('data-question') || '',
      answer: card.getAttribute('data-answer') || 'Use the source note to derive the answer.',
      sourceTitle: card.getAttribute('data-source-title') || 'Source note',
      sourceUrl: card.getAttribute('data-source-url') || '#'
    };
  });
  drillIndex = 0;
  renderDrill();
  document.getElementById('review-drill').hidden = false;
}

function renderDrill() {
  if (drillQueue.length === 0) return;
  var item = drillQueue[drillIndex];

  document.getElementById('review-drill-progress').textContent =
    'Question ' + (drillIndex + 1) + ' of ' + drillQueue.length;
  document.getElementById('review-drill-question').textContent = item.question;
  document.getElementById('review-drill-answer-text').textContent = item.answer;
  document.getElementById('review-drill-source-link').setAttribute('href', item.sourceUrl);
  document.getElementById('review-drill-source-link').textContent = 'Open ' + item.sourceTitle;

  document.getElementById('review-drill-answer').hidden = true;
  document.getElementById('review-drill-show-answer').textContent = 'Show Answer';
  document.getElementById('review-drill-next').textContent =
    drillIndex === drillQueue.length - 1 ? 'Finish Drill' : 'Next';
}

function advanceDrill() {
  if (drillQueue.length === 0) return;
  if (drillIndex >= drillQueue.length - 1) {
    endDrill();
    return;
  }
  drillIndex += 1;
  renderDrill();
}

function endDrill() {
  drillQueue = [];
  drillIndex = 0;
  document.getElementById('review-drill').hidden = true;
}

document.addEventListener('DOMContentLoaded', function () {
  var typeSelect = document.getElementById('review-filter-type');
  var tagSelect = document.getElementById('review-filter-tag');
  var randomizeBtn = document.getElementById('review-randomize-btn');
  var startDrillBtn = document.getElementById('review-start-drill-btn');
  var drillShowAnswerBtn = document.getElementById('review-drill-show-answer');
  var drillNextBtn = document.getElementById('review-drill-next');
  var drillEndBtn = document.getElementById('review-drill-end');

  if (typeSelect) {
    typeSelect.addEventListener('change', applyReviewFilter);
    typeSelect.addEventListener('keyup', function (event) {
      if (event.key === 'Enter') applyReviewFilter();
    });
  }

  if (tagSelect) {
    tagSelect.addEventListener('change', applyReviewFilter);
    tagSelect.addEventListener('keyup', function (event) {
      if (event.key === 'Enter') applyReviewFilter();
    });
  }

  document.querySelectorAll('.review-card__toggle').forEach(function (button) {
    button.addEventListener('click', function () {
      var card = button.closest('.review-card');
      var answer = card.querySelector('.review-card__answer');
      var isHidden = answer.hasAttribute('hidden');
      if (isHidden) {
        answer.removeAttribute('hidden');
        button.textContent = 'Hide Answer';
      } else {
        answer.setAttribute('hidden', 'hidden');
        button.textContent = 'Show Answer';
      }
    });
  });

  if (randomizeBtn) {
    randomizeBtn.addEventListener('click', randomizeVisiblePrompts);
  }
  if (startDrillBtn) {
    startDrillBtn.addEventListener('click', startDrill);
  }
  if (drillShowAnswerBtn) {
    drillShowAnswerBtn.addEventListener('click', function () {
      var answer = document.getElementById('review-drill-answer');
      var isHidden = answer.hasAttribute('hidden');
      if (isHidden) {
        answer.removeAttribute('hidden');
        drillShowAnswerBtn.textContent = 'Hide Answer';
      } else {
        answer.setAttribute('hidden', 'hidden');
        drillShowAnswerBtn.textContent = 'Show Answer';
      }
    });
  }
  if (drillNextBtn) {
    drillNextBtn.addEventListener('click', advanceDrill);
  }
  if (drillEndBtn) {
    drillEndBtn.addEventListener('click', endDrill);
  }
});
</script>

{% endif %}
