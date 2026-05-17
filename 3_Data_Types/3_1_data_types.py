# ================================================
# Module 3 - Lesson 1: Python Data Types
# ================================================
# Learn: int, float, str, bool, None and type()
# ================================================

# ------------------------------------------------
# What is a Data Type?
# ------------------------------------------------
# Every value in Python has a TYPE.
# The type tells Python what kind of data it is
# and what can be done with it.

# ------------------------------------------------
# Type 1: Integer (int)
# ------------------------------------------------
# Whole numbers — no decimal point.
# Used for counting, ages, quantities.

students = 35
prayers_per_day = 5
surahs_in_quran = 114
pakistan_year = 1947

print("Students:", students)
print("Daily prayers:", prayers_per_day)
print("Surahs in Quran:", surahs_in_quran)
print("Type:", type(students))           # <class 'int'>
print()

# ------------------------------------------------
# Type 2: Float (float)
# ------------------------------------------------
# Numbers WITH a decimal point.
# Used for prices, measurements, marks percentage.

price_per_kg = 135.50
temperature = 38.5
percentage = 87.5
zakat_rate = 2.5

print("Price per kg:", price_per_kg)
print("Temperature:", temperature, "C")
print("Marks percentage:", percentage)
print("Type:", type(price_per_kg))       # <class 'float'>
print()

# ------------------------------------------------
# Type 3: String (str)
# ------------------------------------------------
# Text inside quotes — anything in " " or ' '.
# Used for names, messages, labels.

student_name = "Fatima"
city = "Lahore"
greeting = "Assalamu Alaikum"
surah = "Al-Fatiha"

print("Name:", student_name)
print("City:", city)
print("Greeting:", greeting)
print("Type:", type(student_name))       # <class 'str'>
print()

# ------------------------------------------------
# Type 4: Boolean (bool)
# ------------------------------------------------
# Only two possible values: True or False
# Capital T and F — Python is case sensitive!

is_student = True
has_memorized_quran = False
is_fasting = True

print("Is student:", is_student)
print("Has memorized Quran:", has_memorized_quran)
print("Is fasting:", is_fasting)
print("Type:", type(is_student))         # <class 'bool'>
print()

# ------------------------------------------------
# Type 5: None
# ------------------------------------------------
# Represents "nothing" or "no value yet".
# Used as a placeholder before data is available.

future_score = None
print("Future score:", future_score)
print("Type:", type(future_score))       # <class 'NoneType'>
print()

# ------------------------------------------------
# type() — check the type of any value
# ------------------------------------------------
print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("Ahmed"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type(None))         # <class 'NoneType'>
print()

# ------------------------------------------------
# Important: "5" is NOT the same as 5
# ------------------------------------------------
a = "5"     # string
b = 5       # integer

print(type(a))    # str
print(type(b))    # int
print(a + a)      # 55  (joins text)
print(b + b)      # 10  (adds numbers)
print()

# ------------------------------------------------
# Tip: Underscores make large numbers readable
# ------------------------------------------------
population = 220_000_000
print("Pakistan population:", population)

print()
print("You now know all 4 main data types. Ma sha Allah!")
