# Factorial using function

def factorial(num):  # define function
    fact = 1  # store factorial
    for i in range(1, num + 1):  # loop till num
        fact *= i  # multiply
    return fact  # return value

num = int(input("Enter a number: "))  # input

print("\n----- Output -----")
print("Factorial is:", factorial(num))  # print result
#OUTPUT
"""

Enter a number: 4

----- Output -----
Factorial is: 24 
"""