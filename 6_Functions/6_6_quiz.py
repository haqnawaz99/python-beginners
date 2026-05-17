# ================================================
# Module 6 - Quiz: Functions
# ================================================
# Covers: def, parameters, return, default params,
#         functions calling functions
# Difficulty: Easy / Medium / Complex
# ================================================

print("=" * 50)
print("MODULE 6 QUIZ - Functions")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1. Define a function called say_bismillah() that
#     prints "Bismillahir Rahmanir Raheem".
#     Call it 3 times.


# Q2. Define a function called greet(name) that
#     prints "Assalamu Alaikum, <name>!"
#     Call it with 3 different names.


# Q3. Define a function called double(number) that
#     returns the number multiplied by 2.
#     Call it with 5 and print the result.


# Q4. Define a function called is_even(number) that
#     returns True if the number is even, False otherwise.
#     Test it with 4 and 7.


# Q5. Define a function greet(name, greeting="Salam")
#     with a default greeting.
#     Call it once with only a name, once with both arguments.


# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6. Define a function calculate_total(price, quantity)
#     that returns price * quantity.
#     Ask the user for price and quantity using input(),
#     call the function, and print the result with an f-string.


# Q7. Define a function get_grade(marks) that returns:
#       A+ for 90+, A for 80+, B for 70+, Pass for 50+, Fail otherwise.
#     Ask the user for marks and print their grade.


# Q8. Define a function check_eligible(age, surahs_memorized)
#     that returns True if age >= 8 AND surahs_memorized >= 5.
#     Test it with two different inputs.


# Q9. Define two functions:
#     - get_full_name(first, last) — returns "First Last"
#     - print_id_card(first, last, city) — prints a formatted
#       ID card using get_full_name() inside it.
#     Call print_id_card with your own details.


# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10. Build a marks summary system using functions:
#      - get_average(marks_list) — returns the average
#      - get_grade(average) — returns A+/A/B/Pass/Fail
#      - print_summary(name, marks_list) — prints name,
#        each mark, average, and grade
#      Ask for a student name and 5 marks, then call print_summary.


# Q11. Define a function calculate_zakat(savings, rate=2.5)
#      that returns the zakat amount.
#      Define a second function print_zakat_report(name, savings)
#      that calls calculate_zakat() and prints a neat report.
#      Include: name, savings, zakat due, whether they owe zakat
#      (savings must be >= 50000 to owe zakat).


# Q12. Build a number guessing game using functions:
#      - check_guess(guess, secret) — returns "correct",
#        "too high", or "too low"
#      - play_game(secret, max_attempts) — runs the game loop,
#        gives the user max_attempts tries, prints result
#      Call play_game(7, 3) to run the game.


print()
print("Quiz done! Check 6_7_quiz_solution.py for answers.")
