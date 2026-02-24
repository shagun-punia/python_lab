# Program to swap two numbers without using a third variable

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Displaying numbers before swapping
print("\nBefore Swapping:")
print("First Number =", num1)
print("Second Number =", num2)

# Swapping without using third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Displaying numbers after swapping
print("\nAfter Swapping:")
print("First Number =", num1)
print("Second Number =", num2)

#OUTPUT
"""Enter first number: 4
Enter second number: 3

Before Swapping:
First Number = 4
Second Number = 3

After Swapping:
First Number = 3
Second Number = 4"""