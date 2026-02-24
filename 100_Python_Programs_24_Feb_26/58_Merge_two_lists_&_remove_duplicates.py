# Merge two lists and remove duplicates

n1 = int(input("How many elements in first list? "))
list1 = []

for i in range(n1):
    list1.append(int(input("Enter element: ")))

n2 = int(input("How many elements in second list? "))
list2 = []

for i in range(n2):
    list2.append(int(input("Enter element: ")))

merged = list1 + list2
unique = list(set(merged))

print("\n----- Output -----")
print("Merged List:", merged)
print("After Removing Duplicates:", unique)
#OUTPUT
"""
How many elements in first list? 2
Enter element: 4
Enter element: 90
How many elements in second list? 5
Enter element: 7
Enter element: 0
Enter element: 67
Enter element: 4
Enter element: 7

----- Output -----
Merged List: [4, 90, 7, 0, 67, 4, 7]
After Removing Duplicates: [0, 67, 4, 7, 90]
"""