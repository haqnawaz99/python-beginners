# ================================================
# Module 10 - Capstone Project 2
# PRAYER TIME REMINDER — STARTER FILE
# ================================================
# Give this file to students.
# Full solution: 10_2_prayer_reminder.py
# ================================================

print("=" * 50)
print("   PRAYER TIME REMINDER APP")
print("=" * 50)

import os

LOG_FILE = "prayer_log.txt"

# Prayer schedule — already provided
PRAYER_SCHEDULE = {
    "Fajr"   : {"time": "05:00", "rakaat": 2},
    "Dhuhr"  : {"time": "13:00", "rakaat": 4},
    "Asr"    : {"time": "16:30", "rakaat": 4},
    "Maghrib": {"time": "19:00", "rakaat": 3},
    "Isha"   : {"time": "21:00", "rakaat": 4},
}

# ------------------------------------------------
# Helper Functions — already done for you
# ------------------------------------------------

def get_integer_in_range(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"  Enter between {minimum} and {maximum}.")
        except ValueError:
            print("  Invalid! Enter a whole number.")

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("yes", "no", "y", "n"):
            return ans in ("yes", "y")
        print("  Please enter yes or no.")

# ------------------------------------------------
# TODO 1: Write show_schedule()
# Print a table with Prayer, Time, Rakaat
# Use PRAYER_SCHEDULE dictionary
# ------------------------------------------------

def show_schedule():
    print("\n--- Today's Prayer Schedule ---")
    pass  # replace with your code


# ------------------------------------------------
# TODO 2: Write check_current_prayer()
# Steps:
#   1. Ask user for current hour (0-23)
#   2. Check if it matches a prayer time
#   3. Print prayer name and rakaat if it's prayer time
#   4. Print upcoming prayer if 1 hour away
#   5. Print "No prayer due right now" otherwise
# Hint: Fajr=5, Dhuhr=13, Asr=16, Maghrib=19, Isha=21
# ------------------------------------------------

def check_current_prayer():
    print("\n--- Current Prayer Check ---")
    pass  # replace with your code


# ------------------------------------------------
# TODO 3: Write mark_prayers()
# Steps:
#   1. Loop through each prayer
#   2. Ask yes/no if it was offered
#   3. Keep track of offered and missed lists
#   4. Save result to LOG_FILE
#   5. Print summary with encouragement message
# ------------------------------------------------

def mark_prayers():
    print("\n--- Mark Today's Prayers ---")
    pass  # replace with your code


# ------------------------------------------------
# TODO 4: Write view_history()
# Steps:
#   1. Check if LOG_FILE exists
#   2. Read and print each line numbered as "Day 1:", "Day 2:", etc.
# ------------------------------------------------

def view_history():
    print("\n--- Prayer History ---")
    pass  # replace with your code


# ------------------------------------------------
# TODO 5: Write show_statistics()
# Steps:
#   1. Read LOG_FILE
#   2. Count how many times each prayer was offered
#   3. Print a table: Prayer | Offered | Rate%
# ------------------------------------------------

def show_statistics():
    print("\n--- Prayer Statistics ---")
    pass  # replace with your code


# ------------------------------------------------
# Main Menu — already done for you
# ------------------------------------------------

def show_menu():
    print("\n" + "=" * 35)
    print("   PRAYER REMINDER APP — MENU")
    print("=" * 35)
    print("  1. Today's prayer schedule")
    print("  2. Check current prayer time")
    print("  3. Mark today's prayers")
    print("  4. View prayer history")
    print("  5. Prayer statistics")
    print("  6. Exit")
    print("=" * 35)

while True:
    show_menu()
    choice = get_integer_in_range("Choice (1-6): ", 1, 6)
    if choice == 1:
        show_schedule()
    elif choice == 2:
        check_current_prayer()
    elif choice == 3:
        mark_prayers()
    elif choice == 4:
        view_history()
    elif choice == 5:
        show_statistics()
    elif choice == 6:
        print("\nAssalamu Alaikum! May Allah accept your prayers. Ameen.")
        break
