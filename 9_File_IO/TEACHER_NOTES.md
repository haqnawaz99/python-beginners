# Module 9 — File I/O: Teacher Notes

## Duration
2 classes

---

## Learning Objectives

By the end of this module, students will be able to:

- Open a file in **read**, **write**, and **append** modes
- Use the `with` statement to safely handle files
- Read file contents using `read()` and `readlines()`
- Write data to a file
- Handle `FileNotFoundError` gracefully

---

## Lesson Flow

### Class 1

| File | Topic |
|------|-------|
| `9_1_reading_files.py` | `open()`, `read()`, `readlines()`, the `with` statement |
| `9_2_writing_files.py` | Write mode `"w"`, append mode `"a"` |

**Class 1 plan:**
1. Start with the analogy — a file is like a physical notebook (کاپی). You open it, read or write, then close it.
2. Show `open()` without `with` first, then show why `with` is better (automatic close).
3. Demonstrate `read()` vs `readlines()` on the same file — show the difference in output.
4. Move to writing — **live demo the "w" mode danger** (see WARNING below).

### Class 2

| File | Topic |
|------|-------|
| `9_3_applications.py` | Real examples: saving student scores, reading them back |
| `9_4_quiz.py` | Quiz on File I/O concepts |
| Review | Common mistakes, Q&A |

**Class 2 plan:**
1. Open with a quick recap — ask students: what are the three modes? what does `with` do?
2. Walk through `9_3_applications.py` step by step — this is where concepts connect to real use.
3. Run the quiz (`9_4_quiz.py`) as a class activity.
4. End with review of common mistakes (listed below).

---

## Key Concepts

### The `with` Statement — Always Use This

```python
# CORRECT — file closes automatically
with open("scores.txt", "r") as f:
    data = f.read()

# AVOID — easy to forget to close
f = open("scores.txt", "r")
data = f.read()
f.close()
```

> **Tell students:** `with open() as f:` means — open the file, do your work, then it closes automatically. This is best practice.

### File Modes

| Mode | Meaning |
|------|---------|
| `"r"` | Read only |
| `"w"` | Write (overwrites!) |
| `"a"` | Append (adds to end) |

### Reading Methods

```python
with open("data.txt", "r") as f:
    content = f.read()        # Entire file as one string
    lines = f.readlines()     # Each line as a list item
```

---

## WARNING — "w" Mode Deletes Existing Content

> **Show this LIVE in class.** Create a file with some content, then open it with `"w"` mode and write something new. Show students the original content is gone.

This is one of the most common mistakes beginners make — using `"w"` when they mean `"a"`.

**Demonstration script:**
```python
# Step 1 — create a file with content
with open("test.txt", "w") as f:
    f.write("Bismillah\nAssalamu Alaikum\n")

# Step 2 — open with "w" again (DANGER!)
with open("test.txt", "w") as f:
    f.write("Yeh naya content hai")

# Step 3 — read it back — old content is GONE
with open("test.txt", "r") as f:
    print(f.read())
```

---

## Handling FileNotFoundError

```python
try:
    with open("scores.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File nahi mili! Pehle data save karein.")
```

Tell students: when a file does not exist and you use `"r"` mode, Python raises a `FileNotFoundError`. Always handle it.

---

## Common Mistakes to Watch For

1. **Forgetting the mode parameter** — default is `"r"`, but it is better to always write it explicitly.
2. **Using `"w"` when they mean `"a"`** — very common! Remind students before every writing exercise.
3. **Not handling `FileNotFoundError`** — program crashes if the file does not exist.
4. **Forgetting to read after writing** — students sometimes write to a file then try to read in the same `with` block without re-opening.
5. **Wrong indentation inside `with` block** — reading/writing code must be indented under `with`.

---

## Teaching Tips

- **What is a file?** "A file is a document — data saved on the computer. Just as you write notes in a notebook, Python saves data in a file."
- **Explain `with open()`:** "with open() means — open the file, do your work, then close the file. Python handles the closing automatically."
- **`"w"` mode warning:** "'w' mode deletes existing data! If you only want to add to the file, use 'a'."
- **Analogy:** "The mode is like how you open a notebook — opening it just to read is different from opening it to write."

---

## Files in This Module

| File | Description |
|------|-------------|
| `9_1_reading_files.py` | Opening and reading files |
| `9_2_writing_files.py` | Writing and appending to files |
| `9_3_applications.py` | Real-world examples with scores |
| `9_4_quiz.py` | Module quiz |
| `9_5_challenge.py` | Extension/challenge task |

---

## Quick Reference Card (for the board)

```
"r"  → Read   (file must exist)
"w"  → Write  (creates new OR deletes old!)
"a"  → Append (adds to end, safe)

with open("file.txt", "r") as f:
    data = f.read()
```
