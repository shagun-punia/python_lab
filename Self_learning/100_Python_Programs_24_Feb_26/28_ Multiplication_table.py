# Multiplication table

num = int(input("Enter a number: "))  # input
i = 1  # start from 1

print("\n----- Output -----")
while i <= 10:  # loop till 10
    print(num, "x", i, "=", num * i)  # print table
    i += 1  # increase i

    #OUTPUT
    """Enter a number: 5

----- Output -----
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50"""