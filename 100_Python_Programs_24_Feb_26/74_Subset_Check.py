# Check subset

n1 = int(input("Enter size of first set: "))  # size1
s1 = set(int(input("Enter element: ")) for i in range(n1))  # set1

n2 = int(input("Enter size of second set: "))  # size2
s2 = set(int(input("Enter element: ")) for i in range(n2))  # set2

print("\n----- Output -----")  # output
print("Is Subset:", s1.issubset(s2))  # check subset
#OUTPUT
"""
Enter size of first set: 3
Enter element: 34
Enter element: 67
Enter element: 4
Enter size of second set: 4
Enter element: 34
Enter element: 67
Enter element: 4
Enter element: 8

----- Output -----
Is Subset: True
"""