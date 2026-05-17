# ================================================
# Module 8 - Quiz: Error Handling
# ================================================
# Covers: error types, try/except, else, finally,
#         input validation functions
# Difficulty: Easy / Medium / Complex
# ================================================

print("=" * 50)
print("MODULE 8 QUIZ - Error Handling")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1. What type of error does each of these cause?
#     Write the error type as a comment next to each.
#     a) int("hello")
#     b) 10 / 0
#     c) ["Fajr", "Dhuhr"][5]
#     d) {"name": "Ahmed"}["marks"]


# Q2. Wrap this code in a try/except so it does not crash
#     when the user types text instead of a number:
#     number = int(input("Enter a number: "))
#     print(number * 2)


# Q3. Add an else block to Q2's try/except that prints
#     "Valid number entered!" only when no error occurs.


# Q4. Add a finally block to Q3 that always prints
#     "Program complete." whether or not an error occurred.


# Q5. Write a try/except that catches BOTH
#     ValueError AND ZeroDivisionError separately,
#     with a different message for each.
#     Code to wrap:
#       a = int(input("Enter number: "))
#       print(100 / a)


# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6. Write a function get_positive_int(prompt) that:
#     - Keeps asking until the user enters a valid positive integer
#     - Uses try/except for ValueError
#     - Checks the number is > 0
#     Test it by calling it once.


# Q7. Write a function safe_list_access(my_list, index) that:
#     - Tries to return my_list[index]
#     - Returns "Index out of range" if IndexError occurs
#     Test with prayers = ["Fajr","Dhuhr","Asr"] and index 10.


# Q8. Write a safe calculator function safe_calc(a, b, operation)
#     where operation is "+", "-", "*", or "/".
#     Handle ZeroDivisionError for division.
#     Return "Unknown operation" for anything else.
#     Test all four operations including dividing by zero.


# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q9. Build a validated student registration program using functions:
#     - get_integer_in_range(prompt, min, max) — validated int input
#     - get_non_empty(prompt) — validated string input
#     - register_student() — calls the above to collect:
#         name, age (5-25), marks (0-100), city
#       and prints a formatted registration card.


# Q10. Build a simple menu-driven program with error handling:
#      Menu options:
#        1. Calculate total (ask price and qty, multiply)
#        2. Check pass/fail (ask marks)
#        3. Exit
#      Validate all inputs. Loop until user chooses 3.


# Q11. Write a marks input system:
#      - Ask how many subjects (validated 1-10)
#      - For each subject ask name and marks (0-100, validated)
#      - Store in a dictionary
#      - Print each subject, marks, and pass/fail
#      - Print the class average
#      - Wrap the whole thing in a try/except as a safety net


print()
print("Quiz done! Check 8_5_quiz_solution.py for answers.")
