import threedfigures

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Cylinder Volume =", threedfigures.cylinder_volume(r, h))
print("Cylinder Surface Area =", threedfigures.cylinder_surface_area(r, h))
