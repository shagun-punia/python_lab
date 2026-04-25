# problem23_combined_plot.py
import matplotlib.pyplot as plt

# Input data
x = [1, 2, 3, 4, 5]
dataset1 = [5, 7, 9, 6, 10]
dataset2 = [3, 4, 2, 5, 7]

# Plot both datasets
plt.plot(x, dataset1, marker='o', linestyle='-', label='Dataset 1')
plt.plot(x, dataset2, marker='s', linestyle='--', label='Dataset 2')

# Add title and labels
plt.title("Combined Plot of Two Datasets")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add legend
plt.legend()

# Show the plot
plt.show()

