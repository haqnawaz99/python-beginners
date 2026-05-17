# Module 6: Functions — Practice Sheet

**Naam / Name:** ___________________________  
**Tareeq / Date:** ___________________________  
**Class:** ___________________________

---

## Q1 — Easy

Which keyword is used to **define** a function in Python?

**Answer:** ___________________________

---

## Q2 — Easy

What is wrong with this code?

```python
def my_function
    print("Hello!")
```

**Answer:** ___________________________

---

## Q3 — Easy

Write a function called `bismillah_greeting` that takes a `name` parameter and **prints**:

```
Bismillah, Ahmed!
```

(Replace Ahmed with whatever name is passed)

```python
# Write your function here:




```

---

## Q4 — Easy

What does the `return` keyword do inside a function?

**Answer:** ___________________________

---

## Q5 — Medium

Write a function called `add` that takes two parameters `a` and `b` and **returns** their sum.

```python
# Write your function here:




```

---

## Q6 — Medium

What is a **default parameter**? Write one example of a function that uses a default parameter.

**Answer:** ___________________________

```python
# Example:




```

---

## Q7 — Medium

Call the function `add(10, 20)` from Q5 and **print** the result.

```python
# Write your code here:


```

**What will the output be?** ___________________________

---

## Q8 — Medium

Write a function called `check_result` that:
- Takes one parameter: `marks`
- Returns `"Pass"` if marks are 50 or above
- Returns `"Fail"` if marks are below 50

```python
# Write your function here:




```

---

## Q9 — Complex

What happens if you **define** a function but **never call** it?

**Answer:** ___________________________

---

## Challenge — Zakat Calculator

> *"Zakat is obligatory on savings that reach the nisab. The rate is 2.5%."*

Write a function called `calculate_zakat` that:
- Takes one parameter: `amount` (savings in rupees)
- Returns **2.5% of the amount**

Then test it with savings of **100,000 rupees** and print the result clearly.

```python
# Write your function here:




# Test it:


```

**Expected output:**

```
100000 rupees ki zakat: 2500.0 rupees
```

---

## Answers (Teacher Section)

| Q | Answer |
|---|--------|
| Q1 | `def` |
| Q2 | Missing parentheses `()` and colon `:` after the function name — correct: `def my_function():` |
| Q3 | `def bismillah_greeting(name): print(f"Bismillah, {name}!")` |
| Q4 | It sends a value back to wherever the function was called from |
| Q5 | `def add(a, b): return a + b` |
| Q6 | A value used when no argument is provided — e.g., `def greet(name, msg="Salaam"):` |
| Q7 | `print(add(10, 20))` → output: `30` |
| Q8 | `def check_result(marks): return "Pass" if marks >= 50 else "Fail"` |
| Q9 | Nothing happens — the code inside is never executed |
| Challenge | `def calculate_zakat(amount): return amount * 0.025` → `2500.0` |
