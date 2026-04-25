# Fibonacci series using for loop

n = int(input("Enter number of terms: "))  # input
a = 0  # first term
b = 1  # second term

print("\n----- Output -----")
for i in range(n):  # loop n times
    print(a, end=" ")  # print term
    next_term = a + b  # find next term
    a = b  # shift value
    b = next_term  # update value
    #OUTPUT
    """
    Enter number of terms: 4

----- Output -----
0 1 1 2
"""