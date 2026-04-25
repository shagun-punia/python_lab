# Convert tuple to list

n = int(input("Enter size: "))  # size
t = tuple(int(input("Enter element: ")) for i in range(n))  # tuple input

lst = list(t)  # convert to list

print("\n----- Output -----")  # output section
print("List:", lst)  # print result
#OUTPUT
"""
Enter size: 4
Enter element: 45
Enter element: 8
Enter element: 0
Enter element: 45

----- Output -----
List: [45, 8, 0, 45]
"""