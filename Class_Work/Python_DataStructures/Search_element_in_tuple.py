# Program: Search Element in Tuple
# This program takes numbers from the user,
# creates a tuple, and searches for a given element.

# Taking number of elements
n = int(input("Enter how many numbers you want in tuple: "))

# Creating empty list
numbers = []

# Taking input from user
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Converting list into tuple
t = tuple(numbers)

# Taking element to search
element = int(input("Enter the number to search in tuple: "))

# Searching element
print("\n----- Output -----")
print("Tuple Created:", t)

if element in t:
    print("Search Result: Element Found in Tuple")
else:
    print("Search Result: Element Not Found in Tuple")


    #OUTPUT
    """Enter how many numbers you want in tuple: 4
Enter number 1: 2
Enter number 2: 8
Enter number 3: 98
Enter number 4: 6
Enter the number to search in tuple: 98

----- Output -----
Tuple Created: (2, 8, 98, 6)
Search Result: Element Found in Tuple"""