# Program to find first non-repeating character

print("Enter a string:")  # message
s = input()  # take string

found = False  # flag

for ch in s:  # loop characters
    if s.count(ch) == 1:  # check frequency
        print("First non-repeating character is:", ch)
        found = True
        break

if found == False:  # if none found
    print("No non-repeating character found")
    #OUTPUT
    """
    Enter a string:
soon
First non-repeating character is: s
"""