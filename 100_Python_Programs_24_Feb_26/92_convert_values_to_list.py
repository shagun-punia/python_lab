# Program to convert dictionary values into list

print("How many elements?")
n = int(input())

d = {}

for i in range(n):
    print("Enter key:")
    key = input()
    
    print("Enter value:")
    value = input()
    
    d[key] = value

values_list = []  # empty list

for v in d.values():  # loop through values
    values_list.append(v)  # add value to list

print("List of values is:")
print(values_list)
#OUTPUT
"""
How many elements?
3
Enter key:
a
Enter value:
78
Enter key:
b
Enter value:
34
Enter key:
c
Enter value:
56
List of values is:
['78', '34', '56']
"""