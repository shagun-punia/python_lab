#  Inventory Management

stock = list(map(int, input("Enter stock quantities: ").split()))

stock = [s for s in stock if s != 0]

for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

print("Updated Stock:", stock)
print("Total Inventory:", sum(stock))