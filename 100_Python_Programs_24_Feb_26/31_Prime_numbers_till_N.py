# Print prime numbers till N

n = int(input("Enter value of N: "))  # input

print("\n----- Output -----")
for num in range(2, n + 1):  # loop from 2 to N
    prime = True  # assume prime
    for i in range(2, num):  # check divisibility
        if num % i == 0:  # not prime
            prime = False
            break
    if prime:  # if prime
        print(num, end=" ")
        #OUTPUT
        """Enter value of N: 6

----- Output -----
2 3 5
"""