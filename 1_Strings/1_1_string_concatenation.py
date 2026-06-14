# ================================================
# Module 1 - Lesson 1: String Concatenation
# ================================================
# Learn: Joining strings together using +
# ================================================

# ------------------------------------------------
# What is Concatenation?
# ------------------------------------------------
# Concatenation means joining two strings into one.
# We use the + symbol to join strings.
# Think of it like gluing two words together.

# ------------------------------------------------
# Basic Concatenation
# ------------------------------------------------

# Joining two strings
print("Assalamu" + " Alaikum")

# Joining a title and a name
print("Maulana " + "Abdul Rahman")

# Joining three parts
print("Lahore" + ", " + "Pakistan")

# ------------------------------------------------
# Important: Spaces must be added manually
# ------------------------------------------------
# The + symbol joins exactly what you give it.
# If you forget the space, words will run together.

# WRONG - no space between words:
print("Assalamu" + "Alaikum")       # Output: AssalamuAlaikum

# CORRECT - space inside one of the strings:
print("Assalamu " + "Alaikum")      # Output: Assalamu Alaikum
print("Assalamu" + " Alaikum")      # Output: Assalamu Alaikum

# ------------------------------------------------
# Practical Examples
# ------------------------------------------------

# Greeting with full name
print("Welcome, " + "Ustaz Ahmad!")

# Islamic phrase
print("In the name of " + "Allah, the Most Gracious, the Most Merciful")

# School announcement
print("Today's lesson: " + "Introduction to Python")

# City and country
print("I am from " + "Karachi" + ", Pakistan")

# Combining multiple parts
print("The Quran has " + "114" + " Surahs and " + "30" + " Paras")

# ------------------------------------------------
# Urdu Examples
# ------------------------------------------------
print("السلام" + " علیکم")
print("خوش آمدید " + "میرے پیارے طالبعلموں")
print("بِسْمِ اللّٰہِ " + "الرَّحْمٰنِ الرَّحِیْمِ")

# ------------------------------------------------
# Common Mistake
# ------------------------------------------------
# You CANNOT use + to join a string and a number directly.

# WRONG:
# print("There are " + 5 + " prayers")   # TypeError!

# CORRECT - convert number to string using str():
print("There are " + str(5) + " prayers")

# OR - use a comma in print() instead (easier for beginners):
print("There are", 5, "prayers")

# ------------------------------------------------
# Quotes Inside a String
# ------------------------------------------------
# What if the text itself contains a quotation mark?

# Trick 1: use the other type of quote
print("Ahmed's book")
print('She said "Bismillah"')

# Trick 2: use the backslash escape character \
print('Ahmed\'s book')
print("She said \"Bismillah\"")

# ------------------------------------------------
# Special Characters: \n and \t
# ------------------------------------------------
# \n moves to a new line
# \t adds a tab space (like pressing the Tab key)

print("Lahore\nKarachi\nIslamabad")

print("Name:\tAhmed")
print("City:\tLahore")

print("Surah:\tAl-Fatiha\nVerses:\t7")

# ------------------------------------------------
# Drawing Patterns with print()
# ------------------------------------------------
# We can use symbols like * and spaces to draw simple pictures.
# Each print() is one row.

print("  *")
print(" * *")
print("*****")

print()

print("*****")
print("*   *")
print("*****")

print()
print("Great work! You can now join strings together.")
