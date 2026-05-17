# Module 4 — Operators: Practice Sheet

**Naam (Name): ___________________________**
**Taareekh (Date): ________________________**
**Class: _________________________________**

---

Bismillah ir-Rahman ir-Raheem

Operators ka yeh practice sheet dhyan se complete karo. Har sawaal mein socho pehle, phir likho.

---

## Section A — Hisaab (Calculations)

**Q1.** `15 % 4` kya hai?

Socho: 15 ko 4 se divide karo. Baaqi kya bachega?

**Jawab: _______________**

---

**Q2.** `2 ** 8` kya hai? (2 ki power 8)

**Jawab: _______________**

Hint: 2, 4, 8, 16, 32, 64, 128, ___

---

**Q3.** `10 // 3` kya dega?

Circle the correct answer:

```
a) 3.33
b) 3
c) 4
d) 1
```

**Jawab: _______________**

---

**Q4.** Kya `5 == 5.0` True hai ya False?

```
a) True
b) False
```

**Jawab: _______________**

**Kyun? (Explain karo): _______________________________________**

---

**Q5.** `not True` kya evaluate hoga?

**Jawab: _______________**

---

## Section B — Code Likhna

**Q6.** Ek condition likhein jo check kare ke ek number 1 aur 100 ke beech mein hai (`and` use karo):

```python
number = 55

# Yahan apni condition likhein:
if ___________________________________________:
    print("Number sahi range mein hai!")
```

---

**Q7.** Neeche wale code mein galti hai. Galti dhoondho aur theek karo.

```python
umar = 15
if umar = 18:
    print("Vote de sakte ho!")
```

**Galti: _______________________________________________**

**Sahi code:**

```python
umar = 15
if ___________________________________________:
    print("Vote de sakte ho!")
```

---

**Q8.** BODMAS ke mutabiq `2 + 3 * 4` ka result kya hoga?

Show your working:

```
Step 1 (pehle * karo): 3 * 4 = ___
Step 2 (phir + karo):  2 + ___ = ___
```

**Jawab: _______________**

---

**Q9.** Hassan school mein hai. Woh pass hoga agar:
- Marks 50 ya zyada hon **AUR**
- Attendance 75 ya zyada ho

Yeh condition code mein likhein:

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

**Q10.** Ahmed ne ek number socha. Woh jaanna chahta hai ke yeh number even hai ya odd. `%` operator use karke yeh check karo.

**Reminder:** Even numbers ka remainder zero hota hai jab 2 se divide karo.

```python
number = int(input("Koi number likhein: "))

# % use karke check karo:
if ___________________________________________:
    print(f"{number} even number hai.")
else:
    print(f"{number} odd number hai.")
```

---

## Section D — Mixed Problems

**Q11.** Neeche wale expressions ke answers likhein:

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

## Challenge — Mushkil Sawaal

Karachi mein Fatima ke school mein 127 talibaat hain. School mein buses hain jo 12 talibaat le ja sakti hain.

Yeh program likhein jo calculate kare:
1. Kitni poori buses chahiyen?
2. Kitni talibaat baaqi rahengi (extra)?
3. Kya extra bus ki zaroorat hogi? (agar koi bhi baaqi hain toh haan)

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

## Answer Key (Sirf Teacher ke liye)

| Sawaal | Jawab |
|--------|-------|
| Q1 | `3` (15 = 4×3 + 3) |
| Q2 | `256` |
| Q3 | `b) 3` |
| Q4 | `True` — Python int aur float compare kar sakta hai |
| Q5 | `False` |
| Q6 | `if 1 <= number <= 100:` ya `if number >= 1 and number <= 100:` |
| Q7 | `=` ko `==` se replace karo: `if umar == 18:` |
| Q8 | Step 1: 12, Step 2: 14 |
| Q9 | `if marks >= 50 and attendance >= 75:` |
| Q10 | `if number % 2 == 0:` |
| Q11 | 14, 2, 81, 3.75, 3, False, False, True |
| Challenge | `poori_buses = 127 // 12` (=10), `baaqi = 127 % 12` (=7), `if baaqi > 0:` |
