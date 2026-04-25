# Program: Find mean, median, and standard deviation using NumPy

import numpy as np  # Import NumPy library

# Step 1: Take array input
arr = np.array(list(map(int, input("Enter elements: ").split())))

# Step 2: Calculate mean, median, and std deviation
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)

# Step 3: Display results
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

#  Output:
"""
Enter elements: 1 2 3 4 5
Mean: 3.0
Median: 3.0
Standard Deviation: 1.4142135623730951
"""