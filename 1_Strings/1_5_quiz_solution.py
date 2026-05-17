# ================================================
# Module 1 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 1 QUIZ - SOLUTIONS")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1.
print("Assalamu" + " Alaikum")

# Q2.
print("Ahmed" + " " + "Ali")

# Q3.
print("I study at " + "Jamia Islamia" + ", Lahore")

# Q4.
name = input("What is your name? ")
print("Welcome, " + name + "!")

# Q5.
city = input("What is your city? ")
print("You are from " + city + ".")

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
prophet = input("Name your favorite Prophet: ")
print("Peace be upon Prophet " + prophet + " and his family.")

# Q7.
school = input("What is your school name? ")
teacher = input("What is your teacher's name? ")
print("I study at " + school + " and my teacher is " + teacher + ".")

# Q8. Fix: cannot use + with a number, must use str() or comma
# WRONG:  print("Pakistan was created in " + 1947)
# FIXED:
print("Pakistan was created in " + str(1947))
# OR:
print("Pakistan was created in", 1947)

# Q9.
subject = input("What subject are you studying today? ")
print("Bismillah. Today we study " + subject + ". May Allah help us.")

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10.
name = input("Your name: ")
city = input("Your city: ")
school = input("Your school: ")
age = input("Your age: ")
print("My name is " + name + ".")
print("I am from " + city + ".")
print("I study at " + school + ".")
print("I am " + age + " years old.")

# Q11.
city = input("Enter a Pakistani city: ")
print(city + " is a beautiful city in Pakistan.")
print(city + " has famous historical sites.")
print(city + " is known for its delicious food.")

# Q12.
print()
name = input("Student name: ")
age = input("Age: ")
level = input("Class level (e.g. Hifz, Nazra, Alim): ")
fav_subject = input("Favorite Islamic subject: ")
print("================================")
print("MADRASA REGISTRATION")
print("================================")
print("Name          : " + name)
print("Age           : " + age)
print("Class Level   : " + level)
print("Fav Subject   : " + fav_subject)
print("================================")
print("Registration complete. Jazakallah Khair!")

print()
print("End of solutions.")
