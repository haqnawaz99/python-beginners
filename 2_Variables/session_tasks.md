# Module 2 — Variables: After-Session Tasks
### Complete these on your own after class

---

> **بِسْمِ اللّٰہِ** — Start each task with focus. You can do it!

---

## Task 1 — My Islamic Profile ⭐

Write a program that asks the user for:
- Their name
- Their city
- Their favourite Prophet (peace be upon them)
- Their favourite Surah

Then print a neat profile card. Apply `.title()` to the name and city.

**Expected output:**
```
================================
        MY ISLAMIC PROFILE
================================
Name    : Ahmed Ali
City    : Lahore
Prophet : Muhammad (PBUH)
Surah   : Al-Fatiha
================================
JazakAllah Khair!
```

---

## Task 2 — Name Length Checker ⭐

Ask the user to type their first name and last name separately.

Print:
- The full name joined together (with a space)
- The length of the first name
- The length of the last name
- The total length of the full name (including the space)

**Example output:**
```
Full name  : Ahmed Khan
First name : 5 letters
Last name  : 4 letters
Full name  : 10 characters (including space)
```

---

## Task 3 — Name Formatter ⭐⭐

Ask the user to type their name in **any format** (all caps, all lowercase, mixed).

Print the name in all three forms:
1. ALL CAPITALS
2. all lowercase
3. Title Case

**Example output:**
```
You typed   : aHMED aLI
Uppercase   : AHMED ALI
Lowercase   : ahmed ali
Title case  : Ahmed Ali
```

---

## Task 4 — Variable Swap ⭐⭐

Create two variables:
```python
prayer_1 = "Fajr"
prayer_2 = "Isha"
```

Swap them using a temporary variable.  
Print the values before and after the swap.

---

## Task 5 — Madrasa Registration Card ⭐⭐

Ask the user for:
- Student name (apply `.title()`)
- City (apply `.upper()`)
- Class level (e.g. Hifz / Nazra / Alim)
- Favourite Islamic subject

Print a registration card using `\t` for alignment:

**Expected output:**
```
================================
     MADRASA REGISTRATION
================================
Name        :	Ahmed Ali
City        :	LAHORE
Class       :	Hifz
Subject     :	Tafseer
================================
May Allah give you success. Ameen!
```

---

## Task 6 — Predict & Verify ⭐⭐⭐

**Before running**, write what you think each `print()` will output. Then run the code and check.

```python
# Block 1
a = "Quran"
b = a
a = "Hadith"
print(a)
print(b)

# Block 2
city = "Lahore"
city = city + " (Punjab)"
print(city)

# Block 3
name = "  hassan  "
print(name.strip().title())
```

Write your predictions here before running:
```
Block 1 — a: ________   b: ________
Block 2 — city: ________
Block 3 — result: ________
```

---

## Task 7 — Clean Input Program ⭐⭐⭐

Ask the user for their full name.  
The user might type it messily (extra spaces, wrong case).

Your program must:
1. Remove extra spaces with `.strip()`
2. Format it properly with `.title()`
3. Print: `"Assalamu Alaikum, [clean name]!"`
4. Print: `"Your name has [n] letters."` (do NOT count the spaces — hint: use `.replace(" ", "")` inside `len()`)

---

## Bonus Challenge ⭐⭐⭐

Build a **"Three Friends"** program:

1. Ask for the name and city of **three** friends (6 `input()` calls total)
2. Print all three profiles neatly using `\t`
3. Print whose name is longest (just print all three lengths — comparison operators come in Module 5!)

---

## Marking Guide (for your teacher)

| Task | Marks |
|------|-------|
| Task 1 | 2 |
| Task 2 | 2 |
| Task 3 | 2 |
| Task 4 | 2 |
| Task 5 | 3 |
| Task 6 | 3 |
| Task 7 | 3 |
| Bonus  | 3 |
| **Total** | **20** |

---

*Take your time. Read each task twice before writing code. Bismillah!*
