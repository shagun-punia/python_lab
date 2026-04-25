# Program: Perform matrix multiplication of two matrices using NumPy

import numpy as np

# Step 1: Take first matrix input
# Example format: [[1,2],[3,4]]
A = np.array(eval(input("Enter first matrix: ")))

# Step 2: Take second matrix input
B = np.array(eval(input("Enter second matrix: ")))

# Step 3: Multiply matrices
result = np.dot(A, B)

# Step 4: Display result
print("Resultant matrix:\n", result)

#  Output:
"""
Enter first matrix: [[1,2],[3,4]]
Enter second matrix: [[5,6],[7,8]]
Resultant matrix:
 [[19 22]
 [43 50]]
"""