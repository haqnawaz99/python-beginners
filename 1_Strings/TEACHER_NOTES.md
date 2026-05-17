# Module 1 — Strings: Teacher Notes

## Duration
2 classes (45–60 minutes each)

## Learning Objectives
By end of module, students can:
1. Concatenate strings using +
2. Get user input with input()
3. Understand the difference between str and int input
4. Use len() to find string length

## Lesson Flow

### Class 1
| Time | Activity |
|------|----------|
| 0–15 min | Revise Module 0 — run a print() together |
| 15–30 min | 1_1_string_concatenation.py — joining strings with + |
| 30–45 min | 1_2_string_concatenation_urdu.py — Urdu examples |
| 45–55 min | Practice concatenation exercises |

### Class 2
| Time | Activity |
|------|----------|
| 0–15 min | 1_3_user_input.py — input() function |
| 15–30 min | Show how input() always returns a string |
| 30–45 min | Quiz (0_4_quiz.py) |
| 45–55 min | Review answers |

## Key Concept to Emphasize
`input()` always returns a STRING — even if the user types 25, Python sees "25".
This will matter in Module 3 when we learn int().

## Common Mistakes to Watch
- `"Ahmed" + " " + "Khan"` — forgetting the space between names
- Trying to add a number to a string: `"Age: " + 15` → TypeError
- input() result not stored: `input("Name: ")` without `name =`

## Tips for Urdu Delivery
- "String matlab text — jaise SMS mein type karte hain"
- "Plus ka matlab yahan jodo — jaise words ko saath likhna"
- Show name concatenation: `"Muhammad" + " " + "Ahmed"` — students love seeing their own names

## Files in This Module
- 1_0_introduction.py
- 1_1_string_concatenation.py
- 1_2_string_concatenation_urdu.py
- 1_3_user_input.py
- 1_4_quiz.py
- 1_5_quiz_solution.py
