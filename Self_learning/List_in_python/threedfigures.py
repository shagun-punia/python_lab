import math

# Cube
def cube_volume(a):
    return a ** 3

def cube_surface_area(a):
    return 6 * a * a


# Cuboid
def cuboid_volume(l, b, h):
    return l * b * h

def cuboid_surface_area(l, b, h):
    return 2 * (l*b + b*h + l*h)


# Cylinder
def cylinder_volume(r, h):
    return math.pi * r * r * h

def cylinder_surface_area(r, h):
    return 2 * math.pi * r * (r + h)


# Cone
def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h

def cone_surface_area(r, h):
    l = math.sqrt(r*r + h*h)
    return math.pi * r * (r + l)


# Sphere
def sphere_volume(r):
    return (4/3) * math.pi * r ** 3

def sphere_surface_area(r):
    return 4 * math.pi * r * r


# Hemisphere
def hemisphere_volume(r):
    return (2/3) * math.pi * r ** 3

def hemisphere_surface_area(r):
    return 3 * math.pi * r * r
