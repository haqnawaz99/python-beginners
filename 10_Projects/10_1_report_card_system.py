# ================================================
# Module 10 - Capstone Project 1
# STUDENT REPORT CARD SYSTEM
# ================================================
# Skills used: variables, data types, lists,
#   dictionaries, functions, loops, if-else,
#   f-strings, file I/O, error handling
# ================================================

print("=" * 50)
print("   STUDENT REPORT CARD SYSTEM")
print("=" * 50)

import os

RECORDS_FILE = "report_cards.txt"
SUBJECTS = ["Quran", "Hadith", "Fiqh", "Arabic", "Seerah"]
PASSING_MARKS = 50

# ------------------------------------------------
# Helper Functions
# ------------------------------------------------

def get_integer_in_range(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"  Enter a number between {minimum} and {maximum}.")
        except ValueError:
            print("  Invalid! Enter a whole number.")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip().title()
        if value:
            return value
        print("  Cannot be empty.")

def get_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 50: return "D"
    else: return "Fail"

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

# ------------------------------------------------
# Core Features
# ------------------------------------------------

def add_student():
    print("\n--- Add New Student ---")
    name = get_non_empty("Student name: ")
    marks_list = []
    for subject in SUBJECTS:
        m = get_integer_in_range(f"  {subject} (0-100): ", 0, 100)
        marks_list.append(m)

    avg = calculate_average(marks_list)
    grade = get_grade(avg)

    # Save to file
    with open(RECORDS_FILE, "a") as f:
        marks_str = ",".join(str(m) for m in marks_list)
        f.write(f"{name}|{marks_str}|{avg:.1f}|{grade}\n")

    print(f"\n  {name} saved. Average: {avg:.1f}  Grade: {grade}")

def view_all_students():
    print("\n--- All Students ---")
    if not os.path.exists(RECORDS_FILE):
        print("No records yet.")
        return

    with open(RECORDS_FILE, "r") as f:
        lines = [l.strip() for l in f if l.strip()]

    if not lines:
        print("No records yet.")
        return

    print(f"\n{'Name':<20} {'Avg':>6} {'Grade':<6} {'Result'}")
    print("-" * 45)
    for line in lines:
        parts = line.split("|")
        name, avg, grade = parts[0], parts[2], parts[3]
        result = "Pass" if float(avg) >= PASSING_MARKS else "Fail"
        print(f"{name:<20} {avg:>6} {grade:<6} {result}")

    print(f"\nTotal students: {len(lines)}")

def view_student_detail():
    print("\n--- Student Detail ---")
    search = get_non_empty("Enter student name: ")

    if not os.path.exists(RECORDS_FILE):
        print("No records found.")
        return

    found = False
    with open(RECORDS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if parts[0].lower() == search.lower():
                found = True
                name = parts[0]
                marks_list = [int(m) for m in parts[1].split(",")]
                avg = float(parts[2])
                grade = parts[3]

                print("\n" + "=" * 40)
                print(f"  REPORT CARD: {name}")
                print("=" * 40)
                for i, subject in enumerate(SUBJECTS):
                    g = get_grade(marks_list[i])
                    result = "Pass" if marks_list[i] >= PASSING_MARKS else "Fail"
                    print(f"  {subject:<12}: {marks_list[i]:>3}  {g}  {result}")
                print("-" * 40)
                print(f"  {'Average':<12}: {avg:.1f}")
                print(f"  {'Grade':<12}: {grade}")
                print(f"  {'Result':<12}: {'Pass' if avg >= PASSING_MARKS else 'FAIL'}")
                print("=" * 40)
                break

    if not found:
        print(f"'{search}' not found in records.")

def show_class_summary():
    print("\n--- Class Summary ---")
    if not os.path.exists(RECORDS_FILE):
        print("No records yet.")
        return

    averages = []
    with open(RECORDS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) >= 3:
                averages.append(float(parts[2]))

    if not averages:
        print("No data.")
        return

    passed = sum(1 for a in averages if a >= PASSING_MARKS)
    print(f"Total students : {len(averages)}")
    print(f"Class average  : {sum(averages)/len(averages):.1f}")
    print(f"Highest average: {max(averages):.1f}")
    print(f"Lowest average : {min(averages):.1f}")
    print(f"Passed         : {passed}/{len(averages)}")

# ------------------------------------------------
# Main Menu
# ------------------------------------------------

def show_menu():
    print("\n" + "=" * 30)
    print("  REPORT CARD SYSTEM MENU")
    print("=" * 30)
    print("  1. Add student")
    print("  2. View all students")
    print("  3. View student detail")
    print("  4. Class summary")
    print("  5. Exit")
    print("=" * 30)

while True:
    show_menu()
    choice = get_integer_in_range("Choice (1-5): ", 1, 5)
    if choice == 1:
        add_student()
    elif choice == 2:
        view_all_students()
    elif choice == 3:
        view_student_detail()
    elif choice == 4:
        show_class_summary()
    elif choice == 5:
        print("\nAssalamu Alaikum! Goodbye.")
        break
