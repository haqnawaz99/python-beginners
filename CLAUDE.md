# CLAUDE.md — Python Beginners Course
## Project Context for AI-Assisted Development

This file documents all design decisions, constraints, and context for the
**Python for Beginners** course. Reference this in every session so decisions
remain consistent.

---

## 1. Project Overview

| Field | Detail |
|-------|--------|
| **Course name** | Python for Beginners — ISDP |
| **Teacher** | Haq Nawaz (haq.nawaz@ili.digital) — advanced Python user |
| **Target audience** | Pakistani school and Madrasa students, ages 10–16 |
| **Prior knowledge** | Zero — no coding experience assumed |
| **Delivery language** | Urdu (YouTube videos) — code and files remain in English |
| **Platform** | YouTube (video lessons) + GitHub (code files) |
| **GitHub repo** | https://github.com/haqnawaz99/python-beginners |
| **Local working folder** | D:\Haq Nawaz\Teaching\ISDP\2026\python |

### Learning Objectives
By the end of the course, students can:
1. Write, run, and debug basic Python programs
2. Use variables, data types, operators, and f-strings
3. Control program flow with if/elif/else, while, and for loops
4. Define and call functions with parameters and return values
5. Work with lists, tuples, and dictionaries
6. Handle errors gracefully with try/except
7. Read from and write to files
8. Build 3 complete real-world applications from scratch

### Course Duration
~23 classes of 45–60 minutes each. See README.md for per-module estimates.

---

## 2. Course Structure

| Module | Folder | Key Concepts | Classes |
|--------|--------|-------------|---------|
| 0 | `0_Setup` | Python install, VS Code, print(), comments, reading errors | 1 |
| 1 | `1_Strings` | String concatenation, escape characters (`\'` `\"` `\n` `\t`), ASCII-art pattern printing, input(), len() | 2 |
| 2 | `2_Variables` | Variables, naming rules, string methods (upper/lower/title/strip) | 2 |
| 3 | `3_Data_Types` | int/float/str/bool, type(), int()/float()/str(), f-strings | 2 |
| 4 | `4_Operators` | Math operators, BODMAS, comparison, logical (and/or/not) | 2 |
| 5 | `5_Control_Flow` | if/elif/else, while loops, for loops, range() | 3 |
| 6 | `6_Functions` | def, parameters, return, default values | 2 |
| 7 | `7_Lists` | lists, tuples, dictionaries | 2 |
| 8 | `8_Error_Handling` | try/except, ValueError, FileNotFoundError, input validation | 2 |
| 9 | `9_File_IO` | open(), read/write/append, with statement | 2 |
| 10 | `10_Projects` | Report Card, Prayer Reminder, Quiz Game | 3 |

### Files Per Module
Every module contains:
```
N_ModuleName/
├── N_1_lesson.py             ← lesson code (run live in class)
├── N_2_lesson.py             ← next lesson
├── ...
├── N_X_applications.py       ← real-world examples
├── N_Y_quiz.py               ← student practice (Easy/Medium/Complex)
├── N_Z_quiz_solution.py      ← teacher reference
├── TEACHER_NOTES.md          ← duration, flow, Urdu tips, common mistakes
├── ASSESSMENT.md             ← rubric, oral questions, pass criteria
├── practice_sheet.md         ← printable offline exercises
├── N_notebook.ipynb          ← interactive Jupyter notebook (all concepts, runnable)
└── session_tasks.md          ← after-session student tasks (graded, 3 difficulty tiers)
```

