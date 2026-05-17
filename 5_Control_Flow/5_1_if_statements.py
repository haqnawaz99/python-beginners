# ================================================
# Module 5 - Lesson 1: If Statements
# ================================================
# Learn: if, if-else, elif
#        Making decisions in code
# ================================================

print("=" * 50)
print("If Statements — Making Decisions")
print("=" * 50)

# ------------------------------------------------
# What is an if statement?
# ------------------------------------------------
# An if statement runs code ONLY when a condition is True.
# If the condition is False, Python skips that block.
# Indentation (4 spaces) marks which code belongs to the if.

# ------------------------------------------------
# 1. Basic if
# ------------------------------------------------
print("\n1. Basic if:")

marks = 75
if marks >= 50:
    print("Congratulations! You passed.")

age = 8
if age >= 7:
    print("Old enough to start Quran classes.")

is_fasting = True
if is_fasting:
    print("May Allah accept your fast.")

# ------------------------------------------------
# 2. if-else — two paths
# ------------------------------------------------
print("\n2. if-else:")

marks = 45
if marks >= 50:
    print("Result: Pass")
else:
    print("Result: Fail — keep trying!")

prayer_offered = False
if prayer_offered:
    print("JazakAllah Khair for praying.")
else:
    print("Do not forget your prayer!")

temperature = 42
if temperature > 40:
    print("Very hot today — drink water and stay inside.")
else:
    print("Weather is fine today.")

# ------------------------------------------------
# 3. elif — multiple choices
# ------------------------------------------------
print("\n3. elif — multiple choices:")

marks = 88
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print(f"Marks: {marks} — Grade: {grade}")

# Prayer time selector
hour = 6
if hour < 6:
    print("Time for Tahajjud")
elif hour < 8:
    print("Fajr prayer time")
elif hour < 13:
    print("Morning study time")
elif hour < 15:
    print("Dhuhr prayer time")
elif hour < 18:
    print("Asr prayer time")
elif hour < 20:
    print("Maghrib prayer time")
else:
    print("Isha prayer time")

# ------------------------------------------------
# 4. if with input()
# ------------------------------------------------
print("\n4. With user input:")

name = input("Enter your name: ")
marks = int(input(f"Enter {name}'s marks (out of 100): "))

if marks >= 90:
    print(f"Ma sha Allah {name}! Excellent result.")
elif marks >= 70:
    print(f"Well done {name}! Good result.")
elif marks >= 50:
    print(f"Passed {name}. Work harder next time.")
else:
    print(f"Failed {name}. Do not give up — try again!")

# ------------------------------------------------
# 5. Nested if — if inside if
# ------------------------------------------------
print("\n5. Nested if:")

age = int(input("Enter age: "))
has_permission = True

if age >= 10:
    if has_permission:
        print("Welcome to the advanced Quran class!")
    else:
        print("Age is fine but you need parent permission.")
else:
    print("Too young for this class. Join the beginner class.")

print()
print("If statements let your program think and decide. Excellent!")
