// ============================================================
// Python for Beginners — Course Website
// Tab switching + Markdown rendering + Syntax highlighting
// ============================================================

document.addEventListener('DOMContentLoaded', function () {

  // ── Syntax highlighting ──────────────────────────────────
  if (window.hljs) {
    hljs.highlightAll();
  }

  // ── Markdown rendering ───────────────────────────────────
  if (window.marked) {
    marked.setOptions({
      breaks: true,
      gfm: true,
    });

    const mdPairs = [
      ['src-notes',      'md-notes'],
      ['src-practice',   'md-practice'],
      ['src-assessment', 'md-assessment'],
    ];

    mdPairs.forEach(function ([srcId, targetId]) {
      const src    = document.getElementById(srcId);
      const target = document.getElementById(targetId);
      if (src && target) {
        try {
          const raw = JSON.parse(src.textContent);
          target.innerHTML = marked.parse(raw);
          // Make checkboxes in assessment interactive
          target.querySelectorAll('input[type="checkbox"]').forEach(function (cb) {
            cb.removeAttribute('disabled');
          });
        } catch (e) {
          target.textContent = 'Content could not be loaded.';
        }
      }
    });
  }

  // ── Tab switching ────────────────────────────────────────
  const tabBtns  = document.querySelectorAll('.tab-btn');
  const tabPanes = document.querySelectorAll('.tab-pane');

  tabBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      const target = btn.dataset.tab;

      tabBtns.forEach(function (b) { b.classList.remove('active'); });
      tabPanes.forEach(function (p) { p.classList.remove('active'); });

      btn.classList.add('active');
      const pane = document.getElementById('tab-' + target);
      if (pane) pane.classList.add('active');
    });
  });

  // ── Mobile sidebar toggle ────────────────────────────────
  const menuToggle = document.getElementById('menuToggle');
  const sidebar    = document.getElementById('sidebar');

  if (menuToggle && sidebar) {
    menuToggle.addEventListener('click', function () {
      sidebar.classList.toggle('open');
    });

    // Close sidebar when a link is clicked on mobile
    sidebar.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        sidebar.classList.remove('open');
      });
    });

    // Close sidebar when clicking outside it
    document.addEventListener('click', function (e) {
      if (sidebar.classList.contains('open') &&
          !sidebar.contains(e.target) &&
          e.target !== menuToggle) {
        sidebar.classList.remove('open');
      }
    });
  }

});
