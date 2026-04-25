# Sum of first N natural numbers

n = int(input("Enter value of N: "))  # input
total = 0  # store sum

for i in range(1, n + 1):  # loop till N
    total += i  # add number

print("\n----- Output -----")
print("Sum is:", total)  # display

#OUTPUT
"""Enter value of N: 3

----- Output -----
Sum is: 6
"""