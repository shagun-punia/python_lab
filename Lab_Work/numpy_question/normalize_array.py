# Program: Normalize values of a NumPy array between 0 and 1

import numpy as np

# Step 1: Take array input
arr = np.array(list(map(float, input("Enter elements: ").split())))

# Step 2: Normalize using formula (x-min)/(max-min)
normalized = (arr - arr.min()) / (arr.max() - arr.min())

# Step 3: Display result
print("Normalized array:", normalized)

#  Output:
"""
Enter elements: 10 20 30 40
Normalized array: [0.   0.33 0.67 1.  ]
"""