# Find smallest element

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

smallest = lst[0]

for num in lst:
    if num < smallest:
        smallest = num

print("\n----- Output -----")
print("List:", lst)
print("Smallest Element:", smallest)
#OUTPUT
"""
How many elements? 4
Enter element: 6
Enter element: 4
Enter element: 23
Enter element: 5

----- Output -----
List: [6, 4, 23, 5]
Smallest Element: 4
"""