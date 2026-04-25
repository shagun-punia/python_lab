# problem22_histogram.py
import matplotlib.pyplot as plt
import random

# Generate random dataset
data = [random.randint(1, 50) for _ in range(100)]

# Create histogram
plt.hist(data, bins=10, color='orange', edgecolor='black')

# Add title and labels
plt.title("Histogram of Random Data")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

# Show the plot
plt.show()

