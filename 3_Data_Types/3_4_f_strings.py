# ================================================
# Module 3 - Lesson 4: f-strings
# ================================================
# Learn: A cleaner way to combine variables with text
# ================================================

# ------------------------------------------------
# What is an f-string?
# ------------------------------------------------
# An f-string starts with f before the opening quote.
# You put variable names inside { } curly brackets.
# Python replaces {variable} with its actual value.
# Much cleaner than using + and str() everywhere!

# ------------------------------------------------
# Basic Comparison: + method vs f-string
# ------------------------------------------------

name = "Ahmed"
age = 15

# Old way using + (requires str() for numbers):
print("My name is " + name + " and I am " + str(age) + " years old.")

# New way using f-string (cleaner!):
print(f"My name is {name} and I am {age} years old.")

print()

# ------------------------------------------------
# f-string Examples — Islamic Context
# ------------------------------------------------

student = "Hafiz Usman"
ajza = 18
print(f"{student} has memorized {ajza} ajza of the Quran.")

surah = "Al-Fatiha"
verses = 7
print(f"Surah {surah} has {verses} verses.")

prayers = 5
print(f"A Muslim prays {prayers} times every day.")

print()

# ------------------------------------------------
# f-string Examples — Pakistani Context
# ------------------------------------------------

city = "Lahore"
population = 13_000_000
print(f"{city} has a population of about {population}.")

item = "rice"
price = 180
kg = 5
print(f"{kg} kg of {item} costs {price * kg} rupees.")

team = "Pakistan"
score = 320
print(f"{team} scored {score} runs in the match.")

print()

# ------------------------------------------------
# f-strings can do calculations inside {}
# ------------------------------------------------

marks = 85
total = 100
print(f"Marks: {marks} out of {total}")
print(f"Percentage: {marks / total * 100}%")

tasbeeh = 33
print(f"Total tasbeeh in 5 prayers: {tasbeeh * 5}")

print()

# ------------------------------------------------
# f-strings with input()
# ------------------------------------------------

your_name = input("Enter your name: ")
your_city = input("Enter your city: ")
print(f"Assalamu Alaikum {your_name}! Welcome from {your_city}.")

print()

school = input("Your school/madrasa name: ")
teacher = input("Your teacher's name: ")
print(f"You study at {school} under {teacher}. May Allah bless you both!")

print()

# ------------------------------------------------
# f-string vs + — when to use which
# ------------------------------------------------
# Use f-string when:  mixing text with variables or calculations
# Use + when:         simple joining of two strings only

# Both are correct — f-string is just cleaner for complex output

print()
print("f-strings make your code much easier to read. Excellent!")
