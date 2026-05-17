# ================================================
# Module 2 - Lesson 6: Variable Puzzles - SOLUTIONS
# ================================================

print("=== VARIABLE PUZZLES - SOLUTIONS ===")
print()

# ------------------------------------------------
# Puzzle 1 Solution
# ------------------------------------------------
print("--- Puzzle 1 ---")
city = "Lahore"
city = "Karachi"
city = "Islamabad"
print(city)
# Answer: Islamabad
# Reason: Each assignment overwrites the previous one.
#         Only the last value stays.
print()

# ------------------------------------------------
# Puzzle 2 Solution
# ------------------------------------------------
print("--- Puzzle 2: Swap ---")
first = "Fajr"
second = "Isha"
temp = first     # temp = "Fajr"
first = second   # first = "Isha"
second = temp    # second = "Fajr"
print("first  =", first)    # Isha
print("second =", second)   # Fajr
# Key: without temp, you would lose one value permanently.
print()

# ------------------------------------------------
# Puzzle 3 Solution
# ------------------------------------------------
print("--- Puzzle 3: Build Full Name ---")
title = "Maulana"
first_name = "Tariq"
last_name = "Jameel"
full_name = title + " " + first_name + " " + last_name
print(full_name)                  # Maulana Tariq Jameel

first_name = "Abdur Rahman"
full_name = title + " " + first_name + " " + last_name
print(full_name)                  # Maulana Abdur Rahman Jameel
print()

# ------------------------------------------------
# Puzzle 4 Solution
# ------------------------------------------------
print("--- Puzzle 4: Chain Swap ---")
a = "Quran"
b = "Hadith"
c = "Fiqh"
print("Before:", a, b, c)         # Quran Hadith Fiqh

temp = a    # save Quran
a = b       # a = Hadith
b = c       # b = Fiqh
c = temp    # c = Quran

print("After :", a, b, c)         # Hadith Fiqh Quran
print()

# ------------------------------------------------
# Puzzle 5 Solution
# ------------------------------------------------
print("--- Puzzle 5: Prediction ---")
x = "Pakistan"
y = x           # y now holds "Pakistan"
x = "India"     # x changes to "India", but y does NOT change

print(x)        # India
print(y)        # Pakistan
# Key: y = x copies the VALUE at that moment.
#      Changing x later does NOT affect y.
print()

# ------------------------------------------------
# Puzzle 6 Solution
# ------------------------------------------------
print("--- Puzzle 6: Repetition ---")
line = "-" * 30
print(line)
print("  WELCOME TO PYTHON CLASS  ")
print(line)

word = "Al-"
print(word * 3 + "Hamdulillah")   # Al-Al-Al-Hamdulillah
print()

print("End of solutions. How many did you get right?")
