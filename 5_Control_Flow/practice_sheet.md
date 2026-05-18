# Module 5 — Control Flow: Practice Sheet

**Name: ___________________________**
**Date: ________________________**
**Class: _________________________________**

---

Bismillah ir-Rahman ir-Raheem

This practice sheet is for Module 5 — Control Flow. Loops and conditions — the heart of programming!

---

## Section A — Concepts

**Q1.** What does `elif` mean? Write in your own words.

```
_____________________________________________
_____________________________________________
```

---

**Q2.** The code below has an indentation error. Fix it.

```python
# Wrong code:
marks = 75
if marks >= 50:
print("Pass ho gaye!")
print("Mubarak ho!")
```

**Correct code:**

```python
marks = 75
if marks >= 50:
    ___________________________________
    ___________________________________
```

---

**Q3.** What will this code print?

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

**Q4.** Write an if/elif/else that checks whether a number is positive, negative, or zero.

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

**Q5.** What grade will Hassan get if his marks are 73? Use the chart below:

| Marks | Grade |
|-------|-------|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | Fail |

**Hassan's grade: _______________**

---

## Section C — while Loops

**Q6.** Which keyword do you use to exit a loop immediately?

```
a) stop
b) exit
c) break
d) end
```

**Answer: _______________**

---

**Q7.** What is wrong with this code?

```python
while True:
    print("Assalamu Alaikum!")
```

**Mistake: _______________________________________________**

**Fix it:**

```python
ginti = 3
while ginti > 0:
    print("Assalamu Alaikum!")
    ___________________________________
```

---

**Q8.** Write a while loop that counts down from 5 to 1:

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
# Write your code here:
ginti = ___

while ___________________________________________:
    print(ginti)
    ___________________________________

print("Allah Hafiz!")
```

---

## Section D — for Loops

**Q9.** Write a for loop that prints the numbers 1 to 5:

```python
for i in ___________________________________________:
    print(i)
```

---

**Q10.** Complete the Grade Checker below. Print the grade based on marks:

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

**Q11.** In Islamabad, Zainab's school class has 5 students. Their names are: Ahmed, Fatima, Hassan, Zainab, Ibrahim. Write a for loop that prints "Assalamu Alaikum" with each name.

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

Ahmed thought of a secret number: **7**. Your program will let the user keep guessing until they get it right.

Use `while True` and `break` to build this game:

**Requirements:**
- The computer's number is 7 (hard-coded)
- User guesses
- If correct: print "Masha'Allah! Sahi jawab!" and break out of the loop
- If guess is too low: print "Think bigger"
- If guess is too high: print "Think smaller"

```python
secret = 7

print("=== Number Guessing Game ===")
print("I have thought of a number between 1 and 10. Guess it!")

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

## Answer Key (Teacher Only)

| Question | Answer |
|--------|-------|
| Q1 | "else if" — check another condition if the first one was not met |
| Q2 | Indent the `print(...)` statements with 4 spaces |
| Q3 | `0`, `1`, `2` (on three separate lines) |
| Q4 | `if number > 0:` / `elif number < 0:` / `else:` |
| Q5 | B (73 is between 70–79) |
| Q6 | `c) break` |
| Q7 | No `break` — infinite loop. Fix: add a counter |
| Q8 | `ginti = 5`, `while ginti > 0:`, `ginti -= 1` |
| Q9 | `for i in range(1, 6):` |
| Q10 | `>= 80`, `>= 70`, `>= 60`, `>= 50` |
| Q11 | `for naam in talibaat:` / `print(f"Assalamu Alaikum, {naam}!")` |
| Challenge | `if guess == secret: print("Masha'Allah!"); break` / elif/else with messages |
