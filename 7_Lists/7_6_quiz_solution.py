# ================================================
# Module 7 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 7 QUIZ - SOLUTIONS")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1.
cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta"]
print(cities)
print("First:", cities[0])
print("Last :", cities[-1])

# Q2.
subjects = ["Quran", "Hadith", "Fiqh"]
subjects.append("Arabic")
subjects[1] = "Tafseer"
print(subjects)

# Q3.
prayers = ("Fajr", "Dhuhr", "Asr", "Maghrib", "Isha")
print("3rd prayer:", prayers[2])
print("Total     :", len(prayers))

# Q4.
student = {"name": "Ahmed", "city": "Lahore", "marks": 87}
print(student["name"])
print(student["city"])
print(student["marks"])

# Q5.
fruits = ["mango", "apple", "banana", "guava", "date"]
for fruit in fruits:
    print(fruit)

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
marks = [85, 42, 90, 55, 78]
print("Total  :", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest :", min(marks))

# Q7.
prayer_times = {"Fajr": "5:00 AM", "Dhuhr": "1:00 PM", "Asr": "4:30 PM"}
for prayer, time in prayer_times.items():
    print(f"{prayer}: {time}")

name = input("Enter prayer name: ")
if name in prayer_times:
    print(f"{name} time: {prayer_times[name]}")
else:
    print("Prayer not found.")

# Q8.
student_names = []
for i in range(4):
    name = input(f"Student {i+1}: ")
    student_names.append(name)
print("Sorted:", sorted(student_names))

# Q9.
a = "Lahore"
b = "Karachi"
a, b = b, a
print(f"a = {a}, b = {b}")

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10.
num = int(input("Number of students: "))
registry = {}
for i in range(num):
    name = input(f"Student {i+1} name: ")
    marks = int(input(f"Marks for {name}: "))
    registry[name] = marks

print("\nAll students:")
pass_count = 0
for name, marks in registry.items():
    result = "Pass" if marks >= 50 else "Fail"
    print(f"  {name}: {marks} ({result})")
    if marks >= 50:
        pass_count += 1

top_student = max(registry, key=registry.get)
print(f"Top student : {top_student} ({registry[top_student]})")
print(f"Passed      : {pass_count}/{num}")

# Q11.
subjects = ["Quran", "Hadith", "Fiqh"]
marks_by_subject = {}
for subject in subjects:
    marks = []
    for i in range(3):
        m = int(input(f"{subject} mark {i+1}: "))
        marks.append(m)
    marks_by_subject[subject] = marks

print("\nSubject averages:")
for subject, marks in marks_by_subject.items():
    avg = sum(marks) / len(marks)
    print(f"  {subject}: {avg:.1f}")

# Q12.
contact_book = {}
for i in range(3):
    name = input(f"Contact {i+1} name: ")
    phone = input(f"Phone for {name}: ")
    contact_book[name] = phone

search = input("Search for: ")
if search in contact_book:
    print(f"Phone: {contact_book[search]}")
else:
    print("Not found.")

print("\nAll contacts:")
for name, phone in contact_book.items():
    print(f"  {name}: {phone}")

print()
print("End of solutions.")
