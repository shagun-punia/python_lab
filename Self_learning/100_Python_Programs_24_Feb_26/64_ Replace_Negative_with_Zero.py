# Replace negative numbers with zero

n = int(input("Enter size of list: "))  # list size
lst = [int(input("Enter element: ")) for i in range(n)]  # input list

for i in range(n):  # loop through list
    if lst[i] < 0:  # check negative
        lst[i] = 0  # replace with zero

print("\n----- Output -----")  # output section
print("Updated List:", lst)  # print result
#OUTPUT
"""
Enter size of list: 4
Enter element: -9
Enter element: 78
Enter element: 6
Enter element: 8

----- Output -----
Updated List: [0, 78, 6, 8]
"""
