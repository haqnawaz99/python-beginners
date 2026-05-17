# ================================================
# Module 7 - Lesson 2: Tuples
# ================================================
# Learn: What tuples are, how they differ from lists,
#        when to use them, tuple unpacking
# ================================================

print("=" * 50)
print("Tuples — Unchangeable Lists")
print("=" * 50)

# ------------------------------------------------
# What is a Tuple?
# ------------------------------------------------
# A tuple is like a list but IMMUTABLE — cannot be changed.
# Values are inside round brackets ( ) separated by commas.
# Use tuples for data that should never change:
#   - Prayer times, days of week, compass directions
#   - Coordinates, fixed settings, constants

# ------------------------------------------------
# 1. Creating a tuple
# ------------------------------------------------
print("\n1. Creating tuples:")

prayers = ("Fajr", "Dhuhr", "Asr", "Maghrib", "Isha")
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday")
coordinates = (31.5204, 74.3587)        # Lahore coordinates

print(prayers)
print(days)
print(coordinates)

# ------------------------------------------------
# 2. Accessing items — same as lists
# ------------------------------------------------
print("\n2. Accessing:")

print(prayers[0])       # Fajr
print(prayers[-1])      # Isha
print(days[4])          # Friday
print("Length:", len(prayers))

# ------------------------------------------------
# 3. Tuples cannot be changed
# ------------------------------------------------
print("\n3. Tuples are immutable:")

# This would cause a TypeError — commented out to avoid crash:
# prayers[0] = "Tahajjud"    # TypeError: 'tuple' object does not support item assignment

# This is WHY we use tuples — protect fixed data from accidental changes
print("Prayer names are fixed — tuples protect them.")

# ------------------------------------------------
# 4. Tuple unpacking — assign items to variables
# ------------------------------------------------
print("\n4. Tuple unpacking:")

# Assign each item in the tuple to a separate variable
first, second, third, fourth, fifth = prayers
print(f"First prayer : {first}")
print(f"Last prayer  : {fifth}")

# Swap two variables using tuple unpacking
a = "Lahore"
b = "Karachi"
a, b = b, a             # elegant swap — no temp variable needed!
print(f"After swap: a={a}, b={b}")

# Return multiple values from a function using tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)       # returns a tuple

marks = [85, 42, 90, 55, 78]
lowest, highest = get_min_max(marks)
print(f"Lowest: {lowest}, Highest: {highest}")

# ------------------------------------------------
# 5. Looping over a tuple
# ------------------------------------------------
print("\n5. Looping:")

for i, prayer in enumerate(prayers, 1):
    print(f"  {i}. {prayer}")

# ------------------------------------------------
# 6. List vs Tuple — when to use which
# ------------------------------------------------
print("\n6. List vs Tuple:")

# Use LIST when data will change:
student_list = ["Ahmed", "Fatima"]          # students join/leave
student_list.append("Hassan")

# Use TUPLE when data is fixed:
prayer_tuple = ("Fajr", "Dhuhr", "Asr", "Maghrib", "Isha")

print("List (changes allowed):", student_list)
print("Tuple (fixed forever) :", prayer_tuple)

# ------------------------------------------------
# 7. Practical example
# ------------------------------------------------
print("\n7. City coordinates:")

cities = [
    ("Lahore",    31.52, 74.36),
    ("Karachi",   24.86, 67.01),
    ("Islamabad", 33.72, 73.06),
    ("Peshawar",  34.01, 71.57),
]

for city, lat, lon in cities:
    print(f"{city:<12}: Lat {lat}, Lon {lon}")

print()
print("Tuples protect data that should never change. Well done!")
