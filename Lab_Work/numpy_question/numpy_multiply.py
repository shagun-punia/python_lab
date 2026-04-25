# Program: Perform element-wise multiplication of two arrays

import numpy as np  # Import NumPy library

# Step 1: Take first array input
arr1 = np.array(list(map(int, input("Enter first array: ").split())))

# Step 2: Take second array input
arr2 = np.array(list(map(int, input("Enter second array: ").split())))

# Step 3: Perform element-wise multiplication
result = arr1 * arr2

# Step 4: Display result
print("Resultant array:", result)

#  Output:
"""
Enter first array: 1 2 3
Enter second array: 4 5 6
Resultant array: [4 10 18]
"""