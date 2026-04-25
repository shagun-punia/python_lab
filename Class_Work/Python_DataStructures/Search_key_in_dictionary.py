# Program: Search Key in Dictionary
# This program takes key-value pairs from the user,
# stores them in a dictionary, and searches for a given key.

# Taking number of key-value pairs
n = int(input("How many key-value pairs do you want? "))

# Creating empty dictionary
data = {}

# Taking input from user
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input("Enter value: ")
    data[key] = value

# Taking key to search
search_key = input("Enter the key you want to search: ")

# Displaying results
print("\n----- Output -----")
print("Dictionary Created:", data)

if search_key in data:
    print("Search Result: Key Found")
    print("Value of the Key:", data[search_key])
else:
    print("Search Result: Key Not Found")

    #OUTPUT
    """How many key-value pairs do you want? 3
Enter key 1: 2
Enter value: 8
Enter key 2: 5
Enter value: 7
Enter key 3: 3
Enter value: 2
Enter the key you want to search: 2

----- Output -----
Dictionary Created: {'2': '8', '5': '7', '3': '2'}
Search Result: Key Found
Value of the Key: 8"""