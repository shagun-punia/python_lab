# Calculate power without using **

base = int(input("Enter base: "))  # input base
exp = int(input("Enter exponent: "))  # input exponent
result = 1  # store result

for i in range(exp):  # loop exp times
    result *= base  # multiply base

print("\n----- Output -----")
print("Power is:", result)  # display result
#OUTPUT
"""
Enter base: 4
Enter exponent: 6

----- Output -----
Power is: 4096
"""