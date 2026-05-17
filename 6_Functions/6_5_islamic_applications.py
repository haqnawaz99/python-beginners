# ================================================
# Module 6 - Lesson 5: Function Applications
# ================================================
# Real programs built using functions
# ================================================

print("=" * 50)
print("Functions — Real Applications")
print("=" * 50)

# ------------------------------------------------
# Application 1: Student Report Card System
# ------------------------------------------------

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def print_report_card(name, subjects, marks_list):
    print("=" * 40)
    print("       STUDENT REPORT CARD")
    print("=" * 40)
    print(f"Student: {name}")
    print("-" * 40)
    for i in range(len(subjects)):
        grade = get_grade(marks_list[i])
        print(f"{subjects[i]:<12}: {marks_list[i]:>3}  ({grade})")
    print("-" * 40)
    avg = calculate_average(marks_list)
    overall = get_grade(avg)
    print(f"Average    : {avg:.1f}%")
    print(f"Overall    : {overall}")
    print("=" * 40)

print("\n--- Application 1: Report Card ---")
name = input("Student name: ")
subjects = ["Quran", "Hadith", "Fiqh", "Arabic", "Seerah"]
marks_list = []
for subject in subjects:
    m = int(input(f"{subject} marks: "))
    marks_list.append(m)

print_report_card(name, subjects, marks_list)

# ------------------------------------------------
# Application 2: Bill Calculator
# ------------------------------------------------

def calculate_bill(item, price_per_kg, quantity):
    subtotal = price_per_kg * quantity
    return subtotal

def print_receipt(items, prices, quantities):
    print("\n" + "=" * 35)
    print("         SHOP RECEIPT")
    print("=" * 35)
    grand_total = 0
    for i in range(len(items)):
        subtotal = calculate_bill(items[i], prices[i], quantities[i])
        grand_total += subtotal
        print(f"{items[i]:<12}: {quantities[i]} kg x {prices[i]} = {subtotal}")
    print("-" * 35)
    print(f"{'TOTAL':<20}: {grand_total} rupees")
    print("=" * 35)
    print("Jazakallah Khair!")

print("\n--- Application 2: Shop Receipt ---")
num_items = int(input("How many items? "))
items, prices, quantities = [], [], []
for i in range(num_items):
    item = input(f"Item {i+1} name: ")
    price = int(input(f"Price per kg: "))
    qty = float(input(f"Quantity (kg): "))
    items.append(item)
    prices.append(price)
    quantities.append(qty)

print_receipt(items, prices, quantities)

# ------------------------------------------------
# Application 3: Simple Quiz System
# ------------------------------------------------

def ask_question(question, correct_answer):
    answer = input(f"{question} ").strip().lower()
    if answer == correct_answer.lower():
        print("Correct! Ma sha Allah.")
        return 1
    else:
        print(f"Wrong. Answer: {correct_answer}")
        return 0

def run_quiz(questions, answers, topic="Islamic Knowledge"):
    print(f"\n=== {topic} Quiz ===")
    score = 0
    for i in range(len(questions)):
        print(f"\nQ{i+1}:", end=" ")
        score += ask_question(questions[i], answers[i])
    return score

def show_quiz_result(score, total):
    percentage = score / total * 100
    print(f"\nFinal Score: {score}/{total} ({percentage:.0f}%)")
    if score == total:
        print("Perfect! Alhamdulillah!")
    elif percentage >= 60:
        print("Good effort! Keep learning.")
    else:
        print("Keep studying — you will improve!")

print("\n--- Application 3: Quiz ---")
questions = [
    "How many Surahs in the Quran?",
    "How many daily prayers?",
    "Which month was the Quran revealed?"
]
answers = ["114", "5", "Ramadan"]

score = run_quiz(questions, answers)
show_quiz_result(score, len(questions))

print()
print("Functions let you build complete programs. Excellent work!")
