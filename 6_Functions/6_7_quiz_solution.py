# ================================================
# Module 6 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 6 QUIZ - SOLUTIONS")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1.
def say_bismillah():
    print("Bismillahir Rahmanir Raheem")

say_bismillah()
say_bismillah()
say_bismillah()

# Q2.
def greet(name):
    print(f"Assalamu Alaikum, {name}!")

greet("Ahmed")
greet("Fatima")
greet("Abdullah")

# Q3.
def double(number):
    return number * 2

print(double(5))       # 10

# Q4.
def is_even(number):
    return number % 2 == 0

print(is_even(4))      # True
print(is_even(7))      # False

# Q5.
def greet_default(name, greeting="Salam"):
    print(f"{greeting}, {name}!")

greet_default("Ahmed")                  # uses default
greet_default("Fatima", "Good morning") # overrides

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
def calculate_total(price, quantity):
    return price * quantity

price = int(input("Price per item: "))
quantity = int(input("Quantity: "))
total = calculate_total(price, quantity)
print(f"Total bill: {total} rupees")

# Q7.
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"

marks = int(input("Enter marks: "))
print(f"Grade: {get_grade(marks)}")

# Q8.
def check_eligible(age, surahs_memorized):
    return age >= 8 and surahs_memorized >= 5

print(check_eligible(10, 6))    # True
print(check_eligible(7, 8))     # False — age too young
print(check_eligible(12, 3))    # False — not enough surahs

# Q9.
def get_full_name(first, last):
    return first + " " + last

def print_id_card(first, last, city):
    name = get_full_name(first, last)
    print("=" * 30)
    print("     STUDENT ID CARD")
    print("=" * 30)
    print(f"Name : {name}")
    print(f"City : {city}")
    print("=" * 30)

print_id_card("Ahmed", "Ali", "Lahore")

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10.
def get_average(marks_list):
    return sum(marks_list) / len(marks_list)

def get_grade_avg(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

def print_summary(name, marks_list):
    subjects = ["Quran", "Hadith", "Fiqh", "Arabic", "Seerah"]
    print(f"\nStudent: {name}")
    print("-" * 30)
    for i in range(len(marks_list)):
        print(f"{subjects[i]:<10}: {marks_list[i]}")
    avg = get_average(marks_list)
    print("-" * 30)
    print(f"Average : {avg:.1f}")
    print(f"Grade   : {get_grade_avg(avg)}")

name = input("Student name: ")
marks_list = []
for i in range(5):
    m = int(input(f"Mark {i+1}: "))
    marks_list.append(m)
print_summary(name, marks_list)

# Q11.
def calculate_zakat(savings, rate=2.5):
    return savings * rate / 100

def print_zakat_report(name, savings):
    owes = savings >= 50000
    zakat = calculate_zakat(savings) if owes else 0
    print(f"\nName       : {name}")
    print(f"Savings    : {savings} rupees")
    print(f"Owes Zakat : {owes}")
    if owes:
        print(f"Zakat Due  : {zakat} rupees")
    else:
        print("Savings below nisab — no zakat due.")

name = input("Your name: ")
savings = int(input("Total savings (rupees): "))
print_zakat_report(name, savings)

# Q12.
def check_guess(guess, secret):
    if guess == secret:
        return "correct"
    elif guess > secret:
        return "too high"
    else:
        return "too low"

def play_game(secret, max_attempts):
    print(f"\nGuess the number! You have {max_attempts} attempts.")
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: "))
        result = check_guess(guess, secret)
        if result == "correct":
            print(f"Correct! You got it in {attempt} attempt(s)!")
            return
        else:
            print(f"Hint: {result}")
    print(f"Game over! The number was {secret}.")

play_game(7, 3)

print()
print("End of solutions.")
