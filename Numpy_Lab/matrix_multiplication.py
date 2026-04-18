import numpy as np

# Create Matrix A
matrix_A = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Create Matrix B
matrix_B = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# Matrix Multiplication
result_matrix = np.matmul(matrix_A, matrix_B)

print("Result:")
print(result_matrix)
