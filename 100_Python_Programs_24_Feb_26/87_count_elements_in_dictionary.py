# Program to count number of elements in dictionary

print("How many elements?")
n = int(input())

d = {}

for i in range(n):
    print("Enter key:")
    key = input()
    
    print("Enter value:")
    value = input()
    
    d[key] = value

count = len(d)  # count elements

print("Total number of elements in dictionary is:", count)
#OUTPUT
"""
How many elements?
2
Enter key:
a
Enter value:
45
Enter key:
b
Enter value:
34
Total number of elements in dictionary is: 2
"""