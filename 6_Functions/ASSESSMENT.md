# Module 6: Functions — Assessment

## Pass Criteria

A student passes this module if they can:

- [ ] Define a function using `def`
- [ ] Call a function correctly (with parentheses)
- [ ] Pass parameters to a function and use them inside
- [ ] Return a value from a function using `return`
- [ ] Use a default parameter value in a function definition

---

## Oral Questions

Ask these questions to check understanding during or after the lesson:

1. Which keyword is used to define a function in Python?
2. What is the difference between **defining** a function and **calling** a function?
3. What does the `return` keyword do?
4. What is the difference between a **parameter** and an **argument**?
5. If a function has a default parameter, do you have to provide that argument when calling it?

---

## Quiz Marking

| Section | Marks |
|---------|-------|
| Easy questions | 5 |
| Medium questions | 6 |
| Complex questions | 6 |
| **Total** | **17** |

---

## Grade Scale

| Marks | Grade | Remarks |
|-------|-------|---------|
| 15 – 17 | A | Mashallah — Excellent |
| 12 – 14 | B | Very Good |
| 9 – 11 | C | Good — Review mistakes |
| 6 – 8 | D | Needs Revision |
| 0 – 5 | F | Repeat module before moving on |

---

## Practical Assessment

Ask each student (or pair) to complete the following task:

### Task

Write a function called `greet` that:
- Takes two parameters: `name` and `greeting`
- Has a **default value** of `"Assalamu Alaikum"` for `greeting`
- **Returns** the string: `"Assalamu Alaikum, Ahmed!"`  
  (using whatever `name` and `greeting` are passed)

Then **call the function 3 times** with three different names and print the result each time.

### Expected Output (example)

```
Assalamu Alaikum, Ahmed!
Assalamu Alaikum, Fatima!
Assalamu Alaikum, Usman!
```

### Sample Solution

```python
def greet(name, greeting="Assalamu Alaikum"):
    return f"{greeting}, {name}!"

print(greet("Ahmed"))
print(greet("Fatima"))
print(greet("Usman"))
```

---

## Teacher Observation Checklist

Use this during the practical task:

| Student Name | Defined function? | Used parameters? | Used return? | Default parameter? | Pass/Fail |
|--------------|:-----------------:|:----------------:|:------------:|:------------------:|:---------:|
|              | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | |
