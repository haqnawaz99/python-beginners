# ================================================
# Module 2 - Lesson 6: Variable Logic Puzzles
# ================================================
# Learn: Variable swapping, combining, reassigning
# Think carefully before running - predict the output!
# ================================================

print("=== VARIABLE LOGIC PUZZLES ===")
print("Try to predict the output BEFORE running each section.")
print()

# ------------------------------------------------
# Puzzle 1: What gets printed?
# ------------------------------------------------
print("--- Puzzle 1 ---")

city = "Lahore"
city = "Karachi"
city = "Islamabad"
print(city)

# What do you think prints? Why?

# ------------------------------------------------
# Puzzle 2: Swapping Two Variables
# ------------------------------------------------
print()
print("--- Puzzle 2: Swap ---")

# Problem: We have two variables. We want to swap their values.

first = "Fajr"
second = "Isha"

print("Before swap:")
print("first  =", first)
print("second =", second)

# Swap using a temporary variable
temp = first
first = second
second = temp

print("After swap:")
print("first  =", first)
print("second =", second)

# ------------------------------------------------
# Puzzle 3: Building a Full Name
# ------------------------------------------------
print()
print("--- Puzzle 3: Build Full Name ---")

title = "Maulana"
first_name = "Tariq"
last_name = "Jameel"

full_name = title + " " + first_name + " " + last_name
print(full_name)

# Now change first_name and rebuild
first_name = "Abdur Rahman"
full_name = title + " " + first_name + " " + last_name
print(full_name)

# ------------------------------------------------
# Puzzle 4: Chain Swap
# ------------------------------------------------
print()
print("--- Puzzle 4: Chain Swap ---")

a = "Quran"
b = "Hadith"
c = "Fiqh"

print("Before:", a, b, c)

# Shift: a gets b, b gets c, c gets a
temp = a
a = b
b = c
c = temp

print("After :", a, b, c)

# ------------------------------------------------
# Puzzle 5: Prediction Challenge
# ------------------------------------------------
print()
print("--- Puzzle 5: Predict the Output ---")

x = "Pakistan"
y = x
x = "India"

print(x)
print(y)

# Did y change when x changed? Why or why not?

# ------------------------------------------------
# Puzzle 6: String Repetition using *
# ------------------------------------------------
print()
print("--- Puzzle 6: Repetition ---")

line = "-" * 30
print(line)
print("  WELCOME TO PYTHON CLASS  ")
print(line)

word = "Al-"
print(word * 3 + "Hamdulillah")

print()
print("How many did you predict correctly? Keep practicing!")
