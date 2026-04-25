l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

curved = 2 * h * (l + b)
total = 2 * (l*b + b*h + l*h)
volume = l * b * h

print("Curved Surface Area =", curved)
print("Total Surface Area =", total)
print("Volume =", volume)
