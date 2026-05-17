# Module 5 — Control Flow: Assessment Guide

## Pass Criteria

A student passes Module 5 if they can do ALL of the following:

- [ ] Write an `if/elif/else` block with correct indentation and colons
- [ ] Write a `while` loop that terminates (does not run forever)
- [ ] Write a `for` loop using `range()`
- [ ] Use `break` to exit a loop
- [ ] Explain what indentation means and why it matters in Python

---

## Oral Questions

Ask these questions one-on-one or to the class.

| Question | Expected Answer |
|----------|----------------|
| `elif` ka matlab kya hai? | "warna agar" — else if — ek aur condition check karo |
| Agar `if` ke baad colon (`:`  ) bhool jao toh kya hoga? | `SyntaxError` — program run nahin hoga |
| `while` loop kaise rokein? | Counter update karo, ya `break` use karo |
| `range(5)` mein kaunse numbers hain? | 0, 1, 2, 3, 4 |
| `range(1, 6)` mein kaunse numbers hain? | 1, 2, 3, 4, 5 |
| Indentation kyun zaroori hai Python mein? | Python indentation se pata karta hai ke kaunsa code kis block mein hai |
| `break` kab use karte hain? | Jab loop se pehle baahir nikalna ho |

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
| 15–17 | A+ | Masha'Allah! Bohat zabardast! |
| 12–14 | A | Bohat achha! Loops aur conditions mein strong ho. |
| 9–11 | B | Theek hai — thodi aur practice karo. |
| 6–8 | C | Dobara review karo — teacher se madad lo. |
| 0–5 | Needs Support | Module 5 dobara parho. Pehle Module 3 aur 4 confirm karo. |

---

## Practical Assessment

### Task Description

Students write a **Grade Checker** program that:

1. Asks the user for their **marks** (0–100)
2. Validates input — marks must be between 0 and 100 (use `while` loop)
3. Prints the **grade** using if/elif/else:
   - 90–100 → A+
   - 80–89 → A
   - 70–79 → B
   - 60–69 → C
   - 50–59 → D
   - Below 50 → Fail
4. Prints a **personalised message** with each grade using an f-string

### Sample Solution

```python
# Module 5 Practical — Grade Checker
# Bismillah

print("=== Islamia School Grade Checker ===\n")

naam = input("Apna naam likhein: ")

# Input validation using while loop
while True:
    marks = int(input("Apne marks likhein (0-100): "))
    if 0 <= marks <= 100:
        break
    else:
        print("Galat marks! 0 aur 100 ke beech mein likhein.")

# Grade checking using if/elif/else
if marks >= 90:
    grade = "A+"
    message = "Masha'Allah! Bohat aala performance!"
elif marks >= 80:
    grade = "A"
    message = "Bohat achha! Allah ne aap ko ilm diya hai."
elif marks >= 70:
    grade = "B"
    message = "Achha kaam — aur mehnat karo."
elif marks >= 60:
    grade = "C"
    message = "Theek hai — koshish jaari rakho."
elif marks >= 50:
    grade = "D"
    message = "Pass ho gaye, lekin mehnat aur karo."
else:
    grade = "Fail"
    message = "Ghabrao mat — Allah ke sath mehnat se sab mumkin hai."

print(f"\n{naam} ka grade: {grade}")
print(f"Marks: {marks}/100")
print(f"Paigham: {message}")
```

### Sample Output

```
=== Islamia School Grade Checker ===

Apna naam likhein: Fatima
Apne marks likhein (0-100): 150
Galat marks! 0 aur 100 ke beech mein likhein.
Apne marks likhein (0-100): 87

Fatima ka grade: A
Marks: 87/100
Paigham: Bohat achha! Allah ne aap ko ilm diya hai.
```

### Marking Rubric

| Criterion | Marks |
|-----------|-------|
| `int(input())` used for marks | 1 |
| `while` loop used for input validation | 2 |
| if/elif/else for all 6 grades correct | 3 |
| Correct grade assigned for each range | 2 |
| f-string used for output | 1 |
| Program runs without errors | 1 |
| **Total** | **10** |

---

## Extension Task (For Advanced Students)

Add a feature: Ask marks for 3 subjects (e.g., Urdu, Maths, Islamiat) and calculate the average, then give an overall grade.

```python
urdu    = int(input("Urdu ke marks: "))
maths   = int(input("Maths ke marks: "))
din     = int(input("Islamiat ke marks: "))

average = (urdu + maths + din) / 3
print(f"Average marks: {average:.1f}")

# Then apply grade check on average
```

---

## Remediation

**Cannot write correct indentation:**
Use a ruler or finger on the screen. "Yeh sab 4 spaces andar hai — ek group hai." Demonstrate IndentationError deliberately then fix it together.

**while loop runs forever:**
Show the infinite loop deliberately (print "Hello" forever) then Ctrl+C to stop. Explain: "Counter ko update karna bhool gaye. Har baar loop chalte waqt count kam karo."

**Forgets colon:**
Make a rhyme: "if, elif, else, while, for — in ke baad colon zaroori, yaad rakho har bor."

**Off-by-one error in range:**
- `range(5)` → 0 to 4
- `range(1, 6)` → 1 to 5
Draw a number line on the board.

---

## Notes for Teacher

- This is the **most important module** in the course. Nearly everything after this builds on if/elif/else and loops.
- If students cannot write a correct `while` loop, they cannot build interactive programs. Spend extra time.
- The `while True: break` menu pattern should be **memorised** — write it on the wall of the classroom if possible.
- For madrasa students: link `if/elif/else` to Islamic decision-making — agar fajr ka waqt hai, namaz parhein; warna agar zuhr ka waqt hai, zuhr parhein, etc.
