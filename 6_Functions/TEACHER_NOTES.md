# Module 6: Functions — Teacher Notes

## Duration
2 classes

---

## Learning Objectives

By the end of this module, students will be able to:

1. Define a function using the `def` keyword
2. Call a function correctly
3. Pass information into functions using parameters and arguments
4. Get information back from functions using `return`
5. Use default parameter values for optional arguments

---

## Lesson Flow

### Class 1

| File | Topic |
|------|-------|
| `6_1_basic_functions.py` | What is a function? Why use it? (reusability). Define a function and call it. |
| `6_2_parameters.py` | Passing information into a function using parameters |

### Class 2

| File | Topic |
|------|-------|
| `6_3_return_values.py` | Getting information out of a function using `return` |
| `6_4_default_parameters.py` | Optional arguments with default values |
| `6_5_applications.py` | Real-world application examples |
| Quiz | End-of-module assessment |

---

## Key Concept

> **A function is a reusable block of code — write once, run many times.**

Use this analogy for students:

> "Ek recipe ki tarah hai — aap ek baar likhte hain, phir baar baar pakate hain. Aapko har baar recipe dobara likhne ki zaroorat nahi."
> *(It is like a recipe — you write it once, then cook it many times. You don't need to rewrite the recipe each time.)*

---

## Parameter vs Argument — Important Distinction

| Term | Where | Example |
|------|-------|---------|
| **Parameter** | In the function **definition** | `def greet(name):` — here `name` is a parameter |
| **Argument** | In the function **call** | `greet("Ahmed")` — here `"Ahmed"` is an argument |

Explain simply: parameter is the placeholder, argument is the actual value.

---

## Urdu Teaching Tips

- **"Function matlab machine — andar daalo, kuch karo, bahar nikalo"**
  *(Function means machine — put something in, do something, take something out)*

- **"def matlab define karo — naam do is machine ko"**
  *(def means define — give this machine a name)*

- Write on the board: `INPUT → [FUNCTION] → OUTPUT`

---

## Common Mistakes to Watch For

| Mistake | Example | Fix |
|---------|---------|-----|
| Calling function before defining it | `greet()` written before `def greet():` | Always define first |
| Forgetting `return` keyword | `def add(a,b): a + b` | `return a + b` |
| Not storing return value | `add(3, 4)` | `result = add(3, 4)` |
| Confusing `def` name with variable name | Using `add` as both function and variable | Use different names |
| Missing colon after `def` line | `def greet(name)` | `def greet(name):` |

---

## Important: Show the Validation Pattern

Demonstrate how `get_integer_in_range()` works — this is a pattern students will use in ALL future projects:

```python
def get_integer_in_range(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            else:
                print(f"Meherbani karke {minimum} aur {maximum} ke darmiyan number daalein.")
        except ValueError:
            print("Sirf number daalein, haroof nahi.")
```

Tell students: "Yeh function aap ke saath Module 9 tak aur capstone projects mein bhi rahega."
*(This function will stay with you through Module 9 and capstone projects too.)*

---

## Files in This Module

| File | Description |
|------|-------------|
| `6_1_basic_functions.py` | Define and call simple functions |
| `6_2_parameters.py` | Functions with parameters |
| `6_3_return_values.py` | Return values from functions |
| `6_4_default_parameters.py` | Default parameter values |
| `6_5_applications.py` | Applied examples |
| `6_6_quiz.py` | Quiz code |
| `6_7_solutions.py` | Quiz solutions |
