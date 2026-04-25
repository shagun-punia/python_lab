# Program to print numbers from 1 to N using while loop

n = int(input("Enter a number: "))

print("\n----- Output -----")
print("Numbers from 1 to", n, ":")

i = 1
while i <= n:
    print(i, end=" ")
    i += 1
    #OUTPUT
    """Enter a number: 45

----- Output -----    
Numbers from 1 to 45 :
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45"""