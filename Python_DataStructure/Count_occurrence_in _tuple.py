# Program: Count Occurrence in a Tuple
# This program takes numbers from the user,
# creates a tuple, and counts how many times
# a specific number appears in the tuple.

# Taking number of elements
n = int(input("Enter how many numbers you want in tuple: "))

# Creating empty list to store numbers
numbers = []

# Taking input from user
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Converting list into tuple
t = tuple(numbers)

# Taking number to count
element = int(input("Enter the number to count its occurrence: "))

# Counting occurrence
count = t.count(element)

# Displaying results
print("\n----- Output -----")
print("Tuple Created:", t)
print("Number to Count:", element)
print("Total Occurrence:", count)

#OUTPUT
"""Enter how many numbers you want in tuple: 3
Enter number 1: 4
Enter number 2: 5
Enter number 3: 4
Enter the number to count its occurrence: 4

----- Output -----
Tuple Created: (4, 5, 4)
Number to Count: 4
Total Occurrence: 2"""