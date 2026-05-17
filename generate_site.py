"""
generate_site.py — Python for Beginners Course Website Generator
Run from: D:\Haq Nawaz\Teaching\ISDP\2026\python
Output:   docs/index.html + docs/module-N.html for N in 0-10
"""

import os
import json
import html as html_mod
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"

MODULES = [
    (0,  "Setup",         "0_Setup",         "⚙️",  "Install Python & VS Code, write your first program, understand errors"),
    (1,  "Strings",       "1_Strings",       "📝",  "String concatenation, input(), len() — talking to the user"),
    (2,  "Variables",     "2_Variables",     "📦",  "Storing information in variables, naming rules, string methods"),
    (3,  "Data Types",    "3_Data_Types",    "🔢",  "int, float, str, bool — type conversion, f-strings"),
    (4,  "Operators",     "4_Operators",     "➕",  "Math, BODMAS, comparison and logical operators"),
    (5,  "Control Flow",  "5_Control_Flow",  "🔀",  "if/elif/else, while loops, for loops, range()"),
    (6,  "Functions",     "6_Functions",     "🔧",  "def, parameters, return values, default values"),
    (7,  "Lists",         "7_Lists",         "📋",  "Lists, tuples, dictionaries — storing collections of data"),
    (8,  "Error Handling","8_Error_Handling","🛡️",  "try/except, input validation, reusable helper functions"),
    (9,  "File I/O",      "9_File_IO",       "💾",  "Read and write files — saving data between runs"),
    (10, "Projects",      "10_Projects",     "🚀",  "3 capstone projects: Report Card, Prayer Reminder, Quiz Game"),
]

CLASSES = ["1", "2", "2", "2", "2", "3", "2", "2", "2", "2", "3"]

CDN_HLJS   = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0"
CDN_MARKED = "https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js"


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def classify_file(filename: str):
    name = filename.lower()
    if "quiz_solution" in name:
        return "Quiz Solution", "badge-solution"
    if "quiz" in name:
        return "Quiz", "badge-quiz"
    if "islamic_applications" in name or "applications" in name:
        return "Applications", "badge-app"
    if "starter" in name:
        return "Project Starter", "badge-starter"
    if "solution" in name:
        return "Project Solution", "badge-solution"
    return "Lesson", "badge-lesson"


def sidebar_html(active_num: int) -> str:
    items = []
    home_active = "active" if active_num == -1 else ""
    items.append(f'<li><a href="index.html" class="{home_active}">🏠 Home</a></li>')
    for num, title, _, icon, _ in MODULES:
        active = "active" if num == active_num else ""
        items.append(
            f'<li><a href="module-{num}.html" class="{active}">'
            f'{icon} M{num}: {title}</a></li>'
        )
    return '<ul class="sidebar-nav">' + "".join(items) + "</ul>"


def head_html(title: str) -> str:
    return f"""<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_mod.escape(title)} — Python for Beginners</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="{CDN_HLJS}/styles/github-dark.min.css">
</head>"""


def header_html() -> str:
    return """<header class="site-header">
  <div class="header-inner">
    <a href="index.html" class="site-logo">🐍 Python for Beginners</a>
    <button class="menu-toggle" id="menuToggle">☰</button>
  </div>
</header>"""


def scripts_html() -> str:
    return f"""<script src="{CDN_HLJS}/highlight.min.js"></script>
<script src="{CDN_MARKED}"></script>
<script src="assets/js/app.js"></script>"""


