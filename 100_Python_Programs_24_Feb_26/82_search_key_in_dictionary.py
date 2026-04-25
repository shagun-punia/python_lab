# Program to search a key in dictionary

print("How many elements?")  # ask size
n = int(input())  # take number

d = {}  # empty dictionary

for i in range(n):  # loop for input
    print("Enter key:")  # ask key
    key = input()  # take key
    
    print("Enter value:")  # ask value
    value = input()  # take value
    
    d[key] = value  # store in dictionary

print("Enter key to search:")  # ask search key
search_key = input()  # take key

if search_key in d:  # check if key exists
    print("Key found")
    print("Value is:", d[search_key])  # print value
else:
    print("Key not found")
    #OUTPUT
    """
    How many elements?
2
Enter key:
a
Enter value:
78
Enter key:
b
Enter value:
7
Enter key to search:
c
Key not found
"""