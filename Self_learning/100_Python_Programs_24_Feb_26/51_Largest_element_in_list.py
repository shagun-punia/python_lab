# Find largest element

n = int(input("How many elements? "))  # size
lst = []

for i in range(n):  # input list
    lst.append(int(input("Enter element: ")))

largest = lst[0]

for num in lst:  # check each element
    if num > largest:
        largest = num

print("\n----- Output -----")
print("List:", lst)
print("Largest Element:", largest)
#OUTPUT
"""
How many elements? 5
Enter element: 7
Enter element: 4
Enter element: 3
Enter element: 5
Enter element: 2

----- Output -----
List: [7, 4, 3, 5, 2]
Largest Element: 7
"""