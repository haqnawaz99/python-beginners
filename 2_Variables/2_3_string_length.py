# ================================================
# Module 2 - Lesson 3: String Length with len()
# ================================================
# Learn: len() function, counting characters in a string
# ================================================

# ------------------------------------------------
# What is len()?
# ------------------------------------------------
# len() counts the number of characters in a string.
# Characters include: letters, spaces, punctuation, numbers.
# It returns a number (integer).

# ------------------------------------------------
# Basic Examples
# ------------------------------------------------

print(len("Ahmed"))             # 5 letters
print(len("Assalamu Alaikum")) # 16 (includes the space)
print(len("Pakistan"))         # 8
print(len(""))                 # 0 - empty string has length zero

# ------------------------------------------------
# Using len() with a variable
# ------------------------------------------------

name = "Muhammad"
print(len(name))               # 8

city = "Islamabad"
print(len(city))               # 9

surah = "Al-Fatiha"
print(len(surah))              # 9

# ------------------------------------------------
# Printing len() in a sentence
# ------------------------------------------------
# len() returns a number, not a string.
# To join it with text using +, wrap it in str().
# OR use a comma in print() (easier for beginners).

name = "Abdullah"

# Using comma (recommended for beginners):
print("The name", name, "has", len(name), "letters.")

# Using str() and +:
print("The name " + name + " has " + str(len(name)) + " letters.")

# ------------------------------------------------
# Counting from user input
# ------------------------------------------------

word = input("Type any word: ")
print("You typed:", word)
print("It has", len(word), "characters.")

surah_name = input("Enter a Surah name: ")
print("Surah " + surah_name + " has", len(surah_name), "characters in its name.")

# ------------------------------------------------
# Interesting Facts using len()
# ------------------------------------------------

bismillah = "Bismillahirrahmanirrahim"
print("Bismillah has", len(bismillah), "characters (no spaces)")

kalima = "La ilaha illallah Muhammadur Rasulullah"
print("The Kalima has", len(kalima), "characters including spaces")

print()
print("Great! You can now measure the length of any string.")
