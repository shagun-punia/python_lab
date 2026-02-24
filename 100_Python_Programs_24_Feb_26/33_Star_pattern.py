# Print star pattern

n = int(input("Enter number of rows: "))  # input

print("\n----- Output -----")
for i in range(1, n + 1):  # loop rows
    print("*" * i)  # print stars

    #OUTPUT
    """Enter number of rows: 5

----- Output -----
*
**
***
****
*****
"""