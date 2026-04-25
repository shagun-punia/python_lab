import numpy as np

# Create array from 1 to 15
numbers = np.arange(1, 16)

# Find numbers greater than 10
result = numbers[numbers > 10]

print("Numbers greater than 10:")
print(result)
#output
""""Numbers greater than 10:
[11 12 13 14 15]"""
