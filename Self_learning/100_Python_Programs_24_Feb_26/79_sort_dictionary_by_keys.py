# Program to sort dictionary by keys

print("How many elements?")  # ask size
n = int(input())  # take number

d = {}  # empty dictionary

for i in range(n):  # loop for input
    print("Enter key:")  # ask key
    key = input()  # take key
    
    print("Enter value:")  # ask value
    value = input()  # take value
    
    d[key] = value  # store in dictionary

print("Sorted Dictionary:")  # heading

for k in sorted(d):  # sort keys
    print(k, d[k])  # print sorted data 
    #OUTPUT
    """
    How many elements?
2
Enter key:
a
Enter value:
4
Enter key:
b
Enter value:
6
Sorted Dictionary:
a 4
b 6
"""