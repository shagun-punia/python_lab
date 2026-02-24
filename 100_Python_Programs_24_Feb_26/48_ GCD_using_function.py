# Find GCD using function

def find_gcd(a, b):  # define function
    while b != 0:  # loop till 0
        a, b = b, a % b  # update values
    return a  # return gcd

a = int(input("Enter first number: "))  # input
b = int(input("Enter second number: "))  # input

print("\n----- Output -----")
print("GCD is:", find_gcd(a, b))  # print result
#OUTPUT
"""
Enter first number: 4
Enter second number: 2

----- Output -----
GCD is: 2
"""