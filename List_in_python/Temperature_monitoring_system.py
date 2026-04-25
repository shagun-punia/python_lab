# Program 8: Temperature Monitoring System

temps = list(map(int, input("Enter daily temperatures sperated by space: ").split()))

print("\nOriginal Temperature List:", temps)

print("Highest Temperature:", max(temps))
print("Lowest Temperature:", min(temps))

# Replacing temperature above 45 with Heat Alert
for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

# Counting extreme days (>40°C but not Heat Alert)
extreme_days = len([t for t in temps if t != "Heat Alert" and t > 40])

print("\n----- Updated Temperature Report -----")
print("Temperature List After Alert Check:", temps)
print("Extreme Days (>40°C):", extreme_days)
#OUTPUT
"""Enter daily temperatures sperated by space: 9 7 4

Original Temperature List: [9, 7, 4]
Highest Temperature: 9
Lowest Temperature: 4

----- Updated Temperature Report -----
Temperature List After Alert Check: [9, 7, 4]
Extreme Days (>40°C): 0"""
