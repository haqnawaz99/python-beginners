# ================================================
# Module 3 - Lesson 2: Type Conversion
# ================================================
# Learn: int(), float(), str() — converting types
#        The critical skill: int(input())
# ================================================

# ------------------------------------------------
# Why do we need Type Conversion?
# ------------------------------------------------
# Python does NOT mix types automatically.
# You cannot add a number and a string directly.
# Type conversion lets you change one type to another.

# ------------------------------------------------
# str() — Convert number to string
# ------------------------------------------------
# Use when you want to join a number with text using +

age = 15
print("I am " + str(age) + " years old.")

ajza = 18
print("Hafiz Ahmed memorized " + str(ajza) + " ajza.")

year = 1947
print("Pakistan was created in " + str(year) + ".")

print()

# ------------------------------------------------
# int() — Convert string to integer
# ------------------------------------------------
# input() ALWAYS gives back a string.
# Even if the user types 25, Python sees "25" (text).
# Wrap with int() to turn it into a real number.

num_str = "25"
print("String + 5 =", num_str + "5")    # 255  (text joins!)
print("Integer + 5 =", int(num_str) + 5) # 30  (math works!)

print()

# ------------------------------------------------
# The most important skill: int(input())
# ------------------------------------------------

num = int(input("Enter a number: "))
print("Your number doubled:", num * 2)
print("Your number squared:", num ** 2)

print()

# ------------------------------------------------
# float() — Convert string to decimal number
# ------------------------------------------------

price_str = "135.50"
price = float(price_str)
print("Price with 10% tax:", price * 1.1)

print()

# float(input()) for decimal numbers
marks = float(input("Enter your marks (e.g. 87.5): "))
print("Your marks:", marks)
print("Out of 100, you scored:", marks, "%")

print()

# ------------------------------------------------
# Practical Pakistani examples
# ------------------------------------------------

price = int(input("Enter price per item (rupees): "))
quantity = int(input("How many items? "))
total = price * quantity
print("Total bill:", total, "rupees")

print()

students = int(input("Total students in class: "))
absent = int(input("How many absent today? "))
present = students - absent
print("Present:", present, "out of", students)

print()

# ------------------------------------------------
# float to int — decimal part is CUT (not rounded)
# ------------------------------------------------

marks = 89.9
print("As float:", marks)
print("As int:", int(marks))    # 89 — NOT 90, decimal is removed

print()
print("Type conversion is one of the most useful skills. Well done!")
