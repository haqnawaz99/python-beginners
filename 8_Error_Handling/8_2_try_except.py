# ================================================
# Module 8 - Lesson 2: try / except
# ================================================
# Learn: try, except, else, finally
#        Catching and handling errors gracefully
# ================================================

print("=" * 50)
print("try / except — Catching Errors")
print("=" * 50)

# ------------------------------------------------
# The try / except structure
# ------------------------------------------------
# try:
#     code that might cause an error
# except:
#     code that runs IF an error occurs
#
# If no error: except block is skipped.
# If error occurs: Python jumps to except block.
# The program does NOT crash!

# ------------------------------------------------
# 1. Basic try / except
# ------------------------------------------------
print("\n1. Basic try/except:")

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
    print(f"Doubled: {number * 2}")
except:
    print("That was not a valid number. Please try again.")

print("Program continues after error handling.")

# ------------------------------------------------
# 2. Catching specific errors
# ------------------------------------------------
print("\n2. Catching specific errors:")

try:
    number = int(input("Enter a number to divide 100 by: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("Error: Please enter a whole number, not text.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# ------------------------------------------------
# 3. else — runs only when NO error occurred
# ------------------------------------------------
print("\n3. try / except / else:")

try:
    marks = int(input("Enter marks (0-100): "))
except ValueError:
    print("Invalid input — please enter a number.")
else:
    # This only runs if no error happened
    if marks >= 50:
        print(f"{marks} — Pass. Alhamdulillah!")
    else:
        print(f"{marks} — Fail. Work harder next time.")

# ------------------------------------------------
# 4. finally — ALWAYS runs, error or not
# ------------------------------------------------
print("\n4. try / except / finally:")

try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid age entered.")
finally:
    print("Thank you for using this program.")  # always runs

# ------------------------------------------------
# 5. Keeping asking until valid input
# ------------------------------------------------
print("\n5. Loop until valid input:")

while True:
    try:
        price = float(input("Enter price (rupees): "))
        if price < 0:
            print("Price cannot be negative. Try again.")
            continue
        break           # valid input — exit the loop
    except ValueError:
        print("Please enter a valid number.")

print(f"Price entered: {price} rupees")

# ------------------------------------------------
# 6. Practical example — safe calculator
# ------------------------------------------------
print("\n6. Safe calculator:")

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(100, 4))      # 25.0
print(safe_divide(100, 0))      # Cannot divide by zero

# ------------------------------------------------
# 7. Handling missing dictionary keys
# ------------------------------------------------
print("\n7. Safe dictionary access:")

students = {"Ahmed": 85, "Fatima": 92}

name = input("Enter student name to look up: ")
try:
    marks = students[name]
    print(f"{name}'s marks: {marks}")
except KeyError:
    print(f"'{name}' not found in records.")

print()
print("try/except makes your programs professional and user-friendly!")
