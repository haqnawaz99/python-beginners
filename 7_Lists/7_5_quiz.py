# ================================================
# Module 7 - Quiz: Lists, Tuples, Dictionaries
# ================================================
# Covers: list creation/access/modify/methods,
#         tuples, dictionaries, looping over all three
# Difficulty: Easy / Medium / Complex
# ================================================

print("=" * 50)
print("MODULE 7 QUIZ - Data Structures")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1. Create a list of 5 Pakistani cities and print it.
#     Then print only the first and last city.


# Q2. Create this list: subjects = ["Quran", "Hadith", "Fiqh"]
#     Add "Arabic" to the end.
#     Change "Hadith" to "Tafseer".
#     Print the final list.


# Q3. Create a tuple of the 5 daily prayers.
#     Print the 3rd prayer (index 2).
#     Print the total number of prayers using len().


# Q4. Create a dictionary for a student with keys:
#     name, city, marks
#     Print each value using the key.


# Q5. Loop over this list and print each item on its own line:
#     fruits = ["mango", "apple", "banana", "guava", "date"]


# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6. Create a list of 5 marks.
#     Print: total, average, highest, lowest.
#     Use sum(), len(), max(), min().


# Q7. Create a dictionary of prayer times:
#     Fajr: 5:00 AM, Dhuhr: 1:00 PM, Asr: 4:30 PM
#     Loop over it and print each prayer and its time.
#     Then ask the user for a prayer name and print its time.


# Q8. Ask the user for 4 student names using input() in a loop.
#     Store them in a list.
#     Print the list sorted alphabetically using sorted().


# Q9. Use tuple unpacking to do this in one line:
#     Swap the values of two variables:
#     a = "Lahore"
#     b = "Karachi"
#     After the swap, print both variables.


# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10. Ask the user how many students to register (int).
#      For each student ask for name and marks.
#      Store as a dictionary {name: marks}.
#      At the end print:
#        - All students and their marks
#        - The student with the highest marks
#        - How many passed (marks >= 50)


# Q11. Create a dictionary where each key is a subject
#      and each value is a list of 3 marks.
#      subjects: Quran, Hadith, Fiqh
#      Ask the user for 3 marks per subject.
#      Print each subject with its average.


# Q12. Build a contact book program:
#      - Start with an empty dictionary
#      - Loop 3 times asking for: person name and phone number
#      - Store each as contact_book[name] = phone
#      - After all entries, ask the user to search for a name
#      - Print the phone number if found, or "Not found" if not
#      - Print all contacts at the end


print()
print("Quiz done! Check 7_6_quiz_solution.py for answers.")
