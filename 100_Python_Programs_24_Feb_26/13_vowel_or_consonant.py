# Program to check whether a character is vowel or consonant

ch = input("Enter a character: ")

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    result = "It is a Vowel."
else:
    result = "It is a Consonant."

print("\n----- Output -----")
print("Character Entered:", ch)
print(result)

#OUTPUT
"""Enter a character: t

----- Output -----  
Character Entered: t
It is a Consonant."""