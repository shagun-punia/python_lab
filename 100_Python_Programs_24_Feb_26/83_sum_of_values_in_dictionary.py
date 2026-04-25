# Program to find sum of values in dictionary

print("How many elements?")  # ask size
n = int(input())  # take number

d = {}  # empty dictionary

for i in range(n):  # loop for input
    print("Enter key:")  # ask key
    key = input()  # take key
    
    print("Enter value (number only):")  # ask value
    value = int(input())  # take value as integer
    
    d[key] = value  # store in dictionary

total = 0  # variable to store sum

for v in d.values():  # loop through values
    total = total + v  # add each value

print("Sum of all values is:", total)  # print result
#OUTPUT
"""
How many elements?
2
Enter key:
a
Enter value (number only):
6
Enter key:
b
Enter value (number only):
3
Sum of all values is: 9
"""