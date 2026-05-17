// ============================================================
// Python for Beginners — Course Website
// Tab switching + File explorer + Markdown + Syntax highlighting
// ============================================================

document.addEventListener('DOMContentLoaded', function () {

  // ── Syntax highlighting ──────────────────────────────────
  if (window.hljs) {
    hljs.highlightAll();
  }

  // ── Markdown rendering ───────────────────────────────────
  if (window.marked) {
    marked.setOptions({ breaks: true, gfm: true });

    [['src-notes', 'md-notes'], ['src-practice', 'md-practice'], ['src-assessment', 'md-assessment']]
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

  // ── Tab switching ────────────────────────────────────────
  document.querySelectorAll('.tab-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.tab-btn').forEach(function (b) { b.classList.remove('active'); });
      document.querySelectorAll('.tab-pane').forEach(function (p) { p.classList.remove('active'); });
      btn.classList.add('active');
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

      navigator.clipboard.writeText(code.textContent).then(function () {
        copyBtn.textContent = 'Copied!';
        copyBtn.classList.add('copied');
        setTimeout(function () {
          copyBtn.textContent = 'Copy';
          copyBtn.classList.remove('copied');
        }, 2000);
      }).catch(function () {
        // Fallback for older browsers
        var ta = document.createElement('textarea');
        ta.value = code.textContent;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        copyBtn.textContent = 'Copied!';
        setTimeout(function () { copyBtn.textContent = 'Copy'; }, 2000);
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
