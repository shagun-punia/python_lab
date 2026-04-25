# problem21_pie_chart.py
import matplotlib.pyplot as plt

# Input data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [40, 25, 20, 15]

# Create pie chart
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)

# Add title
plt.title("Percentage Distribution of Categories")

# Equal aspect ratio ensures the pie is circular
plt.axis('equal')

# Show the plot
plt.show()

# 