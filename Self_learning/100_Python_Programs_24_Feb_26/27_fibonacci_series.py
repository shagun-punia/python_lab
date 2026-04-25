# Fibonacci series

n = int(input("Enter number of terms: "))  # input
a = 0  # first term
b = 1  # second term
count = 1  # counter

print("\n----- Output -----")
while count <= n:  # loop n times
    print(a, end=" ")  # print term
    next_term = a + b  # next value
    a = b  # shift value
    b = next_term  # update value
    count += 1  # increase count
    #OUTPUT
    """Enter number of terms: 5

----- Output -----
0 1 1 2 3  """