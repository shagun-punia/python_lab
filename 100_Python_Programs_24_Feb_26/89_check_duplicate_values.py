# Program to check duplicate values in dictionary

print("How many elements?")
n = int(input())

d = {}

for i in range(n):
    print("Enter key:")
    key = input()
    
    print("Enter value:")
    value = input()
    
    d[key] = value

duplicate_found = False

for v in d.values():  # check each value
    if list(d.values()).count(v) > 1:
        duplicate_found = True
        break

if duplicate_found:
    print("Duplicate values are present")
else:
    print("No duplicate values")
    #output
    """
    How many elements?
3
Enter key:
a
Enter value:
10
Enter key:
b
Enter value:
7
Enter key:
c
Enter value:
10
Duplicate values are present
"""