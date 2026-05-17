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
| `17 % 5` kya hai? | `2` (remainder when 17 is divided by 5) |
| `==` aur `=` mein kya farq hai? | `=` assign karta hai, `==` compare karta hai |
| `2 ** 3` kya hai? | `8` |
| `10 // 3` kya dega? | `3` (sirf poora hissa) |
| `10 / 3` kya dega? | `3.333...` (decimal) |
| `True and False` kya hai? | `False` |
| `True or False` kya hai? | `True` |
| `not True` kya hai? | `False` |
| BODMAS mein kya pehle calculate hota hai? | Brackets, phir power, phir * aur /, phir + aur - |

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
| 15–17 | A+ | Masha'Allah! Kamaal kar diya! |
| 12–14 | A | Bohat achha — thoda aur practice karo. |
| 9–11 | B | Achha — operators dobara review karo. |
| 6–8 | C | Teacher se madad lo aur practice karo. |
| 0–5 | Needs Support | Module dobara parho — teacher se milein. |

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
    print(f"{pehla} bada hai {doosra} se.")
elif pehla == doosra:
    print(f"Dono numbers baraabar hain!")
else:
    print(f"{doosra} bada hai {pehla} se.")
```

---

## Remediation

**Cannot distinguish `//` from `/`:**
Use the madrasa example: "35 talibaan, 6 per group. Kitne poore groups?" Answer is `35 // 6 = 5`, not `5.83...`.

**Confuses `=` with `==`:**
Explain: "`=` deta hai (assignment), `==` poochta hai (question)." Write on board:
- `naam = "Ahmed"` → Ahmed ko naam diya
- `naam == "Ahmed"` → Kya naam Ahmed hai? True ya False?

**Cannot use `and`/`or`:**
Use this real-world example: "Scholarship ke liye: marks >= 80 AND attendance >= 75. Dono zaroori hain."

---

## Notes for Teacher

- The `=` vs `==` mistake is the #1 bug students will write in Module 5. Catch it now.
- Make sure students understand `%` conceptually (remainder) — not just as a symbol.
- BODMAS matters — test it with: `2 + 3 * 4` (should get 14, not 20).
