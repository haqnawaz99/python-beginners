# ================================================
# Module 7 - Lesson 1: Lists
# ================================================
# Learn: Creating lists, accessing items, modifying,
#        common list methods, looping over lists
# ================================================

print("=" * 50)
print("Lists — Storing Multiple Values")
print("=" * 50)

# ------------------------------------------------
# What is a List?
# ------------------------------------------------
# A list stores multiple values in one variable.
# Values are inside square brackets [ ] separated by commas.
# Each item has a position number called an index.
# Index starts at 0 (not 1).

# ------------------------------------------------
# 1. Creating a list
# ------------------------------------------------
print("\n1. Creating lists:")

prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
marks = [85, 92, 78, 90, 88]
cities = ["Lahore", "Karachi", "Islamabad", "Peshawar"]
mixed = ["Ahmed", 15, "Lahore", True]       # lists can mix types

print(prayers)
print(marks)
print(cities)

# ------------------------------------------------
# 2. Accessing items — index starts at 0
# ------------------------------------------------
print("\n2. Accessing items:")

print(prayers[0])       # Fajr  (first item)
print(prayers[1])       # Dhuhr (second item)
print(prayers[4])       # Isha  (fifth item)
print(prayers[-1])      # Isha  (last item — negative index)
print(prayers[-2])      # Maghrib (second from last)

# Length of a list
print("Number of prayers:", len(prayers))

# ------------------------------------------------
# 3. Slicing — getting a portion of a list
# ------------------------------------------------
print("\n3. Slicing:")

print(prayers[0:3])     # first 3 items: Fajr, Dhuhr, Asr
print(prayers[2:])      # from index 2 to end
print(marks[:3])        # first 3 marks

# ------------------------------------------------
# 4. Modifying items
# ------------------------------------------------
print("\n4. Modifying:")

subjects = ["Quran", "Hadith", "Fiqh"]
print("Before:", subjects)
subjects[1] = "Tafseer"             # change index 1
print("After:", subjects)

# ------------------------------------------------
# 5. Adding items
# ------------------------------------------------
print("\n5. Adding items:")

students = ["Ahmed", "Fatima"]
students.append("Hassan")           # add to end
print(students)

students.insert(1, "Zainab")        # insert at position 1
print(students)

# ------------------------------------------------
# 6. Removing items
# ------------------------------------------------
print("\n6. Removing items:")

fruits = ["mango", "apple", "banana", "guava"]
fruits.remove("apple")              # remove by value
print(fruits)

fruits.pop()                        # remove last item
print(fruits)

fruits.pop(0)                       # remove by index
print(fruits)

# ------------------------------------------------
# 7. Common list methods
# ------------------------------------------------
print("\n7. List methods:")

marks = [85, 42, 90, 55, 78]
print("Original :", marks)
print("Sorted   :", sorted(marks))          # sorted() returns new list
print("Max      :", max(marks))
print("Min      :", min(marks))
print("Sum      :", sum(marks))
print("Count    :", len(marks))
print("Average  :", sum(marks) / len(marks))

# Check if item exists
print("90 in marks:", 90 in marks)
print("100 in marks:", 100 in marks)

# ------------------------------------------------
# 8. Looping over a list
# ------------------------------------------------
print("\n8. Looping:")

for prayer in prayers:
    print(f"  - {prayer}")

print()
# Loop with index using enumerate
for i, prayer in enumerate(prayers, start=1):
    print(f"  {i}. {prayer}")

# ------------------------------------------------
# 9. Building a list from input
# ------------------------------------------------
print("\n9. Building from input:")

num = int(input("How many students? "))
student_names = []
for i in range(num):
    name = input(f"Student {i+1} name: ")
    student_names.append(name)

print("Class list:")
for i, name in enumerate(student_names, 1):
    print(f"  {i}. {name}")

print()
print("Lists are one of Python's most useful tools. Ma sha Allah!")
