# ================================================
# Module 3 - Quiz: Data Types & Type Conversion
# ================================================
# Covers: int, float, str, bool, type(),
#         int(), float(), str(), f-strings
# Difficulty: Easy / Medium / Complex
# ================================================

print("=" * 50)
print("MODULE 3 QUIZ - Data Types & Type Conversion")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1. What is the data type of each value below?
#     Write a print(type(...)) for each one.
#     a) 42
#     b) 3.14
#     c) "Lahore"
#     d) True


# Q2. Create these three variables and print each with its type:
#     student_count = 40       (integer)
#     price = 99.5             (float)
#     city = "Karachi"         (string)


# Q3. Convert the string "786" to an integer and add 14 to it.
#     Print the result.
#     Expected output: 800


# Q4. Convert the integer 1947 to a string and join it with
#     "Pakistan was created in " using +
#     Expected output: Pakistan was created in 1947


# Q5. Rewrite this using an f-string:
#     name = "Fatima"
#     print("Welcome " + name + " to Python class!")


# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6. Ask the user for two numbers using int(input()).
#     Print their sum, difference, and product.


# Q7. Ask the user for their name and marks (as float).
#     Print this using an f-string:
#     "Ahmed scored 87.5 marks. Well done!"


# Q8. The code below has a TypeError. Identify why and fix it.
#     prayers = 5
#     print("We pray " + prayers + " times a day.")


# Q9. Ask the user for a price (float) and quantity (int).
#     Calculate total cost and print using an f-string.
#     Example: "3 items at 45.5 rupees each = 136.5 rupees total"


# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10. Ask the user for:
#      - Their name
#      - Their age (int)
#      - Their marks out of 100 (float)
#      Calculate what percentage they scored.
#      Print a full report using f-strings:
#        Name    : Ahmed
#        Age     : 15
#        Marks   : 87.5 / 100
#        Result  : 87.5%


# Q11. Ask the user for the number of students in a class
#      and the number of absent students.
#      Calculate:
#        - present students
#        - attendance percentage (present / total * 100)
#      Print all results using f-strings.


# Q12. Build a simple shop bill calculator.
#      Ask for:
#        - Item name (string)
#        - Price per kg (float)
#        - Quantity in kg (float)
#        - Discount in rupees (int)
#      Calculate: total = (price * quantity) - discount
#      Print a formatted receipt using f-strings:
#        ==============================
#        SHOP RECEIPT
#        ==============================
#        Item      : Rice
#        Price/kg  : 180.0 rupees
#        Quantity  : 5.0 kg
#        Subtotal  : 900.0 rupees
#        Discount  : 50 rupees
#        Total     : 850.0 rupees
#        ==============================
#        Jazakallah Khair!


print()
print("Quiz done! Check 3_6_quiz_solution.py for answers.")
