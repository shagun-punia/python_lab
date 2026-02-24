# Program to reverse a given number

# Taking input from user
num = int(input("Enter a number: "))

# Storing original number for display
original_num = num

# Making number positive (to handle negative input)
num = abs(num)

# Initializing reverse variable
reverse = 0

# Reversing the number
while num > 0:
    digit = num % 10          # Extract last digit
    reverse = reverse * 10 + digit
    num = num // 10           # Remove last digit

# If original number was negative, make reverse negative
if original_num < 0:
    reverse = -reverse

# Displaying the result
print("\n----- Output -----")
print("Number Entered:", original_num)
print("Reversed Number:", reverse)
#OUTPUT
"""Enter a number: 23

----- Output -----
Number Entered: 23
Reversed Number: 32"""