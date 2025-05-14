# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def count_cases (sentence):
    uppercase = sum (1 for char in sentence if char.isupper())
    lowercase = sum ( 1 for char in sentence if char.islower())

    return uppercase, lowercase

text = "I love Nación Sushi"
uppercase, lowercase = count_cases (text)
print ( f'In this sentence we have: {uppercase} upper cases, and {lowercase} lower cases')


#__________________________________________________________________________________

# 3. Using collections.Counter (Advanced)
# If you want to count letters in a more structured way, use Counter:

from collections import Counter

def count_cases(sentence):
    counts = Counter("upper" if c.isupper() else "lower" if c.islower() else "other" for c in sentence)
    return counts["upper"], counts["lower"]

text = "Welcome to Python!"
upper, lower = count_cases(text)
print(f"Uppercase: {upper}, Lowercase: {lower}")

# Output: Uppercase: 2, Lowercase: 13
