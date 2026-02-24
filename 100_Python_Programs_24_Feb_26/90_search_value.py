# Program to search a value in dictionary

print("How many elements?")
n = int(input())

d = {}

for i in range(n):
    print("Enter key:")
    key = input()
    
    print("Enter value:")
    value = input()
    
    d[key] = value

print("Enter value to search:")
search_value = input()

found = False

for k in d:
    if d[k] == search_value:
        print("Value found at key:", k)
        found = True

if found == False:
    print("Value not found in dictionary")
    #OUTPUT
    """
    How many elements?
2
Enter key:
a
Enter value:
56
Enter key:
b
Enter value:
Enter value to search:
a
Value not found in dictionary
PS C:\Users\DELL\Desktop\List in Python> & C:/Users/DELL/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/DELL/Desktop/List in Python/100_Python_Programs_24_Feb_26/90_search_value.py"
How many elements?
3
Enter key:
a
Enter value:
45
Enter key:
b
Enter value:
78
Enter key:
c
Enter value:
23
Enter value to search:
23
Value found at key: c
"""