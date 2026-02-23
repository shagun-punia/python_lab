#  Temperature Monitoring System

temps = list(map(int, input("Enter temperatures: ").split()))

if len(temps) == 0:
    print("No temperature data.")
else:
    print("Hottest Day:", max(temps))
    print("Coldest Day:", min(temps))

    extreme_days = len([t for t in temps if t > 40])

    updated = []
    for t in temps:
        if t > 45:
            updated.append("Heat Alert")
        else:
            updated.append(t)

    print("Updated Temperature List:", updated)
    print("Extreme Days (>40):", extreme_days)