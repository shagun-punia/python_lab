# Program 6: Inventory Management

stocks = list(map(int, input("Enter product stock quantities: ").split()))

print("\nOriginal Stock List:", stocks)

# Removing items with 0 stock
stocks = [s for s in stocks if s > 0]
print("After Removing 0 Stock Items:", stocks)

# Restocking items below 10
for i in range(len(stocks)):
    if stocks[i] < 10:
        stocks[i] += 50

print("\n----- Updated Inventory -----")
print("Final Stock List:", stocks)
print("Total Inventory Count:", sum(stocks))
#OUTPUT
"""Enter product stock quantities: 0 89 76

Original Stock List: [0, 89, 76]
After Removing 0 Stock Items: [89, 76]

----- Updated Inventory -----
Final Stock List: [89, 76]
Total Inventory Count: 165"""