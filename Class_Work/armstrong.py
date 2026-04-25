# Program: Check whether a number is Armstrong or not

# Step 1: Take input number
num = int(input("Enter a number: "))

# Step 2: Store original number for comparison
temp = num

# Step 3: Find number of digits
power = len(str(num))

# Step 4: Initialize sum
result = 0

# Step 5: Calculate sum of digits raised to power
while temp > 0:
    digit = temp % 10        # Extract last digit
    result += digit ** power # Add powered digit
    temp //= 10              # Remove last digit

# Step 6: Check if Armstrong
if result == num:
    print("True")
else:
    print("False")

# output
"""
Enter a number: 153
True"""