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

<style>
.search-container {
  max-width: 800px;
  margin: 0 auto;
}

#search-input {
  width: 100%;
  padding: 15px;
  font-size: 16px;
  border: 2px solid #e8e8e8;
  border-radius: 4px;
  margin-bottom: 30px;
  box-sizing: border-box;
}

#search-input:focus {
  outline: 3px solid #2a7ae2;
  outline-offset: 2px;
  border-color: #2a7ae2;
}

#results-container {
  list-style: none;
  padding: 0;
}

.search-result {
  padding: 20px;
  margin-bottom: 20px;
  border: 1px solid #e8e8e8;
  border-radius: 4px;
  background: #fafafa;
}

.search-result h3 {
  margin: 0 0 10px 0;
  font-size: 1.3em;
}

.search-result h3 a {
  color: #111;
  text-decoration: none;
}

.search-result h3 a:hover {
  color: #2a7ae2;
}

.search-meta {
  color: #828282;
  font-size: 0.9em;
  margin: 5px 0;
}

.search-summary {
  margin: 10px 0;
  line-height: 1.6;
}

.search-tags {
  color: #666;
  font-size: 0.9em;
  font-style: italic;
}
</style>
