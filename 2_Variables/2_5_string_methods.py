# ================================================
# Module 2 - Lesson 5: String Methods
# ================================================
# Learn: .upper(), .lower(), .title(),
#        .strip(), .lstrip(), .rstrip()
# ================================================

# ------------------------------------------------
# What are String Methods?
# ------------------------------------------------
# Methods are built-in actions you can perform on a string.
# You call them by putting a dot (.) after the string or variable.
# They do NOT change the original variable - they return a new value.

# ------------------------------------------------
# .upper() - Convert to ALL CAPITALS
# ------------------------------------------------

name = "ahmed ali"
print(name.upper())          # AHMED ALI

school = "jamia islamia lahore"
print(school.upper())        # JAMIA ISLAMIA LAHORE

# Useful for: titles, headings, emphasis

# ------------------------------------------------
# .lower() - Convert to all lowercase
# ------------------------------------------------

name = "FATIMA KHAN"
print(name.lower())          # fatima khan

email = "Student@Madrasa.EDU"
print(email.lower())         # student@madrasa.edu

# Useful for: comparing inputs without case issues

# ------------------------------------------------
# .title() - Capitalize First Letter of Each Word
# ------------------------------------------------

name = "maulana abdur rahman"
print(name.title())          # Maulana Abdur Rahman

city = "lahore pakistan"
print(city.title())          # Lahore Pakistan

book = "sahih al-bukhari"
print(book.title())          # Sahih Al-Bukhari

# ------------------------------------------------
# Practical Example with input()
# ------------------------------------------------
# Students often type in different cases.
# .title() cleans up their input automatically.

raw_name = input("Enter your name (any format): ")
clean_name = raw_name.title()
print("Formatted name: " + clean_name)

# ------------------------------------------------
# .strip() - Remove Extra Spaces from Both Sides
# ------------------------------------------------
# Users sometimes type accidental spaces.
# .strip() removes spaces from the left and right.

messy = "   Ahmed   "
print(messy.strip())         # "Ahmed"

with_tabs = "\tLahore\t"
print(with_tabs.strip())     # "Lahore"

# ------------------------------------------------
# .lstrip() and .rstrip() - One Side Only
# ------------------------------------------------

left_spaces = "   Karachi"
print(left_spaces.lstrip())  # "Karachi"   (removed left spaces only)

right_spaces = "Peshawar   "
print(right_spaces.rstrip()) # "Peshawar"  (removed right spaces only)

# ------------------------------------------------
# Chaining Methods
# ------------------------------------------------
# You can use multiple methods together

raw_input = "   maulana tariq jameel   "
clean = raw_input.strip().title()
print(clean)                 # "Maulana Tariq Jameel"

# ------------------------------------------------
# Whitespace Characters: \t and \n
# ------------------------------------------------
# \t  = tab (large space)
# \n  = newline (go to next line)

print("Name:\tAhmed")             # tab between label and value
print("City:\tLahore")
print()
print("Line 1\nLine 2\nLine 3")   # three lines in one print

# Useful for formatting output neatly

print()
print("String methods make your data clean and consistent. Well done!")
