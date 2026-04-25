# Factorial using for loop

num = int(input("Enter a number: "))  # input
fact = 1  # store factorial

for i in range(1, num + 1):  # loop till num
    fact *= i  # multiply

print("\n----- Output -----")
print("Factorial is:", fact)  # display result
#OUTPUT
"""Enter a number: 6

----- Output -----
Factorial is: 720 """