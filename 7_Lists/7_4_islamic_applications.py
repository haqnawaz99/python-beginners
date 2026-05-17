# ================================================
# Module 7 - Lesson 4: Data Structure Applications
# ================================================
# Real programs using lists, tuples, and dictionaries
# ================================================

print("=" * 50)
print("Data Structures — Real Applications")
print("=" * 50)

# ------------------------------------------------
# Application 1: Student Marks Manager
# ------------------------------------------------
print("\n--- Application 1: Marks Manager ---")

def collect_marks(subjects):
    marks = {}
    for subject in subjects:
        m = int(input(f"{subject} marks: "))
        marks[subject] = m
    return marks

def analyse_marks(name, marks_dict):
    marks_list = list(marks_dict.values())
    total = sum(marks_list)
    average = total / len(marks_list)
    highest_subject = max(marks_dict, key=marks_dict.get)
    lowest_subject = min(marks_dict, key=marks_dict.get)

    print(f"\n=== Report for {name} ===")
    for subject, marks in marks_dict.items():
        grade = "Pass" if marks >= 50 else "Fail"
        print(f"  {subject:<12}: {marks:>3}  ({grade})")
    print(f"  {'Total':<12}: {total}")
    print(f"  {'Average':<12}: {average:.1f}")
    print(f"  Best subject : {highest_subject}")
    print(f"  Weak subject : {lowest_subject}")

subjects = ["Quran", "Hadith", "Fiqh", "Arabic"]
name = input("Student name: ")
marks = collect_marks(subjects)
analyse_marks(name, marks)

# ------------------------------------------------
# Application 2: Prayer Time Tracker
# ------------------------------------------------
print("\n--- Application 2: Prayer Tracker ---")

prayer_times = {
    "Fajr"   : "05:00",
    "Dhuhr"  : "13:00",
    "Asr"    : "16:30",
    "Maghrib": "19:00",
    "Isha"   : "21:00"
}

offered = []
missed = []

print("Mark your prayers (yes/no):")
for prayer, time in prayer_times.items():
    status = input(f"  {prayer} ({time}) — offered? ").strip().lower()
    if status == "yes":
        offered.append(prayer)
    else:
        missed.append(prayer)

print(f"\nPrayers offered ({len(offered)}/5): {', '.join(offered) if offered else 'None'}")
print(f"Prayers missed  ({len(missed)}/5): {', '.join(missed) if missed else 'None'}")

if len(missed) == 0:
    print("Ma sha Allah! All 5 prayers offered today!")
elif len(offered) >= 3:
    print("Good effort. Try to complete all 5 tomorrow.")
else:
    print("Please try to offer all prayers. May Allah help you.")

# ------------------------------------------------
# Application 3: Madrasa Library System
# ------------------------------------------------
print("\n--- Application 3: Library System ---")

library = {
    "Sahih Bukhari"  : {"author": "Imam Bukhari", "copies": 5},
    "Sahih Muslim"   : {"author": "Imam Muslim",  "copies": 3},
    "Riyad us Salihin": {"author": "Imam Nawawi",  "copies": 7},
    "Al-Quran"       : {"author": "Allah (SWT)",   "copies": 20},
}

print("Available books:")
print(f"{'Title':<25} {'Author':<20} {'Copies'}")
print("-" * 55)
for title, info in library.items():
    print(f"{title:<25} {info['author']:<20} {info['copies']}")

search = input("\nSearch for a book: ").strip()
if search in library:
    book = library[search]
    print(f"Found: {search}")
    print(f"Author : {book['author']}")
    print(f"Copies : {book['copies']}")
else:
    print(f"'{search}' not found in library.")

# ------------------------------------------------
# Application 4: Pakistani Cities Quiz
# ------------------------------------------------
print("\n--- Application 4: Cities Quiz ---")

city_facts = {
    "Lahore"    : "capital of Punjab",
    "Karachi"   : "largest city of Pakistan",
    "Islamabad" : "capital of Pakistan",
    "Peshawar"  : "capital of KPK",
    "Quetta"    : "capital of Balochistan"
}

score = 0
cities = list(city_facts.keys())

for city in cities:
    answer = input(f"What is {city} known as? ").strip().lower()
    correct = city_facts[city].lower()
    if answer == correct:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. It is the {city_facts[city]}.")

print(f"\nFinal score: {score}/{len(cities)}")

print()
print("These are real programs — you are now a Python programmer!")
