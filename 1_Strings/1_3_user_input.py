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

# Step 1: Ask the user something
# Step 2: Store what they type in a variable
# Step 3: Use it in print()

name = input("Please enter your name: ")
print("Assalamu Alaikum, " + name)

# ------------------------------------------------
# More examples
# ------------------------------------------------

city = input("Which city are you from? ")
print("Ma sha Allah, " + city + " is a wonderful city!")

subject = input("What is your favorite subject? ")
print("Great choice! " + subject + " is very important.")

# ------------------------------------------------
# Using input() directly inside print()
# ------------------------------------------------
# You can skip the variable and use input() straight in print().
# This is shorter but less flexible.

print("Wa Alaikum Assalam, " + input("Who are you replying to? "))

# ------------------------------------------------
# input() always gives back a STRING
# ------------------------------------------------
# Even if the user types a number, it comes back as text.
# We will learn how to handle this in Module 3 (Data Types).

age = input("How old are you? ")
print("You are " + age + " years old. May Allah bless you!")

# ------------------------------------------------
# Islamic & Pakistani Context Examples
# ------------------------------------------------

school = input("What is the name of your school or madrasa? ")
print("May Allah give barakah to " + school + "!")

prophet_name = input("Name your favorite Prophet (peace be upon them): ")
print("Peace and blessings be upon Prophet " + prophet_name)

print()
print("Well done! You can now interact with the user.")
