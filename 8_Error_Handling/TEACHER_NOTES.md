# Module 8: Error Handling — Teacher Notes

## Duration
2 classes

---

## Learning Objectives

By the end of this module, students will be able to:

1. Understand what **exceptions** are and why they happen
2. Use `try/except` to catch `ValueError` and `FileNotFoundError`
3. Write **input validation loops** that keep asking until valid input is given
4. Use `try/except/else/finally` — all four clauses

---

## Lesson Flow

### Class 1

| File | Topic |
|------|-------|
| `8_1_what_are_errors.py` | Types of errors: `SyntaxError`, `NameError`, `TypeError`, `ValueError`, `IndexError`, `KeyError` |
| `8_2_try_except.py` | Catching errors gracefully with `try/except` — program continues instead of crashing |

### Class 2

| File | Topic |
|------|-------|
| `8_3_input_validation.py` | Validate user input with a `while` loop + `try/except` |
| `8_4_quiz.py` | End-of-module quiz |
| Review | Go over common mistakes, reinforce the pattern |

---

## Key Concept

> **`try/except` lets the program continue instead of crashing.**
> The `except` block only runs **IF** an error occurs.

This is not just a module — it is a **skill that every future project depends on.**

Draw this on the board:

```
Without try/except:
User types "abc" → int("abc") → CRASH ❌

With try/except:
User types "abc" → int("abc") → except catches it → friendly message ✓
```

---

## Error Types — Quick Reference Table

| Error Type | When does it happen? | Example |
|------------|---------------------|---------|
| `SyntaxError` | Code is written incorrectly | `if x = 5:` (should be `==`) |
| `NameError` | Using a variable that doesn't exist | `print(score)` before assigning `score` |
| `TypeError` | Wrong type in operation | `"5" + 5` (string + integer) |
| `ValueError` | Right type, wrong value | `int("Ahmed")` |
| `IndexError` | List index out of range | `names[10]` on a 3-item list |
| `KeyError` | Dictionary key not found | `student["phone"]` when key doesn't exist |

---

## The Four Clauses — Teach in Order

```python
try:
    # koshish karo (attempt this)
    number = int(input("Number daalein: "))
except ValueError:
    # agar galti ho to (if this specific error happens)
    print("Sirf number chahiye!")
else:
    # agar koi galti nahi (if NO error occurred)
    print(f"Aap ne daala: {number}")
finally:
    # hamesha chalta hai (always runs — error or not)
    print("Program khatam.")
```

---

## Urdu Teaching Tips

- **"try matlab koshish karo"** *(try means attempt)*

- **"except matlab agar galti ho to"** *(except means if there is a mistake)*

- **"Program crash karna door hai — user ko message dikhao"**
  *(Crashing the program is far away — show the user a message)*

- **"else matlab sab theek tha"** *(else means everything was fine)*

- **"finally matlab hamesha — galti ho ya na ho"** *(finally means always — error or not)*

---

## Common Mistakes to Watch For

| Mistake | Problem | Fix |
|---------|---------|-----|
| Bare `except:` | Catches ALL errors — even ones you don't expect, hides bugs | Always catch specific errors: `except ValueError:` |
| Not re-asking for input after catching error | Loop exits after one bad input | Use `while True` with `continue` or `break` |
| Catching error but not telling user | Silent failure — user doesn't know what went wrong | Always `print()` a helpful message in `except` |
| Using `try/except` without a loop | Validates once only — user can still give wrong input next time | Wrap in `while True:` loop |

---

## Why This Module Matters

Emphasise to students:

> "Yeh module Module 9 (File I/O) ke liye aur aap ke tamam bade projects ke liye zaroori hai. Agar user ne galat input diya aur program crash ho gaya — project fail. Is liye hum ab se yeh pattern seekhte hain."

*(This module is essential for Module 9 (File I/O) and all your big projects. If a user enters wrong input and the program crashes — the project fails. That is why we learn this pattern now.)*

---

## The Reusable Validation Function — Show This

```python
def get_integer_in_range(prompt, minimum, maximum):
    """
    User se integer input leta hai, validate karta hai aur return karta hai.
    Gets an integer from the user, validates it, and returns it.
    """
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            else:
                print(f"Meherbani karke {minimum} aur {maximum} ke darmiyan number daalein.")
        except ValueError:
            print("Sirf number daalein, haroof nahi.")

# Example use:
marks = get_integer_in_range("Marks daalein (0-100): ", 0, 100)
print(f"Marks: {marks}")
```

Tell students: "Yeh ek complete, professional validation function hai. Aap ise har jagah use kar sakte hain."
*(This is a complete, professional validation function. You can use it everywhere.)*

---

## Files in This Module

| File | Description |
|------|-------------|
| `8_1_what_are_errors.py` | Types of Python errors with examples |
| `8_2_try_except.py` | Basic `try/except` and `try/except/else/finally` |
| `8_3_input_validation.py` | Input validation loop pattern |
| `8_4_quiz.py` | Quiz code |
| `8_5_solutions.py` | Quiz solutions |
