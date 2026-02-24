# Program to check whether a number is positive, negative, or zero

# Taking input from user
num = float(input("Enter a number: "))

# Checking the condition
if num > 0:
    result = "The number is Positive."
elif num < 0:
    result = "The number is Negative."
else:
    result = "The number is Zero."

# Displaying the result
print("\n----- Output -----")
print("Number Entered:", num)
print(result)

#OUTPUT
"""Enter a number: 5

----- Output -----
Number Entered: 5.0
The number is Positive."""