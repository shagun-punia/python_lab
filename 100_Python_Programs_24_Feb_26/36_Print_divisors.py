# Print divisors of a number

num = int(input("Enter a number: "))  # input

print("\n----- Output -----")
for i in range(1, num + 1):  # loop till num
    if num % i == 0:  # check divisor
        print(i, end=" ")  # print divisor

        #OUTPUT
        """
        Enter a number: 4

----- Output -----
1 2 4 
"""