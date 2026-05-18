# Module 4 — Operators: Assessment Guide

## Pass Criteria

A student passes Module 4 if they can do ALL of the following:

- [ ] Correctly calculate using all six math operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- [ ] Explain the difference between `/` and `//`
- [ ] Compare two values using `==`, `!=`, `<`, `>`, `<=`, `>=`
- [ ] Use `and`, `or`, `not` to combine conditions
- [ ] Identify the difference between `=` (assignment) and `==` (comparison)

---

## Oral Questions

Ask these questions individually or to the class. Students should answer quickly and confidently.

| Question | Expected Answer |
|----------|----------------|
| What is `17 % 5`? | `2` (remainder when 17 is divided by 5) |
| What is the difference between `==` and `=`? | `=` assigns a value, `==` compares two values |
| What is `2 ** 3`? | `8` |
| What does `10 // 3` give? | `3` (whole part only) |
| What does `10 / 3` give? | `3.333...` (decimal) |
| What is `True and False`? | `False` |
| What is `True or False`? | `True` |
| What is `not True`? | `False` |
| In BODMAS, what is calculated first? | Brackets, then powers, then * and /, then + and - |

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
| 15–17 | A+ | Masha'Allah! Outstanding work! |
| 12–14 | A | Very good — practise a little more. |
| 9–11 | B | Good — review the operators again. |
| 6–8 | C | Ask the teacher for help and keep practising. |
| 0–5 | Needs Support | Re-read the module — see the teacher. |

---

## Practical Assessment

### Task Description

Students write a **simple calculator** that:

1. Asks the user for **two numbers**
2. Calculates and displays **all six results**: `+`, `-`, `*`, `/`, `//`, `%`
3. Uses f-strings for clear output
4. Runs without any errors

### Sample Solution

```python
# Module 4 Practical — Calculator
# Bismillah

print("=== Hisab Kitab Calculator ===")

pehla  = int(input("Pehla number likhein: "))
doosra = int(input("Doosra number likhein: "))

print(f"\nNataaij (Results):")
print(f"{pehla} + {doosra}  = {pehla + doosra}")
print(f"{pehla} - {doosra}  = {pehla - doosra}")
print(f"{pehla} * {doosra}  = {pehla * doosra}")
print(f"{pehla} / {doosra}  = {pehla / doosra:.2f}")
print(f"{pehla} // {doosra} = {pehla // doosra}")
print(f"{pehla} % {doosra}  = {pehla % doosra}")
```

### Sample Output

```
=== Hisab Kitab Calculator ===
Pehla number likhein: 17
Doosra number likhein: 5

Nataaij (Results):
17 + 5  = 22
17 - 5  = 12
17 * 5  = 85
17 / 5  = 3.40
17 // 5 = 3
17 % 5  = 2
```

### Marking Rubric

| Criterion | Marks |
|-----------|-------|
| `int(input())` used for both numbers | 2 |
| Addition and subtraction correct | 1 |
| Multiplication and division correct | 1 |
| `//` (integer division) correct | 2 |
| `%` (remainder) correct | 2 |
| f-strings used for output | 1 |
| Program runs without errors | 1 |
| **Total** | **10** |

---

## Extension Task (For Advanced Students)

Ask students to **add a bonus feature**: check if the first number is greater than, equal to, or less than the second, and print a message.

```python
if pehla > doosra:
    print(f"{pehla} is greater than {doosra}.")
elif pehla == doosra:
    print(f"Both numbers are equal!")
else:
    print(f"{doosra} is greater than {pehla}.")
```

---

## Remediation

**Cannot distinguish `//` from `/`:**
Use the madrasa example: "35 students, 6 per group. How many complete groups?" Answer is `35 // 6 = 5`, not `5.83...`.

**Confuses `=` with `==`:**
Explain: "`=` gives a value (assignment), `==` asks a question (comparison)." Write on board:
- `naam = "Ahmed"` → Ahmed is assigned to naam
- `naam == "Ahmed"` → Is naam equal to Ahmed? True or False?

**Cannot use `and`/`or`:**
Use this real-world example: "For the scholarship: marks >= 80 AND attendance >= 75. Both are required."

---

## Notes for Teacher

- The `=` vs `==` mistake is the #1 bug students will write in Module 5. Catch it now.
- Make sure students understand `%` conceptually (remainder) — not just as a symbol.
- BODMAS matters — test it with: `2 + 3 * 4` (should get 14, not 20).
