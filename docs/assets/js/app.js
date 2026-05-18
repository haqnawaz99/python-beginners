// ============================================================
// Python for Beginners — Course Website
// Tab switching + File explorer + Markdown + Syntax highlighting
// ============================================================

document.addEventListener('DOMContentLoaded', function () {

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── Scroll reveal (index steps + module cards) ─────────────────
  var revealEls = document.querySelectorAll('.reveal-on-scroll');
  revealEls.forEach(function (el, i) {
    el.style.setProperty('--reveal-delay', Math.min(i * 50, 400) + 'ms');
    if (reduceMotion) {
      el.classList.add('is-revealed');
    }
  });
  if (!reduceMotion && revealEls.length && 'IntersectionObserver' in window) {
    var revealObs = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          obs.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.12 });
    revealEls.forEach(function (el) {
      revealObs.observe(el);
    });
  } else if (!reduceMotion && revealEls.length) {
    revealEls.forEach(function (el) { el.classList.add('is-revealed'); });
  }

  // ── Markdown rendering + syntax highlight (order matters) ──
  if (window.marked) {
    marked.setOptions({ breaks: true, gfm: true });

    [['src-notes', 'md-notes'], ['src-practice', 'md-practice'], ['src-assessment', 'md-assessment'], ['src-setup', 'md-setup']]
      .forEach(function ([srcId, targetId]) {
        var src    = document.getElementById(srcId);
        var target = document.getElementById(targetId);
        if (!src || !target) return;
        try {
          target.innerHTML = marked.parse(JSON.parse(src.textContent));
          target.querySelectorAll('input[type="checkbox"]').forEach(function (cb) {
            cb.removeAttribute('disabled');
          });
        } catch (e) {
          target.textContent = 'Content could not be loaded.';
        }
      });
  }

  if (window.hljs) {
    hljs.highlightAll();
  }

  // ── Tab switching ────────────────────────────────────────
  document.querySelectorAll('.tab-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.tab-btn').forEach(function (b) {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      document.querySelectorAll('.tab-pane').forEach(function (p) { p.classList.remove('active'); });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      var pane = document.getElementById('tab-' + btn.dataset.tab);
      if (pane) pane.classList.add('active');
    });
  });

  // ── File explorer (Lessons tab) ──────────────────────────
  var fileItems      = document.querySelectorAll('.file-item');
  var codePanels     = document.querySelectorAll('.code-panel');
  var viewerFilename = document.getElementById('viewer-filename');
  var viewerBadge    = document.getElementById('viewer-badge');

  fileItems.forEach(function (item) {
    item.addEventListener('click', function () {
      // Update active states
      fileItems.forEach(function (i) { i.classList.remove('active'); });
      codePanels.forEach(function (p) { p.classList.remove('active'); });

      item.classList.add('active');

      var target = document.getElementById(item.dataset.target);
      if (target) target.classList.add('active');

      // Update header filename + badge
      if (viewerFilename) viewerFilename.textContent = item.dataset.filename;
      if (viewerBadge)    viewerBadge.className = 'badge ' + item.dataset.badgeClass;
      if (viewerBadge)    viewerBadge.textContent = item.dataset.label;
    });
  });

  // ── Copy button ──────────────────────────────────────────
  var copyBtn = document.getElementById('copy-btn');
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var activePanel = document.querySelector('.code-panel.active');
      if (!activePanel) return;
      var code = activePanel.querySelector('code');
      if (!code) return;

      function setCopyLabel(text) {
        var label = copyBtn.querySelector('.copy-label');
        if (label) label.textContent = text;
        else copyBtn.childNodes.forEach(function (n) {
          if (n.nodeType === 3) n.textContent = text;
        });
      }

      navigator.clipboard.writeText(code.textContent).then(function () {
        setCopyLabel('Copied!');
        copyBtn.classList.add('copied');
        setTimeout(function () {
          setCopyLabel('Copy');
          copyBtn.classList.remove('copied');
        }, 2000);
      }).catch(function () {
        var ta = document.createElement('textarea');
        ta.value = code.textContent;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        setCopyLabel('Copied!');
        setTimeout(function () { setCopyLabel('Copy'); }, 2000);
      });
    });
  }

  // ── Mobile sidebar toggle ────────────────────────────────
  var menuToggle = document.getElementById('menuToggle');
  var sidebar    = document.getElementById('sidebar');

  if (menuToggle && sidebar) {
    menuToggle.addEventListener('click', function () {
      sidebar.classList.toggle('open');
    });
    sidebar.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { sidebar.classList.remove('open'); });
    });
    document.addEventListener('click', function (e) {
      if (sidebar.classList.contains('open') &&
          !sidebar.contains(e.target) && e.target !== menuToggle) {
        sidebar.classList.remove('open');
      }
    });
  }

});
