# Program to convert dictionary keys into list

print("How many elements?")
n = int(input())

d = {}

for i in range(n):
    print("Enter key:")
    key = input()
    
    print("Enter value:")
    value = input()
    
    d[key] = value

keys_list = []  # empty list

for k in d:  # loop through dictionary
    keys_list.append(k)  # add key to list

print("List of keys is:")
print(keys_list)
#OUTPUT
"""
How many elements?
2
Enter key:
a
Enter value:
67
Enter key:
b
Enter value:
34
List of keys is:
['a', 'b']
"""