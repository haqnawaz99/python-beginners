# Module 8: Error Handling — Practice Sheet

**Naam / Name:** ___________________________  
**Tareeq / Date:** ___________________________  
**Class:** ___________________________

---

## Q1 — Easy

What **type of error** occurs when you run this code?

```python
number = int("Ahmed")
```

**Answer:** ___________________________

---

## Q2 — Easy

Write a `try/except` block that safely converts user input to an integer. If the user types text, print `"Sirf number daalein!"`.

```python
# Write your code here:




```

---

## Q3 — Easy

What is the purpose of the **`else`** clause in a `try/except/else` block?

**Answer:** ___________________________

---

## Q4 — Easy

This code will **crash** if the user types text. Fix it so it does not crash:

```python
marks = int(input("Enter marks: "))
print(f"Marks: {marks}")
```

```python
# Fixed code:




```

---

## Q5 — Medium

What does **`finally`** do? When does it run?

**Answer:** ___________________________

Write an example:

```python
# Example with finally:




```

---

## Q6 — Medium

Write a `while` loop that **keeps asking** for a number until the user enters a valid integer (not text).

```python
# Write your loop here:




```

---

## Q7 — Medium

What is the difference between a **`SyntaxError`** and a **`ValueError`**?

| | SyntaxError | ValueError |
|-|-------------|------------|
| When does it happen? | | |
| Example | | |

---

## Q8 — Complex

Write code to open a file called `"marks.txt"` safely. If the file does not exist, print `"File nahi mili!"` instead of crashing.

```python
# Write your code here:




```

---

## Q9 — Complex

Why is **bare `except:`** (without specifying an error type) considered bad practice?

**Answer:** ___________________________

Write the **better** version of this code:

```python
# Bad practice:
try:
    number = int(input("Number: "))
except:
    print("Kuch galat hua.")
```

```python
# Better version:




```

---

## Challenge — Reusable Validation Function

Write a function called `get_integer_in_range(prompt, min_val, max_val)` that:

1. Shows the `prompt` to the user
2. Keeps asking until the user enters a valid **integer**
3. Keeps asking until the number is **between `min_val` and `max_val`** (inclusive)
4. Handles `ValueError` with a helpful message
5. Handles out-of-range with a helpful message
6. **Returns** the valid number

This function should be **reusable for any situation** — marks, age, menu choices, etc.

```python
# Write your function here:




```

Test it with two different calls:

```python
# Test 1 — marks between 0 and 100:
marks = get_integer_in_range("Marks daalein (0-100): ", 0, 100)
print(f"Marks: {marks}")

# Test 2 — menu choice between 1 and 5:
choice = get_integer_in_range("Choice karein (1-5): ", 1, 5)
print(f"Aap ne choose kiya: {choice}")
```

---

## Answers (Teacher Section)

| Q | Answer |
|---|--------|
| Q1 | `ValueError` |
| Q2 | `try: n = int(input("...")) except ValueError: print("Sirf number daalein!")` |
| Q3 | The `else` block runs only if **no error** occurred in the `try` block |
| Q4 | Wrap in `try/except ValueError` |
| Q5 | `finally` always runs — whether there was an error or not. Used for cleanup. |
| Q6 | `while True: try: n = int(input(...)); break  except ValueError: print(...)` |
| Q7 | `SyntaxError` = code is written wrong (caught before running). `ValueError` = code runs but value is wrong type/format. |
| Q8 | `try: f = open("marks.txt")  except FileNotFoundError: print("File nahi mili!")` |
| Q9 | Bare `except` catches all errors including unexpected ones, hides bugs. Better: `except ValueError:` |
| Challenge | Full `get_integer_in_range` function with `while True`, `try/except ValueError`, range check, and `return` |
