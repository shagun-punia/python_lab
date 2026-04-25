# Find maximum in tuple

n = int(input("Enter size: "))  # size
t = tuple(int(input("Enter element: ")) for i in range(n))  # tuple input

print("\n----- Output -----")  # output section
print("Maximum Value:", max(t))  # print max
#OUTPUT
"""
Enter size: 3
Enter element: 56
Enter element: 89
Enter element: 53

----- Output -----
Maximum Value: 89
"""