# Module 9 — File I/O: Practice Sheet

**Name:** _______________________  
**Date:** _______________________  
**Class:** _______________________

---

> **Remember:** File modes — `"r"` (read), `"w"` (write, overwrites!), `"a"` (append)  
> **Remember:** Always use `with open(...) as f:` — it closes the file automatically.

---

## Section A — Short Questions

**Q1.** Which mode is used to open a file for reading only?

```
Answer: _______________________
```

---

**Q2.** What is the difference between `"w"` and `"a"` mode? Write in English.

```
Answer:
_______________________________________________
_______________________________________________
```

---

**Q3.** Write the code to create a file `"salam.txt"` and write `"Assalamu Alaikum"` into it.

```python
# Write your code here:




```

---

**Q4.** Write the code to read `"salam.txt"` and print its contents.

```python
# Write your code here:




```

---

**Q5.** Give one reason why you should use `with open()` instead of just `open()`.

```
Answer:
_______________________________________________
```

---

**Q6.** What error occurs if you try to read a file that does not exist?

```
Answer: _______________________
```

---

## Section B — Code Writing

**Q7.** Write code to add `"JazakAllah Khair"` to the end of an existing file `"dua.txt"` without deleting the old content.

```python
# Write your code here:




```

---

**Q8.** The code below has mistakes. Find them and fix them:

```python
# WRONG CODE:
f = open("data.txt")
data = f.read()
print(data)
```

**Mistakes:**
1. _______________________________________________
2. _______________________________________________

**Fixed code:**

```python
# CORRECT CODE:




```

---

**Q9.** Write code to save a list of three Pakistani cities to a file — one city per line.

```python
# Hint: cities = ["Karachi", "Lahore", "Islamabad"]
# Write your code here:




```

---

## Section C — Challenge Question

**Challenge:** Build a **persistent name collector**.

Program rules:
- Each time it runs, ask the user for a name
- Add that name to the file `"names.txt"` (do not delete old names)
- Then print all names from the file as a numbered list

**Expected output (after 2nd run):**

```
Apna naam darj karein: Fatima

--- All names so far ---
1. Ali
2. Fatima
```

```python
# Write your code here:




```

---

## Quick Reference

```python
# Write to a new file
with open("file.txt", "w") as f:
    f.write("Bismillah\n")

# Read a file
with open("file.txt", "r") as f:
    content = f.read()

# Append to a file
with open("file.txt", "a") as f:
    f.write("Naya data\n")

# Handle missing file error
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File nahi mili!")
```

---

*Module 9 — File I/O | ISDP Python Course*
