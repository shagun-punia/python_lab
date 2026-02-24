# Program to sort dictionary by values

print("How many elements?")  # ask size
n = int(input())  # take number

d = {}  # empty dictionary

for i in range(n):  # loop for input
    print("Enter key:")  # ask key
    key = input()  # take key
    
    print("Enter value:")  # ask value
    value = input()  # take value
    
    d[key] = value  # store in dictionary

print("Sorted Dictionary by Values:")  # heading

sorted_items = sorted(d.items(), key=lambda x: x[1])  # sort by value

for k, v in sorted_items:  # print sorted result
    print(k, v)  # display output
    #OUTPUT
    """
    How many elements?
2
Enter key:
a
Enter value:
8
Enter key:
n
Enter value:
9
Sorted Dictionary by Values:
a 8
n 9
"""