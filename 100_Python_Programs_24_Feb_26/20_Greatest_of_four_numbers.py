# Program to find greatest of four numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d

print("\n----- Output -----")
print("Numbers Entered:", a, b, c, d)
print("Greatest Number is:", largest)

#OUTPUT
"""Enter first number: 34
Enter second number: 89
Enter third number: 76
Enter fourth number: 56

----- Output -----
Numbers Entered: 34.0 89.0 76.0 56.0
Greatest Number is: 89.0"""