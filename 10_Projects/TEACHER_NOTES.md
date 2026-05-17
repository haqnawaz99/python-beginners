# Module 10 — Projects: Teacher Notes

## Duration
3 classes (1 project per class; allow 1.5 classes for slower groups)

---

## Learning Objectives

By the end of this module, students will be able to:

- Build **3 complete Python applications** that combine all skills from Modules 0–9
- Understand real-world program structure: menus, functions, file I/O, and input validation
- Read and understand an existing codebase (starter file), then extend it
- Test their own programs with valid and invalid inputs

---

## Projects Overview

| Class | File | Project |
|-------|------|---------|
| Class 1 | `10_1_report_card_system.py` | Report Card System |
| Class 2 | `10_2_prayer_reminder.py` | Prayer Reminder |
| Class 3 | `10_3_quiz_game.py` | Quiz Game |

---

## Lesson Flow

### Class 1 — Report Card System

**`10_1_report_card_system.py`**

1. Open the **solution file** and run it — let students see the finished product.
2. Show the **starter file** — point out the incomplete functions.
3. Explain the structure: menu loop → function call → file I/O.
4. Students complete the starter file by filling in the functions.
5. Run and test together — try adding a student, viewing all, searching by name.

**What to highlight:**
- How the menu uses a `while True` loop with `if/elif`
- How each menu option calls a separate function
- How `FileNotFoundError` is handled when no data file exists yet

---

### Class 2 — Prayer Reminder

**`10_2_prayer_reminder.py`**

This project is more complex. Demonstrate it fully before students begin.

1. Run the solution — explain what each menu option does.
2. Discuss: why would a Muslim family find this useful?
3. Show the starter file — students fill in the statistics and marking functions.
4. Guide weaker students to complete at least the "view schedule" and "mark prayer" features.
5. Stronger students: challenge them to add a feature to view only missed prayers.

**What to highlight:**
- Using a dictionary to store prayer times
- Appending records to a file with date and status
- Calculating percentage from saved data

---

### Class 3 — Quiz Game

**`10_3_quiz_game.py`**

The most complex project. Consider a **group activity** option for this class.

1. Run the solution — let students play the quiz.
2. Show how questions are stored (list of dictionaries).
3. Students complete the: score calculation, save-to-leaderboard, and display-leaderboard functions.
4. **Group option:** pairs of students work together, one reads the code, one types.
5. End of class: each student plays the finished quiz and sees their name on the leaderboard.

**What to highlight:**
- Input validation loop (keep asking until a/b/c/d is entered)
- How the leaderboard file grows with each game
- How to add a new topic by adding to the questions list

---

## Teaching Approach — For All Three Projects

Follow this sequence for each project:

```
1. Show the SOLUTION running       → "Yeh hamara target hai"
2. Open the STARTER file           → "Yahan se shuru karte hain"
3. Explain what is missing         → "Yeh functions khaali hain"
4. Students fill in the blanks     → Guided practice
5. Run and test together           → "Chalaate hain, dekhte hain"
6. Try bad inputs                  → "Kya hoga agar galat likhein?"
```

---

## Common Mistakes to Watch For

1. **Not passing arguments to functions** — students define `def add_student():` but call it with data — show the difference between parameters and no parameters.
2. **Not calling functions from the menu** — students write the function but forget to connect it to the menu option.
3. **File path issues** — remind students to run the program from the correct folder, or the data file will be created in the wrong place.
4. **Modifying the solution file instead of the starter** — keep both files open side by side.
5. **Skipping input validation** — students think the program works because they tested it with correct inputs only.

---

## Urdu Teaching Tips

- **Opening motivation:** "Yeh sab cheezein jo humne seekhi hain — variables, loops, functions, files — ab sab milaate hain. Ek real software banaate hain!"
- **On starter files:** "Kuch cheezein maine already likh di hain. Aap ko sirf khaali jagah bharna hai — jaise imtihan mein fill in the blanks."
- **On testing with bad input:** "Agar user galat data daale, program toot jaana nahi chahiye. Isliye hum pehle check karte hain."
- **On real-world relevance:** "Yeh programs ASLI data save karte hain. Jab aap chalaaenge, real .txt files banenge aapke computer pe."

---

## Important Reminder for Students

> These programs **save data to files**. Running them creates real `.txt` files in the same folder. Show students where these files appear and how to open them in Notepad to see the saved data.

---

## Files in This Module

| File | Description |
|------|-------------|
| `10_1_report_card_system_starter.py` | Starter file — students complete this |
| `10_1_report_card_system_solution.py` | Full working solution |
| `10_2_prayer_reminder_starter.py` | Starter file |
| `10_2_prayer_reminder_solution.py` | Full working solution |
| `10_3_quiz_game_starter.py` | Starter file |
| `10_3_quiz_game_solution.py` | Full working solution |

---

## Differentiation

| Student Level | Approach |
|---------------|----------|
| Struggling | Focus on running and understanding the solution; complete only 1–2 functions in the starter |
| On track | Complete all functions in the starter file |
| Advanced | Extend the project (see Extension Questions in practice_sheet.md) |
