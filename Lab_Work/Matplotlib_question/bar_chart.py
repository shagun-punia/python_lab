# problem20_bar_chart.py
import matplotlib.pyplot as plt

# Input data
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [150, 200, 300, 250, 180]

# Create bar chart
plt.bar(products, sales, color='green')

# Add title and labels
plt.title("Sales of Products")
plt.xlabel("Products")
plt.ylabel("Sales Units")

# Show the plot
plt.show()  
