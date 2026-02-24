# Program to remove duplicate characters

print("Enter a string:")  # message
s = input()  # take string

result = ""  # empty string

for ch in s:  # loop characters
    if ch not in result:  # check duplicate
        result += ch  # add character

print("String after removing duplicates:")
print(result)
#OUTPUT
"""
Enter a string:
moon
String after removing duplicates:
mon
"""