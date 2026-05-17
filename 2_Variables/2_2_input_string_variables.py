# ================================================
# Module 2 - Lesson 2: Input & String Variables
# ================================================
# Learn: Storing input() in a variable, reusing it
# ================================================

# ------------------------------------------------
# Why store input() in a variable?
# ------------------------------------------------
# In Module 1 we used input() directly in print().
# That works, but you can only use the answer once.
# If you store it in a variable, you can use it many times.

# Without variable (can only use once):
print("Hello, " + input("Your name? "))

print()

# With variable (can use multiple times):
name = input("Your name? ")
print("Assalamu Alaikum, " + name + "!")
print("May Allah bless you, " + name + ".")
print(name + ", welcome to today's Python lesson.")

# ------------------------------------------------
# More Examples
# ------------------------------------------------

favorite_book = input("What is your favorite Islamic book? ")
print("Ma sha Allah! " + favorite_book + " is a wonderful book.")
print("May Allah help you understand " + favorite_book + " deeply.")

madrasa = input("What is the name of your madrasa? ")
print("Barakallah fi " + madrasa + "!")
print("May Allah give success to " + madrasa + " and all its students.")

surah = input("What is your favorite Surah? ")
print("Surah " + surah + " is indeed beautiful.")
print("May Allah give you tawfiq to memorize Surah " + surah + ".")

# ------------------------------------------------
# Asking multiple things and using all together
# ------------------------------------------------
print()
print("Let us build your profile:")
print()

student_name = input("Your name: ")
student_city = input("Your city: ")
student_class = input("Your class/level: ")

print()
print("--- Student Profile ---")
print("Name  : " + student_name)
print("City  : " + student_city)
print("Class : " + student_class)
print("Assalamu Alaikum, " + student_name + " from " + student_city + "!")

print()
print("Well done! Storing input in variables is very useful.")
