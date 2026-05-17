# ================================================
# Module 8 - Lesson 3: Input Validation
# ================================================
# Learn: Validating user input, reusable validation
#        functions, building robust programs
# ================================================

print("=" * 50)
print("Input Validation — Trusted User Input")
print("=" * 50)

# ------------------------------------------------
# What is Input Validation?
# ------------------------------------------------
# Input validation means checking that user input
# is correct BEFORE using it in the program.
# Never trust user input — always validate it!
# This prevents crashes and incorrect results.

# ------------------------------------------------
# 1. Reusable: get a valid integer
# ------------------------------------------------

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Invalid! Please enter a whole number.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid! Please enter a number.")

def get_integer_in_range(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            else:
                print(f"  Must be between {minimum} and {maximum}.")
        except ValueError:
            print("  Invalid! Please enter a whole number.")

# ------------------------------------------------
# 2. Using validation functions
# ------------------------------------------------
print("\n1. Safe integer input:")
age = get_integer("Enter your age: ")
print(f"Age: {age}")

print("\n2. Integer in range:")
marks = get_integer_in_range("Enter marks (0-100): ", 0, 100)
print(f"Marks: {marks}")

print("\n3. Safe float input:")
price = get_float("Enter price (rupees): ")
print(f"Price: {price}")

# ------------------------------------------------
# 3. Validating string input
# ------------------------------------------------
print("\n4. String validation:")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Cannot be empty. Please try again.")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "no", "y", "n"):
            return answer in ("yes", "y")
        print("  Please enter yes or no.")

name = get_non_empty("Enter your name: ")
print(f"Name: {name}")

is_present = get_yes_no("Are you present today? (yes/no): ")
print(f"Present: {is_present}")

# ------------------------------------------------
# 4. Building a validated form
# ------------------------------------------------
print("\n5. Student registration form:")

print("\nPlease fill in your details:")
student_name = get_non_empty("Full name: ")
student_age  = get_integer_in_range("Age (5-25): ", 5, 25)
student_marks = get_integer_in_range("Marks (0-100): ", 0, 100)
student_city = get_non_empty("City: ")

print("\n=== Registration Confirmed ===")
print(f"Name  : {student_name.title()}")
print(f"Age   : {student_age}")
print(f"Marks : {student_marks}")
print(f"City  : {student_city.title()}")
print(f"Result: {'Pass' if student_marks >= 50 else 'Fail'}")
print("==============================")

# ------------------------------------------------
# 5. Validating a menu choice
# ------------------------------------------------
print("\n6. Menu with validation:")

def show_menu():
    print("\nSelect an option:")
    print("  1. View prayers")
    print("  2. Check marks")
    print("  3. Exit")

def get_menu_choice():
    return get_integer_in_range("Enter choice (1-3): ", 1, 3)

prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

while True:
    show_menu()
    choice = get_menu_choice()

    if choice == 1:
        for i, p in enumerate(prayers, 1):
            print(f"  {i}. {p}")
    elif choice == 2:
        m = get_integer_in_range("Enter marks: ", 0, 100)
        print(f"Result: {'Pass' if m >= 50 else 'Fail'}")
    elif choice == 3:
        print("Assalamu Alaikum! Goodbye.")
        break

print()
print("Validated input makes programs safe and professional!")
