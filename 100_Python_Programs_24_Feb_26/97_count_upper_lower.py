# Program to count uppercase and lowercase letters

print("Enter a string:")  # message
s = input()  # take string

upper = 0  # counter
lower = 0  # counter

for ch in s:  # loop characters
    if ch.isupper():  # uppercase check
        upper += 1
    elif ch.islower():  # lowercase check
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
#OUTPUT
"""
Count
Uppercase letters: 1
Lowercase letters: 4
"""