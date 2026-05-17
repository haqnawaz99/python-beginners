# ================================================
# Module 5 - Lesson 4: Control Flow Applications
# ================================================
# Real programs using if, while, and for loops
# ================================================

print("=" * 50)
print("Control Flow — Real Applications")
print("=" * 50)

# ------------------------------------------------
# Application 1: Grade Calculator
# ------------------------------------------------
print("\n--- Application 1: Grade Calculator ---")

subjects = ["Quran", "Hadith", "Fiqh", "Arabic", "Seerah"]
total = 0
passed_count = 0

for subject in subjects:
    marks = int(input(f"{subject} marks (out of 100): "))
    total += marks
    if marks >= 50:
        passed_count += 1

average = total / len(subjects)
print(f"\nTotal marks    : {total} / {len(subjects) * 100}")
print(f"Average        : {average:.1f}%")
print(f"Subjects passed: {passed_count} / {len(subjects)}")

if average >= 80:
    print("Result: Excellent — First Division!")
elif average >= 60:
    print("Result: Good — Second Division")
elif average >= 50:
    print("Result: Pass — Third Division")
else:
    print("Result: Fail — Please study harder")

# ------------------------------------------------
# Application 2: Simple Quiz Game
# ------------------------------------------------
print("\n--- Application 2: Islamic Quiz ---")

questions = [
    ("How many Surahs are in the Quran?", "114"),
    ("How many daily prayers are there?", "5"),
    ("In which month was the Quran revealed?", "ramadan"),
    ("How many Paras are in the Quran?", "30"),
]

score = 0
for number, (question, answer) in enumerate(questions, start=1):
    user_answer = input(f"Q{number}: {question} ").strip().lower()
    if user_answer == answer.lower():
        print("Correct! Ma sha Allah.")
        score += 1
    else:
        print(f"Wrong. The answer is: {answer}")

print(f"\nYour score: {score} out of {len(questions)}")
if score == len(questions):
    print("Perfect score! Alhamdulillah!")
elif score >= len(questions) // 2:
    print("Good effort! Keep learning.")
else:
    print("Keep studying — you will do better next time!")

# ------------------------------------------------
# Application 3: Attendance Tracker
# ------------------------------------------------
print("\n--- Application 3: Attendance Tracker ---")

num_students = int(input("How many students to check? "))
present_count = 0
absent_students = []

for i in range(1, num_students + 1):
    name = input(f"Student {i} name: ")
    status = input(f"Is {name} present? (yes/no): ").strip().lower()
    if status == "yes":
        present_count += 1
    else:
        absent_students.append(name)

absent_count = num_students - present_count
attendance_pct = present_count / num_students * 100

print(f"\nTotal students : {num_students}")
print(f"Present        : {present_count}")
print(f"Absent         : {absent_count}")
print(f"Attendance     : {attendance_pct:.1f}%")

if absent_students:
    print("Absent students:")
    for name in absent_students:
        print(f"  - {name}")

# ------------------------------------------------
# Application 4: Prayer Time Reminder
# ------------------------------------------------
print("\n--- Application 4: Prayer Reminder ---")

prayer_times = {
    "Fajr": 5,
    "Dhuhr": 13,
    "Asr": 16,
    "Maghrib": 19,
    "Isha": 21
}

current_hour = int(input("Enter current hour (0-23): "))
reminder_shown = False

for prayer, hour in prayer_times.items():
    if current_hour == hour:
        print(f"Time for {prayer} prayer! Please stop and pray.")
        reminder_shown = True
        break
    elif current_hour == hour - 1:
        print(f"{prayer} prayer is in 1 hour. Please prepare.")
        reminder_shown = True
        break

if not reminder_shown:
    print("No prayer due at this hour. Continue your work.")

print()
print("These are real programs you can build with control flow. Excellent!")
