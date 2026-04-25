# Program to compress string using character counts

print("Enter a string:")  # message
s = input()  # take string

result = ""  # result string
count = 1  # counter

for i in range(1, len(s)):  # loop string
    if s[i] == s[i-1]:  # same character
        count += 1
    else:
        result += s[i-1] + str(count)  # add char + count
        count = 1  # reset

result += s[-1] + str(count)  # last character

print("Compressed string:")
print(result)
#OUTPUT
"""
Enter a string:
programs
Compressed string:
p1r1o1g1r1a1m1s1  
"""