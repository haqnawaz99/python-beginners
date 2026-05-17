# ================================================
# Module 5 - Lesson 3: For Loops
# ================================================
# Learn: for loop, range(), looping over lists,
#        enumerate(), break, continue, nested loops
# ================================================

print("=" * 50)
print("For Loops — Repeating a Fixed Number of Times")
print("=" * 50)

# ------------------------------------------------
# What is a for loop?
# ------------------------------------------------
# A for loop repeats code a specific number of times,
# or once for each item in a collection.
# Use for loops when you KNOW how many times to repeat.
# Use while loops when you DON'T know in advance.

# ------------------------------------------------
# 1. for with range()
# ------------------------------------------------
print("\n1. for with range():")

# range(5) gives: 0, 1, 2, 3, 4
for i in range(5):
    print(f"Step {i}")

# range(1, 6) gives: 1, 2, 3, 4, 5
print()
for i in range(1, 6):
    print(f"Count: {i}")

# range(1, 11, 2) gives: 1, 3, 5, 7, 9  (step of 2)
print()
print("Odd numbers:")
for i in range(1, 11, 2):
    print(i)

# ------------------------------------------------
# 2. Looping over a list
# ------------------------------------------------
print("\n2. Looping over a list:")

prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
for prayer in prayers:
    print(f"Prayer: {prayer}")

print()
subjects = ["Quran", "Hadith", "Fiqh", "Arabic", "Seerah"]
for subject in subjects:
    print(f"Today we study: {subject}")

# ------------------------------------------------
# 3. Looping over a string
# ------------------------------------------------
print("\n3. Looping over a string:")

word = "PAKISTAN"
for letter in word:
    print(letter)

# Count a specific letter
count = 0
name = "Muhammad"
for letter in name:
    if letter == "a" or letter == "A":
        count += 1
print(f"Letter 'a' appears {count} times in '{name}'")

# ------------------------------------------------
# 4. enumerate() — get index AND value
# ------------------------------------------------
print("\n4. enumerate():")

prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
for number, prayer in enumerate(prayers, start=1):
    print(f"{number}. {prayer}")

# ------------------------------------------------
# 5. for with if — conditional logic inside loop
# ------------------------------------------------
print("\n5. for with if:")

marks_list = [85, 42, 90, 55, 38, 78, 61]
for marks in marks_list:
    if marks >= 50:
        print(f"{marks} — Pass")
    else:
        print(f"{marks} — Fail")

# ------------------------------------------------
# 6. break and continue in for loops
# ------------------------------------------------
print("\n6. break and continue:")

# Stop when we find the first failing mark
print("Search for first failure:")
for marks in [80, 75, 90, 43, 88]:
    if marks < 50:
        print(f"First failure found: {marks}")
        break
    print(f"{marks} — Pass")

# Skip absent students (marked as 0)
print("\nSkip absent students:")
scores = [85, 0, 72, 0, 91, 68]
for score in scores:
    if score == 0:
        continue    # skip absent
    print(f"Score: {score}")

# ------------------------------------------------
# 7. Nested for loops — loop inside a loop
# ------------------------------------------------
print("\n7. Nested loops:")

# Multiplication table for 2 and 3
for table in [2, 3]:
    print(f"\nTable of {table}:")
    for i in range(1, 6):
        print(f"  {table} x {i} = {table * i}")

# ------------------------------------------------
# 8. Calculating total and average with for
# ------------------------------------------------
print("\n8. Total and average:")

marks = [85, 92, 78, 90, 88]
subjects = ["Quran", "Hadith", "Fiqh", "Arabic", "Seerah"]
total = 0

for i in range(len(marks)):
    print(f"{subjects[i]}: {marks[i]}")
    total += marks[i]

average = total / len(marks)
print(f"\nTotal  : {total}")
print(f"Average: {average}")

print()
print("For loops are one of the most useful tools in Python. Excellent!")
