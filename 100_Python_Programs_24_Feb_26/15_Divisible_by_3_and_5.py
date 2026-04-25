# Program to check whether a number is divisible by both 3 and 5

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    result = "The number is divisible by both 3 and 5."
else:
    result = "The number is not divisible by both 3 and 5."

print("\n----- Output -----")
print("Number Entered:", num)
print(result)
#OUTPUT
"""Enter a number: 9

----- Output -----
Number Entered: 9 
The number is not divisible by both 3 and 5."""