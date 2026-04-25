# Symmetric difference of sets

n1 = int(input("Enter size of first set: "))  # size1
s1 = set(int(input("Enter element: ")) for i in range(n1))  # set1

n2 = int(input("Enter size of second set: "))  # size2
s2 = set(int(input("Enter element: ")) for i in range(n2))  # set2

print("\n----- Output -----")  # output
print("Symmetric Difference:", s1 ^ s2)  # symmetric difference
#OUTPUT
"""
Enter size of first set: 3
Enter element: 45
Enter element: 78
Enter element: 8
Enter size of second set: 4
Enter element: 45
Enter element: 8
Enter element: 56
Enter element: 2

----- Output -----
Symmetric Difference: {2, 56, 78}
"""