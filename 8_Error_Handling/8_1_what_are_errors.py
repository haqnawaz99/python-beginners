# ================================================
# Module 8 - Lesson 1: What Are Errors?
# ================================================
# Learn: Types of errors, how to read error messages,
#        the difference between syntax and runtime errors
# ================================================

print("=" * 50)
print("Error Handling — Dealing with Problems")
print("=" * 50)

# ------------------------------------------------
# Why learn Error Handling?
# ------------------------------------------------
# Programs crash when something unexpected happens.
# A user types "abc" when you expected a number.
# A file does not exist when you try to open it.
# Error handling lets your program respond gracefully
# instead of crashing with an ugly error message.

# ------------------------------------------------
# Type 1: SyntaxError — before the program runs
# ------------------------------------------------
# Python cannot even start because the code is written wrong.
# These must be FIXED before running.

# Examples (commented out to prevent crash):
# print("Hello"          # SyntaxError: missing )
# if x = 5:              # SyntaxError: use == not =
# def greet)             # SyntaxError: wrong brackets

print("SyntaxErrors must be fixed in the code — they stop Python from starting.")

# ------------------------------------------------
# Type 2: RuntimeError — while the program is running
# ------------------------------------------------
# The code looks fine but something goes wrong during execution.
# These CAN be caught and handled with try/except.

print("\nCommon Runtime Errors:")

# ValueError — wrong type of value
# int("abc")     # ValueError: invalid literal for int()

# TypeError — wrong type used in operation
# "Age: " + 25   # TypeError: can only concatenate str to str

# ZeroDivisionError — dividing by zero
# 10 / 0         # ZeroDivisionError: division by zero

# IndexError — accessing list index that does not exist
# prayers = ["Fajr", "Dhuhr"]
# print(prayers[5])    # IndexError: list index out of range

# KeyError — accessing dictionary key that does not exist
# student = {"name": "Ahmed"}
# print(student["marks"])    # KeyError: 'marks'

# NameError — using a variable that was never created
# print(undefined_var)   # NameError: name 'undefined_var' is not defined

print("ValueError      — wrong value (e.g. int('abc'))")
print("TypeError       — wrong type (e.g. 'text' + 5)")
print("ZeroDivisionError — dividing by zero")
print("IndexError      — list index out of range")
print("KeyError        — dictionary key not found")
print("NameError       — variable not defined")

# ------------------------------------------------
# How to read an error message
# ------------------------------------------------
print("\nHow to read an error:")
print("  File: which file caused it")
print("  Line: which line number")
print("  Type: what kind of error (ValueError, TypeError...)")
print("  Message: description of what went wrong")
print()
print("Example:")
print("  File '8_1_what_are_errors.py', line 45")
print("  ValueError: invalid literal for int() with base 10: 'abc'")
print()
print("This tells us: line 45, we tried int('abc') which is invalid.")

# ------------------------------------------------
# The most common beginner error
# ------------------------------------------------
print("\nMost common beginner error:")
print("Forgetting int(input()) when you need a number.")
print("input() ALWAYS gives a string — you must convert it!")

# WRONG:
# number = input("Enter a number: ")
# print(number * 2)    # "55" instead of 10 — string * 2 repeats!

# CORRECT:
number = int(input("Enter a number: "))
print("Doubled:", number * 2)

print()
print("Understanding errors is the first step to fixing them. Well done!")