### Notebook Design Rules
- Every concept section has: explanation markdown → runnable example cells → Try It Yourself cells
- Each Try It Yourself task gets its **own** markdown cell + its **own** blank code cell (never one cell for multiple tasks)
- Module 1 notebook avoids `x = input(...)` as the default — `input()` is used inline inside `print()`. Cells that must combine/reuse two answers (e.g. first+last name) are kept as flagged "preview" exceptions with a note pointing to Module 2 for variables
- Final Practice section has **at least 3 programs**, each with its own markdown + code cell, covering all module concepts combined
- Module 1 Section 2 also covers escape characters (`\'`, `\"`, `\n`, `\t`) and simple ASCII-art pattern printing (`*` shapes) — mirrored in `1_1_string_concatenation.py` and `session_tasks.md` (Tasks 8-9)

Module 10 additionally contains:
- `10_X_*_starter.py` — give to students (TODOs to fill in)
- `10_X_*_solution.py` — full working solution

### Notebook Export Pipeline (PDF/DOCX)
- Direct PDF export (`nbconvert --to pdf` / `--to webpdf`) is NOT used — LaTeX's default fonts can't render Urdu/Arabic script or emoji (shows as blank glyphs), and `--to webpdf` needs a Chromium download that may not be available offline
- Use the DOCX pipeline instead, which preserves Urdu/Arabic/emoji correctly:
  1. `python -m nbconvert --to markdown <notebook>.ipynb`
  2. `pandoc <notebook>.md -o <notebook>.docx`
  3. Delete the intermediate `.md` file (and any `_files/` image folder) — keep only the `.docx`
- Requires `pypandoc_binary` installed (`pip install pypandoc_binary`) and its bundled `pandoc.exe` on PATH (`site-packages/pypandoc/files/`)
- Teachers can open the `.docx` in Word/LibreOffice and use "Save As PDF" for a print-ready PDF with correct Urdu/Arabic/emoji rendering

---

## 3. Design Decisions

### Cultural Adaptations for Pakistan
- **Student names used**: Ahmed, Fatima, Hassan, Zainab, Muhammad, Ali, Ayesha
- **Cities used**: Lahore, Karachi, Islamabad, Peshawar, Quetta, Multan, Faisalabad
- **Islamic context**: prayer times, Quran (Surahs, Ayaat, Juz), dhikr counters, madrasa subjects
- **Madrasa subjects**: Quran, Hadith, Fiqh, Arabic, Seerah (used in Report Card project)
- **Currency**: Pakistani Rupees (PKR) in all money examples
- **Local references**: cricket, biryani, rickshaw fare, school fees in rupees
- **Islamic phrases in code feedback**: "Ma sha Allah!", "Alhamdulillah!", "Bismillah", "JazakAllah Khair"

### Language Decision
- **Code**: always English (variable names, function names, comments)
- **YouTube delivery**: Urdu — teacher explains concepts in Urdu
- **TEACHER_NOTES.md**: includes Urdu tips for how to explain each concept
- **Student-facing files**: English only — students learn to read English code

### Teaching Methodology
- Show code running FIRST, let students predict output BEFORE running
- Teacher types live on projector/screen share — students follow along
- Each concept introduced with a Pakistani/Islamic example
- Error messages shown deliberately — "galti se darna nahin"
- Reusable validation functions (`get_integer_in_range`, `get_non_empty`) introduced in Module 8 and carried through all projects

### Capstone Project Approach
1. Teacher runs the SOLUTION file so students see the finished program
2. Students receive the STARTER file (with TODOs)
3. Students complete each TODO function
4. Run and test together as a class

---

## 4. Constraints & Requirements

### Student Environment
- Personal laptops (Windows assumed)
- VS Code as the editor
- Python 3.x (see SETUP.md for install instructions)
- No internet required after setup — all files local

### Skill Level Constraints
- **Zero prior coding** — never assume any concept is "obvious"
- Introduce `int(input())` pattern properly in Module 3 — this is a recurring stumbling block
- Indentation confusion is the #1 issue in Module 5 — spend extra time on it
- Every new concept needs a Pakistani/Islamic example before a generic one

### Resource Limitations
- Some students may have limited screen time — `practice_sheet.md` is designed to be printable
- Madrasa classrooms may have only one computer/projector — teacher-led demonstration mode
- Students may not have GitHub accounts — files should work fully offline

