# ================================================
# Module 10 - Capstone Project 2
# PRAYER TIME REMINDER CLI APP
# ================================================
# Skills used: dictionaries, lists, functions,
#   loops, if-else, f-strings, file I/O,
#   error handling, input validation
# ================================================

print("=" * 50)
print("   PRAYER TIME REMINDER APP")
print("=" * 50)

import os

LOG_FILE = "prayer_log.txt"

PRAYER_SCHEDULE = {
    "Fajr"   : {"time": "05:00", "rakaat": 2},
    "Dhuhr"  : {"time": "13:00", "rakaat": 4},
    "Asr"    : {"time": "16:30", "rakaat": 4},
    "Maghrib": {"time": "19:00", "rakaat": 3},
    "Isha"   : {"time": "21:00", "rakaat": 4},
}

# ------------------------------------------------
# Helper Functions
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
# Feature 1: View today's prayer schedule
# ------------------------------------------------

def show_schedule():
    print("\n--- Today's Prayer Schedule ---")
    print(f"{'Prayer':<10} {'Time':<10} {'Rakaat'}")
    print("-" * 30)
    for prayer, info in PRAYER_SCHEDULE.items():
        print(f"{prayer:<10} {info['time']:<10} {info['rakaat']}")

# ------------------------------------------------
# Feature 2: Check current prayer time
# ------------------------------------------------

def check_current_prayer():
    print("\n--- Current Prayer Check ---")
    hour = get_integer_in_range("Enter current hour (0-23): ", 0, 23)

    schedule_hours = {
        5:  "Fajr",
        13: "Dhuhr",
        16: "Asr",
        19: "Maghrib",
        21: "Isha"
    }

    for h, prayer in schedule_hours.items():
        if hour == h:
            print(f"It is {prayer} time! Please perform your prayer.")
            print(f"Rakaat: {PRAYER_SCHEDULE[prayer]['rakaat']}")
            return
        elif hour == h - 1:
            print(f"{prayer} prayer is in 1 hour. Time: {PRAYER_SCHEDULE[prayer]['time']}")
            return

    print("No prayer due right now. Continue your work.")

# ------------------------------------------------
# Feature 3: Mark prayers offered today
# ------------------------------------------------

def mark_prayers():
    print("\n--- Mark Today's Prayers ---")
    offered = []
    missed = []

    for prayer, info in PRAYER_SCHEDULE.items():
        status = get_yes_no(f"  {prayer} ({info['time']}) — offered? (yes/no): ")
        if status:
            offered.append(prayer)
        else:
            missed.append(prayer)

    # Save to log file
    with open(LOG_FILE, "a") as f:
        offered_str = ",".join(offered) if offered else "none"
        missed_str  = ",".join(missed)  if missed  else "none"
        f.write(f"Offered: {offered_str} | Missed: {missed_str}\n")

    print(f"\nOffered ({len(offered)}/5): {', '.join(offered) if offered else 'None'}")
    print(f"Missed  ({len(missed)}/5) : {', '.join(missed)  if missed  else 'None'}")

    if len(missed) == 0:
        print("Ma sha Allah! All 5 prayers offered. Alhamdulillah!")
    elif len(offered) >= 4:
        print("Almost there! Try to offer all 5 tomorrow.")
    elif len(offered) >= 2:
        print("Good start. Keep improving each day.")
    else:
        print("Please try to offer all prayers. May Allah make it easy.")

# ------------------------------------------------
# Feature 4: View prayer history
# ------------------------------------------------

def view_history():
    print("\n--- Prayer History ---")
    if not os.path.exists(LOG_FILE):
        print("No history yet. Mark your prayers first.")
        return

    with open(LOG_FILE, "r") as f:
        lines = [l.strip() for l in f if l.strip()]

    if not lines:
        print("No history recorded.")
        return

    print(f"Total days recorded: {len(lines)}")
    print()
    for i, line in enumerate(lines, 1):
        print(f"Day {i}: {line}")

# ------------------------------------------------
# Feature 5: Prayer statistics
# ------------------------------------------------

def show_statistics():
    print("\n--- Prayer Statistics ---")
    if not os.path.exists(LOG_FILE):
        print("No data yet.")
        return

    prayer_counts = {p: 0 for p in PRAYER_SCHEDULE}
    days = 0

    with open(LOG_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            days += 1
            if "Offered:" in line:
                offered_part = line.split("|")[0].replace("Offered:", "").strip()
                if offered_part != "none":
                    for prayer in offered_part.split(","):
                        prayer = prayer.strip()
                        if prayer in prayer_counts:
                            prayer_counts[prayer] += 1

    if days == 0:
        print("No data recorded.")
        return

    print(f"Days tracked: {days}")
    print(f"\n{'Prayer':<10} {'Offered':>8} {'Rate':>8}")
    print("-" * 30)
    for prayer, count in prayer_counts.items():
        rate = count / days * 100
        print(f"{prayer:<10} {count:>8} {rate:>7.0f}%")

# ------------------------------------------------
# Main Menu
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
