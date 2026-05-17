# Module 3 — Data Types: Practice Sheet

**Naam (Name): ___________________________**
**Taareekh (Date): ________________________**
**Class: _________________________________**

---

Bismillah ir-Rahman ir-Raheem

Yeh practice sheet Module 3 ke liye hai. Har sawaal ko dhyan se parho aur jawab likhein.

---

## Section A — Short Answer (Mukhtasar Jawabaat)

**Q1.** `type(3.14)` kya return karega? Circle the correct answer.

```
a) <class 'int'>
b) <class 'float'>
c) <class 'str'>
d) <class 'bool'>
```

**Jawab: _______________**

---

**Q2.** Neeche wala code galat hai. Galti dhoondho aur theek karo.

```python
# Galat code:
age = int("Ahmed")
print(age)
```

**Galti kya hai?**

```
_____________________________________________
_____________________________________________
```

**Theek code likhein:**

```python
# Sahi code:
age = ___________________________________
```

---

**Q3.** Agar `name = "Ahmed"` ho, toh neeche wali f-string ka output kya hoga?

```python
print(f"Assalamu Alaikum {name}")
```

**Output: _______________________________________________**

---

**Q4.** User se umar poochho aur use integer ke tor par store karo. Code likhein:

```python
# Yahan apna code likhein:
umar = ___________________________________
```

---

**Q5.** Neeche wala calculation kya result dega?

```python
result = int("25") + int("10")
print(result)
```

**Result: _______________**

---

**Q6.** `99` ko string mein convert karo `str()` use karke:

```python
number = 99
text = ___________________________________
print(type(text))  # <class 'str'> aana chahiye
```

---

## Section B — Writing Code (Code Likhna)

**Q7.** Ek f-string likhein jo yeh print kare:
> **Ahmed is 15 years old**

```python
naam = "Ahmed"
umar = 15

print(  ________________________________  )
```

---

**Q8.** Samjhao — `int(input())` kyun use karte hain jab user se number lena ho? (Apni zaban mein likhein)

```
_____________________________________________
_____________________________________________
_____________________________________________
```

---

## Section C — Fix the Bug (Galti Theek Karo)

**Q9.** Neeche ke code mein kya galat hai? Theek karo.

```python
# Galat:
naam = "Fatima"
city = "Lahore"
print("Main {naam} hoon aur {city} mein rehti hoon.")
```

**Galti: _______________________________________________**

**Sahi code:**

```python
print(  ________________________________  )
```

---

**Q10.** Yeh code crash karta hai. Kyun? Aur kaise theek karein?

```python
saal = input("Paidaishi saal likhein: ")
umar = 2026 - saal
print(umar)
```

**Kyun crash hota hai:**

```
_____________________________________________
```

**Theek code:**

```python
saal = ___________________________________
umar = 2026 - saal
print(f"Aap ki umar hai: {umar}")
```

---

## Challenge — Mushkil Sawaal

Ahmed, Hassan, aur Zainab ne ek program banana chaha jo do numbers user se le aur unka total print kare. Pura program likhein:

**Requirements:**
- User se pehla number lo (integer)
- User se doosra number lo (integer)
- Dono numbers add karo
- Result f-string se print karo
- Example output: `Ahmed ki calculation: 25 + 10 = 35`

```python
# Apna program yahan likhein:




```

---

## Answer Key (Sirf Teacher ke liye)

| Sawaal | Jawab |
|--------|-------|
| Q1 | `b) <class 'float'>` |
| Q2 | `int("Ahmed")` galat hai — sirf numeric strings convert ho sakti hain. `age = int("15")` ya `age = int(input(...))` |
| Q3 | `Assalamu Alaikum Ahmed` |
| Q4 | `umar = int(input("Apni umar likhein: "))` |
| Q5 | `35` |
| Q6 | `text = str(99)` |
| Q7 | `print(f"{naam} is {umar} years old")` |
| Q8 | Kyunki `input()` hamesha string return karta hai, math ke liye `int()` mein convert karna zaroori hai |
| Q9 | `f` prefix missing hai. Sahi: `print(f"Main {naam} hoon aur {city} mein rehti hoon.")` |
| Q10 | `saal` string hai, integer se subtract nahin ho sakta. `saal = int(input(...))` |
| Challenge | `n1 = int(input(...))`, `n2 = int(input(...))`, `print(f"... {n1} + {n2} = {n1+n2}")` |
