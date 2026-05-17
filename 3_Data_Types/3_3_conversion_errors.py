# ================================================
# Module 3 - Lesson 3: Conversion Errors
# ================================================
# Learn: What goes wrong with int() and float(),
#        how to read the error, how to fix it
# ================================================

# ------------------------------------------------
# Error 1: Converting text to int — ValueError
# ------------------------------------------------
# int() only works on strings that look like whole numbers.
# If the string has letters or symbols, it fails.

# WRONG:
# number = int("abc")       # ValueError
# number = int("12 years")  # ValueError
# number = int("12.5")      # ValueError — use float() first!

# CORRECT:
number = int("123")
print("Correct:", number)

print()

# ------------------------------------------------
# Error 2: Mixing int and str — TypeError
# ------------------------------------------------
# You cannot use + to join a string and a number.

# WRONG:
# age = 20
# print("You are " + age + " years old.")   # TypeError

# CORRECT option 1 — use str():
age = 20
print("You are " + str(age) + " years old.")

# CORRECT option 2 — use comma in print():
print("You are", age, "years old.")

print()

# ------------------------------------------------
# Error 3: Converting "12.5" to int directly — ValueError
# ------------------------------------------------
# "12.5" is a float string. int() cannot handle it.
# Solution: convert to float first, then to int.

# WRONG:
# x = int("45.6")           # ValueError

# CORRECT — two steps:
float_val = float("45.6")
int_val = int(float_val)
print("Float string to int:", int_val)   # 45

print()

# ------------------------------------------------
# Error 4: Forgetting to convert input() — TypeError
# ------------------------------------------------
# This is the most common beginner mistake!

# WRONG:
# num = input("Enter a number: ")
# print(num + 5)             # TypeError — "5" + 5 fails

# CORRECT:
num = int(input("Enter a number: "))
print("Your number + 5 =", num + 5)

print()

# ------------------------------------------------
# Error 5: Empty string to int — ValueError
# ------------------------------------------------
# If user presses Enter without typing, input() gives "".
# int("") causes a ValueError.

# For now: just make sure students type a number.
# We will handle this safely in Module 8 (Error Handling).

# ------------------------------------------------
# Summary: Common Conversion Rules
# ------------------------------------------------
print("--- Conversion Rules ---")
print(int("25"))          # 25    works
print(float("25.5"))      # 25.5  works
print(str(100))           # 100   works
print(int(float("25.5"))) # 25    works (two steps)

print()
print("Remember: when in doubt, check the type with type()")
x = input("Type anything: ")
print("You typed:", x)
print("Its type is:", type(x))    # always str from input()
