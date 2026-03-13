import numpy as np

# Create array from 1 to 25
numbers = np.arange(1, 26)

# Reshape into 5x5 matrix
matrix = numbers.reshape(5, 5)

# Extract middle 3x3 sub-matrix
sub_matrix = matrix[1:4, 1:4]

print("Sub Matrix:")
print(sub_matrix)
