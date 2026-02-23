#  Salary Processing System

salaries = list(map(float, input("Enter salaries: ").split()))

# Remove salaries below minimum wage (10000)
salaries = [s for s in salaries if s >= 10000]

for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] = salaries[i] * 1.05   # 5% bonus

salaries.sort(reverse=True)

print("Processed Salaries:", salaries)

if len(salaries) >= 3:
    print("Top 3 Salaries:", salaries[:3])
else:
    print("Less than 3 employees.")