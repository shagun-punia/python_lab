# Program: Replace all odd numbers in an array with -1

import numpy as np

# Step 1: Take array input
arr = np.array(list(map(int, input("Enter elements: ").split())))

# Step 2: Replace odd numbers
arr[arr % 2 == 1] = -1

# Step 3: Display result
print("Modified array:", arr)

#  Output:
"""
Enter elements: 1 2 3 4 5
Modified array: [-1  2 -1  4 -1]
"""