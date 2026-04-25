# Fibonacci using function

def fibonacci(n):  # define function
    a = 0  # first term
    b = 1  # second term
    for i in range(n):  # loop n times
        print(a, end=" ")  # print term
        next_term = a + b  # next value
        a = b  # shift
        b = next_term  # update

n = int(input("Enter number of terms: "))  # input

print("\n----- Output -----")
fibonacci(n)  # call 
#OUTPUT
"""
Enter number of terms: 5

----- Output -----
0 1 1 2 3
"""