# Program 4: Salary Processing System
# This program processes employee salaries.

# Taking input
salaries = list(map(int, input("Enter employee salaries separated by space: ").split()))
min_wage = int(input("Enter minimum wage: "))

print("\n----- Original Salaries -----")
print(salaries)

# Removing salaries below minimum wage
valid_salaries = [s for s in salaries if s >= min_wage]

print("\nAfter Removing Salaries Below Minimum Wage:")
print(valid_salaries)

updated = []

# Adding 5% bonus to salaries above 50000
for s in valid_salaries:
    if s > 50000:
        bonus = s * 0.05
        s = s + bonus
    updated.append(s)

# Sorting in descending order
updated.sort(reverse=True)

print("\n----- Final Processed Salaries -----")
print(updated)

# Displaying top 3 salaries
if len(updated) >= 3:
    print("Top 3 Highest Salaries:", updated[:3])
else:
    print("Available Salaries:", updated)
    #OUTPUT
    """Enter employee salaries separated by space: 5600 7800 45000
Enter minimum wage: 56

----- Original Salaries -----
[5600, 7800, 45000]

After Removing Salaries Below Minimum Wage:
[5600, 7800, 45000]

----- Final Processed Salaries -----
[45000, 7800, 5600]
Top 3 Highest Salaries: [45000, 7800, 5600]"""