# Reverse list manually

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

reversed_list = []

for i in range(len(lst)-1, -1, -1):
    reversed_list.append(lst[i])

print("\n----- Output -----")
print("Reversed List:", reversed_list)
#OUTPUT
"""
How many elements? 4
Enter element: 78
Enter element: 6
Enter element: 9
Enter element: 0

----- Output -----
Reversed List: [0, 9, 6, 78]
"""