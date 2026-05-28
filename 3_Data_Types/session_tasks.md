# Module 3 — Data Types: After-Session Tasks
### Complete these on your own after class

---

> **بِسْمِ اللّٰہِ** — Start each task with focus. You can do it!

---

## Task 1 — Type Detective ⭐

What is the data type of each value below?  
Write your answer as a comment, then use `type()` to check.

```python
42
3.14
"Lahore"
True
"99"
False
114
"True"
```

**Expected:** You should find `int`, `float`, `str`, and `bool` values in this list.

---

## Task 2 — Build Variables of Every Type ⭐

Create one variable of each type using an Islamic or Pakistani theme.  
Print each variable with a label and its type.

Example:
```
prayers_per_day = 5       → int
zakat_rate = 2.5          → float
favorite_surah = "Yaseen" → str
is_fasting = True         → bool
```

---

## Task 3 — int(input()) Practice ⭐⭐

Write three separate programs (in three code cells):

**Program A:** Ask the user for a number. Print the number multiplied by 3.

**Program B:** Ask for the price of one roti (in rupees) and how many rotis. Print the total cost.

**Program C:** Ask how many ajza the student has memorized. Print how many remain (Quran = 30 ajza).

---

## Task 4 — Fix the Errors ⭐⭐

Each block below has one error. Fix it and run it.

```python
# Block 1
total = 50
print("Total students: " + total)

# Block 2
num = input("Enter a number: ")
print(num * 2)

# Block 3
x = int("87.5")
print(x)

# Block 4
age = 14
print(f"I am {age years old.")
```

---

## Task 5 — f-string Rewrite ⭐⭐

Rewrite each of these using f-strings (no `+` or `str()` allowed):

```python
name = "Hassan"
city = "Peshawar"
ajza = 12
marks = 88.5

print("My name is " + name + " and I am from " + city + ".")
print("I have memorized " + str(ajza) + " ajza of the Quran.")
print("My marks are " + str(marks) + " out of 100.")
```

---

## Task 6 — Age & Year Calculator ⭐⭐

Ask the user for:
- Their name
- Their birth year

Calculate and print using f-strings:
1. Their current age (year 2026)
2. The year they will turn 18
3. The year they will turn 60

**Expected output:**
```
Assalamu Alaikum Ahmed!
You were born in 2012.
You are approximately 14 years old.
You will turn 18 in 2030.
You will turn 60 in 2072.
```

---

## Task 7 — Full Report Card ⭐⭐⭐

Ask the user for:
- Student name
- Marks in Quran (out of 100, use `int(input())`)
- Marks in Arabic (out of 100)
- Marks in Fiqh (out of 100)

Calculate:
- Total marks (out of 300)
- Percentage

Print a full report card using f-strings:

```
================================
        REPORT CARD
================================
Student   : Ahmed Ali
Quran     : 85 / 100
Arabic    : 78 / 100
Fiqh      : 90 / 100
--------------------------------
Total     : 253 / 300
Percentage: 84.33%
================================
Ma sha Allah! Keep it up!
```

---

## Bonus Challenge ⭐⭐⭐

Build a **Sadaqah Calculator**:

Ask the user for:
- Their monthly income in rupees (use `int(input())`)

Calculate and print using f-strings:
- 2.5% Zakat amount (if income is above 50,000)
- Recommended daily sadaqah (income / 30 / 10)
- Recommended weekly sadaqah

Use variables with clear names. All output must use f-strings.

---

## Marking Guide (for your teacher)

| Task | Marks |
|------|-------|
| Task 1 | 1 |
| Task 2 | 2 |
| Task 3 | 3 |
| Task 4 | 3 |
| Task 5 | 2 |
| Task 6 | 3 |
| Task 7 | 4 |
| Bonus  | 3 |
| **Total** | **21** |

---

*Take your time. The `int(input())` pattern will appear in every future module — make sure you understand it well. Bismillah!*
