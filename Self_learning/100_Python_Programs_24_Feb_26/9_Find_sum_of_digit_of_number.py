# Program to find the sum of digits of a number

# Taking input from user
num = int(input("Enter a number: "))

# Storing original number for display
original_num = num

# Making number positive (in case user enters negative number)
num = abs(num)

# Initializing sum variable
digit_sum = 0

# Calculating sum of digits
while num > 0:
    digit = num % 10       # Extract last digit
    digit_sum += digit     # Add digit to sum
    num = num // 10        # Remove last digit

# Displaying the result
print("\n----- Output -----")
print("Number Entered:", original_num)
print("Sum of Digits:", digit_sum)

#OUTPUT
"""Enter a number: 67

----- Output -----
Number Entered: 67
Sum of Digits: 13"""