# Reverse a string

text = input("Enter a string: ")  # input
rev = ""  # store reverse

print("\n----- Output -----")
for ch in text:  # loop through string
    rev = ch + rev  # build reverse string

print("Reversed string is:", rev)  # print result

#OUTPUT
"""
Enter a string: shagun

----- Output -----        
Reversed string is: nugahs
"""