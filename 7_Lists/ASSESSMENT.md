# Module 7: Lists, Tuples & Dictionaries — Assessment

## Pass Criteria

A student passes this module if they can:

- [ ] Create a list and access items by index
- [ ] Use `append()` to add an item to a list
- [ ] Create a dictionary with at least 3 keys
- [ ] Access a dictionary value using its key
- [ ] Explain the difference between a list and a dictionary

---

## Oral Questions

Ask these questions to check understanding:

1. What index number is the **first** item in a list?
2. How do you **add** a new item to a list?
3. What is the difference between a **list** and a **dictionary**?
4. What is a **tuple** and how is it different from a list?
5. If `student = {"name": "Ahmed"}`, how do you get the value `"Ahmed"`?

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

Ask each student to complete the following task at the computer:

### Task

Create a **dictionary** for a madrasa student with the following keys and appropriate values:

| Key | Example Value |
|-----|---------------|
| `name` | `"Ahmed"` |
| `age` | `14` |
| `city` | `"Lahore"` |
| `subject` | `"Hifz"` |
| `marks` | `88` |

Then **print each value** with a clear label, like:

```
Naam: Ahmed
Umar: 14
Shehar: Lahore
Subject: Hifz
Marks: 88
```

### Sample Solution

```python
student = {
    "name": "Ahmed",
    "age": 14,
    "city": "Lahore",
    "subject": "Hifz",
    "marks": 88
}

print(f"Naam: {student['name']}")
print(f"Umar: {student['age']}")
print(f"Shehar: {student['city']}")
print(f"Subject: {student['subject']}")
print(f"Marks: {student['marks']}")
```

---

## Teacher Observation Checklist

| Student Name | Created list? | Index access? | Used append? | Created dict (3+ keys)? | Dict value access? | Pass/Fail |
|--------------|:-------------:|:-------------:|:------------:|:-----------------------:|:-----------------:|:---------:|
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
|              | ☐ | ☐ | ☐ | ☐ | ☐ | |