### Difficulty Tiers
Every quiz file is divided into three clearly labelled sections:
- **Easy** — single concept, recall/fill-in-the-blank
- **Medium** — combining 2-3 concepts
- **Complex** — multi-step, real-world problem

This allows teachers to differentiate: slower students do Easy + Medium, faster students attempt Complex.

---

## 5. Established Conventions

### Code Style (do not deviate without reason)
- `int(input())` pattern — always used for numeric input (never `eval()`)
- `with open()` — always used for file operations (never bare `open()`)
- Reusable helper functions — `get_integer_in_range(prompt, min, max)` and `get_non_empty(prompt)` appear in all projects
- f-strings — always preferred over concatenation for formatted output
- `while True: ... break` — used for all menus
- No external libraries — standard library only (os module is the only import besides builtins)

### Naming Conventions
- Lesson files: `N_X_descriptive_name.py` (snake_case, numbered)
- Constants: `UPPER_CASE` (e.g. `RECORDS_FILE`, `PASSING_MARKS`)
- Functions: `verb_noun()` style (e.g. `add_student()`, `view_history()`, `show_menu()`)
- Variables: `snake_case`

### File Saving Behavior
Projects save data to `.txt` files in the same folder:
- Report Card → `report_cards.txt`
- Prayer Reminder → `prayer_log.txt`
- Quiz Game → `quiz_scores.txt`

Students should run programs from within their module folder.

### Assessment Standard
- All quizzes marked out of 17 (Easy: 5, Medium: 6, Complex: 6)
- Grade scale: 15-17 Excellent, 11-14 Good, 7-10 Needs Revision, 0-6 Repeat module
- Practical submission required per module (see each ASSESSMENT.md)
- Capstone projects marked out of 10 each (30 total) — see `10_Projects/ASSESSMENT.md`

---

## 6. Module-Specific Notes

### Module 0 — Setup
- Do Python + VS Code install together as a class (or pre-install on lab machines)
- Key message: error messages are helpers, not failures

### Module 3 — Data Types (Critical)
- `int(input())` pattern is introduced here — it appears in EVERY subsequent module
- Teach `f-strings` here, not string concatenation for formatting
- `type()` function is a useful debugging tool — show it early

### Module 5 — Control Flow (Most Difficult)
- Indentation is the hardest concept — use consistent 4-space indentation always
- Show the `while True: ... break` menu pattern here — it's used in all 3 projects
- Spend extra time — this is the gateway to all real programs

### Module 8 — Error Handling (New — not in other AI tool versions)
- This module does NOT exist in the codex or cursor versions — it's a unique strength
- Critical for all file operations in Module 9 and all capstone projects
- Teach `get_integer_in_range()` here as a reusable pattern

### Module 9 — File I/O (New — not in other AI tool versions)
- WARN students: `"w"` mode overwrites existing data — demonstrate this live
- Always use `with open()` — show what happens without it (file not closed)
- `os.path.exists()` check before reading — standard pattern in all projects

### Module 10 — Projects
- All 3 projects are FULLY RUNNABLE — not stubs or pseudocode
- Projects intentionally integrate all skills from Modules 0-9
- Run in this order: Report Card (simplest) → Prayer Reminder → Quiz Game (most complex)

---

## 7. What Has Been Completed

- [x] All 65 lesson/quiz/solution `.py` files (Modules 0–10)
- [x] `TEACHER_NOTES.md` for all 11 modules
- [x] `ASSESSMENT.md` for all 11 modules
- [x] `practice_sheet.md` for all 11 modules
- [x] 3 capstone project SOLUTION files
- [x] 3 capstone project STARTER files (with TODOs for students)
- [x] `README.md` — course map and usage guide
- [x] `SETUP.md` — Python + VS Code install guide for students
- [x] Git repo initialized and pushed to GitHub
- [x] GitHub Pages website (`docs/` folder) with pages for all 11 modules
- [x] `1_strings_notebook.ipynb` — interactive Jupyter notebook for Module 1
- [x] `2_variables_notebook.ipynb` — interactive Jupyter notebook for Module 2
- [x] `session_tasks.md` for Module 2 — 7 graded after-session student tasks + bonus

