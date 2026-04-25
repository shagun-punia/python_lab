# Program: Swap keys and values in a dictionary

# Step 1: Create empty dictionary
data = {}

# Step 2: Take number of key-value pairs
n = int(input("Enter number of key-value pairs: "))

# Step 3: Take input for dictionary
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

# Step 4: Swap keys and values
swapped = {}
for key, value in data.items():
    swapped[value] = key

# Step 5: Display result
print("Swapped dictionary:", swapped)

#  Output:
"""
Enter number of key-value pairs: 2
Enter key: a
Enter value: 1
Enter key: b
Enter value: 2
Swapped dictionary: {'1': 'a', '2': 'b'}
"""