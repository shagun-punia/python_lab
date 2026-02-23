# Program 2: E-Commerce Cart System

prices = list(map(float, input("Enter product prices: ").split()))

# Remove duplicates
prices = list(set(prices))

total = sum(prices)

if total > 5000:
    total = total * 0.9   # 10% discount

total = total * 1.18      # 18% GST

print("Final Payable Amount:", total)