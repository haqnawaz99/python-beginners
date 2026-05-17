# ================================================
# Module 9 - Lesson 3: File I/O Applications
# ================================================
# Real programs that save and load data from files
# ================================================

print("=" * 50)
print("File I/O — Real Applications")
print("=" * 50)

import os

# ------------------------------------------------
# Application 1: Student Record System
# ------------------------------------------------
# Save student records to a file.
# Load and display them later.

STUDENTS_FILE = "student_records.txt"

def save_student(name, marks, city):
    with open(STUDENTS_FILE, "a") as f:
        f.write(f"{name},{marks},{city}\n")

def load_students():
    students = []
    if not os.path.exists(STUDENTS_FILE):
        return students
    with open(STUDENTS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                students.append({
                    "name": parts[0],
                    "marks": int(parts[1]),
                    "city": parts[2]
                })
    return students

def display_students(students):
    if not students:
        print("No records found.")
        return
    print(f"\n{'Name':<20} {'Marks':>6} {'City':<15} {'Result'}")
    print("-" * 55)
    for s in students:
        result = "Pass" if s["marks"] >= 50 else "Fail"
        print(f"{s['name']:<20} {s['marks']:>6} {s['city']:<15} {result}")

print("\n--- Application 1: Student Records ---")
print("1. Add student  2. View all  3. Skip")
choice = input("Choice: ").strip()

if choice == "1":
    name  = input("Name: ").strip().title()
    marks = int(input("Marks: "))
    city  = input("City: ").strip().title()
    save_student(name, marks, city)
    print("Student saved!")

students = load_students()
display_students(students)

# ------------------------------------------------
# Application 2: Daily Notes / Journal
# ------------------------------------------------
NOTES_FILE = "daily_notes.txt"

def add_note(note):
    with open(NOTES_FILE, "a") as f:
        f.write(note.strip() + "\n")

def read_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes yet.")
        return
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    print(f"\nAll notes ({len(lines)} total):")
    for i, line in enumerate(lines, 1):
        print(f"  {i}. {line.strip()}")

print("\n--- Application 2: Daily Notes ---")
note = input("Add a note (or press Enter to skip): ").strip()
if note:
    add_note(note)
    print("Note saved!")
read_notes()

# ------------------------------------------------
# Application 3: Simple Marks Log
# ------------------------------------------------
MARKS_FILE = "marks_log.txt"

def log_marks(subject, marks):
    with open(MARKS_FILE, "a") as f:
        f.write(f"{subject},{marks}\n")

def show_marks_summary():
    if not os.path.exists(MARKS_FILE):
        print("No marks recorded yet.")
        return
    subjects = []
    marks_list = []
    with open(MARKS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if "," in line:
                subject, marks = line.split(",")
                subjects.append(subject)
                marks_list.append(int(marks))

    print(f"\nMarks Summary ({len(marks_list)} entries):")
    for s, m in zip(subjects, marks_list):
        print(f"  {s:<15}: {m}")
    if marks_list:
        print(f"Average: {sum(marks_list) / len(marks_list):.1f}")

print("\n--- Application 3: Marks Log ---")
add_more = input("Add marks? (yes/no): ").strip().lower()
if add_more == "yes":
    subject = input("Subject: ")
    marks = int(input("Marks: "))
    log_marks(subject, marks)
    print("Marks logged!")

show_marks_summary()

print()
print("File I/O makes your programs remember data between runs!")
