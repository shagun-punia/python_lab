# Program to replace all vowels with *

print("Enter a string:")  # message for user
s = input()  # take string

result = ""  # empty string

for ch in s:  # check each character
    if ch.lower() in "aeiou":  # if vowel
        result += "*"  # replace with *
    else:
        result += ch  # keep same

print("Output after replacing vowels:")  # output message
print(result)  # print result
#OUTPUT
"""
Enter a string:
ramshyam
Output after replacing vowels:
r*mshy*m
"""