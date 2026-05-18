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
| What does `elif` mean? | "else if" — check another condition if the first was not met |
| What happens if you forget the colon (`:`) after `if`? | `SyntaxError` — the program will not run |
| How do you stop a `while` loop? | Update the counter, or use `break` |
| What numbers are in `range(5)`? | 0, 1, 2, 3, 4 |
| What numbers are in `range(1, 6)`? | 1, 2, 3, 4, 5 |
| Why is indentation important in Python? | Python uses indentation to know which code belongs to which block |
| When do you use `break`? | When you want to exit the loop before the condition becomes False |

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
| 15–17 | A+ | Masha'Allah! Outstanding! |
| 12–14 | A | Very good! You are strong with loops and conditions. |
| 9–11 | B | Good — practise a little more. |
| 6–8 | C | Review again — ask the teacher for help. |
| 0–5 | Needs Support | Re-read Module 5. First confirm Modules 3 and 4. |

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
Use a ruler or finger on the screen. "All of this is 4 spaces in — it is one group." Demonstrate IndentationError deliberately then fix it together.

**while loop runs forever:**
Show the infinite loop deliberately (print "Hello" forever) then Ctrl+C to stop. Explain: "We forgot to update the counter. Decrease the count each time the loop runs."

**Forgets colon:**
Make a rhyme: "if, elif, else, while, for — every one of these needs a colon, remember it always."

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
