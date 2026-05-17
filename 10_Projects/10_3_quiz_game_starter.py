# ================================================
# Module 10 - Capstone Project 3
# QUIZ GAME — STARTER FILE
# ================================================
# Give this file to students.
# Full solution: 10_3_quiz_game.py
# ================================================

print("=" * 50)
print("         QUIZ GAME")
print("=" * 50)

import os

SCORES_FILE = "quiz_scores.txt"

# Question banks — already provided, do not change
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
            print("  Invalid! Enter a number.")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Cannot be empty.")

# ------------------------------------------------
# TODO 1: Write show_topics()
# Print all available topics from QUIZ_TOPICS
# Format: "  1. Islamic Knowledge"
# ------------------------------------------------

def show_topics():
    print("\nAvailable topics:")
    pass  # replace with your code


# ------------------------------------------------
# TODO 2: Write run_quiz(player_name, topic_key)
# Steps:
#   1. Get the topic and its questions from QUIZ_TOPICS
#   2. Print quiz header (topic name, player name, number of questions)
#   3. Loop through questions:
#      a. Print question number and text
#      b. Print all options
#      c. Get answer (a/b/c/d) — validate it
#      d. Check if correct — update score
#      e. Print correct/wrong feedback and explanation
#   4. Return final score
# ------------------------------------------------

def run_quiz(player_name, topic_key):
    topic = QUIZ_TOPICS[topic_key]
    questions = topic["questions"]
    score = 0

    print(f"\n=== {topic['name']} Quiz ===")
    print(f"Player : {player_name}")
    print(f"Questions: {len(questions)}")
    print("Good luck! Bismillah.\n")

    # TODO: loop through questions, ask each one, check answer
    pass  # replace with your code

    return score


# ------------------------------------------------
# TODO 3: Write show_result(player_name, score, total, topic_name)
# Print a result box showing:
#   - Player name, topic, score (x/5), percentage
#   - Message based on percentage:
#     100% → "PERFECT SCORE! Alhamdulillah!"
#     >=80% → "Excellent! Ma sha Allah!"
#     >=60% → "Good effort. Keep learning!"
#     >=40% → "Keep practising. You can do it!"
#     else  → "Study more and try again!"
# ------------------------------------------------

def show_result(player_name, score, total, topic_name):
    pass  # replace with your code


# ------------------------------------------------
# TODO 4: Write save_score(player_name, topic_name, score, total)
# Append to SCORES_FILE in format:
#   player_name,topic_name,score,total
# ------------------------------------------------

def save_score(player_name, topic_name, score, total):
    pass  # replace with your code


# ------------------------------------------------
# TODO 5: Write view_leaderboard()
# Steps:
#   1. Check if SCORES_FILE exists
#   2. Read all scores and calculate percentage
#   3. Sort by percentage (highest first)
#   4. Print numbered table: #, Name, Topic, Score, %
# ------------------------------------------------

def view_leaderboard():
    print("\n--- Leaderboard ---")
    pass  # replace with your code


# ------------------------------------------------
# Main Menu — already done for you
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
