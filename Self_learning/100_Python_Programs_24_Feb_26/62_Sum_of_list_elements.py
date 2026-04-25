# Find sum of list elements

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

total = 0

for num in lst:
    total += num

print("\n----- Output -----")
print("Sum of elements:", total)
#OUTPUT
"""
How many elements? 3
Enter element: 78
Enter element: 89
Enter element: 5

----- Output -----
Sum of elements: 172
"""