# problem19_line_plot.py
import matplotlib.pyplot as plt

# Input data (replaceable)
x = [1, 2, 3, 4, 5]
y = [10, 15, 8, 12, 20]

# Create a line plot
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add title and labels
plt.title("Line Plot of X vs Y")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()  

