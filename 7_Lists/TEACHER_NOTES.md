# Module 7: Lists, Tuples & Dictionaries — Teacher Notes

## Duration
2 classes

---

## Learning Objectives

By the end of this module, students will be able to:

1. Create and use **lists** with square brackets `[]`
2. Access list items by **index** (including negative index)
3. Use `append()`, `remove()`, and `len()` on lists
4. Loop through a list using `for`
5. Create and use **tuples** (immutable ordered collections)
6. Create and use **dictionaries** with key-value pairs
7. Access, add, and update dictionary entries by key

---

## Lesson Flow

### Class 1

| File | Topic |
|------|-------|
| `7_1_lists.py` | Create lists, access by index, `append`, `remove`, `len`, loop through list |
| `7_2_tuples.py` | Same as list but **cannot be changed** — ordered and fixed |

### Class 2

| File | Topic |
|------|-------|
| `7_3_dictionaries.py` | Key-value pairs, accessing by key, adding new keys |
| `7_4_applications.py` | Real-world applied examples |
| Quiz | End-of-module assessment |

---

## Key Concepts Summary

| Type | Syntax | Ordered? | Changeable? | Access by |
|------|--------|----------|-------------|-----------|
| **List** | `[1, 2, 3]` | Yes | Yes | Index |
| **Tuple** | `(1, 2, 3)` | Yes | No | Index |
| **Dictionary** | `{"key": value}` | Yes (Python 3.7+) | Yes | Key |

---

## Index Starts at 0 — Teach This Carefully

This always surprises beginners. Spend time here.

```python
names = ["Ahmed", "Fatima", "Usman"]
#         [0]       [1]       [2]

print(names[0])   # Ahmed   ← first item
print(names[1])   # Fatima
print(names[-1])  # Usman   ← last item (negative index)
```

> Tell students: "Python 0 se shuru karta hai, 1 se nahi. Jaise computer ka zihn alag hota hai!"
> *(Python starts from 0, not 1. It is like a computer thinks differently!)*

Show on the whiteboard: draw boxes with numbers 0, 1, 2 under each item.

---

## Urdu Teaching Tips

- **"List matlab fehrist — jaise shopping list ya class ki hazri list"**
  *(List means a list — like a shopping list or a class attendance list)*

- **"Dictionary matlab koi cheez dhundna — key se value milti hai, jaise asli dictionary mein word dhundna"**
  *(Dictionary means finding something — key gives you the value, like looking up a word in a real dictionary)*

- **"Tuple matlab pakka — change nahi ho sakta. Jaise taareekh-e-wiladat — badal nahi sakti!"**
  *(Tuple means fixed — cannot be changed. Like a date of birth — it cannot change!)*

---

## Common Mistakes to Watch For

| Mistake | Example | Error | Fix |
|---------|---------|-------|-----|
| Index out of range | `names[5]` on a 3-item list | `IndexError` | Check `len()` first |
| Using `[]` with missing dict key | `student["phone"]` when key doesn't exist | `KeyError` | Use `.get("phone")` or check first |
| Confusing `[]` list with `{}` dict | Writing `{1, 2, 3}` thinking it's a list | Wrong type | Lists use `[]`, dicts use `{}` |
| Trying to change a tuple | `months[0] = "Jan"` on a tuple | `TypeError` | Tuples cannot be modified |
| Forgetting quotes around dict keys | `student[name]` | `NameError` | `student["name"]` |

---

## Demonstration Ideas

**List — Class Attendance:**
```python
students = ["Ahmed", "Bilal", "Fatima", "Zainab", "Usman"]
print(f"Total students: {len(students)}")
students.append("Hassan")   # new student joined
students.remove("Bilal")    # student left
```

**Dictionary — Student Record:**
```python
student = {
    "name": "Ahmed",
    "class": "7th",
    "city": "Lahore",
    "marks": 85
}
print(f"Naam: {student['name']}")
print(f"Marks: {student['marks']}")
```

**Surah Dictionary (Islamic Context):**
```python
surahs = {
    "Al-Fatiha": 7,
    "Al-Baqarah": 286,
    "Al-Ikhlas": 4
}
for surah, ayaat in surahs.items():
    print(f"{surah}: {ayaat} ayaat")
```

---

## Files in This Module

| File | Description |
|------|-------------|
| `7_1_lists.py` | List creation, indexing, methods, loops |
| `7_2_tuples.py` | Tuples — immutable sequences |
| `7_3_dictionaries.py` | Dictionary creation and access |
| `7_4_applications.py` | Applied real-world examples |
| `7_5_quiz.py` | Quiz code |
| `7_6_solutions.py` | Quiz solutions |
