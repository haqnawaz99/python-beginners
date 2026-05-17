# Module 7: Lists, Tuples & Dictionaries — Practice Sheet

**Naam / Name:** ___________________________  
**Tareeq / Date:** ___________________________  
**Class:** ___________________________

---

## Q1 — Easy

Given this list:

```python
cities = ["Lahore", "Karachi", "Islamabad"]
```

What does `cities[0]` return?

**Answer:** ___________________________

---

## Q2 — Easy

How do you **add** `"Peshawar"` to the `cities` list above?

```python
# Write the code:

```

---

## Q3 — Easy

What is the output of this code?

```python
print(len(["a", "b", "c"]))
```

**Answer:** ___________________________

---

## Q4 — Easy

Write code to create a **list** of 5 Pakistani cities.

```python
# Write your list here:


```

---

## Q5 — Medium

What is a **tuple**? How is it different from a list?

**Answer:** ___________________________

Write an example of a tuple containing 3 months:

```python
# Write your tuple here:

```

---

## Q6 — Medium

Create a **dictionary** for a madrasa student with three keys: `name`, `class_level`, and `marks`.

```python
# Write your dictionary here:




```

---

## Q7 — Medium

Given this dictionary:

```python
student = {"name": "Fatima", "marks": 92}
```

How do you access the value for the key `"name"`?

```python
# Write the code:

```

**What will it print?** ___________________________

---

## Q8 — Medium

What **error** occurs if you try to access index `5` in a list that only has `3` items?

**Answer:** ___________________________

---

## Q9 — Complex

Write a `for` loop that prints each subject from this list on a new line:

```python
subjects = ["Quran", "Urdu", "Maths"]
```

```python
# Write your loop here:



```

**Expected output:**

```
Quran
Urdu
Maths
```

---

## Challenge — Surah Ayaat Counter

> *"The Quran has 114 Surahs, each with a different number of ayaat."*

Create a **dictionary** of **5 Surahs** with their number of ayaat:

| Surah | Ayaat |
|-------|-------|
| Al-Fatiha | 7 |
| Al-Baqarah | 286 |
| Al-Imran | 200 |
| Al-Ikhlas | 4 |
| Al-Kawthar | 3 |

Then write a loop to **print each Surah name and its ayat count** clearly.

```python
# Create the dictionary:




# Print each surah:




```

**Expected output:**

```
Al-Fatiha: 7 ayaat
Al-Baqarah: 286 ayaat
Al-Imran: 200 ayaat
Al-Ikhlas: 4 ayaat
Al-Kawthar: 3 ayaat
```

---

## Answers (Teacher Section)

| Q | Answer |
|---|--------|
| Q1 | `"Lahore"` |
| Q2 | `cities.append("Peshawar")` |
| Q3 | `3` |
| Q4 | e.g. `cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta"]` |
| Q5 | A tuple is like a list but cannot be changed. e.g. `months = ("January", "February", "March")` |
| Q6 | `student = {"name": "Ahmed", "class_level": "7th", "marks": 85}` |
| Q7 | `print(student["name"])` → `Fatima` |
| Q8 | `IndexError` |
| Q9 | `for subject in subjects: print(subject)` |
| Challenge | `for surah, ayaat in surahs.items(): print(f"{surah}: {ayaat} ayaat")` |
