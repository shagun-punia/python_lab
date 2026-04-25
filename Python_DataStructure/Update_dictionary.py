# Program: Update Dictionary
# This program takes key-value pairs from the user,
# stores them in a dictionary, and updates a given key.

# Taking number of key-value pairs
n = int(input("How many key-value pairs do you want? "))

# Creating empty dictionary
data = {}

# Taking input from user
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input("Enter value: ")
    data[key] = value

# Display original dictionary
print("\n----- Original Dictionary -----")
print(data)

# Taking key to update
update_key = input("Enter the key you want to update: ")

# Updating value if key exists
if update_key in data:
    new_value = input("Enter new value: ")
    data[update_key] = new_value

    print("\n----- Output -----")
    print("Dictionary Updated Successfully")
    print("Updated Dictionary:", data)
else:
    print("\n----- Output -----")
    print("Key Not Found. Cannot Update.")

    #OUTPUT
    """How many key-value pairs do you want? 2
Enter key 1: name
Enter value: govind
Enter key 2: age
Enter value: 97

----- Original Dictionary -----
{'name': 'govind', 'age': '97'}
Enter the key you want to update: age
Enter new value: 55

----- Output -----
Dictionary Updated Successfully
Updated Dictionary: {'name': 'govind', 'age': '55'}"""