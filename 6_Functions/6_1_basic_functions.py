# ================================================
# Module 6 - Lesson 1: Basic Functions
# ================================================
# Learn: def, calling a function, why functions matter
# ================================================

print("=" * 50)
print("Functions — Reusable Blocks of Code")
print("=" * 50)

# ------------------------------------------------
# What is a Function?
# ------------------------------------------------
# A function is a block of code with a name.
# You define it once, then call it as many times as you want.
# Functions help avoid repeating the same code.
#
# Think of it like a recipe:
# You write the recipe once.
# You can cook that dish any number of times.

# ------------------------------------------------
# How to define a function
# ------------------------------------------------
# def function_name():
#     code goes here (indented)
#
# def  = keyword that starts a function
# ()   = brackets (empty for now — we add inputs later)
# :    = colon at the end of the def line
# code = indented 4 spaces inside the function

# ------------------------------------------------
# 1. Simple function with no parameters
# ------------------------------------------------

def say_salam():
    print("Assalamu Alaikum wa Rahmatullahi wa Barakatuh")

def say_bismillah():
    print("Bismillahir Rahmanir Raheem")

def show_daily_reminder():
    print("Remember: 5 prayers, recite Quran, do dhikr.")

# Calling (running) the functions:
say_salam()
say_bismillah()
show_daily_reminder()

# ------------------------------------------------
# 2. Calling a function multiple times
# ------------------------------------------------
print()

def print_separator():
    print("-" * 40)

print_separator()
print("Lesson: Introduction to Functions")
print_separator()
print("Teacher: Maulana Ahmed")
print_separator()

# ------------------------------------------------
# 3. Functions make code cleaner
# ------------------------------------------------
print()

# WITHOUT a function — repetitive code:
print("Assalamu Alaikum!")
print("Welcome to Python class.")
print("Today we learn functions.")
print()
print("Assalamu Alaikum!")
print("Welcome to Python class.")
print("Today we learn functions.")

print()

# WITH a function — clean and reusable:
def welcome_message():
    print("Assalamu Alaikum!")
    print("Welcome to Python class.")
    print("Today we learn functions.")

welcome_message()
print()
welcome_message()

# ------------------------------------------------
# 4. Function that does a calculation
# ------------------------------------------------
print()

def show_prayer_count():
    prayers_per_day = 5
    days_per_week = 7
    total = prayers_per_day * days_per_week
    print(f"In one week, a Muslim prays {total} times.")

def show_quran_facts():
    print(f"The Quran has 114 Surahs.")
    print(f"The Quran has 30 Paras.")
    print(f"The Quran has 6236 Ayaat.")

show_prayer_count()
print()
show_quran_facts()

# ------------------------------------------------
# 5. Order matters — define before calling
# ------------------------------------------------
print()

# WRONG: calling before defining causes NameError
# greet()              # NameError!
# def greet():
#     print("Hello")

# CORRECT: always define first, then call
def greet():
    print("Hello from the function!")

greet()

print()
print("Functions make your code organised and reusable. Ma sha Allah!")
