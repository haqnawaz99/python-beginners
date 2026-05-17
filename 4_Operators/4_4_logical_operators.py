# ================================================
# Module 4 - Lesson 4: Logical Operators
# ================================================
# Learn: and, or, not
#        Combining multiple True/False conditions
# ================================================

print("=" * 50)
print("Logical Operators — and, or, not")
print("=" * 50)

# ------------------------------------------------
# What are Logical Operators?
# ------------------------------------------------
# Logical operators combine two or more conditions.
# The result is always True or False.
# They are the building blocks of complex decisions.

# ------------------------------------------------
# 1. AND — both conditions must be True
# ------------------------------------------------
# True  and True  -> True
# True  and False -> False
# False and True  -> False
# False and False -> False

print("\n1. AND — both must be True:")

has_attended = True
has_done_homework = True
print("Attended AND homework done:", has_attended and has_done_homework)  # True

has_attended = True
has_done_homework = False
print("Attended AND homework done:", has_attended and has_done_homework)  # False

# Real example: student gets certificate only if attended AND passed
attended = True
passed = True
gets_certificate = attended and passed
print("Gets certificate:", gets_certificate)

# ------------------------------------------------
# 2. OR — at least one condition must be True
# ------------------------------------------------
# True  or True  -> True
# True  or False -> True
# False or True  -> True
# False or False -> False

print("\n2. OR — at least one must be True:")

is_reading_quran = True
is_listening_lecture = False
print("Reading OR listening:", is_reading_quran or is_listening_lecture)  # True

is_reading_quran = False
is_listening_lecture = False
print("Reading OR listening:", is_reading_quran or is_listening_lecture)  # False

# Real example: student gets extra time if sick OR has valid excuse
is_sick = False
has_valid_excuse = True
gets_extra_time = is_sick or has_valid_excuse
print("Gets extra time:", gets_extra_time)

# ------------------------------------------------
# 3. NOT — reverses the condition
# ------------------------------------------------
# not True  -> False
# not False -> True

print("\n3. NOT — reverses True/False:")

is_fasting = False
print("not is_fasting:", not is_fasting)    # True

is_weekend = True
print("not is_weekend:", not is_weekend)    # False

is_absent = False
print("Is present:", not is_absent)         # True (not absent = present)

# ------------------------------------------------
# 4. Combining operators
# ------------------------------------------------
print("\n4. Combined Logic:")

age = 15
has_basic_knowledge = True
is_weekend = False

eligible = age >= 12 and has_basic_knowledge and not is_weekend
print("Eligible for advanced class:", eligible)

# Madrasa admission: age between 8 and 16, AND has memorized at least 5 surahs
student_age = 12
surahs_memorized = 8
can_join = (student_age >= 8 and student_age <= 16) and surahs_memorized >= 5
print("Can join Hifz program:", can_join)

# ------------------------------------------------
# Using with input()
# ------------------------------------------------
print()
age = int(input("Student age: "))
marks = int(input("Student marks (out of 100): "))

passed = marks >= 50
correct_age = age >= 10 and age <= 16
promoted = passed and correct_age

print(f"\nAge in range (10-16)  : {correct_age}")
print(f"Passed exam (50+)     : {passed}")
print(f"Eligible for promotion: {promoted}")

print()
print("Logical operators let you make complex decisions. Excellent!")
