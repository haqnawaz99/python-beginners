# ================================================
# Module 4 - Lesson 1: Mathematical Operators
# ================================================
# Learn: +  -  *  /  //  %  **
# ================================================

print("=" * 50)
print("Mathematical Operators")
print("=" * 50)

# ------------------------------------------------
# 1. Addition (+)
# ------------------------------------------------
print("\n1. Addition (+)")

tafsir_books = 40
hadith_books = 30
total_books = tafsir_books + hadith_books
print("Islamic books in library:", total_books)

fajr_students = 15
dhuhr_students = 22
print("Students in two sessions:", fajr_students + dhuhr_students)

# ------------------------------------------------
# 2. Subtraction (-)
# ------------------------------------------------
print("\n2. Subtraction (-)")

total_students = 35
absent = 3
present = total_students - absent
print("Present students:", present)

budget = 5000
spent = 1350
remaining = budget - spent
print("Remaining budget:", remaining, "rupees")

# ------------------------------------------------
# 3. Multiplication (*)
# ------------------------------------------------
print("\n3. Multiplication (*)")

price_per_kg = 170
kg = 5
total_cost = price_per_kg * kg
print("Cost of sugar:", total_cost, "rupees")

students = 12
ayat_each = 5
total_ayat = students * ayat_each
print("Total ayat memorized:", total_ayat)

# ------------------------------------------------
# 4. Division (/)
# ------------------------------------------------
# Always gives a float result (decimal number)
print("\n4. Division (/)")

zakat_money = 10000
people = 4
share = zakat_money / people
print("Each person's share:", share, "rupees")

pages = 600
days = 30
pages_per_day = pages / days
print("Pages to read per day:", pages_per_day)

# ------------------------------------------------
# 5. Floor Division (//)
# ------------------------------------------------
# Divides and removes the decimal — whole number only
print("\n5. Floor Division (//)")

qurans = 25
rows = 3
per_row = qurans // rows
print("Qurans per row:", per_row)     # 8 (not 8.33)

rupees = 1000
per_child = rupees // 7
print("Rupees per child:", per_child)

# ------------------------------------------------
# 6. Modulus (%) — Remainder
# ------------------------------------------------
print("\n6. Modulus (%) — Remainder")

leftover_qurans = 25 % 3
print("Leftover Qurans:", leftover_qurans)    # 1

leftover_rupees = 1000 % 7
print("Leftover rupees:", leftover_rupees)

# Check if a number is even or odd
students = 35
print("Is class size even?", students % 2 == 0)   # False

# ------------------------------------------------
# 7. Exponent (**) — Power
# ------------------------------------------------
print("\n7. Exponent (**)")

print("2 ** 3 =", 2 ** 3)    # 8
print("3 ** 2 =", 3 ** 2)    # 9
print("10 ** 2 =", 10 ** 2)  # 100

# ------------------------------------------------
# Using with input()
# ------------------------------------------------
print()
price = int(input("Enter price per item (rupees): "))
qty = int(input("Enter quantity: "))
print(f"Total cost: {price * qty} rupees")
print(f"Each item costs {price} rupees — {qty} items = {price * qty} rupees")

print()
print("All 7 mathematical operators covered. Well done!")
