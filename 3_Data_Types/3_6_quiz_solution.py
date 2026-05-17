# ================================================
# Module 3 - Quiz Solutions
# ================================================

print("=" * 50)
print("MODULE 3 QUIZ - SOLUTIONS")
print("=" * 50)
print()

# ------------------------------------------------
# EASY
# ------------------------------------------------
print("--- EASY ---")
print()

# Q1.
print(type(42))          # int
print(type(3.14))        # float
print(type("Lahore"))    # str
print(type(True))        # bool

# Q2.
student_count = 40
price = 99.5
city = "Karachi"
print(student_count, type(student_count))
print(price, type(price))
print(city, type(city))

# Q3.
result = int("786") + 14
print(result)            # 800

# Q4.
print("Pakistan was created in " + str(1947))

# Q5.
name = "Fatima"
print(f"Welcome {name} to Python class!")

# ------------------------------------------------
# MEDIUM
# ------------------------------------------------
print()
print("--- MEDIUM ---")
print()

# Q6.
a = int(input("First number: "))
b = int(input("Second number: "))
print(f"Sum        : {a + b}")
print(f"Difference : {a - b}")
print(f"Product    : {a * b}")

# Q7.
name = input("Your name: ")
marks = float(input("Your marks: "))
print(f"{name} scored {marks} marks. Well done!")

# Q8. Fix: prayers is int, cannot use + with string
# WRONG: print("We pray " + prayers + " times a day.")
prayers = 5
# FIXED option 1:
print("We pray " + str(prayers) + " times a day.")
# FIXED option 2:
print(f"We pray {prayers} times a day.")

# Q9.
price = float(input("Price per item (rupees): "))
qty = int(input("Quantity: "))
total = price * qty
print(f"{qty} items at {price} rupees each = {total} rupees total")

# ------------------------------------------------
# COMPLEX
# ------------------------------------------------
print()
print("--- COMPLEX ---")
print()

# Q10.
name = input("Your name: ")
age = int(input("Your age: "))
marks = float(input("Your marks out of 100: "))
percentage = marks
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Marks   : {marks} / 100")
print(f"Result  : {percentage}%")

# Q11.
total = int(input("Total students: "))
absent = int(input("Absent students: "))
present = total - absent
attendance = present / total * 100
print(f"Present           : {present} out of {total}")
print(f"Attendance        : {attendance}%")

# Q12.
item = input("Item name: ")
price = float(input("Price per kg: "))
qty = float(input("Quantity in kg: "))
discount = int(input("Discount (rupees): "))
subtotal = price * qty
total = subtotal - discount
print("==============================")
print("SHOP RECEIPT")
print("==============================")
print(f"Item      : {item}")
print(f"Price/kg  : {price} rupees")
print(f"Quantity  : {qty} kg")
print(f"Subtotal  : {subtotal} rupees")
print(f"Discount  : {discount} rupees")
print(f"Total     : {total} rupees")
print("==============================")
print("Jazakallah Khair!")

print()
print("End of solutions.")
