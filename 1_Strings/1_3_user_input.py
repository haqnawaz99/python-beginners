# ================================================
# Module 1 - Lesson 3: User Input
# ================================================
# Learn: input(), getting information from the user
# ================================================

# ------------------------------------------------
# What is input()?
# ------------------------------------------------
# input() pauses the program and waits for the user to type.
# Whatever the user types is returned as a string.
# The text inside input("...") is the question shown to the user.

# ------------------------------------------------
# Basic input() usage
# ------------------------------------------------
# input("...") can be placed directly inside print(), joined with +.
# Python asks the question, waits for the answer, and uses it right there.

print("Assalamu Alaikum, " + input("Please enter your name: "))

# ------------------------------------------------
# More examples
# ------------------------------------------------

print("Ma sha Allah, " + input("Which city are you from? ") + " is a wonderful city!")

print("Great choice! " + input("What is your favorite subject? ") + " is very important.")

# ------------------------------------------------
# input() always gives back a STRING
# ------------------------------------------------
# Even if the user types a number, it comes back as text.
# We will learn how to handle this in Module 3 (Data Types).

print("You are " + input("How old are you? ") + " years old. May Allah bless you!")

# ------------------------------------------------
# Islamic & Pakistani Context Examples
# ------------------------------------------------

print("May Allah give barakah to " + input("What is the name of your school or madrasa? ") + "!")

print("Peace and blessings be upon Prophet " + input("Name your favorite Prophet (peace be upon them): "))

# ------------------------------------------------
# Asking multiple questions
# ------------------------------------------------
# You can call input() as many times as you need - each call asks one question.
#
# A small preview: to COMBINE the answers to two different questions into
# one sentence, we need a way to give each answer a name so we can use it
# again later. That "naming" idea is called a variable - the full lesson
# is in Module 2. For now, here is a small preview:

first = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Assalamu Alaikum, " + first + " " + last + "!")

print()
print("Well done! You can now interact with the user.")
