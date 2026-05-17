# ================================================
# Module 2 - Lesson 1: Introduction to Variables
# ================================================
# Learn: What is a variable, how to create one,
#        how to use it in print()
# ================================================

# ------------------------------------------------
# What is a Variable?
# ------------------------------------------------
# A variable is a named box that stores a value.
# You give it a name, then put something inside.
# Later you can use that name to get the value back.

# Think of it like this:
# A student's bag has a name tag.
# You can put books inside the bag.
# You find the bag by reading the name tag.

# ------------------------------------------------
# Creating a Variable
# ------------------------------------------------
# variable_name = value
# The = sign means "store this value in this name"

greeting = "Assalamu Alaikum"
student_name = "Ahmed"
city = "Lahore"
school = "Jamia Islamia"

# ------------------------------------------------
# Using a Variable
# ------------------------------------------------
# Just write the variable name - no quotes needed!

print(greeting)
print(student_name)
print(city)
print(school)

# ------------------------------------------------
# Variables in Concatenation
# ------------------------------------------------
# Variables can be joined with + just like strings

print("Hello, " + student_name)
print(student_name + " is from " + city)
print("Welcome to " + school + "!")

# ------------------------------------------------
# Changing a Variable
# ------------------------------------------------
# You can update a variable at any time.
# The new value replaces the old one.

subject = "Quran"
print("Today's subject: " + subject)

subject = "Hadith"
print("Now the subject is: " + subject)

# ------------------------------------------------
# Multiple Variables Together
# ------------------------------------------------

first_name = "Fatima"
last_name = "Khan"
age = "15"
city = "Karachi"

print("Name : " + first_name + " " + last_name)
print("Age  : " + age)
print("City : " + city)

# ------------------------------------------------
# Summary
# ------------------------------------------------
# variable_name = value       creates a variable
# print(variable_name)        shows its value
# Variables make code cleaner and reusable

print()
print("You now understand variables. Excellent work!")
