# ================================================
# Module 7 - Lesson 3: Dictionaries
# ================================================
# Learn: Creating dictionaries, accessing/modifying values,
#        looping, common methods
# ================================================

print("=" * 50)
print("Dictionaries — Key-Value Pairs")
print("=" * 50)

# ------------------------------------------------
# What is a Dictionary?
# ------------------------------------------------
# A dictionary stores data as key: value pairs.
# Think of it like a real dictionary:
#   word (key) → definition (value)
# Or a student record:
#   "name" → "Ahmed", "marks" → 85
#
# Keys must be unique. Values can be anything.
# Use { } curly brackets.

# ------------------------------------------------
# 1. Creating a dictionary
# ------------------------------------------------
print("\n1. Creating dictionaries:")

student = {
    "name": "Ahmed Ali",
    "age": 15,
    "city": "Lahore",
    "marks": 87
}

prayer_times = {
    "Fajr": "5:00 AM",
    "Dhuhr": "1:00 PM",
    "Asr": "4:30 PM",
    "Maghrib": "7:00 PM",
    "Isha": "9:00 PM"
}

print(student)
print(prayer_times)

# ------------------------------------------------
# 2. Accessing values
# ------------------------------------------------
print("\n2. Accessing values:")

print(student["name"])          # Ahmed Ali
print(student["marks"])         # 87
print(prayer_times["Fajr"])     # 5:00 AM

# .get() is safer — returns None if key not found
print(student.get("city"))      # Lahore
print(student.get("grade"))     # None — no error

# ------------------------------------------------
# 3. Modifying values
# ------------------------------------------------
print("\n3. Modifying:")

student["marks"] = 92           # update existing key
student["grade"] = "A"          # add new key
print(student)

# Remove a key
del student["age"]
print(student)

# ------------------------------------------------
# 4. Checking if a key exists
# ------------------------------------------------
print("\n4. Checking keys:")

print("name" in student)        # True
print("phone" in student)       # False

if "city" in student:
    print(f"City is: {student['city']}")

# ------------------------------------------------
# 5. Looping over a dictionary
# ------------------------------------------------
print("\n5. Looping:")

# Loop over keys only
print("Keys:")
for key in prayer_times:
    print(f"  {key}")

# Loop over values only
print("Times:")
for time in prayer_times.values():
    print(f"  {time}")

# Loop over both key and value
print("Prayer schedule:")
for prayer, time in prayer_times.items():
    print(f"  {prayer:<10}: {time}")

# ------------------------------------------------
# 6. Dictionary with list values
# ------------------------------------------------
print("\n6. Dictionary with lists:")

class_marks = {
    "Ahmed":  [85, 90, 78],
    "Fatima": [92, 88, 95],
    "Hassan": [70, 65, 80]
}

for name, marks in class_marks.items():
    avg = sum(marks) / len(marks)
    print(f"{name:<10}: {marks}  avg = {avg:.1f}")

# ------------------------------------------------
# 7. Building a dictionary from input
# ------------------------------------------------
print("\n7. Building from input:")

num = int(input("How many students to register? "))
registry = {}

for i in range(num):
    name = input(f"Student {i+1} name: ")
    marks = int(input(f"Marks for {name}: "))
    registry[name] = marks

print("\nClass registry:")
for name, marks in registry.items():
    result = "Pass" if marks >= 50 else "Fail"
    print(f"  {name:<15}: {marks}  ({result})")

# ------------------------------------------------
# 8. Nested dictionary — dictionary inside dictionary
# ------------------------------------------------
print("\n8. Nested dictionary:")

madrasa = {
    "Jamia Islamia": {
        "city": "Lahore",
        "students": 450,
        "founded": 1965
    },
    "Darul Uloom": {
        "city": "Karachi",
        "students": 800,
        "founded": 1947
    }
}

for name, info in madrasa.items():
    print(f"{name}: {info['city']}, {info['students']} students")

print()
print("Dictionaries are perfect for structured data. Excellent!")
