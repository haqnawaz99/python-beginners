# ================================================
# Module 9 - Lesson 1: Reading Files
# ================================================
# Learn: open(), read(), readline(), readlines(),
#        with statement, file does not exist error
# ================================================

print("=" * 50)
print("File I/O — Reading Files")
print("=" * 50)

# ------------------------------------------------
# Why work with files?
# ------------------------------------------------
# So far, all our data disappears when the program stops.
# Files let us SAVE data permanently and READ it back later.
# This is how real programs work:
#   - Save student records to a file
#   - Read a list of names from a file
#   - Log results to a file

# ------------------------------------------------
# The with statement — safest way to open files
# ------------------------------------------------
# with open("filename", "mode") as file:
#     do something with file
#
# Mode:
#   "r"  = read   (file must exist)
#   "w"  = write  (creates or overwrites file)
#   "a"  = append (adds to end of existing file)
#
# with automatically closes the file when done.

# ------------------------------------------------
# First: create a test file to read from
# ------------------------------------------------
# We create this file now so the reading examples work.

with open("students.txt", "w") as f:
    f.write("Ahmed Ali\n")
    f.write("Fatima Khan\n")
    f.write("Hassan Raza\n")
    f.write("Zainab Mir\n")
    f.write("Abdullah Shah\n")

print("File 'students.txt' created.")

# ------------------------------------------------
# 1. Read the entire file at once
# ------------------------------------------------
print("\n1. read() — entire file:")

with open("students.txt", "r") as f:
    content = f.read()
    print(content)

# ------------------------------------------------
# 2. Read line by line with a loop
# ------------------------------------------------
print("2. Loop through lines:")

with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())         # .strip() removes the \n at end

# ------------------------------------------------
# 3. Read all lines into a list
# ------------------------------------------------
print("\n3. readlines() — list of lines:")

with open("students.txt", "r") as f:
    lines = f.readlines()

print(f"Total students: {len(lines)}")
print(f"First student : {lines[0].strip()}")
print(f"Last student  : {lines[-1].strip()}")

# Process the list
print("\nNumbered list:")
for i, line in enumerate(lines, 1):
    print(f"  {i}. {line.strip()}")

# ------------------------------------------------
# 4. Handle file not found
# ------------------------------------------------
print("\n4. File not found error:")

try:
    with open("missing_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found. Please check the filename.")

# ------------------------------------------------
# 5. Check if a file exists before opening
# ------------------------------------------------
print("\n5. Check if file exists:")

import os

filename = "students.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    print(f"File found — {len(lines)} lines.")
else:
    print(f"File '{filename}' does not exist.")

print()
print("Reading files lets you work with saved data. Well done!")
