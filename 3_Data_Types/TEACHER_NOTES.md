# Module 3 — Data Types: Teacher Notes

## Overview

| Item | Detail |
|------|--------|
| Module | 3 — Data Types |
| Duration | 2 classes |
| Level | Beginner |
| Age Group | 10–16 years |
| Language | Urdu (with English terms) |

---

## Learning Objectives

By the end of this module, students will be able to:

1. Identify the four basic data types: `int`, `float`, `str`, `bool`
2. Use `type()` to find the data type of any value
3. Convert between types using `int()`, `float()`, `str()`
4. Use the `int(input())` pattern to get numbers from users
5. Write f-strings to display values inside text

---

## Lesson Flow

### Class 1 (55 minutes)

| Time | Activity | File |
|------|----------|------|
| 0–10 min | Revise variables — ask students: "Ahmed ne ek variable banaya `naam = 'Ahmed'`. Yeh kya hai?" | Revision |
| 10–30 min | Introduce int, float, str, bool with real examples | `3_1_data_types.py` |
| 30–55 min | Type conversion — int(), float(), str() with examples | `3_2_type_conversion.py` |

### Class 2 (55 minutes)

| Time | Activity | File |
|------|----------|------|
| 0–20 min | Conversion errors — what happens when conversion fails | `3_3_conversion_errors.py` |
| 20–45 min | f-strings — the fill-in-the-blank method | `3_4_f_strings.py` |
| 45–55 min | Quiz | — |

---

## Key Concepts to Emphasise

### The `int(input())` Pattern

> **This is the most important pattern in this module. Students will use it in EVERY future module.**

```python
# Wrong — input() always returns a string!
umar = input("Apni umar likhein: ")
agli_saal = umar + 1  # ERROR!

# Correct — convert to int first
umar = int(input("Apni umar likhein: "))
agli_saal = umar + 1  # Works!
print(f"Agli saal aap ki umar hogi: {agli_saal}")
```

Explain clearly: `input()` hamesha **string** return karta hai, chahe user number type kare. Math karne ke liye pehle `int()` mein convert karna padta hai.

### The Four Types

```python
naam    = "Ahmed"      # str   — text / matn
umar    = 15           # int   — poora number
qad     = 5.7          # float — decimal number
Muslim  = True         # bool  — haan ya na (True/False)
```

---

## Common Mistakes

| Mistake | What Happens | Correction |
|---------|-------------|------------|
| `int("Ahmed")` | `ValueError` crash | Only convert numeric strings like `int("25")` |
| Forgetting `int()` with `input()` | Wrong result or crash when doing math | Always use `int(input(...))` for numbers |
| f-string without `f` prefix | Curly braces print literally | Write `f"..."` not `"..."` |
| `str + int` | `TypeError` | Convert both to same type first |

---

## Urdu Teaching Tips

Use these Urdu explanations on the whiteboard:

- **int** — "int matlab poora number — jaise 5, 100, -3. Decimal nahin hota."
- **float** — "float matlab decimal wala number — jaise 5.7, 3.14, 99.9."
- **str** — "str matlab text — jo bhi quotes mein likha ho woh string hai."
- **bool** — "bool matlab sirf do jawab — ya True (haan) ya False (na)."
- **f-string** — "f-string matlab fill-in-the-blank — curly brackets mein variable ka naam likhein aur Python khud woh value daal deta hai."

---

## Classroom Activity Ideas

**Activity 1 — Type Detective:**
Write values on the board. Students call out the data type.
- `"Lahore"` → str
- `42` → int
- `3.14` → float
- `False` → bool

**Activity 2 — Fix the Bug:**
Show broken code. Students find and fix the problem.
```python
# Fix karo:
marks = input("Marks likhein: ")
total = marks + 50
print(total)
```

**Activity 3 — f-string Story:**
Students write one sentence about themselves using an f-string.
```python
naam = "Fatima"
city = "Karachi"
print(f"Mera naam {naam} hai aur main {city} mein rehti hoon.")
```

---

## Module Files

| File | Topic |
|------|-------|
| `3_1_data_types.py` | int, float, str, bool — introduction |
| `3_2_type_conversion.py` | int(), float(), str() conversion |
| `3_3_conversion_errors.py` | What goes wrong with bad conversions |
| `3_4_f_strings.py` | f-strings — formatting output |
| `3_5_practice.py` | Combined practice |
| `3_6_quiz.py` | Module quiz |

---

## Next Module Preview

Module 4 (Operators) builds directly on this module. Students must know:
- The difference between `int` and `float`
- The `int(input())` pattern

Make sure every student can write `int(input())` confidently before moving on.
