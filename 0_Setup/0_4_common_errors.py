# ================================================
# Module 0 - Lesson 4: Common Errors
# ================================================
# Learn: What errors look like, how to read them,
#        and how to fix the 3 most common ones
# ================================================

# ------------------------------------------------
# Errors are NORMAL - do not be afraid!
# ------------------------------------------------
# Every programmer sees errors. Even experts.
# An error means Python found something it cannot understand.
# Python tells you WHAT went wrong and WHERE.
# Read the error message - it is helping you!

# ------------------------------------------------
# Error Type 1: SyntaxError
# ------------------------------------------------
# Syntax means the rules of writing Python.
# A SyntaxError means you broke a rule.
# Most common cause: missing bracket, missing quote.

# WRONG - missing closing quote:
# print("Assalamu Alaikum)
# Error: SyntaxError: EOL while scanning string literal

# WRONG - missing closing bracket:
# print("Hello"
# Error: SyntaxError: unexpected EOF while parsing

# CORRECT:
print("Assalamu Alaikum")
print("Hello")

# ------------------------------------------------
# Error Type 2: NameError
# ------------------------------------------------
# A NameError means you used a word Python does not know.
# Most common cause: typo in a function name.

# WRONG - typo: 'Print' should be 'print' (lowercase p)
# Print("Hello")
# Error: NameError: name 'Print' is not defined

# WRONG - typo in function name
# priint("Hello")
# Error: NameError: name 'priint' is not defined

# CORRECT - Python is case sensitive, always lowercase 'print'
print("No errors here!")

# ------------------------------------------------
# Error Type 3: IndentationError
# ------------------------------------------------
# Python uses spaces/indentation to organize code.
# We will see this more when we learn if/loops.
# For now: do NOT add extra spaces at the start of a line.

# WRONG - unexpected indent:
# print("Hello")
#     print("Indented by mistake")
# Error: IndentationError: unexpected indent

# CORRECT - all basic statements start at the left edge
print("Line 1")
print("Line 2")

# ------------------------------------------------
# How to READ an error message
# ------------------------------------------------
# When you see an error, look for:
# 1. The FILE name - which file has the error
# 2. The LINE number - which line caused it
# 3. The ERROR TYPE - SyntaxError, NameError, etc.
# 4. The MESSAGE - description of the problem

# Example error message:
#   File "0_4_common_errors.py", line 45, in <module>
#     Print("Hello")
#   NameError: name 'Print' is not defined
#
# This tells us: line 45, we wrote 'Print' but it should be 'print'

# ------------------------------------------------
# Golden Rule
# ------------------------------------------------
# When you see an error:
# Step 1 - Do NOT panic
# Step 2 - Read the error message carefully
# Step 3 - Find the line number it mentions
# Step 4 - Fix the mistake
# Step 5 - Run again

print()
print("Errors are your teacher - they show you exactly what to fix!")
print("Every expert programmer fixes errors every single day.")
