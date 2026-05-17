# Module 9 — File I/O: Practice Sheet

**Naam / Name:** _______________________  
**Taareekh / Date:** _______________________  
**Class:** _______________________

---

> **Yaad rakhein:** File modes — `"r"` (read), `"w"` (write, overwrites!), `"a"` (append)  
> **Remember:** Always use `with open(...) as f:` — it closes the file automatically.

---

## Section A — Short Questions

**Q1.** File ko sirf parhne (reading only) ke liye kaunsa mode use hota hai?

```
Jawab: _______________________
```

---

**Q2.** `"w"` aur `"a"` mode mein kya farq hai? Urdu ya English mein likho.

```
Jawab:
_______________________________________________
_______________________________________________
```

---

**Q3.** Yeh code likho: ek file `"salam.txt"` banao aur usme `"Assalamu Alaikum"` likho.

```python
# Yahan apna code likho:




```

---

**Q4.** Yeh code likho: `"salam.txt"` file paro aur uska content print karo.

```python
# Yahan apna code likho:




```

---

**Q5.** `with open()` use kyun karna chahiye sirf `open()` ki jagah? Ek wajah batao.

```
Jawab:
_______________________________________________
```

---

**Q6.** Kya error aata hai agar aap aisi file read karne ki koshish karo jo exist nahi karti?

```
Jawab: _______________________
```

---

## Section B — Code Writing

**Q7.** Yeh code likho: ek existing file `"dua.txt"` ke end mein `"JazakAllah Khair"` add karo (purana content na mithe).

```python
# Yahan apna code likho:




```

---

**Q8.** Neeche wala code galat hai. Galtiyan dhundo aur theek karo:

```python
# GALAT CODE:
f = open("data.txt")
data = f.read()
print(data)
```

**Galtiyan (mistakes):**
1. _______________________________________________
2. _______________________________________________

**Theek kiya hua code:**

```python
# THEEK CODE:




```

---

**Q9.** Yeh code likho: teen Pakistani shehar (cities) ki list bana ke file mein save karo — har shehar ek alag line mein.

```python
# Hint: cities = ["Karachi", "Lahore", "Islamabad"]
# Yahan apna code likho:




```

---

## Section C — Challenge Question

**Challenge:** Ek **persistent naam collector** banao.

Program ke rules:
- Har baar run hone par, user se ek naam maango
- Woh naam file `"names.txt"` mein **add** karo (purane naam na mitten)
- Phir file ke **saare naam** numbered list mein print karo

**Expected output (2nd run ke baad):**

```
Apna naam darj karein: Fatima

--- Ab tak ke saare naam ---
1. Ali
2. Fatima
```

```python
# Yahan apna code likho:




```

---

## Mutaliq Maloomat (Quick Reference)

```python
# File likhna (naya banao)
with open("file.txt", "w") as f:
    f.write("Bismillah\n")

# File parhna
with open("file.txt", "r") as f:
    content = f.read()

# File mein add karna
with open("file.txt", "a") as f:
    f.write("Naya data\n")

# Error handle karna
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File nahi mili!")
```

---

*Module 9 — File I/O | ISDP Python Course*
