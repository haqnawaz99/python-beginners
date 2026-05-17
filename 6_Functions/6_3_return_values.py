# ================================================
# Module 6 - Lesson 3: Return Values
# ================================================
# Learn: return, using the result of a function,
#        the difference between print and return
# ================================================

print("=" * 50)
print("Return Values — Getting Data Back from Functions")
print("=" * 50)

# ------------------------------------------------
# What is return?
# ------------------------------------------------
# So far our functions only PRINT things.
# return sends a value BACK to wherever the function was called.
# The calling code can store that value in a variable.
# This makes functions truly useful in larger programs.

# print vs return:
# print  — shows something on screen, returns nothing useful
# return — sends a value back, can be stored and used later

# ------------------------------------------------
# 1. Basic return
# ------------------------------------------------

def get_greeting(name):
    return "Assalamu Alaikum, " + name + "!"

message = get_greeting("Ahmed")
print(message)                          # store and use later
print(get_greeting("Fatima"))           # use directly

print()

# ------------------------------------------------
# 2. Returning a calculated number
# ------------------------------------------------

def calculate_total(price, quantity):
    return price * quantity

bill = calculate_total(150, 5)
print(f"Your bill is {bill} rupees")

# Using the returned value in another calculation
total = calculate_total(200, 3)
tax = total * 0.10
grand_total = total + tax
print(f"Subtotal : {total}")
print(f"Tax (10%): {tax}")
print(f"Total    : {grand_total}")

print()

# ------------------------------------------------
# 3. Return with if-else
# ------------------------------------------------

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"

marks = int(input("Enter marks: "))
grade = get_grade(marks)
print(f"Your grade is: {grade}")

print()

# ------------------------------------------------
# 4. Returning True or False
# ------------------------------------------------

def is_passing(marks):
    return marks >= 50

def is_adult(age):
    return age >= 18

def is_eligible_for_hifz(age, surahs):
    return age >= 8 and surahs >= 3

print(is_passing(75))               # True
print(is_passing(35))               # False

age = int(input("Enter age: "))
print(f"Is adult: {is_adult(age)}")

print()

# ------------------------------------------------
# 5. Using returned values together
# ------------------------------------------------

def calculate_average(marks_list):
    total = 0
    for m in marks_list:
        total += m
    return total / len(marks_list)

def get_result(average):
    if average >= 80:
        return "Excellent"
    elif average >= 60:
        return "Good"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

student_marks = [85, 78, 92, 70, 88]
avg = calculate_average(student_marks)
result = get_result(avg)
print(f"Average : {avg:.1f}")
print(f"Result  : {result}")

print()

# ------------------------------------------------
# 6. Functions calling other functions
# ------------------------------------------------

def get_full_name(first, last):
    return first + " " + last

def generate_id_card(first, last, city):
    name = get_full_name(first, last)       # calls another function
    print("=" * 30)
    print("STUDENT ID CARD")
    print("=" * 30)
    print(f"Name : {name}")
    print(f"City : {city}")
    print("=" * 30)

generate_id_card("Ahmed", "Ali", "Lahore")

print()
print("return makes functions truly powerful. Well done!")
