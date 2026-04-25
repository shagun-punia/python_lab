# Program: Transpose a 2D matrix using NumPy

import numpy as np

# Step 1: Take 2D matrix input
# Example input format: [[1,2,3],[4,5,6]]
matrix = np.array(eval(input("Enter 2D matrix: ")))

# Step 2: Transpose the matrix
transpose = matrix.T

# Step 3: Display result
print("Transposed matrix:\n", transpose)

#  Output:
"""
Enter 2D matrix: [[1,2,3],[4,5,6]]
Transposed matrix:
 [[1 4]
 [2 5]
 [3 6]]
"""