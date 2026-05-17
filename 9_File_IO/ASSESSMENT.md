# Module 9 — File I/O: Assessment

## Pass Criteria

A student passes this module when they can:

- [ ] Create a file and write text to it using `"w"` mode
- [ ] Read a file and print its contents using `"r"` mode
- [ ] Append to an existing file without losing old data using `"a"` mode
- [ ] Handle `FileNotFoundError` with a `try/except` block

---

## Oral Questions

Ask these during the practical assessment or as a class check. Accept answers in Urdu or English.

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | `"w"` aur `"a"` mode mein kya farq hai? | `"w"` purana data delete karta hai, `"a"` end mein add karta hai |
| 2 | `with open()` kya karta hai? | File kholta hai, kaam ke baad automatically band karta hai |
| 3 | Agar file exist nahi kare aur aap read karein toh kya error aata hai? | `FileNotFoundError` |
| 4 | `read()` aur `readlines()` mein kya farq hai? | `read()` poora file ek string mein, `readlines()` list of lines deta hai |
| 5 | Hamesha `with` use kyun karna chahiye? | File automatically close hoti hai, resource leak nahi hota |

---

## Quiz Marking Scheme

**Total: 17 marks**

| Section | Questions | Marks Each | Total |
|---------|-----------|------------|-------|
| Easy | 5 questions | 1 mark | 5 |
| Medium | 3 questions | 2 marks | 6 |
| Complex | 2 questions | 3 marks | 6 |

---

## Grade Scale

| Marks | Grade | Urdu Feedback |
|-------|-------|---------------|
| 15 – 17 | Excellent | Mashallah! Bahut achi tarah samjha |
| 11 – 14 | Good | Wah! Acha kaam kiya |
| 7 – 10 | Pass | Theek hai, thodi aur practice karo |
| 0 – 6 | Needs more work | Koi baat nahi, dobara karte hain |

---

## Practical Assessment Task

### Task: Student Name File Manager

Write a complete Python program that does the following:

1. **Save names** — ask the user to enter student names one by one (until they type `"done"`), and save each name to a file called `students.txt`, one name per line
2. **Read and display** — read `students.txt` and print all names with numbers (1, 2, 3 ...)
3. **Handle missing file** — if `students.txt` does not exist when reading, print a helpful message instead of crashing

**Sample output:**

```
Naam darj karein (done likhein jab khatam ho): Ali
Naam darj karein (done likhein jab khatam ho): Sara
Naam darj karein (done likhein jab khatam ho): Bilal
Naam darj karein (done likhein jab khatam ho): done

--- Saare Students ---
1. Ali
2. Sara
3. Bilal
```

### Marking Rubric — Practical Task

| Criterion | Marks |
|-----------|-------|
| File is created and names are written correctly | 3 |
| Names are read back and printed with numbers | 3 |
| Loop runs until user types "done" | 2 |
| `FileNotFoundError` is handled | 2 |
| **Total** | **10** |

---

## Suggested Timeline

| Activity | Time |
|----------|------|
| Quiz (written) | 15 minutes |
| Practical task | 20 minutes |
| Oral questions (spot-check 3–4 students) | 10 minutes |
| Review and feedback | 5 minutes |

---

## Notes for Teacher

- For the practical, allow students to have the practice sheet open as a reference.
- If a student cannot write the code from scratch, ask them to **explain** what the code should do — partial credit for understanding is valid.
- Students who finish early: ask them to add an **append** feature (add more names without losing old ones).
