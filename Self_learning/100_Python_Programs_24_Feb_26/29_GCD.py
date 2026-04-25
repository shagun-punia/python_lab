# Find GCD

a = int(input("Enter first number: "))  # input
b = int(input("Enter second number: "))  # input

while b != 0:  # loop till b becomes 0
    a, b = b, a % b  # update values

print("\n----- Output -----")
print("GCD is:", a)  # print gcd
#OUTPUT
"""Enter first number: 4
Enter second number: 7

----- Output -----
GCD is: 1"""