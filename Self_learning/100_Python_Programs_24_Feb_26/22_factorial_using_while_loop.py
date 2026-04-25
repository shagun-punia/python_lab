# Program to find factorial using while loop

num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print("\n----- Output -----")
print("Factorial of", num, "is:", fact)

#OUTPUT
"""Enter a number: 6

----- Output -----    
Factorial of 6 is: 720"""