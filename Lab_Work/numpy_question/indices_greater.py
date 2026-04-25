# Program: Find indices of elements greater than a given value

import numpy as np

# Step 1: Take array input
arr = np.array(list(map(int, input("Enter elements: ").split())))

# Step 2: Take value for comparison
value = int(input("Enter value: "))

# Step 3: Find indices
indices = np.where(arr > value)[0]

# Step 4: Display result
print("Indices of elements greater than", value, ":", indices)

#  Output:
"""
Enter elements: 1 5 3 7 2
Enter value: 3
Indices of elements greater than 3 : [1 3]
"""