---
layout: default
title: Knowledge Graph
nav_order: 10
permalink: /graph/
search_exclude: true
---

# Knowledge Graph

Visual map of all pages and their connections. **Nodes** are content pages; **solid edges** are explicit internal links; **dashed edges** connect pages sharing a specific topic tag.

Click a node to open its page. Drag to rearrange. Scroll to zoom.

<script>
var GRAPH_DATA_URL = '{{ "/assets/graph-data.json" | relative_url }}';
var SITE_BASEURL = '{{ site.baseurl }}';
</script>

<div id="graph-controls" style="display:flex;flex-wrap:wrap;gap:0.5rem 1.5rem;align-items:center;margin-bottom:0.75rem;font-size:0.875rem;">
  <strong>Nodes:</strong>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" class="type-filter" value="reading" checked> <span class="legend-dot" data-type="reading"></span> Reading</label>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" class="type-filter" value="synthesis" checked> <span class="legend-dot" data-type="synthesis"></span> Synthesis</label>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" class="type-filter" value="knowledge-base" checked> <span class="legend-dot" data-type="knowledge-base"></span> Knowledge Base</label>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" class="type-filter" value="journal" checked> <span class="legend-dot" data-type="journal"></span> Journal</label>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" class="type-filter" value="survey" checked> <span class="legend-dot" data-type="survey"></span> Survey</label>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" class="type-filter" value="strange" checked> <span class="legend-dot" data-type="strange"></span> Strange</label>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" class="type-filter" value="reference" checked> <span class="legend-dot" data-type="reference"></span> Reference</label>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" class="type-filter" value="other" checked> <span class="legend-dot" data-type="other"></span> Other</label>
</div>

<div id="edge-controls" style="display:flex;flex-wrap:wrap;gap:0.5rem 1.5rem;align-items:center;margin-bottom:1rem;font-size:0.875rem;">
  <strong>Edges:</strong>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" id="show-link-edges" checked> <svg width="24" height="10"><line x1="0" y1="5" x2="24" y2="5" stroke="#60a5fa" stroke-width="2"/></svg> Internal link</label>
  <label style="display:inline-flex;align-items:center;gap:0.3rem;cursor:pointer;"><input type="checkbox" id="show-tag-edges" checked> <svg width="24" height="10"><line x1="0" y1="5" x2="24" y2="5" stroke="#888" stroke-width="1.5" stroke-dasharray="4 3"/></svg> Shared tag</label>
</div>

<div id="graph-container" style="width:100%;height:580px;border:1px solid var(--border-color,#333);border-radius:6px;overflow:hidden;background:var(--code-background-color,#1e1e2e);position:relative;">
  <svg id="graph-svg" style="width:100%;height:100%;"></svg>
  <div id="graph-tooltip" style="position:absolute;display:none;background:var(--code-background-color,#1e1e2e);border:1px solid var(--border-color,#444);border-radius:4px;padding:0.4rem 0.6rem;font-size:0.8rem;pointer-events:none;max-width:240px;z-index:10;"></div>
  <div id="graph-loading" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:0.9rem;color:#888;">Loading graph…</div>
</div>

<p style="font-size:0.8rem;color:#888;margin-top:0.5rem;">
  Shared-tag edges only appear for tags used by few pages (see <code>MAX_SHARED_TAG_PAGES</code> in <code>generate-graph.py</code>). Run <code>make graph</code> after adding content to refresh.
</p>

