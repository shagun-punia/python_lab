# Program to find the largest of three numbers

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Displaying the result
print("\n----- Output -----")
print("Numbers Entered:", num1, num2, num3)
print("Largest Number is:", largest)

#OUTPUT
"""Enter first number: 4
Enter second number: 2
Enter third number: 7

----- Output -----
Numbers Entered: 4.0 2.0 7.0
Largest Number is: 7.0"""