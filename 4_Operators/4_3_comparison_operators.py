# ================================================
# Module 4 - Lesson 3: Comparison Operators
# ================================================
# Learn: ==  !=  >  <  >=  <=
#        These always return True or False
# ================================================

print("=" * 50)
print("Comparison Operators")
print("=" * 50)

# ------------------------------------------------
# What are Comparison Operators?
# ------------------------------------------------
# Comparison operators compare two values.
# The result is ALWAYS a Boolean: True or False.
# These are the foundation of decision-making in Python.

# ------------------------------------------------
# 1. Equal to (==)
# ------------------------------------------------
# Checks if two values are exactly the same.
# Note: = assigns a value,  == checks equality
print("\n1. Equal to (==):")
print("'Fajr' == 'Fajr'     ->", "Fajr" == "Fajr")        # True
print("'Maghrib' == 'Isha'  ->", "Maghrib" == "Isha")      # False
print("5 == 5               ->", 5 == 5)                    # True
print("5 == 6               ->", 5 == 6)                    # False

# ------------------------------------------------
# 2. Not equal to (!=)
# ------------------------------------------------
print("\n2. Not equal to (!=):")
print("'Ramadan' != 'Shawwal' ->", "Ramadan" != "Shawwal") # True
print("'Friday' != 'Friday'   ->", "Friday" != "Friday")   # False
print("10 != 5                ->", 10 != 5)                 # True

# ------------------------------------------------
# 3. Greater than (>)
# ------------------------------------------------
print("\n3. Greater than (>):")
print("4 > 2  ->", 4 > 2)       # True
print("8 > 10 ->", 8 > 10)      # False

study_hours = 4
print("Study hours > 2:", study_hours > 2)

# ------------------------------------------------
# 4. Less than (<)
# ------------------------------------------------
print("\n4. Less than (<):")
print("5 < 10  ->", 5 < 10)     # True
print("65 < 50 ->", 65 < 50)    # False

marks = 65
passing = 50
print("Marks less than passing:", marks < passing)

# ------------------------------------------------
# 5. Greater than or equal to (>=)
# ------------------------------------------------
print("\n5. Greater than or equal to (>=):")
score = 70
passing_score = 70
print("Score >= passing score:", score >= passing_score)    # True

age = 9
print("Age >= 10:", age >= 10)                              # False

# ------------------------------------------------
# 6. Less than or equal to (<=)
# ------------------------------------------------
print("\n6. Less than or equal to (<=):")
quran_level = 3
print("Level <= 5:", quran_level <= 5)     # True
print("12 <= 6:", 12 <= 6)                 # False

# ------------------------------------------------
# Using with variables from input()
# ------------------------------------------------
print()
student_marks = int(input("Enter student marks (out of 100): "))
passing_marks = 50

print(f"Marks entered      : {student_marks}")
print(f"Did student pass?  : {student_marks >= passing_marks}")
print(f"Did student fail?  : {student_marks < passing_marks}")
print(f"Full marks?        : {student_marks == 100}")

print()
print("Comparison operators always give True or False. Great work!")
