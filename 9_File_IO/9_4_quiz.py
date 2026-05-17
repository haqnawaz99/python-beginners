# ================================================
# Module 9 - Quiz: File I/O
# ================================================
# Covers: open(), read/write/append, with statement,
#         FileNotFoundError, saving/loading data
# Difficulty: Easy / Medium / Complex
# ================================================

print("=" * 50)
print("MODULE 9 QUIZ - File I/O")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1. Write code that creates a file called "salam.txt"
#     and writes these 3 lines into it:
#       Assalamu Alaikum
#       Bismillah
#       JazakAllah Khair
#     Then read the file and print its contents.


# Q2. Open "salam.txt" in APPEND mode and add one more line:
#     "Ma sha Allah"
#     Then read and print the full file again.


# Q3. Write a try/except that handles FileNotFoundError
#     when trying to open "does_not_exist.txt"
#     Print a helpful message if the file is not found.


# Q4. Create a list of 5 Pakistani cities.
#     Write each city to "cities.txt" (one per line).
#     Read the file and print the number of cities saved.


# Q5. Ask the user for their name and favourite subject.
#     Save both to a file called "profile.txt".
#     Then read and display the file contents.


# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6. Ask the user for 3 student names in a loop.
#     Append each name to "class.txt" as you collect them
#     (don't wait — append each one immediately).
#     After the loop, read the file and display a numbered list.


# Q7. Write a function save_score(name, score, filename)
#     that appends "name,score\n" to the file.
#     Write another function load_scores(filename) that
#     reads the file and returns a list of (name, score) tuples.
#     Test with 3 entries and print all scores.


# Q8. Read "students.txt" (created in Lesson 1).
#     Count how many students are in the file.
#     Print the total count and list all names.
#     Handle FileNotFoundError if the file doesn't exist.


# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q9. Build a persistent contact book:
#     - File: "contacts.txt" (format: name,phone per line)
#     - Menu:
#         1. Add contact (append to file)
#         2. View all contacts (read file, print neatly)
#         3. Search by name (read file, find match)
#         4. Exit
#     - Handle FileNotFoundError for empty/missing file
#     - Loop until user chooses 4


# Q10. Build a marks tracker that persists across runs:
#      - File: "all_marks.txt" (format: student,subject,marks)
#      - Let user add a new record
#      - Display all records grouped by student
#      - Show each student's average


# Q11. Build a "daily dhikr counter":
#      - File: "dhikr_log.txt"
#      - Ask user which dhikr (SubhanAllah / Alhamdulillah / AllahuAkbar)
#      - Ask how many times they recited
#      - Append to file with the dhikr name and count
#      - Read the file and show total count for each type
#      - Print overall grand total


print()
print("Quiz done! Check 9_5_quiz_solution.py for answers.")
