# Sum of even numbers up to N and print them

n = int(input("Enter value of N: "))  # input
total = 0  # store sum
i = 1  # starting value

print("\n----- Output -----")
print("Even numbers are:")  # heading

while i <= n:  # loop till N
    if i % 2 == 0:  # check even
        print(i, end=" ")  # print even number
        total += i  # add to sum
    i += 1  # increase i

print("\nSum of even numbers:", total)  # print sum
#OUTPUT
"""Enter value of N: 6

----- Output -----
Even numbers are:
2 4 6
Sum of even numbers: 12"""