def generate_module_page(num: int, title: str, folder: str, icon: str, _desc: str) -> str:
    module_dir = BASE_DIR / folder

    # Collect and sort Python files
    py_files = sorted(module_dir.glob("*.py"))

    # Build lessons tab
    lessons_parts = []
    for py_file in py_files:
        code = read_file(py_file)
        label, badge_cls = classify_file(py_file.name)
        escaped = html_mod.escape(code)
        lessons_parts.append(f"""
    <div class="code-file">
      <div class="code-file-header">
        <span class="file-name">📄 {html_mod.escape(py_file.name)}</span>
        <span class="badge {badge_cls}">{label}</span>
      </div>
      <pre><code class="language-python">{escaped}</code></pre>
    </div>""")

    lessons_html = "\n".join(lessons_parts) if lessons_parts else "<p>No lesson files found.</p>"

    # Read markdown content — encode as JSON for safe embedding
    notes_json      = json.dumps(read_file(module_dir / "TEACHER_NOTES.md"))
    practice_json   = json.dumps(read_file(module_dir / "practice_sheet.md"))
    assessment_json = json.dumps(read_file(module_dir / "ASSESSMENT.md"))

    # Prev / next links
    prev_link = f'<a href="module-{num-1}.html" class="nav-btn">← Module {num-1}</a>' if num > 0 else "<span></span>"
    next_link = f'<a href="module-{num+1}.html" class="nav-btn">Module {num+1} →</a>' if num < 10 else "<span></span>"

    sidebar = sidebar_html(num)
    page_title = f"Module {num}: {title}"

    return f"""<!DOCTYPE html>
<html lang="en">
{head_html(page_title)}
<body>
{header_html()}
<div class="layout">
  <aside class="sidebar" id="sidebar">{sidebar}</aside>
  <main class="main-content">

    <div class="module-header">
      <span class="module-icon">{icon}</span>
      <div>
        <p class="module-label">Module {num}</p>
        <h1>{html_mod.escape(title)}</h1>
      </div>
    </div>

    <div class="tab-bar">
      <button class="tab-btn active" data-tab="lessons">📚 Lessons</button>
      <button class="tab-btn" data-tab="notes">📋 Teacher Notes</button>
      <button class="tab-btn" data-tab="practice">✏️ Practice Sheet</button>
      <button class="tab-btn" data-tab="assessment">📊 Assessment</button>
    </div>

    <div class="tab-panes">

      <div id="tab-lessons" class="tab-pane active">
        {lessons_html}
      </div>

      <div id="tab-notes" class="tab-pane">
        <div class="markdown-body" id="md-notes"></div>
        <script type="application/json" id="src-notes">{notes_json}</script>
      </div>

      <div id="tab-practice" class="tab-pane">
        <div class="markdown-body print-friendly" id="md-practice"></div>
        <script type="application/json" id="src-practice">{practice_json}</script>
        <button class="print-btn no-print" onclick="window.print()">🖨️ Print Practice Sheet</button>
      </div>

      <div id="tab-assessment" class="tab-pane">
        <div class="markdown-body" id="md-assessment"></div>
        <script type="application/json" id="src-assessment">{assessment_json}</script>
      </div>

    </div>

    <div class="module-nav">
      {prev_link}
      <a href="index.html" class="nav-btn nav-home">🏠 All Modules</a>
      {next_link}
    </div>

  </main>
</div>
{scripts_html()}
</body>
</html>"""


def generate_index() -> str:
    cards = []
    for num, title, folder, icon, desc in MODULES:
        module_dir = BASE_DIR / folder
        py_count   = len(list(module_dir.glob("*.py")))
        classes    = CLASSES[num]
        cards.append(f"""
    <a href="module-{num}.html" class="module-card">
      <span class="card-num">Module {num}</span>
      <span class="card-icon">{icon}</span>
      <span class="card-title">{html_mod.escape(title)}</span>
      <span class="card-desc">{html_mod.escape(desc)}</span>
      <span class="card-files">📄 {py_count} files &nbsp;·&nbsp; 🕐 {classes} class{'es' if classes != '1' else ''}</span>
    </a>""")

    cards_html = "\n".join(cards)
    sidebar    = sidebar_html(-1)

    return f"""<!DOCTYPE html>
<html lang="en">
{head_html("Course Overview")}
<body>
{header_html()}
<div class="layout">
  <aside class="sidebar" id="sidebar">{sidebar}</aside>
  <main class="main-content">

    <div class="index-hero">
      <h1>🐍 Python for Beginners</h1>
      <p>A complete beginner course for Pakistani school and Madrasa students, ages 10–16.<br>
         Videos in Urdu · Code in English · Zero prior knowledge required.</p>
      <div class="hero-meta">
        <span class="hero-badge">📚 11 Modules</span>
        <span class="hero-badge">🕐 ~23 Classes</span>
        <span class="hero-badge">🚀 3 Real Projects</span>
        <span class="hero-badge">🇵🇰 Pakistani Context</span>
      </div>
    </div>

    <div class="modules-grid">
      {cards_html}
    </div>

    <footer class="index-footer">
      <p>Taught by <strong>Haq Nawaz</strong> · haq.nawaz@ili.digital ·
         <a href="https://github.com/haqnawaz99/python-beginners" target="_blank">GitHub Repo</a></p>
      <p style="margin-top:0.4rem; font-size:0.8rem; opacity:0.7;">
        Bismillah. May this course benefit every student who learns from it. Ameen.
      </p>
    </footer>

  </main>
</div>
{scripts_html()}
</body>
</html>"""


def main():
    DOCS_DIR.mkdir(exist_ok=True)

    # Generate index
    index_path = DOCS_DIR / "index.html"
    index_path.write_text(generate_index(), encoding="utf-8")
    print("OK index.html")

    # Generate module pages
    for num, title, folder, icon, desc in MODULES:
        html_content = generate_module_page(num, title, folder, icon, desc)
        out_path = DOCS_DIR / f"module-{num}.html"
        out_path.write_text(html_content, encoding="utf-8")
        print(f"OK module-{num}.html  ({title})")

    print(f"\nSite generated in: {DOCS_DIR}")
    print("Open docs/index.html in a browser to preview.")
    print("Push to GitHub and enable Pages -> /docs to go live.")


if __name__ == "__main__":
    main()
