# Program: Extract diagonal elements from a 2D matrix

import numpy as np

# Step 1: Take 2D matrix input
matrix = np.array(eval(input("Enter 2D matrix: ")))

# Step 2: Extract diagonal elements
diag = np.diagonal(matrix)

# Step 3: Display result
print("Diagonal elements:", diag)

#  Output:
"""
Enter 2D matrix: [[1,2,3],[4,5,6],[7,8,9]]
Diagonal elements: [1 5 9]
"""