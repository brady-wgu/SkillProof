/* ============================================================================
   SkillProof — shared table controls (filter chips + search + sort)
   Site-wide standard (2026-06-01).

   Auto-injects a control bar above every <table> on the page:
     - Filter chips  : derived from the table's most categorical column
                       (Status/Role/Type/etc.); always at least "All".
     - Search box    : hides data rows whose text doesn't match the query.
     - Sort dropdown : per-column ascending/descending.

   Handles the heterogeneous tables across the storyboards:
     - Standard tables (<thead>, or a first row of all-<th>)  -> chips+search+sort
     - Tables with footer / spanning rows  -> those rows are pinned & always
       shown; sort/filter act only on the uniform data rows.
     - Key-value tables (each row = <th>label + <td>value)   -> search only
     - Tables that already have bespoke .chip-filter controls -> left untouched
       (skipped) so their richer existing controls keep working.

   Re-runnable via window.SkillProofTableControls.init().
   ============================================================================ */
(function () {
  'use strict';

  function txt(el) { return (el ? el.textContent : '').replace(/\s+/g, ' ').trim(); }
  function cellTexts(row) { return Array.prototype.map.call(row.cells, txt); }
  function hasSpan(row) {
    return Array.prototype.some.call(row.cells, function (c) { return c.colSpan > 1 || c.rowSpan > 1; });
  }
  function numericKey(s) {
    var m = String(s).replace(/[$,%\s]+/g, '').match(/-?\d+(\.\d+)?/);
    return m ? parseFloat(m[0]) : null;
  }

  // Skip tables that already have curated chip controls just before them.
  function hasBespokeChips(table) {
    var wrap = table.closest('.table-scroll, .heatmap-scroll-container') || table;
    var nodes = [];
    [wrap, table].forEach(function (n) {
      var p = n.previousElementSibling, hops = 0;
      while (p && hops < 4) { nodes.push(p); p = p.previousElementSibling; hops++; }
    });
    return nodes.some(function (n) {
      return n.classList && (n.classList.contains('chip-filter') ||
        (n.querySelector && n.querySelector('.chip-filter')));
    });
  }

  // Determine header + data-row layout.
  function analyze(table, body) {
    var rows = Array.prototype.slice.call(body.rows);
    function split(count, dataPool) {
      var data = [], others = [];
      dataPool.forEach(function (r) {
        if (r.cells.length === count && !hasSpan(r)) data.push(r); else others.push(r);
      });
      return { data: data, others: others };
    }
    if (table.tHead && table.tHead.rows.length) {
      var hr = table.tHead.rows[table.tHead.rows.length - 1];
      var s = split(hr.cells.length, rows);
      return { mode: 'header', count: hr.cells.length, labels: cellTexts(hr), data: s.data, others: s.others, all: rows };
    }
    var r0 = rows[0];
    var allTh = r0.cells.length > 0 && Array.prototype.every.call(r0.cells, function (c) { return c.tagName === 'TH'; });
    if (allTh && r0.cells.length >= 2) {
      var s2 = split(r0.cells.length, rows.slice(1));
      return { mode: 'header', count: r0.cells.length, labels: cellTexts(r0), data: s2.data, others: s2.others, headerRow: r0, all: rows };
    }
    // key-value / headerless -> search only
    var maxCells = rows.reduce(function (m, r) { return Math.max(m, r.cells.length); }, 0);
    return { mode: 'kv', count: maxCells || 1, labels: [], data: rows.filter(function (r) { return !hasSpan(r); }), others: rows.filter(hasSpan), all: rows };
  }

  function pickCategory(labels, dataRows) {
    var preferred = /(status|state|type|role|category|risk|tier|level|severity|result|outcome|provider|plan)/i;
    var best = -1, bestScore = -1, colCount = dataRows.length ? dataRows[0].cells.length : 0;
    for (var c = 0; c < colCount; c++) {
      var seen = {}, count = 0, numCount = 0, dateCount = 0, badCol = false;
      var junkRe = /^(—|–|-|n\/a|n\.a\.|none|null|all|tbd)$/i;
      var dateRe = /(\d{1,2}\s+\w{3,}\s+\d{2,4})|(\d{4}-\d{2}-\d{2})|(\d{1,2}\/\d{1,2}\/\d{2,4})/;
      for (var r = 0; r < dataRows.length; r++) {
        var cell = dataRows[r].cells[c]; if (!cell) continue;
        var raw = txt(cell); if (raw === '' || junkRe.test(raw)) continue;       // ignore placeholders
        if (raw.length > 28 || raw.split(/\s+/).length > 4 || /[.!?]$/.test(raw)) { badCol = true; break; } // sentence-like -> not a category
        var v = raw.toLowerCase();
        seen[v] = (seen[v] || 0) + 1; count++;
        if (numericKey(raw) !== null) numCount++;
        if (dateRe.test(raw)) dateCount++;
      }
      if (badCol || count === 0) continue;
      var distinct = Object.keys(seen).length;
      if (distinct < 2 || distinct > 6 || distinct >= count) continue;
      if ((numCount + dateCount) / count > 0.5) continue;  // skip date / number columns
      var score = (count - distinct) + (6 - distinct) + ((labels[c] && preferred.test(labels[c])) ? 100 : 0);
      if (score > bestScore) { bestScore = score; best = c; }
    }
    if (best === -1) return null;
    var order = [], label = {}, junkRe2 = /^(—|–|-|n\/a|n\.a\.|none|null|all|tbd)$/i;
    dataRows.forEach(function (row) {
      var cc = row.cells[best]; if (!cc) return;
      var raw = txt(cc); if (!raw || junkRe2.test(raw)) return;
      var key = raw.toLowerCase();
      if (!(key in label)) { label[key] = raw; order.push(key); }
    });
    return { index: best, keys: order, label: label };
  }

  function initOne(table) {
    if (table.dataset.tcInit) return;
    if (table.closest('[data-no-controls]')) return;
    var body = table.tBodies[0];
    if (!body || body.rows.length === 0) return;
    if (hasBespokeChips(table)) { table.dataset.tcInit = 'curated'; return; }

    // Skip key-value info boxes (no <thead>, every row starts with a <th> label) — these are info panels, not data tables
    var noThead = !(table.tHead && table.tHead.rows.length);
    if (noThead && Array.prototype.every.call(body.rows, function (r) { return r.cells[0] && r.cells[0].tagName === 'TH'; })) {
      table.dataset.tcInit = 'kv-skip'; return;
    }

    var info = analyze(table, body);
    if (info.count === 0) return;
    table.dataset.tcInit = '1';

    var sortable = info.mode === 'header' && info.count >= 2 && info.data.length >= 2;
    var cat = (info.mode === 'header') ? pickCategory(info.labels, info.data) : null;
    var dataSet = info.data;          // rows we filter/sort
    var origOrder = info.all.slice();  // for "Default order"
    var activeChip = '__all__';
    var tableName = table.getAttribute('aria-label');

    var bar = document.createElement('div');
    bar.className = 'table-controls';

    // chips
    var chipWrap = document.createElement('div'); chipWrap.className = 'tc-chips';
    var fl = document.createElement('span'); fl.className = 'tc-label'; fl.textContent = 'Filter:';
    chipWrap.appendChild(fl);
    var defs = [{ label: 'All', value: '__all__' }];
    if (cat) cat.keys.forEach(function (k) { defs.push({ label: cat.label[k], value: k }); });
    defs.forEach(function (d, i) {
      var chip = document.createElement('button');
      chip.type = 'button'; chip.className = 'tc-chip' + (i === 0 ? ' active' : '');
      chip.textContent = d.label; chip.setAttribute('aria-pressed', i === 0 ? 'true' : 'false');
      chip.addEventListener('click', function () {
        activeChip = d.value;
        chipWrap.querySelectorAll('.tc-chip').forEach(function (x) { x.classList.remove('active'); x.setAttribute('aria-pressed', 'false'); });
        chip.classList.add('active'); chip.setAttribute('aria-pressed', 'true');
        apply();
      });
      chipWrap.appendChild(chip);
    });
    bar.appendChild(chipWrap);

    // right cluster: search + sort
    var right = document.createElement('div'); right.className = 'tc-right';
    var sWrap = document.createElement('span'); sWrap.className = 'tc-search';
    var sIcon = document.createElement('span'); sIcon.className = 'material-icons-outlined'; sIcon.textContent = 'search'; sIcon.setAttribute('aria-hidden', 'true');
    var input = document.createElement('input'); input.type = 'search'; input.placeholder = 'Search…';
    input.setAttribute('aria-label', 'Search table' + (tableName ? ': ' + tableName : ''));
    input.addEventListener('input', apply);
    sWrap.appendChild(sIcon); sWrap.appendChild(input); right.appendChild(sWrap);

    if (sortable) {
      var sortLbl = document.createElement('span'); sortLbl.className = 'tc-label'; sortLbl.textContent = 'Sort:';
      var sel = document.createElement('select'); sel.className = 'tc-sort';
      sel.setAttribute('aria-label', 'Sort table' + (tableName ? ': ' + tableName : ''));
      var od = document.createElement('option'); od.value = ''; od.textContent = 'Default order'; sel.appendChild(od);
      info.labels.forEach(function (h, idx) {
        if (!h || /^(actions?|controls?)$/i.test(h)) return;
        var a = document.createElement('option'); a.value = idx + ':asc'; a.textContent = h + ' ↑'; sel.appendChild(a);
        var b = document.createElement('option'); b.value = idx + ':desc'; b.textContent = h + ' ↓'; sel.appendChild(b);
      });
      sel.addEventListener('change', function () {
        if (!sel.value) { origOrder.forEach(function (r) { body.appendChild(r); }); apply(); return; }
        var p = sel.value.split(':'), col = +p[0], dir = p[1] === 'desc' ? -1 : 1;
        dataSet.slice().sort(function (x, y) {
          var xv = txt(x.cells[col]), yv = txt(y.cells[col]), xn = numericKey(xv), yn = numericKey(yv), c;
          if (xn !== null && yn !== null) c = xn - yn; else c = xv.toLowerCase().localeCompare(yv.toLowerCase());
          return c * dir;
        }).forEach(function (r) { body.appendChild(r); });
        info.others.forEach(function (r) { body.appendChild(r); }); // pin non-data rows after
        apply();
      });
      right.appendChild(sortLbl); right.appendChild(sel);
    }
    bar.appendChild(right);

    // empty-state row
    var emptyRow = document.createElement('tr'); emptyRow.className = 'tc-empty-row';
    var emptyCell = document.createElement('td'); emptyCell.colSpan = info.count; emptyCell.textContent = 'No matching rows';
    emptyRow.appendChild(emptyCell); emptyRow.style.display = 'none'; body.appendChild(emptyRow);

    function apply() {
      var q = input.value.trim().toLowerCase();
      var ci = cat ? cat.index : -1, visible = 0;
      dataSet.forEach(function (row) {
        var okChip = (activeChip === '__all__') || (ci >= 0 && row.cells[ci] && txt(row.cells[ci]).toLowerCase() === activeChip);
        var okSearch = (q === '') || txt(row).toLowerCase().indexOf(q) !== -1;
        var show = okChip && okSearch;
        row.style.display = show ? '' : 'none';
        if (show) visible++;
      });
      emptyRow.style.display = (visible === 0 && dataSet.length > 0) ? '' : 'none';
    }

    var wrapper = table.closest('.table-scroll, .heatmap-scroll-container') || table;
    wrapper.parentNode.insertBefore(bar, wrapper);
  }

  function init(scope) {
    var tables = (scope || document).querySelectorAll('table');
    Array.prototype.forEach.call(tables, initOne);
  }

  /* ---- Universal search box for bespoke filter-chip bars ----
     Adds a text search to any .chip-filter bar that lacks one (heatmaps, card
     grids, curated tables). Coexists with the existing chips: a .tc-search-hide
     class (display:none !important) ANDs with whatever the chips already hide. */
  function collectionFor(bar) {
    var el = bar.nextElementSibling, hops = 0;
    while (el && hops < 6) {
      var hg = el.matches('.heatmap-grid') ? el : el.querySelector('.heatmap-grid');
      if (hg) return { type: 'heatmap', el: hg };
      var tb = el.matches('table') ? el : el.querySelector('table');
      if (tb && tb.tBodies && tb.tBodies[0]) return { type: 'table', el: tb };
      var grid = el.matches('#courses-grid, .row') ? el : el.querySelector('#courses-grid, .row');
      if (grid && grid.querySelectorAll('[data-course-code], .section-card').length > 1) return { type: 'cards', el: grid };
      el = el.nextElementSibling; hops++;
    }
    return null;
  }
  function alreadySearched(bar, coll) {
    if (bar.querySelector('input[type="search"]')) return true;
    if (coll && coll.type === 'table') {
      var w = coll.el.closest('.table-scroll, .heatmap-scroll-container') || coll.el;
      var p = w.previousElementSibling;
      if (p && p.classList && p.classList.contains('table-controls')) return true;
    }
    return false;
  }
  function heatmapGroups(grid) {
    var groups = [], cur = null;
    Array.prototype.forEach.call(grid.children, function (ch) {
      if (ch.classList.contains('heatmap-row-label')) { cur = { label: ch, els: [ch] }; groups.push(cur); }
      else if (ch.classList.contains('heatmap-cell') && cur) { cur.els.push(ch); }
    });
    return groups;
  }
  /* Adds a Sort dropdown to a bespoke chip-filter bar whose collection is a TABLE
     (not heatmaps/cards — row-sorting those is meaningless). Reuses txt/numericKey. */
  function addChipBarSort(bar, table) {
    if (bar.querySelector('.tc-sort')) return;
    var body = table.tBodies && table.tBodies[0]; if (!body) return;
    var headRow = table.tHead && table.tHead.rows[0]; if (!headRow) return;
    var headers = Array.prototype.map.call(headRow.cells, function (c) { return txt(c); });
    var hasSortable = false;
    headers.forEach(function (h) { if (h && !/^(actions?|controls?)$/i.test(h)) hasSortable = true; });
    if (!hasSortable) return;
    var origRows = Array.prototype.filter.call(body.rows, function (r) { return !r.classList.contains('tc-empty-row'); });
    var lbl = document.createElement('span'); lbl.className = 'tc-label'; lbl.style.marginLeft = '8px'; lbl.textContent = 'Sort:';
    var sel = document.createElement('select'); sel.className = 'tc-sort'; sel.setAttribute('aria-label', 'Sort table');
    var od = document.createElement('option'); od.value = ''; od.textContent = 'Default order'; sel.appendChild(od);
    headers.forEach(function (h, idx) {
      if (!h || /^(actions?|controls?)$/i.test(h)) return;
      var a = document.createElement('option'); a.value = idx + ':asc'; a.textContent = h + ' ↑'; sel.appendChild(a);
      var b = document.createElement('option'); b.value = idx + ':desc'; b.textContent = h + ' ↓'; sel.appendChild(b);
    });
    sel.addEventListener('change', function () {
      if (!sel.value) { origRows.forEach(function (r) { body.appendChild(r); }); }
      else {
        var p = sel.value.split(':'), col = +p[0], dir = p[1] === 'desc' ? -1 : 1;
        origRows.slice().sort(function (x, y) {
          var xv = txt(x.cells[col]), yv = txt(y.cells[col]), xn = numericKey(xv), yn = numericKey(yv), c;
          if (xn !== null && yn !== null) c = xn - yn; else c = xv.toLowerCase().localeCompare(yv.toLowerCase());
          return c * dir;
        }).forEach(function (r) { body.appendChild(r); });
      }
      var er = body.querySelector('.tc-empty-row'); if (er) body.appendChild(er);
    });
    bar.appendChild(lbl); bar.appendChild(sel);
  }

  function addChipBarSearch() {
    var bars = [], seen = [];
    document.querySelectorAll('.chip-filter').forEach(function (c) {
      if (c.parentElement && seen.indexOf(c.parentElement) === -1) { seen.push(c.parentElement); bars.push(c.parentElement); }
    });
    bars.forEach(function (bar) {
      if (bar.dataset.tcSearch) return;
      var coll = collectionFor(bar);
      if (!coll) { bar.dataset.tcSearch = 'none'; return; }
      if (alreadySearched(bar, coll)) { bar.dataset.tcSearch = 'skip'; return; }
      bar.dataset.tcSearch = '1';
      var wrap = document.createElement('span'); wrap.className = 'tc-chip-search'; wrap.style.marginLeft = 'auto';
      var icon = document.createElement('span'); icon.className = 'material-icons-outlined'; icon.textContent = 'search'; icon.setAttribute('aria-hidden', 'true');
      var input = document.createElement('input'); input.type = 'search'; input.placeholder = 'Search…'; input.setAttribute('aria-label', 'Search');
      wrap.appendChild(icon); wrap.appendChild(input); bar.appendChild(wrap);
      if (coll.type === 'table') addChipBarSort(bar, coll.el);
      input.addEventListener('input', function () {
        var q = input.value.trim().toLowerCase();
        if (coll.type === 'heatmap') {
          heatmapGroups(coll.el).forEach(function (g) {
            var show = q === '' || g.label.textContent.toLowerCase().indexOf(q) !== -1;
            g.els.forEach(function (e) { e.classList.toggle('tc-search-hide', !show); });
          });
        } else if (coll.type === 'table') {
          Array.prototype.forEach.call(coll.el.tBodies[0].rows, function (r) {
            if (r.classList.contains('tc-empty-row')) return;
            r.classList.toggle('tc-search-hide', !(q === '' || r.textContent.toLowerCase().indexOf(q) !== -1));
          });
        } else if (coll.type === 'cards') {
          Array.prototype.forEach.call(coll.el.children, function (card) {
            card.classList.toggle('tc-search-hide', !(q === '' || card.textContent.toLowerCase().indexOf(q) !== -1));
          });
        }
      });
    });
  }

  /* ---- Sticky section nav + scroll-spy for long analytics pages ----
     Tag a scroll container with [data-analytics-nav] and each section start with
     <span class="an-anchor" data-an-label="Label"></span>. Builds a sticky tab bar
     that smooth-scrolls to each section and highlights the active one on scroll. */
  function initAnalyticsNav() {
    document.querySelectorAll('[data-analytics-nav]').forEach(function (scope) {
      if (scope.dataset.anInit) return;
      var anchors = Array.prototype.slice.call(scope.querySelectorAll('[data-an-label]'));
      if (anchors.length < 2) return;
      scope.dataset.anInit = '1';
      var nav = document.createElement('nav'); nav.className = 'an-tabs'; nav.setAttribute('aria-label', 'Analytics sections');
      var tabs = [];
      anchors.forEach(function (a, i) {
        if (!a.id) a.id = 'an-sec-' + i;
        var btn = document.createElement('button'); btn.type = 'button';
        btn.className = 'an-tab' + (i === 0 ? ' active' : '');
        btn.textContent = a.dataset.anLabel;
        btn.setAttribute('aria-current', i === 0 ? 'true' : 'false');
        btn.addEventListener('click', function () { a.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
        nav.appendChild(btn); tabs.push(btn);
      });
      var anH1 = scope.querySelector('h1');
      if (anH1) { var anTop = anH1; while (anTop.parentNode && anTop.parentNode !== scope) anTop = anTop.parentNode; if (anTop.parentNode === scope) anTop.insertAdjacentElement('afterend', nav); else scope.insertBefore(nav, scope.firstChild); }
      else scope.insertBefore(nav, scope.firstChild);
      if ('IntersectionObserver' in window) {
        var obs = new IntersectionObserver(function (entries) {
          entries.forEach(function (e) {
            if (!e.isIntersecting) return;
            var idx = anchors.indexOf(e.target);
            tabs.forEach(function (t) { t.classList.remove('active'); t.setAttribute('aria-current', 'false'); });
            if (tabs[idx]) { tabs[idx].classList.add('active'); tabs[idx].setAttribute('aria-current', 'true'); }
          });
        }, { rootMargin: '0px 0px -75% 0px', threshold: 0 });
        anchors.forEach(function (a) { obs.observe(a); });
      }
    });
  }

  function run() { init(document); addChipBarSearch(); initAnalyticsNav(); }
  if (document.readyState !== 'loading') run();
  else document.addEventListener('DOMContentLoaded', run);
  window.SkillProofTableControls = { init: init };
})();
