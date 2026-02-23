# Program 1: Create a Tuple from User Input
# This program takes numbers from user and stores them in a tuple.

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

# Displaying results
print("\n----- Output -----")
print("Numbers Entered:", numbers)
print("Final Tuple:", t)
print("Total Elements in Tuple:", len(t))
#OUTPUT
"""Enter how many numbers you want in tuple: 4
Enter number 1: 2
Enter number 2: 3
Enter number 3: 5
Enter number 4: 12

----- Output -----
Numbers Entered: [2, 3, 5, 12]
Final Tuple: (2, 3, 5, 12)
Total Elements in Tuple: 4"""