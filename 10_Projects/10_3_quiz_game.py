# ================================================
# Module 10 - Capstone Project 3
# QUIZ GAME
# ================================================
# Skills used: lists, dictionaries, functions,
#   loops, if-else, f-strings, file I/O,
#   error handling, input validation
# ================================================

print("=" * 50)
print("         QUIZ GAME")
print("=" * 50)

import os

SCORES_FILE = "quiz_scores.txt"

# ------------------------------------------------
# Question Banks — student picks one topic
# ------------------------------------------------

QUIZ_TOPICS = {
    "1": {
        "name": "Islamic Knowledge",
        "questions": [
            {
                "question": "How many Surahs are in the Quran?",
                "options": ["a) 99", "b) 114", "c) 120", "d) 108"],
                "answer": "b",
                "explanation": "The Quran has 114 Surahs."
            },
            {
                "question": "How many daily prayers are obligatory?",
                "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
                "answer": "c",
                "explanation": "Five daily prayers: Fajr, Dhuhr, Asr, Maghrib, Isha."
            },
            {
                "question": "In which month was the Quran first revealed?",
                "options": ["a) Rajab", "b) Shawwal", "c) Muharram", "d) Ramadan"],
                "answer": "d",
                "explanation": "The Quran was revealed in Ramadan."
            },
            {
                "question": "How many Paras (Juz) are in the Quran?",
                "options": ["a) 25", "b) 28", "c) 30", "d) 32"],
                "answer": "c",
                "explanation": "The Quran has 30 Paras."
            },
            {
                "question": "Which Surah is called the 'Heart of the Quran'?",
                "options": ["a) Al-Fatiha", "b) Al-Baqara", "c) Ya-Sin", "d) Al-Ikhlas"],
                "answer": "c",
                "explanation": "Surah Ya-Sin is called the Heart of the Quran."
            },
        ]
    },
    "2": {
        "name": "Pakistan Geography",
        "questions": [
            {
                "question": "What is the capital of Pakistan?",
                "options": ["a) Lahore", "b) Karachi", "c) Islamabad", "d) Peshawar"],
                "answer": "c",
                "explanation": "Islamabad has been Pakistan's capital since 1967."
            },
            {
                "question": "Which is the largest city of Pakistan by population?",
                "options": ["a) Lahore", "b) Karachi", "c) Islamabad", "d) Faisalabad"],
                "answer": "b",
                "explanation": "Karachi is Pakistan's largest city."
            },
            {
                "question": "What is the capital of Punjab province?",
                "options": ["a) Multan", "b) Faisalabad", "c) Rawalpindi", "d) Lahore"],
                "answer": "d",
                "explanation": "Lahore is the capital of Punjab."
            },
            {
                "question": "Which mountain is the highest peak in Pakistan?",
                "options": ["a) Nanga Parbat", "b) K2", "c) Tirich Mir", "d) Rakaposhi"],
                "answer": "b",
                "explanation": "K2 is the highest peak in Pakistan and 2nd highest in the world."
            },
            {
                "question": "In which year did Pakistan gain independence?",
                "options": ["a) 1945", "b) 1946", "c) 1947", "d) 1948"],
                "answer": "c",
                "explanation": "Pakistan became independent on 14 August 1947."
            },
        ]
    },
    "3": {
        "name": "Python Programming",
        "questions": [
            {
                "question": "Which function prints output in Python?",
                "options": ["a) show()", "b) display()", "c) print()", "d) output()"],
                "answer": "c",
                "explanation": "print() is Python's built-in output function."
            },
            {
                "question": "What does len('Ahmed') return?",
                "options": ["a) 4", "b) 5", "c) 6", "d) Error"],
                "answer": "b",
                "explanation": "'Ahmed' has 5 characters."
            },
            {
                "question": "Which symbol starts a comment in Python?",
                "options": ["a) //", "b) /*", "c) --", "d) #"],
                "answer": "d",
                "explanation": "# starts a comment in Python."
            },
            {
                "question": "What does int('25') do?",
                "options": ["a) Error", "b) Returns '25'", "c) Returns 25", "d) Returns 2.5"],
                "answer": "c",
                "explanation": "int() converts a string to an integer."
            },
            {
                "question": "What keyword is used to define a function?",
                "options": ["a) func", "b) define", "c) function", "d) def"],
                "answer": "d",
                "explanation": "def is used to define functions in Python."
            },
        ]
    }
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
            print("  Invalid! Enter a number.")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Cannot be empty.")

# ------------------------------------------------
# Core Game Functions
# ------------------------------------------------

def show_topics():
    print("\nAvailable topics:")
    for key, topic in QUIZ_TOPICS.items():
        print(f"  {key}. {topic['name']}")

def run_quiz(player_name, topic_key):
    topic = QUIZ_TOPICS[topic_key]
    questions = topic["questions"]
    score = 0

    print(f"\n=== {topic['name']} Quiz ===")
    print(f"Player : {player_name}")
    print(f"Questions: {len(questions)}")
    print("Good luck! Bismillah.\n")

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for option in q["options"]:
            print(f"  {option}")

        answer = input("Your answer (a/b/c/d): ").strip().lower()
        while answer not in ("a", "b", "c", "d"):
            answer = input("  Please enter a, b, c, or d: ").strip().lower()

        if answer == q["answer"]:
            print("  Correct! Ma sha Allah.")
            score += 1
        else:
            print(f"  Wrong. Correct answer: {q['answer'].upper()}")
            print(f"  Explanation: {q['explanation']}")
        print()

    return score

def show_result(player_name, score, total, topic_name):
    percentage = score / total * 100
    print("=" * 40)
    print("       QUIZ RESULT")
    print("=" * 40)
    print(f"Player    : {player_name}")
    print(f"Topic     : {topic_name}")
    print(f"Score     : {score} / {total}")
    print(f"Percentage: {percentage:.0f}%")

    if score == total:
        print("Result    : PERFECT SCORE! Alhamdulillah!")
    elif percentage >= 80:
        print("Result    : Excellent! Ma sha Allah!")
    elif percentage >= 60:
        print("Result    : Good effort. Keep learning!")
    elif percentage >= 40:
        print("Result    : Keep practising. You can do it!")
    else:
        print("Result    : Study more and try again!")
    print("=" * 40)

def save_score(player_name, topic_name, score, total):
    with open(SCORES_FILE, "a") as f:
        f.write(f"{player_name},{topic_name},{score},{total}\n")

def view_leaderboard():
    print("\n--- Leaderboard ---")
    if not os.path.exists(SCORES_FILE):
        print("No scores yet. Play a quiz first!")
        return

    scores = []
    with open(SCORES_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 4:
                name, topic, score, total = parts
                pct = int(score) / int(total) * 100
                scores.append((name, topic, int(score), int(total), pct))

    if not scores:
        print("No scores yet.")
        return

    scores.sort(key=lambda x: x[4], reverse=True)

    print(f"\n{'#':<4} {'Name':<15} {'Topic':<22} {'Score':<8} {'%'}")
    print("-" * 55)
    for i, (name, topic, score, total, pct) in enumerate(scores, 1):
        print(f"{i:<4} {name:<15} {topic:<22} {score}/{total:<5} {pct:.0f}%")

# ------------------------------------------------
# Main Menu
# ------------------------------------------------

def show_menu():
    print("\n" + "=" * 35)
    print("       QUIZ GAME — MENU")
    print("=" * 35)
    print("  1. Play quiz")
    print("  2. View leaderboard")
    print("  3. Exit")
    print("=" * 35)

while True:
    show_menu()
    choice = get_integer_in_range("Choice (1-3): ", 1, 3)

    if choice == 1:
        player_name = get_non_empty("Enter your name: ").title()
        show_topics()
        topic_key = input("Choose topic (1/2/3): ").strip()
        while topic_key not in QUIZ_TOPICS:
            topic_key = input("  Enter 1, 2, or 3: ").strip()

        score = run_quiz(player_name, topic_key)
        total = len(QUIZ_TOPICS[topic_key]["questions"])
        topic_name = QUIZ_TOPICS[topic_key]["name"]

        show_result(player_name, score, total, topic_name)
        save_score(player_name, topic_name, score, total)

    elif choice == 2:
        view_leaderboard()

    elif choice == 3:
        print("\nJazakAllah Khair for playing! Assalamu Alaikum.")
        break
