import numpy as np

# Create 5x5 matrix with random integers between 1 and 100
random_matrix = np.random.randint(1, 101, size=(5, 5))

# Find minimum and maximum values
minimum_value = np.min(random_matrix)
maximum_value = np.max(random_matrix)

print("Matrix:")
print(random_matrix)

print("Min =", minimum_value)
print("Max =", maximum_value)
