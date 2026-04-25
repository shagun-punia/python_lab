# problem25_styled_plot.py
import matplotlib.pyplot as plt

# Input data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [5000, 7000, 8000, 6000, 7500, 9000]

# Create line plot
plt.plot(months, revenue, marker='o', color='purple', linestyle='-')

# Add title, labels, and grid
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.grid(True)

# Show the plot
plt.show()
