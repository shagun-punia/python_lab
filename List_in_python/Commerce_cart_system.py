# Program 2: E-Commerce Cart System
# This program calculates final payable amount.

prices = list(map(float, input("Enter product prices separated by space: ").split()))

# Removing duplicate items
prices = list(set(prices))

# Calculating total amount
total = sum(prices)

print("\nTotal before discount:", total)

# Applying 10% discount if total > 5000
if total > 5000:
    total = total * 0.90
    print("10% Discount Applied")

# Adding 18% GST
total = total * 1.18

print("Final Payable Amount (with GST):", round(total, 2))
#OUTPUT
"""Enter product prices separated by space: 344 67 900 789 67

Total before discount: 2100.0
Final Payable Amount (with GST): 2478.0  """
