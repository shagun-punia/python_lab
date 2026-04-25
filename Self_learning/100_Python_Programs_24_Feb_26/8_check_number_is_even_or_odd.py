# Program to check whether a number is even or odd
# without using modulus (%) operator

# Taking input from user
num = int(input("Enter a number: "))

# Checking even or odd without using %
# If a number divided by 2 and multiplied back by 2
# gives the same number, then it is even
if (num // 2) * 2 == num:
    result = "The number is Even."
else:
    result = "The number is Odd."

# Displaying the result
print("\n----- Output -----")
print("Number Entered:", num)
print(result)

#OUTPUT
"""Enter a number: 45

----- Output -----
Number Entered: 45
The number is Odd."""