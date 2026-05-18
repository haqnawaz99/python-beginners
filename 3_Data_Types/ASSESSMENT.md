# Module 3 — Data Types: Assessment Guide

## Pass Criteria

A student passes Module 3 if they can do ALL of the following:

- [ ] Use `type()` to find the type of a value
- [ ] Convert a string to an integer using `int()`
- [ ] Use the `int(input())` pattern correctly
- [ ] Write a working f-string that includes a variable

---

## Oral Questions

Ask these questions one-on-one or to the class. Look for confident, correct answers.

| Question | Expected Answer |
|----------|----------------|
| What will `type(5)` return? | `<class 'int'>` |
| What will `type(3.14)` return? | `<class 'float'>` |
| What is the result of `int("25")`? | `25` (as integer) |
| What happens with `int("Ahmed")`? | Error — ValueError |
| If name = "Hassan", how do you write an f-string? | `f"Mera naam {name} hai"` |
| What type does `input()` always return? | String (`str`) |
| How do you convert input to do math? | `int(input(...))` |

---

## Quiz Marking Scheme

**Total Marks: 17**

| Section | Questions | Marks Each | Total |
|---------|-----------|-----------|-------|
| Easy | 5 questions | 1 mark | 5 marks |
| Medium | 3 questions | 2 marks | 6 marks |
| Complex | 2 questions | 3 marks | 6 marks |

### Grade Scale

| Marks | Grade | Message |
|-------|-------|---------|
| 15–17 | A+ | Masha'Allah! Excellent work! |
| 12–14 | A | Very good! Keep working hard. |
| 9–11 | B | Good — keep practising. |
| 6–8 | C | Review again and ask your teacher. |
| 0–5 | Needs Support | See the teacher — extra help needed. |

---

## Practical Assessment

### Task Description

Students write a complete program that does the following:

1. Asks the user for their **name**
2. Asks the user for their **birth year** (as integer)
3. Calculates their **age** (current year is 2026)
4. Prints the result using an **f-string**

### Sample Solution

```python
# Module 3 Practical — Umar Calculator
naam = input("Apna naam likhein: ")
paidaishi_saal = int(input("Apna paidaishi saal likhein: "))

umar = 2026 - paidaishi_saal

print(f"Assalamu Alaikum {naam}!")
print(f"Aap ki umar takriban {umar} saal hai.")
```

### Sample Output

```
Apna naam likhein: Zainab
Apna paidaishi saal likhein: 2012
Assalamu Alaikum Zainab!
Aap ki umar takriban 14 saal hai.
```

### Marking Rubric

| Criterion | Marks |
|-----------|-------|
| `input()` used correctly for name | 1 |
| `int(input())` used for birth year | 2 |
| Age calculated correctly | 2 |
| f-string used for output | 2 |
| Program runs without errors | 1 |
| Correct output displayed | 2 |
| **Total** | **10** |

---

## Remediation

If a student struggles, focus on these specific areas:

**Cannot use `type()`:**
Show them: `print(type(42))` and `print(type("Ahmed"))` side by side.

**Forgets `int()` with `input()`:**
Ask: "If Ahmed types 5, does Python know it is a number?" Answer: No — it sees `"5"` (a string). So we wrap it: `int(input(...))`.

**f-string problems:**
Check: Is the `f` before the opening quote? Are curly braces `{}` used (not round brackets)?

---

## Notes for Teacher

- The `int(input())` pattern is the single most important thing in this module.
- Do not rush past it — spend extra time if needed.
- Every future module (calculators, games, etc.) depends on this pattern.
- If a student cannot do the practical, they should review Module 3 before proceeding.
