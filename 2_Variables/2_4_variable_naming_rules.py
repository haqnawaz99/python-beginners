# ================================================
# Module 2 - Lesson 4: Variable Naming Rules & Errors
# ================================================
# Learn: Rules for naming variables, common mistakes
# ================================================

# ------------------------------------------------
# Rules for Naming Variables
# ------------------------------------------------
# 1. Use only letters, numbers, and underscores (_)
# 2. Must START with a letter or underscore (not a number)
# 3. No spaces allowed - use underscore instead
# 4. Cannot use Python reserved words (if, for, print, etc.)
# 5. Python is case-sensitive: name and Name are different

# ------------------------------------------------
# CORRECT Variable Names
# ------------------------------------------------

student_name = "Ahmed"
city1 = "Lahore"
_my_var = "test"
firstName = "Fatima"
SCHOOL = "Jamia Islamia"
total_students = "50"

print(student_name)
print(city1)
print(firstName)
print(SCHOOL)

# ------------------------------------------------
# WRONG Variable Names (these cause errors)
# ------------------------------------------------

# Spaces in name:
# student name = "Ahmed"       # SyntaxError

# Starts with a number:
# 1city = "Lahore"             # SyntaxError

# Special character:
# student-name = "Ahmed"       # SyntaxError (hyphen not allowed)
# student@name = "Ahmed"       # SyntaxError

# Python reserved word:
# print = "something"          # This breaks the print function!
# for = "loop"                 # SyntaxError

# ------------------------------------------------
# Python is Case-Sensitive
# ------------------------------------------------

name = "Ahmed"
Name = "Ali"
NAME = "Hassan"

print(name)     # Ahmed
print(Name)     # Ali
print(NAME)     # Hassan

# These are THREE different variables!

# ------------------------------------------------
# Good Naming Habits
# ------------------------------------------------

# Bad - unclear what it stores:
x = "Lahore"
y = "Ahmed"

# Good - name tells you what it stores:
student_city = "Lahore"
student_name = "Ahmed"

# Bad - too short:
sn = "Jamia"

# Good - clear and readable:
school_name = "Jamia Islamia"

# ------------------------------------------------
# Use underscore for multi-word names
# ------------------------------------------------
favorite_surah = "Al-Fatiha"
prayer_time = "Fajr"
total_students_in_class = "35"

print("Favorite Surah : " + favorite_surah)
print("Prayer time   : " + prayer_time)
print("Total students: " + total_students_in_class)

print()
print("Remember: good variable names make your code easy to read!")
