import numpy as np

# Generate 10 random numbers between 0 and 1
array = np.random.rand(10)

# Normalize array
normalized_array = (array - np.min(array)) / (np.max(array) - np.min(array))

print("Original Array:")
print(array)

print("Normalized Array:")
print(normalized_array)
#output
"""Original Array:
[0.3994908  0.88960619 0.02184487 0.47224703 0.48522733 0.59342552
 0.79285405 0.67408164 0.6516791  0.99034619]
Normalized Array:
[0.38992815 0.89598362 0.         0.46505064 0.4784531  0.59017023
 0.7960848  0.67344955 0.6503184  1.        ]

"""