<style>
.legend-dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: 1.5px solid rgba(255,255,255,0.3);
}
.legend-dot[data-type="reading"]        { background: #4a9eff; }
.legend-dot[data-type="synthesis"]      { background: #4ade80; }
.legend-dot[data-type="knowledge-base"] { background: #facc15; }
.legend-dot[data-type="journal"]        { background: #94a3b8; }
.legend-dot[data-type="survey"]         { background: #2dd4bf; }
.legend-dot[data-type="strange"]        { background: #c084fc; }
.legend-dot[data-type="reference"]      { background: #fb923c; }
.legend-dot[data-type="other"]          { background: #6b7280; }
</style>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
(function () {
  var TYPE_COLOR = {
    'reading':        '#4a9eff',
    'synthesis':      '#4ade80',
    'knowledge-base': '#facc15',
    'journal':        '#94a3b8',
    'survey':         '#2dd4bf',
    'strange':        '#c084fc',
    'reference':      '#fb923c',
    'other':          '#6b7280'
  };

  function nodeColor(type) {
    return TYPE_COLOR[type] || TYPE_COLOR['other'];
  }

  // --- DOM refs ---
  var container  = document.getElementById('graph-container');
  var svgEl      = document.getElementById('graph-svg');
  var tooltip    = document.getElementById('graph-tooltip');
  var loadingEl  = document.getElementById('graph-loading');

  // --- Dimensions ---
  var W = container.clientWidth  || 800;
  var H = container.clientHeight || 580;

  // --- SVG + zoom ---
  var svg = d3.select(svgEl);
  var g   = svg.append('g');

  var zoom = d3.zoom()
    .scaleExtent([0.15, 5])
    .on('zoom', function (event) { g.attr('transform', event.transform); });
  svg.call(zoom);

  // --- Arrow marker for link edges ---
  svg.append('defs').append('marker')
    .attr('id', 'arrow')
    .attr('viewBox', '0 -4 8 8')
    .attr('refX', 16)
    .attr('refY', 0)
    .attr('markerWidth', 6)
    .attr('markerHeight', 6)
    .attr('orient', 'auto')
    .append('path')
    .attr('d', 'M0,-4L8,0L0,4')
    .attr('fill', '#60a5fa')
    .attr('opacity', 0.7);

  // --- Force simulation ---
  var simulation = d3.forceSimulation()
    .force('link',    d3.forceLink().id(function (d) { return d.id; }).distance(120).strength(0.4))
    .force('charge',  d3.forceManyBody().strength(-220))
    .force('center',  d3.forceCenter(W / 2, H / 2))
    .force('collide', d3.forceCollide(22));

  // --- State ---
  var allNodes = [], allEdges = [];
  var linkSel, nodeSel;
  var activeTypes = new Set(Object.keys(TYPE_COLOR));
  var showLinkEdges = true;
  var showTagEdges  = true;

  // --- Load data ---
  fetch(GRAPH_DATA_URL)
    .then(function (r) { return r.json(); })
    .then(function (data) {
      loadingEl.style.display = 'none';
      allNodes = data.nodes;
      allEdges = data.edges;
      buildGraph();
      wireFilters();
    })
    .catch(function (err) {
      loadingEl.textContent = 'Failed to load graph data.';
      console.error('Graph load error:', err);
    });

  // --- Build graph from allNodes / allEdges ---
  function buildGraph() {
    g.selectAll('*').remove();

    // Deep-copy nodes so simulation doesn't mutate original objects
    var nodes = allNodes
      .filter(function (n) { return activeTypes.has(n.type || 'other'); })
      .map(function (n) { return Object.assign({}, n); });

    var nodeSet = new Set(nodes.map(function (n) { return n.id; }));

    var edges = allEdges.filter(function (e) {
      var sid = typeof e.source === 'object' ? e.source.id : e.source;
      var tid = typeof e.target === 'object' ? e.target.id : e.target;
      if (!nodeSet.has(sid) || !nodeSet.has(tid)) return false;
      if (e.type === 'internal-link') return showLinkEdges;
      if (e.type === 'shared-tag')    return showTagEdges;
      return true;
    }).map(function (e) {
      return {
        source: typeof e.source === 'object' ? e.source.id : e.source,
        target: typeof e.target === 'object' ? e.target.id : e.target,
        type:   e.type,
        tag:    e.tag
      };
    });

    // Edge layer
    linkSel = g.append('g').attr('class', 'edges')
      .selectAll('line')
      .data(edges)
      .join('line')
      .attr('stroke', function (e) {
        return e.type === 'internal-link' ? '#60a5fa' : '#888';
      })
      .attr('stroke-width', function (e) {
        return e.type === 'internal-link' ? 1.8 : 1;
      })
      .attr('stroke-dasharray', function (e) {
        return e.type === 'shared-tag' ? '5 4' : null;
      })
      .attr('stroke-opacity', function (e) {
        return e.type === 'internal-link' ? 0.75 : 0.45;
      })
      .attr('marker-end', function (e) {
        return e.type === 'internal-link' ? 'url(#arrow)' : null;
      });

    // Node layer
    nodeSel = g.append('g').attr('class', 'nodes')
      .selectAll('g')
      .data(nodes)
      .join('g')
      .attr('cursor', 'pointer')
      .call(
        d3.drag()
          .on('start', function (event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x; d.fy = d.y;
          })
          .on('drag', function (event, d) {
            d.fx = event.x; d.fy = event.y;
          })
          .on('end', function (event, d) {
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null; d.fy = null;
          })
      )
      .on('click', function (event, d) {
        event.stopPropagation();
        window.location.href = SITE_BASEURL + '/' + d.id + '/';
      })
      .on('mouseover', function (event, d) {
        var tags = (d.tags || []).join(', ') || '—';
        tooltip.innerHTML =
          '<strong>' + escapeHtml(d.label) + '</strong>' +
          '<br><span style="opacity:0.7">' + escapeHtml(d.type) + '</span>' +
          '<br><span style="opacity:0.6;font-size:0.75em">' + escapeHtml(tags) + '</span>';
        tooltip.style.display = 'block';
      })
      .on('mousemove', function (event) {
        var rect = container.getBoundingClientRect();
        var x = event.clientX - rect.left + 12;
        var y = event.clientY - rect.top  - 10;
        // Keep inside container
        if (x + 250 > rect.width)  x = event.clientX - rect.left - 260;
        if (y + 80  > rect.height) y = event.clientY - rect.top  - 80;
        tooltip.style.left = x + 'px';
        tooltip.style.top  = y + 'px';
      })
      .on('mouseout', function () {
        tooltip.style.display = 'none';
      });

    nodeSel.append('circle')
      .attr('r', 9)
      .attr('fill', function (d) { return nodeColor(d.type); })
      .attr('stroke', '#fff')
      .attr('stroke-width', 1.5)
      .attr('stroke-opacity', 0.5);

    nodeSel.append('text')
      .attr('x', 12)
      .attr('y', 4)
      .attr('font-size', '10px')
      .attr('fill', 'currentColor')
      .attr('pointer-events', 'none')
      .text(function (d) {
        return d.label.length > 32 ? d.label.slice(0, 30) + '…' : d.label;
      });

    // Wire simulation
    simulation
      .nodes(nodes)
      .force('link', d3.forceLink(edges).id(function (d) { return d.id; }).distance(120).strength(0.4))
      .force('charge', d3.forceManyBody().strength(-220))
      .force('center', d3.forceCenter(W / 2, H / 2))
      .force('collide', d3.forceCollide(22))
      .alpha(0.8)
      .restart()
      .on('tick', function () {
        linkSel
          .attr('x1', function (e) { return e.source.x; })
          .attr('y1', function (e) { return e.source.y; })
          .attr('x2', function (e) { return e.target.x; })
          .attr('y2', function (e) { return e.target.y; });
        nodeSel.attr('transform', function (d) {
          return 'translate(' + d.x + ',' + d.y + ')';
        });
      });
  }

  // --- Filters ---
  function wireFilters() {
    d3.selectAll('.type-filter').on('change', function () {
      activeTypes = new Set();
      d3.selectAll('.type-filter').each(function () {
        if (this.checked) activeTypes.add(this.value);
      });
      buildGraph();
    });

    document.getElementById('show-link-edges').addEventListener('change', function () {
      showLinkEdges = this.checked;
      buildGraph();
    });

    document.getElementById('show-tag-edges').addEventListener('change', function () {
      showTagEdges = this.checked;
      buildGraph();
    });
  }

  // --- Utility ---
  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
})();
</script>
