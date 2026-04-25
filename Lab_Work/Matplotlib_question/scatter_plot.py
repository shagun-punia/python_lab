# problem24_scatter_plot.py
import matplotlib.pyplot as plt

# Input data
x = [1, 2, 3, 4, 5]
y = [10, 15, 8, 20, 12]

# Find index of maximum point
max_index = y.index(max(y))

# Create scatter plot
plt.scatter(x, y, color='blue')
plt.scatter(x[max_index], y[max_index], color='red', s=100, label='Max Point')

# Add title and labels
plt.title("Scatter Plot Highlighting Maximum Point")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Show the plot
plt.show()

