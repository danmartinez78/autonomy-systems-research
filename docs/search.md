---
layout: page
title: Search
permalink: /search/
---

# Search Knowledge Base

<div class="search-container">
  <input type="text" id="search-input" placeholder="Search for topics, tags, or keywords..." autofocus>
  <ul id="results-container"></ul>
</div>

<script src="https://unpkg.com/simple-jekyll-search@1.10.0/dest/simple-jekyll-search.min.js" 
        integrity="sha384-OLBgp1GsljhM2TJ+sbHjaiH9txEUvgdDTAzHv2P24donTt6/529l+9Ua0vFImLlb" 
        crossorigin="anonymous"></script>

<script>
  window.simpleJekyllSearch = SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '{{ site.baseurl }}/search.json',
    searchResultTemplate: '<li><div class="search-result"><h3><a href="{url}">{title}</a></h3>{{#type}}<p class="search-meta">{type}{{#date}} &middot; {date}{{/date}}</p>{{/type}}{{^type}}{{#date}}<p class="search-meta">{date}</p>{{/date}}{{/type}}{{#summary}}<p class="search-summary">{summary}</p>{{/summary}}{{#tags}}<p class="search-tags">Tags: {tags}</p>{{/tags}}</div></li>',
    noResultsText: '<li>No results found</li>',
    limit: 10,
    fuzzy: false,
    exclude: [],
    templateMiddleware: function(prop, value, template) {
      if (prop === 'tags' && Array.isArray(value)) {
        return value.join(', ');
      }
      return value;
    }
  })
</script>
