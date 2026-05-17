# ================================================
# Module 6 - Lesson 2: Function Parameters
# ================================================
# Learn: Passing data into functions using parameters
# ================================================

print("=" * 50)
print("Function Parameters — Passing Data In")
print("=" * 50)

# ------------------------------------------------
# What is a Parameter?
# ------------------------------------------------
# A parameter is a variable inside the function brackets.
# When you call the function you pass in a value (argument).
# The function uses that value in its code.
# This makes functions flexible — different input, different output.

# ------------------------------------------------
# 1. One parameter
# ------------------------------------------------

def greet_student(name):
    print(f"Assalamu Alaikum, {name}!")

greet_student("Ahmed")
greet_student("Fatima")
greet_student("Abdullah")

print()

def show_prayer(prayer_name):
    print(f"It is time for {prayer_name} prayer. Please stop and pray.")

show_prayer("Fajr")
show_prayer("Dhuhr")
show_prayer("Maghrib")

# ------------------------------------------------
# 2. Multiple parameters
# ------------------------------------------------
print()

def introduce_student(name, city, school):
    print(f"Name  : {name}")
    print(f"City  : {city}")
    print(f"School: {school}")
    print()

introduce_student("Ahmed Ali", "Lahore", "Jamia Islamia")
introduce_student("Fatima Khan", "Karachi", "Al-Huda Institute")

# ------------------------------------------------
# 3. Parameters with calculations
# ------------------------------------------------
print()

def calculate_bill(price, quantity):
    total = price * quantity
    print(f"Price : {price} rupees")
    print(f"Qty   : {quantity}")
    print(f"Total : {total} rupees")

calculate_bill(150, 5)
print()
calculate_bill(850, 3)

print()

def show_attendance(total, absent):
    present = total - absent
    percentage = present / total * 100
    print(f"Total    : {total}")
    print(f"Present  : {present}")
    print(f"Absent   : {absent}")
    print(f"Rate     : {percentage:.1f}%")

show_attendance(35, 3)

# ------------------------------------------------
# 4. Parameters with if statements inside
# ------------------------------------------------
print()

def check_grade(name, marks):
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "Pass"
    else:
        grade = "Fail"
    print(f"{name} scored {marks} — Grade: {grade}")

check_grade("Ahmed", 92)
check_grade("Fatima", 78)
check_grade("Hassan", 45)

# ------------------------------------------------
# 5. Using parameters with input()
# ------------------------------------------------
print()

def personal_greeting(name, subject):
    print(f"Bismillah {name}! Today we study {subject}.")
    print(f"May Allah make {subject} easy for you. Ameen.")

student = input("Enter student name: ")
topic = input("Enter today's subject: ")
personal_greeting(student, topic)

print()
print("Parameters make functions flexible and powerful. Excellent!")
