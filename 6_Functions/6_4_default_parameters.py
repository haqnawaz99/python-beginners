# ================================================
# Module 6 - Lesson 4: Default Parameters
# ================================================
# Learn: Setting default values for parameters
#        so the function works even without arguments
# ================================================

print("=" * 50)
print("Default Parameters")
print("=" * 50)

# ------------------------------------------------
# What are Default Parameters?
# ------------------------------------------------
# A default parameter has a pre-set value.
# If the caller does not pass a value, the default is used.
# If the caller does pass a value, it overrides the default.
# This makes functions more flexible.

# ------------------------------------------------
# 1. Simple default parameter
# ------------------------------------------------

def greet(name, greeting="Assalamu Alaikum"):
    print(f"{greeting}, {name}!")

greet("Ahmed")                          # uses default greeting
greet("Fatima")                         # uses default greeting
greet("Hassan", "Good morning")         # overrides with custom greeting

print()

# ------------------------------------------------
# 2. Default language/title
# ------------------------------------------------

def introduce(name, title="Student", city="Pakistan"):
    print(f"{title} {name} is from {city}.")

introduce("Ahmed")                          # all defaults
introduce("Maulana Tariq", "Scholar")       # override title only
introduce("Dr. Fatima", "Teacher", "Lahore") # override all

print()

# ------------------------------------------------
# 3. Default in calculation
# ------------------------------------------------

def calculate_zakat(savings, rate=2.5):
    zakat = savings * rate / 100
    return zakat

# Using default rate of 2.5%
zakat1 = calculate_zakat(100000)
print(f"Zakat on 100,000 (2.5%): {zakat1}")

# Overriding the rate
zakat2 = calculate_zakat(100000, 5)
print(f"Zakat on 100,000 (5%): {zakat2}")

print()

# ------------------------------------------------
# 4. Default in grading
# ------------------------------------------------

def check_result(marks, passing_marks=50):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"

print(check_result(75))           # uses default passing = 50
print(check_result(75, 80))       # harder requirement — Fail
print(check_result(40))           # Fail with default
print(check_result(40, 35))       # Pass with lower requirement

print()

# ------------------------------------------------
# 5. Default parameters with multiple arguments
# ------------------------------------------------

def student_report(name, marks, subject="General", passing=50):
    result = "Pass" if marks >= passing else "Fail"
    print(f"Subject : {subject}")
    print(f"Student : {name}")
    print(f"Marks   : {marks}")
    print(f"Result  : {result}")
    print()

student_report("Ahmed", 85, "Quran")
student_report("Fatima", 92, "Hadith", 80)
student_report("Hassan", 45)            # all defaults for subject and passing

# ------------------------------------------------
# 6. Important rule: defaults go AFTER non-defaults
# ------------------------------------------------

# WRONG — default parameter before non-default:
# def greet(greeting="Hello", name):   # SyntaxError!

# CORRECT — non-default first, default last:
def greet_properly(name, greeting="Assalamu Alaikum"):
    print(f"{greeting}, {name}!")

greet_properly("Ahmed")
greet_properly("Fatima", "Welcome back")

print()
print("Default parameters add flexibility to your functions. Excellent!")
