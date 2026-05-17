# ================================================
# Module 8 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 8 QUIZ - SOLUTIONS")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1. Error types:
# a) int("hello")    -> ValueError
# b) 10 / 0          -> ZeroDivisionError
# c) list[5]         -> IndexError
# d) dict["marks"]   -> KeyError
print("Q1: ValueError, ZeroDivisionError, IndexError, KeyError")

# Q2.
try:
    number = int(input("Enter a number: "))
    print(number * 2)
except ValueError:
    print("Invalid! Please enter a number.")

# Q3.
try:
    number = int(input("Enter a number: "))
    print(number * 2)
except ValueError:
    print("Invalid! Please enter a number.")
else:
    print("Valid number entered!")

# Q4.
try:
    number = int(input("Enter a number: "))
    print(number * 2)
except ValueError:
    print("Invalid! Please enter a number.")
else:
    print("Valid number entered!")
finally:
    print("Program complete.")

# Q5.
try:
    a = int(input("Enter a number: "))
    print(100 / a)
except ValueError:
    print("Error: Please enter a whole number, not text.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("  Must be a positive number.")
        except ValueError:
            print("  Invalid! Enter a whole number.")

result = get_positive_int("Enter a positive number: ")
print(f"You entered: {result}")

# Q7.
def safe_list_access(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "Index out of range"

prayers = ["Fajr", "Dhuhr", "Asr"]
print(safe_list_access(prayers, 1))     # Dhuhr
print(safe_list_access(prayers, 10))    # Index out of range

# Q8.
def safe_calc(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return "Unknown operation"

print(safe_calc(10, 5, "+"))    # 15
print(safe_calc(10, 5, "-"))    # 5
print(safe_calc(10, 5, "*"))    # 50
print(safe_calc(10, 0, "/"))    # Cannot divide by zero
print(safe_calc(10, 5, "^"))    # Unknown operation

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q9.
def get_integer_in_range(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"  Must be between {minimum} and {maximum}.")
        except ValueError:
            print("  Invalid! Enter a whole number.")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Cannot be empty.")

def register_student():
    print("\nStudent Registration:")
    name  = get_non_empty("Full name: ")
    age   = get_integer_in_range("Age (5-25): ", 5, 25)
    marks = get_integer_in_range("Marks (0-100): ", 0, 100)
    city  = get_non_empty("City: ")
    print("\n=== Registration Card ===")
    print(f"Name  : {name.title()}")
    print(f"Age   : {age}")
    print(f"Marks : {marks}")
    print(f"City  : {city.title()}")
    print(f"Result: {'Pass' if marks >= 50 else 'Fail'}")
    print("=========================")

register_student()

# Q10.
def show_menu():
    print("\n1. Calculate total")
    print("2. Check pass/fail")
    print("3. Exit")

while True:
    show_menu()
    choice = get_integer_in_range("Choice (1-3): ", 1, 3)
    if choice == 1:
        price = get_integer_in_range("Price: ", 1, 100000)
        qty   = get_integer_in_range("Quantity: ", 1, 1000)
        print(f"Total: {price * qty} rupees")
    elif choice == 2:
        marks = get_integer_in_range("Marks (0-100): ", 0, 100)
        print("Pass" if marks >= 50 else "Fail")
    else:
        print("Goodbye!")
        break

# Q11.
try:
    num_subjects = get_integer_in_range("How many subjects (1-10)? ", 1, 10)
    subject_marks = {}
    for i in range(num_subjects):
        subject = get_non_empty(f"Subject {i+1} name: ")
        marks = get_integer_in_range(f"Marks for {subject} (0-100): ", 0, 100)
        subject_marks[subject] = marks

    print("\nResults:")
    total = 0
    for subject, marks in subject_marks.items():
        result = "Pass" if marks >= 50 else "Fail"
        print(f"  {subject:<15}: {marks}  ({result})")
        total += marks
    print(f"Average: {total / len(subject_marks):.1f}")
except Exception as e:
    print(f"Unexpected error: {e}")

print()
print("End of solutions.")
