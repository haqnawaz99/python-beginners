# ================================================
# Module 9 - Lesson 2: Writing Files
# ================================================
# Learn: write(), append mode, saving program data,
#        writing lists and dictionaries to files
# ================================================

print("=" * 50)
print("File I/O — Writing Files")
print("=" * 50)

# ------------------------------------------------
# 1. Write mode "w" — creates or overwrites
# ------------------------------------------------
print("\n1. Write mode (w):")

with open("greetings.txt", "w") as f:
    f.write("Assalamu Alaikum\n")
    f.write("Welcome to Python\n")
    f.write("Bismillah\n")

print("greetings.txt created.")

# Read it back to verify
with open("greetings.txt", "r") as f:
    print(f.read())

# ------------------------------------------------
# 2. Append mode "a" — adds to existing file
# ------------------------------------------------
print("2. Append mode (a):")

with open("greetings.txt", "a") as f:
    f.write("JazakAllah Khair\n")
    f.write("Assalamu Alaikum wa Rahmatullahi\n")

print("Two lines added.")
with open("greetings.txt", "r") as f:
    print(f.read())

# ------------------------------------------------
# 3. Writing a list to a file
# ------------------------------------------------
print("3. Writing a list:")

prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

with open("prayers.txt", "w") as f:
    for prayer in prayers:
        f.write(prayer + "\n")

print("prayers.txt saved.")
with open("prayers.txt", "r") as f:
    print(f.read())

# ------------------------------------------------
# 4. Saving user input to a file
# ------------------------------------------------
print("4. Save student names to file:")

filename = "class_list.txt"
num = int(input("How many students? "))

with open(filename, "w") as f:
    for i in range(num):
        name = input(f"Student {i+1}: ")
        f.write(name.strip().title() + "\n")

print(f"\nSaved to {filename}:")
with open(filename, "r") as f:
    print(f.read())

# ------------------------------------------------
# 5. Saving marks — structured data
# ------------------------------------------------
print("5. Save marks report:")

subjects = ["Quran", "Hadith", "Fiqh"]
student_name = input("Student name: ")
marks_data = {}

for subject in subjects:
    m = int(input(f"{subject} marks: "))
    marks_data[subject] = m

total = sum(marks_data.values())
average = total / len(marks_data)

with open("report.txt", "w") as f:
    f.write("=" * 30 + "\n")
    f.write("STUDENT REPORT\n")
    f.write("=" * 30 + "\n")
    f.write(f"Name: {student_name}\n")
    f.write("-" * 30 + "\n")
    for subject, marks in marks_data.items():
        result = "Pass" if marks >= 50 else "Fail"
        f.write(f"{subject:<12}: {marks}  ({result})\n")
    f.write("-" * 30 + "\n")
    f.write(f"Total  : {total}\n")
    f.write(f"Average: {average:.1f}\n")
    f.write("=" * 30 + "\n")

print("\nReport saved to report.txt:")
with open("report.txt", "r") as f:
    print(f.read())

print()
print("Writing files lets you save your program's results forever!")
