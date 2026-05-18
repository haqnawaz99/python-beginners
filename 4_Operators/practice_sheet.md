# Module 4 — Operators: Practice Sheet

**Name: ___________________________**
**Date: ________________________**
**Class: _________________________________**

---

Bismillah ir-Rahman ir-Raheem

Complete this operators practice sheet carefully. Think before you write, then write.

---

## Section A — Calculations

**Q1.** What is `15 % 4`?

Think: divide 15 by 4. What is the remainder?

**Answer: _______________**

---

**Q2.** What is `2 ** 8`? (2 to the power of 8)

**Answer: _______________**

Hint: 2, 4, 8, 16, 32, 64, 128, ___

---

**Q3.** What does `10 // 3` give?

Circle the correct answer:

```
a) 3.33
b) 3
c) 4
d) 1
```

**Answer: _______________**

---

**Q4.** Is `5 == 5.0` True or False?

```
a) True
b) False
```

**Answer: _______________**

**Why? (Explain): _______________________________________**

---

**Q5.** What does `not True` evaluate to?

**Answer: _______________**

---

## Section B — Writing Code

**Q6.** Write a condition that checks whether a number is between 1 and 100 (use `and`):

```python
number = 55

# Write your condition here:
if ___________________________________________:
    print("Number sahi range mein hai!")
```

---

**Q7.** There is a mistake in the code below. Find it and fix it.

```python
umar = 15
if umar = 18:
    print("Vote de sakte ho!")
```

**Mistake: _______________________________________________**

**Correct code:**

```python
umar = 15
if ___________________________________________:
    print("Vote de sakte ho!")
```

---

**Q8.** Following BODMAS, what is the result of `2 + 3 * 4`?

Show your working:

```
Step 1 (multiply first): 3 * 4 = ___
Step 2 (then add):       2 + ___ = ___
```

**Answer: _______________**

---

**Q9.** Hassan is at school. He will pass if:
- Marks are 50 or above **AND**
- Attendance is 75 or above

Write this condition in code:

```python
marks = int(input("Marks likhein: "))
attendance = int(input("Attendance % likhein: "))

if ___________________________________________:
    print("Hassan pass ho gaya! Masha'Allah!")
else:
    print("Hassan fail ho gaya. Mehnat karo.")
```

---

## Section C — Even/Odd Challenge

**Q10.** Ahmed thought of a number. He wants to know if it is even or odd. Check this using the `%` operator.

**Reminder:** Even numbers have a remainder of zero when divided by 2.

```python
number = int(input("Koi number likhein: "))

# Check using %:
if ___________________________________________:
    print(f"{number} even number hai.")
else:
    print(f"{number} odd number hai.")
```

---

## Section D — Mixed Problems

**Q11.** Write the answers to the expressions below:

| Expression | Answer |
|-----------|--------|
| `100 // 7` | |
| `100 % 7` | |
| `3 ** 4` | |
| `15 / 4` | |
| `15 // 4` | |
| `not (5 > 3)` | |
| `(3 > 2) and (10 < 5)` | |
| `(3 > 2) or (10 < 5)` | |

---

## Challenge — Difficult Question

In Karachi, Fatima's school has 127 female students. The school has buses that can carry 12 students each.

Write a program that calculates:
1. How many complete buses are needed?
2. How many students will be left over (extra)?
3. Is an extra bus needed? (yes if there are any students left over)

```python
talibaat = 127
bus_capacity = 12

poori_buses = ___________________________
baaqi = ___________________________

print(f"Poori buses: {poori_buses}")
print(f"Baaqi talibaat: {baaqi}")

if baaqi _____ 0:
    print("Ek aur bus chahiye!")
else:
    print("Sab buses mein fit ho gayin.")
```

---

## Answer Key (Teacher Only)

| Question | Answer |
|--------|-------|
| Q1 | `3` (15 = 4×3 + 3) |
| Q2 | `256` |
| Q3 | `b) 3` |
| Q4 | `True` — Python can compare int and float |
| Q5 | `False` |
| Q6 | `if 1 <= number <= 100:` or `if number >= 1 and number <= 100:` |
| Q7 | Replace `=` with `==`: `if umar == 18:` |
| Q8 | Step 1: 12, Step 2: 14 |
| Q9 | `if marks >= 50 and attendance >= 75:` |
| Q10 | `if number % 2 == 0:` |
| Q11 | 14, 2, 81, 3.75, 3, False, False, True |
| Challenge | `poori_buses = 127 // 12` (=10), `baaqi = 127 % 12` (=7), `if baaqi > 0:` |
