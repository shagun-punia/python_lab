# Program: Create a Dictionary
# This program takes key-value pairs from the user
# and stores them in a dictionary.

# Taking number of key-value pairs
n = int(input("How many key-value pairs do you want? "))

# Creating empty dictionary
data = {}

# Taking input from user
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input("Enter value: ")
    data[key] = value

# Displaying results
print("\n----- Output -----")
print("Dictionary Created Successfully")
print("Total Entries:", len(data))
print("Dictionary Data:", data)

#OUTPUT
"""How many key-value pairs do you want? 4
Enter key 1: 1
Enter value: 4
Enter key 2: 6
Enter value: 2
Enter key 3: 4
Enter value: 2
Enter key 4: 3
Enter value: 7

----- Output -----
Dictionary Created Successfully
Total Entries: 4
Dictionary Data: {'1': '4', '6': '2', '4': '2', '3': '7'}"""