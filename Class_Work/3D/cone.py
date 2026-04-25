import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

l = math.sqrt(r*r + h*h)

curved = math.pi * r * l
total = math.pi * r * (r + l)
volume = (1/3) * math.pi * r * r * h

print("Curved Surface Area =", curved)
print("Total Surface Area =", total)
print("Volume =", volume)
