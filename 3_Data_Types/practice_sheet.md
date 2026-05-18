# Module 3 — Data Types: Practice Sheet

**Name: ___________________________**
**Date: ________________________**
**Class: _________________________________**

---

Bismillah ir-Rahman ir-Raheem

This practice sheet is for Module 3. Read each question carefully and write your answers.

---

## Section A — Short Answer

**Q1.** What will `type(3.14)` return? Circle the correct answer.

```
a) <class 'int'>
b) <class 'float'>
c) <class 'str'>
d) <class 'bool'>
```

**Answer: _______________**

---

**Q2.** The code below has an error. Find the mistake and fix it.

```python
# Wrong code:
age = int("Ahmed")
print(age)
```

**What is the mistake?**

```
_____________________________________________
_____________________________________________
```

**Write the correct code:**

```python
# Correct code:
age = ___________________________________
```

---

**Q3.** If `name = "Ahmed"`, what will the output of the f-string below be?

```python
print(f"Assalamu Alaikum {name}")
```

**Output: _______________________________________________**

---

**Q4.** Ask the user for their age and store it as an integer. Write the code:

```python
# Write your code here:
umar = ___________________________________
```

---

**Q5.** What result will the calculation below give?

```python
result = int("25") + int("10")
print(result)
```

**Result: _______________**

---

**Q6.** Convert `99` to a string using `str()`:

```python
number = 99
text = ___________________________________
print(type(text))  # should show <class 'str'>
```

---

## Section B — Writing Code

**Q7.** Write an f-string that prints:
> **Ahmed is 15 years old**

```python
naam = "Ahmed"
umar = 15

print(  ________________________________  )
```

---

**Q8.** Explain — why do we use `int(input())` when we want a number from the user? (Write in your own words.)

```
_____________________________________________
_____________________________________________
_____________________________________________
```

---

## Section C — Fix the Bug

**Q9.** What is wrong with the code below? Fix it.

```python
# Wrong:
naam = "Fatima"
city = "Lahore"
print("Main {naam} hoon aur {city} mein rehti hoon.")
```

**Mistake: _______________________________________________**

**Correct code:**

```python
print(  ________________________________  )
```

---

**Q10.** This code crashes. Why? And how do you fix it?

```python
saal = input("Paidaishi saal likhein: ")
umar = 2026 - saal
print(umar)
```

**Why it crashes:**

```
_____________________________________________
```

**Fixed code:**

```python
saal = ___________________________________
umar = 2026 - saal
print(f"Aap ki umar hai: {umar}")
```

---

## Challenge — Difficult Question

Ahmed, Hassan, and Zainab want to write a program that takes two numbers from the user and prints their total. Write the complete program:

**Requirements:**
- Get the first number from the user (integer)
- Get the second number from the user (integer)
- Add both numbers
- Print the result using an f-string
- Example output: `Ahmed ki calculation: 25 + 10 = 35`

```python
# Write your program here:




```

---

## Answer Key (Teacher Only)

| Question | Answer |
|--------|-------|
| Q1 | `b) <class 'float'>` |
| Q2 | `int("Ahmed")` is wrong — only numeric strings can be converted. `age = int("15")` or `age = int(input(...))` |
| Q3 | `Assalamu Alaikum Ahmed` |
| Q4 | `umar = int(input("Apni umar likhein: "))` |
| Q5 | `35` |
| Q6 | `text = str(99)` |
| Q7 | `print(f"{naam} is {umar} years old")` |
| Q8 | Because `input()` always returns a string; to do math you must convert it with `int()` |
| Q9 | `f` prefix is missing. Correct: `print(f"Main {naam} hoon aur {city} mein rehti hoon.")` |
| Q10 | `saal` is a string, cannot subtract from an integer. `saal = int(input(...))` |
| Challenge | `n1 = int(input(...))`, `n2 = int(input(...))`, `print(f"... {n1} + {n2} = {n1+n2}")` |
