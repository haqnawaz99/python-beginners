# ================================================
# Module 4 - Lesson 2: Operator Precedence (BODMAS)
# ================================================
# Learn: Order Python follows when calculating
#        Brackets, Orders, Division/Multiplication,
#        Addition/Subtraction
# ================================================

print("=" * 50)
print("Operator Precedence — BODMAS")
print("=" * 50)

# ------------------------------------------------
# What is BODMAS?
# ------------------------------------------------
# When a calculation has multiple operators,
# Python follows a specific order — just like maths class.
#
# B — Brackets        ( )
# O — Orders          **  (powers)
# D — Division        /  //  %
# M — Multiplication  *
# A — Addition        +
# S — Subtraction     -
#
# Division and Multiplication have equal priority (left to right)
# Addition and Subtraction have equal priority (left to right)

# ------------------------------------------------
# 1. Without Brackets — Python decides the order
# ------------------------------------------------
print("\n1. Without Brackets:")
print("5 + 3 * 2  =", 5 + 3 * 2)      # 11 not 16 — * before +
print("10 - 4 * 2 =", 10 - 4 * 2)     # 2  not 12
print("6 + 8 / 4  =", 6 + 8 / 4)      # 8.0 not 3.5

# ------------------------------------------------
# 2. With Brackets — YOU control the order
# ------------------------------------------------
print("\n2. With Brackets:")
print("(5 + 3) * 2  =", (5 + 3) * 2)      # 16
print("(10 - 4) * 2 =", (10 - 4) * 2)     # 12
print("(6 + 8) / 4  =", (6 + 8) / 4)      # 3.5

# ------------------------------------------------
# 3. Powers before Multiplication
# ------------------------------------------------
print("\n3. Power before Multiplication:")
print("2 * 3 ** 2  =", 2 * 3 ** 2)    # 18 (3**2=9, then 2*9)
print("5 + 2 ** 3  =", 5 + 2 ** 3)    # 13 (2**3=8, then 5+8)
print("(2 + 1) ** 3 =", (2 + 1) ** 3) # 27 (bracket first: 3**3)

# ------------------------------------------------
# 4. Division and Multiplication — left to right
# ------------------------------------------------
print("\n4. Division and Multiplication (left to right):")
print("12 / 3 * 2 =", 12 / 3 * 2)    # 8.0 (12/3=4, then 4*2)
print("20 / 4 * 5 =", 20 / 4 * 5)    # 25.0

# ------------------------------------------------
# 5. Islamic / Pakistani context examples
# ------------------------------------------------
print("\n5. Real Examples:")

# Tasbeeh: 33 times per prayer × 5 prayers, done by 3 people
total_tasbeeh = 33 * 5 * 3
print(f"Total tasbeeh (3 people, 5 prayers): {total_tasbeeh}")

# 30 paras × 20 pages each, minus 10 pages already done
remaining_pages = (30 * 20) - 10
print(f"Remaining Quran pages to read: {remaining_pages}")

# Cricket: Pakistan scores in 3 innings, average per over
runs = (150 + 180 + 210) / 3
print(f"Average innings score: {runs}")

# Bill split: 3 items at 250 each, split among 5 friends
bill = (3 * 250) / 5
print(f"Each friend pays: {bill} rupees")

# ------------------------------------------------
# 6. Prediction Challenge
# ------------------------------------------------
print("\n6. Predict before running:")
print("10 + 5 * 3       =", 10 + 5 * 3)
print("(10 + 5) * 3     =", (10 + 5) * 3)
print("2 ** 3 + 4 * 2   =", 2 ** 3 + 4 * 2)
print("(2 ** 3 + 4) * 2 =", (2 ** 3 + 4) * 2)

print()
print("When in doubt — use brackets! They make your intention clear.")
