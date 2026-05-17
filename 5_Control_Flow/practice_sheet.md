# Module 5 — Control Flow: Practice Sheet

**Naam (Name): ___________________________**
**Taareekh (Date): ________________________**
**Class: _________________________________**

---

Bismillah ir-Rahman ir-Raheem

Control Flow ka yeh practice sheet Module 5 ke liye hai. Loops aur conditions — programming ka dil!

---

## Section A — Concepts (Tasawwuraat)

**Q1.** `elif` ka matlab kya hai? Apni zaban mein likhein.

```
_____________________________________________
_____________________________________________
```

---

**Q2.** Neeche wale code mein indentation ki galti hai. Theek karo.

```python
# Galat code:
marks = 75
if marks >= 50:
print("Pass ho gaye!")
print("Mubarak ho!")
```

**Sahi code:**

```python
marks = 75
if marks >= 50:
    ___________________________________
    ___________________________________
```

---

**Q3.** Yeh code kya print karega?

```python
for i in range(3):
    print(i)
```

**Output:**

```
___
___
___
```

---

## Section B — if / elif / else

**Q4.** Ek if/elif/else likhein jo check kare ke koi number positive hai, negative hai, ya zero.

```python
number = int(input("Koi number likhein: "))

if ___________________________________________:
    print("Yeh positive number hai.")
elif ___________________________________________:
    print("Yeh negative number hai.")
else:
    print("Yeh zero hai.")
```

---

**Q5.** Hassan ka grade kya hoga agar uske marks 73 hain? Neeche ke chart mein dekho:

| Marks | Grade |
|-------|-------|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | Fail |

**Hassan ka grade: _______________**

---

## Section C — while Loops

**Q6.** Loop se jaldi baahir nikalne ke liye kaunsa keyword use karte hain?

```
a) stop
b) exit
c) break
d) end
```

**Jawab: _______________**

---

**Q7.** Yeh code kya galat hai?

```python
while True:
    print("Assalamu Alaikum!")
```

**Galti: _______________________________________________**

**Theek karo:**

```python
ginti = 3
while ginti > 0:
    print("Assalamu Alaikum!")
    ___________________________________
```

---

**Q8.** 5 se 1 tak countdown karne ke liye while loop likhein:

**Expected output:**
```
5
4
3
2
1
Allah Hafiz!
```

```python
# Yahan apna code likhein:
ginti = ___

while ___________________________________________:
    print(ginti)
    ___________________________________

print("Allah Hafiz!")
```

---

## Section D — for Loops

**Q9.** 1 se 5 tak numbers print karne ke liye for loop likhein:

```python
for i in ___________________________________________:
    print(i)
```

---

**Q10.** Neeche wala Grade Checker complete karo. Marks ke mutabiq grade print karo:

```python
marks = int(input("Marks likhein: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= ___:
    print("Grade: A")
elif marks >= ___:
    print("Grade: B")
elif marks >= ___:
    print("Grade: C")
elif marks >= ___:
    print("Grade: D")
else:
    print("Grade: Fail")
```

---

## Section E — Mixed Practice

**Q11.** Islamabad mein Zainab ke school ki class mein 5 talibaat hain. Unke naam hain: Ahmed, Fatima, Hassan, Zainab, Ibrahim. Ek for loop likhein jo har naam ke saath "Assalamu Alaikum" print kare.

```python
talibaat = ["Ahmed", "Fatima", "Hassan", "Zainab", "Ibrahim"]

for ___ in ___________________________________________:
    print(f"___________________________________________")
```

**Expected output:**
```
Assalamu Alaikum, Ahmed!
Assalamu Alaikum, Fatima!
Assalamu Alaikum, Hassan!
Assalamu Alaikum, Zainab!
Assalamu Alaikum, Ibrahim!
```

---

## Challenge — Number Guessing Game

Ahmed ne ek secret number socha: **7**. Tumhara program user ko guess karne dega jab tak woh sahi number na de.

`while True` aur `break` use karke yeh game banao:

**Requirements:**
- Computer ka number 7 hai (hard-code karo)
- User guess karta hai
- Agar guess sahi hai: "Masha'Allah! Sahi jawab!" print karo aur loop tod do
- Agar guess kam hai: "Aur bada socho" print karo
- Agar guess zyada hai: "Thoda kam socho" print karo

```python
secret = 7

print("=== Number Guessing Game ===")
print("Main ne 1-10 ke beech ek number socha hai. Guess karo!")

while True:
    guess = int(input("Tumhara guess: "))

    if guess == secret:
        print("___________________________________")
        _______________
    elif guess < secret:
        print("___________________________________")
    else:
        print("___________________________________")
```

---

## Answer Key (Sirf Teacher ke liye)

| Sawaal | Jawab |
|--------|-------|
| Q1 | "warna agar" — ek aur condition check karo agar pehli poori nahin hui |
| Q2 | `print(...)` statements ko 4 spaces indent karo |
| Q3 | `0`, `1`, `2` (teen alag lines mein) |
| Q4 | `if number > 0:` / `elif number < 0:` / `else:` |
| Q5 | B (73 is between 70–79) |
| Q6 | `c) break` |
| Q7 | `break` nahin hai — infinite loop. Fix: counter add karo |
| Q8 | `ginti = 5`, `while ginti > 0:`, `ginti -= 1` |
| Q9 | `for i in range(1, 6):` |
| Q10 | `>= 80`, `>= 70`, `>= 60`, `>= 50` |
| Q11 | `for naam in talibaat:` / `print(f"Assalamu Alaikum, {naam}!")` |
| Challenge | `if guess == secret: print("Masha'Allah!"); break` / elif/else with messages |
