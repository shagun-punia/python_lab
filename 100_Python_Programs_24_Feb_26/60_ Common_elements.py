# Find common elements

n1 = int(input("How many elements in first list? "))
list1 = []

for i in range(n1):
    list1.append(int(input("Enter element: ")))

n2 = int(input("How many elements in second list? "))
list2 = []

for i in range(n2):
    list2.append(int(input("Enter element: ")))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("\n----- Output -----")
print("Common Elements:", common)
#OUTPUT
"""
How many elements in first list? 3
Enter element: 34
Enter element: 56
Enter element: 2
How many elements in second list? 3
Enter element: 2
Enter element: 34
Enter element: 7

----- Output -----
Common Elements: [34, 2]
"""