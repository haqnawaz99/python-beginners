# ================================================
# Module 9 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 9 QUIZ - SOLUTIONS")
print("=" * 50)
print()

import os

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1.
with open("salam.txt", "w") as f:
    f.write("Assalamu Alaikum\n")
    f.write("Bismillah\n")
    f.write("JazakAllah Khair\n")

with open("salam.txt", "r") as f:
    print(f.read())

# Q2.
with open("salam.txt", "a") as f:
    f.write("Ma sha Allah\n")

with open("salam.txt", "r") as f:
    print(f.read())

# Q3.
try:
    with open("does_not_exist.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found! Please check the filename.")

# Q4.
cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta"]
with open("cities.txt", "w") as f:
    for city in cities:
        f.write(city + "\n")

with open("cities.txt", "r") as f:
    lines = f.readlines()
print(f"Cities saved: {len(lines)}")

# Q5.
name = input("Your name: ")
subject = input("Favourite subject: ")
with open("profile.txt", "w") as f:
    f.write(f"Name   : {name}\n")
    f.write(f"Subject: {subject}\n")

with open("profile.txt", "r") as f:
    print(f.read())

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
for i in range(3):
    name = input(f"Student {i+1}: ")
    with open("class.txt", "a") as f:
        f.write(name.strip() + "\n")

with open("class.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  {i}. {line.strip()}")

# Q7.
def save_score(name, score, filename):
    with open(filename, "a") as f:
        f.write(f"{name},{score}\n")

def load_scores(filename):
    scores = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if "," in line:
                    name, score = line.split(",")
                    scores.append((name, int(score)))
    except FileNotFoundError:
        pass
    return scores

save_score("Ahmed",  85, "scores.txt")
save_score("Fatima", 92, "scores.txt")
save_score("Hassan", 70, "scores.txt")

scores = load_scores("scores.txt")
for name, score in scores:
    print(f"  {name}: {score}")

# Q8.
try:
    with open("students.txt", "r") as f:
        names = [line.strip() for line in f if line.strip()]
    print(f"Total students: {len(names)}")
    for i, name in enumerate(names, 1):
        print(f"  {i}. {name}")
except FileNotFoundError:
    print("students.txt not found.")

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q9.
CONTACTS = "contacts.txt"

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    with open(CONTACTS, "a") as f:
        f.write(f"{name},{phone}\n")
    print("Contact saved!")

def view_contacts():
    try:
        with open(CONTACTS, "r") as f:
            lines = [l.strip() for l in f if l.strip()]
        if not lines:
            print("No contacts yet.")
            return
        for line in lines:
            name, phone = line.split(",")
            print(f"  {name:<20}: {phone}")
    except FileNotFoundError:
        print("No contacts file yet.")

def search_contact(query):
    try:
        with open(CONTACTS, "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                if query.lower() in name.lower():
                    print(f"Found: {name} — {phone}")
                    return
        print("Not found.")
    except FileNotFoundError:
        print("No contacts file yet.")

while True:
    print("\n1.Add  2.View  3.Search  4.Exit")
    c = input("Choice: ").strip()
    if c == "1":
        add_contact()
    elif c == "2":
        view_contacts()
    elif c == "3":
        q = input("Search name: ")
        search_contact(q)
    elif c == "4":
        break

# Q10.
MARKS_FILE = "all_marks.txt"

student = input("Student name: ")
subject = input("Subject: ")
marks = int(input("Marks: "))
with open(MARKS_FILE, "a") as f:
    f.write(f"{student},{subject},{marks}\n")

data = {}
try:
    with open(MARKS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if "," in line:
                s, sub, m = line.split(",")
                if s not in data:
                    data[s] = []
                data[s].append((sub, int(m)))
except FileNotFoundError:
    pass

for name, records in data.items():
    total = sum(m for _, m in records)
    avg = total / len(records)
    print(f"\n{name} (avg: {avg:.1f})")
    for sub, m in records:
        print(f"  {sub}: {m}")

# Q11.
DHIKR_FILE = "dhikr_log.txt"
dhikr = input("Which dhikr (SubhanAllah/Alhamdulillah/AllahuAkbar): ").strip()
count = int(input("How many times: "))
with open(DHIKR_FILE, "a") as f:
    f.write(f"{dhikr},{count}\n")

totals = {}
grand_total = 0
try:
    with open(DHIKR_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if "," in line:
                d, c = line.split(",")
                totals[d] = totals.get(d, 0) + int(c)
                grand_total += int(c)
except FileNotFoundError:
    pass

print("\nDhikr Summary:")
for d, c in totals.items():
    print(f"  {d}: {c}")
print(f"Grand Total: {grand_total}")

print()
print("End of solutions.")
