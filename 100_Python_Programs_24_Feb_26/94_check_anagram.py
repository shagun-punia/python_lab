# Program to check whether two strings are anagrams

print("Enter first string:")  # message
s1 = input()  # first string

print("Enter second string:")  # message
s2 = input()  # second string

if sorted(s1) == sorted(s2):  # compare sorted strings
    print("Output: Anagrams")
else:
    print("Output: Not Anagrams")
    #output
    """
    Enter first string:
listen
Enter second string:
silent
Output: Anagrams
"""