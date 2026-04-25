# Program to merge two dictionaries manually

# Taking size of first dictionary
n1 = int(input("Enter number of elements in first dictionary: "))

dict1 = {}

# Taking key-value pairs for first dictionary
for i in range(n1):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

# Taking size of second dictionary
n2 = int(input("Enter number of elements in second dictionary: "))

dict2 = {}

# Taking key-value pairs for second dictionary
for i in range(n2):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict2[key] = value

# Manually merging second dictionary into first
for key in dict2:
    dict1[key] = dict2[key]   # Update if key already exists

# Printing merged dictionary
print("Merged Dictionary is:")
print(dict1)
#OUTPUT
"""
Enter number of elements in first dictionary: 2
Enter key: 2
Enter value: 3
Enter key: 5
Enter value: 6
Enter number of elements in second dictionary: 1
Enter key: 3
Enter value: 4
Merged Dictionary is:
{'2': 3, '5': 6, '3': 4}
"""