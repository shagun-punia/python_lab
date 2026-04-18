import numpy as np

# Create array from 1 to 10
numbers = np.arange(1, 11)

# Replace even numbers with 0
numbers[numbers % 2 == 0] = 0

print(numbers)
