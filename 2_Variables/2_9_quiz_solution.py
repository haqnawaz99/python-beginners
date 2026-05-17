# ================================================
# Module 2 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 2 QUIZ - SOLUTIONS")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1.
prayer_name = "Fajr"
print(prayer_name)

# Q2.
first_name = "Ahmed"
last_name = "Ali"
print(first_name + " " + last_name)

# Q3.
city_description = "lahore is beautiful"
print(city_description.title())

# Q4.
student_name = input("What is your name? ")
print("Welcome, " + student_name + "!")

# Q5.
messy_name = "  Ahmed  "
print(messy_name.strip())

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
madrasa = input("Enter your madrasa name: ")
print(madrasa.upper())

# Q7.
raw_name = input("Type your name: ")
clean_name = raw_name.strip().title()
print("Cleaned name: " + clean_name)

# Q8.
word = "Bismillah"
print("Word  : " + word)
print("Length:", len(word))

# Q9. Fixed variable names:
# a) student name = "Ahmed"   -> space not allowed
student_name = "Ahmed"

# b) 1city = "Lahore"         -> cannot start with number
city1 = "Lahore"

# c) my_school = "Jamia"      -> this is CORRECT already
my_school = "Jamia"

# d) for = "loop"             -> 'for' is a reserved keyword
for_example = "loop"

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10.
first = input("First name: ").strip().title()
last = input("Last name: ").strip().title()
city = input("City: ").strip().title()
full_name = first + " " + last
print("Full Name  : " + full_name)
print("City       : " + city)
print("Name Length:", len(full_name))

# Q11.
subject1 = input("Subject 1: ")
subject2 = input("Subject 2: ")
print("Before swap:", subject1, "and", subject2)
temp = subject1
subject1 = subject2
subject2 = temp
print("After swap :", subject1, "and", subject2)

# Q12.
print()
name = input("Student name: ").strip().title()
teacher = input("Teacher name: ").strip().title()
level = input("Class level: ").strip().title()
city = input("City: ").strip().title()
print("=============================")
print("MADRASA STUDENT ID CARD")
print("=============================")
print("Student : " + name)
print("Teacher : " + teacher)
print("Level   : " + level)
print("City    : " + city)
print("=============================")

print()
print("End of solutions.")
