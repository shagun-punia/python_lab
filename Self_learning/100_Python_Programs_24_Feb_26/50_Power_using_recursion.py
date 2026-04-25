# Calculate power using recursive function

def power(base, exp):  # recursive function
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input("Enter base: "))  # input
exp = int(input("Enter exponent: "))  # input

print("\n----- Output -----")
print("Result:", power(base, exp))
#OUTPUT
"""
Enter base: 5
Enter exponent: 6

----- Output -----
Result: 15625
"""