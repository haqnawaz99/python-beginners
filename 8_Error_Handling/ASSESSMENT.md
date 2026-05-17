# Module 8: Error Handling — Assessment

## Pass Criteria

A student passes this module if they can:

- [ ] Write a `try/except` block that catches `ValueError`
- [ ] Write an input validation loop that **keeps asking** until valid input is given
- [ ] Explain in their own words what `try/except` does and why it is useful
- [ ] Name at least 3 types of Python errors

---

## Oral Questions

Ask these questions to check understanding:

1. What happens **without** `try/except` when the user types text instead of a number?
2. What does the `except` block **catch**?
3. When does the `else` clause run in `try/except/else`?
4. When does `finally` run — only when there is an error, or always?
5. Why is `except:` (bare except, catching everything) considered **bad practice**?

---

## Quiz Marking

| Section | Marks |
|---------|-------|
| Easy questions | 5 |
| Medium questions | 6 |
| Complex questions | 6 |
| **Total** | **17** |

---

## Grade Scale

| Marks | Grade | Remarks |
|-------|-------|---------|
| 15 – 17 | A | Mashallah — Excellent |
| 12 – 14 | B | Very Good |
| 9 – 11 | C | Good — Review mistakes |
| 6 – 8 | D | Needs Revision |
| 0 – 5 | F | Repeat module before moving on |

---

## Practical Assessment

Ask each student to complete the following task at the computer:

### Task

Write a function called `get_marks()` that:

1. **Keeps asking** the user to enter marks
2. Handles **`ValueError`** — if the user types text instead of a number, show a friendly message and ask again
3. Handles **out-of-range** — if the number is not between 0 and 100, show a message and ask again
4. **Returns** the valid marks only when input is correct

### Expected Behaviour

```
Marks daalein (0-100): abc
Sirf number daalein.
Marks daalein (0-100): 150
Marks 0 aur 100 ke darmiyan honi chahiye.
Marks daalein (0-100): 85
```
*(Function returns 85)*

### Sample Solution

```python
def get_marks():
    while True:
        try:
            marks = int(input("Marks daalein (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks 0 aur 100 ke darmiyan honi chahiye.")
        except ValueError:
            print("Sirf number daalein.")

result = get_marks()
print(f"Valid marks: {result}")
```

---

## Teacher Observation Checklist

| Student Name | try/except written? | ValueError caught? | Loop re-asks? | Range check? | Returns value? | Pass/Fail |
|--------------|:-------------------:|:------------------:|:-------------:|:------------:|:--------------:|:---------:|
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
