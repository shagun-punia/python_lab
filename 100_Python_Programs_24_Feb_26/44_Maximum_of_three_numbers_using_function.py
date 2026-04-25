# Find maximum of three numbers

def find_max(a, b, c):  # define function
    if a >= b and a >= c:  # check a
        return a
    elif b >= a and b >= c:  # check b
        return b
    else:
        return c  # else c

a = int(input("Enter first number: "))  # input
b = int(input("Enter second number: "))  # input
c = int(input("Enter third number: "))  # input

print("\n----- Output -----")
print("Maximum number is:", find_max(a, b, c))  # print result

#OUTPUT
"""
Enter first number: 4
Enter second number: 6
Enter third number: 23

----- Output -----
Maximum number is: 23
"""