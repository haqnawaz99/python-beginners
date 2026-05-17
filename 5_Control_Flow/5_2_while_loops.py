# ================================================
# Module 5 - Lesson 2: While Loops
# ================================================
# Learn: while loop, break, continue
#        Repeating code while a condition is True
# ================================================

print("=" * 50)
print("While Loops — Repeating with a Condition")
print("=" * 50)

# ------------------------------------------------
# What is a while loop?
# ------------------------------------------------
# A while loop repeats a block of code AS LONG AS
# a condition remains True.
# When the condition becomes False, the loop stops.
#
# WARNING: If the condition never becomes False,
# the loop runs forever (infinite loop)!
# Always make sure the condition will eventually be False.

# ------------------------------------------------
# 1. Basic while loop
# ------------------------------------------------
print("\n1. Basic while loop:")

count = 1
while count <= 5:
    print(f"Count: {count}")
    count = count + 1    # this changes count so loop will end

print("Loop finished!")

# ------------------------------------------------
# 2. Counting prayers
# ------------------------------------------------
print("\n2. Prayer counter:")

prayer = 1
prayer_names = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
while prayer <= 5:
    print(f"Prayer {prayer}: {prayer_names[prayer - 1]}")
    prayer += 1     # += 1 is shortcut for prayer = prayer + 1

# ------------------------------------------------
# 3. Countdown
# ------------------------------------------------
print("\n3. Countdown:")

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Bismillah — let us begin!")

# ------------------------------------------------
# 4. while with user input — repeat until correct
# ------------------------------------------------
print("\n4. Repeat until correct answer:")

correct_answer = "786"
answer = input("What is 700 + 86? ")
while answer != correct_answer:
    print("Wrong! Try again.")
    answer = input("What is 700 + 86? ")
print("Correct! Well done.")

# ------------------------------------------------
# 5. break — exit the loop early
# ------------------------------------------------
print("\n5. break — stop loop early:")

# Stop counting when we find the number 3
number = 1
while number <= 10:
    if number == 3:
        print("Found 3 — stopping!")
        break
    print(number)
    number += 1

# ------------------------------------------------
# 6. continue — skip current step, go to next
# ------------------------------------------------
print("\n6. continue — skip a step:")

# Print 1 to 7 but skip 4
number = 0
while number < 7:
    number += 1
    if number == 4:
        continue        # skip printing 4
    print(number)

# ------------------------------------------------
# 7. Tasbeeh counter
# ------------------------------------------------
print("\n7. Tasbeeh counter:")

target = int(input("How many tasbeeh do you want to count? "))
count = 0
while count < target:
    count += 1
print(f"Alhamdulillah! You completed {count} tasbeeh.")

# ------------------------------------------------
# 8. Running total with while
# ------------------------------------------------
print("\n8. Running total (enter 0 to stop):")

total = 0
while True:                      # runs forever until break
    amount = int(input("Enter amount (0 to stop): "))
    if amount == 0:
        break
    total += amount
    print(f"Running total: {total} rupees")

print(f"Final total: {total} rupees")

print()
print("While loops are powerful — use them carefully. Great work!")
