# ================================================
# Module 4 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 4 QUIZ - SOLUTIONS")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1.
tafsir = 55
hadith = 45
print("Total books:", tafsir + hadith)

# Q2.
price = 850
quantity = 3
print("Total cost:", price * quantity, "rupees")

# Q3.
qurans = 28
shelves = 5
print("Per shelf:", qurans // shelves)
print("Leftover:", qurans % shelves)

# Q4.
print("10 + 5 * 2  =", 10 + 5 * 2)      # 20 — * runs first
print("(10 + 5) * 2 =", (10 + 5) * 2)   # 30 — brackets first
# They are different because BODMAS applies without brackets.

# Q5.
marks = 75
print("Marks >= 50:", marks >= 50)

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
price = int(input("Price per item: "))
qty = int(input("Quantity: "))
print(f"Total bill: {price * qty} rupees")

# Q7.
marks = int(input("Your marks (out of 100): "))
print(f"Passed (>=50)      : {marks >= 50}")
print(f"Distinction (>=80) : {marks >= 80}")
print(f"Full marks (==100) : {marks == 100}")

# Q8.
age = 12
surahs_memorized = 5
eligible = (age >= 8 and age <= 15) and surahs_memorized >= 3
print(f"Eligible for Hifz class: {eligible}")

# Q9. Predictions and results:
# a) 2 + 3 * 4 = 14  (3*4=12, then +2)
print("2 + 3 * 4  =", 2 + 3 * 4)        # 14

# b) (2 + 3) * 4 = 20  (bracket first: 5*4)
print("(2 + 3) * 4 =", (2 + 3) * 4)     # 20

# c) 2 ** 3 + 1 = 9  (2**3=8, then +1)
print("2 ** 3 + 1  =", 2 ** 3 + 1)      # 9

# d) floor div and modulus
print("10 // 3, 10 % 3 =", 10 // 3, 10 % 3)   # 3  1

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10.
total = int(input("Total students: "))
absent = int(input("Absent students: "))
passing = int(input("Passing marks: "))
student_marks = int(input("Student's marks: "))

present = total - absent
attendance_pct = present / total * 100
passed = student_marks >= passing
good_attendance = attendance_pct >= 80

print(f"Present students    : {present}")
print(f"Attendance          : {attendance_pct}%")
print(f"Student passed      : {passed}")
print(f"Attendance above 80%: {good_attendance}")

# Q11.
savings = int(input("Your total savings (rupees): "))
owes_zakat = savings >= 50000
zakat_amount = savings * 2.5 / 100
print(f"Savings     : {savings} rupees")
print(f"Owes zakat  : {owes_zakat}")
if owes_zakat:
    print(f"Zakat due   : {zakat_amount} rupees")

# Q12.
pak_score = int(input("Pakistan score: "))
ind_score = int(input("India score: "))
target = int(input("Target to win: "))

print(f"Pakistan score      : {pak_score}")
print(f"India score         : {ind_score}")
print(f"Pakistan wins       : {pak_score > ind_score}")
print(f"Pakistan hit target : {pak_score >= target}")
print(f"Run difference      : {abs(pak_score - ind_score)}")
print(f"Average score       : {(pak_score + ind_score) / 2}")

print()
print("End of solutions.")
