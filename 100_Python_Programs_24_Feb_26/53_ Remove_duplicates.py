# Remove duplicate elements

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("\n----- Output -----")
print("List without duplicates:", unique)
#OUTPUT
"""
How many elements? 3
Enter element: 6
Enter element: 54
Enter element: 5

----- Output -----
List without duplicates: [6, 54, 5]
"""