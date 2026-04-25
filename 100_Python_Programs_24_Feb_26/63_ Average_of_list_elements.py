# Find average of list elements

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

total = 0

for num in lst:
    total += num

average = total / n

print("\n----- Output -----")
print("Average:", average)
#OUTPUT
"""
How many elements? 3
Enter element: 78
Enter element: 98
Enter element: 4

----- Output -----
Average: 60.0
"""