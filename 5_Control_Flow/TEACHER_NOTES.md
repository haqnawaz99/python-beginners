# Module 5 — Control Flow: Teacher Notes

## Overview

| Item | Detail |
|------|--------|
| Module | 5 — Control Flow |
| Duration | 3 classes (this is a large module) |
| Level | Beginner to Intermediate |
| Age Group | 10–16 years |
| Language | English (with Urdu delivery) |

---

## Learning Objectives

By the end of this module, students will be able to:

1. Write `if`, `elif`, `else` blocks with correct indentation
2. Build grade checkers and pass/fail programs
3. Write `while` loops that terminate correctly
4. Use `break` to exit a loop early
5. Write `for` loops using `range()` and lists
6. Use the `while True: ... break` pattern for menus

---

## Lesson Flow

### Class 1 — if / elif / else (55 minutes)

| Time | Activity | File |
|------|----------|------|
| 0–15 min | Introduce `if` — single condition, real examples | `5_1_if_else.py` |
| 15–30 min | Add `elif` — multiple conditions | `5_1_if_else.py` |
| 30–45 min | Grade calculator — full if/elif/else chain | `5_2_grade_checker.py` |
| 45–55 min | Pass/fail checker — practice | `5_2_grade_checker.py` |

### Class 2 — while loops (55 minutes)

| Time | Activity | File |
|------|----------|------|
| 0–15 min | Introduce `while` — countdown example | `5_3_while_loop.py` |
| 15–30 min | Infinite loop danger — show and fix | `5_3_while_loop.py` |
| 30–45 min | Input validation loop — keep asking until valid | `5_4_while_input.py` |
| 45–55 min | `while True: ... break` menu pattern | `5_4_while_input.py` |

### Class 3 — for loops + Applications (55 minutes)

| Time | Activity | File |
|------|----------|------|
| 0–15 min | Introduce `for` with `range()` | `5_5_for_loop.py` |
| 15–30 min | `for` with lists — student names, cities | `5_5_for_loop.py` |
| 30–45 min | Combined application — mini project | `5_6_applications.py` |
| 45–55 min | Quiz | — |

---

## Key Concepts to Emphasise

### 1. Indentation Is Not Optional

> **This is the #1 thing to teach in this module. Python uses indentation as structure — not just style.**

```python
# CORRECT:
marks = 85
if marks >= 50:
    print("Pass ho gaye!")    # 4 spaces in
    print("Mubarak ho!")      # same level

# WRONG (IndentationError):
marks = 85
if marks >= 50:
print("Pass ho gaye!")        # ERROR! no indent
```

**Whiteboard demonstration:** Draw a box around indented code. "All of this is one group. Without the indent, Python will not understand."

### 2. The Colon After if / elif / else / while / for

```python
if marks >= 50:        # colon required ← here
    print("Pass")

while count > 0:       # here too ← colon
    count -= 1

for i in range(5):     # here too ← colon
    print(i)
```

Tell students: "Whenever you tell Python to start a block, put a colon at the end."

### 3. if / elif / else Structure

```python
marks = int(input("Marks likhein (0-100): "))

if marks >= 90:
    print("Grade: A+  — Masha'Allah!")
elif marks >= 80:
    print("Grade: A   — Bohat achha!")
elif marks >= 70:
    print("Grade: B   — Achha!")
elif marks >= 60:
    print("Grade: C   — Theek hai.")
elif marks >= 50:
    print("Grade: D   — Koshish karo.")
else:
    print("Grade: Fail — Mehnat karo, Allah madad karega.")
```

**Key point:** Python checks conditions **in order, top to bottom**. As soon as one is True, it runs that block and skips the rest.

### 4. while Loop — Must Have an Exit

```python
# DANGEROUS — Infinite loop!
count = 5
while count > 0:
    print(count)
    # count was never updated — the loop will never end!

# CORRECT:
count = 5
while count > 0:
    print(count)
    count -= 1          # decrease count each time
print("Khatam!")
```

### 5. The `while True: break` Menu Pattern

> **This pattern is used in all future projects. Teach it explicitly.**

```python
while True:
    print("\n=== Main Menu ===")
    print("1. Marks check karo")
    print("2. Calculator")
    print("3. Baahir jao")

    choice = input("Apna choice likhein: ")

    if choice == "1":
        print("Marks checking...")
    elif choice == "2":
        print("Calculator...")
    elif choice == "3":
        print("Allah Hafiz!")
        break           # Exit the loop
    else:
        print("Galat choice — dobara likhein.")
```

### 6. for Loop with range()

```python
# range(5) → 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# range(1, 6) → 1, 2, 3, 4, 5
for i in range(1, 6):
    print(i)

# range(1, 11, 2) → 1, 3, 5, 7, 9  (step 2)
for i in range(1, 11, 2):
    print(i)
```

### 7. for Loop with Lists

```python
talibaan = ["Ahmed", "Fatima", "Hassan", "Zainab"]

for naam in talibaan:
    print(f"Assalamu Alaikum, {naam}!")
```

---

## Common Mistakes

| Mistake | What Happens | Correction |
|---------|-------------|------------|
| Missing colon (`:`) after `if`/`while`/`for` | `SyntaxError` | Always end with `:` |
| Wrong indentation | `IndentationError` or wrong logic | 4 spaces, consistent |
| `while` loop without updating counter | Infinite loop — program freezes | Always update the variable |
| Using `=` instead of `==` in `if` | `SyntaxError` | Use `==` for comparison |
| `for i in range(5)` → expects 1 to 5 but gets 0 to 4 | Off-by-one error | Use `range(1, 6)` for 1 to 5 |

---

## Teaching Tips

| Keyword | Explanation |
|---------|-----------------|
| `if` | "if" — if this is true, then do this |
| `elif` | "else if" — if the first condition is not met, check this one |
| `else` | "otherwise" — if none of the conditions were true |
| `while` | "while" — keep doing this as long as it is true |
| `for` | "for each" — for each value in this list or range |
| `break` | "stop" — exit the loop immediately |
| `range()` | "sequence" — a series of numbers |

---

## Classroom Activity Ideas

**Activity 1 — Human Robot:**
Teacher calls out: "If your name starts with A, stand up. Otherwise sit down." Students act as if/else.

**Activity 2 — Countdown Together:**
Whole class counts down from 10 together (like a while loop). Stop at 0 (like the condition).

**Activity 3 — Grade Calculator Race:**
Give students marks on a slip of paper. First student to correctly tell their grade using the if/elif/else chain wins.

**Activity 4 — Name Loop:**
Write 5 student names on board. Students write a `for` loop that prints "Assalamu Alaikum" to each.

---

## Module Files

| File | Topic |
|------|-------|
| `5_1_if_else.py` | if, elif, else — introduction |
| `5_2_grade_checker.py` | Grade calculator application |
| `5_3_while_loop.py` | while loops — countdown, validation |
| `5_4_while_input.py` | while True + break menu pattern |
| `5_5_for_loop.py` | for loops with range() and lists |
| `5_6_applications.py` | Combined applications and mini-project |

---

## Important Note for Teacher

This module is **the foundation of all programming logic**. Students who master this module will be able to build real projects. Take extra time here — do not rush. If the class needs 4 sessions instead of 3, that is completely fine.

The `while True: ... break` pattern alone will appear in every project from Module 6 onwards.
