# Count frequency of elements

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

frequency = {}

for item in lst:
    frequency[item] = frequency.get(item, 0) + 1

print("\n----- Output -----")
print("Frequency:", frequency)
#OUTPUT
"""
How many elements? 3
Enter element: 67
Enter element: 54
Enter element: 45

----- Output -----
Frequency: {67: 1, 54: 1, 45: 1}
"""