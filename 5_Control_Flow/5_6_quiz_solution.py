# ================================================
# Module 5 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 5 QUIZ - SOLUTIONS")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1.
marks = int(input("Enter your marks: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Q2.
for i in range(1, 11):
    print(i)

# Q3.
prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
for prayer in prayers:
    print(prayer)

# Q4.
count = 1
while count <= 5:
    print(count)
    count += 1

# Q5.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
else:
    print("Adult")

# Q7.
num = int(input("Enter a number for its table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Q8.
secret = 42
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct! Well done!")
        break
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

# Q9.
marks_list = [85, 42, 90, 55, 38, 78, 61, 29, 95, 48]
passed = 0
failed = 0
for m in marks_list:
    if m >= 50:
        passed += 1
    else:
        failed += 1
print(f"Passed: {passed}")
print(f"Failed: {failed}")

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10.
num_students = int(input("Number of students: "))
total = 0
highest = 0
pass_count = 0

for i in range(1, num_students + 1):
    name = input(f"Student {i} name: ")
    marks = int(input(f"Marks for {name}: "))
    total += marks
    if marks > highest:
        highest = marks
    if marks >= 50:
        pass_count += 1

print(f"Total marks  : {total}")
print(f"Class average: {total / num_students:.1f}")
print(f"Highest marks: {highest}")
print(f"Passed       : {pass_count} out of {num_students}")

# Q11.
for row in range(1, 6):
    print("* " * row)

# Q12.
secret = 7
won = False
for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt} — Guess the number: "))
    if guess == secret:
        print("Correct! You win!")
        won = True
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")

if not won:
    print(f"Game over! The number was {secret}")

print()
print("End of solutions.")
