import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

curved = 2 * math.pi * r * h
total = 2 * math.pi * r * (r + h)
volume = math.pi * r * r * h

print("Curved Surface Area =", curved)
print("Total Surface Area =", total)
print("Volume =", volume)