---

## 8. Next Steps

### Immediate
- [ ] Review each module file personally and test all code runs without errors
- [ ] Record YouTube videos module by module (start with Module 0)
- [ ] Add YouTube video links to each module's `TEACHER_NOTES.md` once recorded

### Notebooks & Session Tasks (in progress — follow established pattern)
- [x] Module 1 — `1_strings_notebook.ipynb` + `session_tasks.md`
- [x] Module 2 — `2_variables_notebook.ipynb` + `session_tasks.md`
- [x] Module 3 — `3_data_types_notebook.ipynb` + `session_tasks.md`
- [x] Module 4 — `4_operators_notebook.ipynb` + `session_tasks.md`
- [ ] Module 5 — `5_control_flow_notebook.ipynb` + `session_tasks.md`
- [ ] Module 6 — `6_functions_notebook.ipynb` + `session_tasks.md`
- [ ] Module 7 — `7_lists_notebook.ipynb` + `session_tasks.md`
- [ ] Module 8 — `8_error_handling_notebook.ipynb` + `session_tasks.md`
- [ ] Module 9 — `9_file_io_notebook.ipynb` + `session_tasks.md`
- [ ] Module 10 — `10_projects_notebook.ipynb` + `session_tasks.md`
- [x] `session_tasks.md` added to Module 1

### Short Term
- [ ] Add a `STUDENT_GUIDE.md` — one-page guide written directly for students (not teachers)
- [ ] Create a `resources/` folder with a Pakistan-themed cheat sheet (one-pager: variables, loops, functions quick reference)
- [ ] Test all 3 capstone projects end-to-end on a fresh machine
- Generate printable exports for each module notebook using the DOCX pipeline (see "Notebook Export Pipeline" above):
  - [x] Module 1 — `1_strings_notebook.docx` generated and committed
  - [ ] Module 2 — pending
  - [ ] Module 3 — pending
  - [ ] Module 4 — pending
  - [ ] Modules 5–10 — pending

### Future Enhancements
- [ ] Add Module 11 — OOP basics (classes, objects) — currently out of scope
- [ ] Add Module 12 — Simple GUI with tkinter (optional advanced module)
- [ ] Translate `practice_sheet.md` files to Urdu for Madrasa-only classrooms
- [ ] Add answer keys to `practice_sheet.md` files (currently teacher-only)
- [ ] Create video timestamps document matching YouTube videos to file names

### How to Update This Repo
```
# After making changes in D:\Haq Nawaz\Teaching\ISDP\2026\python:
git add .
git commit -m "Brief description of what changed"
git push
```

---

## 9. Comparison with Other AI Tools

This course was also drafted by Codex and Cursor. Key differences:

| Feature | This repo (Claude) | Codex | Cursor |
|---------|-------------------|-------|--------|
| Runnable lesson .py files | Yes | Yes | Yes |
| Error Handling module | **Yes** | No | No |
| File I/O module | **Yes** | No | No |
| Capstone projects (runnable) | **3 complete** | Rubric only | 6 starters |
| Starter files for projects | **Yes** | No | Yes |
| TEACHER_NOTES per module | **Yes** | Per-lesson plans | Yes |
| ASSESSMENT rubrics | **Yes** | Yes | Yes |
| Practice sheets | **Yes** | Yes | Yes |
| Input validation pattern | **Yes** | No | No |
| Difficulty tiers (Easy/Med/Complex) | **Yes** | No | No |
| VS Code setup guide | Yes | No | Yes |

---

*Bismillah. May this course benefit every student who learns from it. Ameen.*
