# ================================================
# Module 10 - Capstone Project 1
# STUDENT REPORT CARD SYSTEM — STARTER FILE
# ================================================
# Give this file to students.
# Full solution: 10_1_report_card_system.py
# ================================================
# Skills: variables, lists, dictionaries,
#   functions, loops, if-else, f-strings,
#   file I/O, error handling, input validation
# ================================================

print("=" * 50)
print("   STUDENT REPORT CARD SYSTEM")
print("=" * 50)

import os

RECORDS_FILE = "report_cards.txt"
SUBJECTS = ["Quran", "Hadith", "Fiqh", "Arabic", "Seerah"]
PASSING_MARKS = 50

# ------------------------------------------------
# Helper Functions — already done for you
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

# ------------------------------------------------
# TODO 1: Write get_grade(marks) function
# Returns: "A+" if marks >= 90
#          "A"  if marks >= 80
#          "B"  if marks >= 70
#          "C"  if marks >= 60
#          "D"  if marks >= 50
#          "Fail" otherwise
# ------------------------------------------------

def get_grade(marks):
    pass  # replace with your code


# ------------------------------------------------
# TODO 2: Write calculate_average(marks_list)
# Returns the average of all numbers in the list
# Hint: use sum() and len()
# ------------------------------------------------

def calculate_average(marks_list):
    pass  # replace with your code


# ------------------------------------------------
# TODO 3: Complete add_student()
# Steps:
#   1. Get student name using get_non_empty()
#   2. Loop through SUBJECTS and get marks (0-100) for each
#   3. Calculate average using calculate_average()
#   4. Get grade using get_grade()
#   5. Save to RECORDS_FILE as: name|marks1,marks2,...|avg|grade
#   6. Print confirmation
# ------------------------------------------------

def add_student():
    print("\n--- Add New Student ---")
    pass  # replace with your code


# ------------------------------------------------
# TODO 4: Complete view_all_students()
# Steps:
#   1. Check if RECORDS_FILE exists (os.path.exists)
#   2. Read all lines from the file
#   3. Print a table with Name, Average, Grade, Pass/Fail
# ------------------------------------------------

def view_all_students():
    print("\n--- All Students ---")
    pass  # replace with your code


# ------------------------------------------------
# TODO 5: Complete view_student_detail()
# Steps:
#   1. Ask for student name (search)
#   2. Find the student in the file
#   3. Print each subject with marks, grade, pass/fail
#   4. Print average and overall result
# ------------------------------------------------

def view_student_detail():
    print("\n--- Student Detail ---")
    pass  # replace with your code


# ------------------------------------------------
# TODO 6: Complete show_class_summary()
# Steps:
#   1. Read all averages from the file
#   2. Print: total students, class average, highest, lowest, pass count
# ------------------------------------------------

def show_class_summary():
    print("\n--- Class Summary ---")
    pass  # replace with your code


# ------------------------------------------------
# Main Menu — already done for you
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
