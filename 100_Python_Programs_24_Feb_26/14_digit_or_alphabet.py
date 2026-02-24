# Program to check whether a character is digit or alphabet

ch = input("Enter a character: ")

if ch.isdigit():
    result = "It is a Digit."
elif ch.isalpha():
    result = "It is an Alphabet."
else:
    result = "It is neither Digit nor Alphabet."

print("\n----- Output -----")
print("Character Entered:", ch)
print(result)
#OUTPUT
"""Enter a character: 23

----- Output -----   
Character Entered: 23
It is a Digit."""