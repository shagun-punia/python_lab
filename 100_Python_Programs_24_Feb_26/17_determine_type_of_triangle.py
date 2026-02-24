# Program to determine type of triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b == c:
    result = "Equilateral Triangle"
elif a == b or b == c or a == c:
    result = "Isosceles Triangle"
else:
    result = "Scalene Triangle"

print("\n----- Output -----")
print("Sides:", a, b, c)
print("Triangle Type:", result)
#OUTPUT
"""Enter first side: 5
Enter second side: 7
Enter third side: 5

----- Output -----
Sides: 5.0 7.0 5.0
Triangle Type: Isosceles Triangle"""