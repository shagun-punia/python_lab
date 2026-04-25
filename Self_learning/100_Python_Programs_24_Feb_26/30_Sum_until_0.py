# Sum until 0 entered

total = 0  # store sum

while True:  # infinite loop
    num = int(input("Enter number (0 to stop): "))  # input
    if num == 0:  # stop condition
        break
    total += num  # add number

print("\n----- Output -----")
print("Sum is:", total)  # display sum

#OUTPUT
"""Enter number (0 to stop): 4
Enter number (0 to stop): 7
Enter number (0 to stop): 8
Enter number (0 to stop): 0

----- Output -----
Sum is: 19"""